from ._element import _element
from .find_germanium_object import find_germanium_object

from selenium.webdriver.support.select import Select


def get_value_g(context, selector):
    germanium = find_germanium_object(context)
    element = _element(germanium, selector)

    if element.tag_name == "select" and element.get_attribute("multiple"):
        return list(map(lambda x: x.get_attribute("value"), Select(element).all_selected_options))

    return germanium.js("return arguments[0].value;", element)
