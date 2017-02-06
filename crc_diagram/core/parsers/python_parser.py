# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from os import path
from contextlib import closing

from crc_diagram.exceptions import ParserException
from crc_diagram.core import CRC
from crc_diagram import utils
from crc_diagram.core.parsers.base_parser import BaseParser


class PythonParser(BaseParser, ast.NodeVisitor):
    """
    A parser class which extracts CRC data from docstrings using :py:data:`ast` module.

    :param path_or_stream: A file path or a file like object from where the CRCs will be extracted.
    :param regular_expression collaborator_pattern: A regex pattern do extract the collaborators
     from docstrings.
     The default is :py:data:`COLLABORATOR_PATTERN`.
    :param regular_expression responsibility_pattern: A regex pattern do extract the
     responsibilities from docstrings.
     The default is :py:data:`RESPONSIBILITY_PATTERN`.

    Example::

            parser = PythonParser('file.py').parse()
            parser.result

    The result is a list of :py:data:`CRC` instances::

            [
                CRC(name='HtmlToMarkdown',
                    kind='class',
                    collaborators=['ImageUploader'],
                    responsibilities=['Convert html files to markdown']
                    ),
                CRC(name='ImageUploader',
                    kind='class',
                    collaborators=[],
                    responsibilities=['Store images in the cloud']
                    )
            ]

    You can change the patterns used to extract responsibilities and collaborators
    passing a regular expression to PythonParser::

        responsibility_pattern = r'\s*?:responsibility:(.*)$'

        parser = PythonParser(
                    'file.py',
                    responsibility_pattern=responsibility_pattern
                )

    This will extract any data in docstring which has the following format::

        :responsibility: Save the world

    The same is valid to collaborators::

        collaborator_pattern = r'\s*?:collaborator:(.*)$'

        parser = PythonParser(
                    'file.py',
                    collaborator_pattern=collaborator_pattern
                )

    And you also can pass :py:data:`re.compile` objects::

        import re

        collaborator_pattern = re.compile(r'\s*?:collaborator:(.*)$')

        parser = PythonParser(
                    'file.py',
                    collaborator_pattern=collaborator_pattern
                )
        collaborator
    """
    def parse(self):
        """
        The main functionality. It parses a tree from :py:data:`self.path_or_stream`
        and uses :py:data:`ast.NodeVisitor` to iterate over the tree.

        :returns: self
        """
        self.stream.seek(0)
        try:
            with closing(self.stream) as stream:
                tree = ast.parse(stream.read())
        except (SyntaxError,):
            raise ParserException('File {file} is not a python file'.format(
                file=self.stream.name
            ))
        else:
            self.visit(tree)
        return self

    def visit_ClassDef(self, node):
        """
        Called when :py:data:`ast.NodeVisitor` finds a class.
        """
        self._add_crc(node, node.name, 'class')

    def visit_Module(self, node):
        """
        Called when :py:data:`ast.NodeVisitor` finds a module.
        """
        _, filename = path.split(self.stream.name)
        module_name, _ = utils.split_by_extension(filename)
        self._add_crc(node, module_name, 'module')
        self.generic_visit(node)

    def _add_crc(self, node, name, kind):
        docstring = ast.get_docstring(node)
        if docstring:
            self.current_crc = CRC(name=name, kind=kind)
            for line in docstring.split('\n'):
                self.get_collaborator(line)
                self.get_responsibility(line)
            self._crcs.append(self.current_crc)
