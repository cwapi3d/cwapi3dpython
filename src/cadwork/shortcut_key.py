from enum import IntEnum, unique


@unique
class shortcut_key(IntEnum):
    """Shortcut key.

    Examples:
        >>> utility_controller.execute_shortcut(shortcut_key.F1, shortcut_key_modifier.shift)

    Args:
        F1 (int): 1
        F2 (int): 2
        F3 (int): 3
        F4 (int): 4
        F5 (int): 5
        F6 (int): 6
        F7 (int): 7
        F8 (int): 8
        F9 (int): 9
        F10 (int): 10
        F11 (int): 11
        F12 (int): 12
    """
    F1 = 1
    F2 = 2
    F3 = 3
    F4 = 4
    F5 = 5
    F6 = 6
    F7 = 7
    F8 = 8
    F9 = 9
    F10 = 10
    F11 = 11
    F12 = 12

    def __int__(self) -> int:
        return self.value


@unique
class shortcut_key_modifier(IntEnum):
    """Shortcut key.

    Examples:
        >>> utility_controller.execute_shortcut(shortcut_key.F1, shortcut_key_modifier.shift)

    Args:
        no_modifier (int): 0
        shift (int): 1
        ctrl (int): 2
        alt (int): 3
    """
    no_modifier = 0
    shift = 1
    ctrl = 2
    alt = 3

    def __int__(self) -> int:
        return self.value
