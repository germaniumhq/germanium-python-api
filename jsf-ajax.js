(function() {

var ajaxCallsRunning = 0;
var interval = setInterval(function() {
    if (jsf && jsf.ajax && jsf.ajax.addOnEvent) {
        jsf.ajax.addOnEvent(function(ev) {
            if (ev.status === "begin") {
                ajaxCallsRunning++;
            }

            if (ev.status === "complete") {
                ajaxCallsRunning--;
            }
        });

        jsf.ajax.isAjaxRunning = function() {
            return ajaxCallsRunning > 0;
        };

        clearInterval(interval);
    }
}, 100);

})();
