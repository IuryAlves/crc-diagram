# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import ast


def ast_from_file(fp):
    try:
        tree = ast.parse(fp.read())
    finally:
        if not fp.closed:
            fp.close()
    return tree
