from .AbstractSelector import AbstractSelector


class Link(AbstractSelector):
    """
    A selector that finds links in the page.
    """
    def __init__(self, search_text=None, text=None, search_href=None, href=None):
        super(Link, self).__init__()

        self._search_text = search_text
        self._text = text
        self._search_href = search_href
        self._href = href

    def get_selectors(self):
        """ Return the xpsth locator to find the text """
        if self._search_text and self._text:
            raise Exception("You can't have both a searched text and an exact text match")

        if self._search_href and self._href:
            raise Exception("You can't have both a searched href and an exact href match")

        css_locator = '//a'

        if self._search_text:
            css_locator += "[contains(normalize-space(string()), \"%s\")]" % self._search_text

        if self._text:
            css_locator += '[string()="%s"]' % self._text

        if self._search_href:
            css_locator += "[contains(@href, \"%s\")]" % self._search_href

        if self._href:
            css_locator += '[@href="%s"]' % self._href

        return [css_locator]
