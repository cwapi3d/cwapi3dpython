from enum import IntEnum, unique


@unique
class shortcut_key(IntEnum):
    """shortcut key

    Examples:
        >>> cadwork.shortcut_key.F1
        F1
    """
    F1 = 1
    """"""
    F2 = 2
    """"""
    F3 = 3
    """"""
    F4 = 4
    """"""
    F5 = 5
    """"""
    F6 = 6
    """"""
    F7 = 7
    """"""
    F8 = 8
    """"""
    F9 = 9
    """"""
    F10 = 10
    """"""
    F11 = 11
    """"""
    F12 = 12
    """"""

    def __int__(self) -> int:
        return self.value

