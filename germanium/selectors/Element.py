from .AbstractSelector import AbstractSelector
import collections


class Element(AbstractSelector):
    def __init__(self,
                 tag_name=None,
                 *args,
                 index=None,
                 id=None,
                 exact_text=None,
                 contains_text=None,
                 css_classes=None,
                 exact_attributes=None,
                 extra_xpath=None,
                 contains_attributes=None,
                 **kw):
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

        xpath_locator = './/' + tag_name

        if contains_text:
            xpath_locator += "[contains(normalize-space(string()), '%s')]" % contains_text

        if exact_text:
            xpath_locator += "[string() = '%s']" % exact_text

        if css_classes is None:
            css_classes = []
        elif isinstance(css_classes, str):
            css_classes = css_classes.split()
        elif not isinstance(css_classes, collections.Iterable):
            raise Exception("A css_classes attribute was sent that is not an `iterable` nor "
                            "`string` object. It was a `%s` with value: `%s`" % (type(css_classes), css_classes))

        for css_class in css_classes:
            xpath_locator += '[contains(concat(" ", @class, " "), " %s ")]' % css_class

        for k, v in exact_attributes.items():
            xpath_locator += '[@%s = "%s"]' % (k, v)

        # all the unknown attributes can be mapped to the exact attributes.
        for k, v in kw:
            xpath_locator += '[@%s = "%s"]' % (k, v)

        for k, v in contains_attributes.items():
            xpath_locator += "[contains(normalize-space(@%s), '%s')]" % (k, v)

        if extra_xpath:
            xpath_locator += extra_xpath

        if isinstance(index, str):
            index = int(index)

        if index is not None:
            if index > 0:
                xpath_locator = '(%s)[%d]' % (xpath_locator, index)
            else:
                raise Exception("The number received as an index for selectors was less "
                                "or equal to 0. These are XPath indexes, so they must "
                                "start with 1. 1st item, not 0st item.")

        self._xpath_locator = 'xpath:' + xpath_locator

    def get_selectors(self):
        return [self._xpath_locator]
