# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from six import string_types


def path_to_stream(path_or_stream):
    if isinstance(path_or_stream, string_types):
        return open(path_or_stream)
    return path_or_stream


def split_by_extension(filename):
    splitted = filename.split('.')
    if len(splitted) == 1:
        return filename, None
    return ''.join(splitted[:-1]), splitted[-1]
