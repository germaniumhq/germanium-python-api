from .global_germanium_instance import *

from selenium import webdriver
from selenium.webdriver import FirefoxProfile

from germanium import GermaniumDriver
from germanium.GermaniumDriver import NoopIFrameSelector


def open_browser(browser="Firefox",
                 wd=None,
                 iframe_selector=NoopIFrameSelector(),
                 screenshot_folder="screenshots",
                 scripts=list()):
    """
    Open the given browser.
    :param browser:
    :param wd:
    :param iframe_selector:
    :param screenshot_folder:
    :param scripts:
    """
    if get_instance():
        raise Exception("A browser already runs. Close it first with close_browser()")

    if wd:
        web_driver = wd
    elif browser.lower() == "firefox" or browser.lower() == "ff":
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 0)

        web_driver = webdriver.Firefox()
    elif browser.lower() == "chrome":
        web_driver = webdriver.Chrome()
    elif browser.lower() == "ie":
        web_driver = webdriver.Ie()
    else:
        raise Exception("Unknown browser: %s, only firefox, chrome and ie are supported." % browser)

    set_instance(GermaniumDriver(web_driver,
                                 iframe_selector=iframe_selector,
                                 screenshot_folder=screenshot_folder,
                                 scripts=scripts))

    return get_instance()
