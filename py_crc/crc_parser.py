# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast


class CRCParser(ast.NodeVisitor):

	def __init__(self, *args, **kwargs):
		super(CRCParser, self).__init__()
		self.output = {
			'colaborators': []
		}

	def visit_Import(self, node):
		self.output['colaborators'].extend([alias.name for alias in node.names])
