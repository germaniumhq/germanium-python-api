
global_germanium = None


def get_instance():
    """
    :return: GermaniumDriver
    """
    global global_germanium

    return global_germanium


def set_instance(instance):
    global global_germanium

    global_germanium = instance
