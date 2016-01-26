
from behave import *
from time import sleep

@step(u'there is no error message.')
def step_impl(context):
    assert context.germanium.S('"NO ERROR"')

