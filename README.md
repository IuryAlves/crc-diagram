# CRCDiagram  

Generate Class Responsibility Collaboration (CRC) Diagrams from python code using [Dot language](http://www.graphviz.org/doc/info/lang.html)

[![Coverage Status](https://coveralls.io/repos/github/IuryAlves/CRCDiagram/badge.svg?branch=master)](https://coveralls.io/github/IuryAlves/CRCDiagram?branch=master)
[![Build Status](https://travis-ci.org/IuryAlves/CRCDiagram.svg?branch=master)](https://travis-ci.org/IuryAlves/CRCDiagram)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

# Table of contents
1. [What is CRC](#what_is_crc)
2. [Project Goal](#project_goal)
3. [Installing](#installing)
4. [Usage](#usage)
6. [Notes and Documentation](#notes_and_documentation)
7. [Contributing](#contributing)


## What is CRC ? <a name='what_is_crc'></a>

A Class Responsibility Collaboration (CRC) is a collection of standard index cards that have been divided into three sections.

![CRC Card](docs/crc_card.png)


A class represents a collection of similar objects, a responsibility is something that a class knows or does,
 and a collaborator is another class that a class interacts with to fulfill its responsibilities.


[More information](http://agilemodeling.com/artifacts/crcModel.htm)


## Project Goal <a name='project_goal'></a>

Imagine that your project have the class HtmlToMarkdown.

```python

class HtmlToMarkdown(object):
    """
    Converts html files to markdown.
    """

    def __init__(self, image_uploader):
        self.image_uploader = image_uploader

    # code
```

The responsibility of the class is to convert html files to markdown, if the html has images, the class uses a collaborator called `image_uploader`
to upload the images to somewhere.

Where "Converts html files to markdown" is the responsibility of the class
and "image_uploader" is a collaborator


So to make CRCDiagram generate the diagram, you add `annotations` to the docstring in the class:


```python

class HtmlToMarkdown(object):
    """
    @responsibility: Converts html files to markdown.
    @collaborator: image_uploader
    """

    def __init__(self, image_uploader):
        self.image_uploader = image_uploader

    # code
```

The output of the CRC generated will be the following:

![CRC Card](docs/crc_card.png)


## Installing <a name='installing'></a>

  * Install [Dot](http://www.graphviz.org/Download..php)
  * Install the requirements


    pip install -r requirements/base.txt


## Usage <a name='usage'></a>

    TODO

## Notes and Documentation <a name='notes_and_documentation'></a>

    TODO

## Contributing <a name='contributing'></a>

See [contributing](CONTRIBUTING.md) guide.
