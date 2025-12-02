from enum import IntEnum, unique


@unique
class multi_layer_cover_type(IntEnum):
    """multi layer cover type

    Examples:
        >>> cadwork.multi_layer_cover_type.framedWall
        framedWall
    """
    framedWall = 0
    """"""
    solidWall = 1
    """"""
    logWall = 2
    """"""
    framedRoof = 3
    """"""
    solidRoof = 4
    """"""
    framedFloor = 5
    """"""
    solidFloor = 6
    """"""

    def __int__(self) -> int:
        return self.value

