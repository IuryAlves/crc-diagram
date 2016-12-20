# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from six import string_types
from .svg import SvgRender
from .abstract import AbstractRender


__all__ = [
    'available_renders',
    'render_to'
    'SvgRender',
    'AbstractRender'
]


available_renders = {
    'svg': SvgRender
}


def render_to(strategy, x, y, height, width, crc_cards, filename, **kwargs):

    if isinstance(strategy, string_types):
        try:
            strategy = available_renders[strategy]
        except KeyError:
            options = ','.join(available_renders.keys())
            raise Exception('Strategy {strategy} not available.'
                            ' Options are: {options}.'.format(
                                strategy=strategy,
                                options=options))

    strategy(x, y, height, width,
             crc_cards, **kwargs).render(filename)
