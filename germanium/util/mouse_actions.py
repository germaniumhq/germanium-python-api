from selenium.webdriver import ActionChains

from germanium.points import Point
from ._element import _element
from .find_germanium_object import find_germanium_object


def _element_or_position(germanium, selector):
    if isinstance(selector, Point):
        return selector
    return _element(germanium, selector)


def _move_mouse(germanium, selector, point, move_mouse_over=False, action=None):
    if not action:
        action = ActionChains(germanium.web_driver)

    element = _element_or_position(germanium, selector)

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

    return action


def click_g(context, selector=None, point=None, move_mouse_over=True):
    """ Click the given selector
    :param context:
    :param selector:
    :param point:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    _move_mouse(germanium, selector, point, move_mouse_over)\
        .click().perform()


def right_click_g(context, selector=None, point=None, move_mouse_over=True):
    """ Right click the given location
    :param context:
    :param selector:
    :param point:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    _move_mouse(germanium, selector, point, move_mouse_over) \
        .context_click().perform()


def double_click_g(context, selector=None, point=None, move_mouse_over=True):
    """ Double click the given location
    :param context:
    :param selector:
    :param point:
    :param move_mouse_over:
    """
    germanium = find_germanium_object(context)

    _move_mouse(germanium, selector, point, move_mouse_over) \
        .double_click().perform()


def hover_g(context, selector=None, point=None):
    """ Hover the given location
    :param context:
    :param selector:
    :param point:
    """
    germanium = find_germanium_object(context)

    _move_mouse(germanium, selector, point, move_mouse_over=True) \
        .perform()
