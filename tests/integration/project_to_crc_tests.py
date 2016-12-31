# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram import project_to_crc
from crc_diagram.test import testcase


class ProjectToCrcTestCase(testcase.CrcTestCase):

    def test_project_to_crc(self):
        project_path = join(self.test_files, 'python_project')
        crcs = project_to_crc(project_path)
        self.assertEqual(len(crcs), 5)
