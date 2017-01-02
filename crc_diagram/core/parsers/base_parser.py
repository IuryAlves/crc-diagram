# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from abc import ABCMeta, abstractmethod
from six import with_metaclass
from crc_diagram.core.patterns import COLLABORATOR_PATTERN, RESPONSIBILITY_PATTERN
from crc_diagram import utils


class BaseParser(with_metaclass(ABCMeta)):

    def __init__(self, path_or_stream,
                 collaborator_pattern=COLLABORATOR_PATTERN,
                 responsibility_pattern=RESPONSIBILITY_PATTERN):
        super(BaseParser, self).__init__()
        self.stream = utils.path_to_stream(path_or_stream)
        self.responsibility_pattern = responsibility_pattern
        self.collaborator_pattern = collaborator_pattern
        self._crcs = []
        self.current_crc = None

    @abstractmethod
    def parse(self):
        pass  # pragma: no cover

    @property
    def result(self):
        return [crc for crc in self._crcs]

    def get_responsibility(self, string):
        responsibility = self._get_annotation(
            string,
            self.responsibility_pattern
        )
        if responsibility:
            self.current_crc.responsibilities.append(responsibility)

    def get_collaborator(self, string):
        collaborator = self._get_annotation(string, self.collaborator_pattern)
        if collaborator:
            self.current_crc.collaborators.append(collaborator)

    def _get_annotation(self, string, pattern):
        annotation = pattern.match(string)
        return annotation.group(1).strip() if annotation is not None else None
