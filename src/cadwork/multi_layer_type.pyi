from enum import IntEnum, unique


@unique
class multi_layer_type(IntEnum):
    """multi layer type

    Examples:
        >>> cadwork.multi_layer_type.undefined
        undefined
    """
    undefined = 0
    """"""
    structure = 1
    """"""
    panel = 2
    """"""
    lathing = 3
    """"""
    air = 4
    """"""
    covering = 5
    """"""

    def __int__(self) -> int:
        return self.value

