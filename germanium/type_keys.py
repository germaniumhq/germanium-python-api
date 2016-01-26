
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from .arguments_processor import find_germanium_object

class BasicKeysAction(object):
    """
    A class that just denotes basic keys to be sent to the WebDriver.
    basic keys can also be made of keys such as ENTER, UP, etc.
    """
    def __init__(self, keys):
        self.keys = []
        for i in range(len(keys)):
            self.keys.append(keys[i])

class ComboKeyDown(object):
    """
    An action that marks a single combo key that should be pressed
    !shift, !control, !ctrl, !alt
    """
    def __init__(self, key):
        self.key = key

class ComboKeyUp(object):
    """
    An action that marks a single combo key that should be released
    ^shift, ^control, ^ctrl, ^alt
    """
    def __init__(self, key):
        self.key = key


def type_keys(context, keys_typed, element=None, *args):
    """
    :type germanium.GermaniumDriver
    """
    germanium = find_germanium_object([context])
    keys_array = transform_to_keys(keys_typed)

    action_chain = ActionChains(germanium.web_driver)

    for key_action in keys_array:
        if isinstance(key_action, BasicKeysAction):
            if element:
                action_chain.send_keys_to_element(element, key_action.keys)
            else:
                print(key_action.keys)
                action_chain.send_keys(key_action.keys)
        elif isinstance(key_action, ComboKeyDown):
            action_chain.key_down(key_action.key, element)
        elif isinstance(key_action, ComboKeyUp):
            action_chain.key_up(key_action.key, element)

    action_chain.perform()


def transform_to_keys(keys):
    """
    Transforms the given keys string into an array of keys action
    that can be fed into an ActionChain
    """
    combo_re = re.compile('<(.*?)>')
    combo_key_scanner = combo_re.scanner(keys)

    initial_key_index = 0
    transformed_keys = []
    last_action = None

    while True:
        m = combo_key_scanner.search()
        if not m:
            break

        if m.start() - initial_key_index > 0:
            if isinstance(last_action, BasicKeysAction):
                for key in keys[initial_key_index: m.start()]:
                    last_action.keys.append(key)
            else:
                action = BasicKeysAction(keys[initial_key_index: m.start()])
                last_action = action
                transformed_keys.append(action)

        pressed_keys = m.group(1)

        if is_up_down_toggle(pressed_keys):
            action = create_up_down_toggle(pressed_keys)
            transformed_keys.append(action)
            last_action = action
        elif is_multikey_combo(pressed_keys):
            multi_combo_actions = create_multicombo(pressed_keys)
            for multi_combo_action in multi_combo_actions:
                transformed_keys.append(multi_combo_action)
                last_action = multi_combo_action
        else:
            if isinstance(last_action, BasicKeysAction):
                key = create_custom_key(pressed_keys)
                last_action.keys.append(key)
            else:
                key = create_custom_key(pressed_keys)
                action = BasicKeysAction([key])
                transformed_keys.append(action)

        initial_key_index = m.end()

    if len(keys) - initial_key_index > 0:
        action = BasicKeysAction(keys[initial_key_index:])
        transformed_keys.append(action)

    return transformed_keys


def is_multikey_combo(pressed_keys):
    return "-" in pressed_keys


def is_up_down_toggle(pressed_keys):
    return pressed_keys.find('^') == 0 or \
           pressed_keys.find('!') == 0


def create_up_down_toggle(pressed_keys):
    """
    Create a toggling of a button down.
    :param pressed_keys:
    :return:
    """
    if pressed_keys.find('^') == 0:  # release key
        key = create_custom_key(pressed_keys[1:])
        return ComboKeyUp(key)
    elif pressed_keys.find('!') == 0:  # pressed key
        key = create_custom_key(pressed_keys[1:])
        return ComboKeyDown(key)
    else:
        raise Exception("Unable to create key toggle for: '%s'" % pressed_keys)


def create_multicombo(pressed_keys):
    """
    Create a combo made of multiple keys (e.g. ctrl-shift-s)
    :param pressed_keys:
    :return:
    """
    keys_pressed = []
    keys_released = []
    result = []
    combo_key=None

    tokens = pressed_keys.split("-")

    for i in reversed(range(len(tokens))):
        if i < len(tokens) - 1:
            custom_key = create_custom_key(tokens[i])
            combo_key = custom_key + combo_key + custom_key
        else:
            combo_key = create_key(tokens[i])

    result.append(BasicKeysAction(combo_key))

    return result

def create_custom_key(combo_string):
    """
    Create a single key for webdriver that represents a custom
    key (<CR>, <SHIFT>, <UP> etc)
    """
    key_string = combo_string.upper()

    key = create_abbreviated_key(key_string)
    if key:
        return key

    if key_string == "C":
        return Keys.CONTROL
    elif key_string == "S":
        return Keys.SHIFT
    elif key_string == "M":
        return Keys.META

    return getattr(Keys, key_string)

def create_key(combo_string):
    """
    Create a single key for webdriver that represents a regular
    or a custom key, that is the last part of the macro.
    """
    # if it's a single character return it
    if len(combo_string) <= 1:
        return combo_string

    key_string = combo_string.upper()
    key = create_abbreviated_key(key_string)

    if key:
        return key

    return getattr(Keys, key_string)

def create_abbreviated_key(key_string):
    if key_string == "CR":
        return Keys.ENTER
    elif key_string == "CTRL" or \
         key_string == "CTL":
        return Keys.CONTROL
    elif key_string == "DEL":
        return Keys.DELETE
    elif key_string == "CMD":
        return Keys.COMMAND
    elif key_string == "BS":
        return Keys.BACKSPACE
    elif key_string == "INS":
        return Keys.INSERT
    elif key_string == "PGUP":
        return Keys.PAGE_UP
    elif key_string == "PGDN":
        return Keys.PAGE_DOWN

    return None
