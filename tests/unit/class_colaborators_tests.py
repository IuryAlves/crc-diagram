# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os
from pycrc import py_to_crc
from tests import test


join = os.path.join


class ClassColaboratorsTestCase(test.CrcTestCase):

    def test_class_colaborator(self):
        python_file = 'class_colaborator'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['colaborators'], ['image_uploader'])

    def test_multiple_class_colaborators(self):
        python_file = 'multiple_class_colaborators'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['colaborators'], ['html_parser', 'json_parser'])
