from selenium.common.exceptions import NoSuchElementException

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
            return self._germanium.find_elements_by_css_selector(self._locator)
        except NoSuchElementException as e:
            return None
