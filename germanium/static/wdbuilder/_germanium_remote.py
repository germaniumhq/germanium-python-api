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
