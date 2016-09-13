import collections

from .DeferredLocator import DeferredLocator


class StaticElementLocator(DeferredLocator):
    def __init__(self, element):
        """ Just holds a static reference to the elements. """
        super(StaticElementLocator, self).__init__(None)

        if not isinstance(element, collections.Iterable):
            self._element = [element]
        else:
            self._element = element

    def _find_element(self):
        """ Returns the locally stored element. """
        return self._element[0]

    def _find_element_list(self):
        return self._element
