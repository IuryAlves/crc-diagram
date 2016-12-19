# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import unittest
import subprocess
import json
import os
from crc_diagram import test


class CommandLineTestCase(test.CrcTestCase):

    def setUp(self):
        super(CommandLineTestCase, self).setUp()
        self.out_file = 'test.svg'

    def tearDown(self):
        os.remove(self.out_file)

    def test_render_crc_cards_as_svg(self):
        command = 'python -m crc_diagram --render=svg {test_files}/{folder} {out_file}'.format(
            test_files=self.test_files,
            folder='project',
            out_file=self.out_file
        )
        status = subprocess.check_call(command.split())

        self.assertEqual(status, 0)

    def test_execute_as_raw(self):
        command = 'python -m crc_diagram --raw=true {folder}/{file}'.format(
            folder=os.path.join(self.test_files, 'project'),
            file='professor.py',
        )
        out = subprocess.check_output(command.split())
        result = json.loads(out.decode())
        self.assertEqual(result,
                         [
                             {
                                 'name': 'Professor',
                                 'collaborators': ['Seminar'],
                                 'responsibilities': ['Provide information', 'Get Seminars instructing']
                             }
                         ])


if __name__ == '__main__':
    unittest.main()
