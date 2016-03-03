from behave import *

from germanium.selectors import Input, Text

use_step_matcher("re")


@step(u'I search for an Input left of the text "(.*?)"')
def step_impl(context, text):
    selector = Input().left_of(Text(text))
    element = context.germanium.S(selector).element()

    assert element

    context.found_element = element

@step(u'I search for an Input right of the text "(.*?)"')
def step_impl(context, text):
    selector = Input().right_of(Text(text))
    element = context.germanium.S(selector).element()

    assert element

    context.found_element = element

