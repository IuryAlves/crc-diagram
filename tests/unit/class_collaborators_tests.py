# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from pycrc import py_to_crc, test


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
