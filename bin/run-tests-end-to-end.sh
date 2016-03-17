#!/usr/bin/env bash

#
# This will run the tets for Germanium end-to-end inside a specifically
# built docker instance.
#

set -e

GERMANIUM_FOLDER=$(readlink -f $(dirname $0)/..)
TAG_VERSION=$($GERMANIUM_FOLDER/bin/version/python-version.sh --tag)

cd $GERMANIUM_FOLDER

if [[ "$1" == "--test" ]]; then
    # running in testing the thing in the docker instance
    echo "Running with --test flag, will set TEST_REUSE_BROWSER=1"
    docker run -it \
               -v $GERMANIUM_FOLDER:/tests:ro \
               -e TEST_REUSE_BROWSER=1 \
               germanium/germanium-$TAG_VERSION
else # not [[ "$1" == "--test" ]]
    # distribution mode.
    docker run -it \
               -v $GERMANIUM_FOLDER/features:/tests/features:ro \
                germanium/germanium-$TAG_VERSION
fi   # else [[ "$1" == "--test" ]]

