# coding: utf-8

from __future__ import (
    absolute_import,
)

from os.path import join
from crc_diagram import to_crc
from crc_diagram.testing import testcase


class PyToCrcTestCase(testcase.CrcTestCase):

    def test_raise_exception_if_is_not_python_file(self):
        file_ = 'file.txt'
        file_path = join(self.test_files, file_)
        result = to_crc(file_path)

        self.assertEqual(result, [])

    def test_py_to_crc(self):
        file_path = join(self.test_files, 'python_project', 'student.py')

        crc_cards = to_crc(file_path)
        crc_card = crc_cards[1]
        self.assertEqual(crc_card.name, 'Student')
        self.assertEqual(crc_card.collaborators, ['Enrollment'])
        self.assertEqual(crc_card.responsibilities,
                         ['Validate Identifying info',
                          'Provide list of seminars taken'])
