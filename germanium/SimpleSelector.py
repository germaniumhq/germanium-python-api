import traceback
import sys


class SimpleSelector(object):
    """
    A SimpleSelector object that is able to find elements
    using the magic of the simple locator.
    """
    def __init__(self, germanium_driver):
        self.germanium_driver = germanium_driver

    def find_element(self, locator):
        """
        Finds several elements using the simple locator.
        Always use two sets of quotes for simple locator arguments! Even for a simple string!!!
        """
        script = "return parent.locateElementBySimple('%s', document);" % (locator.replace("\'", "\\'"))  #escape single quotes

        try:
            return self.germanium_driver.execute_script(script)
        except Exception:  # assume it failed because of the locator
            self.germanium_driver.load_simple_locator()
            try:
                return self.germanium_driver.execute_script(script)
            except Exception as e:
                traceback.print_exc( sys.stdout )
                raise e
