# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.core import CRCParser, CRC
from crc_diagram import utils
from crc_diagram.test import testcase


class CRCParserTestCase(testcase.CrcTestCase):

    def test_parser_class_collaborator(self):
        tree = utils.ast_from_file(join(self.test_files, 'project', 'student.py'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]
        self.assertListEqual(
            crc_card.collaborators,
            ["Enrollment"]
        )

    def test_parser_class_responsibility(self):
        tree = utils.ast_from_file(join(self.test_files, 'project', 'enrollment.py'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]

        self.assertListEqual(
            crc_card.responsibilities,
            ['Get students', 'Get seminar', 'Get Final Grade']
        )

    def test_parser_class_name(self):
        tree = utils.ast_from_file(join(self.test_files, 'project', 'seminar.py'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]
        self.assertEqual(crc_card.name, "Seminar")
