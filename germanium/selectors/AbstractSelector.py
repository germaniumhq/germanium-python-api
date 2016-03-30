from germanium.impl import _ensure_list


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

    def element_list(self, *argv, germanium=None, **kw):
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
        return S(self, germanium=germanium).element_list(*argv, **kw)

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


class XPathInsideFilterSelector(AbstractSelector):
    def __init__(self, parent_selector):
        super(XPathInsideFilterSelector, self).__init__()

        self._selectors = list(parent_selector.get_selectors())

    def get_selectors(self):
        return self._selectors

    def inside(self, *argv, **kw):
        new_selectors = []
        inside_xpath_string_selectors = _get_xpath_selectors(argv)

        for inside_selector in inside_xpath_string_selectors:
            for reference_selector in self._selectors:
                new_selectors.append(inside_selector + reference_selector)

        self._selectors = new_selectors

        return self

    def containing(self, *argv, **kw):
        new_selectors = []
        containing_xpath_string_selectors = _get_xpath_selectors(argv)

        for reference_selector in self._selectors:
            for containing_selector in containing_xpath_string_selectors:
                new_selectors.append("%s[.%s]" % (reference_selector, containing_selector))

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

    from .JsSelector import JsSelector
    from .XPath import XPath
    from .Css import Css

    for i in range(len(items)):
        item = items[i]

        if isinstance(item, str):
            if item.startswith("js:"):
                items[i] = JsSelector(item[3:])
            elif item.startswith("xpath:"):
                items[i] = XPath(item[6:])
            elif item.startswith("//"):
                items[i] = XPath(item)
            elif item.startswith("css"):
                items[i] = Css(item)
            else:
                items[i] = Css(item)

    return items


def _get_xpath_selectors(selector_objects):
    selector_objects = _ensure_selectors(selector_objects)
    result = []

    for selector in selector_objects:
        if isinstance(selector, PositionalFilterSelector):
            raise Exception("Positional selectors are not supported, only "
                            "selectors that will return XPath global searches, without positional "
                            "references.")

        string_selectors = selector.get_selectors()

        for string_selector in string_selectors:
            if not string_selector.startswith("//") \
                    and not string_selector.startswith("xpath://"):
                raise Exception("Only selectors that return XPath are supported "
                                "calls. Currently `%s` was found. In case you want to use a CSS selector, "
                                "use instead the `germanium.selectors.Element` selector, since it "
                                "generates XPath." % string_selector)

        for string_selector in string_selectors:
            if string_selector.startswith("xpath://"):
                string_selector = string_selector[6:]

            result.append(string_selector)

    return result
