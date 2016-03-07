


def get_attributes(context, selector):
    """
    Return the attribute names for the element is obtained from the selector.
    :param context:
    :param selector:
    :return:
    """
    germanium = find_germanium_object([context])
    element = germanium.S(element).element()


