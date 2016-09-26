# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc
from tests import test

join = os.path.join


class ModuleResponsabilityTestCase(test.CrcTestCase):

    def test_module_responsability(self):
        python_file = 'module_responsability'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        self.assertEqual(result['module']['responsability'], 'Module Responsability')

    def test_only_first_string_should_be_the_docstring(self):
        python_file = 'module_responsability_multiple_strings'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        self.assertEqual(result['module']['responsability'], 'First string')
