
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
        return self._find_element()

    def element_list(self):
        return self._find_element_list()

    def exists(self):
        """ Return True/False if the currently matched element exists or not """
        return self.element() is not None

    def _find_element(self):
        """ Find the element. """
        raise Exception("not implemented")

    def _find_element_list(self):
        """
        Find all the elements that match the given locator.
        :return:
        """
        raise Exception("Not implemented")
