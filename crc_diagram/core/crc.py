# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


class CRC(object):
    """
    Class that represents a CRC Card.

    :param name: The name of the class.
    :param collaborators: A list of strings containing the collaborators.
    :param responsibilities: A list of strings containing the responsibilities.

    Example::

        crc = CRC('HtmlToMarkdown',
                  collaborators=['ImageUploader'],
                  responsibilities=['Convert html to markdown']
              )

        crc.to_dict()

    And the result::

        {
            'collaborators': ['ImageUploader'],
            'name': 'HtmlToMarkdown',
            'responsibilities': ['Convert html to markdown']
        }

    """
    def __init__(self, name, collaborators=None, responsibilities=None):
        self.name = name
        self.collaborators = collaborators or []
        self.responsibilities = responsibilities or []

    def __repr__(self):
        return '{class_}(name={name},' \
               ' collaborators={collaborators},' \
               'responsibilities={responsibilities})'\
            .format(class_=self.__class__.__name__,
                    name=self.name,
                    collaborators=self.collaborators,
                    responsibilities=self.responsibilities
                    )

    def to_dict(self):
        """
        Return a dict representation of the instance attributes.
        """
        return {
            'name': self.name,
            'collaborators': self.collaborators,
            'responsibilities': self.responsibilities
        }
