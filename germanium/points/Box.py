from germanium.impl._load_script import load_script
from .Point import Point


class Box(object):
    def __init__(self, selector):
        self._selector = selector
        self._box = None

    def top_left(self):
        if not self._box:
            self.get_element_box()

        return Point(self._box['left'],
                     self._box['top'])

    def top_right(self):
        if not self._box:
            self.get_element_box()

        return Point(self._box['right'],
                     self._box['top'])

    def bottom_left(self):
        if not self._box:
            self.get_element_box()

        return Point(self._box['left'],
                     self._box['bottom'])

    def bottom_right(self):
        if not self._box:
            self.get_element_box()

        return Point(self._box['right'],
                     self._box['bottom'])

    def get_element_box(self):
        from germanium.static import S, js
        code = load_script(__name__, 'box.min.js')

        top, right, bottom, left, width, height = js(code, S(self._selector).element())

        self._box = {
            "top": top,
            "right": right,
            "bottom": bottom,
            "left": left,
            "width": width,
            "height": height
        }

        print("found box %s " % self._box)

        return self._box
