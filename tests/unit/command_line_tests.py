# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import subprocess
import json
from tests import test


class CrcNameTestCase(test.CrcTestCase):

    def test_execute_as_raw(self):
        command = 'python -m pycrc --raw=true {test_files}/{file}'.format(
            test_files=self.test_files,
            file='class_colaborator'
        )
        out = subprocess.check_output(command.split())
        result = json.loads(out.decode())
        self.assertEqual(result, {
            'classes': [
                {'colaborators': ['image_uploader'],
                 'name': 'HtmlParser',
                 'responsibility': None}
            ],
            'module': {
                'colaborators': [],
                'name': 'class_colaborator',
                'responsibility': None
            }
        })
