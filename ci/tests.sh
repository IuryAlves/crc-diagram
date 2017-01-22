#!/usr/bin/env sh

set -e

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

coverage run tests/__main__.py
flake8 .
