# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import tempfile
from xml.etree import ElementTree

from crc_diagram.test import xml, CrcTestCase
from crc_diagram.renders import Render, svg
from crc_diagram.core.crc import CRC


class SvgRenderTestCase(CrcTestCase):

    def test_svg_render_rect(self):
        crc = CRC(name='parser',
                  responsibilities=['parse things'],
                  collaborators=['uploader'])
        with tempfile.NamedTemporaryFile() as tmp:
            Render(svg.svg_render, 0, 0, 150, 300).draw(crc, tmp.name)
            root = ElementTree.parse(tmp.name).getroot()

        element = root.findall('svg:rect', xml.svg_namespace)[0]

        self.assertEqual(element.attrib,
                         {'fill': 'white',
                          'height': '150',
                          'stroke': 'black',
                          'stroke-width': '1',
                          'width': '300',
                          'x': '0',
                          'y': '0'
                          })
