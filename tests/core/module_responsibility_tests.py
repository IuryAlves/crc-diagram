# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from pycrc import py_to_crc, test


class ModuleResponsibilityTestCase(test.CrcTestCase):

    def test_module_responsibility(self):
        python_file = 'module_responsibility'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        self.assertEqual(result['module']['responsibility'], 'Module responsibility')

    def test_only_first_string_should_be_the_docstring(self):
        python_file = 'module_responsibility_multiple_strings'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        self.assertEqual(result['module']['responsibility'], 'First string')
