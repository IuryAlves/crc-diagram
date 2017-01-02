# coding: utf-8

from __future__ import (
    absolute_import,
)

import tempfile
from xml.etree import ElementTree

from crc_diagram.test import xml
from crc_diagram.test.testcase import CrcTestCase
from crc_diagram.renders import render_to
from crc_diagram.core import CRC


class SvgRenderTestCase(CrcTestCase):

    def test_svg_render_multiple_crc_cards(self):
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
            )
        ]

        with tempfile.NamedTemporaryFile() as tmp:
            render_to('svg', 0, 0, 150, 300, crcs, tmp.name)
            element_root = ElementTree.parse(tmp.name).getroot()
        elements = element_root.findall('svg:rect', xml.svg_namespace)

        self.assertItemsEqual(
            [element.attrib for element in elements],
            [{'fill': 'white',
              'height': '30',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '300',
              'x': '0',
              'y': '0'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '0',
              'y': '30'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '150',
              'y': '30'},
             {'fill': 'white',
              'height': '30',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '300',
              'x': '0',
              'y': '180'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '0',
              'y': '210'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '150',
              'y': '210'},
             {'fill': 'white',
              'height': '30',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '300',
              'x': '0',
              'y': '360'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '0',
              'y': '390'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '150',
              'y': '390'},
             {'fill': 'white',
              'height': '30',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '300',
              'x': '0',
              'y': '540'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '0',
              'y': '570'},
             {'fill': 'white',
              'height': '120',
              'stroke': 'black',
              'stroke-width': '1',
              'width': '150',
              'x': '150',
              'y': '570'}]
        )

    def test_card_with_long_name_should_be_sliced(self):
        crc = CRC(
            name='Awesome Very very very loooooooong name',
            responsibilities=['Another awesome very very very long responsibility'],
            collaborators=['Yet another awesome very very very long collaborator']
        )

        with tempfile.NamedTemporaryFile() as tmp:
            render_to('svg', 0, 0, 150, 300, [crc], tmp.name)
            element_root = ElementTree.parse(tmp.name).getroot()
        elements = element_root.findall('svg:text', xml.svg_namespace)
        crc_name, crc_responsibilities, crc_collaborators = (element.text for element in elements)

        self.assertEqual(crc_name, 'Awesome Very very ...')
        self.assertEqual(crc_responsibilities, 'Another awesome v ...')
        self.assertEqual(crc_collaborators, 'Yet another aweso ...')

    def test_svg_render(self):
        crc = CRC(name='parser',
                  responsibilities=['parse things'],
                  collaborators=['uploader'])
        with tempfile.NamedTemporaryFile() as tmp:
            render_to('svg', 0, 0, 150, 300, [crc], tmp.name)
            element_root = ElementTree.parse(tmp.name).getroot()

        rects = element_root.findall('svg:rect', xml.svg_namespace)

        self.assertDictEqual(rects[0].attrib,
                             {'fill': 'white',
                              'height': '30',
                              'stroke': 'black',
                              'stroke-width': '1',
                              'width': '300',
                              'x': '0',
                              'y': '0'
                              })

        self.assertDictEqual(rects[1].attrib,
                             {'fill': 'white',
                              'height': '120',
                              'stroke': 'black',
                              'stroke-width': '1',
                              'width': '150',
                              'x': '0',
                              'y': '30'})

        self.assertDictEqual(rects[2].attrib,
                             {'fill': 'white',
                              'height': '120',
                              'stroke': 'black',
                              'stroke-width': '1',
                              'width': '150',
                              'x': '150',
                              'y': '30'})
