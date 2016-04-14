import re

from selenium import webdriver

from germanium.driver import GermaniumDriver
from germanium.iframe_selector import DefaultIFrameSelector
from .global_germanium_instance import *

REMOTE_ADDRESS = re.compile(r"^(\w+?):(.*?)$")


def open_browser(browser="Firefox",
                 wd=None,
                 iframe_selector=DefaultIFrameSelector(),
                 screenshot_folder="screenshots",
                 scripts=list(),
                 timeout=60):
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

    remote_match = REMOTE_ADDRESS.match(browser)

    if wd:
        web_driver = wd
    elif remote_match:
        remote_browser = remote_match.group(1)

        if remote_browser.lower() == "firefox" or remote_browser.lower() == "ff":
            remote_capabilities = webdriver.DesiredCapabilities.FIREFOX
        elif remote_browser.lower() == "chrome":
            remote_capabilities = webdriver.DesiredCapabilities.CHROME
        elif remote_browser.lower() == "ie":
            remote_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        else:
            raise Exception("Unknown browser: %s, only firefox, "
                            "chrome and ie are supported." % browser)

        web_driver = webdriver.Remote(command_executor=remote_match.group(2),
                                      desired_capabilities=remote_capabilities)
    elif browser.lower() == "firefox" or browser.lower() == "ff":
        web_driver = webdriver.Firefox(timeout=timeout)
    elif browser.lower() == "chrome":
        web_driver = webdriver.Chrome()
    elif browser.lower() == "ie":
        web_driver = webdriver.Ie(timeout=timeout)
    else:
        raise Exception("Unknown browser: %s, only firefox, "
                        "chrome and ie are supported." % browser)

    set_instance(GermaniumDriver(web_driver,
                                 iframe_selector=iframe_selector,
                                 screenshot_folder=screenshot_folder,
                                 scripts=scripts))

    return get_instance()
