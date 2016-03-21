from time import sleep

import pkg_resources

from .SimpleSelector import SimpleSelector
from .locators import CssLocator, SimpleLocator, XPathLocator, JsLocator
from .iframe_selector import DefaultIFrameSelector, CallableIFrameSelector
from .create_locator import create_locator

from selenium.webdriver.remote.webelement import WebElement


class JavaScriptException(Exception):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return "JavaScriptException: %s - %s" % (self.name, self.message)


class GermaniumDriver(object):
    """
    A Germanium extension to top of WebDriver
    """
    def __init__(self,
                 web_driver,
                 iframe_selector=DefaultIFrameSelector(),
                 screenshot_folder="screenshots",
                 scripts=list()):

        if hasattr(iframe_selector, '__call__'):
            iframe_selector=CallableIFrameSelector(iframe_selector)

        self.web_driver = web_driver
        self.simple_selector = SimpleSelector(self)
        self._screenshot_folder = screenshot_folder
        self._iframe_selector = iframe_selector
        self._current_iframe = None
        self._scripts_to_load = scripts

        self.locator_map = {
            "simple": SimpleLocator,
            "xpath": XPathLocator,
            "css": CssLocator,
            "js": JsLocator
        }

        self.select_iframe("default")

    def S(self, locator, strategy='detect'):
        """ Finds an element by the given locator.
        :param locator:
        :param strategy:
        """
        return create_locator(self, locator, strategy)

    def get(self, url, *args, **kwargs):
        result = self.web_driver.get(url, *args, **kwargs)
        self.wait_for_page_to_load()

        return result

    def find_element_by_simple(self, locator):
        """
        Find an element using the simple locator.
        """
        return self.simple_selector.find_element(locator)

    def reload_page(self):
        """
        Reloads the page via JS, and waits for it to load.
        """
        self.js('document.location.reload();')
        self.wait_for_page_to_load()

    def execute_script(self, script, *args, **kwargs):
        """ deprecated js """
        return self.js(script, *args, **kwargs)

    #
    # This executes a script taking care of actually catching and rethrowing correctly
    # JavaScript exceptions.
    #
    # It takes special care for returning web elements directly since if they are exported
    # using a map, under python-3.4 webdriver gets dizzy, and returns the elements as "dict"
    #
    def js(self, script, *args, **kwargs):
        try:
            """
            Execute the script, and also display it on the console for debug purposes.
            """
            wrapper_script = """try {
                function __isElement(n) {
                    return n && n.nodeType && n.ownerDocument
                }

                function __isElementList(l) {
                    if (l && typeof l['length'] != 'undefined') {
                        for (var __i = 0; __i < l.length; __i++) {
                            if (!__isElement(l[__i])) {
                                return false;
                            }
                        }

                        return true;
                    }
                }

                var result = {
                    data : (function() {
                        %s
                    }).apply(this, arguments),
                    status : "SUCCESS"
                };

                return __isElement(result.data) || __isElementList(result.data) ?
                       result.data :
                       result;
            } catch (e) {
                return {  // return the exception information in case of failure.
                    status : "FAILURE",
                    name : e.name,
                    message : e.message
                };
            }
            """ % script

            eval_script = wrapper_script

            response = self.web_driver.execute_script(eval_script, *args, **kwargs)

            if isinstance(response, WebElement) or isinstance(response, list):
                return response

            if response['status'] == 'SUCCESS':
                return response['data']
            else:
                raise JavaScriptException( response['name'], response['message'] )
        except Exception as e:
            print(wrapper_script)
            print("Failure executing script: %s, error: %s" % (script, e))
            raise e


    def wait_for_page_to_load(self):
        """
        Wait for the page to load.
        """
        self.select_iframe("default")
        self.wait_for_javascript("""return "complete" == document["readyState"]""")

        self.load_simple_locator()  # automatically load the simple locator if waiting for the page to load finished.

        for script_name in self._scripts_to_load:
            self.load_script(script_name)

    def wait_for_action_to_complete(self, throttle=0):
        """
        Waits for all the AJAX and Page calls to finish.
        """
        self.wait_for_ajax_to_complete(throttle)
        self.wait_for_page_to_load()

    def wait_for_ajax_to_complete(self, throttle=0):
        """
        Waits for the action calls to complete.
        """
        self.wait_for_javascript("""window.AJAX_OPERATION_TIMEOUT = %s; return (!XMLHttpRequest.isAjaxRunning || ! XMLHttpRequest.isAjaxRunning()) && "complete" == document["readyState"];""" % throttle)

    def wait_for_javascript(self, script, timeout = 60):
        """
        Executes a script every 400 milliseconds until it returns true. If it goes more than timeout seconds, then this
        function throws an exception. If the given script throws an exception, it's assumed that it returned false.
        """
        start_time = 0 # FIXME: get actual start time.
        wrapper_script = """
            try {
                %s // original script
            } catch (e) {
                console.log(e);
                return false;
            }
        """ % script

        self.wait_for_closure(lambda : self.js(wrapper_script))

    def wait_for_closure(self, closure, timeout = 10):
        """
        Executes a function given as argument every 400 milliseconds until it returns true. If it goes more than
        the timeout seconds, then this function throws an exception. If the function throws an exception, then
        it is assumed it is false.
        """
        def closure_try_catch():
            try:
                return closure()
            except Exception as e:
                print("WARNING: waiting as false since: %s" % e)
                return False

        passed_timeout = 0
        while passed_timeout < timeout and not closure_try_catch():
            passed_timeout += 0.4

            if passed_timeout >= 2:
                print("Running takes more than 2 seconds.")

            sleep(0.4)

    def load_simple_locator(self):
        """
        Since the simple locator script is a bazillion bytes big, it should be loaded independently.
        """
        if self.js("return !window.locateElementBySimple"):
            self.load_script('simple-locator.js')
            self.load_script('ajax-interceptor.js')
            self.load_script('is-ajax-running.js')

    def load_script(self, script_name):
        """
        Load an external script into the current window context.
        """
        script = pkg_resources.resource_string(__name__, script_name)
        if type(script) != 'str':  # it is bytes
            script = script.decode('utf-8')

        self.js(script)

    def take_screenshot(self, name, *args, **kwargs):
        """
        Takes a screenshot of the current browser.
        :param name:
        :return:
        """
        path = self._screenshot_folder + "/" + name + ".png"
        self.web_driver.get_screenshot_as_file(path, *args, **kwargs)
        print("Screenshot saved as " + path)

    def select_iframe(self, iframe_name):
        """
        Selects the iframe, only if the iframe is different
        :param iframe_name:
        :return:
        """
        if iframe_name != self._current_iframe:
            self._current_iframe = self._iframe_selector.select_iframe(self, iframe_name)

        if not self._current_iframe:
            self._current_iframe = iframe_name

        return self._current_iframe

    def __getattr__(self, item):
        """
        Delegate all the attributes that are missing to the web_driver.
        :param item:
        :return:
        """
        if "current_iframe" == item:
            return self._current_iframe

        return getattr(self.web_driver, item)
