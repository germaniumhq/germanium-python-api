from behave import *

from germanium.selectors import JsSelector

use_step_matcher("re")


@step(u'I look for the following js selector: (.*)')
def step_impl(context, code):
    element = context.germanium.S(JsSelector(code)).element()

    context.found_element = element

