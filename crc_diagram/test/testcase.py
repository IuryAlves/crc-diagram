# coding: utf-8

from os.path import abspath, join, pardir
import unittest


class CrcTestCase(unittest.TestCase):

    def setUp(self):
        super(CrcTestCase, self).setUp()
        self.test_files = abspath(
            join(__file__, pardir, 'files')
        )
