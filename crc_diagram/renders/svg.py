# coding: utf-8

from svgwrite import Drawing, shapes, text


def _add_contents(drawing, contents, x, y):
    position_y = 0
    for collaborator in contents:
        drawing.add(drawing.text(collaborator, insert=(x, y + position_y)))
        position_y += 15


def svg_render(x, y, height, width, crc, filename, fill="white",
               stroke="black", stroke_width=1, crc_name_height=30):

    half_width = width // 2
    height_minus_30 = height - crc_name_height
    title_rect = shapes.Rect(insert=(x, y),
                             size=(width, crc_name_height),
                             fill=fill,
                             stroke_width=stroke_width,
                             stroke=stroke)
    responsibilities_rect = shapes.Rect(insert=(x, y + crc_name_height),
                                        size=(half_width, height_minus_30),
                                        fill=fill,
                                        stroke_width=stroke_width,
                                        stroke=stroke
                                        )
    collaborators_rect = shapes.Rect(insert=(x + half_width, y + crc_name_height),
                                     size=(half_width, height_minus_30),
                                     fill=fill,
                                     stroke_width=stroke_width,
                                     stroke=stroke)
    crc_name = text.Text(crc.name[:35] + ' ...', insert=(20, 20))

    dwg = Drawing(filename)
    dwg.add(title_rect)
    dwg.add(responsibilities_rect)
    dwg.add(collaborators_rect)
    dwg.add(crc_name)
    _add_contents(dwg, crc.responsibilities, 20, 50)
    _add_contents(dwg, crc.collaborators, 160, 50)
    dwg.save()
