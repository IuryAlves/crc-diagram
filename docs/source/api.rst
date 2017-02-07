API
===

High Level API
--------------
.. module:: crc_diagram
.. autofunction:: to_crc(fp, parser_class=PythonParser, **parser_class_kwargs)
.. autofunction:: folder_to_crc(path, parser_class=PythonParser, **parser_class_kwargs)

Core
----
.. module:: crc_diagram.core
.. autoclass:: CRC
   :members:

Parsers
-------

.. module:: crc_diagram.core.parsers
.. autoclass:: PythonParser(stream, responsibility_pattern, collaborator_pattern)
   :members: parse


Renders
-------

.. module:: crc_diagram.renders
.. autoclass:: DotRender
