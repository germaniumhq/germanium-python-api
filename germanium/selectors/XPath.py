from .AbstractSelector import AbstractSelector


class XPath(AbstractSelector):
    """
    Just a selector that finds some XPath.
    """
    def __init__(self, selector=None):
        self._selector = selector

    def get_selectors(self):
        """ Return the XPath selector itself """
        return ["xpath:" + self._selector]

