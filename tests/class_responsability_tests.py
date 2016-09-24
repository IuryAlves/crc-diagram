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


class ClassResponsabilityTestCase(unittest.TestCase):

    def setUp(self):
        super(ClassResponsabilityTestCase, self).setUp()
        self.current_path = dirname(os.path.realpath(__file__))

    def test_class_colaborator(self):
        python_file = 'class_responsability'
        result = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        cls = result['classes'][0]
        self.assertEqual(cls['responsability'], 'A class that represents a game scene')
