from enum import IntEnum, unique


@unique
class division_zone_direction(IntEnum):
    """division zone direction

    Examples:
        >>> cadwork.division_zone_direction.positive
        positive
    """
    positive = 1
    """"""
    negative = 2
    """"""
    no_direction = 3
    """"""

    def __int__(self) -> int:
        return self.value

