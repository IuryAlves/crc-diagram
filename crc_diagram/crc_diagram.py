# coding: utf-8

from __future__ import (
    unicode_literals,
    absolute_import
)

import os

from crc_diagram.core.parsers import PythonParser


def to_crc(fp, parser_class=PythonParser, **parser_class_kwargs):
    """
    Shortcut to :py:data:`PythonParser(fp).parse().result`.

    :param: file|str fp: The file to extract the CRCs.
     Can be either a file path as string or a file like object.
    :param: BaseParser parser_class: The parser class.
    :param: parser_class_kwargs: additional keyword arguments to :py:data:`parser_class`
    :return: A list of CRCs

    Example::

        to_crc('html_to_markdown.py')

    Will return::

        [
        CRC(name=HtmlToMarkdown,
            kind=class,
            collaborators=['ImageUploader'],
            responsibilities=['Convert html files to markdown']
        ),
        CRC(name=ImageUploader,
            kind=class,
            collaborators=[],
            responsibilities=['Store images in the cloud'])
        ]

    """
    return parser_class(fp, **parser_class_kwargs).parse().result


def folder_to_crc(path, parser_class=PythonParser, **parser_class_kwargs):
    """
    Iterate in all files in :py:data:`path` and call :py:data:`to_crc`
    to each one.

    :param str path: The folder path.
    :param BaseParser parser_class: The parser class.
    :param: parser_class_kwargs: additional keyword arguments to :py:data:`parser_class`
    :return: A list of CRCs of all files in :py:data:`path`.

    Example::

        from os.path import join

        folder = join('crc_diagram', 'testing', 'files', 'python_project')
        folder_to_crc(folder)

    And the result::

        [
        CRC(name=Student,
           kind=class,
           collaborators=['Enrollment'],
           responsibilities=['Validate Identifying info', 'Provide list of seminars taken']
        ),
        CRC(name=Seminar,
            kind=class,
            collaborators=['Student', 'Professor'],
            responsibilities=['List transcripts',
                              'Drop student',
                              'Add student',
                              'Get enrolled students']
        ),
        # ...

    """
    crcs = []
    for _, _, files in os.walk(path):
        for file_ in files:
            file_path = os.path.join(path, file_)
            crcs.extend(to_crc(file_path, parser_class=parser_class))
    return crcs
