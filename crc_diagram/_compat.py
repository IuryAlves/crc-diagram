# coding: utf-8

import six


if six.PY3:
    from io import IOBase

    file = IOBase
else:
    file = __builtins__['file']


__all__ = [
    'file'
]
