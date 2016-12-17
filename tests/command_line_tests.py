# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import unittest
import subprocess
import json
from crc_diagram import test


class CommandLineTestCase(test.CrcTestCase):

    def test_render_crc_cards_as_svg(self):
        command = 'python -m crc_diagram --render=svg ' \
                  '{test_files}/{folder} test.svg'.format(
                    test_files=self.test_files,
                    folder='project'
        )
        status = subprocess.check_call(command.split())

        self.assertEqual(status, 0)

    def test_execute_as_raw(self):
        command = 'python -m crc_diagram --raw=true {test_files}/{file}'.format(
            test_files=self.test_files,
            file='class_collaborator',
        )
        out = subprocess.check_output(command.split())
        result = json.loads(out.decode())
        self.assertEqual(result,
                         [
                             {
                                 'name': 'HtmlParser',
                                 'collaborators': ['ImageUploader'],
                                 'responsibilities': []
                             }
                         ])


if __name__ == '__main__':
    unittest.main()
