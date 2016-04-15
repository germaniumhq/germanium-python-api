from .find_germanium_object import find_germanium_object
from ._element import _element
from germanium.impl import _ensure_list

from selenium.webdriver.support.select import Select


def select_g(context, selector, text=None, *argv, index=None, value=None):
    germanium = find_germanium_object(context)
    select_element = _element(germanium, selector)

    s = Select(select_element)

    if text is not None:
        for single_text in _ensure_list(text):
            s.select_by_visible_text(single_text)
    elif index is not None:
        for single_index in _ensure_list(index):
            s.select_by_visible_text(single_index)
    elif value is not None:
        for single_value in _ensure_list(index):
            s.select_by_visible_text(single_value)
