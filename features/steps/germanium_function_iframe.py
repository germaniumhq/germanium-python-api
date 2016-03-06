from behave import *

from features.steps.asserts import *
from germanium.static import *

use_step_matcher("re")


@step(u'I type into the following text: (.*)')
def step_impl(context, text):
    type_keys(text)


@step(u'I type into iframe in (.*) the following text: (.*)')
@iframe('iframe')
def type_text_into_iframe_name(context, locator, text):
    type_keys(text, locator)


@step(u"in the iframe the value for the (.*?) is '(.*)'")
@iframe('iframe')
def check_value(context, locator, value):
    element = S(locator).element()

    assert_true(element)
    assert_equals(value, element.get_attribute("value"))
