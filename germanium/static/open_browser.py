import re

import germaniumdrivers
from selenium import webdriver

from germanium.driver import GermaniumDriver
from germanium.iframe_selector import DefaultIFrameSelector
from germanium.impl._workaround import workaround
from germanium.wa.firefox_open_browser_with_marionette import \
    _is_use_marionette_evironment_var_set, \
    _open_local_firefox_with_marionette
from .global_germanium_instance import *


REMOTE_ADDRESS = re.compile(r"^(\w+?):(.*?)$")


@workaround(_is_use_marionette_evironment_var_set,
            _open_local_firefox_with_marionette)
def _open_local_firefox(timeout):
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX

    return webdriver.Firefox(capabilities=firefox_capabilities,
                             timeout=timeout)


def _open_local_chrome(timeout):
    germaniumdrivers.ensure_driver("chrome")
    return webdriver.Chrome()


def _open_local_ie(timeout):
    germaniumdrivers.ensure_driver("ie")
    capabilities = {"requireWindowFocus": True}
    return webdriver.Ie(timeout=timeout,
                        capabilities=capabilities)


def _open_local_edge(timeout):
    germaniumdrivers.ensure_driver("edge")
    return webdriver.Edge()


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
            remote_capabilities = dict(webdriver.DesiredCapabilities.INTERNETEXPLORER)
            remote_capabilities["requireWindowFocus"] = True
        elif remote_browser.lower() == "edge":
            remote_capabilities = webdriver.DesiredCapabilities.EDGE
        else:
            raise Exception("Unknown browser: %s, only firefox, "
                            "chrome and ie are supported." % browser)

        web_driver = webdriver.Remote(command_executor=remote_match.group(2),
                                      desired_capabilities=remote_capabilities)
    elif browser.lower() == "firefox" or browser.lower() == "ff":
        web_driver = _open_local_firefox(timeout)
    elif browser.lower() == "chrome":
        web_driver = _open_local_chrome(timeout)
    elif browser.lower() == "ie":
        web_driver = _open_local_ie(timeout)
    elif browser.lower() == "edge":
        web_driver = _open_local_edge(timeout)
    else:
        raise Exception("Unknown browser: %s, only firefox, "
                        "chrome and ie are supported." % browser)

    set_instance(GermaniumDriver(web_driver,
                                 iframe_selector=iframe_selector,
                                 screenshot_folder=screenshot_folder,
                                 scripts=scripts))

    return get_instance()
