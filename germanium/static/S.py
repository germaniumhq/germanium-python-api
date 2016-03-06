from .global_germanium_instance import *


def S(*argv, **kwargs):
    """
    Call the super selector from germanium.
    """
    if not get_instance():
        raise Exception("You need to start a browser first with open_browser()")

    return get_instance().S(*argv, **kwargs)
