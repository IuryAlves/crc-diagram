# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import unittest
import os
import ast

from py_crc import CRCParser

join = os.path.sep.join


class ModuleColaboratorsTestCase(unittest.TestCase):

	def setUp(self):
		super(ModuleColaboratorsTestCase, self).setUp()
		self.current_path = os.path.dirname(os.path.realpath(__file__))

	def test_import_colaborator(self):
		python_file = 'import_module.py'
		with open(join([self.current_path, 'test_files', 'import_module.py'])) as file:
			tree = ast.parse(file.read())

		crc_parser = CRCParser()
		crc_parser.visit(tree)

		self.assertEqual(crc_parser.output, {'colaborators': ['json']})
