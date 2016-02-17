from behave import *
from germanium.selectors import Link

use_step_matcher("re")

@step(u'I look for a link with some text: \'(.*?)\'')
def step_impl(context, text):
    element = context.germanium.S(Link(text)).element()

    assert element

    context.found_element = element

@step(u'I look for a link with exactly the text: \'(.*?)\'')
def step_impl(context, text):
    element = context.germanium.S(Link(text=text)).element()

    assert element

    context.found_element = element

@when(u'I look for a link with the href: \'(.*?)\'')
def step_impl(context, href):
    element = context.germanium.S(Link(href=href)).element()

    assert element

    context.found_element = element

