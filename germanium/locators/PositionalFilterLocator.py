from .DeferredLocator import DeferredLocator


class PositionalFilterLocator(DeferredLocator):
    def __init__(self, locator, left_of_filters=[], right_of_filters=[], above_filters=[], below_filters=[]):
        super(DeferredLocator, self).__init__()
        self.locator = locator
        self.left_of_filters = left_of_filters
        self.right_of_filters = right_of_filters
        self.above_filters = above_filters
        self.below_filters = below_filters

    def _find_element(self):
        items = self._find_element_list()
        if len(items):
            return items[0]

        return None

    def _find_element_list(self):
        elements = self.locator.element_list()

        elements = self._below_filter(elements)
        elements = self._above_filter(elements)
        elements = self._left_of_filter(elements)
        elements = self._right_of_filter(elements)

        return elements

    def _below_filter(self, elements):
        below_elements = []
        for below_filter in self.below_filters:
            below_elements.extend(below_filter.element_list())

        def is_below_all(element):
            for e in below_elements:
                if e.location['y'] <= element.location['y']:
                    return True
            return False

        if len(below_elements):
            elements = list(filter(is_below_all, elements))
            pivot_x = below_elements[0].location['x']
            elements = sorted(elements, key=lambda e: abs(e.location['x'] - pivot_x))
        return elements

    def _above_filter(self, elements):
        above_elements = []
        for above_filter in self.above_filters:
            above_elements.extend(above_filter.element_list())

        def is_above_all(element):
            for e in above_elements:
                if e.location['y'] >= element.location['y']:
                    return True
            return False

        if len(above_elements):
            elements = list(filter(is_above_all, elements))
            pivot_x = above_elements[0].location['x']
            elements = sorted(elements, key=lambda e: abs(e.location['x'] - pivot_x))
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

    def _right_of_filter(self, elements):
        right_of_elements = []
        for right_of_filter in self.right_of_filters:
            right_of_elements.extend(right_of_filter.element_list())

        def is_right_of_all(element):
            for e in right_of_elements:
                if e.location['x'] <= element.location['x']:
                    return True
            return False

        if len(right_of_elements):
            elements = list(filter(is_right_of_all, elements))
            pivot_y = right_of_elements[0].location['y']
            elements = sorted(elements, key=lambda e: abs(e.location['y'] - pivot_y))

        return elements
