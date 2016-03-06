from germanium import type_keys as type_keys_impl
from .global_germanium_instance import *


def type_keys(keys, selector = None):
    """
    Type the keys specified into the element, or the currently active element.
    """
    if not get_instance():
        raise Exception("You need to start a browser first with open_browser()")

    type_keys_impl(get_instance(), keys, selector)
