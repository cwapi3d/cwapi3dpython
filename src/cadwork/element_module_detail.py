from enum import IntEnum, unique


@unique
class element_module_detail(IntEnum):
    """Add element situation to detail. 

    Examples:
        >>> element_controller.add_elements_to_detail(element_ids, element_module_detail.cross)

    Args:
        no_detail (int): 0
        angle_detail (int): 1
        area_detail (int): 2
        cross_detail (int): 3
        edge_detail (int): 4
        end_detail (int): 5
        line_detail (int): 6
        open_detail (int): 7
        t_detail (int): 8
        floor_area_detail (int): 9
        floor_end_detail (int): 10
        floor_line_detail (int): 11
        floor_open_detail (int): 12

    """
    no_detail = 0,
    angle_detail = 1,
    area_detail = 2,
    cross_detail = 3,
    edge_detail = 4,
    end_detail = 5,
    line_detail = 6,
    open_detail = 7,
    t_detail = 8,
    floor_area_detail = 9,
    floor_end_detail = 10,
    floor_line_detail = 11,
    floor_open_detail = 12

    def __int__(self) -> int:
        return self.value
