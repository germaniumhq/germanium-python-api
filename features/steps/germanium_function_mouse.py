
from behave import *
from germanium import right_click, hover, double_click

use_step_matcher("re")

@step(u'I right click on (.*?)')
def step_impl(context, selector):
    right_click(context.germanium, selector)

@step(u'I doubleclick on (.*?)')
def step_impl(context, selector):
    double_click(context.germanium, selector)

@step(u'I mouse over on (.*?)')
def step_impl(context, selector):
    hover(context.germanium, selector)
