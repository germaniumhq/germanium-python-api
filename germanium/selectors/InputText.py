
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
        css_selectors = ["css:input[type='text']", "css:input"]

        if self._input_name:
            for i in range(len(css_selectors)):
                css_selectors[i] += "[name='%s']" % self._input_name

        css_selectors[1] += ":not([type])"

        return css_selectors
