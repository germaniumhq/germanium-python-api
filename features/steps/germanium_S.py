from germanium.static import *
from behave import *

use_step_matcher("re")


@step(u'I search using S for (?P<locator>.*)')
def step_impl(context, locator):
    print("Search for locator: %s" % locator)
    S(locator).exists()


@step(u"the selector '(.*?)' exists somewhere")
def step_impl(context, selector):
    assert S(selector).exists(only_visible=False)


@step(u"the selector '(.*?)' exists and is visible")
def step_impl(context, selector):
    assert S(selector).exists()


@step(u"the selector '(.*?)' doesn't exists at all")
def step_impl(context, selector):
    assert S(selector).not_exists(only_visible=False)


@step(u"the selector '(.*?)' doesn't exists as visible")
def step_impl(context, selector):
    assert S(selector).not_exists()


@step(u'nothing happens')
def step_impl(context):
    pass


@step(u"I search using a nested locator for '(.*?)'")
def step_impl(context, selector):
    element = S(S(selector)).element()

    context.found_element = element


@step(u"I search using a callable that returns a CssSelector '(.*?)'")
def step_impl(context, selector):
    def fn():
        return Css(selector)

    element = S(fn).element()

    context.found_element = element
