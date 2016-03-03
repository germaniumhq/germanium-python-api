
class AbstractSelector(object):
    """
    Just a marker interface.
    """
    def __init__(self):
        pass

    def get_selectors(self):
        raise Exception("Abstract class, not implemented.")

    def left_of(self, other_selector):
        return PositionalFilterSelector(self)\
            .left_of(other_selector)

    def right_of(self, other_selector):
        return PositionalFilterSelector(self) \
            .right_of(other_selector)

    def above(self, other_selector):
        return PositionalFilterSelector(self) \
            .above(other_selector)

    def below(self, other_selector):
        return PositionalFilterSelector(self) \
            .below(other_selector)


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

    def left_of(self, other_selector):
        self.left_of_filters.append(other_selector)
        return self

    def right_of(self, other_selector):
        self.right_of_filters.append(other_selector)
        return self

    def above(self, other_selector):
        self.above_filters.append(other_selector)
        return self

    def below(self, other_selector):
        self.below_filters.append(other_selector)
        return self
