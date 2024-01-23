from typing import List
from cadwork import facet_list
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """Gets the last error 
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def rotate_height_axis_90(element_id_list: List[int]) -> None:
    """Rotates the element height axis 90 degrees 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_height_axis_180(element_id_list: List[int]) -> None:
    """Rotates the element height axis 180 degrees 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_over_width(element_id_list: List[int], value: float) -> None:
    """Sets the element overwidth 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_over_height(element_id_list: List[int], value: float) -> None:
    """Sets the element overheight 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_over_length(element_id_list: List[int], value: float) -> None:
    """Sets the element overlength 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_width(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding width 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_height(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding height 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_length(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding length 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_width(element_id_list: List[int], value: float) -> None:
    """Sets the element negative width cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_width(element_id_list: List[int], value: float) -> None:
    """Sets the element positive width cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_height(element_id_list: List[int], value: float) -> None:
    """Sets the element negative height cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_height(element_id_list: List[int], value: float) -> None:
    """Sets the element positive height cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_length(element_id_list: List[int], value: float) -> None:
    """Sets the element negative length cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_length(element_id_list: List[int], value: float) -> None:
    """Sets the element positive length cross correction 
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def apply_global_scale(element_id_list: List[int], scale: float, origin: point_3d) -> None:
    """Applies a global scale to element 
    Args:
        element_id_list ( List[int]): element_id_list
        scale ( float): scale
        origin ( point_3d): origin

    Returns:
        None
    """

def auto_regenerate_axes(element_id_list: List[int]) -> None:
    """Automatically regenerates axes on element 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_length_axis_90(element_id_list: List[int]) -> None:
    """Rotates element length axis 90 degrees 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_length_axis_180(element_id_list: List[int]) -> None:
    """Rotates element length axis 180 degrees 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def invert_model(element_id_list: List[int]) -> None:
    """Inverts element model 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_width_real(elements: List[int], width: float) -> None:
    """Sets the element real width 
    Args:
        elements ( List[int]): elements
        width ( float): width

    Returns:
        None
    """

def set_height_real(elements: List[int], height: float) -> None:
    """Sets the element real height 
    Args:
        elements ( List[int]): elements
        height ( float): height

    Returns:
        None
    """

def set_length_real(elements: List[int], length: float) -> None:
    """Gets the element real length 
    Args:
        elements ( List[int]): elements
        length ( float): length

    Returns:
        None
    """

def rotate_height_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element height axis via 2 points 
    Args:
        elements ( List[int]): elements
        point1 ( point_3d): point1
        point2 ( point_3d): point2

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def set_drilling_tolerance(elements: List[int], tolerance: float) -> None:
    """Gets the division zone points 
    Args:
        elements ( List[int]): elements
        tolerance ( float): tolerance

    Returns:
        None
    """

def auto_regenerate_axes_silently(a0: List[int]) -> None:
    """auto regenerate axes silently
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def rotate_length_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element length axis via 2 points 
    Args:
        elements ( List[int]): elements
        point1 ( point_3d): point1
        point2 ( point_3d): point2

    Returns:
        None
    """

def get_width(element_id: int) -> float:
    """Gets the element width 
    Args:
        element_id ( int): element_id

    Returns:
        element width (float)
    """

def get_height(element_id: int) -> float:
    """Gets the element height 
    Args:
        element_id ( int): element_id

    Returns:
        element height (float)
    """

def get_length(element_id: int) -> float:
    """Gets the element length 
    Args:
        element_id ( int): element_id

    Returns:
        element length (float)
    """

def get_p1(element_id: int) -> point_3d:
    """Gets the element P1 
    Args:
        element_id ( int): element_id

    Returns:
        element P1 (point_3d)
    """

def get_p2(element_id: int) -> point_3d:
    """Gets the element P2 
    Args:
        element_id ( int): element_id

    Returns:
        element P2 (point_3d)
    """

def get_p3(element_id: int) -> point_3d:
    """Gets the element P3 
    Args:
        element_id ( int): element_id

    Returns:
        element P3 (point_3d)
    """

def get_start_height_cut_angle(element_id: int) -> float:
    """Gets the element start height cut angle 
    Args:
        element_id ( int): element_id

    Returns:
        element start height cut angle (float)
    """

def get_start_width_cut_angle(element_id: int) -> float:
    """Gets the element start width cut angle 
    Args:
        element_id ( int): element_id

    Returns:
        element start width cut angle (float)
    """

def get_end_height_cut_angle(element_id: int) -> float:
    """Gets the element end height cut angle 
    Args:
        element_id ( int): element_id

    Returns:
        element end height cut angle (float)
    """

def get_end_width_cut_angle(element_id: int) -> float:
    """Gets the element end width cut angle 
    Args:
        element_id ( int): element_id

    Returns:
        element end width cut angle (float)
    """

def get_over_width(element_id: int) -> float:
    """Gets the element overwidth 
    Args:
        element_id ( int): element_id

    Returns:
        element overwidth (float)
    """

def get_over_height(element_id: int) -> float:
    """Gets the element overheight 
    Args:
        element_id ( int): element_id

    Returns:
        element overheight (float)
    """

def get_over_length(element_id: int) -> float:
    """Gets the element overlength 
    Args:
        element_id ( int): element_id

    Returns:
        element overlength (float)
    """

def get_rounding_width(element_id: int) -> float:
    """Gets the element rounding width 
    Args:
        element_id ( int): element_id

    Returns:
        element rounding width (float)
    """

def get_rounding_height(element_id: int) -> float:
    """Gets the element rounding height 
    Args:
        element_id ( int): element_id

    Returns:
        element rounding height (float)
    """

def get_rounding_length(element_id: int) -> float:
    """Gets the element rounding length 
    Args:
        element_id ( int): element_id

    Returns:
        element rounding length (float)
    """

def get_cross_correction_negative_width(element_id: int) -> float:
    """Gets the element negative width cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element negative width cross correction (float)
    """

def get_cross_correction_positive_width(element_id: int) -> float:
    """Gets the element positive width cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element positive width cross correction (float)
    """

def get_cross_correction_negative_height(element_id: int) -> float:
    """Gets the element negative height cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element negative height cross correction (float)
    """

def get_cross_correction_positive_height(element_id: int) -> float:
    """Gets the element positive height cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element positive height cross correction (float)
    """

def get_cross_correction_negative_length(element_id: int) -> float:
    """Gets the element negative length cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element negative length cross correction (float)
    """

def get_cross_correction_positive_length(element_id: int) -> float:
    """Gets the element positive length cross correction 
    Args:
        element_id ( int): element_id

    Returns:
        element positive length cross correction (float)
    """

def get_weight(element_id: int) -> float:
    """Gets the element real weight 
    Args:
        element_id ( int): element_id

    Returns:
        element real weight (float)
    """

def get_list_weight(element_id: int) -> float:
    """Gets the element list weight 
    Args:
        element_id ( int): element_id

    Returns:
        element list weight (float)
    """

def get_volume(element_id: int) -> float:
    """Gets the element raw volume 

    This does not include negative geometry operations, such as end-types,
    drillings, connectors, openings, and MEP elements.

    Args:
        element_id ( int): element_id

    Returns:
        element raw volume (float)
    """

def get_list_volume(element_id: int) -> float:
    """Gets the element list volume 
    Args:
        element_id ( int): element_id

    Returns:
        element list volume (float)
    """

def get_xl(element_id: int) -> point_3d:
    """Gets the element XL vector 
    Args:
        element_id ( int): element_id

    Returns:
        element XL vector (point_3d)
    """

def get_yl(element_id: int) -> point_3d:
    """Gets the element YL vector 
    Args:
        element_id ( int): element_id

    Returns:
        element YL vector (point_3d)
    """

def get_zl(element_id: int) -> point_3d:
    """Gets the element ZL vector 
    Args:
        element_id ( int): element_id

    Returns:
        element ZL vector (point_3d)
    """

def get_center_of_gravity(element_id: int) -> point_3d:
    """Gets the element center of gravity 
    Args:
        element_id ( int): element_id

    Returns:
        element center of gravity (point_3d)
    """

def get_reference_side(element_id: int) -> int:
    """Gets the element reference side 
    Args:
        element_id ( int): element_id

    Returns:
        element reference side (int)
    """

def get_element_vertices(element_id: int) -> List[point_3d]:
    """Gets the element vertices 
    Args:
        element_id ( int): element_id

    Returns:
        element vertices (List[point_3d])
    """

def get_element_facets(element_id: int) -> facet_list:
    """Gets the element facets 
    Args:
        element_id ( int): element_id

    Returns:
        element facets (facet_list)
    """

def get_list_width(element_id: int) -> float:
    """Get the element list width 
    Args:
        element_id ( int): element_id

    Returns:
        element list width (float)
    """

def get_list_height(element_id: int) -> float:
    """Gets the element list height 
    Args:
        element_id ( int): element_id

    Returns:
        element list height (float)
    """

def get_list_length(element_id: int) -> float:
    """Gets the element list length 
    Args:
        element_id ( int): element_id

    Returns:
        element list length (float)
    """

def get_minimum_distance_between_elements(first_id: int, second_id: int) -> float:
    """Gets the minimum distance between 2 elements 
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        minimum distance (float)
    """

def get_total_area_of_all_faces(element: int) -> float:
    """Gets the total area of all faces for element 
    Args:
        element ( int): element

    Returns:
        element total faces area (float)
    """

def get_area_of_front_face(element: int) -> float:
    """Gets the front face are for element 
    Args:
        element ( int): element

    Returns:
        element front face area (float)
    """

def get_door_surface(elements: List[int]) -> float:
    """Gets the element door surface 
    Args:
        elements ( List[int]): elements

    Returns:
        element door surface (float)
    """

def get_window_surface(elements: List[int]) -> float:
    """Gets the element window surface 
    Args:
        elements ( List[int]): elements

    Returns:
        element window surface (float)
    """

def get_local_x() -> point_3d:
    """Gets the local X vector 
    Args:

    Returns:
        local X vector (point_3d)
    """

def get_local_z() -> point_3d:
    """Gets the local Y vector 
    Args:

    Returns:
        local Y vector (point_3d)
    """

def get_local_y() -> point_3d:
    """Gets the local Z vector 
    Args:

    Returns:
        local Z vector (point_3d)
    """

def get_drilling_tolerance(element: int) -> float:
    """Gets the drilling tolerance of an axis 
    Args:
        element ( int): element

    Returns:
        the drilling tolerance (float)
    """

def get_element_reference_face_vertices(element_id: int) -> List[point_3d]:
    """Gets the vertices of the reference side 
    Args:
        element_id ( int): element_id

    Returns:
        vertexlist of all points (List[point_3d])
    """

def get_element_reference_face_area(element_id: int) -> float:
    """Gets the area of the reference side 
    Args:
        element_id ( int): element_id

    Returns:
        area (size) of reference face (float)
    """

def get_center_of_gravity_for_list(elements: List[int]) -> point_3d:
    """Gets center of gravity for list 
    Args:
        elements ( List[int]): elements

    Returns:
        center of gravity (point_3d)
    """

def get_center_of_gravity_for_list_considering_materials(elements: List[int]) -> point_3d:
    """Gets center of gravity for list considering materials 
    Args:
        elements ( List[int]): elements

    Returns:
        center of gravity (point_3d)
    """

def get_element_facet_count(element_id: int) -> int:
    """Gets element facet count 
    Args:
        element_id ( int): element_id

    Returns:
        element facet count (int)
    """

def get_weight_real(element_id: int) -> float:
    """Gets weight of the element 
    Args:
        element_id ( int): element_id

    Returns:
        weight of the element (float)
    """

def get_actual_physical_weight(a0: int) -> float:
    """Gets actual physical weight 
    Args:
        a0 ( int): a0

    Returns:
        actual physical weight (float)
    """

def get_actual_physical_volume(a0: int) -> float:
    """Gets actual physical volume 

    This includes negative geometry operations, such as end-types, drillings,
    connectors, openings, and MEP elements. It might also take into account
    different drilling bodies and counterbores in a connector.

    Args:
        a0 ( int): a0

    Returns:
        actual physical volume (float)
    """

def are_facets_coplanar(a0: List[point_3d], a1: List[point_3d]) -> bool:
    """Tests if facets are coplanar 
    Args:
        a0 ( List[point_3d]): a0
        a1 ( List[point_3d]): a1

    Returns:
        are facets coplanar (bool)
    """

