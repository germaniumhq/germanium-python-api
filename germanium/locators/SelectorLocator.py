
from germanium.util import create_locator


class SelectorLocator(DeferredLocator):
    """
    A Locator that uses the given selector to locate elements.
    It will defer all the actual work to `create_locator`
    """
    def __init__(self, germanium, selector_instance):
        super(SelectorLocator, self).__init__(germanium)
        self._locator = create_locator(germanium, selector_instance)

    def _findElement(self):
        """
        Finds the element by just using the actual locator that
        was created.
        """
        return self._locator._find_element()

    def _findElements(self):
        """
        Finds the elements using the locator that was created.
        :return:
        """
        return self._locator._find_element_list()