from germanium.impl._load_script import load_script
from .DeferredLocator import DeferredLocator


class InsideFilterLocator(DeferredLocator):
    def __init__(self,
                 germanium,
                 locator,
                 inside_filters=None,
                 containing_filters=None,
                 without_children=False):

        super(InsideFilterLocator, self).__init__(germanium=germanium)

        if not inside_filters:
            inside_filters = []

        if not containing_filters:
            containing_filters = []

        self.locator = locator
        self.inside_filters = inside_filters
        self.containing_filters = containing_filters
        self.without_children = without_children

    def _find_element(self):
        items = self._find_element_list()
        if len(items):
            return items[0]

        return None

    def _find_element_list(self):
        elements = self.locator._find_element_list()

        inside_elements = set()
        for selector in self.inside_filters:
            for inside_element in selector.element_list():
                inside_elements.add(inside_element)

        containing_elements = set()
        for selector in self.containing_filters:
            for containing_element in selector.element_list():
                containing_elements.add(containing_element)

        js_arguments = []

        code = load_script(__name__, 'inside-filter.min.js')

        js_arguments.append(code)
        js_arguments.append(1 if self.without_children else 0)
        js_arguments.append(len(inside_elements))
        for inside_element in inside_elements:
            js_arguments.append(inside_element)
        js_arguments.append(len(containing_elements))
        for containing_element in containing_elements:
            js_arguments.append(containing_element)
        js_arguments.append(len(elements))
        for element in elements:
            js_arguments.append(element)

        result_elements = self._germanium.js(*js_arguments)

        return result_elements
