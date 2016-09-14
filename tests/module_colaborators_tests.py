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


class ModuleColaboratorsTestCase(unittest.TestCase):

    def setUp(self):
        super(ModuleColaboratorsTestCase, self).setUp()
        self.current_path = dirname(os.path.realpath(__file__))

    def test_import_colaborator(self):
        python_file = 'import_module.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )
        self.assertEqual(output['colaborators'], ['json'])

    def test_import_modules(self):
        python_file = 'import_modules.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )

        self.assertEqual(output['colaborators'], ['ast', 're'])

    def test_import_module_as(self):
        python_file = 'import_module_as.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ])
        )

        self.assertEqual(output['colaborators'], ['io'])

    def test_import_from(self):
        python_file = 'import_from.py'
        output = py_to_crc(join([
            self.current_path,
            'test_files',
            python_file
        ]))

        self.assertEqual(output['colaborators'], ['namedtuple', 'deque'])
