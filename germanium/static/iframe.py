from .global_germanium_instance import get_instance


def iframe(target, keep_new_context = False):
    """
    Switch the iframe in static contexts.
    """
    def wrapper(original):
        def original_aspect(*args, **kwargs):
            germanium = get_instance()
            original_iframe = germanium.current_iframe

            germanium.select_iframe(target)

            try:
                return original(*args, **kwargs)
            finally:
                if not keep_new_context:
                    germanium.select_iframe(original_iframe)

        return original_aspect

    return wrapper
