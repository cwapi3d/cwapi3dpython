from enum import IntEnum, unique


@unique
class projection_type(IntEnum):
    """projection type

    Examples:
        >>> cadwork.projection_type.Perspective
        Perspective
    """
    Perspective = 0
    """"""
    Orthographic = 1
    """"""

    def __int__(self) -> int:
        return self.value

