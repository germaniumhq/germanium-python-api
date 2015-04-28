
from GermaniumDriver import GermaniumDriver


def find_germanium_object(items):
    """
    Finds the germanium object in the given call. Searches it
    first in the parameter list, and if is not there, it searches
    it in the self reference, as either self.germanium or self._germanium.
    :param items:
    :return:
    """
    for item in items:
        if isinstance(item, GermaniumDriver):
            return item

    self = items[0]  # get the self reference

    _germanium = getattr(self, "germanium", None)

    if _germanium:
        return _germanium

    return self._germanium


def iframe(target, restore=False):
    """
    IFrame selector for various operations.
    :param target: The IFrame to set.
    :param restore: True if should restore the IFrame to the current iframe after this method is done.
    :param germanium:
    :return:
    """
    def wrapper(original):
        def original_aspect(*args, **kwargs):
            germanium = find_germanium_object(args)
            original_iframe = germanium.current_iframe

            germanium.select_iframe(target)

            try:
                return original(*args, **kwargs)
            finally:
                if restore:
                    germanium.select_iframe(original_iframe)

        return original_aspect

    return wrapper
