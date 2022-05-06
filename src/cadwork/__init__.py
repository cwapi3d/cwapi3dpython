
from typing import List


class layer_settings():
    def __init__(self) -> None:
        pass

class extended_settings():
    def __init__(self) -> None:
        pass
    
class output_type():
    def __init__(self) -> None:
        pass
    
class process_type():
    def __init__(self) -> None:
        pass
    def is_hip_valley(self, output_type):
        pass
    def is_jack_rafter(self, output_type):
        pass
    def is_log(self, output_type):
        pass
    def is_none(self, output_type):
        pass
    def is_panel_1(self, output_type):
        pass
    def is_panel_2(self, output_type):
        pass
    def is_panel_3(self, output_type):
        pass
    def is_panel_4(self, output_type):
        pass
    def is_panel_5(self, output_type):
        pass
    def is_purlin(self, output_type):
        pass
    def is_rafter(self, output_type):
        pass
    def is_rough_volume_framed_wall(self, output_type):
        pass
    def is_rough_volume_log_home(self, output_type):
        pass
    def is_rough_volume_solid_wood_wall(self, output_type):
        pass
    def is_stud(self, output_type):
        pass
    def is_tread(self, output_type):
        pass
    def is_truss(self, output_type):
        pass
    def is_user_1(self, output_type):
        pass
    def is_user_2(self, output_type):
        pass
    def is_user_3(self, output_type):
        pass
    def is_user_4(self, output_type):
        pass
    def is_user_5(self, output_type):
        pass
    def set_hip_valley(self, element_ids:List[int], output_type):
        pass
    def set_jack_rafter(self, element_ids:List[int], output_type):
        pass
    def set_log(self, element_ids:List[int], output_type):
        pass
    def set_none(self, element_ids:List[int], output_type):
        pass
    def set_panel_1(self, element_ids:List[int], output_type):
        pass
    def set_panel_2(self, element_ids:List[int], output_type):
        pass
    def set_panel_3(self, element_ids:List[int], output_type):
        pass
    def set_panel_4(self, element_ids:List[int], output_type):
        pass
    def set_panel_5(self, element_ids:List[int], output_type):
        pass
    def set_purlin(self, element_ids:List[int], output_type):
        pass
    def set_rafter(self, element_ids:List[int], output_type):
        pass
    def set_rough_volume_framed_wall(self, element_ids:List[int], output_type):
        pass
    def set_rough_volume_log_home(self, element_ids:List[int], output_type):
        pass
    def set_rough_volume_solid_wood_wall(self, element_ids:List[int], output_type):
        pass
    def set_stud(self, element_ids:List[int], output_type):
        pass
    def set_tread(self, element_ids:List[int], output_type):
        pass
    def set_truss(self, element_ids:List[int], output_type):
        pass
    def set_user_1(self, element_ids:List[int], output_type):
        pass
    def set_user_2(self, element_ids:List[int], output_type):
        pass
    def set_user_3(self, element_ids:List[int], output_type):
        pass
    def set_user_4(self, element_ids:List[int], output_type):
        pass
    def set_user_5(self, element_ids:List[int], output_type):
        pass

class element_type():
    def __init__(self) -> None:
        pass
    def isAdditionalElement(self, element_type):
        pass
    def isAuxiliary(self, element_type):
        pass
    def isCadwork(self, element_type):
        pass
    def isCircularAxis(self, element_type):
        pass
    def isCircularBeam(self, element_type):
        pass
    def isConnectorAxis(self, element_type):
        pass
    def isConnectorNode(self, element_type):
        pass
    def isContainer(self, element_type):
        pass
    def isDimension(self, element_type):
        pass
    def isDrillingAxis(self, element_type):
        pass
    def isEaveAxis(self, element_type):
        pass
    def isExportSolid(self, element_type):
        pass
    def isExportSolidScene(self, element_type):
        pass
    def isFloor(self, element_type):
        pass
    def isGlobalCut(self, element_type):
        pass
    def isGraphicalObject(self, element_type):
        pass
    def isLine(self, element_type):
        pass
    def isNestingParent(self, element_type):
        pass
    def isNone(self, element_type):
        pass
    def isNormalNode(self, element_type):
        pass
    def isOpening(self, element_type):
        pass
    def isPanel(self, element_type):
        pass
    def isRectangularAxis(self, element_type):
        pass
    def isRectangularBeam(self, element_type):
        pass
    def isRoof(self, element_type):
        pass
    def isRoom(self, element_type):
        pass
    def isRotationElement(self, element_type):
        pass
    def isSectionTrace(self, element_type):
        pass
    def isSteelShape(self, element_type):
        pass
    def isSurface(self, element_type):
        pass
    def isTextDocument(self, element_type):
        pass
    def isWall(self, element_type):
        pass
    def isWireAxis(self, element_type):
        pass
    def is_additional_element(self, element_type):
        pass
    def is_auxiliary(self, element_type):
        pass
    def is_cadwork(self, element_type):
        pass
    def is_circular_axis(self, element_type):
        pass
    def is_circular_beam(self, element_type):
        pass
    def is_connector_axis(self, element_type):
        pass
    def is_connector_node(self, element_type):
        pass
    def is_container(self, element_type):
        pass
    def is_dimension(self, element_type):
        pass
    def is_drilling_axis(self, element_type):
        pass
    def is_eave_axis(self, element_type):
        pass
    def is_export_solid(self, element_type):
        pass
    def is_export_solid_scene(self, element_type):
        pass
    def is_floor(self, element_type):
        pass
    def is_global_cut(self, element_type):
        pass
    def is_graphical_object(self, element_type):
        pass
    def is_line(self, element_type):
        pass
    def is_nesting_parent(self, element_type):
        pass
    def is_none(self, element_type):
        pass
    def is_normal_node(self, element_type):
        pass
    def is_opening(self, element_type):
        pass
    def is_panel(self, element_type):
        pass
    def is_rectangular_axis(self, element_type):
        pass
    def is_rectangular_beam(self, element_type):
        pass
    def is_roof(self, element_type):
        pass
    def is_room(self, element_type):
        pass
    def is_rotation_element(self, element_type):
        pass
    def is_section_trace(self, element_type):
        pass
    def is_steel_shape(self, element_type):
        pass
    def is_surface(self, element_type):
        pass
    def is_text_document(self, element_type):
        pass
    def is_wall(self, element_type):
        pass
    def is_wire_axis(self, element_type):
        pass

class rgb_color():
    def __init__(self) -> None:
        pass

class visibility_state():
    def __init__(self) -> None:
        pass
    
class activation_state():
    def __init__(self) -> None:
        pass

class point_3d():
    def __init__(self, x:float, y:float, z:float)->None:
        self.x = x
        self.y = y
        self.z = z
    def cross(self, another_point_3d):
        """cross product takes two vectors and produces a third vector that is orthogonal to both

        Args:
            point_3d (point_3d): a second vector

        Returns:
            point_3d: a third vector orthogonal to both
        """

    def distance(self, another_point_3d) -> float:
        """distance between to points

        Args:
            point_3d (point_3d): a second point

        Returns:
            float: distance
        """

    def dot(self, another_point_3d) -> float:
        """When calculating the dot product of two unit vectors, the result is always between -1 and +1.
        The scalar product of two vectors of given length is thus zero if they are perpendicular to each other, and maximum if they have the same direction.
        A negative dot product between two vectors means that the two vectors go in the opposite general direction.

        Args:
            point_3d (point_3d): a second vector

        Returns:
            float: value betweend 0.0 and 1.0
        """
        
    def magnitude(self) -> float:
        """magnitude of a vector is the length of the vector.

        Returns:
            float: vector length
        """

    def normalized(self):
        """A normalized vector is a vector with a length equal to one unit.

        Returns:
            point_3d: normalized vector
        """
    def invert(self):
        """Invert point_3d
        
        Returns:
            point_3d: inverted point_3d
        """

def get_auto_attribute_elements() -> List[int]:
    """Get ontly the elements of the selected types in the attribute manager dialog. All other elements will 
    get an empty attribute value.

    Returns:
        List[int]: element IDs
    """

def set_auto_attribute(elements: List[int], value:str) -> None:
    """Set the auto attribute to the selected element types. 

    Args:
        elements (List[int]): element IDs 
        value (str): attribute 
    """

class element_module_properties():
    def __init__(self) -> None:
        pass
    def get_cutting_element_priority(self):
        pass
    def get_distribute_in_axis_direction_distance(self):
        pass
    def get_distribute_in_axis_direction_number(self):
        pass
    def get_distribute_perpendicular_to_axis_direction_distance(self):
        pass
    def get_distribute_perpendicular_to_axis_direction_number(self):
        pass
    def get_keep_in_center_Of_layer_current_wall(self):
        pass
    def get_keep_in_center_Of_layer_neighbour_wall(self):
        pass
    def get_unique_layername(self):
        pass
    def is_auxiliary(self):
        pass
    def is_bottom_plate(self):
        pass
    def is_cutting_element(self):
        pass
    def is_distribute_in_axis_direction(self):
        pass
    def is_distribute_in_axis_direction_use_max_distance(self):
        pass
    def is_distribute_in_axis_direction_use_number(self):
        pass
    def is_distribute_perpendicular_to_axis_direction(self):
        pass
    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self):
        pass
    def is_distribute_perpendicular_to_axis_direction_use_number(self):
        pass
    def is_element_from_detail(self):
        pass
    def is_keep_in_center_Of_layer_current_wall(self):
        pass
    def is_keep_in_center_Of_layer_neighbour_wall(self):
        pass
    def is_main_element(self):
        pass
    def is_move_according_length_axis(self):
        pass
    def is_move_according_thickness_axis(self):
        pass
    def is_move_with_top_of_wall(self):
        pass
    def is_no_collision_control(self):
        pass
    def is_no_inside_cover_control(self):
        pass
    def is_not_cut_with_cutting_element(self):
        pass
    def is_not_placed_at_end_of_wall(self):
        pass
    def is_not_placed_at_start_of_wall(self):
        pass
    def is_opening_lintel(self, active:bool):
        pass
    def is_opening_sill(self, active:bool):
        pass
    def is_solder_in_axis_direction(self):
        pass
    def is_stop_in_axis_direction(self):
        pass
    def is_stop_perpendicular_to_axis_direction(self):
        pass
    def is_strecht_according_length_axis(self):
        pass
    def is_strecht_according_thickness_axis(self):
        pass
    def is_stretch_with_opening_lintel(self):
        pass
    def is_stretch_with_opening_sill(self):
        pass
    def is_stretch_with_top_of_wall(self):
        pass
    def is_top_plate(self):
        pass
    def is_unique_layername(self):
        pass
    def is_use_for_detail_coordinate_system(self):
        pass
    def set_auxiliary(self, active:bool):
        pass
    def set_bottom_plate(self, active:bool):
        pass
    def set_cutting_element(self, active:bool, priority:int):
        pass
    def set_distribute_in_axis_direction_use_max_distance(self):
        pass
    def set_distribute_in_axis_direction_use_number(self):
        pass
    def set_distribute_in_axis_direction(self, active:bool, distance:int):
        pass
    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self):
        pass
    def set_distribute_perpendicular_to_axis_direction_use_number(self):
        pass
    def set_distribute_perpendicular_to_axis_direction(self, active:bool, distance:int):
        pass
    def set_element_from_detail(self):
        pass
    def set_keep_in_center_Of_layer_current_wall(self):
        pass
    def set_keep_in_center_Of_layer_neighbour_wall(self):
        pass
    def set_keep_in_center_Of_rough_volume(self):
        pass
    def set_main_element(self):
        pass
    def set_move_according_length_axis(self):
        pass
    def set_move_according_thickness_axis(self):
        pass
    def set_move_with_top_of_wall(self, aActive:bool):
        pass
    def set_no_collision_control(self, active:bool):
        pass
    def set_no_inside_cover_control(self, active:bool):
        pass
    def set_not_cut_with_cutting_element(self, active:bool):
        pass
    def set_not_placed_at_end_of_wall(self, active:bool):
        pass
    def set_not_placed_at_start_of_wall(self, active:bool):
        pass
    def set_opening_lintel(self):
        pass
    def set_opening_sill(self):
        pass
    def set_solder_in_axis_direction(self, active:bool):
        pass
    def set_stop_in_axis_direction(self, active:bool):
        pass
    def set_stop_perpendicular_to_axis_direction(self, active:bool):
        pass
    def set_strecht_according_length_axis(self):
        pass
    def set_strecht_according_thickness_axis(self):
        pass
    def set_stretch_with_opening_lintel(self, active:bool):
        pass
    def set_stretch_with_opening_sill(self, active:bool):
        pass
    def set_stretch_with_top_of_wall(self, aActive:bool):
        pass
    def set_top_plate(self, active:bool):
        pass
    def set_unique_layername(self):
        pass
    def set_use_for_detail_coordinate_system(self, active:bool):
        pass

class ifc_2x3_element_type():
    def __init__(self) -> None:
        pass
    def is_ifc_beam(self, ifc_type):
        pass
    def is_ifc_building_element_part(self, ifc_type):
        pass
    def is_ifc_building_element_proxy(self, ifc_type):
        pass
    def is_ifc_chimney(self, ifc_type):
        pass
    def is_ifc_column(self, ifc_type):
        pass
    def is_ifc_covering(self, ifc_type):
        pass
    def is_ifc_curtain_wall(self, ifc_type):
        pass
    def is_ifc_discrete_accessory(self, ifc_type):
        pass
    def is_ifc_door(self, ifc_type):
        pass
    def is_ifc_fastener(self, ifc_type):
        pass
    def is_ifc_flow_segment(self, ifc_type):
        pass
    def is_ifc_footing(self, ifc_type):
        pass
    def is_ifc_furnishing_element(self, ifc_type):
        pass
    def is_ifc_mechanical_fastener(self, ifc_type):
        pass
    def is_ifc_member(self, ifc_type):
        pass
    def is_ifc_opening_element(self, ifc_type):
        pass
    def is_ifc_plate(self, ifc_type):
        pass
    def is_ifc_railing(self, ifc_type):
        pass
    def is_ifc_ramp(self, ifc_type):
        pass
    def is_ifc_ramp_flight(self, ifc_type):
        pass
    def is_ifc_roof(self, ifc_type):
        pass
    def is_ifc_slab(self, ifc_type):
        pass
    def is_ifc_space(self, ifc_type):
        pass
    def is_ifc_stair(self, ifc_type):
        pass
    def is_ifc_stair_flight(self, ifc_type):
        pass
    def is_ifc_wall(self, ifc_type):
        pass
    def is_ifc_wall_standard_case(self, ifc_type):
        pass
    def is_ifc_window(self, ifc_type):
        pass
    def is_none(self, ifc_type):
        pass
    def set_ifc_beam(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_building_element_part(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_building_element_proxy(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_chimney(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_column(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_covering(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_curtain_wall(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_discrete_accessory(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_door(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_fastener(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_flow_segment(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_footing(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_furnishing_element(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_mechanical_fastener(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_member(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_opening_element(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_plate(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_railing(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_ramp(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_ramp_flight(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_roof(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_slab(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_space(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_stair(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_stair_flight(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_wall(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_wall_standard_case(self, element_ids:List[int], ifc_type):
        pass
    def set_ifc_window(self, element_ids:List[int], ifc_type):
        pass
    def set_none(self, element_ids:List[int], ifc_type):
        pass