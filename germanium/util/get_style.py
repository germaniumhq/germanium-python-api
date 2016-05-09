from selenium.webdriver.remote.webelement import WebElement

from ._element import _element
from .find_germanium_object import find_germanium_object


def get_style_g(context, selector, name):
    germanium = find_germanium_object(context)

    if isinstance(selector, WebElement):
        element = selector
    else:
        element = _element(germanium, selector)

    return germanium.js("""
        if (arguments[0].style && arguments[0].style[arguments[1]]) {
            return arguments[0].style[arguments[1]];
        } else {
            return window.getComputedStyle(arguments[0], null)[arguments[1]];
        }
    """, element, name)
