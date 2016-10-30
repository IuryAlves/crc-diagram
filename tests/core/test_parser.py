# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from pycrc import Parser, test, utils


class ParserTestCase(test.CrcTestCase):

    def test_parser_class_collaborator(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_collaborator'))
        result = Parser(tree).run().get_result()

        self.assertEqual(
            result["classes"]["HtmlParser"]["collaborators"],
            ["image_uploader"]
        )

    def test_parser_class_docstring(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_responsibility'))
        result = Parser(tree).run().get_result()

        self.assertEqual(
            result["classes"]["GameScene"]["docstring"],
            "@responsibility: A class that represents a game scene"
        )

    def test_parser_class_methods(self):
        tree = utils.ast_from_file(join(self.test_files, 'class_methods'))
        result = Parser(tree).run().get_result()

        self.assertSetEqual(
            set(result["classes"]["Character"]["methods"]),
            {"attack", "guard", "roll", "walk"}
        )
