# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast

from crc_diagram.exceptions import ParserException
from crc_diagram.core.crc import CRC
from crc_diagram.core.parsers.base_parser import BaseParser


class PythonParser(BaseParser, ast.NodeVisitor):

    def parse(self):
        try:
            self.stream.seek(0)
            tree = ast.parse(self.stream.read())
        except (SyntaxError,):
            raise ParserException('File {file} is not a python file'.format(
                file=self.stream.name
            ))
        else:
            self.visit(tree)
        finally:
            if not self.stream.closed:
                self.stream.close()
        return self

    def _add_crc(self, node, kind):
        self.current_crc = CRC(kind, name=node.name)
        docstring = ast.get_docstring(node) or ""
        for line in docstring.split('\n'):
            self.get_collaborator(line)
            self.get_responsibility(line)
        self._crcs.append(self.current_crc)

    def visit_Module(self, node):
        self._add_crc(node, 'module')

    def visit_ClassDef(self, node):
        self._add_crc(node, 'class')
