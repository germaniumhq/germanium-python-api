
from .AbstractSelector import AbstractSelector


class Input(AbstractSelector):
    """
    Just a selector that finds an input by its name.
    """
    def __init__(self, name=None):
        super(AbstractSelector, self).__init__()
        self._input_name = name

    def get_selectors(self):
        # CSS selector.
        css_selector = "input"

        if self._input_name:
            css_selector += "[name='%s']" % self._input_name

        return [css_selector]
