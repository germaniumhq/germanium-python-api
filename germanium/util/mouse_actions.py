from selenium.webdriver import ActionChains
from .find_germanium_object import find_germanium_object
from ._element import _element

from germanium.points import Point


def _element_or_position(germanium, selector):
    if isinstance(selector, Point):
        return selector
    return _element(germanium, selector)


def click_g(context, selector=None, point=None, move_mouse_over=True):
    """ Click the given selector
    :param context:
    :param selector:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    element = _element_or_position(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if isinstance(element, Point):
        action.move_to_element_with_offset(
            germanium.S('body').element(),
            element.x,
            element.y)
    elif selector and point:
        action.move_to_element_with_offset(
            element,
            point.x,
            point.y)
    elif move_mouse_over and selector:
        action.move_to_element(element)

    action.click().perform()


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


def hover_g(context, selector=None, point=None):
    """ Hover the given location
    :param context:
    :param selector:
    """
    germanium = find_germanium_object(context)

    element = _element_or_position(germanium, selector)
    action = ActionChains(germanium.web_driver)

    if isinstance(element, Point):
        action.move_to_element_with_offset(
            germanium.S('body').element(),
            element.x,
            element.y)
    elif selector and point:
        action.move_to_element_with_offset(
            element,
            point.x,
            point.y)
    else:
        action.move_to_element(element)

    action.perform()
