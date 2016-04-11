from behave import *
from germanium.static import *

from features.steps.asserts import *

use_step_matcher("re")


@step(u'there is an alert that exists')
def step_impl(context):
    assert_true(Alert().exists())


@step(u'the text of the alert is "(.*?)"')
def step_impl(context, alert_text):
    assert_equals(alert_text, Alert().text())


@step(u'I close the alert dialog by ok')
def step_impl(context):
    Alert().accept()


@step(u'I close the alert dialog by cancel')
def step_impl(context):
    Alert().dismiss()


@step(u"I write into the alert '(.*?)'")
def step_impl(context, text):
    type_keys(text, Alert())
