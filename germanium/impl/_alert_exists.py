from selenium.common.exceptions import NoAlertPresentException


def _alert_exists(germanium):
    try:
        alert = germanium.web_driver.switch_to.alert
        alert.text
        return alert
    except NoAlertPresentException:
        return False
