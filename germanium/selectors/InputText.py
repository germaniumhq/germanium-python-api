
from .Element import Element


class InputText(Element):
    """
    Just a selector that finds an input text by its name.
    """
    def __init__(self, placeholder=None, *args, **kw):
        extra_xpath = "[@type='text' or not(@type)]"

        if placeholder is not None:
            extra_xpath += "[@placeholder = '%s']" % placeholder

        super(InputText, self).__init__("input",
                                        extra_xpath=extra_xpath,
                                        *args,
                                        **kw)
