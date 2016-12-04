# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram.core import CRCParser, CRC
from crc_diagram import test, utils


class CRCParserTestCase(test.CrcTestCase):

    def test_parser_class_collaborator(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]
        self.assertListEqual(
            crc_card.collaborators,
            ["ImageUploader"]
        )

    def test_parser_class_responsibility(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_responsibility'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]

        self.assertListEqual(
            crc_card.responsibilities,
            ["A class that represents a game scene"]
        )

    def test_parser_class_name(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        crc_cards = CRCParser(tree, CRC).run().result
        crc_card = crc_cards[0]
        self.assertEqual(crc_card.name, "HtmlParser")
