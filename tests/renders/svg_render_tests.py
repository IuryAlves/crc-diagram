# coding: utf-8

from __future__ import (
    absolute_import,
)

import tempfile
from xml.etree import ElementTree

from crc_diagram.test import xml, CrcTestCase
from crc_diagram.renders import render_to
from crc_diagram.core import CRC


class SvgRenderTestCase(CrcTestCase):

    def test_svg_render(self):
        crc = CRC(name='parser',
                  responsibilities=['parse things'],
                  collaborators=['uploader'])
        with tempfile.NamedTemporaryFile() as tmp:
            render_to('svg', 0, 0, 150, 300, [crc], tmp.name)
            root = ElementTree.parse(tmp.name).getroot()

        rects = root.findall('svg:rect', xml.svg_namespace)

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
