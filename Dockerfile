FROM ubuntu:16.04
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>

ENV REFRESHED_AT="2016.06.12-22:39:57"

# allowed options are firefox, chrome.
ENV TEST_BROWSER=firefox

ENV PYTHON_VERSION=3.5.2

ENV RUN_VNC_SERVER=1
ENV VNC_SERVER_WIDTH=1024
ENV VNC_SERVER_HEIGHT=768
ENV VNC_SERVER_BPP=16
ENV RUN_WEB_INTERFACE=0
ENV RUN_ICEWM=1
ENV VNC_PASSWORD=germanium

ENV DISPLAY=:1

ENV UID=1000
ENV GID=1000

EXPOSE 8081
EXPOSE 5901

# system update
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common

#
# Actual python installation required programs, and general dependencies.
#
RUN apt-get install -y \
    wget \
    libssl-dev \
    openssl \
    build-essential \
    unzip \
    bzip2

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
RUN $PYTHON_BINARY -m ensurepip && \
    $PYTHON_BINARY -m pip install virtualenv && \
    virtualenv /python && \
    /python/bin/pip install behave

#
# Install remoting apps
#
RUN apt-get install -y vnc4server \
    novnc \
    websockify \
    psmisc \
    icewm

# Setup remoting
RUN useradd -m germanium

RUN cp -R /usr/share/novnc /home/germanium/novnc && \
    mkdir -p /home/germanium/.icewm && \
    echo 'Theme="metal2/default.theme"' > /home/germanium/.icewm/theme && \
    mkdir -p /home/germanium/.vnc

COPY bin/docker/index.html /home/germanium/novnc/
COPY bin/docker/xstartup /home/germanium/.vnc/xstartup

#
# BROWSERS SECTION
#
ENV BROWSERS_REFRESHED_AT="2016.07.28-23:55:25"

#
# Install firefox, and its webdriver
#
RUN cd /opt && \
    wget 'https://download.mozilla.org/?product=firefox-47.0.1-SSL&os=linux64&lang=en-US' -O firefox.tar.bz2 && \
    tar -jxvf firefox.tar.bz2 && \
    rm /opt/firefox.tar.bz2

ENV PATH /opt/firefox:$PATH

#
# install chrome, and its webdriver
#
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable

#
# Behave run script
#
COPY bin/docker/run-behave.sh /home/germanium/bin/run-behave.sh

# add germanium the project only after having the docker binaries in the
# home folder, to reduce the time to create new docker images
COPY . /germanium
RUN cd /germanium && \
    /python/bin/python setup.py install && \
    rm -fr /germanium

RUN perl -pi -e "s/germanium:x:1000:1000/germanium:x:$UID:$GID/" /etc/passwd && \
    perl -pi -e "s/germanium:x:1000:/germanium:x:$GID:/" /etc/group && \
    chown -R germanium:germanium /home/germanium/ /python

USER germanium

CMD /home/germanium/bin/run-behave.sh

