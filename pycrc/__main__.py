# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import argparse
import json
import sys
import pycrc


def _create_parser():
    parser = argparse.ArgumentParser(description='Generete CRC diagrams from python code.')
    parser.add_argument('--raw', type=bool)
    parser.add_argument('source')
    return parser


if __name__ == '__main__':
    args = _create_parser().parse_args()

    if args.raw:
        result = pycrc.py_to_crc(args.source)
        json.dump(result, sys.stdout, indent=4)
