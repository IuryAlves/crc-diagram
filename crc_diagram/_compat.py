# coding: utf-8

import six


if six.PY3:
    from io import IOBase

    file = IOBase


__all__ = [
    'file'
]
