from germanium.impl import _ensure_list
from cssselect import GenericTranslator


class AbstractSelector(object):
    """
    Just a marker interface.
    """
    def __init__(self):
        pass

    def get_selectors(self):
        raise Exception("Abstract class, not implemented.")

    def left_of(self, *argv, **kw):
        return PositionalFilterSelector(self)\
            .left_of(*argv, **kw)

    def right_of(self, *argv, **kw):
        return PositionalFilterSelector(self) \
            .right_of(*argv, **kw)

    def above(self, *argv, **kw):
        return PositionalFilterSelector(self) \
            .above(*argv, **kw)

    def below(self, *argv, **kw):
        return PositionalFilterSelector(self) \
            .below(*argv, **kw)

    def inside(self, *argv, **kw):
        return XPathInsideFilterSelector(self) \
            .inside(*argv, **kw)

    def containing(self, *argv, **kw):
        return XPathInsideFilterSelector(self) \
            .containing(*argv, **kw)

    def without_children(self, *argv, **kw):
        return XPathInsideFilterSelector(self) \
            .without_children(*argv, **kw)

    def __call__(self, *args, **kwargs):
        """
        Return the element list. If germanium is provided, the selector
        is evaluated using g.S(self).element_list(). If is not
        provided, this is equivalent to
        germanium.static.S(self).element_list()
        :param args:
        :param kwargs:
        :return:
        """
        return self.element_list(*args, **kwargs)

    def element(self, *argv, germanium=None, **kw):
        """
        If the germanium is provided, the selector is evaluated using
        germanium.S. If the germanium attribute is not provided,
        this is equivalent to: germanium.static.S(self).element()
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).element(*argv, **kw)

    def element_list(self, index=None, *argv, germanium=None, **kw):
        """
        If the germanium is provided, the selector is evaluated using
        germanium.S. If the germanium attribute is not provided,
        this is equivalent to: germanium.static.S(self).element_list()
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).element_list(index=index, *argv, **kw)

    def exists(self, *argv, germanium=None, **kw):
        """
        If the germanium is provided, the selector is evaluated using
        germanium.S. If the germanium attribute is not provided,
        this is equivalent to: germanium.static.S(self).exists()
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).exists(*argv, **kw)

    def not_exists(self, *argv, germanium=None, **kw):
        """
        If the germanium is provided, the selector is evaluated using
        germanium.S. If the germanium attribute is not provided,
        this is equivalent to: germanium.static.S(self).not_exists()
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).not_exists(*argv, **kw)

    def text(self, *argv, germanium=None, **kw):
        """
        Returns the text of the `element()` returned by this selector.
        If the germanium is provided, the selector is evaluated using
        germanium.S. If the germanium attribute is not provided,
        this is equivalent to: germanium.static.S(self).text()
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).text(*argv, **kw)


class XPathInsideFilterSelector(AbstractSelector):
    def __init__(self, parent_selector):
        super(XPathInsideFilterSelector, self).__init__()

        self._selectors = _get_xpath_selectors(parent_selector.get_selectors())

    def get_selectors(self):
        return self._selectors

    def inside(self, *argv, **kw):
        new_selectors = []
        inside_xpath_string_selectors = _get_xpath_selectors(argv)

        for inside_selector in inside_xpath_string_selectors:
            for reference_selector in self._selectors:
                # when concatenating XPath, we need to add a slash if the expression
                # is an axis navigation.
                if not reference_selector.startswith("/"):
                    reference_selector = "/" + reference_selector

                new_selectors.append("xpath:" + inside_selector + reference_selector)

        self._selectors = new_selectors

        return self

    def containing(self, *argv, **kw):
        new_selectors = []
        containing_xpath_string_selectors = _get_xpath_selectors(argv)

        for reference_selector in self._selectors:
            for containing_selector in containing_xpath_string_selectors:
                # when concatenating XPath, we need to add a slash if the expression
                # is an axis navigation.
                if not containing_selector.startswith("/"):
                    containing_selector = "/" + containing_selector

                new_selectors.append("xpath:%s[.%s]" % (reference_selector, containing_selector))

        self._selectors = new_selectors

        return self

    def without_children(self, *argv, **kw):
        new_selectors = []

        for reference_selector in _get_xpath_selectors(self._selectors):
            new_selectors.append("xpath:%s[count(./*) = 0][string() = '']" % reference_selector)

        self._selectors = new_selectors

        return self


class PositionalFilterSelector(AbstractSelector):
    """
    Filters selectors
    """
    def __init__(self, parent_selector):
        super(AbstractSelector, self).__init__()

        self.selector = parent_selector

        self.left_of_filters = []
        self.right_of_filters = []
        self.above_filters = []
        self.below_filters = []

    def left_of(self, *argv, **kw):
        other_selector = _ensure_selectors(argv)
        self.left_of_filters.extend(other_selector)

        return self

    def right_of(self, *argv, **kw):
        other_selector = _ensure_selectors(argv)
        self.right_of_filters.extend(other_selector)

        return self

    def above(self, *argv, **kw):
        other_selector = _ensure_selectors(argv)
        self.above_filters.extend(other_selector)

        return self

    def below(self, *argv, **kw):
        other_selector = _ensure_selectors(argv)
        self.below_filters.extend(other_selector)

        return self


def _ensure_selectors(items):
    items = _ensure_list(items)

    for i in range(len(items)):
        items[i] = _ensure_selector(items[i])

    return items


def _ensure_selector(item):
    from .JsSelector import JsSelector
    from .XPath import XPath
    from .Css import Css

    if isinstance(item, AbstractSelector):
        return item

    if hasattr(item, '__call__'):
        return _ensure_selector(item())

    if isinstance(item, str):
        if item.startswith("js:"):
            return JsSelector(item[3:])
        elif item.startswith("xpath:"):
            return XPath(item[6:])
        elif item.startswith("//"):
            return XPath(item)
        elif item.startswith("css:"):
            return Css(item[4:])
        else:
            return Css(item)

    raise Exception("The element given as a selector %s was not a valid selector"
                    "for this context." % item)


def _get_xpath_selectors(selector_objects):
    selector_objects = _ensure_selectors(selector_objects)
    result = []

    for selector in selector_objects:
        if isinstance(selector, PositionalFilterSelector):
            raise Exception("Positional selectors are not supported, only "
                            "selectors that will return XPath global searches, without positional "
                            "references.")

        if not isinstance(selector, AbstractSelector):
            raise Exception("The passed selector: %s is not an instance of "
                            "AbstractSelector, string, or callable that builds an "
                            "AbstractSelector." % selector)

        string_selectors = selector.get_selectors()

        for string_selector in string_selectors:
            is_xpath = _is_xpath_selector(string_selector)
            is_css = _is_css_selector(string_selector)

            if not is_xpath and not is_css:
                raise Exception("Only selectors that return XPath or CSS are supported "
                                "calls. Currently `%s` was found. When unsure use instead the "
                                "`germanium.selectors.Element` selector, since it generates "
                                "XPath, or CSS selectors, and they will be converted to "
                                "XPath." % string_selector)

            if is_css:
                if string_selector.startswith("css:"):
                    string_selector = string_selector[4:]

                string_selector = GenericTranslator().css_to_xpath(string_selector)

                # IE8 at least stutters if the descendant-or-self axis appears as a
                # sub part of the expression. E.g.: //asd/descendant-or-self::test

                string_selector = string_selector.replace("descendant-or-self::", "//")

            if string_selector.startswith("xpath://"):
                string_selector = string_selector[6:]

            result.append(string_selector)

    return result


import re

LOCATOR_SPECIFIER = re.compile(r'((\w[\w\d]*?)\:)(.*)', re.MULTILINE|re.DOTALL)


def _is_css_selector(selector):
    if selector == "alert" or selector.startswith("alert:"):
        return False

    if selector.startswith("//"):
        return False

    m = LOCATOR_SPECIFIER.match(selector)

    if not m:
        return True

    if m.group(2) == "css":
        return True

    return False


def _is_xpath_selector(selector):
    if selector == "alert" or selector.startswith("alert:"):
        return False

    if selector.startswith("//"):
        return True

    m = LOCATOR_SPECIFIER.match(selector)

    if not m:
        return False

    if m.group(2) == "xpath":
        return True

    return False
