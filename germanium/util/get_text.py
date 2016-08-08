from selenium.webdriver.remote.webelement import WebElement

from ._element import _element
from .find_germanium_object import find_germanium_object


def get_text_g(context, selector):
    germanium = find_germanium_object(context)

    if isinstance(selector, WebElement):
        element = selector
    else:
        element = _element(germanium, selector)

    result = element.text

    return str(result).replace("\r\n", "\n")

