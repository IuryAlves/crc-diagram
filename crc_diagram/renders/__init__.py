# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from six import string_types
from .svg import SvgRender


available_strategies = {
    'svg': SvgRender
}


class RenderTo(object):

    def __init__(self, strategy, x, y, height, width, **kwargs):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.kwargs = kwargs

        if isinstance(strategy, string_types):
            try:
                strategy = available_strategies[strategy]
            except KeyError:
                raise Exception('Strategy {strategy} not available.'
                                ' Options are {available_strategies}'.format(
                                    strategy=strategy,
                                    available_strategies=available_strategies))
        self.strategy = strategy

    def draw(self, crc_cards, filename):
        strategy = self.strategy(self.x, self.y,
                                 self.height, self.width,
                                 crc_cards, **self.kwargs)
        strategy.render(filename)
