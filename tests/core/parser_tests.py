# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.core import CRCParser
from crc_diagram.test import testcase


class CRCParserTestCase(testcase.CrcTestCase):

    def test_parser_class_collaborator(self):
        crc_cards = CRCParser(join(self.test_files, 'project', 'student.py')).run().result
        crc_card = crc_cards[0]
        self.assertListEqual(
            crc_card.collaborators,
            ["Enrollment"]
        )

    def test_parser_class_responsibility(self):

        with open(join(self.test_files, 'project', 'enrollment.py')) as fp:
            crc_cards = CRCParser(fp).run().result
        crc_card = crc_cards[0]

        self.assertListEqual(
            crc_card.responsibilities,
            ['Get students', 'Get seminar', 'Get Final Grade']
        )

    def test_parser_class_name(self):
        crc_cards = CRCParser(join(self.test_files, 'project', 'seminar.py')).run().result
        crc_card = crc_cards[0]
        self.assertEqual(crc_card.name, "Seminar")
