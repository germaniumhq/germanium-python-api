from behave import *

from germanium import wait
from germanium.static import *


@step(u'waiting for success to happen should fail')
def step_impl(context):
    wait_threw_exception = True

    try:
        wait(S('div#successContent'),
             while_not=S('div#errorContent'))
        wait_threw_exception = False
    except Exception as e:
        pass

    if not S('div#errorContent'):
        assert False

    if not wait_threw_exception:
        assert False


@step(u'waiting for error to happen should pass')
def step_impl(context):
    wait(S('div#errorContent'))


@step(u'waiting for error or success to happen should pass with array callbacks')
def step_impl(context):
    wait([S('div#successContent'), S('div#errorContent')])


@step(u'waiting for error or success to happen should pass with multiarg callbacks')
def step_impl(context):
    wait(S('div#successContent'), S('div#errorContent'))


@step(u'I wait on a closure that returns a closure that returns False')
def wait_on_a_closure_that_returns_a_closure_that_returns_false(context):
    def return_false():
        return False

    def return_return_false():
        return return_false

    try:
        wait(return_return_false, timeout=0.5)
        context.wait_function_call_failed = False
    except:
        context.wait_function_call_failed = True


@step('the wait function call failed')
def wait_function_call_fails(context):
    assert context.wait_function_call_failed
