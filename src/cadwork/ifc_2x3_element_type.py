from typing import List


class ifc_2x3_element_type():
    def __init__(self) -> None:
        pass

    def is_ifc_beam(self, ifc_type) -> bool:
        """
        Examples:
            >>> import      element_controller      as ec
            >>> import      bim_controller          as bc
            >>> import      cadwork

            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> ifc_type = bc.get_ifc2x3_element_type(element)
                >>> if cadwork.ifc_2x3_element_type.is_ifc_member(ifc_type):
                    >>>   # do something
        Args:
            ifc_type (_type_): ifc element type

        Returns:
            bool: condition
        """

    def is_ifc_building_element_part(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_building_element_proxy(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_chimney(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_column(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_covering(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_curtain_wall(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_discrete_accessory(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_door(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_fastener(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_flow_segment(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_footing(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_furnishing_element(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_mechanical_fastener(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_member(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_opening_element(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_plate(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_railing(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_ramp(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_ramp_flight(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_roof(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_slab(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_space(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_stair(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_stair_flight(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_wall(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_wall_standard_case(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_window(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_none(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def set_ifc_beam(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_building_element_part(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_building_element_proxy(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_chimney(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_column(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_covering(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_curtain_wall(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_discrete_accessory(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_door(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_fastener(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_flow_segment(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_footing(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_furnishing_element(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_mechanical_fastener(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_member(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_opening_element(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_plate(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_railing(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_ramp(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_ramp_flight(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_roof(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_slab(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_space(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_stair(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_stair_flight(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_wall(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_wall_standard_case(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_window(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_none(self, element_ids: List[int], ifc_type) -> None:
        """_summary_

        Args:
            element_ids (List[int]): _description_
            ifc_type (_type_): _description_
        """
