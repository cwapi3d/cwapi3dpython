from enum import IntEnum, unique


@unique
class element_grouping_type(IntEnum):
    """ Element grouping type.

    Examples:
        >>> attribute_controller.set_element_grouping_type(element_grouping_type.subgroup)
        >>> attribute_controller.get_element_grouping_type()

    Args:
        group (int): 1
        subgroup (int): 2

    """

    group = 1
    subgroup = 2
    _none = 3

    def __int__(self) -> int:
        return self.value
