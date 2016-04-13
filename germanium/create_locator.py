import re

from selenium.webdriver.remote.webelement import WebElement

from germanium.locators import \
    XPathLocator, \
    CssLocator, \
    CompositeLocator, \
    DeferredLocator, \
    StaticElementLocator, \
    PositionalFilterLocator, \
    AlertLocator
from germanium.selectors import AbstractSelector, PositionalFilterSelector, Alert

LOCATOR_SPECIFIER = re.compile(r'((\w[\w\d]*?)\:)(.*)', re.MULTILINE|re.DOTALL)


def create_locator(germanium, selector, strategy='detect'):
    if selector is None:
        raise Exception("A `None` selector was passed to Germanium to create a "
                        "locator out of it. Maybe an invalid function return "
                        "is being used?")

    if strategy != 'detect':
        locator_constructor = germanium.locator_map[strategy]

        if not locator_constructor:
            raise Exception('Unable to find strategy %s. Available strategies: detect, %s' % (strategy, ', '.join(germanium.locator_map.keys())))

        return locator_constructor(germanium, selector)

    if isinstance(selector, DeferredLocator):
        if strategy is not 'detect':
            raise Exception('The locator is already constructed, but a strategy is also defined: "%s"' % strategy)

        return selector

    if isinstance(selector, PositionalFilterSelector):
        left_of_filters = map(lambda x: create_locator(germanium, x),
                              selector.left_of_filters)

        right_of_filters = map(lambda x: create_locator(germanium, x),
                               selector.right_of_filters)

        above_filters = map(lambda x: create_locator(germanium, x),
                            selector.above_filters)

        below_filters = map(lambda x: create_locator(germanium, x),
                            selector.below_filters)

        return PositionalFilterLocator(
            locator=create_locator(germanium, selector.selector),
            left_of_filters=left_of_filters,
            right_of_filters=right_of_filters,
            above_filters=above_filters,
            below_filters=below_filters
        )

    if isinstance(selector, AbstractSelector):
        selectors = selector.get_selectors()

        # if there is only one locator, don't apply the composite.
        if len(selectors) == 1:
            return create_locator(germanium, selectors[0])

        # if we have multiple locators, apply the composite locator.
        locator_list = []
        for selector in selector.get_selectors():
            locator_list.append(create_locator(germanium, selector))

        return CompositeLocator(locator_list)

    if isinstance(selector, WebElement):
        return StaticElementLocator(selector)

    if isinstance(selector, Alert):
        return AlertLocator(germanium)

    if hasattr(selector, '__call__'):
        return create_locator(germanium, selector())

    if not isinstance(selector, str):
        raise Exception('Unable to build locator from the selector. '
                        'The selector: %s, that is of type: %s is '
                        'not a string selector, does not inherit from '
                        'AbstractSelector, and is not an Alert.' % (selector, type(selector)))

    if selector == "alert":
        return AlertLocator(germanium, selector)

    # if it starts with // it's probably an XPath locator.
    if selector[0:2] == "//":
        return XPathLocator(germanium, selector)

    m = LOCATOR_SPECIFIER.match(selector)
    if m:
        locator_constructor = germanium.locator_map[m.group(2)]
        if locator_constructor:
            return locator_constructor(germanium, m.group(3))

    return CssLocator(germanium, selector)

