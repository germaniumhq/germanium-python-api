#!/usr/bin/env bash

set -e

GERMANIUM_FOLDER=$(readlink -f $(dirname $0)/..)
TAG_VERSION=$($GERMANIUM_FOLDER/bin/version/python-version.sh --tag)

cd $GERMANIUM_FOLDER

docker build \
    -t germanium/germanium-$TAG_VERSION \
    --build-arg pypi_url=$PIPY_URL \
    --build-arg pypi_index_url=$PYPI_INDEX_URL \
    .

cd $GERMANIUM_FOLDER/features

docker build -t germanium/germanium-${TAG_VERSION}-tests .
