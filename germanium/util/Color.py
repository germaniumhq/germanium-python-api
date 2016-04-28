import webcolors, re

RGB_PARSER = re.compile(r'^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\);?$')


class Color(object):
    """
    A class that supports parsing of colors, that are most likely
    returned by a get_style() call.
    """
    def __init__(self, definition):
        if not isinstance(definition, str):
            raise Exception("Unable to parse color %s" % definition)

        color_definition = definition.lower()

        if color_definition.startswith("rgb("):
            m = RGB_PARSER.match(color_definition)
            color_rgb =(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            self.value = webcolors.rgb_to_hex(color_rgb)
        elif color_definition.startswith("#"):
            self.value = webcolors.normalize_hex(color_definition)
        else:
            self.value = webcolors.rgb_to_hex(webcolors.html5_parse_legacy_color(color_definition))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.value == other.value
