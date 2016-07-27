from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I search for a TableRow with a CheckBox left of text "Surname"')
def step_impl(context):
    selector = TableRow() \
        .containing_all(TableCell("Surname")) \
        .containing_all(CheckBox())

    element = S(selector).element()

    assert element

    context.found_element = element


@step(u"I search for a TableRow with a Button that has label 'edit'")
def step_impl(context):
    selector = TableRow() \
        .containing(Button('edit'))

    element = S(selector).element()

    assert element

    context.found_element = element


@step(u"I search for a TableRow with a custom XPath that is (.*)")
def step_impl(context, xpath):
    selector = TableRow() \
        .containing(XPath(xpath))
    element = S(selector).element()

    assert element

    context.found_element = element


@step(u'I search for a TableRow with positional locator CheckBox left of "Surname"')
def step_impl(context):
    try:
        selector = TableRow() \
            .containing(CheckBox().left_of(Text("Surname")))

        element = S(selector).element()
    except Exception as e:
        context.exception = e


@step(u'it throws an exception')
def step_impl(context):
    assert context.exception
    print(context.exception)
