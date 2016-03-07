from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

from .arguments_processor import find_germanium_object

def click(context, selector = None, move_mouse_over = True):
    """ Click the given selector """
    germanium = find_germanium_object([context])

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.click(element).perform()

def right_click(context, selector = None, move_mouse_over = True):
    """ Right click the given location """
    germanium = find_germanium_object([context])

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.context_click(element).perform()

def double_click(context, selector = None, move_mouse_over = True):
    """ Double click the given location """
    germanium = find_germanium_object([context])

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.double_click(element).perform()

def hover(context, selector = None):
    """ Hover the given location """
    """ Double click the given location """
    germanium = find_germanium_object([context])

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    action.move_to_element(element).perform()

def _element(germanium, selector):
    element = None

    if selector:
        element = germanium.S(selector).element()
        if not element:
            raise NoSuchElementException(selector)

    return element

