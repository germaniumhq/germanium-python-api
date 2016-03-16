from .Element import Element


class TableCell(Element):
    def __init__(self, contains_text=None, *argv, **kw):
        super(TableCell, self).__init__("td", contains_text=contains_text, *argv, **kw)
