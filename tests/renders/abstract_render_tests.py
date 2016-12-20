# coding: utf-8

from __future__ import (
    absolute_import,
)

from crc_diagram.test import CrcTestCase
from crc_diagram.renders import AbstractRender


class SvgRenderTestCase(CrcTestCase):

    def test_abstract_render(self):

        class Render(AbstractRender):
            pass

        with self.assertRaises(TypeError):
            Render(0, 0, 300, 150, [])
