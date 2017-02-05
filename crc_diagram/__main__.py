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
from crc_diagram.renders import DotRender, FORMATS
from crc_diagram.utils import path_to_stream

click.disable_unicode_literals_warning = True


@click.command(name='crc-diagram')
@click.argument('source')
@click.argument('out', required=False)
@click.option('--raw', '-r', type=bool,
              is_flag=True, help='Return the CRC cards as json.')
@click.option('--view', '-v', default=False, type=bool,
              help='Open the output.', is_flag=True)
@click.option('--format', default='png', type=click.Choice(FORMATS),
              help='format that output will be saved. Default is png.')
def main(source, out, raw, format, view):
    """
    Generate CRCDiagrams from SOURCE saving they as OUT.
    \n
    The default output format is png.
    \n
    Example:\n
    crc-diagram source_file.py output.png
    """
    if os.path.isdir(source):
        crc_cards = crc_diagram.project_to_crc(source)
    else:
        crc_cards = crc_diagram.py_to_crc(source)

    if raw:
        out = path_to_stream(out or sys.stdout, 'w')
        json.dump([crc.to_dict() for crc in crc_cards], out, indent=4)
    else:
        if out is None:
            raise click.UsageError('Missing argument "out".')
        DotRender(crc_cards, format=format).render(out, view=view)

if __name__ == '__main__':
    main()  # pragma: no cover
