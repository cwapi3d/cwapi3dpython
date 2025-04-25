from enum import IntEnum, unique


@unique
class dxf_layer_format_type(IntEnum):
    """ Enumeration for DXF layer format type.

    Examples:
        >>> cadwork.dxf_layer_format_type.color

    """
    all_in_no_1 = 0
    """"""
    color = 1
    """"""
    material = 2
    """"""
    name = 3
    """"""
    group = 4
    """"""
    subgroup = 5
    """"""

    def __int__(self) -> int:
        return self.value
