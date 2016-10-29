# coding: utf-8

from svgwrite import Drawing, shapes


class SvgRender(object):

    def __init__(self, x, y,
                 height,
                 width,
                 fill="white",
                 stroke="black",
                 stroke_width=1,
                 crc_name_height=30):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crc_name_height = crc_name_height

        self.rect = shapes.Rect(insert=(self.x, self.y),
                                size=(self.width, self.height),
                                fill=fill,
                                stroke_width=stroke_width,
                                stroke=stroke)
        self.horizontal_line = shapes.Line(
            (self.x, self.crc_name_height),
            (self.width, self.crc_name_height),
            stroke_width=1,
            stroke="black"
            )

        self.vertical_line = shapes.Line(
            (self.width / 2, self.height),
            (self.width / 2, self.crc_name_height),
            stroke_width=1,
            stroke="black")

    def draw(self, crc, filename):
        dwg = Drawing(filename)
        dwg.add(self.rect)
        dwg.add(self.horizontal_line)
        dwg.add(self.vertical_line)
        dwg.add(dwg.text(crc.name, insert=(20, 20)))
        dwg.add(dwg.text(crc.responsability, insert=(20, 50)))
        dwg.add(dwg.text(crc.colaborators, insert=(160, 50)))
        dwg.save()
