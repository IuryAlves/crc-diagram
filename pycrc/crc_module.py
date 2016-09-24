# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRCModule(object):
    """
    class that represents a python module
    """

    def __init__(self, name, colaborators=None, responsability=''):
        self.name = name
        self.colaborators = colaborators or []
        self.responsability = responsability

    def to_dict(self):
        return {
            'name': self.name,
            'colaborators': self.colaborators,
            'responsability': self.responsability
        }
