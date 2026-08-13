from enum import IntEnum, unique


@unique
class panel_prefab_element_type(IntEnum):
    """panel prefab element type

    Exclusive machine panel prefabrication element type of an element.

    Examples:
        >>> cadwork.panel_prefab_element_type.batten
        batten
    """
    none = 0
    """"""
    frame = 1
    """"""
    panel = 2
    """"""
    batten = 3
    """"""
    cladding = 4
    """"""
    insulation = 5
    """"""
    built_in_part = 6
    """"""

    def __int__(self) -> int:
        return self.value
