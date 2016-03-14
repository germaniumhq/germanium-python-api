from behave import *

from germanium.static import *

use_step_matcher("re")


@step(u"I look for a '(.*?)' element with '(.*?)' text in it")
def step_impl(context, element_name, contained_text):
    element = S(Element(element_name, contains_text=contained_text)).element()

    context.found_element = element


@step(u"I look for a '(.*?)' element with a '(.*?)=(.*?)' attribute")
def step_impl(context, element_name, attribute_name, attribute_value):
    element = S(Element(element_name,
                        exact_attributes={attribute_name: attribute_value})).element()

    context.found_element = element


@step(u"I look for a '(.*?)' element with '(.*?)' class")
def step_impl(context, element_name, class_name):
    element = S(Element(element_name,
                        css_classes=[class_name])).element()

    context.found_element = element
