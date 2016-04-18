from behave import *
from germanium.static import *

from features.steps.asserts import *

use_step_matcher("re")


@step(u"I get the text from element '(.*?)'")
def step_impl(context, selector):
    e = S(selector).element(only_visible=False)
    context.element_text = get_text(e)


@step(u"the text from that element is")
def step_impl(context):
    assert_equals(context.text, context.element_text)
