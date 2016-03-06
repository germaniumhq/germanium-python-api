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
