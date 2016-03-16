from .AbstractSelector import AbstractSelector


class TableRow(AbstractSelector):
    def __init__(self):
        super(TableRow, self).__init__()

        self._cell_selectors = []

    def containing(self, cell_selector):
        self._cell_selectors.append(cell_selector)
        return self

    def get_selectors(self):
        result = ["//tr"]

        for cell_selector in self._cell_selectors:
            string_selectors = cell_selector.get_selectors()

            for string_selector in string_selectors:
                if not string_selector.startswith("//"):
                    raise Exception("Only selectors that return XPath are supported for `TableRow.containing` "
                                    "calls. Currently `%s` was found. In case you want to use a CSS selector, "
                                    "use instead the `germanium.selectors.Element` selector, since it "
                                    "generates XPath, and will function correctly with TableRow selectors.")

            if len(string_selectors) > 1:
                new_result = []
                for string_selector in string_selectors:
                    for current_result in result:
                        new_result.append("%s[.%s]" % (current_result, string_selector))
                result = new_result
            else:
                for i in range(len(result)):
                    result[i] += "[.%s]" % string_selectors[0]

        return result
