from .AbstractSelector import AbstractSelector

class Link(AbstractSelector):
    """
    A selector that finds links in the page.
    """
    def __init__(self, search_text=None, text=None, href=None):
        self._search_text = search_text
        self._text = text
        self._href = href

    def get_selectors(self):
        """ Return the simple locator to find the text """
        if self._search_text and self._text:
            raise Exception("You can't have both a searched text and an exact text match")

        css_locator = 'xpath://a'

        if self._search_text:
            css_locator += "[contains(normalize-space(string()), \"%s\")]" % self._search_text

        if self._text:
            css_locator += '[string()="%s"]' % self._text

        if self._href:
            css_locator += '[@href="%s"]' % self._href

        return [css_locator]

