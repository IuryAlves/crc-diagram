# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRC(object):
    """
    Class that represents a CRC Card.

    :param str name: The name of the class.
    :param str kind: The kind of the CRC. Default is 'class'
    :param list collaborators: A list of strings containing the collaborators.
    :param list responsibilities: A list of strings containing the responsibilities.

    Example::

        crc = CRC('HtmlToMarkdown',
                  kind='class',
                  collaborators=['ImageUploader'],
                  responsibilities=['Convert html to markdown']
              )

        crc.to_dict()

    And the result::

        {
            'collaborators': ['ImageUploader'],
            'name': 'HtmlToMarkdown',
            'kind': 'class',
            'responsibilities': ['Convert html to markdown']
        }

    """

    def __init__(self, name, kind='class',
                 collaborators=None,
                 responsibilities=None):
        self.name = name
        self.kind = kind
        self.collaborators = collaborators or []
        self.responsibilities = responsibilities or []

    def __repr__(self):
        template = (
            '{class_}(name={name},',
            ' kind={kind},',
            ' collaborators={collaborators},',
            'responsibilities={responsibilities})'
        )

        return ''.join(template).format(
            class_=self.__class__.__name__,
            name=self.name,
            kind=self.kind,
            collaborators=self.collaborators,
            responsibilities=self.responsibilities
        )

    def to_dict(self):
        """
        Return a dict representation of the instance attributes.
        """
        return {
            'name': self.name,
            'kind': self.kind,
            'collaborators': self.collaborators,
            'responsibilities': self.responsibilities
        }
