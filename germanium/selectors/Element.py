from .AbstractSelector import AbstractSelector
from germanium.impl import _ensure_list


class Element(AbstractSelector):
    def __init__(self,
                 tag_name=None,
                 *args,
                 index=-1,
                 id=None,
                 exact_text=None,
                 contains_text=None,
                 css_classes=None,
                 exact_attributes=None,
                 contains_attributes=None):
        """ A general element selector. """
        super(Element, self).__init__()

        if not contains_attributes:
            contains_attributes = {}

        if not exact_attributes:
            exact_attributes = {}

        if id:
            exact_attributes['id'] = id

        if exact_text and contains_text:
            raise Exception("Having the exact text to be matched, "
                            "and a partial text to be searched is not supported.")

        xpath_locator = '//' + tag_name

        if contains_text:
            xpath_locator += "[contains(normalize-space(string()), '%s')]" % contains_text

        if exact_text:
            xpath_locator += "[string() = '%s']" % exact_text

        css_classes = _ensure_list(css_classes)
        for css_class in css_classes:
            xpath_locator += '[contains(concat(" ", @class, " "), " %s ")]' % css_class

        for k, v in exact_attributes.items():
            xpath_locator += '[@%s = "%s"]' % (k, v)

        for k, v in contains_attributes.items():
            xpath_locator += "[contains(normalize-space(@%s), '%s')]" % (k, v)

        if index >= 0:
            xpath_locator = 'xpath:(%s)[%d]' % (xpath_locator, index)

        self._xpath_locator = xpath_locator

    def get_selectors(self):
        return [self._xpath_locator]
