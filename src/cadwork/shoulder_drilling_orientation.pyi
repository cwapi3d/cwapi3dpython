from enum import IntEnum, unique


@unique
class shoulder_drilling_orientation(IntEnum):
    """shoulder drilling orientation

    Examples:
        >>> cadwork.shoulder_drilling_orientation.perpendicular_to_bisector
        perpendicular_to_bisector
    """
    perpendicular_to_bisector = 1
    """"""
    perpendicular_to_counter_part = 2
    """"""
    perpendicular_to_strut = 3
    """"""
    perpendicular_to_contact_surface = 4
    """"""

    def __int__(self) -> int:
        return self.value

