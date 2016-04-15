from .find_germanium_object import find_germanium_object
from ._element import _element

from selenium.webdriver.support.select import Select


def select_g(context, selector, text=None, *argv, index=None, value=None):
    germanium = find_germanium_object(context)
    select_element = _element(germanium, selector)

    s = Select(select_element)

    if text is not None:
        s.select_by_visible_text(text)
    elif index is not None:
        s.select_by_index(index)
    elif value is not None:
        s.select_by_value(value)
