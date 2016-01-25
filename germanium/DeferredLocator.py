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

    def element(self):
        """ Return the current matched element. """
        return self._findElement()

    def exists(self):
        """ Return True/False if the currently matched element exists or not """
        return self.element() is not None

    def _findElement(self):
        """ Find the element. """
        raise Exception("not implemented")


class CssLocator(DeferredLocator):
    """
    A CSS Deferred locator.
    """
    def __init__(self, germanium, locator):
        super(CssLocator, self).__init__(germanium)
        self._locator = locator

    def _findElement(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        try:
            return self._germanium.find_element_by_css_selector(self._locator)
        except NoSuchElementException as e:
            return None


class SimpleLocator(DeferredLocator):
    """
    A Simple Deferred locator.
    """
    def __init__(self, germanium, locator):
        super(SimpleLocator, self).__init__(germanium)
        self._locator = locator

    def _findElement(self):
        """
        Find an element using the Simple locator provided at creation.
        """
        return self._germanium.find_element_by_simple(self._locator)


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


def create_locator(germanium, locator, strategy='detect'):
    if strategy == 'css':
        return CssLocator(germanium, locator)

    if strategy == 'xpath':
        return XPathLocator(germanium, locator)

    if strategy == 'simple':
        return SimpleLocator(germanium, locator)

    if strategy != 'detect':
        raise Exception('Unable to find element. Available strategies: detect, css, xpath, simple')

    # if it starts with // it's probably an XPath locator.
    if locator[0:2] == "//":
        return XPathLocator(germanium, locator)

    if not '"' in locator:
        return CssLocator(germanium, locator)

    return SimpleLocator(germanium, locator)

