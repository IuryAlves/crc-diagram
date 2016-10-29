# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from pycrc._compat import get_function_argument_names


class CRCParser(ast.NodeVisitor):

    def __init__(self, module, crc, tree, *args, **kwargs):
        super(CRCParser, self).__init__(*args, **kwargs)
        self.tree = tree
        self.crc_class = crc
        self.module = self.crc_class(name=module)
        self.current_crc_class = None
        self.classes = []

    def run(self):
        self.visit(self.tree)
        self._add_module_responsibility()

    def to_dict(self):
        return {
            'module': self.module.to_dict(),
            'classes': [cls.to_dict() for cls in self.classes]
        }

    def _add_module_colaborator(self, node):
        self.module.colaborators.extend(
            [alias.name for alias in node.names]
        )

    def _add_module_responsibility(self):
        self.module.responsibility = ast.get_docstring(self.tree)

    def _add_class_colaborator(self, node):
        function_args = node.args.args
        function_args_names = get_function_argument_names(function_args, ('self', ))
        self.current_crc_class.colaborators.extend(function_args_names)

    def _add_class_responsibility(self, node):
        self.current_crc_class.responsibility = ast.get_docstring(node)

    def visit_Import(self, node):
        self._add_module_colaborator(node)

    def visit_ImportFrom(self, node):
        self._add_module_colaborator(node)

    def visit_FunctionDef(self, node):
        if node.name == '__init__':
            self._add_class_colaborator(node)

    def visit_ClassDef(self, node):
        self.current_crc_class = self.crc_class(name=node.name)
        self._add_class_responsibility(node)
        self.classes.append(self.current_crc_class)
        self.generic_visit(node)
