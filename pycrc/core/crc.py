# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRC(object):
    """
    class that represents a CRC Card
    """

    def __init__(self, name='', collaborators=None, responsibilities=None):
        self.name = name
        self.collaborators = collaborators or []
        self.responsibilities = responsibilities or []

    def to_dict(self):
        return {
            'collaborators': self.collaborators,
            'responsibilities': self.responsibilities
        }
