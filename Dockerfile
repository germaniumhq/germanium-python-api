FROM ubuntu:14.04
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>

# system update
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common


ENV PYTHON_VERSION=3.5.1

# programs that we need for tests, and building python.
RUN apt-get install -y wget libssl-dev openssl build-essential firefox vnc4server

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

#RUN pip install --upgrade pip
RUN pip install behave

