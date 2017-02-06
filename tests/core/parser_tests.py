# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.testing import testcase
from crc_diagram.core.parsers import PythonParser


class PythonParserTestCase(testcase.CrcTestCase):

    def test_parser_module_collaborator(self):
        crc_cards = PythonParser(join(self.test_files, 'module.py')).parse().result
        card = crc_cards[0]

        self.assertEqual(card.kind, 'module')
        self.assertEqual(card.name, 'module')

    def test_parser_class_collaborator_with_raw_string_pattern(self):
        parser = PythonParser(
            join(self.test_files, 'python_project', 'student.py'),
            r'\s*?@collaborator:(.*)$'
        )
        parser.parse()
        crc_cards = parser.result
        crc_card = crc_cards[0]
        self.assertListEqual(
            crc_card.collaborators,
            ["Enrollment"]
        )

    def test_parser_class_collaborator(self):
        parser = PythonParser(join(self.test_files,
                                   'python_project',
                                   'student.py'))
        crc_cards = parser.parse().result
        crc_card = crc_cards[0]
        self.assertListEqual(
            crc_card.collaborators,
            ["Enrollment"]
        )

    def test_parser_class_responsibility(self):

        with open(join(self.test_files, 'python_project', 'enrollment.py')) as fp:
            crc_cards = PythonParser(fp).parse().result
        crc_card = crc_cards[0]

        self.assertListEqual(
            crc_card.responsibilities,
            ['Get students', 'Get seminar', 'Get Final Grade']
        )

    def test_parser_class_name(self):
        parser = PythonParser(join(self.test_files,
                                   'python_project',
                                   'seminar.py'))

        crc_cards = parser.parse().result
        crc_card = crc_cards[0]
        self.assertEqual(crc_card.name, "Seminar")
