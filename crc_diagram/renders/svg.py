# coding: utf-8

from svgwrite import shapes, drawing
from .abstract import AbstractRender


class SvgRender(AbstractRender):
    """
    A class that knows how to render svg.
    """

    def __init__(self, start_x, start_y, height, width, crc_cards, **kwargs):
        super(SvgRender, self).__init__(start_x, start_y, height, width, crc_cards)
        self.fill = kwargs.pop('fill', 'white')
        self.stroke = kwargs.pop('stroke', 'black')
        self.stroke_width = kwargs.pop('stroke_width', 1)
        self.drawing = drawing.Drawing()

    def add_texts(self, texts, x, y):
        if not isinstance(texts, list):
            texts = [texts]
        position_y = 0
        for text in texts:
            self.drawing.add(self.drawing.text(text, insert=(x, y + position_y)))
            position_y += 15

    def get_title_rect(self, x, y):
        return shapes.Rect(insert=(x, y), size=(self.width, 30),
                           fill=self.fill,
                           stroke_width=self.stroke_width,
                           stroke=self.stroke)

    def get_responsibilities_rect(self, x, y, half_width, height_minus_30):
        return shapes.Rect(insert=(x, y + 30),
                           size=(half_width, height_minus_30),
                           fill=self.fill,
                           stroke_width=self.stroke_width,
                           stroke=self.stroke)

    def get_collaborators_rect(self, x, y, half_width, height_minus_30):
        return shapes.Rect(insert=(x + half_width, y + 30),
                           size=(half_width, height_minus_30),
                           fill=self.fill,
                           stroke_width=self.stroke_width,
                           stroke=self.stroke)

    def format_card_name(self, card_name):
        if len(card_name) > 35:
            card_name = card_name[:35] + ' ...'
        return card_name

    def render(self, filename):
        half_width = self.width // 2
        height_minus_30 = self.height - 30
        x, y = self.start_x, self.start_y
        for crc_card in self.crc_cards:
            title_rect = self.get_title_rect(x, y)
            responsibilities_rect = self.get_responsibilities_rect(x, y, half_width, height_minus_30)
            collaborators_rect = self.get_collaborators_rect(x, y, half_width, height_minus_30)
            card_name = self.format_card_name(crc_card.name)

            self.drawing.add(title_rect)
            self.drawing.add(responsibilities_rect)
            self.drawing.add(collaborators_rect)
            self.add_texts(card_name, 20, 20)
            self.add_texts(crc_card.responsibilities, 20, 50)
            self.add_texts(crc_card.collaborators, 160, 50)
        return self.drawing.saveas(filename)
