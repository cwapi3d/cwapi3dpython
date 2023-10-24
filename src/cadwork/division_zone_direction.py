from enum import IntEnum, unique


@unique
class division_zone_direction(IntEnum):
    """ Add division zone direction.

    Examples:
        >>> point = cadwork.point_3d(0, 0, 0)
        >>> geometry_controller.create_division_zone(123456, point, division_zone_direction.positive)

    Args:
        positive (int): 1
        negative (int): -1
        none (int): 0
    """
    positive = 1
    negative = -1
    no_direction = 0

    def __int__(self) -> int:
        return self.value
