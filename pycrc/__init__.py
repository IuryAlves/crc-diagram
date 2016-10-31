# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)
import os

from pycrc.core.parser import CRCParser
from pycrc.core.crc import CRC
from pycrc.renders import Render
from pycrc.renders.svg import svg_render
from .exceptions import NotAPythonFile
from .utils import ast_from_file


def py_to_crc(module, path=None):
    if path is not None:
        module = os.path.join(path, module)
    try:
        tree = ast_from_file(module)
    except (SyntaxError, ):
        raise NotAPythonFile('File {file} is not a python file'.format(file=module))
    else:
        parser = CRCParser(tree, CRC)
        return parser.run().get_result()


def project_to_crc(path):
    for item in os.walk(path):
        files = item[2]
        for file in files:
            yield py_to_crc(file, path=path)


__all__ = [
    'ast_from_file',
    'CRC',
    'CRCParser',
    'NotAPythonFile',
    'py_to_crc',
    'project_to_crc',
    'Render',
    'svg_render'
]
