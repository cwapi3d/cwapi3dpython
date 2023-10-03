class element_module_properties():
    def __init__(self) -> None:
        pass

    def get_cutting_element_priority(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cutting_priority = cw.element_module_properties.get_cutting_element_priority(element_module_properties)

        Args:
            element_module_properties (_type_): element module properties

        Returns:
            int: cutting_element_priority
        """

    def get_distribute_in_axis_direction_distance(self, element_module_properties) -> float:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_in_axis_direction_distance = cw.element_module_properties.get_distribute_in_axis_direction_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            float: distribute_in_axis_direction_distance
        """

    def get_distribute_in_axis_direction_number(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_in_axis_direction_number = cw.element_module_properties.get_distribute_in_axis_direction_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            int: distribute_in_axis_direction_number
        """

    def get_distribute_perpendicular_to_axis_direction_distance(self, element_module_properties) -> float:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_perpendicular_to_axis_direction_distance = cw.element_module_properties.get_distribute_perpendicular_to_axis_direction_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            float: distribute_perpendicular_to_axis_direction_distance
        """

    def get_distribute_perpendicular_to_axis_direction_number(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_perpendicular_to_axis_direction_number = cw.element_module_properties.get_distribute_perpendicular_to_axis_direction_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            int: distribute_perpendicular_to_axis_direction_number
        """

    def get_keep_in_center_of_layer_current_wall(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_keep_in_center_of_layer_current_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def get_keep_in_center_of_layer_neighbour_wall(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_keep_in_center_of_layer_neighbour_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def get_unique_layername(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_unique_layername(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def is_auxiliary(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_auxiliary = cw.element_module_properties.is_auxiliary(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_bottom_plate(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_bottom_plate = cw.element_module_properties.is_bottom_plate(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_cutting_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_cutting_element = cw.element_module_properties.is_cutting_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction = cw.element_module_properties.is_distribute_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction_use_max_distance(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction_use_max_distance = cw.element_module_properties.is_distribute_in_axis_direction_use_max_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction_use_number(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction_use_number = cw.element_module_properties.is_distribute_in_axis_direction_use_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction_use_max_distance = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction_use_number(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction_use_number = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction_use_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_element_from_detail(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_element_from_detail = cw.element_module_properties.is_element_from_detail(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_keep_in_center_of_layer_current_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_keep_in_center_of_layer_current_wall = cw.element_module_properties.is_keep_in_center_of_layer_current_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_keep_in_center_of_layer_neighbour_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_keep_in_center_of_layer_neighbour_wall = cw.element_module_properties.is_keep_in_center_of_layer_neighbour_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_main_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_main_element = cw.element_module_properties.is_main_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_according_length_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_according_length_axis = cw.element_module_properties.is_move_according_length_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_according_thickness_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_according_thickness_axis = cw.element_module_properties.is_move_according_thickness_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_with_top_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_with_top_of_wall = cw.element_module_properties.is_move_with_top_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_no_collision_control(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_no_collision_control = cw.element_module_properties.is_no_collision_control(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_no_inside_cover_control(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_no_inside_cover_control = cw.element_module_properties.is_no_inside_cover_control(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_cut_with_cutting_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_cut_with_cutting_element = cw.element_module_properties.is_not_cut_with_cutting_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_placed_at_end_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_placed_at_end_of_wall = cw.element_module_properties.is_not_placed_at_end_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_placed_at_start_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_placed_at_start_of_wall = cw.element_module_properties.is_not_placed_at_start_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_opening_lintel(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_opening_lintel = cw.element_module_properties.is_opening_lintel(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_opening_sill(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_opening_sill = cw.element_module_properties.is_opening_sill(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_solder_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_solder_in_axis_direction = cw.element_module_properties.is_solder_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stop_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stop_in_axis_direction = cw.element_module_properties.is_stop_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stop_perpendicular_to_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stop_perpendicular_to_axis_direction = cw.element_module_properties.is_stop_perpendicular_to_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_strecht_according_length_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_strecht_according_length_axis = cw.element_module_properties.is_strecht_according_length_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_strecht_according_thickness_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_strecht_according_thickness_axis = cw.element_module_properties.is_strecht_according_thickness_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_opening_lintel(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_opening_lintel = cw.element_module_properties.is_stretch_with_opening_lintel(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_opening_sill(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_opening_sill = cw.element_module_properties.is_stretch_with_opening_sill(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_in_opening_width(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_in_opening_width = cw.element_module_properties.is_stretch_in_opening_width(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_top_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_top_of_wall = cw.element_module_properties.is_stretch_with_top_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_top_plate(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_top_plate = cw.element_module_properties.is_top_plate(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
        Returns:
            bool: condition
        """

    def is_unique_layername(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_unique_layername = cw.element_module_properties.is_unique_layername(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_use_for_detail_coordinate_system(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_use_for_detail_coordinate_system = cw.element_module_properties.is_use_for_detail_coordinate_system(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def set_auxiliary(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_auxiliary(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_bottom_plate(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_bottom_plate(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_cutting_element(self, element_module_properties, active: bool, priority: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_cutting_element(element_module_properties, True, 3)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            priority (int): _description_
        """

    def set_distribute_in_axis_direction_use_max_distance(self, element_module_properties, acitve: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_max_distance(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            priority (int): _description_
        """

    def set_distribute_in_axis_direction_use_number(self, element_module_properties, active: bool, number: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_number(element_module_properties, True, 11)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            number (int): _description_
        """

    def set_distribute_in_axis_direction(self, element_module_properties, active: bool, distance: float) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_max_distance(element_module_properties, False)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            distance (float): _description_
        """

    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_distribute_perpendicular_to_axis_direction_use_number(self, element_module_properties, active: bool, number: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_number(element_module_properties, True, 15)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            number (int): _description_
        """

    def set_distribute_perpendicular_to_axis_direction(self, element_module_properties, active: bool, distance: float) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties, False)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            distance (float): _description_
        """

    def set_element_from_detail(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_element_from_detail(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_keep_in_center_of_layer_current_wall(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_layer_current_wall(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_keep_in_center_of_layer_neighbour_wall(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_layer_neighbour_wall(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_keep_in_center_of_rough_volume(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_rough_volume(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_main_element(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_rough_volume(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_according_length_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_according_length_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_according_thickness_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_according_thickness_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_with_top_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_with_top_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_no_collision_control(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_no_collision_control(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_no_inside_cover_control(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_no_inside_cover_control(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_cut_with_cutting_element(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_cut_with_cutting_element(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_placed_at_end_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_placed_at_end_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_placed_at_start_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_placed_at_start_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_opening_lintel(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_opening_lintel(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_opening_sill(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_opening_sill(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_solder_in_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_solder_in_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stop_in_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stop_in_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stop_perpendicular_to_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stop_perpendicular_to_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_according_length_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_strecht_according_length_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_according_thickness_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_strecht_according_thickness_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_opening_lintel(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_opening_lintel(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_opening_sill(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_opening_sill(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_top_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_top_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_in_opening_width(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_in_opening_width(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_top_plate(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_top_plate(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_unique_layername(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_unique_layername(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_use_for_detail_coordinate_system(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_use_for_detail_coordinate_system(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """
