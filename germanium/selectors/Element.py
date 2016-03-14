from .AbstractSelector import AbstractSelector


class Element(AbstractSelector):
    def __init__(self,
                 tag_name=None,
                 index=-1,
                 exact_text=None,
                 contains_text=None,
                 css_classes=[],
                 exact_attributes={}):
        """ A general element selector. """
        self._tag_name = tag_name
        self._index = index
        self._text = exact_text
        self._contains_text = contains_text
        self._css_classes = css_classes
        self._exact_attributes = exact_attributes

        if self._text and self._contains_text:
            raise Exception("Having the exact text to be matched, "
                            "and a partial text to be searched is not supported.")

    def get_selectors(self):
        xpath_locator = '//' + self._tag_name

        if self._contains_text:
            xpath_locator += "[contains(normalize-space(string()), '%s')]" % self._contains_text

        if self._text:
            xpath_locator += "[string() = '%s']" % self._text

        for css_class in self._css_classes:
            xpath_locator += '[contains(concat(" ", @class, " "), " %s ")]' % css_class

        for k, v in self._exact_attributes.items():
            xpath_locator += '[@%s = "%s"]' % (k, v)

        if self._index >= 0:
            xpath_locator = '(%s)[%d]' % (xpath_locator, self._index)

        return ["xpath:" + xpath_locator]
