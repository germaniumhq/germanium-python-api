from behave import *
from germanium.static import *

from features.steps.asserts import *

use_step_matcher("re")


@step(u'there is an alert that exists')
def step_impl(context):
    assert_true(Alert().exists())


@step(u'the text of the alert is "alert is present"')
def step_impl(context):
    assert_equals("alert is present", Alert().text())


@step(u'I close the alert dialog by ok')
def step_impl(context):
    Alert().accept()
