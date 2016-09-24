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


class ClassColaboratorsTestCase(unittest.TestCase):

    def setUp(self):
        super(ClassColaboratorsTestCase, self).setUp()
        self.current_path = dirname(os.path.realpath(__file__))

    def test_class_colaborator(self):
        python_file = 'class_colaborator'
        result = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        cls = result['classes'][0]
        self.assertEqual(cls['colaborators'], ['image_uploader'])

    def test_multiple_class_colaborators(self):
        python_file = 'multiple_class_colaborators'
        result = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        cls = result['classes'][0]

        self.assertEqual(cls['colaborators'], ['html_parser', 'json_parser'])
