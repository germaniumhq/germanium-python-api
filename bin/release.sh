#!/usr/bin/env bash

#
# Just a tiny script to do all the rebases, and check
# all supported versions of python.
#

set -e

VERSION=$1

git checkout python3.4
git rebase -ff master
git checkout python3.5
git rebase -ff master
git checkout python2.7
git rebase master
git checkout master
git push --all -f

if [[ "$VERSION" != "" ]]; then
    git tag -f $VERSION master
    git tag -f "$VERSION-python2.7" python2.7
    git tag -f "$VERSION-python3.4" python3.4
    git tag -f "$VERSION-python3.5" python3.5
    git push -f --tags

    python setup.py sdist upload -r pypitest
    python setup.py sdist upload -r pypi
fi # [[ "$VERSION" != "" ]]

