from ._element import _element
from .find_germanium_object import find_germanium_object


def get_value_g(context, selector):
    germanium = find_germanium_object(context)
    element = _element(germanium, selector)

    return germanium.js("return arguments[0].value;", element)
