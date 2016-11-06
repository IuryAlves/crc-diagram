# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import unittest
from os.path import abspath, join, pardir


class CrcTestCase(unittest.TestCase):

    def setUp(self):
        super(CrcTestCase, self).setUp()
        self.test_files = abspath(
            join(__file__, pardir,
                 pardir, pardir,
                 'tests', 'test_files')
        )
