from ._element import _element
from .find_germanium_object import find_germanium_object


def child_nodes_g(context, selector, only_elements=True):
    germanium = find_germanium_object(context)
    element = _element(germanium, selector)

    return germanium.js("""
        var result = [];
        var element = arguments[0];
        var onlyElements = arguments[1];

        if (!element.childNodes) {
            return result;
        }

        for (var i = 0; i < element.childNodes.length; i++) {
            if (onlyElements && element.childNodes[i].nodeType != 1) {
                continue;
            }

            result.push(element.childNodes[i]);
        }

        return result;
    """, element, only_elements)
