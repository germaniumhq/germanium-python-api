from behave import *
from germanium.static import *

from features.steps.asserts import *

use_step_matcher("re")


@step("I click on the top left corner of '(.*?)'")
def i_click_on_top_left_corner(context, selector):
    click(Box(selector).top_left())


@step("the text of the '(.*?)' is '(.*?)'")
def verify_text(context, selector, expected_text):
    assert get_text(selector) == expected_text
