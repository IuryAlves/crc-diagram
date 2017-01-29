# coding: utf-8

from __future__ import (
    unicode_literals,
    absolute_import
)

import os

from crc_diagram.core.parsers import PythonParser


def py_to_crc(fp, path=None, parser_class=PythonParser):
    """
    return a list of CRC objects
    """
    if path is not None:
        fp = os.path.join(path, fp)
    return parser_class(fp).parse().result


def project_to_crc(path, parser_class=PythonParser):
    crcs = []
    for _, _, files in os.walk(path):
        for file in files:
            crcs.extend(py_to_crc(file, path=path, parser_class=parser_class))
    return crcs
