# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from .patterns import COLLABORATOR_PATTERN, RESPONSIBILITY_PATTERN


class CRCParser(ast.NodeVisitor):

    def __init__(self, tree, CRC,
                 collaborator_pattern=COLLABORATOR_PATTERN,
                 responsibility_pattern=RESPONSIBILITY_PATTERN):
        super(CRCParser, self).__init__()
        self.tree = tree
        self.CRC = CRC
        self.responsibility_pattern = responsibility_pattern
        self.collaborator_pattern = collaborator_pattern
        self._crcs = []
        self.current_crc = None

    def run(self):
        self.visit(self.tree)
        return self

    def get_result(self):
        return {
            "classes": {crc.name: crc.to_dict() for crc in self._crcs}
        }

    def _get_responsibility(self, string):
        responsibility_match = self.responsibility_pattern.match(string)
        if responsibility_match is not None:
            responsibility = responsibility_match.group(1).strip()
            self.current_crc.responsibilities.append(responsibility)

    def _get_collaborator(self, string):
        collaborator_match = self.collaborator_pattern.match(string)
        if collaborator_match is not None:
            collaborator = collaborator_match.group(1).strip()
            self.current_crc.collaborators.append(collaborator)

    def visit_ClassDef(self, node):
        self.current_crc = self.CRC(name=node.name)
        docstring = ast.get_docstring(node) or ""
        for line in docstring.split('\n'):
            self._get_collaborator(line)
            self._get_responsibility(line)
        self._crcs.append(self.current_crc)
