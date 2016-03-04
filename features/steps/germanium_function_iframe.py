from behave import *

from germanium import type_keys, iframe

from features.steps.asserts import *

use_step_matcher("re")

@step(u'I type into the following text: (.*)')
def step_impl(context, text):
    type_keys(context.germanium, text)

@step(u'I type into iframe in (.*) the following text: (.*)')
@iframe('iframe')
def type_text_into_iframe_name(context, locator, text):
    type_keys(context.germanium, text, locator)

@step(u"in the iframe the value for the (.*?) is '(.*)'")
@iframe('iframe')
def check_value(context, locator, value):
    element = context.germanium.S(locator).element()

    assert_true(element)
    assert_equals(value, element.get_attribute("value"))
