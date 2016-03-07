
from time import sleep

def wait(closure, while_not=None, timeout = 10):
    """
    Executes a function given as argument every 400 milliseconds until it returns true. If it goes more than
    the timeout seconds, then this function throws an exception. If the function throws an exception, then
    it is assumed it is false.
    """
    def closure_try_catch():
        try:
            return closure()
        except Exception as e:
            print("WARNING: waiting as false since: %s" % e)
            return False

    # compute the while_not_closures that need evaluation.
    while_not_closures = None

    if not while_not:
        while_not_closures = []
    elif hasattr(while_not, '__call__'):
        while_not_closures = [while_not]
    else:
        while_not_closures = while_not

    passed_timeout = 0
    closure_result = False

    while passed_timeout < timeout:
        for while_not_closure in while_not_closures:
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

