# coding: utf-8

"""
Simple log configuration using coloredlogs.
"""

import logging

import coloredlogs

__all__ = [
    'logger'
]


FORMAT = '%(levelname)s %(message)s'

logger = logging.getLogger()
coloredlogs.install(level='INFO', fmt=FORMAT)
