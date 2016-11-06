# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import re


RESPONSIBILITY_PATTERN = re.compile(r'@responsibility:(.*)$')
COLLABORATOR_PATTERN = re.compile(r'@collaborator:(.*)$')
