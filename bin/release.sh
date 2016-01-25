#!/usr/bin/env bash

#
# Just a tiny script to do all the rebases, and check
# all supported versions of python.
#

set -e

git checkout python2.7
git rebase master
git checkout python3.4
git rebase -ff master
git push --all

