from .find_germanium_object import find_germanium_object

from .mouse_actions import _move_mouse


def drag_and_drop_g(context, from_selector, to_selector, from_point=None, to_point=None):
    germanium = find_germanium_object(context)

    action = _move_mouse(germanium, from_selector, from_point, move_mouse_over=True) \
                .click_and_hold()

    _move_mouse(germanium, to_selector, to_point, move_mouse_over=True, action=action)\
        .release()

    action.perform()
