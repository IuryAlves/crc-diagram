# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os
import ast
from .utils import ast_from_file
from .crc_module import CRCModule


def py_to_crc(module):
    tree = ast_from_file(module)
    module_name = os.path.split(module)[-1]
    crc_parser = CRCParser(module_name, CRCModule, tree)
    crc_parser.run()
    return crc_parser.to_dict()


class CRCParser(ast.NodeVisitor):

    def __init__(self, module, crc_module, tree, *args, **kwargs):
        super(CRCParser, self).__init__()
        self.tree = tree
        self.module = crc_module(name=module)
        self.classes = []

    def run(self):
        self.visit(self.tree)
        self._add_module_responsability()

    def to_dict(self):
        return {
            'module': self.module.to_dict()
        }

    def _add_module_colaborator(self, node):
        self.module.colaborators.extend(
            [alias.name for alias in node.names]
        )

    def _add_module_responsability(self):
        self.module.responsability = ast.get_docstring(self.tree)

    def visit_Import(self, node):
        self._add_module_colaborator(node)

    def visit_ImportFrom(self, node):
        self._add_module_colaborator(node)
