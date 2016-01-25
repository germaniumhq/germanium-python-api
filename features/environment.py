from behave import *

def after_scenario(context, scenario):
    context.germanium.quit()

