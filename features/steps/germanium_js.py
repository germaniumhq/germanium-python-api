
from behave import *
from germanium.static import *

use_step_matcher("re")

@step(u'I execute js with one parameter \'(.*?)\'')
def step_impl(context, js_parameter):
    js(context.text, js_parameter)
