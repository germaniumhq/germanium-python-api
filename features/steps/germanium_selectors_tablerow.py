from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u'I search for a TableRow with a CheckBox left of text "Surname"')
def step_impl(context):
    selector = TableRow() \
        .containing(TableCell("Surname")) \
        .containing(CheckBox())

    element = S(selector).element()

    assert element

    context.found_element = element


@step(u"I search for a TableRow with a Button that has label 'edit'")
def step_impl(context):
    selector = TableRow() \
        .containing(Button('edit')) \

    element = S(selector).element()

    assert element

    context.found_element = element
