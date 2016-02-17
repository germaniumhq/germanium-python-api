
class DeferredLocator(object):
    """
    Create a deferred locator that can be used in matching
    elements in wait conditions.
    """
    def __init__(self, germanium):
        self._germanium = germanium

    def __call__(self):
        return self.element()

    def element(self):
        """ Return the current matched element. """
        return self._findElement()

    def exists(self):
        """ Return True/False if the currently matched element exists or not """
        return self.element() is not None

    def _findElement(self):
        """ Find the element. """
        raise Exception("not implemented")

