# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import argparse
import json
import sys
import os
from itertools import chain
import crc_diagram
from crc_diagram.renders import RenderTo


def _create_parser():
    parser = argparse.ArgumentParser(description='Generate CRC diagrams from python code.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--raw', type=bool)
    group.add_argument('--render', default='svg')
    parser.add_argument('source')
    parser.add_argument('--out', default=sys.stdout)
    return parser


if __name__ == '__main__':
    args = _create_parser().parse_args()
    source = args.source
    out = args.out
    if os.path.isdir(source):
        crc_cards = chain.from_iterable(crc_diagram.project_to_crc(source))
    else:
        crc_cards = crc_diagram.py_to_crc(source)

    if args.raw:
        json.dump([crc.to_dict() for crc in crc_cards], out, indent=4)
    else:
        RenderTo('svg', 0, 0, 150, 300).draw(crc_cards, out)
