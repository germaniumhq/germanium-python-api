from selenium.webdriver.remote.webelement import WebElement

from .DeferredLocator import DeferredLocator


class JsLocator(DeferredLocator):
    """
    A JS Deferred locator. This locator will execute some JavaScript
    code in order to find the elements.
    """
    def __init__(self, germanium, code):
        super(JsLocator, self).__init__(germanium)

        self._code = code

    def _find_element(self):
        """
        Finds a single element using the provided JS Code.
        """
        element = self._germanium.js(self._code)

        if not element:
            return None

        if not isinstance(element, WebElement):
            raise Exception("Code `%s` is not returning an element." % self._code)

        return element

    def _find_element_list(self):
        """
        Finds a single element using the given code.
        """
        element = self._find_element()

        if not element:
            return []

        return [element]
