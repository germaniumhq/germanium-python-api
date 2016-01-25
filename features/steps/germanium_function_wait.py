from behave import *
from time import sleep

from germanium import wait

@step(u'waiting for success to happen should fail')
def step_impl(context):
    g = context.germanium
    wait_threw_exception = True

    try:
        wait(lambda: g.find_element_by_simple('div#successContent') is not None,
            while_not=lambda: g.find_element_by_simple('div#errorContent') is not None)
        wait_threw_exception = False
    except Exception as e:
        pass

    if not wait_threw_exception:
        assert False

@step(u'waiting for error to happen should pass')
def step_impl(context):
    g = context.germanium
    wait(lambda: g.find_element_by_simple('div#errorContent') is not None)
