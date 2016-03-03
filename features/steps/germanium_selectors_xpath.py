from behave import *

from germanium.selectors import XPath

use_step_matcher("re")


@step(u'I look for the following xpath selector: (.*)')
def step_impl(context, expected_text):
    element = context.germanium.S(XPath(expected_text)).element()

    context.found_element = element

