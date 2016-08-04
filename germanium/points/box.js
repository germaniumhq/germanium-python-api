//noinspection JSAnnotator,JSReferencingArgumentsOutsideOfFunction,JSUnresolvedVariable,ThisExpressionReferencesGlobalObjectJS
return (function() {
    var style = document.body.currentStyle ||
                window.getComputedStyle(document.body);

    var bodyMarginTop = parseInt(style.marginTop),
        bodyMarginLeft = parseInt(style.marginLeft);

    function left(element) {
        var result = - bodyMarginLeft;
        while (element && element != document.body) {
            result += element.offsetLeft;
            element = element.offsetParent;
        }

        return result;
    }

    function top(element) {
        var result = - bodyMarginTop;
        while (element && element != document.body) {
            result += element.offsetTop;
            element = element.offsetParent;
        }

        return result;
    }

    function right(element) {
        var result = element.offsetWidth - bodyMarginLeft;
        while (element && element != document.body) {
            result += element.offsetLeft;
            element = element.offsetParent;
        }

        return result;
    }

    function bottom(element) {
        var result = element.offsetHeight - bodyMarginTop;
        while (element && element != document.body) {
            result += element.offsetTop;
            element = element.offsetParent;
        }

        return result;
    }

    var element = arguments[0];

    return [top(element), right(element), bottom(element), left(element)];
}.apply(this, arguments));
