from .DeferredLocator import DeferredLocator

class CompositeLocator(DeferredLocator):
    """
    A locator that will search using the locators it contains.
    """
    def __init__(self, locators):
        self._locators = locators

    def _findElement(self):
        for locator in self._locators:
            element = locator.element()
            if element:
                return element
        return None

    def _findElements(self):
        result = []

        for locator in self._locators:
            result.extend(locator.element_list())

        return result
