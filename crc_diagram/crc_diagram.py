# coding: utf-8

from __future__ import (
    unicode_literals,
    absolute_import
)

import os

from .core import CRCParser, CRC
from .exceptions import ParserException
from .utils import ast_from_file


def py_to_crc(file, path=None):
    """
    return a list of CRC objects
    """
    if path is not None:
        file = os.path.join(path, file)
    try:
        tree = ast_from_file(file)
    except (SyntaxError, ):
        raise ParserException('File {file} is not a python file'.format(file=file))
    else:
        return CRCParser(tree, CRC).run().result


def project_to_crc(path):
    crcs = []
    for _, _, files in os.walk(path):
        for file in files:
            crcs.extend(py_to_crc(file, path=path))
    return crcs
