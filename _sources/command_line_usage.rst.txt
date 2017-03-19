Command Line Usage
==================


-----------
Basic Usage
-----------

The simplest way to use the command line is specifying a *source* and an *output*::


    crc-diagram source_file.py output.png


*source* can be a folder::

    crc-diagram source_folder/ output.png


--------------------------
Changing the output format
--------------------------

The default output format is png. You can use any format that is accepted by DOT::


    crc-diagram source_file.py output.svg --format=svg


Or::


    crc-diagram source_file.py output.pdf --format=pdf


You can see `here`_ the list of accepted formats.


.. _here: http://www.graphviz.org/doc/info/output.html



.. note:: crc-diagram does not care about file extensions. If you are saving a file with :code:`--format=pdf` and the
          filename is output.png the file format still will be pdf.


----------------------------
Viewing the rendered diagram
----------------------------

To view the output file you can add :code:`--view` or the shortcut :code:`-v` to the cli, for example::

    crc-diagram source_file.py output.png --view


--------
Raw CRCs
--------

You can use crc-diagram to output just the CRC structure as json::

    crc-diagram source_file.py --raw


Or you can use the shortcut :code:`-r`::

    crc-diagram source_file.py -r


And the output is::

    [
        {
            "name": "CRC Card Name",
            "collaborators": [...],
            "responsibilities": [...]
        },
        {
            "name": "Another CRC Card Name",
            "collaborators": [...],
            "responsibilities": [...]
        }
    ]


You can specify a output to the json::


    crc-diagram source_file.py output.json --raw


`Next >>`_

.. _Next >>: api.html 
