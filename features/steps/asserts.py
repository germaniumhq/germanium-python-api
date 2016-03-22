
# just a bunch of assert methods to use.


class AssertionFailedException(Exception):
    """
    Just an exception that we throw when failing an assert

    """
    def __init__(self, message):
        super(AssertionFailedException, self).__init__(message)


def assert_equals(expected, actual, message = None):
    """
    Checks if the given values are equal
    :param expected:
    :param actual:
    :param message:
    """
    if expected == actual:
        return

    if message:
        raise AssertionFailedException(message)

    message = "Expected: \n%s\n, found instead: \n%s\n." % (expected, actual)

    raise AssertionFailedException(message)


def assert_true(expected, message = None):
    """
    Checks if the given value is true.
    """
    if expected:
        return

    if message:
        raise AssertionFailedException(message)

    message = "Expected value to be true. Was instead: %s" % expected

    raise AssertionFailedException(message)


def assert_false(expected, message = None):
    """
    Checks if the given value is false.
    """
    if not expected:
        return

    if message:
        raise AssertionFailedException(message)

    message = "Expected value to be false. Was instead: %s" % expected

    raise AssertionFailedException(message)
