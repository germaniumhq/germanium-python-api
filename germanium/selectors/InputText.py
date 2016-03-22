
from .AbstractSelector import AbstractSelector


class InputText(AbstractSelector):
    """
    Just a selector that finds an input text by its name.
    """
    def __init__(self, name=None):
        super(InputText, self).__init__()

        xpath_selectors = ["//input[@type='text']",
                           "//input[not(@type)]"]

        if name:
            for i in range(len(xpath_selectors)):
                xpath_selectors[i] += "[@name='%s']" % name

        self._xpath_selectors = xpath_selectors

    def get_selectors(self):
        # CSS selector.
        return self._xpath_selectors
