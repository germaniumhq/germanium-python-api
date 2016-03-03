from .AbstractSelector import AbstractSelector


class Text(AbstractSelector):
    """
    Just a selector that finds the text in the page.
    """
    def __init__(self, text):
        super(AbstractSelector, self).__init__()
        self._text = text

    def get_selectors(self):
        """ Return the simple selector to find the text """
        simple_locator = 'simple:"%s"' % self._text

        return [simple_locator]
