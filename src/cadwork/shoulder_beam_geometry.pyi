from enum import IntEnum, unique


@unique
class shoulder_beam_geometry(IntEnum):
    """shoulder beam geometry

    Examples:
        >>> cadwork.shoulder_beam_geometry.bisector
        bisector
    """

    bisector = 0
    """Bisector
    """
    birdsmouth = 2
    """PerpBirdmouth
    """
    perpendicular_to_strut = 3
    """PerpShoulder
    """
    perpendicular_to_counter_part = 4
    """PerpChord
    """

    def __int__(self) -> int:
        return self.value

