from selenium.common.exceptions import NoSuchElementException
from germanium.selectors import AbstractSelector
from selenium.webdriver.remote.webelement import WebElement

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


class StaticElementLocator(DeferredLocator):
    def __init__(self, element):
        """ documentation """
        self._element = element

    def _findElement(self):
        """ Returns the locally stored element. """
        return self._element


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


def create_locator(germanium, locator, strategy='detect'):
    if strategy == 'css':
        return CssLocator(germanium, locator)

    if strategy == 'xpath':
        return XPathLocator(germanium, locator)

    if strategy == 'simple':
        return SimpleLocator(germanium, locator)

    if strategy != 'detect':
        raise Exception('Unable to find element. Available strategies: detect, css, xpath, simple')

    if isinstance(locator, AbstractSelector):
        selectors = locator.get_selectors()

        # if there is only one locator, don't apply the composite.
        if len(selectors) == 1:
            return create_locator(germanium, selectors[0])

        # if we have multiple locators, apply the composite locator.
        locator_list = []
        for selector in locator.get_selectors():
            locator_list.append(create_locator(germanium, selector))

        return CompositeLocator(locator_list)

    if isinstance(locator, WebElement):
        return StaticElementLocator(locator)

    # if it starts with // it's probably an XPath locator.
    if locator[0:2] == "//":
        return XPathLocator(germanium, locator)

    if not '"' in locator:
        return CssLocator(germanium, locator)

    return SimpleLocator(germanium, locator)

