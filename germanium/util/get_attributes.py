from selenium.webdriver.remote.webelement import WebElement

from .find_germanium_object import find_germanium_object


def get_attributes_g(context, selector, only_visible=True):
    """
    Return the attributes for the element that is obtained
    from the selector as a dictionary object.
    :param context:
    :param selector:
    :param only_visible:
    :return:
    """
    germanium = find_germanium_object(context)

    if isinstance(selector, WebElement):
        element = selector
    else:
        element = germanium.S(selector).element(only_visible=only_visible)

    if not element:
        raise Exception("Unable to find '%s' to get_attributes." % selector)

    return germanium.js("""
        var attributes = arguments[0].attributes;
        var result = {};

        for (var i = 0; i < attributes.length; i++) {
            if (attributes[i].specified) {
                result[attributes[i].name] = attributes[i].value;
            }
        }

        return result;
    """, element)
