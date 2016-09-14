# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from .utils import ast_from_file


def py_to_crc(python_file):
    tree = ast_from_file(python_file)
    crc_parser = CRCParser()
    crc_parser.visit(tree)
    return crc_parser.output


class CRCParser(ast.NodeVisitor):

    def __init__(self, *args, **kwargs):
        super(CRCParser, self).__init__()
        self.output = {
            'colaborators': [],
            'responsability': ''
        }

    def _add_colaborator(self, node):
        self.output['colaborators'].extend(
            [alias.name for alias in node.names]
        )

    def visit_Import(self, node):
        self._add_colaborator(node)

    def visit_ImportFrom(self, node):
        self._add_colaborator(node)

    def visit_Str(self, node):
        self.output['responsability'] += node.s
