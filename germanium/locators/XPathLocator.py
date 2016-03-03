from selenium.common.exceptions import NoSuchElementException

from .DeferredLocator import DeferredLocator


class XPathLocator(DeferredLocator):
    """
    A XPath Deferred locator.
    """
    def __init__(self, germanium, locator):
        super(XPathLocator, self).__init__(germanium)
        self._locator = locator

    def _findElement(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        try:
            return self._germanium.find_element_by_xpath(self._locator)
        except NoSuchElementException as e:
            return None

    def _findElements(self):
        """
        Find an element using the CSS locator
        :return:
        """
        try:
            return self._germanium.find_elements_by_xpath(self._locator)
        except NoSuchElementException as e:
            return None
