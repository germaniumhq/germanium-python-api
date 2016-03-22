from .AbstractSelector import AbstractSelector, PositionalFilterSelector


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
            if isinstance(cell_selector, PositionalFilterSelector):
                raise Exception("Positional selectors are not supported in TableRow.containing(), only "
                                "selectors that will return XPath global searches, without positional "
                                "references.")

            string_selectors = cell_selector.get_selectors()

            for string_selector in string_selectors:
                if not string_selector.startswith("//") \
                        and not string_selector.startswith("xpath://"):
                    raise Exception("Only selectors that return XPath are supported for `TableRow.containing` "
                                    "calls. Currently `%s` was found. In case you want to use a CSS selector, "
                                    "use instead the `germanium.selectors.Element` selector, since it "
                                    "generates XPath, and will function correctly with TableRow selectors." % string_selector)

            if len(string_selectors) > 1:
                new_result = []

                for string_selector in string_selectors:
                    if string_selector.startswith("xpath://"):
                        string_selector = string_selector[6:]

                    for current_result in result:
                        new_result.append("%s[.%s]" % (current_result, string_selector))

                result = new_result
            else:
                for i in range(len(result)):
                    string_selector = string_selectors[0]

                    if string_selector.startswith("xpath://"):
                        string_selector = string_selector[6:]

                    result[i] += "[.%s]" % string_selector

        return result
