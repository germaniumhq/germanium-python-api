class Alert(object):
    def __call__(self, *args, **kwargs):
        """
        Return the element list. If germanium is provided, the selector
        is evaluated using g.S(self).element_list(). If is not
        provided, this is equivalent to
        germanium.static.S(self).element_list()
        :param args:
        :param kwargs:
        :return:
        """
        return self.exists(*args, **kwargs)

    def element(self, *argv, germanium=None, **kw):
        """
        Returns the existing alert instance for the given germanium instance.
        If the alert is not present, then it will return None.
        If the germanium parameter is not set it will use instead the
        `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).element(*argv, **kw)

    def element_list(self, *argv, germanium=None, **kw):
        """
        Returns the existing alert instance as a list for the given
        germanium instance. If the alert is not present, then it will
        return None. If the germanium parameter is not set it will use
        instead the `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).element(*argv, **kw)

    def exists(self, *argv, germanium=None, **kw):
        """
        Returns true if an alert is present for the given germanium instance.
        If it is not present, then it will return false. If the germanium parameter
        is not set it will use instead the `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).exists(*argv, **kw)

    def not_exists(self, *argv, germanium=None, **kw):
        """
        Returns false if an alert is present for the given germanium instance.
        If it is not present, then it will return true. If the germanium parameter
        is not set it will use instead the `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).not_exists(*argv, **kw)

    def text(self, *argv, germanium=None, **kw):
        """
        Returns the text of the currently visible alert. If the germanium parameter
        is not set it will use instead the `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        return S(self, germanium=germanium).text(*argv, **kw)

    def accept(self, *argv, germanium=None, **kw):
        """
        Accepts the current alert from the germanium instance. If the germanium parameter
        is not set it will use instead the `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        alert = S(self, germanium=germanium).element(*argv, **kw)

        alert.accept()

    def dismiss(self, *argv, germanium=None, **kw):
        """
        Dismisses (i.e. cancels) the current alert from the germanium instance.
        If the germanium parameter is not set it will use instead the
        `germanium.static.get_germanium` instance.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        alert = S(self, germanium=germanium).element(*argv, **kw)

        alert.dismiss()

    def send_keys(self, text, *argv, germanium=None, **kw):
        """
        Types the given keys into the alert.
        If the germanium parameter is not set it will use instead the
        `germanium.static.get_germanium` instance.
        :param text: The text to type into.
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        alert = S(self, germanium=germanium).element(*argv, **kw)

        alert.send_keys(text)

    def authenticate(self, username, password, *argv, germanium=None, **kw):
        """
        Fills in the username and password into the alert.
        If the germanium parameter is not set it will use instead the
        `germanium.static.get_germanium` instance.
        :param password:
        :param username:
        :param argv:
        :param germanium:
        :param kw:
        :return:
        """
        from germanium.static import S
        alert = S(self, germanium=germanium).element(*argv, **kw)

        alert.autenticate(username, password)
