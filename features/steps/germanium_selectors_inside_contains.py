from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I search for an InputText inside the div with id inputTextContainer')
def step_impl(context):
    selector = InputText().inside(Element("div", id="inputTextContainer"))
    element = S(selector).element()

    assert element

    context.found_element = element


@step(u'I search for a div containing an InputText')
def step_impl(context):
    selector = Element("div").containing(InputText())
    element = S(selector).element()

    assert element

    context.found_element = element


@step(u'I search for a div inside a CSS selector')
def step_impl(context):
    try:
        selector = Element("div").inside(".what")
    except Exception as e:
        context.exception = e


@step(u'I search for a div containing a CSS selector')
def step_impl(context):
    try:
        selector = Element("div").containing(".what")
    except Exception as e:
        context.exception = e
