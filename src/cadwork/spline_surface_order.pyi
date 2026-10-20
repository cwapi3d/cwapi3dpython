from enum import IntEnum, unique

@unique
class spline_surface_order(IntEnum):
    """spline surface order

    Examples:
        >>> cadwork.spline_surface_order.linear
        linear
    """

    linear = 1
    """sections follow each other along a roughly straight run, sorted by their centres of gravity"""
    circular = 2
    """sections are arranged around a common centre, sorted by angle around it"""

    def __int__(self) -> int:
        return self.value
