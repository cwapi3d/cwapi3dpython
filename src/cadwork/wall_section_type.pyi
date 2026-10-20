from enum import IntEnum, unique

@unique
class wall_section_type(IntEnum):
    """wall section type

    Examples:
        >>> cadwork.wall_section_type.horizontal
        horizontal
    """

    horizontal = 1
    """perpendicular to the element's yl axis (across its width)"""
    vertical = 2
    """perpendicular to the element's xl axis (along its length)"""

    def __int__(self) -> int:
        return self.value
