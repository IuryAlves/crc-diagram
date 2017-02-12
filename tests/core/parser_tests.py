# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.testing import testcase
from crc_diagram.core.parsers import PythonParser
from crc_diagram.exceptions import ParserException


class PythonParserTestCase(testcase.CrcTestCase):

    def test_parsing_txt_files_raises_exception(self):

        parser = PythonParser(join(self.test_files, 'file.txt'))

        with self.assertRaises(ParserException) as ctx:
            parser.parse()

        self.assertIn('file.txt is not a python file',
                      str(ctx.exception))

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
