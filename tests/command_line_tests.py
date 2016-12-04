# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import subprocess
import json
from crc_diagram import test


class CommandLineTestCase(test.CrcTestCase):

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
