# coding: utf-8

from svgwrite import Drawing, shapes, text


def svg_render(x, y, height, width, crc, filename,
               fill="white", stroke="black",
               stroke_width=1, crc_name_height=30):

        rect = shapes.Rect(insert=(x, y),
                           size=(width, height),
                           fill=fill,
                           stroke_width=stroke_width,
                           stroke=stroke)

        horizontal_line = shapes.Line((x, crc_name_height),
                                      (width, crc_name_height),
                                      stroke_width=1,
                                      stroke="black")

        vertical_line = shapes.Line((width / 2, height),
                                    (width / 2, crc_name_height),
                                    stroke_width=1,
                                    stroke="black")
        crc_name = text.Text(crc.name, insert=(20, 20))
        crc_responsibility = text.Text(crc.responsibility,
                                       insert=(20, 50))
        crc_collaborators = text.Text(crc.collaborators,
                                      insert=(160, 50))

        dwg = Drawing(filename)
        dwg.add(rect)
        dwg.add(horizontal_line)
        dwg.add(vertical_line)
        dwg.add(crc_name)
        dwg.add(crc_responsibility)
        dwg.add(crc_collaborators)
        dwg.save()
