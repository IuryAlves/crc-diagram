# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.testing import testcase
from crc_diagram.core.parsers import SmallTalkParser, PythonParser


class SmallTalkParserTestCase(testcase.CrcTestCase):

    def test_parser_smalltalk_file(self):
        parser = SmallTalkParser(
            join(self.test_files, 'smalltalk_project', 'enrollment.st')
        )
        crc_cards = parser.parse().result
        crc_card = crc_cards[0]

        self.assertEqual(crc_card.collaborators, ['Seminar'])


class PythonParserTestCase(testcase.CrcTestCase):
    def test_parser_class_collaborator(self):
        crc_cards = PythonParser(join(self.test_files, 'python_project', 'student.py')).parse().result
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
        crc_cards = PythonParser(join(self.test_files, 'python_project', 'seminar.py')).parse().result
        crc_card = crc_cards[0]
        self.assertEqual(crc_card.name, "Seminar")
