# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import re
from six import string_types


def regex_compile(pattern, flags=0):
    if not isinstance(pattern, re._pattern_type):
        return re.compile(pattern, flags=flags)
    return pattern


def path_to_stream(path_or_stream, mode='r'):
    if isinstance(path_or_stream, string_types):
        return open(path_or_stream, mode=mode)
    return path_or_stream


def split_by_extension(filename):
    splitted = filename.split('.')
    if len(splitted) == 1:
        return filename, None
    return ''.join(splitted[:-1]), splitted[-1]
