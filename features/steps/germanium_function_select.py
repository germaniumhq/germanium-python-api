from behave import *

from germanium.static import *
from features.steps.asserts import *

use_step_matcher("re")


@step(u"I select in the first select the entry with text 'A1'")
def step_impl(context):
    select("#firstSelect", "A1")


@step(u"I select in the first select the entry with value 'a2value'")
def step_impl(context):
    select("#firstSelect", value="a2value")


@step(u"I select in the first select the entry with index 3")
def step_impl(context):
    select("#firstSelect", index="3")


@step(u"the value in the first select is '(.*?)'")
def step_impl(context, expected_value):
    assert_equals(expected_value, get_value("#firstSelect"))
