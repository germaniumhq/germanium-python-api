from germanium import GermaniumDriver, type_keys as type_keys_impl
from germanium.selectors import *

from selenium import webdriver
from selenium.webdriver import FirefoxProfile

global_germanium = None

def open_browser(browser = "Firefox", wd = None):
    """
    Open the given browser.
    """
    global global_germanium

    if global_germanium:
        raise Exception("A browser already runs. Close it first with close_browser()")

    if wd:
        web_driver = wd
    elif browser.lower() == "firefox" or browser.lower() == "ff":
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 0)

        web_driver = webdriver.Firefox(firefox_profile)
    elif browser.lower() == "chrome":
        web_driver = webdriver.Chrome()
    elif browser.lower() == "ie":
        web_driver = webdriver.Ie()
    else:
        raise Exception("Unknown browser: %s, only firefox, chrome and ie are supported." % browser)

    global_germanium = GermaniumDriver(web_driver)

    return global_germanium

def close_browser():
    """ Close the currently running browser. """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    global_germanium.quit()

def go_to(url):
    """
    Go to the given URL, and wait for the page to load.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    global_germanium.get(url)

def type_keys(what, where = None):
    """
    Type the keys specified into the element, or the currently active element.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    element = None

    if where:
        element = global_germanium.S(where).element()

    type_keys_impl(global_germanium, what, element)

def click(where):
    """
    Click the element with the given selector.
    """
    element = global_germanium.S(where).element()
    element.click()

def double_click(where):
    pass

def right_click(where):
    pass

def get_web_driver():
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    return global_germanium.web_driver

def get_germanium():
    global global_germanium

    return global_germanium

def S(*argv, **kwargs):
    """
    Call the super selector from germanium.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    return global_germanium.S(*argv, **kwargs)

