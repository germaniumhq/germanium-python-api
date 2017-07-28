#!/usr/bin/env bash

#
# Just a tiny script to do all the rebases, and check
# all supported versions of python.
#

set -e

VERSION=$1

PYTHON_VERSIONS="python2.7 python3.4 python3.5"

for PYTHON_VERSION in $PYTHON_VERSIONS; do
    git checkout $PYTHON_VERSION
    git rebase master
done

git checkout master
git push origin --all -f

if [[ "$VERSION" != "" ]]; then
    eval $(archer py)

    git tag -f $VERSION master

    for PYTHON_VERSION in $PYTHON_VERSIONS; do
        git tag -f "$VERSION-$PYTHON_VERSION" $PYTHON_VERSION
    done

    git push origin -f --tags

    py 3
    git checkout python3.5
    python setup.py bdist_wheel upload -r pypitest
    python setup.py bdist_wheel upload -r pypimain

    py 2
    git checkout python2.7
    python setup.py bdist_wheel upload -r pypitest
    python setup.py bdist_wheel upload -r pypimain

    git checkout master
fi # [[ "$VERSION" != "" ]]

