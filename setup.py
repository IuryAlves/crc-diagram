#!/usr/bin/env python

import ast
import re
from setuptools import setup
from os.path import join

_version_re = re.compile(r'__version__\s+=\s+(.*)')


def parse_requirements(requirements_file):
    with open(requirements_file) as fp:
        requirements = map(
          lambda requirement: requirement.replace('==', '>='),
          fp.read().splitlines()
        )
    return list(requirements)


def get_version(file_path):
    with open(file_path) as fp:
        return str(ast.literal_eval(_version_re.search(
            fp.read()).group(1)))


setup(name='crc-diagram',
      version=get_version(join('crc_diagram', '__init__.py')),
      url="https://github.com/IuryAlves/crcdiagram",
      description='Generate Class Responsibility Collaboration (CRC) Diagrams from python code',
      author='Iury Alves',
      author_email='iuryalves20@gmail.com',
      packages=['crc_diagram',
                'crc_diagram.core',
                'crc_diagram.renders',
                'crc_diagram.testing',
                'crc_diagram.testing.files',
                'crc_diagram.core.parsers'],
      install_requires=parse_requirements(join('requirements', 'base.txt')),
      entry_points={
          'console_scripts': [
              'crc-diagram = crc_diagram.__main__:main'
              ]
          }
      )
