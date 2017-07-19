from .driver import GermaniumDriver
from .iframe import iframe

from .util import get_attributes_g
from .util import click_g, right_click_g, double_click_g, hover_g
from .util import type_keys_g
from .util import wait

# patch the capabilities from FIREFOX itself.
import selenium
selenium.webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "ignore"
