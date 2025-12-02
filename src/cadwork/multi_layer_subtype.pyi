from enum import IntEnum, unique


@unique
class multi_layer_subtype(IntEnum):
    """multi layer subtype

    Examples:
        >>> cadwork.multi_layer_subtype.undefined
        undefined
    """    
    undefined = 0
    """"""
    loadBearingFrameStructure = 1
    """"""
    solidStructure = 2
    """"""
    straightEdge = 3
    """"""
    biasEdge = 4
    """"""
    vertical = 5
    """"""
    horizontal = 6
    """"""
    air = 7
    """"""
    nonLoadBearingFrameStructure = 8
    """"""

    def __int__(self) -> int:
        return self.value

