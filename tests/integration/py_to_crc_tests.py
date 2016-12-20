# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram import py_to_crc,  exceptions
from crc_diagram.test import testcase


class PyToCrcTestCase(testcase.CrcTestCase):

    def test_raise_exception_if_is_not_python_file(self):
        file = 'not_a_python_file'

        with self.assertRaises(exceptions.ParserException) as context:
            py_to_crc(file, self.test_files)

        self.assertIn('not_a_python_file is not a python file',
                      str(context.exception))

    def test_py_to_crc(self):
        file = join('project', 'student.py')

        crc_cards = py_to_crc(file, self.test_files)
        crc_card = crc_cards[0]

        self.assertDictEqual(crc_card.to_dict(), {
                'name': 'Student',
                'collaborators': ['Enrollment'],
                'responsibilities': [
                    'Validate Identifying info',
                    'Provide list of seminars taken'
                ]
                }
        )
