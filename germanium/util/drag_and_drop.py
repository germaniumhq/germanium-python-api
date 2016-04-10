from selenium.webdriver import ActionChains
from ._element import _element
from .find_germanium_object import find_germanium_object


def drag_and_drop_g(context, from_selector, to_selector):
    germanium = find_germanium_object(context)
    from_element = _element(germanium, from_selector)
    to_element = _element(germanium, to_selector)

    action = ActionChains(germanium.web_driver)

    action.drag_and_drop(from_element, to_element)\
          .perform()
