from .AbstractSelector import AbstractSelector

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

