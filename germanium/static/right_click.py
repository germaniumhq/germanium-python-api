from .global_germanium_instance import *

from germanium import right_click as right_click_impl


def right_click(selector):
    """
    Right click the element with the given selector.
    """
    if not get_instance():
        raise Exception("You need to start a browser first with open_browser()")

    right_click_impl(get_instance(), selector)
