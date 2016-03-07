from behave import *
from germanium.static import *
from features.steps.asserts import *

use_step_matcher("re")


@step(u'I get the (.*?) element attributes')
def step_impl(context, selector):
    context.found_attributes = get_attributes(selector)


@step('there are 4 attributes')
def step_impl(context):
    assert_equals(4, len(context.found_attributes))


@step("the attribute '(.*?)' is '(.*?)'")
def step_impl(context, name, value):
    assert_equals(value, context.found_attributes[name])
