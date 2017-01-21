# coding: utf-8


from graphviz import Digraph
from crc_diagram.utils import split_by_extension
from crc_diagram.log import logger


class DotRender(object):

    def __init__(self, crc_cards, format='svg'):
        self.format = format
        self.crc_cards = crc_cards
        self.graph = Digraph(comment='CRC Diagram', node_attr={'shape': 'record'}, format=self.format)
        self._init()

    def get_collaborators_rect(self, collaborators):
        return '\l'.join(collaborators)

    def get_responsibilities_rect(self, responsibilities):
        return '\l'.join(responsibilities)

    def get_crc_name_rect(self, crc_name):
        return crc_name

    def create_edges(self, crc):
        for collaborator in crc.collaborators:
            self.graph.edge(crc.name, collaborator)

    def _init(self):
        for index, crc in enumerate(self.crc_cards):
            crc_name = self.get_crc_name_rect(crc.name)
            collaborators = self.get_collaborators_rect(crc.collaborators)
            responsibilities = self.get_responsibilities_rect(crc.responsibilities)

            self.graph.node(crc_name, "{%s|{%s|%s}}" % (crc_name, collaborators, responsibilities))
            self.create_edges(crc)

    def render(self, filename, view=False):
        filename, extension = split_by_extension(filename)
        if extension is None:
            logger.warn('File extension not informed. Getting extension from output format.')
        self.graph.render(filename, view=view)
