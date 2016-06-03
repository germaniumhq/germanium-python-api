from .DeferredLocator import DeferredLocator


class PositionalFilterLocator(DeferredLocator):
    def __init__(self,
                 locator,
                 left_of_filters=None,
                 right_of_filters=None,
                 above_filters=None,
                 below_filters=None):

        super(PositionalFilterLocator, self).__init__()

        if not left_of_filters:
            left_of_filters = []

        if not right_of_filters:
            right_of_filters = []

        if not above_filters:
            above_filters = []

        if not below_filters:
            below_filters = []

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

        self._cache = dict()
        self._add_to_position_cache(elements)

        elements = self._below_filter(elements)
        elements = self._above_filter(elements)
        elements = self._left_of_filter(elements)
        elements = self._right_of_filter(elements)

        self._cache = None

        return elements

    def _below_filter(self, elements):
        below_elements = []
        for below_filter in self.below_filters:
            below_elements.extend(below_filter.element_list())

        self._add_to_position_cache(below_elements)
        cache = self._cache

        def is_below_all(element):
            for e in below_elements:
                if cache[e]['location']['y'] + cache[e]['size']['height'] <= cache[element]['location']['y']:
                    return True
            return False

        if len(below_elements):
            elements = list(filter(is_below_all, elements))
            pivot_x = cache[below_elements[0]]['location']['x']
            pivot_y = cache[below_elements[0]]['location']['y']
            elements = sorted(elements,
                              key=lambda e: pow(abs(cache[e]['location']['x'] - pivot_x), 2) +
                                            abs(cache[e]['location']['y'] - pivot_y))
        return elements

    def _above_filter(self, elements):
        above_elements = []
        for above_filter in self.above_filters:
            above_elements.extend(above_filter.element_list())

        self._add_to_position_cache(above_elements)
        cache = self._cache

        def is_above_all(element):
            for e in above_elements:
                if cache[e]['location']['y'] >= cache[element]['location']['y'] + cache[element]['size']['height']:
                    return True
            return False

        if len(above_elements):
            elements = list(filter(is_above_all, elements))
            pivot_x = cache[above_elements[0]]['location']['x']
            pivot_y = cache[above_elements[0]]['location']['y']
            elements = sorted(elements,
                              key=lambda e: pow(abs(cache[e]['location']['x'] - pivot_x), 2) +
                                            abs(cache[e]['location']['y'] - pivot_y))
        return elements

    def _left_of_filter(self, elements):
        left_of_elements = []
        for left_of_filter in self.left_of_filters:
            left_of_elements.extend(left_of_filter.element_list())

        self._add_to_position_cache(left_of_elements)
        cache = self._cache

        def is_left_of_all(element):
            for e in left_of_elements:
                if cache[e]['location']['x'] >= cache[element]['location']['x'] + cache[element]['size']['width']:
                    return True
            return False

        if len(left_of_elements):
            elements = list(filter(is_left_of_all, elements))
            pivot_x = cache[left_of_elements[0]]['location']['x']
            pivot_y = cache[left_of_elements[0]]['location']['y']
            elements = sorted(elements,
                              key=lambda e: pow(abs(cache[e]['location']['y'] - pivot_y), 2) +
                                            abs(cache[e]['location']['x'] - pivot_x))
        return elements

    def _right_of_filter(self, elements):
        right_of_elements = []
        for right_of_filter in self.right_of_filters:
            right_of_elements.extend(right_of_filter.element_list())

        self._add_to_position_cache(right_of_elements)
        cache = self._cache

        def is_right_of_all(element):
            for e in right_of_elements:
                if cache[e]['location']['x'] + cache[e]['size']['width'] <= cache[element]['location']['x']:
                    return True
            return False

        if len(right_of_elements):
            elements = list(filter(is_right_of_all, elements))
            pivot_x = cache[right_of_elements[0]]['location']['x']
            pivot_y = cache[right_of_elements[0]]['location']['y']
            elements = sorted(elements,
                              key=lambda e: pow(abs(cache[e]['location']['y'] - pivot_y), 2) +
                                            abs(cache[e]['location']['x'] - pivot_x))

        return elements

    def _add_to_position_cache(self, elements):
        for element in elements:
            if element in self._cache:
                continue

            self._cache[element] = {
                "location": element.location,
                "size": element.size
            }
