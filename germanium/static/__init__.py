from germanium import GermaniumDriver,\
    type_keys as type_keys_impl,\
    iframe as iframe_impl, \
    right_click as right_click_impl, \
    click as click_impl, \
    hover as hover_impl, \
    double_click as double_click_impl
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
    """
    Close the currently running browser.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    global_germanium.quit()
    global_germanium = None

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
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    click_impl(global_germanium, where)

def hover(where):
    """
    Hover the element with the given selector.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    hover_impl(global_germanium, where)

def double_click(where):
    """
    Double click the element with the given selector.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    double_click_impl(global_germanium, where)

def right_click(where):
    """
    Right click the element with the given selector.
    """
    global global_germanium

    if not global_germanium:
        raise Exception("You need to start a browser first with open_browser()")

    right_click_impl(global_germanium, where)

def get_web_driver():
    """
    Returns the currently used web_driver object by germanium.
    """
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

def iframe(target, keep_new_context = False):
    """
    Allow using the iframe method in static contexts.
    """
    def wrapper(original):
        @iframe_impl(target, keep_new_context)
        def original_aspect(*args, **kwargs):
            return original(*args, **kwargs)

        return original_aspect

    return wrapper

