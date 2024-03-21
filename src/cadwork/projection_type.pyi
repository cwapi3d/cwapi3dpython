from enum import IntEnum, unique


@unique
class projection_type(IntEnum):
    """projection type

    Examples:
        >>> cadwork.projection_type.Perspective
        Perspective
    """
    Perspective = 1
    """"""
    Orthographic = 2
    """"""

    def __int__(self) -> int:
        return self.value

