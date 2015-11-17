from behave import *

use_step_matcher("re")

from germanium import GermaniumDriver

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


@then("the title of the page contains '(?P<what>.*?)'")
def check_title_page(context, what):
    context.germanium.quit()
