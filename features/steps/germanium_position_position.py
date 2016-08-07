from behave import *

from features.steps.asserts import *
from germanium.static import *

use_step_matcher("re")


@step("I click on the top left corner of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_left())


@step("I click on the top right corner of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_right())


@step("I click on the bottom left corner of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).bottom_left())


@step("I click on the bottom right corner of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).bottom_right())


@step("the text of the '(.*?)' is '(.*?)'")
def verify_text(context, selector, expected_text):
    assert_equals(expected_text, get_text(selector))
