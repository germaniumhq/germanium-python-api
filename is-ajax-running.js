var lastCheckedTime = -1,
    OPERATION_TIMEOUT = 400;

XMLHttpRequest.interceptorsBefore.push(function() {
    lastCheckedTime = -1;
});

XMLHttpRequest.interceptorsAfter.push(function() {
    lastCheckedTime = -1;
});

XMLHttpRequest.isAjaxRunning = function() {
    if (lastCheckedTime < 0) {
        lastCheckedTime = new Date().getTime();
        return true;
    }

    var currentTime = new Date().getTime();

    if (currentTime - lastCheckedTime > OPERATION_TIMEOUT && XMLHttpRequest.runningCalls == 0) {
        lastCheckedTime = -1;
        return false;
    }

    return true;
};