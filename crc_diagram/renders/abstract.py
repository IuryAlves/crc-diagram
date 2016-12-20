# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

from abc import ABCMeta, abstractmethod


class AbstractRender(object):
    """
    A base render. Must be extended.
    """
    __metaclass__ = ABCMeta

    def __init__(self, start_x, start_y, height, width, crc_cards):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width
        self.crc_cards = crc_cards

    @abstractmethod
    def add_texts(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_title_rect(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_responsibilities_rect(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_collaborators_rect(self, *args, **kwargs):
        pass

    @abstractmethod
    def render(self, *args, **kwargs):
        pass
