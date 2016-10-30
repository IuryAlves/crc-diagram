# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from pycrc._compat import get_function_argument_names


def _build_class():
    return {
        "collaborators": [],
        "docstring": "",
        "methods": []
    }


class Parser(ast.NodeVisitor):

    def __init__(self, tree):
        super(Parser, self).__init__()
        self.tree = tree
        self._classes = {}
        self.current_class = None

    def run(self):
        self.visit(self.tree)
        return self

    def get_result(self):
        return {
            "classes": self._classes
        }

    def _get_class_docstring(self, node):
        self.current_class["docstring"] = ast.get_docstring(node) or ""

    def _get_class_methods(self, node):
        self.current_class['methods'].append(node.name)

    def visit_FunctionDef(self, node):
        name = node.name
        if not name.startswith('__') and not name.endswith('__'):
            self._get_class_methods(node)

    def visit_ClassDef(self, node):
        self.current_class = _build_class()
        self._get_class_docstring(node)
        self.generic_visit(node)
        self._classes.update({
            node.name: self.current_class
        })
