# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast

from ._compat import get_function_argument_names
from .utils import filter_function_defs


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
        self._add_module_responsability()

    def to_dict(self):
        return {
            'module': self.module.to_dict(),
            'classes': [cls.to_dict() for cls in self.classes]
        }

    def _add_module_colaborator(self, node):
        self.module.colaborators.extend(
            [alias.name for alias in node.names]
        )

    def _add_module_responsability(self):
        self.module.responsability = ast.get_docstring(self.tree)

    def _add_class_colaborator(self, function_defs):
        functions = list(filter(lambda function: function.name == '__init__', function_defs))
        if functions:
            init_function = functions[0]
            function_args = init_function.args.args
            function_args_names = get_function_argument_names(function_args, ('self', ))
            self.current_crc_class.colaborators.extend(function_args_names)

    def _add_class_responsability(self, node):
        self.current_crc_class.responsability = ast.get_docstring(node)

    def visit_Import(self, node):
        self._add_module_colaborator(node)

    def visit_ImportFrom(self, node):
        self._add_module_colaborator(node)

    def visit_ClassDef(self, node):
        self.current_crc_class = self.crc_class()
        function_defs = filter_function_defs(node.body)
        self._add_class_colaborator(function_defs)
        self._add_class_responsability(node)
        self.classes.append(self.current_crc_class)
