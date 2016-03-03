
from .DeferredLocator import DeferredLocator

class SimpleLocator(DeferredLocator):
    """
    A Simple Deferred locator.
    """
    def __init__(self, germanium, locator):
        super(SimpleLocator, self).__init__(germanium)
        print("A deprecated SimpleLocator instance was created. SimpleLocator will be removed in a future release.")
        self._locator = locator

    def _find_element_list(self):
        element = self._find_element()

        if element:
            return [element]

        return []

    def _find_element(self):
        """
        Find an element using the Simple locator provided at creation.
        """
        return self._germanium.find_element_by_simple(self._locator)

