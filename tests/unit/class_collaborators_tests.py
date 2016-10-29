# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os
from pycrc import py_to_crc
from tests import test


join = os.path.join


class ClassCollaboratorsTestCase(test.CrcTestCase):

    def test_class_collaborator(self):
        python_file = 'class_collaborator'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['collaborators'], ['image_uploader'])

    def test_multiple_class_collaborators(self):
        python_file = 'multiple_class_collaborators'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        cls = result['classes'][0]
        self.assertEqual(cls['collaborators'], ['html_parser', 'json_parser'])
