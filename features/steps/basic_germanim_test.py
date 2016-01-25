from behave import *
from time import sleep

use_step_matcher("re")

from germanium import GermaniumDriver, type_keys

from selenium import webdriver
from selenium.webdriver import FirefoxProfile

@step("I open firefox")
def open_browser(context):
    """
    :param context:
    :return: void
    """
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("network.proxy.type", 0)

    context.germanium = GermaniumDriver(
        webdriver.Firefox(firefox_profile))

@when("I go to '(?P<page>.*?)'")
@when("I navigate to '(?P<page>.*?)'")
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
    element = context.germanium.find_element_by_simple(simple_locator)
    element.send_keys(keys)


@step(u'the value for the (?P<simple_locator>.*) is \'(?P<value>.*?)\'')
def step_impl(context, simple_locator, value):
    element = context.germanium.find_element_by_simple(simple_locator)
    assert element.get_attribute("value") == value


@step("the title of the page equals '(?P<what>.*?)'")
def check_title_page(context, what):
    assert context.germanium.title == what

@step(u'I type_keys \'(?P<what>.*?)\'')
def type_keys_impl(context, what):
    type_keys(context, what)

@step(u'I click on (?P<simple_locator>.*)')
def step_impl(context, simple_locator):
    element = context.germanium.find_element_by_simple(simple_locator)
    element.click()

