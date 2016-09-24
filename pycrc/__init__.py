# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)
import os

from .crc_parser import CRCParser
from .crc import CRC
from .utils import ast_from_file


def py_to_crc(module):
    tree = ast_from_file(module)
    module_name = os.path.split(module)[-1]
    crc_parser = CRCParser(module_name, CRC, tree)
    crc_parser.run()
    return crc_parser.to_dict()


__all__ = [
    'ast_from_file',
    'CRC',
    'CRCParser',
    'py_to_crc',
]
