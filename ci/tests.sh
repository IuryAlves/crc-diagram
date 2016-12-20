#!/usr/bin/env sh

set +e

coverage run tests/__main__.py
flake8 .
