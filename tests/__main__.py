#! /usr/bin/env python
# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import sys
import os
import unittest
import click


@click.command('test-runner')
@click.option('--test-pattern', default='*tests.py')
@click.option('--test-case', default=None)
def main(test_pattern, test_case):

    project_path = os.path.split(os.path.dirname(__file__))
    sys.path.append(project_path[0])
    test_loader = unittest.TestLoader()
    if test_case is not None:
        tests = unittest.TestSuite()
        tests.addTest()
    else:
        tests = test_loader.discover("tests", test_pattern)
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    main()
