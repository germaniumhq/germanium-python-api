from behave import *

use_step_matcher("re")

@step(u'I search using S for (?P<locator>.*)')
def step_impl(context, locator):
    print("Search for locator: %s" % locator)
    context.germanium.S(locator).exists()

@step(u'nothing happens')
def step_impl(context):
    pass
