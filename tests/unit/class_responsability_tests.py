# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc
from tests import test

join = os.path.join


class ClassResponsabilityTestCase(test.CrcTestCase):

    def test_class_colaborator(self):
        python_file = 'class_responsability'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['responsability'], 'A class that represents a game scene')
