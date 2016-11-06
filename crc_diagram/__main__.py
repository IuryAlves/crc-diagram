# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import argparse
import json
import sys
import crc_diagram


def _create_parser():
    parser = argparse.ArgumentParser(description='Generate CRC diagrams from python code.')
    parser.add_argument('--raw', type=bool)
    parser.add_argument('source')
    return parser


if __name__ == '__main__':
    args = _create_parser().parse_args()

    if args.raw:
        result = [crc.to_dict() for crc in crc_diagram.py_to_crc(args.source)]
        json.dump(result, sys.stdout, indent=4)
