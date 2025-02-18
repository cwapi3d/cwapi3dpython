from enum import IntEnum, unique


@unique
class shoulder_beam_geometry(IntEnum):
    """shoulder beam geometry

    Examples:
        >>> cadwork.shoulder_beam_geometry.bisector
        bisector
    """
    bisector = 0
    """"""
    perpendicular_to_strut = 1
    """"""
    perpendicular_to_counter_part = 2
    """"""
    birdsmouth = 3
    """"""

    def __int__(self) -> int:
        return self.value

