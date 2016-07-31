from behave import *

from germanium import wait
from germanium.static import *

use_step_matcher("re")


@step("I select the window with the title '(.*?)'")
def i_select_the_window_named(context, window_title):
    use_window(window_title)


@step("I select the default window")
def i_select_the_default_window(context):
    use_window(index=0)
