crc-diagram
===========

![image1](https://coveralls.io/repos/github/IuryAlves/crc-diagram/badge.svg?branch=master) ![image2](https://travis-ci.org/IuryAlves/crc-diagram.svg?branch=master) ![image3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)

# Table of contents

1.  [What is CRC](#what_is_crc)
2.  [How it works](#how_it_works)
3.  [Installing](#installing)
4.  [Full documentation](https://iuryalves.github.io/crc-diagram)

crc-diagram is a generator of Class Responsibility Collaboration diagrams in python (more languages will be available soon) using [DOT language](http://www.graphviz.org/doc/info/lang.html).


<a name='what_is_crc'></a>
## What is CRC?

A Class Responsibility Collaboration (CRC) is a collection of standard index cards that have been divided into three sections.

![image](http://agilemodeling.com/images/models/crcCardLayout.jpg)

A class represents a collection of similar objects, a responsibility is something that a class knows or does, and a collaborator is another class that a class interacts with to fulfill its responsibilities.

[More information](http://agilemodeling.com/artifacts/crcModel.htm).

<a name='how_it_works'></a>
## How it works

Suppose that you have a project with two classes: HtmlToMarkdown and ImageUploader.

HtmlToMarkdown converts html files to markdown files, but HtmlToMarkdown does not know what to do with images. So it uses a collaborator called ImageUploader. ImageUploader knows how to store images in the cloud.

These classes could be write as follows:

```python
class HtmlToMarkdown(object):

   def __init__(self, image_uploader):
      self.image_uploader = image_uploader


class ImageUploader(object):
   pass
```

To make `crc-diagram` generate the CRC cards just add docstrings to the classes with these notations:

```python
class HtmlToMarkdown(object):
   """
   @collaborator: ImageUploader
   @responsibility: Convert html files to markdown
   """
   def __init__(self, image_uploader):
      self.image_uploader = image_uploader


class ImageUploader(object):
   """
   @responsibility: Store images in the cloud
   """
   pass
```

> Any of the notations can be ignored, as you can see in ImageUploader and you can add more than one collaborator or responsibility.

Save this code as markdown\_converter.py and run the following command:

    crc-diagram markdown_converter.py markdown_converter.png --view

This command will extract the CRC Cards and render as png. The `--view` option is to open the rendered diagram.

And the result is:

![image4](https://s27.postimg.org/6l3wauu4j/markdown_converter.png)

<a name='installing'></a>
## Installing


You can get the library directly from PyPI::

   pip install crc-diagram



To render the diagrams you need to install dot:

* Ubuntu/Debian::

   apt-get update && apt-get install graphviz

* Fedora/CentOS::

   yum install graphviz

