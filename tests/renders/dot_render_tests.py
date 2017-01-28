# coding: utf-8

from __future__ import (
    absolute_import,
)

from os.path import exists, join, abspath, curdir
from os import remove
from crc_diagram.testing.testcase import CrcTestCase
from crc_diagram.renders import DotRender
from crc_diagram.core import CRC


class DotRenderTestCase(CrcTestCase):

    def test_use_extension_from_format(self):
        crcs = [
            CRC(
                name='Enrollment',
                responsibilities=['Get students', 'Get seminar', 'Get Final Grade'],
                collaborators=['Seminar']
            ),
        ]

        DotRender(crcs, format='svg').render('crc')

        self.assertTrue(exists(join(abspath(curdir), 'crc.svg')))

        remove('crc.svg')
        remove('crc')

    def test_render_multiple_crc_cards(self):
        crcs = [
            CRC(
                name='Enrollment',
                responsibilities=['Get students', 'Get seminar', 'Get Final Grade'],
                collaborators=['Seminar']
            ),
            CRC(
                name='Professor',
                collaborators=['Seminar'],
                responsibilities=['Provide information', 'Get Seminars instructing']
            ),
            CRC(
                name='Seminar',
                collaborators=['Student', 'Professor'],
                responsibilities=['List transcripts', 'Drop student', 'Add student', 'Get enrolled students']
            ),
            CRC(
                name='Transcript',
                collaborators=['Student', 'Seminar', 'Professor', 'Enrollment'],
                responsibilities=['Determine average mark']
            ),
        ]

        dot = DotRender(crcs, format='svg')
        self.assertMultiLineEscapeCharsEqual(
            dot.graph.source,
            '''
            // CRC Diagram
            digraph {
                node [shape=record]
                    Enrollment [label="{Enrollment|{Seminar|Get students\lGet seminar\lGet Final Grade}}"]
                        Enrollment -> Seminar
                    Professor [label="{Professor|{Seminar|Provide information\lGet Seminars instructing}}"]
                        Professor -> Seminar
                    Seminar [label="{Seminar|{Student\lProfessor|List transcripts\lDrop student\lAdd student\lGet
                    enrolled students}}"]
                        Seminar -> Student
                        Seminar -> Professor
                    Transcript [label="{Transcript|{Student\lSeminar\lProfessor\lEnrollment|Determine average mark}}"]
                        Transcript -> Student
                        Transcript -> Seminar
                        Transcript -> Professor
                        Transcript -> Enrollment
            }
            ''')
