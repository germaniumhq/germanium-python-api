from selenium.webdriver import ActionChains
from germanium.impl import _filter_one_for_action
from .find_germanium_object import find_germanium_object


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


def _element(germanium, selector):
    """
    Finds the given element.
    :param germanium:
    :param selector:
    :return:
    """
    element = None

    if selector:
        items = germanium.S(selector).element_list(only_visible=False)
        element = _filter_one_for_action(items)

    return element
