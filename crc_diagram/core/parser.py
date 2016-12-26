# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from six import string_types

from crc_diagram.utils import ast_from_file
from crc_diagram.exceptions import ParserException
from .patterns import COLLABORATOR_PATTERN, RESPONSIBILITY_PATTERN
from .crc import CRC


class CRCParser(ast.NodeVisitor):

    def __init__(self, path_or_stream,
                 collaborator_pattern=COLLABORATOR_PATTERN,
                 responsibility_pattern=RESPONSIBILITY_PATTERN):
        super(CRCParser, self).__init__()
        self.path_or_stream = path_or_stream
        self.responsibility_pattern = responsibility_pattern
        self.collaborator_pattern = collaborator_pattern
        self._crcs = []
        self.current_crc = None

    def run(self):
        if isinstance(self.path_or_stream, string_types):
            self.path_or_stream = open(self.path_or_stream)
        try:
            tree = ast_from_file(self.path_or_stream)
        except (SyntaxError, ):
            raise ParserException('File {file} is not a python file'.format(
                file=self.path_or_stream.name
                ))
        else:
            self.visit(tree)
        return self

    @property
    def result(self):
        return [crc for crc in self._crcs]

    def get_responsibility(self, string):
        responsibility = self._get_annotation(
            string,
            self.responsibility_pattern
        )
        if responsibility:
            self.current_crc.responsibilities.append(responsibility)

    def get_collaborator(self, string):
        collaborator = self._get_annotation(string, self.collaborator_pattern)
        if collaborator:
            self.current_crc.collaborators.append(collaborator)

    def _get_annotation(self, string, pattern):
        annotation = pattern.match(string)
        return annotation.group(1).strip() if annotation is not None else None

    def visit_ClassDef(self, node):
        self.current_crc = CRC(name=node.name)
        docstring = ast.get_docstring(node) or ""
        for line in docstring.split('\n'):
            self.get_collaborator(line)
            self.get_responsibility(line)
        self._crcs.append(self.current_crc)
