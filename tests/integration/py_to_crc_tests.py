# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from pycrc import py_to_crc, NotAPythonFile, test


class PyToCrcTestCase(test.CrcTestCase):

    def test_raise_exception_if_is_not_python_file(self):
        file = 'not_a_python_file'

        with self.assertRaises(NotAPythonFile) as context:
            py_to_crc(join(
                self.test_files,
                file))

        self.assertIn('not_a_python_file is not a python file',
                      str(context.exception))

    def test_py_to_crc(self):
        file = 'class_responsibilities_and_collaborators'

        result = py_to_crc(join(
            self.test_files,
            file
        ))

        self.assertEqual(result, {
            'classes': {
                'Student': {
                    'collaborators': ['Seminar', 'Transcript'],
                    'responsibilities': [
                        'enroll in seminars',
                        'drop seminars',
                        'request transcripts'
                    ]
                }
            }
        })
