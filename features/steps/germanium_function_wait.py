from behave import *
from time import sleep

from germanium import wait

@step(u'waiting for success to happen should fail')
def step_impl(context):
    S = context.germanium.S
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
    wait(context.germanium.S('div#errorContent'))

