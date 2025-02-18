from enum import IntEnum, unique


@unique
class heel_shoulder_beam_geometry(IntEnum):
    """heel shoulder beam geometry

    Examples:
        >>> cadwork.heel_shoulder_beam_geometry.normal
        normal
    """
    normal = 0
    """"""
    straight = 1
    """"""

    def __int__(self) -> int:
        return self.value

