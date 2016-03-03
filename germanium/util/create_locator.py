
from germanium.selectors import AbstractSelector, PositionalFilterSelector
from selenium.webdriver.remote.webelement import WebElement

from germanium.locators import \
    XPathLocator, \
    CssLocator, \
    SimpleLocator, \
    CompositeLocator, \
    DeferredLocator, \
    StaticElementLocator, \
    PositionalFilterLocator

import re

LOCATOR_SPECIFIER = re.compile(r'((\w[\w\d]*?)\:)(.*)')


def create_locator(germanium, locator, strategy='detect'):
    if strategy == 'css':
        return CssLocator(germanium, locator)

    if strategy == 'xpath':
        return XPathLocator(germanium, locator)

    if strategy == 'simple':
        return SimpleLocator(germanium, locator)

    if strategy != 'detect':
        locator_constructor = germanium.locator_map[strategy]

        if not locator_constructor:
            raise Exception('Unable to find strategy %s. Available strategies: detect, %s' % (strategy, ', '.join(germanium.locator_map.keys())))

        return locator_constructor(germanium, locator)

    if isinstance(locator, DeferredLocator):
        if strategy is not 'detect':
            raise Exception('The locator is already constructed, but a strategy is also defined: "%s"' % strategy)

        return locator

    if isinstance(locator, PositionalFilterSelector):
        left_of_filters = map(lambda x: create_locator(germanium, x),
                              locator.left_of_filters)

        right_of_filters = map(lambda x: create_locator(germanium, x),
                               locator.right_of_filters)

        above_filters = map(lambda x: create_locator(germanium, x),
                            locator.above_filters)

        below_filters = map(lambda x: create_locator(germanium, x),
                            locator.below_filters)

        return PositionalFilterLocator(
            locator=create_locator(germanium, locator.selector),
            left_of_filters=left_of_filters,
            right_of_filters=right_of_filters,
            above_filters=above_filters,
            below_filters=below_filters
        )

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

    m = LOCATOR_SPECIFIER.match(locator)
    if m:
        locator_constructor = germanium.locator_map[m.group(2)]
        if locator_constructor:
            return locator_constructor(germanium, m.group(3))

    return CssLocator(germanium, locator)

