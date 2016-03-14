
from .AbstractSelector import AbstractSelector


class InputText(AbstractSelector):
    """
    Just a selector that finds an input text by its name.
    """
    def __init__(self, name=None):
        super(AbstractSelector, self).__init__()
        self._input_name = name

    def get_selectors(self):
        # CSS selector.
        xpath_selectors = ["xpath://input[@type='text']",
                           "xpath://input[not(@type)]"]

        if self._input_name:
            for i in range(len(xpath_selectors)):
                xpath_selectors[i] += "[@name='%s']" % self._input_name

        return xpath_selectors
