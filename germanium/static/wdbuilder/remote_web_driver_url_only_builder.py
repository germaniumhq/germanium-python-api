
from selenium import webdriver


class GermaniumRemote(webdriver.Remote):
    def __init__(self, *args, **kw):
        super(GermaniumRemote, self).__init__(*args, **kw)

    def execute(self, driver_command, params=None):
        if driver_command != 'newSession':
            return super(GermaniumRemote, self).execute(driver_command, params=params)

        if params:
            params.pop('capabilities', None)

        return super(GermaniumRemote, self).execute(driver_command, params=params)


def create_url_remote_driver(remote_match):
    remote_browser = remote_match.group(1)

    if remote_browser.lower() == "firefox" or remote_browser.lower() == "ff":
        remote_capabilities = webdriver.DesiredCapabilities.FIREFOX
    elif remote_browser.lower() == "chrome":
        remote_capabilities = webdriver.DesiredCapabilities.CHROME
    elif remote_browser.lower() == "ie":
        remote_capabilities = dict(webdriver.DesiredCapabilities.INTERNETEXPLORER)
        remote_capabilities["requireWindowFocus"] = True
    elif remote_browser.lower() == "edge":
        remote_capabilities = webdriver.DesiredCapabilities.EDGE
    else:
        raise Exception("Unknown browser: %s, only firefox, "
                        "chrome and ie are supported." % remote_browser)

    return GermaniumRemote(command_executor=remote_match.group(2),
                           desired_capabilities=remote_capabilities)
