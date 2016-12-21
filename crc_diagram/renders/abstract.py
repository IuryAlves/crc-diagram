# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class AbstractRender(with_metaclass(ABCMeta)):
    """
    A base render. Must be extended.
    """

    def __init__(self, start_x, start_y, height, width, crc_cards):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width
        self.crc_cards = crc_cards

    @abstractmethod
    def add_texts(self, *args, **kwargs):
        pass  # pragma: no cover

    @abstractmethod
    def get_title_box(self, *args, **kwargs):
        pass  # pragma: no cover

    @abstractmethod
    def get_responsibilities_box(self, *args, **kwargs):
        pass  # pragma: no cover

    @abstractmethod
    def get_collaborators_box(self, *args, **kwargs):
        pass  # pragma: no cover

    @abstractmethod
    def render(self, *args, **kwargs):
        pass  # pragma: no cover
