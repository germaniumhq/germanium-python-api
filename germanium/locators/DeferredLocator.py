from selenium.common.exceptions import NoSuchElementException


class DeferredLocator(object):
    """
    Create a deferred locator that can be used in matching
    elements in wait conditions.
    """
    def __init__(self, germanium):
        self._germanium = germanium

    def __call__(self):
        return self.element()

    def element(self, only_visible=False):
        """ Return the current matched element.
        :param only_visible: bool Find the element only
        if it's visible, so it can be interacted with.
        """
        if only_visible:
            elements = self.element_list(only_visible=only_visible)
            if not elements:
                raise NoSuchElementException()

            return elements[0]

        return self._find_element()

    def element_list(self, only_visible=False):
        """
        :type only_visible: boolean
        """
        if not only_visible:
            return self._find_element_list()

        found_items = self._find_element_list()
        items = filter(lambda x: x.is_displayed(), found_items)
        return list(items)

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
