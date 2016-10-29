# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRC(object):
    """
    class that represents a CRC Card
    """

    def __init__(self, name='', colaborators=None, responsibility=''):
        self.name = name
        self.colaborators = colaborators or []
        self.responsibility = responsibility

    def to_dict(self):
        return {
            'name': self.name,
            'colaborators': self.colaborators,
            'responsibility': self.responsibility
        }
