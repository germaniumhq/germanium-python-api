#!/usr/bin/env bash

set -e

GERMANIUM_FOLDER=$(readlink -f $(dirname $0)/..)
TAG_VERSION=$($GERMANIUM_FOLDER/bin/version/python-version.sh --tag)

cd $GERMANIUM_FOLDER

echo "Germanium folder is now `pwd`"
find $GERMANIUM_FOLDER/features
docker run -v $GERMANIUM_FOLDER/features:/tests/features:ro \
            germanium/germanium-$TAG_VERSION

