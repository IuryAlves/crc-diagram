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


class CrcNameTestCase(unittest.TestCase):

    def setUp(self):
        super(CrcNameTestCase, self).setUp()
        self.current_path = dirname(os.path.realpath(__file__))

    def test_class_name(self):
        python_file = 'class_colaborator'
        result = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        cls = result['classes'][0]
        self.assertEqual(cls['name'], 'HtmlParser')

    def test_module_name(self):
        python_file = 'import_module'
        result = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        module = result['module']

        self.assertEqual(module['name'], 'import_module')
