#!/usr/bin/env bash

GERMANIUM_FOLDER=$(readlink -f $(dirname $0)/../..)

cat $GERMANIUM_FOLDER/Dockerfile  | grep "ENV PYTHON_VERSION" | cut -f2 -d=

