from enum import IntEnum, unique


@unique
class shortcut_key_modifier(IntEnum):
    """shortcut key modifier

    Examples:
        >>> cadwork.shortcut_key_modifier.shift
        shift
    """
    shift = 1
    """"""
    ctrl = 2
    """"""
    alt = 3
    """"""

    def __int__(self) -> int:
        return self.value

