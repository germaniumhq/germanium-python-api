from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I look for the following js selector: (.*)')
def step_impl(context, code):
    element = S(JsSelector(code)).element()

    context.found_element = element
