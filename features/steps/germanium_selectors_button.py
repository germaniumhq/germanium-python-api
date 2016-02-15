from behave import *
from germanium.selectors import Button, Text

use_step_matcher("re")

@step(u'I look for a button with the text: \'(.*?)\'')
def step_impl(context, expected_text):
    element = context.germanium.S(Button(expected_text)).element()

    assert element

    context.found_element = element

@step(u'I look for a button with the name: \'(.*?)\'')
def step_impl(context, expected_name):
    element = context.germanium.S(Button(name=expected_name)).element()

    assert element

    context.found_element = element

@step(u'I find the element with id: \'(.*?)\'')
def step_impl(context, actualId):
    assert context.found_element.get_attribute('id') == actualId

@step(u'I look for some text: \'(.*?)\'')
def step_impl(context, text):
    element = context.germanium.S(Text(text)).element()

    assert element

    context.found_element = element
