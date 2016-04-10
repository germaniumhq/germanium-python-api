
from time import sleep
from germanium.impl import _ensure_list


def wait(closures, *extra_closures, while_not=None, timeout=10):
    """
    Executes a function given as argument every 400 milliseconds until it returns true. If it goes more than
    the timeout seconds, then this function throws an exception. If the function throws an exception, then
    it is assumed it is false.
    :param closures:
    :param while_not:
    :param timeout:
    :param extra_closures:
    """
    while_not = _ensure_list(while_not)
    closures = list(_ensure_list(closures))
    closures.extend(extra_closures)

    def closure_try_catch():
        for closure in closures:
            try:
                result = closure()
                if result:
                    return result
            except Exception as e:
                print("WARNING: waiting as false since: %s" % e)

    passed_timeout = 0
    closure_result = False

    while passed_timeout < timeout:
        for while_not_closure in while_not:
            try:
                if while_not_closure():
                    raise Exception("Waiting failed, since while_not condition matched")
            except Exception as e:
                raise Exception("Waiting failed, since while_not condition raised exception", e)

        closure_result = closure_try_catch()

        if closure_result:
            break

        passed_timeout += 0.4

        if passed_timeout >= 2:
            print("Running takes more than 2 seconds.")

        sleep(0.4)

    if not closure_result:
        raise Exception("Waiting has failed")
