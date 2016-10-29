# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)
import os

from pycrc.core.crc_parser import CRCParser
from pycrc.core.crc import CRC
from pycrc.renders.svg import SvgRender
from .exceptions import NotAPythonFile
from .utils import ast_from_file


def py_to_crc(module, folder=None):
    if folder is not None:
        module = os.path.join(folder, module)
    try:
        tree = ast_from_file(module)
    except (SyntaxError, ):
        raise NotAPythonFile('File {file} is not a python file'.format(file=module))
    else:
        module_name = os.path.split(module)[-1].strip('.py')
        crc_parser = CRCParser(module_name, CRC, tree)
        crc_parser.run()
        return crc_parser.to_dict()


def project_to_crc(folder):
    for item in os.walk(folder):
        files = item[2]
        for file in files:
            yield py_to_crc(file, folder=folder)


__all__ = [
    'ast_from_file',
    'CRC',
    'CRCParser',
    'NotAPythonFile',
    'py_to_crc',
    'project_to_crc',
    'SvgRender'
]
