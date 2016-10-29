# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRC(object):
    """
    class that represents a CRC Card
    """

    def __init__(self, name='', collaborators=None, responsibility=''):
        self.name = name
        self.collaborators = collaborators or []
        self.responsibility = responsibility

    def to_dict(self):
        return {
            'name': self.name,
            'collaborators': self.collaborators,
            'responsibility': self.responsibility
        }
