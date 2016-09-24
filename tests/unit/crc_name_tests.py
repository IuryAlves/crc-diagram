# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc
from tests import test

join = os.path.sep.join


class CrcNameTestCase(test.CrcTestCase):

    def test_class_name(self):
        python_file = 'class_colaborator'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ]))

        cls = result['classes'][0]
        self.assertEqual(cls['name'], 'HtmlParser')

    def test_module_name(self):
        python_file = 'import_module'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ]))

        module = result['module']

        self.assertEqual(module['name'], 'import_module')
