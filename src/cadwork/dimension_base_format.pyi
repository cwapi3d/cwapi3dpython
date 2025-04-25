from enum import IntEnum, unique


@unique
class dimension_base_format(IntEnum):
    """ Enumeration for dimension base format.

    Examples:
        >>> cadwork.dimension_base_format.sum_only

    """
    none = 0
    """"""
    distance_only = 1
    """"""
    sum_only = 2
    """"""
    distance_and_sum = 3
    """"""
    sum_moved = 4
    """"""

    def __int__(self) -> int:
        return self.value
