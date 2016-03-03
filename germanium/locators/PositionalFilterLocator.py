from .DeferredLocator import DeferredLocator


class PositionalFilterLocator(DeferredLocator):
    def __init__(self, locator, left_of_filters=[]):
        super(DeferredLocator, self).__init__()
        self.locator = locator
        self.left_of_filters = left_of_filters

    def _findElement(self):
        items = self._findElements()
        if len(items):
            return items[0]

        return None

    def _findElements(self):
        elements = self.locator.element_list()

        elements = self._left_of_filter(elements)

        return elements

    def _left_of_filter(self, elements):
        left_of_elements = []
        for left_of_filter in self.left_of_filters:
            left_of_elements.extend(left_of_filter.element_list())

        def is_left_of_all(element):
            for e in left_of_elements:
                if e.location['x'] >= element.location['x']:
                    return True
            return False

        if len(left_of_elements):
            elements = list(filter(is_left_of_all, elements))
            pivot_y = left_of_elements[0].location['y']
            elements = sorted(elements, key=lambda e: abs(e.location['y'] - pivot_y))
        return elements
