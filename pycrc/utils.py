# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)
import ast


def ast_from_file(file):
    with open(file) as fp:
        tree = ast.parse(fp.read())
    return tree
