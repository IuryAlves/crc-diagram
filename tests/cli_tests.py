# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os
import imghdr
import json
from click.testing import CliRunner
from crc_diagram.testing import testcase
from crc_diagram.__main__ import main


class CliTestCase(testcase.CrcTestCase):

    def setUp(self):
        super(CliTestCase, self).setUp()
        self.runner = CliRunner()

    def test_generate_crc_diagram_from_python_project(self):
        source = os.path.join(self.test_files, 'python_project')

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(main, [source, 'out.png'])

            self.assertEqual(result.exit_code, 0)
            with open('out.png', 'rb') as out:
                self.assertEqual(imghdr.test_png(out.read(), None), 'png')

    def test_generate_raw_crc_diagram(self):
        source = os.path.join(self.test_files, 'python_project', 'professor.py')
        result = self.runner.invoke(main, [source, '--raw=true'])
        output = json.loads(result.output)
        self.assertEqual(output,
                         [
                             {
                                 'name': 'Professor',
                                 'collaborators': ['Seminar'],
                                 'responsibilities': ['Provide information', 'Get Seminars instructing']
                             }
                         ])

    def test_generate_crc_diagram_without_output_argument(self):
        source = os.path.join(self.test_files, 'python_project', 'professor.py')
        result = self.runner.invoke(main, [source])

        self.assertEqual(result.output, 'Usage: crc-diagram [OPTIONS] SOURCE [OUT]\n\nError: Missing argument "out".\n')

    def test_invalid_format_option(self):
        source = os.path.join(self.test_files, 'python_project', 'professor.py')
        result = self.runner.invoke(main, [source, '--format=epub', 'out.png'])

        self.assertIn('Error: Invalid value for "--format": invalid choice: epub.', result.output)
