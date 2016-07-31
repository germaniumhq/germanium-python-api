from germanium.util import use_window_g
from .global_germanium_instance import *


def use_window(title=None, index=None, id=None, *argv, **kw):
    """
    Use the given window.
    """
    if not get_instance():
        raise Exception("You need to start a browser first with open_browser()")

    return use_window_g(get_instance(), title=title, index=index, id=id, *argv, **kw)


