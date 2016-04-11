class Alert(object):
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
