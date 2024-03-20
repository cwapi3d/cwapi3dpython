from enum import IntEnum, unique


@unique
class element_grouping_type(IntEnum):
    """element grouping type

    Examples:
        >>> cadwork.element_grouping_type.group
        group
    """
    group = 1
    """"""
    subgroup = 2
    """"""
    _none = 3
    """"""

    def __int__(self) -> int:
        return self.value

