#!/usr/bin/env bash

PYTHON_VERSIONS="python2.7 python3.4 python3.5"

set -e

GERMANIUM_FOLDER=$(readlink -f $(dirname $0)/..)

for PYTHON_VERSION in $PYTHON_VERSIONS; do
    git checkout $PYTHON_VERSION
    git rebase -ff master
    docker build -t germanium/germanium-$PYTHON_VERSION -t germanium/germanium .
    docker run --rm -it -v $GERMANIUM_FOLDER/features:/tests/features:ro germanium/germanium-$PYTHON_VERSION
done

