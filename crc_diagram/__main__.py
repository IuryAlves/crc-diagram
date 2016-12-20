# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import json
import sys
import os
import click
import crc_diagram
from crc_diagram.renders import render_to


@click.command(name='pycrc')
@click.argument('source')
@click.argument('out', required=False)
@click.option('--raw', type=bool)
@click.option('--render', default='svg', type=str)
def main(source, out, raw, render):

    if os.path.isdir(source):
        crc_cards = crc_diagram.project_to_crc(source)
    else:
        crc_cards = crc_diagram.py_to_crc(source)

    if raw:
        out = out or sys.stdout
        json.dump([crc.to_dict() for crc in crc_cards], out, indent=4)
    else:
        if out is None:
            raise click.UsageError('Missing argument "out".')
        render_to(render, 0, 0, 150, 300, crc_cards, out)

if __name__ == '__main__':
    main()
