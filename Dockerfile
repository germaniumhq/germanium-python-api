FROM ubuntu:14.04
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>

ENV REFRESHED_AT="2016.03.14-23:39:29"

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
    websockify


ENV PYTHON_VERSION=3.5.1

ENV RUN_VNC_SERVER=1
ENV RUN_WEB_INTERFACE=1
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

RUN ln /usr/local/bin/pip3.5 /usr/local/bin/pip && \
    ln /usr/local/bin/python3.5 /usr/local/bin/python

# Install behave and germanium into the package.
#RUN pip install --upgrade pip
RUN pip install behave

RUN useradd -m germanium
ADD . /germanium
RUN cd /germanium && python setup.py install


RUN cp -R /usr/share/novnc /home/germanium/novnc
ADD bin/docker/index.html /home/germanium/novnc/
ADD bin/docker/xstartup /home/germanium/.vnc/xstartup
ADD bin/docker/run-behave.sh /home/germanium/bin/run-behave.sh

RUN chown -R germanium:germanium /home/germanium/

CMD perl -pi -e "s/germanium:x:1000:1000/germanium:x:$UID:$GID/" /etc/passwd && \
    perl -pi -e "s/germanium:x:1000:/germanium:x:$GID:/" /etc/group

USER germanium

CMD /home/germanium/bin/run-behave.sh

