# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from os.path import join
from crc_diagram import folder_to_crc
from crc_diagram.testing import testcase


class ProjectToCrcTestCase(testcase.CrcTestCase):

    def test_project_to_crc(self):
        project_path = join(self.test_files, 'python_project')
        crcs = folder_to_crc(project_path)
        self.assertEqual(len(crcs), 10)
