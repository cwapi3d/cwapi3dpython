from typing import List
from cadwork import point_3d


def get_width(element: int) -> float:
    """Get element width. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float: width
    """


def get_height(element: int) -> float:
    """Get element height. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float: height
    """


def get_length(element: int) -> float:
    """Get element length. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float: length
    """


def get_p1(element: int) -> point_3d:
    """Get start Point of element. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: start point
    """


def get_p2(element: int) -> point_3d:
    """Get end Point of element. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: end point
    """


def get_p3(element: int) -> point_3d:
    """Point for orientation of the Z axis of the element. This point is on the same plane as point 1.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: orientation point
    """


def get_start_height_cut_angle(element: int) -> float:
    """get start height cut angle

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID 

    Returns:
        float:  value
    """


def get_start_width_cut_angle(element: int) -> float:
    """get start width cut angle

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_end_height_cut_angle(element: int) -> float:
    """get end height cut angle

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_end_width_cut_angle(element: int) -> float:
    """get end width cut angle

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def rotate_height_axis_90(elements: List[int]) -> None:
    """rotate element height axis 90° 

    Args:
        elements (List[int]):  element IDs
    """


def rotate_height_axis_180(elements: List[int]) -> None:
    """rotate element height axis 180° 

    Args:
        elements (List[int]):  element IDs
    """


def get_over_width(element: int) -> float:
    """get over widht

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_over_width(element: int, value: float) -> None:
    """set over width

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_over_height(element: int) -> float:
    """get over height

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_over_height(element: int, value: float) -> None:
    """set over height

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_over_length(element: int) -> float:
    """get over length

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_over_length(element: int, value: float) -> None:
    """set over length

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_rounding_width(element: int) -> float:
    """get rounding width

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_rounding_width(element: int, value: float) -> None:
    """set rounding width

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_rounding_height(element: int) -> float:
    """get rounding height

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_rounding_height(element: int, value: float) -> None:
    """set rounding height

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_rounding_length(element: int) -> float:
    """get rounding length

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_rounding_length(element: int, value: float) -> None:
    """set rounding length

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_negative_width(element: int) -> float:
    """get cross correction negative width

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_negative_width(element: int, value: float) -> None:
    """set cross correction negative width

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_positive_width(element: int) -> float:
    """get cross correction positive width

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_positive_width(element: int, value: float) -> None:
    """set cross correction positive width

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_negative_height(element: int) -> float:
    """set cross correction negative height

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_negative_height(element: int, value: float) -> None:
    """set cross correction negative height

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_positive_height(element: int) -> float:
    """get cross correction positive height

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_positive_height(element: int, value: float) -> None:
    """set cross correction positive height

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_negative_length(element: int) -> float:
    """get cross correction negative length

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_negative_length(element: int, value: float) -> None:
    """set cross correction negative length

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_cross_correction_positive_length(element: int) -> float:
    """get cross correction positive length

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_cross_correction_positive_length(element: int, value: float) -> None:
    """set cross correction positive length

    Args:
        element (int): element ID
        value (float):  a value
    """


def get_weight(element: int) -> float:
    """get element weight

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_list_weight(element: int) -> float:
    """get element list weight 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_volume(element: int) -> float:
    """get element volume

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_list_volume(element: int) -> float:
    """get element list volume

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_xl(element: int) -> point_3d:
    """get local X vector

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_yl(element: int) -> point_3d:
    """get local Y vector

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_zl(element: int) -> point_3d:
    """get local Z vector

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_center_of_gravity(element: int) -> point_3d:
    """get center of gravity geometrical 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_center_of_gravity_for_list_considering_materials(elements: List[int]) -> point_3d:
    """get center of gravity considering material weights 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]):  element IDs

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_reference_side(element: int) -> int:
    """get element reference side

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: face ID
    """


def get_element_vertices(element: int) -> List[point_3d]:
    """get BREP vertices of element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[point_3d]: vertex list
    """


def apply_global_scale(elements: List[int], scale: float, origin: point_3d) -> None:
    """apply global scale

    Args:
        elements (List[int]):  element IDs
        scale (float): scale factor
        origin (point_3d): a origin
    """


def auto_regenerate_axes(elements: List[int]) -> None:
    """regenerate element axis system

    Args:
        elements (List[int]):  element IDs
    """


def rotate_length_axis_90(elements: List[int]) -> None:
    """rotate length axis 90°

    Args:
        elements (List[int]):  element IDs
    """


def rotate_length_axis_180(elements: List[int]) -> None:
    """rotate length axis 180°

    Args:
        elements (List[int]):  element IDs
    """


def invert_model(elements: List[int]) -> None:
    """Inverts element model

    Args:
        elements (List[int]):  element IDs
    """


def get_element_facets(element: int) -> List[List[point_3d]]:
    """get element facets in a nested list

    Args:
        element (int): element ID

    Returns:
        List[List[point_3d]]: nested vertex list
    """


def get_list_width(element: int) -> float:
    """get list width

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_list_height(element: int) -> float:
    """get list height

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_list_length(element: int) -> float:
    """get list length

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def set_width_real(elements: List[int], value: float) -> None:
    """set width real

    Args:
        elements (List[int]):  element IDs
        value (float):  a value
    """


def set_height_real(elements: List[int], value: float) -> None:
    """set height real

    Args:
        elements (List[int]):  element IDs
        value (float):  a value
    """


def set_length_real(elements: List[int], value: float) -> None:
    """set length real

    Args:
        elements (List[int]):  element IDs
        value (float):  a value
    """


def rotate_height_axis_2_points(elements: List[int], start: point_3d, end: point_3d) -> None:
    """rotate height axis via 2 points. The axis is defined by a point 1 and a point 2. 

    Args:
        elements (List[int]):  element IDs
        start (point_3d): start point
        end (point_3d): end point
    """


def get_minimum_distance_between_elements(first_element: int, second_element: int) -> float:
    """get the minimum distance between two elements

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        first_element (int): element ID
        second_element (int): element ID

    Returns:
        float:  value
    """


def get_total_area_of_all_faces(element: int) -> float:
    """get total area fo all element faces

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_area_of_front_face(element: int) -> float:
    """get area of reference face

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_door_surface(elements: List[int]) -> float:
    """get door surface

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]):  element IDs

    Returns:
        float:  value
    """


def get_window_surface(elements: List[int]) -> float:
    """get window surface

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]):  element IDs

    Returns:
        float:  value
    """


def get_local_x() -> point_3d:
    """X vector of the coordinate system in 3D

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_local_z() -> point_3d:
    """Z vector of the coordinate system in 3D

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        point_3d: point_3d (x,y,z)
    """


def get_local_y() -> point_3d:
    """Y vector of the coordinate system in 3D

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        point_3d: point_3d (x,y,z)
    """


def set_drilling_tolerance(elements: List[int], value: float) -> None:
    """set drilling tolerance

    Args:
        elements (List[int]):  element IDs
        value (float):  a value
    """


def get_drilling_tolerance(element: int) -> float:
    """get drilling tolerance

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def get_element_reference_face_vertices(element: int) -> List[point_3d]:
    """get element reference face vertices

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[point_3d]: vertex list
    """


def get_element_reference_face_area(element: int) -> float:
    """get element reference face area

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float:  value
    """


def auto_regenerate_axes_silently(elements: List[int]) -> None:
    """automatic, silent regeneration of element axes 

    Args:
        elements (List[int]):  element IDs
    """


def rotate_length_axis_2_points(elements: List[int], start: point_3d, end: point_3d) -> None:
    """rotate length axis via 2 points. The axis is defined by a point 1 and a point 2. 

    Args:
        elements (List[int]):  element IDs
        start (point_3d): start point
        end (point_3d): end point
    """


def get_center_of_gravity_for_list(elements: List[int]) -> point_3d:
    """get geometrical center of gravity for elements

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]):  element IDs

    Returns:
        point_3d: point_3d (x,y,z)
    """


def are_facets_coplanar(vertices_first_plane: List[point_3d], vertices_second_plane: List[point_3d]) -> bool:
    """checks if points of facet/plane are coplanar

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        vertices_first_plane (List[point_3d]): a first point list
        vertices_second_plane (List[point_3d]): a second point list

    Returns:
        bool: are facets/vertices coplanar
    """


def get_actual_physical_volume(element: int) -> float:
    """get the real/physical volume of an element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float: volume
    """


def get_element_facet_count(element: int) -> int:
    """Get element facet count

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: number of facets
    """


def get_weight_real(element: int) -> float:
    """Get weight real

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        float: weight real
    """
