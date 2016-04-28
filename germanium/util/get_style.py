from selenium.webdriver.remote.webelement import WebElement

from ._element import _element
from .find_germanium_object import find_germanium_object


def get_style_g(context, selector, name):
    germanium = find_germanium_object(context)

    if isinstance(selector, WebElement):
        element = selector
    else:
        element = _element(germanium, selector)

    return germanium.js("return window.getComputedStyle(arguments[0])[arguments[1]];", element, name)
