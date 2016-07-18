//noinspection JSAnnotator,JSUnresolvedVariable,JSReferencingArgumentsOutsideOfFunction,ThisExpressionReferencesGlobalObjectJS
return (function() {
    var aboveElements = [],
        belowElements = [],
        rightOfElements = [],
        leftOfElements = [],
        elements = [],
        i, j,
        count,
        args;

    args = Array.prototype.splice.call(arguments, 0);
    // console.log("Running on: " + args);

    function readElements(targetArray) {
        count = args.shift();
        while (count--) {
            targetArray.push(args.shift());
        }
    }

    function left(element) {
        var result = 0;
        while (element && element != document.body) {
            result += element.offsetLeft;
            element = element.offsetParent;
        }

        return result;
    }

    function top(element) {
        var result = 0;
        while (element && element != document.body) {
            result += element.offsetTop;
            element = element.offsetParent;
        }

        return result;
    }

    function right(element) {
        var result = element.offsetWidth;
        while (element && element != document.body) {
            result += element.offsetLeft;
            element = element.offsetParent;
        }

        return result;
    }

    function bottom(element) {
        var result = element.offsetHeight;
        while (element && element != document.body) {
            result += element.offsetTop;
            element = element.offsetParent;
        }

        return result;
    }

    readElements(aboveElements);
    readElements(rightOfElements);
    readElements(belowElements);
    readElements(leftOfElements);
    readElements(elements);

    // console.log("above", aboveElements);
    // console.log("rightOf", rightOfElements);
    // console.log("below", belowElements);
    // console.log("leftOf", leftOfElements);

    for (i = elements.length - 1; i >= 0; i--) {
        for (j = 0; j < aboveElements.length; j++) {
            if (bottom(elements[i]) >= top(aboveElements[j])) {
                elements.splice(i, 1)
            }
        }
    }

    for (i = elements.length - 1; i >= 0; i--) {
        for (j = 0; j < belowElements.length; j++) {
            if (top(elements[i]) <= bottom(belowElements[j])) {
                elements.splice(i, 1)
            }
        }
    }

    for (i = elements.length - 1; i >= 0; i--) {
        for (j = 0; j < leftOfElements.length; j++) {
            if (right(elements[i]) >= left(leftOfElements[j])) {
                elements.splice(i, 1)
            }
        }

        if (leftOfElements.length) {
            var topReference = top(leftOfElements[0]);

            elements.sort(function(e1, e2) {
                return Math.pow(Math.abs(topReference - top(e1)), 2) -
                    Math.pow(Math.abs(topReference - top(e2)), 2);
            });
        }
    }

    for (i = elements.length - 1; i >= 0; i--) {
        for (j = 0; j < rightOfElements.length; j++) {
            if (left(elements[i]) <= right(rightOfElements[j])) {
                elements.splice(i, 1)
            }
        }

        if (rightOfElements.length) {
            var topReference = top(rightOfElements[0]);

            elements.sort(function(e1, e2) {
                return Math.pow(Math.abs(topReference - top(e1)), 2) -
                    Math.pow(Math.abs(topReference - top(e2)), 2);
            });
        }
    }

    return elements;
}.apply(this, arguments));