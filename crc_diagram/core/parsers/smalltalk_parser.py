# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from crc_diagram.core.crc import CRC
from .base_parser import BaseParser


class SmallTalkParser(BaseParser):

    def parse(self):
        self.current_crc = CRC(name='')
        for line in self.stream.read().splitlines():
            self.get_collaborator(line)
            self.get_responsibility(line)
        self._crcs.append(self.current_crc)
        return self
