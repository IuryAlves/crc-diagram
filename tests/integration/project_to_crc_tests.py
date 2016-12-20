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
        project_path = join(self.test_files, 'project')
        crcs = project_to_crc(project_path)
        crc_0, crc_1, crc_2 = crcs[:3]

        self.assertEqual(len(crcs), 5)
        self.assertDictEqual(crc_0.to_dict(), {
            'collaborators': ['Seminar'],
            'name': 'Enrollment',
            'responsibilities':
                ['Get students', 'Get seminar', 'Get Final Grade']
        })
        self.assertDictEqual(crc_1.to_dict(), {
            'collaborators': ['Seminar'],
            'name': 'Professor',
            'responsibilities':
                ['Provide information', 'Get Seminars instructing']
        })
        self.assertDictEqual(crc_2.to_dict(), {
            'collaborators': ['Student', 'Professor'],
            'name': 'Seminar',
            'responsibilities':
                ['List transcripts', 'Drop student',
                 'Add student', 'Get enrolled students']
        })
