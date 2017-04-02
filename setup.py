#!/usr/bin/env python

import ast
import re
import subprocess
import platform
import sys
import traceback
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


def install_system_package(package_name):
    command_map = {
        'fedora': 'yum install dot',
        'ubuntu': 'apt-get install graphviz',
        'debian': 'apt install dot',
        'mac': 'brew install dot'
    }
    command = command_map[platform.dist()[0]]

    subprocess.check_call(['sudo', command])


print('In order to render the diagrams dot must be installed.'
      'crc-diagram will try to install dot using your system`s package'
      ' manager.')

try:
    install_system_package('dot')
except Exception:
    print('Could not install dot. You must install dot  by your own'
          'using your system`s package manager or downloading here:'
          ' http://www.graphviz.org/Download..php')

    sys.stderr.write(traceback.format_exc())

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
