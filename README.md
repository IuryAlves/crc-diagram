# PyCRC

Generate Class Responsibility Collaborator (CRC) Diagrams from python code

[![Coverage Status](https://coveralls.io/repos/github/IuryAlves/pycrc/badge.svg?branch=master)](https://coveralls.io/github/IuryAlves/pycrc?branch=master)
[![Build Status](https://travis-ci.org/IuryAlves/pycrc.svg?branch=master)](https://travis-ci.org/IuryAlves/pycrc)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3802e396ad414648a7f7b04741c92038)](https://www.codacy.com/app/satriani-16/pycrc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=IuryAlves/pycrc&amp;utm_campaign=Badge_Grade)

# Table of contents
1. [What is CRC](#what_is_crc)
2. [Usage](#usage)
3. [Running Tests](#running_tests)
4. [Notes and Documentation](#notes_and_documentation)
5. [Contributing](#contributing)

## What is CRC ? <a name='what_is_crc'></a>

[http://agilemodeling.com/artifacts/crcModel.htm](http://agilemodeling.com/artifacts/crcModel.htm)


## Project Goal

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

The responsability of the class is to convert html files to markdown.
If the html has images, the class uses a colaborator called `image_uploader``
to upload the images to somewhere.

The CRC of this class could be represent as follows:


```
----------------------------------------|
|           HtmlToMarkdown              |
|---------------------------------------|
| Converts html files  | image_uploader |
|  to markdown         |                |
|                      |                |
-----------------------------------------
```

Where "Converts html files to markdown" is the responsability of the class
and "image_uploader" is a colaborator


## Usage <a name='usage'></a>

#### In Command Line

    python -m pycrc --raw=true file

## Running tests <a name='running_tests'></a>

    pip install -r requirements.txt
    tox

## Notes and Documentation <a name='notes_and_documentation'></a>

    TODO

## Contributing <a name='contributing'></a>

    TODO

