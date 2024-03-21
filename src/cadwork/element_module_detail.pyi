from enum import IntEnum, unique


@unique
class element_module_detail(IntEnum):
    """element module detail

    Examples:
        >>> cadwork.element_module_detail.no_detail
        no_detail
    """
    no_detail = 1
    """"""
    angle_detail = 2
    """"""
    area_detail = 3
    """"""
    cross_detail = 4
    """"""
    edge_detail = 5
    """"""
    end_detail = 6
    """"""
    line_detail = 7
    """"""
    open_detail = 8
    """"""
    t_detail = 9
    """"""
    floor_area_detail = 10
    """"""
    floor_end_detail = 11
    """"""
    floor_line_detail = 12
    """"""
    floor_open_detail = 13
    """"""

    def __int__(self) -> int:
        return self.value

