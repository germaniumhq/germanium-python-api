from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I search for an Input left of the text "(.*?)"')
def step_impl(context, text):
    selector = Input().left_of(Text(text))
    element = S(selector).element()

    assert element

    context.found_element = element


@step(u'I search for an Input right of the text "(.*?)"')
def step_impl(context, text):
    selector = Input().right_of(Text(text))
    element = S(selector).element()

    assert element

    context.found_element = element


@step(u'I search for an InputText above the text "(.*?)"')
def step_impl(context, text):
    selector = InputText().above(Text(text))
    element = S(selector).element()

    assert element

    context.found_element = element

@step(u'I search for an InputText below the text "(.*?)"')
def step_impl(context, text):
    selector = InputText().below(Text(text))
    element = S(selector).element()

    assert element

    context.found_element = element
