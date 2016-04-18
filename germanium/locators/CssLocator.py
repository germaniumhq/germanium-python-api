import collections

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from .DeferredLocator import DeferredLocator


class CssLocator(DeferredLocator):
    """
    A CSS Deferred locator.
    """
    def __init__(self, germanium, locator):
        super(CssLocator, self).__init__(germanium)

        self._locator = locator

    def _find_element(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        try:
            return self._germanium.find_element_by_css_selector(self._locator)
        except NoSuchElementException as e:
            return None

    def _find_element_list(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        try:
            result = self._germanium.find_elements_by_css_selector(self._locator)

            if isinstance(result, collections.Iterable):
                return result

            if isinstance(result, WebElement):
                return [result]

            raise Exception("Expected an iterable, but found instead %s with type %s as "
                            "a return for `web_driver.find_elements_by_css_selector('%s'), on "
                            "locator %s." %
                            (result,
                             type(result),
                             self._locator,
                             self))
        except NoSuchElementException as e:
            return None
