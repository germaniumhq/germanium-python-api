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

    var _top = top(element),
        _right = right(element),
        _bottom = bottom(element),
        _left = left(element),
        _width = _right - _left,
        _height = _bottom - _top,
        _center = _left + parseInt(_width / 2),
        _middle = _top + parseInt(_height / 2);

    // the right and the bottom values need to be adjusted to be inside
    // the box.

    _right -= 1;
    _bottom -= 1;

    return [_top, _right, _bottom, _left, _center, _middle, _width, _height];
}.apply(this, arguments));
