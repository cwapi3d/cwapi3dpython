from typing import List
from cadwork import facet_list
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def rotate_height_axis_90(element_id_list: List[int]) -> None:
    """rotate height axis 90
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_height_axis_180(element_id_list: List[int]) -> None:
    """rotate height axis 180
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_over_width(element_id_list: List[int], value: float) -> None:
    """set over width
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_over_height(element_id_list: List[int], value: float) -> None:
    """set over height
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_over_length(element_id_list: List[int], value: float) -> None:
    """set over length
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_width(element_id_list: List[int], value: float) -> None:
    """set rounding width
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_height(element_id_list: List[int], value: float) -> None:
    """set rounding height
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_rounding_length(element_id_list: List[int], value: float) -> None:
    """set rounding length
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_width(element_id_list: List[int], value: float) -> None:
    """set cross correction negative width
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_width(element_id_list: List[int], value: float) -> None:
    """set cross correction positive width
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_height(element_id_list: List[int], value: float) -> None:
    """set cross correction negative height
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_height(element_id_list: List[int], value: float) -> None:
    """set cross correction positive height
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_negative_length(element_id_list: List[int], value: float) -> None:
    """set cross correction negative length
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def set_cross_correction_positive_length(element_id_list: List[int], value: float) -> None:
    """set cross correction positive length
    Args:
        element_id_list ( List[int]): element_id_list
        value ( float): value

    Returns:
        None
    """

def apply_global_scale(element_id_list: List[int], scale: float, origin: point_3d) -> None:
    """apply global scale
    Args:
        element_id_list ( List[int]): element_id_list
        scale ( float): scale
        origin ( point_3d): origin

    Returns:
        None
    """

def auto_regenerate_axes(element_id_list: List[int]) -> None:
    """auto regenerate axes
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_length_axis_90(element_id_list: List[int]) -> None:
    """rotate length axis 90
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def rotate_length_axis_180(element_id_list: List[int]) -> None:
    """rotate length axis 180
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def invert_model(element_id_list: List[int]) -> None:
    """invert model
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_width_real(elements: List[int], width: float) -> None:
    """set width real
    Args:
        elements ( List[int]): elements
        width ( float): width

    Returns:
        None
    """

def set_height_real(elements: List[int], height: float) -> None:
    """set height real
    Args:
        elements ( List[int]): elements
        height ( float): height

    Returns:
        None
    """

def set_length_real(elements: List[int], length: float) -> None:
    """set length real
    Args:
        elements ( List[int]): elements
        length ( float): length

    Returns:
        None
    """

def rotate_height_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """rotate height axis 2 points
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
    """set drilling tolerance
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
    """rotate length axis 2 points
    Args:
        elements ( List[int]): elements
        point1 ( point_3d): point1
        point2 ( point_3d): point2

    Returns:
        None
    """

def get_width(id: int) -> float:
    """get width
    Args:
        id ( int): id

    Returns:
        element width (float)
    """

def get_height(id: int) -> float:
    """get height
    Args:
        id ( int): id

    Returns:
        element height (float)
    """

def get_length(id: int) -> float:
    """get length
    Args:
        id ( int): id

    Returns:
        element length (float)
    """

def get_p1(id: int) -> point_3d:
    """get p1
    Args:
        id ( int): id

    Returns:
        element P1 (point_3d)
    """

def get_p2(id: int) -> point_3d:
    """get p2
    Args:
        id ( int): id

    Returns:
        element P2 (point_3d)
    """

def get_p3(id: int) -> point_3d:
    """get p3
    Args:
        id ( int): id

    Returns:
        element P3 (point_3d)
    """

def get_start_height_cut_angle(id: int) -> float:
    """get start height cut angle
    Args:
        id ( int): id

    Returns:
        element start height cut angle (float)
    """

def get_start_width_cut_angle(id: int) -> float:
    """get start width cut angle
    Args:
        id ( int): id

    Returns:
        element start width cut angle (float)
    """

def get_end_height_cut_angle(id: int) -> float:
    """get end height cut angle
    Args:
        id ( int): id

    Returns:
        element end height cut angle (float)
    """

def get_end_width_cut_angle(id: int) -> float:
    """get end width cut angle
    Args:
        id ( int): id

    Returns:
        element end width cut angle (float)
    """

def get_over_width(id: int) -> float:
    """get over width
    Args:
        id ( int): id

    Returns:
        element overwidth (float)
    """

def get_over_height(id: int) -> float:
    """get over height
    Args:
        id ( int): id

    Returns:
        element overheight (float)
    """

def get_over_length(id: int) -> float:
    """get over length
    Args:
        id ( int): id

    Returns:
        element overlength (float)
    """

def get_rounding_width(id: int) -> float:
    """get rounding width
    Args:
        id ( int): id

    Returns:
        element rounding width (float)
    """

def get_rounding_height(id: int) -> float:
    """get rounding height
    Args:
        id ( int): id

    Returns:
        element rounding height (float)
    """

def get_rounding_length(id: int) -> float:
    """get rounding length
    Args:
        id ( int): id

    Returns:
        element rounding length (float)
    """

def get_cross_correction_negative_width(id: int) -> float:
    """get cross correction negative width
    Args:
        id ( int): id

    Returns:
        element negative width cross correction (float)
    """

def get_cross_correction_positive_width(id: int) -> float:
    """get cross correction positive width
    Args:
        id ( int): id

    Returns:
        element positive width cross correction (float)
    """

def get_cross_correction_negative_height(id: int) -> float:
    """get cross correction negative height
    Args:
        id ( int): id

    Returns:
        element negative height cross correction (float)
    """

def get_cross_correction_positive_height(id: int) -> float:
    """get cross correction positive height
    Args:
        id ( int): id

    Returns:
        element positive height cross correction (float)
    """

def get_cross_correction_negative_length(id: int) -> float:
    """get cross correction negative length
    Args:
        id ( int): id

    Returns:
        element negative length cross correction (float)
    """

def get_cross_correction_positive_length(id: int) -> float:
    """get cross correction positive length
    Args:
        id ( int): id

    Returns:
        element positive length cross correction (float)
    """

def get_weight(id: int) -> float:
    """get weight
    Args:
        id ( int): id

    Returns:
        element real weight (float)
    """

def get_list_weight(id: int) -> float:
    """get list weight
    Args:
        id ( int): id

    Returns:
        element list weight (float)
    """

def get_volume(id: int) -> float:
    """get volume
    Args:
        id ( int): id

    Returns:
        element real volume (float)
    """

def get_list_volume(id: int) -> float:
    """get list volume
    Args:
        id ( int): id

    Returns:
        element list volume (float)
    """

def get_xl(id: int) -> point_3d:
    """get xl
    Args:
        id ( int): id

    Returns:
        element XL vector (point_3d)
    """

def get_yl(id: int) -> point_3d:
    """get yl
    Args:
        id ( int): id

    Returns:
        element YL vector (point_3d)
    """

def get_zl(id: int) -> point_3d:
    """get zl
    Args:
        id ( int): id

    Returns:
        element ZL vector (point_3d)
    """

def get_center_of_gravity(id: int) -> point_3d:
    """get center of gravity
    Args:
        id ( int): id

    Returns:
        element center of gravity (point_3d)
    """

def get_reference_side(id: int) -> int:
    """get reference side
    Args:
        id ( int): id

    Returns:
        element reference side (int)
    """

def get_element_vertices(id: int) -> List[point_3d]:
    """get element vertices
    Args:
        id ( int): id

    Returns:
        element vertices (List[point_3d])
    """

def get_element_facets(id: int) -> facet_list:
    """get element facets
    Args:
        id ( int): id

    Returns:
        element facets (facet_list)
    """

def get_list_width(id: int) -> float:
    """get list width
    Args:
        id ( int): id

    Returns:
        element list width (float)
    """

def get_list_height(id: int) -> float:
    """get list height
    Args:
        id ( int): id

    Returns:
        element list height (float)
    """

def get_list_length(id: int) -> float:
    """get list length
    Args:
        id ( int): id

    Returns:
        element list length (float)
    """

def get_minimum_distance_between_elements(first_id: int, second_id: int) -> float:
    """get minimum distance between elements
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        minimum distance (float)
    """

def get_total_area_of_all_faces(element: int) -> float:
    """get total area of all faces
    Args:
        element ( int): element

    Returns:
        element total faces area (float)
    """

def get_area_of_front_face(element: int) -> float:
    """get area of front face
    Args:
        element ( int): element

    Returns:
        element front face area (float)
    """

def get_door_surface(elements: List[int]) -> float:
    """get door surface
    Args:
        elements ( List[int]): elements

    Returns:
        element door surface (float)
    """

def get_window_surface(elements: List[int]) -> float:
    """get window surface
    Args:
        elements ( List[int]): elements

    Returns:
        element window surface (float)
    """

def get_local_x() -> point_3d:
    """get local x
    Args:

    Returns:
        local X vector (point_3d)
    """

def get_local_z() -> point_3d:
    """get local z
    Args:

    Returns:
        local Y vector (point_3d)
    """

def get_local_y() -> point_3d:
    """get local y
    Args:

    Returns:
        local Z vector (point_3d)
    """

def get_drilling_tolerance(element: int) -> float:
    """get drilling tolerance
    Args:
        element ( int): element

    Returns:
        the drilling tolerance (float)
    """

def get_element_reference_face_vertices(element_id: int) -> List[point_3d]:
    """get element reference face vertices
    Args:
        element_id ( int): element_id

    Returns:
        vertexlist of all points (List[point_3d])
    """

def get_element_reference_face_area(element_id: int) -> float:
    """get element reference face area
    Args:
        element_id ( int): element_id

    Returns:
        area(size) of reference face (float)
    """

def get_center_of_gravity_for_list(elements: List[int]) -> point_3d:
    """get center of gravity for list
    Args:
        elements ( List[int]): elements

    Returns:
        point_3d
    """

def get_center_of_gravity_for_list_considering_materials(elements: List[int]) -> point_3d:
    """get center of gravity for list considering materials
    Args:
        elements ( List[int]): elements

    Returns:
        point_3d
    """

def get_element_facet_count(id: int) -> int:
    """get element facet count
    Args:
        id ( int): id

    Returns:
        int
    """

def get_weight_real(id: int) -> float:
    """get weight real
    Args:
        id ( int): id

    Returns:
        float
    """

def get_actual_physical_weight(a0: int) -> float:
    """get actual physical weight
    Args:
        a0 ( int): a0

    Returns:
        float
    """

def get_actual_physical_volume(a0: int) -> float:
    """get actual physical volume
    Args:
        a0 ( int): a0

    Returns:
        float
    """

def are_facets_coplanar(a0: List[point_3d], a1: List[point_3d]) -> bool:
    """are facets coplanar
    Args:
        a0 ( List[point_3d]): a0
        a1 ( List[point_3d]): a1

    Returns:
        bool
    """

