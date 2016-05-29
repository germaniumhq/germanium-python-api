from selenium.common.exceptions import WebDriverException
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


def allow_alert(germanium):
    """
    Marks a section of code as runnable even if there is an alert
    displayed. The section will return a reference to the alert
    itself if raised, from the given germanium instance.

    :param germanium:
    :return:
    """
    def decorator(code):
        def wrapper():
            try:
                return code()
            except UnexpectedAlertPresentException:
                pass
            except WebDriverException as e:
                if 'unexpected alert open' not in e.msg:
                    raise e
                print("An unexpected alert exception was caught by Germanium "
                      "while loading the page: %s" % e)

            return germanium.web_driver.switch_to.alert

        return wrapper

    return decorator