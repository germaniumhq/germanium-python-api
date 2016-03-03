from .DeferredLocator import DeferredLocator


class StaticElementLocator(DeferredLocator):
    def __init__(self, element):
        """ documentation """
        self._element = element

    def _findElement(self):
        """ Returns the locally stored element. """
        return self._element

    def _findElements(self):
        return [self._element]
