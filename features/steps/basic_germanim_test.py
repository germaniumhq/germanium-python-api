from behave import *
from time import sleep

from germanium import GermaniumDriver, type_keys

from selenium import webdriver
from selenium.webdriver import FirefoxProfile

import os

import g

use_step_matcher("re")

def instantiate_germanium_webdriver():
    browser = None
    web_driver = None

    if 'TEST_BROWSER' in os.environ:
        browser = os.environ['TEST_BROWSER']

    if browser.lower() == "firefox":
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 0)

        web_driver = webdriver.Firefox(firefox_profile)
    elif browser.lower() == "chrome":
        web_driver = webdriver.Chrome()
    elif browser.lower() == "ie":
        web_driver = webdriver.Ie()
    else:
        raise Exception("Unknown browser: %s, only firefox, chrome and ie are supported." % browser)

    return GermaniumDriver(web_driver)


@step("I open (.*?)")
def open_browser(context, browser):
    """
    :param context:
    :return: void
    """
    if 'TEST_REUSE_BROWSER' in os.environ:
        if not g.global_germanium:
            g.global_germanium = instantiate_germanium_webdriver()

        context.germanium = g.global_germanium
    else:
        context.germanium = instantiate_germanium_webdriver()


@step("I go to '(?P<page>.*?)'")
@step("I navigate to '(?P<page>.*?)'")
def navigate_to_page(context, page):
    """
    Navigate to the given URL.
    :param context:
    :param page:
    :return:
    """
    context.germanium.get(page)

@step(u'I type \'(?P<keys>.*?)\' into (?P<simple_locator>.*)')
def type_keys_with_simple_locator(context, keys, simple_locator):
    element = context.germanium.S(simple_locator).element()
    element.send_keys(keys)


@step(u'the value for the (?P<simple_locator>.*) is \'(?P<value>.*?)\'')
def step_impl(context, simple_locator, value):
    element = context.germanium.S(simple_locator).element()
    assert element.get_attribute("value") == value


@step("the title of the page equals '(?P<what>.*?)'")
def check_title_page(context, what):
    assert context.germanium.title == what

@step(u'I type_keys \'(?P<what>.*?)\'')
def type_keys_impl(context, what):
    type_keys(context, what)

@step(u'I click on (?P<simple_locator>.*)')
def step_impl(context, simple_locator):
    element = context.germanium.S(simple_locator).element()
    element.click()

@step(u'I wait forever')
def step_impl(context):
    sleep(10000000)
