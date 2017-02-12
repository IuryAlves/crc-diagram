# coding: utf-8


from graphviz import Digraph
from crc_diagram.utils import split_by_extension
from crc_diagram.log import logger


class DotRender(object):
    """
    Render CRC cards using DOT language.

    :param list crc_cards: A list of :py:data:`CRC` objects.
    :param str format: The format used to save the diagram. Default is png.
    :param dict graph_data: graph attributes, see documentation `here`_.

    .. _here: http://www.graphviz.org/doc/info/attrs.html

    Example::

        from crc_diagram import py_to_crc

        # getting crcs from a file
        crcs = py_to_crc('html_to_markdown.py')

        DotRender(crcs).render('html_to_markdown.png')

    This will save to html_to_markdown.png the diagram

    You can open it passing :py:data:`view=True` to :py:data:`render` method::

        DotRender(crcs).render('html_to_markdown.png', view=True)

    By default :py:class: DotRender uses a directed graph.

    You can customize the graph passing a dictionary to :py:data:`graph_data=graph_data`::

        # create a blue graph
        graph_data = {
            'fillcolor': 'blue',
            'style': 'filled'
        }

        DotRender(crcs, graph_data=graph_data).render(
            'html_to_markdown.png',
            view=True
            )

    Rendered diagram:

    .. image:: _images/blue_card.png

    |
    """
    def __init__(self, crc_cards, format='png', graph_data=None):
        self.format = format
        self.crc_cards = crc_cards
        self.graph_data = {'shape': 'record'}
        self._edges = []  # keep track of the edges

        if graph_data is not None:
            self.graph_data.update(graph_data)

        self.graph = Digraph(
            comment='CRC Diagram',
            node_attr=self.graph_data,
            format=self.format
        )

        self._init()

    @property
    def source(self):
        """
        Returns the DOT source of the :py:data:`self.graph`
        """
        return self.graph.source

    @staticmethod
    def format(texts, format_spec='\l'):

        return format_spec.join(texts)

    def get_edge_direction(self, collaborator, crc_name):
        """
        Check if a collaborator has bidirectional reference::

            A -> B
            B -> A

        :param str collaborator: The collaborator to check against.
        :param str crc_name: The name of the CRC to check against.

        :return direction: both if the collaborator has bidirectional reference
         or single otherwise.
        """
        direction = 'single'
        for crc_card in self.crc_cards:
            if collaborator == crc_card.name and crc_name in crc_card.collaborators:
                direction = 'both'
        return direction

    def edge_already_added(self, crc_name, collaborator):
        """
        Return True if a edge have already been added for that collaborator
        return False otherwise.

        :param str crc_name: The CRC name.
        :param str collaborator: The CRC collaborator.
        """
        return (
            (crc_name, collaborator) in self._edges or
            (collaborator, crc_name) in self._edges
        )

    def create_edges(self, crc):
        """
        Iterate over :py:data:`crc.collaborators` and create a edge
        for each one if the edge hasn't already been created.

        :param CRC crc: A CRC instance.
        """
        for collaborator in crc.collaborators:
            direction = self.get_edge_direction(collaborator, crc.name)
            if not self.edge_already_added(crc.name, collaborator):
                self.graph.edge(crc.name, collaborator, dir=direction)
            self._edges.append((crc.name, collaborator))

    def _init(self):
        """
        Iterate over :py:data:`self.crc_cards` and create a graph node
        for each one,then calls :py:data:`create_edges` to create the edges
        for each node.
        """
        for index, crc in enumerate(self.crc_cards):
            crc_name = crc.name

            if crc.collaborators:
                collaborators = DotRender.format(crc.collaborators)
            else:
                collaborators = "NO-COLLABORATORS"

            if crc.responsibilities:
                responsibilities = DotRender.format(crc.responsibilities)
            else:
                responsibilities = "NO-RESPONSIBILITIES"

            self.graph.node(crc_name, "{%s|{%s|%s}}" % (
                crc_name,
                collaborators,
                responsibilities
            ))
            self.create_edges(crc)

    def render(self, filename, view=False):
        """
        Render :py:data:`self.graph`.

        :param str filename: The filename where the diagram will be saved.
        :param bool view: Set to True to open the rendered diagram.
        """
        filename, extension = split_by_extension(filename)
        if extension is not None and extension != self.format:
            logger.warn(
                'File extension is different from --format. '
                'The file name is {filename}.{extension} '
                'but it will be saved as {format}'.format(
                    filename=filename,
                    extension=extension,
                    format=self.format
                )
            )
        self.graph.render(filename, view=view)
