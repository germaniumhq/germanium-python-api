from .AbstractSelector import AbstractSelector


class Element(AbstractSelector):
    def __init__(self,
                 tag_name=None,
                 index=-1,
                 exact_text=None,
                 contains_text=None,
                 css_classes=[],
                 exact_attributes={},
                 contains_attributes={}):
        """ A general element selector. """
        super(AbstractSelector, self).__init__()

        if exact_text and contains_text:
            raise Exception("Having the exact text to be matched, "
                            "and a partial text to be searched is not supported.")

        xpath_locator = '//' + tag_name

        if contains_text:
            xpath_locator += "[contains(normalize-space(string()), '%s')]" % contains_text

        if exact_text:
            xpath_locator += "[string() = '%s']" % exact_text

        for css_class in css_classes:
            xpath_locator += '[contains(concat(" ", @class, " "), " %s ")]' % css_class

        for k, v in exact_attributes.items():
            xpath_locator += '[@%s = "%s"]' % (k, v)

        for k, v in contains_attributes.items():
            xpath_locator += "[contains(normalize-space(@%s), '%s')]" % (k, v)

        if index >= 0:
            xpath_locator = '(%s)[%d]' % (xpath_locator, index)

        self._xpath_locator = xpath_locator

    def get_selectors(self):
        return ["xpath:" + self._xpath_locator]
