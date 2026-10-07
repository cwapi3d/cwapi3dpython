from enum import IntEnum, unique


@unique
class element_segment_type(IntEnum):
    """element segment type

    Examples:
        >>> cadwork.element_segment_type.straight
        straight
    """
    straight = 1
    """straight line from the running point to mPosition"""
    arc = 2
    """circular arc from the running point through mSupportPosition to mPosition"""
    spline = 3
    """a point on a natural-cubic-spline run; consecutive Spline entries are fit through ONE curve"""

    def __int__(self) -> int:
        return self.value
