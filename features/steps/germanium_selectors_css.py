from behave import *

from germanium.selectors import Css

use_step_matcher("re")


@step(u'I look for the following css selector: (.*)')
def step_impl(context, expected_text):
    element = context.germanium.S(Css(expected_text)).element()

    context.found_element = element

