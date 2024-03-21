from enum import IntEnum, unique


@unique
class text_element_type(IntEnum):
    """text element type

    Examples:
        >>> cadwork.text_element_type.line
        line
    """
    line = 0
    """"""
    surface = 1
    """"""
    volume = 2
    """"""
    raster = 3
    """"""

    def __int__(self) -> int:
        return self.value

