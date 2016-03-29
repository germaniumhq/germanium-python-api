from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I search using selectors for an InputText above the text "(.*?)"')
def step_impl(context, text):
    element = InputText().above(Text(text)).element()

    assert element

    context.found_element = element


@step(u'I search using selectors for all InputText elements')
def step_impl(context):
    context.found_elements = InputText().element_list()


@step(u'I search using selectors if an InputText above the text "Surname" exists')
def step_impl(context):
    context.does_element_exist = InputText().above(Text("Surname")).exists()


@step(u'I search using selectors if an Image above the text "Surname" exists')
def step_impl(context):
    context.does_element_exist = Image().above(Text("Surname")).exists()


@step(u'yes, it exists')
def step_impl(context):
    assert context.does_element_exist


@step(u"no, it doesn't exists")
def step_impl(context):
    assert not context.does_element_exist
