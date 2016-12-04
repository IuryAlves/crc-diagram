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
    for item in os.walk(path):
        files = item[2]
        for file in files:
            yield py_to_crc(file, path=path)
