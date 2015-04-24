from time import sleep
import pkg_resources
from SimpleSelector import SimpleSelector


class GermaniumDriver(object):
    """
    A Germanium extension to top of WebDriver
    """
    def __init__(self, web_driver, screenshot_folder="screenshots"):
        self.web_driver = web_driver
        self.simple_selector = SimpleSelector(self)
        self._screenshot_folder = screenshot_folder

    def find_element_by_simple(self, locator):
        """
        Find an element using the simple locator.
        """
        return self.simple_selector.find_element(locator)


    def reload_page(self):
        """
        Reloads the page via JS, and waits for it to load.
        """
        self.execute_script('document.location.href = document.location.href;')
        self.wait_for_page_to_load()


    def execute_script(self, script):
        """
        Execute the script, and also display it on the console for debug purposes.
        """
        try:
            wrapper_script = """try {
                return {
                    data : (function() {
                        %s
                    })(),
                    status : "SUCCESS"
                };
            } catch (e) {
                return {  // return the exception information in case of failure.
                    status : "FAILURE",
                    name : e.name,
                    message : e.message
                };
            }
            """ % script

            #eval_script = wrapper_script % (script,)
            eval_script = script

            return self.web_driver.execute_script(eval_script)

            # this is for when using the wrapper script.
            #if response['status'] == 'SUCCESS':
            #    return response['data']
            #else:
            #    raise JavaScriptException( response['name'], response['message'] )


        except Exception as e:
           # print "Script failed. `%s`" % eval_script
            raise Exception(e)


    def wait_for_page_to_load(self):
        """
        Wait for the page to load.
        """
        self.wait_for_javascript("""return "complete" == document["readyState"]""")
        self.load_simple_locator() #automatically load the simple locator if waiting for the page to load finished.


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

        self.wait_for_closure(lambda : self.execute_script(wrapper_script))

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
                print "WARNING: waiting as false since: %s" % e
                return False

        passed_timeout = 0
        while passed_timeout < timeout and not closure_try_catch():
            passed_timeout += 0.4
            sleep(0.4)


    def load_simple_locator(self):
        """
        Since the simple locator script is a bazillion bytes big, it should be loaded independently.
        """
        self.load_script('simple-locator.js')


    def load_script(self, script_name):
        """
        Load an external script into the current window context.
        """
        script = pkg_resources.resource_string(__name__, script_name)
        self.execute_script(script)

    def take_screenshot(self, name):
        """
        Takes a screenshot of the current browser.
        :param name:
        :return:
        """
        self.web_driver.get_screenshot_as_file(self._screenshot_folder + "/" + name + ".png")

    def __getattr__(self, item):
        """
        Delegate all the gett attributes that are missing to the web_driver.
        :param item:
        :return:
        """
        return getattr(self.web_driver, item)
