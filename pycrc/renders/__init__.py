# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class Render(object):

    def __init__(self, strategy, x, y, height, width, **kwargs):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.strategy = strategy
        self.kwargs = kwargs

    def draw(self, crc, filename):
        self.strategy(self.x, self.y, self.height,
                      self.width, crc, filename,
                      **self.kwargs)
