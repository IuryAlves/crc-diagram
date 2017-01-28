# coding: utf-8

from os.path import abspath, join, pardir
import unittest
import re


class CrcTestCase(unittest.TestCase):

    def setUp(self):
        super(CrcTestCase, self).setUp()
        self.test_files = abspath(
            join(__file__, pardir, 'files')
        )

    def assertMultiLineEscapeCharsEqual(self, first, second, msg=None):
        escape_regex = re.compile(r'\s\n\t')
        first = escape_regex.sub(first, '')
        second = escape_regex.sub(second, '')

        return self.assertMultiLineEqual(first, second, msg=msg)
