from enum import IntEnum, unique


@unique
class text_element_type(IntEnum):
    """text element type

    Examples:
        >>> cadwork.text_element_type.line
        line

    Args:
        line = 0
        surface = 1
        volume = 2

    """
    line = 0
    surface = 1
    volume = 2

    def __int__(self) -> int:
        return self.value

