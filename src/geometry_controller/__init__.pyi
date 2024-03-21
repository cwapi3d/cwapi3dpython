from typing import List
from cadwork import facet_list
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def rotate_height_axis_90(element_id_list: List[int]) -> None:
    """Rotates the element height axis 90 degrees

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def rotate_height_axis_180(element_id_list: List[int]) -> None:
    """Rotates the element height axis 180 degrees

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_over_width(element_id_list: List[int], value: float) -> None:
    """Sets the element overwidth

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_over_height(element_id_list: List[int], value: float) -> None:
    """Sets the element overheight

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_over_length(element_id_list: List[int], value: float) -> None:
    """Sets the element overlength

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_rounding_width(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding width

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_rounding_height(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding height

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_rounding_length(element_id_list: List[int], value: float) -> None:
    """Sets the element rounding length

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_negative_width(element_id_list: List[int], value: float) -> None:
    """Sets the element negative width cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_positive_width(element_id_list: List[int], value: float) -> None:
    """Sets the element positive width cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_negative_height(element_id_list: List[int], value: float) -> None:
    """Sets the element negative height cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_positive_height(element_id_list: List[int], value: float) -> None:
    """Sets the element positive height cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_negative_length(element_id_list: List[int], value: float) -> None:
    """Sets the element negative length cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def set_cross_correction_positive_length(element_id_list: List[int], value: float) -> None:
    """Sets the element positive length cross correction

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

def apply_global_scale(element_id_list: List[int], scale: float, origin: point_3d) -> None:
    """Applies a global scale to element

    Parameters:
        element_id_list: element_id_list
        scale: scale
        origin: origin

    Returns:
        None
    """

def auto_regenerate_axes(element_id_list: List[int]) -> None:
    """Automatically regenerates axes on element

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def rotate_length_axis_90(element_id_list: List[int]) -> None:
    """Rotates element length axis 90 degrees

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def rotate_length_axis_180(element_id_list: List[int]) -> None:
    """Rotates element length axis 180 degrees

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def invert_model(element_id_list: List[int]) -> None:
    """Inverts element model

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_width_real(elements: List[int], width: float) -> None:
    """Sets the element real width

    Parameters:
        elements: elements
        width: width

    Returns:
        None
    """

def set_height_real(elements: List[int], height: float) -> None:
    """Sets the element real height

    Parameters:
        elements: elements
        height: height

    Returns:
        None
    """

def set_length_real(elements: List[int], length: float) -> None:
    """Gets the element real length

    Parameters:
        elements: elements
        length: length

    Returns:
        None
    """

def rotate_height_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element height axis via 2 points

    Parameters:
        elements: elements
        point1: point1
        point2: point2

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def set_drilling_tolerance(elements: List[int], tolerance: float) -> None:
    """Gets the division zone points

    Parameters:
        elements: elements
        tolerance: tolerance

    Returns:
        None
    """

def auto_regenerate_axes_silently(a0: List[int]) -> None:
    """auto regenerate axes silently

    Parameters:
        a0: a0

    Returns:
        None
    """

def rotate_length_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element length axis via 2 points

    Parameters:
        elements: elements
        point1: point1
        point2: point2

    Returns:
        None
    """

def get_width(element_id: int) -> float:
    """Gets the element width

    Parameters:
        element_id: element_id

    Returns:
        element width
    """

def get_height(element_id: int) -> float:
    """Gets the element height

    Parameters:
        element_id: element_id

    Returns:
        element height
    """

def get_length(element_id: int) -> float:
    """Gets the element length

    Parameters:
        element_id: element_id

    Returns:
        element length
    """

def get_p1(element_id: int) -> point_3d:
    """Gets the element P1

    Parameters:
        element_id: element_id

    Returns:
        element P1
    """

def get_p2(element_id: int) -> point_3d:
    """Gets the element P2

    Parameters:
        element_id: element_id

    Returns:
        element P2
    """

def get_p3(element_id: int) -> point_3d:
    """Gets the element P3

    Parameters:
        element_id: element_id

    Returns:
        element P3
    """

def get_start_height_cut_angle(element_id: int) -> float:
    """Gets the element start height cut angle

    Parameters:
        element_id: element_id

    Returns:
        element start height cut angle
    """

def get_start_width_cut_angle(element_id: int) -> float:
    """Gets the element start width cut angle

    Parameters:
        element_id: element_id

    Returns:
        element start width cut angle
    """

def get_end_height_cut_angle(element_id: int) -> float:
    """Gets the element end height cut angle

    Parameters:
        element_id: element_id

    Returns:
        element end height cut angle
    """

def get_end_width_cut_angle(element_id: int) -> float:
    """Gets the element end width cut angle

    Parameters:
        element_id: element_id

    Returns:
        element end width cut angle
    """

def get_over_width(element_id: int) -> float:
    """Gets the element overwidth

    Parameters:
        element_id: element_id

    Returns:
        element overwidth
    """

def get_over_height(element_id: int) -> float:
    """Gets the element overheight

    Parameters:
        element_id: element_id

    Returns:
        element overheight
    """

def get_over_length(element_id: int) -> float:
    """Gets the element overlength

    Parameters:
        element_id: element_id

    Returns:
        element overlength
    """

def get_rounding_width(element_id: int) -> float:
    """Gets the element rounding width

    Parameters:
        element_id: element_id

    Returns:
        element rounding width
    """

def get_rounding_height(element_id: int) -> float:
    """Gets the element rounding height

    Parameters:
        element_id: element_id

    Returns:
        element rounding height
    """

def get_rounding_length(element_id: int) -> float:
    """Gets the element rounding length

    Parameters:
        element_id: element_id

    Returns:
        element rounding length
    """

def get_cross_correction_negative_width(element_id: int) -> float:
    """Gets the element negative width cross correction

    Parameters:
        element_id: element_id

    Returns:
        element negative width cross correction
    """

def get_cross_correction_positive_width(element_id: int) -> float:
    """Gets the element positive width cross correction

    Parameters:
        element_id: element_id

    Returns:
        element positive width cross correction
    """

def get_cross_correction_negative_height(element_id: int) -> float:
    """Gets the element negative height cross correction

    Parameters:
        element_id: element_id

    Returns:
        element negative height cross correction
    """

def get_cross_correction_positive_height(element_id: int) -> float:
    """Gets the element positive height cross correction

    Parameters:
        element_id: element_id

    Returns:
        element positive height cross correction
    """

def get_cross_correction_negative_length(element_id: int) -> float:
    """Gets the element negative length cross correction

    Parameters:
        element_id: element_id

    Returns:
        element negative length cross correction
    """

def get_cross_correction_positive_length(element_id: int) -> float:
    """Gets the element positive length cross correction

    Parameters:
        element_id: element_id

    Returns:
        element positive length cross correction
    """

def get_weight(element_id: int) -> float:
    """Gets the element real weight

    Parameters:
        element_id: element_id

    Returns:
        element real weight
    """

def get_list_weight(element_id: int) -> float:
    """Gets the element list weight

    Parameters:
        element_id: element_id

    Returns:
        element list weight
    """

def get_volume(element_id: int) -> float:
    """Gets the element real volume

    Parameters:
        element_id: element_id

    Returns:
        element real volume
    """

def get_list_volume(element_id: int) -> float:
    """Gets the element list volume

    Parameters:
        element_id: element_id

    Returns:
        element list volume
    """

def get_xl(element_id: int) -> point_3d:
    """Gets the element XL vector

    Parameters:
        element_id: element_id

    Returns:
        element XL vector
    """

def get_yl(element_id: int) -> point_3d:
    """Gets the element YL vector

    Parameters:
        element_id: element_id

    Returns:
        element YL vector
    """

def get_zl(element_id: int) -> point_3d:
    """Gets the element ZL vector

    Parameters:
        element_id: element_id

    Returns:
        element ZL vector
    """

def get_center_of_gravity(element_id: int) -> point_3d:
    """Gets the element center of gravity

    Parameters:
        element_id: element_id

    Returns:
        element center of gravity
    """

def get_reference_side(element_id: int) -> int:
    """Gets the element reference side

    Parameters:
        element_id: element_id

    Returns:
        element reference side
    """

def get_element_vertices(element_id: int) -> List[point_3d]:
    """Gets the element vertices

    Parameters:
        element_id: element_id

    Returns:
        element vertices
    """

def get_element_facets(element_id: int) -> facet_list:
    """Gets the element facets

    Parameters:
        element_id: element_id

    Returns:
        element facets
    """

def get_list_width(element_id: int) -> float:
    """Get the element list width

    Parameters:
        element_id: element_id

    Returns:
        element list width
    """

def get_list_height(element_id: int) -> float:
    """Gets the element list height

    Parameters:
        element_id: element_id

    Returns:
        element list height
    """

def get_list_length(element_id: int) -> float:
    """Gets the element list length

    Parameters:
        element_id: element_id

    Returns:
        element list length
    """

def get_minimum_distance_between_elements(first_id: int, second_id: int) -> float:
    """Gets the minimum distance between 2 elements

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        minimum distance
    """

def get_total_area_of_all_faces(element: int) -> float:
    """Gets the total area of all faces for element

    Parameters:
        element: element

    Returns:
        element total faces area
    """

def get_area_of_front_face(element: int) -> float:
    """Gets the front face are for element

    Parameters:
        element: element

    Returns:
        element front face area
    """

def get_door_surface(elements: List[int]) -> float:
    """Gets the element door surface

    Parameters:
        elements: elements

    Returns:
        element door surface
    """

def get_window_surface(elements: List[int]) -> float:
    """Gets the element window surface

    Parameters:
        elements: elements

    Returns:
        element window surface
    """

def get_local_x() -> point_3d:
    """Gets the local X vector

    Returns:
        local X vector
    """

def get_local_z() -> point_3d:
    """Gets the local Y vector

    Returns:
        local Y vector
    """

def get_local_y() -> point_3d:
    """Gets the local Z vector

    Returns:
        local Z vector
    """

def get_drilling_tolerance(element: int) -> float:
    """Gets the drilling tolerance of an axis

    Parameters:
        element: element

    Returns:
        the drilling tolerance
    """

def get_element_reference_face_vertices(element_id: int) -> List[point_3d]:
    """Gets the vertices of the reference side

    Parameters:
        element_id: element_id

    Returns:
        vertexlist of all points
    """

def get_element_reference_face_area(element_id: int) -> float:
    """Gets the area of the reference side

    Parameters:
        element_id: element_id

    Returns:
        area(size) of reference face
    """

def get_center_of_gravity_for_list(elements: List[int]) -> point_3d:
    """get center of gravity for list

    Parameters:
        elements: elements

    Returns:
        point_3d
    """

def get_center_of_gravity_for_list_considering_materials(elements: List[int]) -> point_3d:
    """get center of gravity for list considering materials

    Parameters:
        elements: elements

    Returns:
        point_3d
    """

def get_element_facet_count(element_id: int) -> int:
    """get element facet count

    Parameters:
        element_id: element_id

    Returns:
        int
    """

def get_weight_real(element_id: int) -> float:
    """get weight real

    Parameters:
        element_id: element_id

    Returns:
        float
    """

def get_actual_physical_weight(a0: int) -> float:
    """get actual physical weight

    Parameters:
        a0: a0

    Returns:
        float
    """

def get_actual_physical_volume(a0: int) -> float:
    """get actual physical volume

    Parameters:
        a0: a0

    Returns:
        float
    """

def are_facets_coplanar(a0: List[point_3d], a1: List[point_3d]) -> bool:
    """are facets coplanar

    Parameters:
        a0: a0
        a1: a1

    Returns:
        bool
    """

