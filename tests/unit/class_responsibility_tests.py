# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join

from pycrc import py_to_crc, test


class ClassResponsibilityTestCase(test.CrcTestCase):

    def test_class_responsibility(self):
        python_file = 'class_responsibility'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['responsibility'], 'A class that represents a game scene')
