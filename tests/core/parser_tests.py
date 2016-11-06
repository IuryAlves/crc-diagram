# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from pycrc import CRCParser, CRC, test, utils


class CRCParserTestCase(test.CrcTestCase):

    def test_parser_class_collaborator(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        crc_gen = CRCParser(tree, CRC).run().result
        crc = next(crc_gen)
        self.assertListEqual(
            crc.collaborators,
            ["ImageUploader"]
        )

    def test_parser_class_responsibility(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_responsibility'))
        crc_gen = CRCParser(tree, CRC).run().result
        crc = next(crc_gen)

        self.assertListEqual(
            crc.responsibilities,
            ["A class that represents a game scene"]
        )

    def test_parser_class_name(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        crc_gen = CRCParser(tree, CRC).run().result
        crc = next(crc_gen)
        self.assertEqual(crc.name, "HtmlParser")
