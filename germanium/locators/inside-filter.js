//noinspection JSAnnotator,JSUnresolvedVariable,JSReferencingArgumentsOutsideOfFunction,ThisExpressionReferencesGlobalObjectJS
return (function() {
    var insideElements = [],
        containingElements = [],
        withoutChildren,
        elements = [],
        i, j,
        count,
        args;

    args = [];
    for (i = 0; i < arguments.length; i++) {
        args.push(arguments[i]);
    }

    function readElements(targetArray) {
        count = args.shift();
        while (count--) {
            targetArray.push(args.shift());
        }
    }

    withoutChildren = args.shift();
    readElements(insideElements);
    readElements(containingElements);
    readElements(elements);

    function isInside(parentNode, childNode) {
        if (!childNode || !parentNode) {
            return false;
        }

        while (childNode) {
            if (childNode == parentNode) {
                return true;
            }

            childNode = childNode.parentNode;
        }

        return false;
    }

    if (withoutChildren) {
        for (i = elements.length - 1; i >= 0; i--) {
            if (elements[i].childNodes &&
                elements[i].childNodes.length) {

                elements.splice(i, 1);
            }
        }
    }

    if (insideElements.length) {
        nextI:
        for (i = elements.length - 1; i >= 0; i--) {
            for (j = 0; j < insideElements.length; j++) {
                if (isInside(insideElements[j], elements[i])) {
                    continue nextI;
                }
            }

            elements.splice(i, 1);
        }
    }

    if (containingElements.length) {
        nextI:
        for (i = elements.length - 1; i >= 0; i--) {
            for (j = 0; j < containingElements.length; j++) {
                if (isInside(elements[i], containingElements[j])) {
                    continue nextI;
                }
            }

            elements.splice(i, 1);
        }
    }

    return elements;
}.apply(this, arguments));
