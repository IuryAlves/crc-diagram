# coding: utf-8

from __future__ import (
    absolute_import,
)

from crc_diagram.test import CrcTestCase
from crc_diagram.renders import RenderTo


class AvailableStrategiesTestCase(CrcTestCase):

    def test_unavailable_strategy_raises_exception(self):

        with self.assertRaises(Exception) as e:
            RenderTo('html', 0, 0, 150, 300)

        self.assertEqual(str(e.exception), 'Strategy html not available. Options are: svg.')
