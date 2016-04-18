from .DeferredLocator import DeferredLocator


class CompositeLocator(DeferredLocator):
    """
    A locator that will search using the locators it contains.
    """
    def __init__(self, locators):
        super(CompositeLocator, self).__init__(None)

        self._locators = locators

    def _find_element(self):
        for locator in self._locators:
            element = locator.element()
            if element:
                return element
        return None

    def _find_element_list(self):
        result = []

        for locator in self._locators:
            result.extend(locator.element_list())

        return result
