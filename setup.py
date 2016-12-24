#!/usr/bin/env python

from setuptools import setup
from os import path


def parse_requirements(requirements_file):
    with open(requirements_file) as fp:
        requirements = map(
          lambda requirement: requirement.replace('==', '>='),
          fp.read().splitlines()
        )
    return list(requirements)


setup(name='crcdiagram',
      version='0.0.1',
      url="https://github.com/IuryAlves/crcdiagram",
      description='Generate Class Responsibility Collaboration (CRC) Diagrams from python code',
      author='Iury Alves',
      author_email='iuryalves20@gmail.com',
      packages=['crc_diagram', 'crc_diagram.core', 'crc_diagram.renders', 'crc_diagram.test'],
      install_requires=parse_requirements(path.join('requirements', 'base.txt')),
      entry_points={
          'console_scripts': [
              'crc_diagram = crc_diagram.__main__:main'
              ]
          }
      )
