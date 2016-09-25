# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc
from tests import test

join = os.path.sep.join


class ModuleColaboratorsTestCase(test.CrcTestCase):

    def test_module_name(self):
        python_file = 'import_module'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ])
        )

        self.assertEqual(result['module']['name'], 'import_module')

    def test_import_colaborator(self):
        python_file = 'import_module'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ])
        )
        self.assertEqual(result['module']['colaborators'], ['json'])

    def test_import_modules(self):
        python_file = 'import_modules'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ])
        )

        self.assertEqual(result['module']['colaborators'], ['ast', 're'])

    def test_import_module_as(self):
        python_file = 'import_module_as'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ])
        )

        self.assertEqual(result['module']['colaborators'], ['io'])

    def test_import_from(self):
        python_file = 'import_from'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ]))

        self.assertEqual(result['module']['colaborators'], ['namedtuple', 'deque'])