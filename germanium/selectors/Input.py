
from .AbstractSelector import AbstractSelector

class Input(AbstractSelector):
    """
    Just a selector that finds an input by its name.
    """
    def __init__(self, name):
        self._input_name = name

    def get_selectors(self):
        # CSS selector.
        return [ "input[name='%s']" % self._input_name ]

