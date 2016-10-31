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
        result = CRCParser(tree, CRC).run().get_result()

        self.assertEqual(
            result["classes"]["HtmlParser"]["collaborators"],
            ["ImageUploader"]
        )

    def test_parser_class_responsibility(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_responsibility'))
        result = CRCParser(tree, CRC).run().get_result()

        self.assertEqual(
            result["classes"]["GameScene"]["responsibilities"],
            ["A class that represents a game scene"]
        )

    def test_parser_class_name(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        result = CRCParser(tree, CRC).run().get_result()

        self.assertEqual(list(result["classes"].keys()), ["HtmlParser"])
