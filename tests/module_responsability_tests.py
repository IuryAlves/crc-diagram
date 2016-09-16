# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import unittest
import os

from pycrc import py_to_crc

join = os.path.sep.join
dirname = os.path.dirname


class ModuleResponsabilityTestCase(unittest.TestCase):

    def setUp(self):
        super(ModuleResponsabilityTestCase, self).setUp()
        self.current_path = dirname(os.path.realpath(__file__))

    def test_module_responsability(self):
        python_file = 'module_responsability.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )
        self.assertEqual(output['responsability'], 'Module Responsability')

    def test_only_first_string_should_be_the_docstring(self):
        python_file = 'module_responsability_multiple_strings.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )
        self.assertEqual(output['responsability'], 'First string')
