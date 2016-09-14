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

    def test_import_colaborator(self):
        python_file = 'module_responsability.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )
        self.assertEqual(output['responsability'], '\nModule Responsability\n')
