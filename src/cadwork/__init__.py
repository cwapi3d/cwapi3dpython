
from platform import node
from typing import List
from enum import Enum, unique


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
    def is_hip_valley(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_jack_rafter(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_log(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_none(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_panel_1(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_panel_2(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_panel_3(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_panel_4(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_panel_5(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_purlin(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_rafter(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_rough_volume_framed_wall(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_rough_volume_log_home(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_rough_volume_solid_wood_wall(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_stud(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_tread(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_truss(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_user_1(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_user_2(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_user_3(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_user_4(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def is_user_5(self, output_type:output_type)->bool:
        """

        Args:
            output_type (output_type): output type

        Returns:
            bool: condition
        """
    def set_hip_valley(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_jack_rafter(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_log(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_none(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_panel_1(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_panel_2(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_panel_3(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_panel_4(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_panel_5(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_purlin(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_rafter(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_rough_volume_framed_wall(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_rough_volume_log_home(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_rough_volume_solid_wood_wall(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_stud(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_tread(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_truss(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_user_1(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_user_2(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_user_3(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_user_4(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """
    def set_user_5(self)->None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """


class element_type():
    def __init__(self) -> None:
        pass
    def isAdditionalElement(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isAuxiliary(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isCadwork(self, element_type)->bool:
        """
        
        !!! Warning
            Function deprecated.
            
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isCircularAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isCircularBeam(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isConnectorAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isConnectorNode(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isContainer(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isDimension(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isDrillingAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isEaveAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isExportSolid(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isExportSolidScene(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isFloor(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isGlobalCut(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isGraphicalObject(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isLine(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isNestingParent(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isNone(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isNormalNode(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isOpening(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isPanel(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isRectangularAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isRectangularBeam(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isRoof(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isRoom(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isRotationElement(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isSectionTrace(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isSteelShape(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isSurface(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isTextDocument(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isWall(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def isWireAxis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_additional_element(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_auxiliary(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_cadwork(self, element_type)->bool:
        """
        !!! Warning
            Function deprecated.
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_circular_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_circular_beam(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_connector_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_connector_node(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_container(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_dimension(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_drilling_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_eave_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_export_solid(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_export_solid_scene(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_floor(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_global_cut(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_graphical_object(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_line(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_nesting_parent(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_none(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_normal_node(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_opening(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_panel(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_rectangular_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_rectangular_beam(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_roof(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_room(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_rotation_element(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_section_trace(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_steel_shape(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_surface(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_text_document(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_wall(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """
    def is_wire_axis(self, element_type)->bool:
        """
        Args:
            element_type (element type): element type 

        Returns:
            bool: condition
        """

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
    def get_cutting_element_priority(self)->int:
        """ToDo Documentation
        """
    def get_distribute_in_axis_direction_distance(self)->int:
        """ToDo Documentation
        """
    def get_distribute_in_axis_direction_number(self)->int:
        """ToDo Documentation
        """
    def get_distribute_perpendicular_to_axis_direction_distance(self)->int:
        """ToDo Documentation
        """
    def get_distribute_perpendicular_to_axis_direction_number(self)->int:
        """ToDo Documentation
        """
    def get_keep_in_center_of_layer_current_wall(self)->str:
        """ToDo Documentation
        """
    def get_keep_in_center_of_layer_neighbour_wall(self):
        """ToDo Documentation
        """
    def get_unique_layername(self):
        """ToDo Documentation
        """
    def is_auxiliary(self)-> bool:
        """ToDo Documentation
        """
    def is_bottom_plate(self)-> bool:
        """ToDo Documentation
        """
    def is_cutting_element(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_in_axis_direction(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_in_axis_direction_use_max_distance(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_in_axis_direction_use_number(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_perpendicular_to_axis_direction(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self)-> bool:
        """ToDo Documentation
        """
    def is_distribute_perpendicular_to_axis_direction_use_number(self)-> bool:
        """ToDo Documentation
        """
    def is_element_from_detail(self)-> bool:
        """ToDo Documentation
        """
    def is_keep_in_center_of_layer_current_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_keep_in_center_of_layer_neighbour_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_main_element(self)-> bool:
        """ToDo Documentation
        """
    def is_move_according_length_axis(self)-> bool:
        """ToDo Documentation
        """
    def is_move_according_thickness_axis(self)-> bool:
        """ToDo Documentation
        """
    def is_move_with_top_of_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_no_collision_control(self)-> bool:
        """ToDo Documentation
        """
    def is_no_inside_cover_control(self)-> bool:
        """ToDo Documentation
        """
    def is_not_cut_with_cutting_element(self)-> bool:
        """ToDo Documentation
        """
    def is_not_placed_at_end_of_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_not_placed_at_start_of_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_opening_lintel(self)-> bool:
        """ToDo Documentation
        """
    def is_opening_sill(self)-> bool:
        """ToDo Documentation
        """
    def is_solder_in_axis_direction(self)-> bool:
        """ToDo Documentation
        """
    def is_stop_in_axis_direction(self)-> bool:
        """ToDo Documentation
        """
    def is_stop_perpendicular_to_axis_direction(self)-> bool:
        """ToDo Documentation
        """
    def is_strecht_according_length_axis(self)-> bool:
        """ToDo Documentation
        """
    def is_strecht_according_thickness_axis(self)-> bool:
        """ToDo Documentation
        """
    def is_stretch_with_opening_lintel(self)-> bool:
        """ToDo Documentation
        """
    def is_stretch_with_opening_sill(self)-> bool:
        """ToDo Documentation
        """
    def is_stretch_in_opening_width(self)-> bool:
        """ToDo Documentation
        """
    def is_stretch_with_top_of_wall(self)-> bool:
        """ToDo Documentation
        """
    def is_top_plate(self)-> bool:
        """ToDo Documentation
        """
    def is_unique_layername(self)-> bool:
        """ToDo Documentation
        """
    def is_use_for_detail_coordinate_system(self)-> bool:
        """ToDo Documentation
        """
    def set_auxiliary(self, active:bool):
        """ToDo Documentation
        """
    def set_bottom_plate(self, active:bool):
        """ToDo Documentation
        """
    def set_cutting_element(self, active:bool, priority:int):
        """ToDo Documentation
        """
    def set_distribute_in_axis_direction_use_max_distance(self):
        """ToDo Documentation
        """
    def set_distribute_in_axis_direction_use_number(self):
        """ToDo Documentation
        """
    def set_distribute_in_axis_direction(self, active:bool, distance:int):
        """ToDo Documentation
        """
    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self):
        """ToDo Documentation
        """
    def set_distribute_perpendicular_to_axis_direction_use_number(self):
        """ToDo Documentation
        """
    def set_distribute_perpendicular_to_axis_direction(self, active:bool, distance:int):
        """ToDo Documentation
        """
    def set_element_from_detail(self):
        """ToDo Documentation
        """
    def set_keep_in_center_of_layer_current_wall(self):
        """ToDo Documentation
        """
    def set_keep_in_center_of_layer_neighbour_wall(self):
        """ToDo Documentation
        """
    def set_keep_in_center_of_rough_volume(self):
        """ToDo Documentation
        """
    def set_main_element(self):
        """ToDo Documentation
        """
    def set_move_according_length_axis(self):
        """ToDo Documentation
        """
    def set_move_according_thickness_axis(self):
        """ToDo Documentation
        """
    def set_move_with_top_of_wall(self, active:bool):
        """ToDo Documentation
        """
    def set_no_collision_control(self, active:bool):
        """ToDo Documentation
        """
    def set_no_inside_cover_control(self, active:bool):
        """ToDo Documentation
        """
    def set_not_cut_with_cutting_element(self, active:bool):
        """ToDo Documentation
        """
    def set_not_placed_at_end_of_wall(self, active:bool):
        """ToDo Documentation
        """
    def set_not_placed_at_start_of_wall(self, active:bool):
        """ToDo Documentation
        """
    def set_opening_lintel(self):
        """ToDo Documentation
        """
    def set_opening_sill(self):
        """ToDo Documentation
        """
    def set_solder_in_axis_direction(self, active:bool):
        """ToDo Documentation
        """
    def set_stop_in_axis_direction(self, active:bool):
        """ToDo Documentation
        """
    def set_stop_perpendicular_to_axis_direction(self, active:bool):
        """ToDo Documentation
        """
    def set_strecht_according_length_axis(self):
        """ToDo Documentation
        """
    def set_strecht_according_thickness_axis(self):
        """ToDo Documentation
        """
    def set_stretch_with_opening_lintel(self, active:bool):
        """ToDo Documentation
        """
    def set_stretch_with_opening_sill(self, active:bool):
        """ToDo Documentation
        """
    def set_stretch_with_top_of_wall(self, active:bool):
        """ToDo Documentation
        """
    def set_stretch_in_opening_width(self, active:bool):
        """ToDo Documentation
        """
    def set_top_plate(self, active:bool):
        """ToDo Documentation
        """
    def set_unique_layername(self):
        """ToDo Documentation
        """
    def set_use_for_detail_coordinate_system(self, active:bool):
        """ToDo Documentation
        """

class ifc_2x3_element_type():
    def __init__(self) -> None:
        pass
    def is_ifc_beam(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_building_element_part(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_building_element_proxy(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_chimney(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_column(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_covering(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_curtain_wall(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_discrete_accessory(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_door(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_fastener(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_flow_segment(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_footing(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_furnishing_element(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_mechanical_fastener(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_member(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_opening_element(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_plate(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_railing(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_ramp(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_ramp_flight(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_roof(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_slab(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_space(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_stair(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_stair_flight(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_wall(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_wall_standard_case(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_ifc_window(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def is_none(self, ifc_type)->bool:
        """ToDo Documentation
        """
    def set_ifc_beam(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_building_element_part(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_building_element_proxy(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_chimney(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_column(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_covering(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_curtain_wall(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_discrete_accessory(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_door(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_fastener(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_flow_segment(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_footing(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_furnishing_element(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_mechanical_fastener(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_member(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_opening_element(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_plate(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_railing(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_ramp(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_ramp_flight(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_roof(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_slab(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_space(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_stair(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_stair_flight(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_wall(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_wall_standard_case(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_ifc_window(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
    def set_none(self, element_ids:List[int], ifc_type)->None:
        """ToDo Documentation
        """
# Node Symbols
@unique
class node_symbol(Enum):
    """Change node symbol. 

    Args:
        Enum (int): symbol type
    """
    SmallSquare         = 1
    Square              = 2
    Cross               = 3
    Circle              = 4
    FilledCircle        = 5
    ChessSquare         = 6
    HalfFilledSquare    = 7
    CrossSquare         = 8
    FilledSquare        = 9


@unique
class element_module_detail(Enum):
    """Add element situation to detail. 

    Args:
        Enum (int): detail situation
    """
    no_detail          = 0
    angle_detail       = 1
    area_detail        = 2
    cross_detail       = 3
    edge_detail        = 4
    end_detail         = 5
    line_detail        = 6
    open_detail        = 7
    t_detail           = 8
    floor_area_detail  = 10
    floor_end_detail   = 11
    floor_line_detail  = 12
    floor_open_detail  = 13



