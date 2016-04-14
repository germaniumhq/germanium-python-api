from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException


def _alert_exists(germanium):
    if germanium.web_driver.name == "firefox":
        return _alert_exists_firefox(germanium)
    return _alert_exists_default(germanium)


def _alert_exists_default(germanium):
    try:
        alert = germanium.web_driver.switch_to.alert
        alert.text
        return alert
    except NoAlertPresentException:
        return False


def _alert_exists_firefox(germanium):
    try:
        germanium.web_driver.execute_script("1 == 1")
    except UnexpectedAlertPresentException as e:
        return True
