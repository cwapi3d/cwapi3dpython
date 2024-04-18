from enum import IntEnum, unique


@unique
class standard_element_type(IntEnum):
    """standard element type

    Examples:
        >>> cadwork.standard_element_type.beam
        beam
    """
    beam = 0
    """"""
    panel = 2
    """"""
    vba = 3
    """"""
    exportSolid = 4
    """"""
    container = 5
    """"""
    metal = 6
    """"""

    def __int__(self) -> int:
        return self.value

