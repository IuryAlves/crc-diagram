# coding: utf-8

from svgwrite import Drawing, shapes


class CRCShape(object):

    def __init__(self, x, y, height, width,
                 fill="white",
                 stroke="black",
                 stroke_width=1):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = shapes.Rect(insert=(self.x, self.y),
                                size=(self.width, self.height),
                                fill=fill,
                                stroke_width=stroke_width,
                                stroke=stroke)
        self.horizontal_line = shapes.Line(
            (self.x, 20),
            (self.width, 20),
            stroke_width=1,
            stroke="black"
            )

        self.vertical_line = shapes.Line(
            (self.height, self.height),
            (self.width / 2, 20),
            stroke_width=1,
            stroke="black")

    def draw(self, filename):
        dwg = Drawing(filename)
        dwg.add(self.rect)
        dwg.add(self.horizontal_line)
        dwg.add(self.vertical_line)
        dwg.save()
