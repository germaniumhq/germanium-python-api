from selenium import webdriver


class ActionChains(webdriver.ActionChains):
    def add_action(self, f):
        self._actions.append(f)
