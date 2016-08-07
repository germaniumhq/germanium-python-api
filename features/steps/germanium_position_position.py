from behave import *

from features.steps.asserts import *
from germanium.static import *

use_step_matcher("re")


@step("I click on the exact element of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(selector)


@step("I click on the center of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).center())


@step("I click on the top left of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_left())


@step("I click on the top center of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_center())


@step("I click on the top right of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_right())


@step("I click on the middle left of '(.*?)'")
def i_click_on_the_middle_left(context, selector):
    click(Box(selector).middle_left())


@step("I click on the middle right of '(.*?)'")
def i_click_on_middle_right_corner(context, selector):
    click(Box(selector).middle_right())


@step("I click on the bottom left of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).bottom_left())


@step("I click on the bottom center of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).bottom_center())


@step("I click on the bottom right of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).bottom_right())


@step("the text of the '(.*?)' is '(.*?)'")
def verify_text(context, selector, expected_text):
    assert_equals(expected_text, get_text(selector))
