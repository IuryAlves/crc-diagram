# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from .utils import ast_from_file


def py_to_crc(python_file):
    tree = ast_from_file(python_file)
    crc_parser = CRCParser(tree)
    crc_parser.run()
    return crc_parser.output


class CRCParser(ast.NodeVisitor):

    def __init__(self, tree, *args, **kwargs):
        super(CRCParser, self).__init__()
        self.tree = tree
        self.output = {
            'colaborators': [],
            'responsability': ''
        }

    def run(self):
        self.visit(self.tree)
        self._add_module_responsability()

    def _add_colaborator(self, node):
        self.output['colaborators'].extend(
            [alias.name for alias in node.names]
        )

    def _add_module_responsability(self):
        self.output['responsability'] = ast.get_docstring(self.tree)

    def visit_Import(self, node):
        self._add_colaborator(node)

    def visit_ImportFrom(self, node):
        self._add_colaborator(node)
