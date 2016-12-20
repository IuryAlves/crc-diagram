# coding: utf-8

from __future__ import (
    absolute_import,
)

from crc_diagram.test import CrcTestCase
from crc_diagram.renders import render_to


class AvailableStrategiesTestCase(CrcTestCase):

    def test_unavailable_strategy_raises_exception(self):

        with self.assertRaises(Exception) as e:
            render_to('html', 0, 0, 150, 300, [], 'test.svg')

        self.assertEqual(str(e.exception), 'Strategy html not available. Options are: svg.')
