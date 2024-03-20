class element_module_properties:
    
    def is_stretch_with_top_of_wall(self) -> bool:
        """is stretch with top of wall

        Returns:
            bool
        """

    def is_move_with_top_of_wall(self) -> bool:
        """is move with top of wall

        Returns:
            bool
        """

    def is_distribute_in_axis_direction(self) -> bool:
        """is distribute in axis direction

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction(self) -> bool:
        """is distribute perpendicular to axis direction

        Returns:
            bool
        """

    def is_stop_in_axis_direction(self) -> bool:
        """is stop in axis direction

        Returns:
            bool
        """

    def is_stop_perpendicular_to_axis_direction(self) -> bool:
        """is stop perpendicular to axis direction

        Returns:
            bool
        """

    def is_bottom_plate(self) -> bool:
        """is bottom plate

        Returns:
            bool
        """

    def is_top_plate(self) -> bool:
        """is top plate

        Returns:
            bool
        """

    def is_opening_sill(self) -> bool:
        """is opening sill

        Returns:
            bool
        """

    def is_opening_lintel(self) -> bool:
        """is opening lintel

        Returns:
            bool
        """

    def is_cutting_element(self) -> bool:
        """is cutting element

        Returns:
            bool
        """

    def is_not_cut_with_cutting_element(self) -> bool:
        """is not cut with cutting element

        Returns:
            bool
        """

    def is_auxiliary(self) -> bool:
        """is auxiliary

        Returns:
            bool
        """

    def is_not_placed_at_end_of_wall(self) -> bool:
        """is not placed at end of wall

        Returns:
            bool
        """

    def is_not_placed_at_start_of_wall(self) -> bool:
        """is not placed at start of wall

        Returns:
            bool
        """

    def is_stretch_with_opening_lintel(self) -> bool:
        """is stretch with opening lintel

        Returns:
            bool
        """

    def is_stretch_with_opening_sill(self) -> bool:
        """is stretch with opening sill

        Returns:
            bool
        """

    def is_solder_in_axis_direction(self) -> bool:
        """is solder in axis direction

        Returns:
            bool
        """

    def is_no_collision_control(self) -> bool:
        """is no collision control

        Returns:
            bool
        """

    def is_no_inside_cover_control(self) -> bool:
        """is no inside cover control

        Returns:
            bool
        """

    def is_use_for_detail_coordinate_system(self) -> bool:
        """is use for detail coordinate system

        Returns:
            bool
        """

    def set_stretch_with_top_of_wall(self, active: bool) -> None:
        """set stretch with top of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_with_top_of_wall(self, active: bool) -> None:
        """set move with top of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_in_axis_direction(self, active: bool, distance: float) -> None:
        """set distribute in axis direction

        Parameters:
            active: active
            distance: distance

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction(self, active: bool, distance: float) -> None:
        """set distribute perpendicular to axis direction

        Parameters:
            active: active
            distance: distance

        Returns:
            None
        """

    def set_stop_in_axis_direction(self, active: bool) -> None:
        """set stop in axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stop_perpendicular_to_axis_direction(self, active: bool) -> None:
        """set stop perpendicular to axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_bottom_plate(self, active: bool) -> None:
        """set bottom plate

        Parameters:
            active: active

        Returns:
            None
        """

    def set_top_plate(self, active: bool) -> None:
        """set top plate

        Parameters:
            active: active

        Returns:
            None
        """

    def set_opening_sill(self, active: bool) -> None:
        """set opening sill

        Parameters:
            active: active

        Returns:
            None
        """

    def set_opening_lintel(self, active: bool) -> None:
        """set opening lintel

        Parameters:
            active: active

        Returns:
            None
        """

    def set_cutting_element(self, active: bool, priority: int) -> None:
        """set cutting element

        Parameters:
            active: active
            priority: priority

        Returns:
            None
        """

    def set_not_cut_with_cutting_element(self, active: bool) -> None:
        """set not cut with cutting element

        Parameters:
            active: active

        Returns:
            None
        """

    def set_auxiliary(self) -> None:
        """set auxiliary

        Returns:
            None
        """

    def set_not_placed_at_end_of_wall(self, active: bool) -> None:
        """set not placed at end of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_not_placed_at_start_of_wall(self, active: bool) -> None:
        """set not placed at start of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stretch_with_opening_lintel(self, active: bool) -> None:
        """set stretch with opening lintel

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stretch_with_opening_sill(self, active: bool) -> None:
        """set stretch with opening sill

        Parameters:
            active: active

        Returns:
            None
        """

    def set_solder_in_axis_direction(self, active: bool) -> None:
        """set solder in axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_no_collision_control(self, active: bool) -> None:
        """set no collision control

        Parameters:
            active: active

        Returns:
            None
        """

    def set_no_inside_cover_control(self, active: bool) -> None:
        """set no inside cover control

        Parameters:
            active: active

        Returns:
            None
        """

    def set_use_for_detail_coordinate_system(self, active: bool) -> None:
        """set use for detail coordinate system

        Parameters:
            active: active

        Returns:
            None
        """

    def get_distribute_in_axis_direction_distance(self) -> float:
        """get distribute in axis direction distance

        Returns:
            float
        """

    def get_distribute_perpendicular_to_axis_direction_distance(self) -> float:
        """get distribute perpendicular to axis direction distance

        Returns:
            float
        """

    def get_cutting_element_priority(self) -> int:
        """get cutting element priority

        Returns:
            int
        """

    def is_distribute_in_axis_direction_use_max_distance(self) -> bool:
        """is distribute in axis direction use max distance

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self) -> bool:
        """is distribute perpendicular to axis direction use max distance

        Returns:
            bool
        """

    def is_distribute_in_axis_direction_use_number(self) -> bool:
        """is distribute in axis direction use number

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction_use_number(self) -> bool:
        """is distribute perpendicular to axis direction use number

        Returns:
            bool
        """

    def set_distribute_in_axis_direction_use_max_distance(self, active: bool) -> None:
        """set distribute in axis direction use max distance

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self, active: bool) -> None:
        """set distribute perpendicular to axis direction use max distance

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_in_axis_direction_use_number(self, active: bool, number: int) -> None:
        """set distribute in axis direction use number

        Parameters:
            active: active
            number: number

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction_use_number(self, active: bool, number: int) -> None:
        """set distribute perpendicular to axis direction use number

        Parameters:
            active: active
            number: number

        Returns:
            None
        """

    def get_distribute_in_axis_direction_number(self) -> int:
        """get distribute in axis direction number

        Returns:
            int
        """

    def get_distribute_perpendicular_to_axis_direction_number(self) -> int:
        """get distribute perpendicular to axis direction number

        Returns:
            int
        """

    def is_main_element(self) -> bool:
        """is main element

        Returns:
            bool
        """

    def is_strecht_according_thickness_axis(self) -> bool:
        """is strecht according thickness axis

        Returns:
            bool
        """

    def is_strecht_according_length_axis(self) -> bool:
        """is strecht according length axis

        Returns:
            bool
        """

    def is_move_according_thickness_axis(self) -> bool:
        """is move according thickness axis

        Returns:
            bool
        """

    def is_move_according_length_axis(self) -> bool:
        """is move according length axis

        Returns:
            bool
        """

    def is_unique_layername(self) -> bool:
        """is unique layername

        Returns:
            bool
        """

    def is_keep_in_center_of_layer_current_wall(self) -> bool:
        """is keep in center of layer current wall

        Returns:
            bool
        """

    def is_keep_in_center_of_layer_neighbour_wall(self) -> bool:
        """is keep in center of layer neighbour wall

        Returns:
            bool
        """

    def is_keep_in_center_of_rough_volume(self) -> bool:
        """is keep in center of rough volume

        Returns:
            bool
        """

    def is_element_from_detail(self) -> bool:
        """is element from detail

        Returns:
            bool
        """

    def set_main_element(self, active: bool) -> None:
        """set main element

        Parameters:
            active: active

        Returns:
            None
        """

    def set_strecht_according_thickness_axis(self, active: bool) -> None:
        """set strecht according thickness axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_strecht_according_length_axis(self, active: bool) -> None:
        """set strecht according length axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_according_thickness_axis(self, active: bool) -> None:
        """set move according thickness axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_according_length_axis(self, active: bool) -> None:
        """set move according length axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_unique_layername(self, active: bool, layername: str) -> None:
        """set unique layername

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_layer_current_wall(self, active: bool, layername: str) -> None:
        """set keep in center of layer current wall

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_layer_neighbour_wall(self, active: bool, layername: str) -> None:
        """set keep in center of layer neighbour wall

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_rough_volume(self, active: bool) -> None:
        """set keep in center of rough volume

        Parameters:
            active: active

        Returns:
            None
        """

    def set_element_from_detail(self, active: bool) -> None:
        """set element from detail

        Parameters:
            active: active

        Returns:
            None
        """

    def get_unique_layername(self) -> str:
        """get unique layername

        Returns:
            str
        """

    def get_keep_in_center_of_layer_current_wall(self) -> str:
        """get keep in center of layer current wall

        Returns:
            str
        """

    def get_keep_in_center_of_layer_neighbour_wall(self) -> str:
        """get keep in center of layer neighbour wall

        Returns:
            str
        """

    def is_stretch_in_opening_width(self) -> bool:
        """is stretch in opening width

        Returns:
            bool
        """

    def set_stretch_in_opening_width(self, active: bool) -> None:
        """set stretch in opening width

        Parameters:
            active: active

        Returns:
            None
        """

