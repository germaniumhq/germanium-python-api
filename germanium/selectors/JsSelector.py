from .AbstractSelector import AbstractSelector


class JsSelector(AbstractSelector):
    """
    Just a selector that finds some elements using some
    Js code. The code must return a single WebDriver element.
    """
    def __init__(self, code=None):
        super(JsSelector, self).__init__()

        self._code = code

    def get_selectors(self):
        """ Return the JavaScript selector itself """
        return ["js:" + self._code]
