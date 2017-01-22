# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import tempfile
from crc_diagram.test import testcase
from crc_diagram import utils
from crc_diagram._compat import file


class UtilsTestCase(testcase.CrcTestCase):

    def test_split_by_extension(self):

        self.assertEqual(utils.split_by_extension('crc.png'), ('crc', 'png'))

    def test_split_by_extension_without_extension(self):

        self.assertEqual(utils.split_by_extension('crc'), ('crc', None))

    def test_path_to_stream_as_string(self):

        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            self.assertIsInstance(utils.path_to_stream(tmp.name), file)
