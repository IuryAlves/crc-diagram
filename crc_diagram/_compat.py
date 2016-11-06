# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import sys

PY2 = sys.version_info[0] == 2


if PY2:
    def get_function_argument_names(fn_args, exclude):
        return [arg.id for arg in fn_args if arg.id not in exclude]
else:
    def get_function_argument_names(fn_args, exclude):
        return [arg.arg for arg in fn_args if arg.arg not in exclude]
