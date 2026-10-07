from enum import IntEnum, unique

@unique
class navigation_widget_subwindow_position(IntEnum):
    """navigation widget subwindow position

    Examples:
        >>> cadwork.navigation_widget_subwindow_position.none
        none
    """

    none = 0
    """"""
    top_right = 1
    """"""
    top_left = 2
    """"""
    bottom_left = 3
    """"""
    bottom_right = 4
    """"""

    def __int__(self) -> int:
        return self.value
