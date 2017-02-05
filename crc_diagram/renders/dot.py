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
        return self.graph.source

    def get_collaborators_box(self, collaborators):
        return '\l'.join(collaborators)

    def get_responsibilities_box(self, responsibilities):
        return '\l'.join(responsibilities)

    def get_crc_name_box(self, crc_name):
        return crc_name

    def get_edge_direction(self, collaborator, crc_name):
        direction = 'single'
        for crc_card in self.crc_cards:
            if collaborator == crc_card.name and crc_name in crc_card.collaborators:
                direction = 'both'
        return direction

    def edge_already_added(self, current_crc_name, current_collaborator):
        return (
            (current_crc_name, current_collaborator) in self._edges or
            (current_collaborator, current_crc_name) in self._edges
        )

    def create_edges(self, crc):
        for collaborator in crc.collaborators:
            direction = self.get_edge_direction(collaborator, crc.name)
            if not self.edge_already_added(crc.name, collaborator):
                self.graph.edge(crc.name, collaborator, dir=direction)
            self._edges.append((crc.name, collaborator))

    def _init(self):
        for index, crc in enumerate(self.crc_cards):
            crc_name = self.get_crc_name_box(crc.name)
            collaborators = self.get_collaborators_box(crc.collaborators)
            responsibilities = self.get_responsibilities_box(crc.responsibilities)

            self.graph.node(crc_name, "{%s|{%s|%s}}" % (
                crc_name,
                collaborators,
                responsibilities
            ))
            self.create_edges(crc)

    def render(self, filename, view=False):
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
