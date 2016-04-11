from germanium.impl._alert_exists import _alert_exists
from selenium.common.exceptions import NoAlertPresentException


class AlertLocator(object):
    """
    Create a deferred locator that can be used in matching
    elements in wait conditions.
    """
    def __init__(self, germanium=None):
        self._germanium = germanium

    def __call__(self):
        return self.exists()

    def element(self):
        """
        Returns the current alert, or None if no alert is present.
        :return:
        """
        try:
            alert = self._germanium.web_driver.switch_to.alert
            return alert
        except NoAlertPresentException:
            return None

    def element_list(self):
        """
        Returns a list with just this alert, or an empty list if no alert
        is present.
        :return:
        """
        result = self.element()

        if result:
            return [result]

        return []

    def exists(self):
        """
        Returns true if an alert is present.
        :return:
        """
        return _alert_exists(self._germanium)

    def not_exists(self):
        """
        Returns false if alert exists.
        :return:
        """
        return not self.exists()

    def text(self):
        """
        Returns the text of the current alert.
        :return:
        """
        alert = self._germanium.web_driver.switch_to.alert
        return alert.text
