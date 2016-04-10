from selenium.webdriver import ActionChains
from .find_germanium_object import find_germanium_object
from ._element import _element


def click_g(context, selector=None, move_mouse_over=True):
    """ Click the given selector
    :param context:
    :param selector:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.click(element).perform()


def right_click_g(context, selector=None, move_mouse_over=True):
    """ Right click the given location
    :param context:
    :param selector:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.context_click(element).perform()


def double_click_g(context, selector=None, move_mouse_over=True):
    """ Double click the given location
    :param context:
    :param selector:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if move_mouse_over and selector:
        action.move_to_element(element)

    action.double_click(element).perform()


def hover_g(context, selector=None):
    """ Hover the given location
    :param context:
    :param selector:
    """
    germanium = find_germanium_object(context)

    element = _element(germanium, selector)
    action = ActionChains(germanium.web_driver)

    action.move_to_element(element).perform()
