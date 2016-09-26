# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os
from unittest import TestCase


dirname = os.path.dirname
realpath = os.path.realpath
join = os.path.join


class CrcTestCase(TestCase):

    def setUp(self):
        super(CrcTestCase, self).setUp()
        self.test_files = join(
            dirname(realpath(__file__)),
            'test_files'
        )
