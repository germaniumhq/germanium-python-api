FROM ubuntu:14.04
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>

ENV REFRESHED_AT="2016.03.29-21:10:18"

# system update
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common

# programs that we need for tests, and building python.
RUN apt-get install -y \
    wget \
    libssl-dev \
    openssl \
    build-essential \
    firefox \
    vnc4server \
    novnc \
    websockify \
    unzip

# install chrome, and its webdriver
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable

RUN wget https://chromedriver.storage.googleapis.com/2.21/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin && \
    rm chromedriver_linux64.zip

# allowed options are firefox, chrome.
ENV TEST_BROWSER=firefox

ENV PYTHON_VERSION=3.5.1

ENV RUN_VNC_SERVER=1
ENV RUN_WEB_INTERFACE=0
ENV VNC_PASSWORD=germanium

ENV DISPLAY=:1

ENV UID=1000
ENV GID=1000

EXPOSE 8081
EXPOSE 5901

#
# Actual python installation.
#
RUN mkdir /build && \
    cd /build && \
    wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-${PYTHON_VERSION}.tgz && \
    tar -zxvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure && \
    make && \
    make install && \
    rm -fr /build

ENV PYTHON_BINARY=/usr/local/bin/python3.5

# Install behave and germanium into the package.
#RUN pip install --upgrade pip
RUN $PYTHON_BINARY -m ensurepip && \
    $PYTHON_BINARY -m pip install virtualenv && \
    virtualenv /python && \
    /python/bin/pip install behave

RUN useradd -m germanium

RUN cp -R /usr/share/novnc /home/germanium/novnc
ADD bin/docker/index.html /home/germanium/novnc/
ADD bin/docker/xstartup /home/germanium/.vnc/xstartup
ADD bin/docker/run-behave.sh /home/germanium/bin/run-behave.sh

# add germanium the project only after having the docker binaries in the
# home folder, to reduce the time to create new docker iamges
ADD . /germanium
RUN cd /germanium && \
    /python/bin/python setup.py install && \
    rm -fr /germanium

RUN perl -pi -e "s/germanium:x:1000:1000/germanium:x:$UID:$GID/" /etc/passwd && \
    perl -pi -e "s/germanium:x:1000:/germanium:x:$GID:/" /etc/group && \
    chown -R germanium:germanium /home/germanium/ /python

RUN chmod +x /usr/local/bin/chromedriver

USER germanium

CMD /home/germanium/bin/run-behave.sh
