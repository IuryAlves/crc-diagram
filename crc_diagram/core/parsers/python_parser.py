# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast
from contextlib import closing
from crc_diagram.exceptions import ParserException
from crc_diagram.core.crc import CRC
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
    :param tuple allowed_file_extensions: A list of file extensions do accept.
      The parser will ignore any file which extension isn`t in this list.

    Example::

            parser = PythonParser('file.py').parse()
            parser.result

    The result is a list of :py:data:`CRC` instances::

            [
                CRC(name='HtmlToMarkdown',
                    collaborators=['ImageUploader'],
                    responsibilities=['Convert html files to markdown']
                    ),
                CRC(name='ImageUploader',
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

    def __init__(self, *args, **kwargs):
        super(PythonParser, self).__init__(*args, **kwargs)

        if not self.allowed_file_extensions:
            self.allowed_file_extensions = ('.py', )

    def parse(self):
        """
        The main functionality. It parses a tree from :py:data:`self.path_or_stream`
        and uses :py:data:`ast.NodeVisitor` to iterate over the tree.

        :returns: self
        """
        try:
            self.stream.seek(0)
            with closing(self.stream) as stream:
                tree = ast.parse(stream.read())
        except (SyntaxError,):
            raise ParserException('File {file_} is not a python file'.format(
                file_=self.stream.name
            ))
        else:
            self.visit(tree)
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
