
class AbstractSelector(object):
    """
    Just a marker interface.
    """
    def __init__(self):
        pass


class Input(AbstractSelector):
    """
    Just a selector that finds an input by its name.
    """
    def __init__(self, input_name):
        self._input_name = input_name

    def get_selectors(self):
        # CSS selector.
        return [ "input[name='%s']" % self._input_name ]


class Button(AbstractSelector):
    """
    Just a selector that finds a button by its label or name.
    """
    def __init__(self, label = None, name = None):
        self._label = label
        self._name = name

    def get_selectors(self):
        """ Return the CSS selector to find the button. """
        button_selector = "//button"
        input_selector = "input[type='button']"

        if self._name:
            button_selector += "[@name='%s']" % self._name
            input_selector += "[name='%s']" % self._name

        if self._label:
            button_selector += "[string(.)='%s']" % self._label
            input_selector += "[value='%s']" % self._label

        return [input_selector, button_selector]


class Text(AbstractSelector):
    """
    Just a selector that finds the text in the page.
    """
    def __init__(self, text):
        self._text = text

    def get_selectors(self):
        """ Return the simple selector to find the text """
        simple_locator = '"%s"' % self._text

        return [simple_locator]

