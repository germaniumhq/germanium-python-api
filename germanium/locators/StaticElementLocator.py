from .DeferredLocator import DeferredLocator


class StaticElementLocator(DeferredLocator):
    def __init__(self, element):
        """ Just holds a static reference to a single element. """
        super(StaticElementLocator, self).__init__(None)

        self._element = element

    def _find_element(self):
        """ Returns the locally stored element. """
        return self._element

    def _find_element_list(self):
        return [self._element]
