
from GermaniumDriver import GermaniumDriver


def find_germanium_object(items):
    """
    Finds the germanium object in the given call. Searches it
    first in the parameter list, and if is not there, it searches
    it in the self reference.
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


def iframe(target):
    """
    IFrame selector for various operations.
    :param method:
    :param germanium:
    :return:
    """
    def wrapper(original):
        def original_aspect(*args, **kwargs):
            germanium = find_germanium_object(args)
            germanium.select_iframe(target)

            return original(*args, **kwargs)

        return original_aspect

    return wrapper
