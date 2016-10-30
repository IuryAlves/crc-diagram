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

    def _get_class_collaborator(self, node):
        function_args = node.args.args
        function_args_names = get_function_argument_names(function_args, ('self', ))
        self.current_class["collaborators"].extend(function_args_names)
    
    def _get_class_docstring(self, node):
        self.current_class["docstring"] = ast.get_docstring(node) or ""

    def _get_class_methods(self, node):
        self.current_class['methods'].append(node.name)

    def visit_FunctionDef(self, node):
        if node.name == '__init__':
            self._get_class_collaborator(node)
        else:
            self._get_class_methods(node)

    def visit_ClassDef(self, node):
        self.current_class = _build_class()
        self._get_class_docstring(node)
        self.generic_visit(node)
        self._classes.update({
            node.name: self.current_class
        })
