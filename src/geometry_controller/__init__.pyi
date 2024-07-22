from typing import List
from cadwork import facet_list
from cadwork import point_3d


def rotate_height_axis_90(element_id_list: List[int]) -> None:
    """rotate height axis 90

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def rotate_height_axis_180(element_id_list: List[int]) -> None:
    """rotate height axis 180

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_over_width(element_id_list: List[int], value: float) -> None:
    """set over width

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_over_height(element_id_list: List[int], value: float) -> None:
    """set over height

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_over_length(element_id_list: List[int], value: float) -> None:
    """set over length

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_rounding_width(element_id_list: List[int], value: float) -> None:
    """set rounding width

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_rounding_height(element_id_list: List[int], value: float) -> None:
    """set rounding height

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_rounding_length(element_id_list: List[int], value: float) -> None:
    """set rounding length

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_negative_width(element_id_list: List[int], value: float) -> None:
    """set cross correction negative width

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_positive_width(element_id_list: List[int], value: float) -> None:
    """set cross correction positive width

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_negative_height(element_id_list: List[int], value: float) -> None:
    """set cross correction negative height

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_positive_height(element_id_list: List[int], value: float) -> None:
    """set cross correction positive height

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_negative_length(element_id_list: List[int], value: float) -> None:
    """set cross correction negative length

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_cross_correction_positive_length(element_id_list: List[int], value: float) -> None:
    """set cross correction positive length

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def apply_global_scale(element_id_list: List[int], scale: float, origin: point_3d) -> None:
    """apply global scale

    Parameters:
        element_id_list: element_id_list
        scale: scale
        origin: origin

    Returns:
        None
    """


def auto_regenerate_axes(element_id_list: List[int]) -> None:
    """auto regenerate axes

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def rotate_length_axis_90(element_id_list: List[int]) -> None:
    """rotate length axis 90

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def rotate_length_axis_180(element_id_list: List[int]) -> None:
    """rotate length axis 180

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def invert_model(element_id_list: List[int]) -> None:
    """invert model

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_width_real(elements: List[int], width: float) -> None:
    """set width real

    Parameters:
        elements: elements
        width: width

    Returns:
        None
    """


def set_height_real(elements: List[int], height: float) -> None:
    """set height real

    Parameters:
        elements: elements
        height: height

    Returns:
        None
    """


def set_length_real(elements: List[int], length: float) -> None:
    """set length real

    Parameters:
        elements: elements
        length: length

    Returns:
        None
    """


def rotate_height_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """rotate height axis 2 points

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
    """set drilling tolerance

    Parameters:
        elements: elements
        tolerance: tolerance

    Returns:
        None
    """


def auto_regenerate_axes_silently(element_id_list: List[int]) -> None:
    """auto regenerate axes silently

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def rotate_length_axis_2_points(elements: List[int], point1: point_3d, point2: point_3d) -> None:
    """rotate length axis 2 points

    Parameters:
        elements: elements
        point1: point1
        point2: point2

    Returns:
        None
    """


def get_width(element_id: int) -> float:
    """get width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_height(element_id: int) -> float:
    """get height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_length(element_id: int) -> float:
    """get length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_p1(element_id: int) -> point_3d:
    """get p1

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_p2(element_id: int) -> point_3d:
    """get p2

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_p3(element_id: int) -> point_3d:
    """get p3

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_start_height_cut_angle(element_id: int) -> float:
    """get start height cut angle

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_start_width_cut_angle(element_id: int) -> float:
    """get start width cut angle

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_end_height_cut_angle(element_id: int) -> float:
    """get end height cut angle

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_end_width_cut_angle(element_id: int) -> float:
    """get end width cut angle

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_over_width(element_id: int) -> float:
    """get over width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_over_height(element_id: int) -> float:
    """get over height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_over_length(element_id: int) -> float:
    """get over length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_rounding_width(element_id: int) -> float:
    """get rounding width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_rounding_height(element_id: int) -> float:
    """get rounding height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_rounding_length(element_id: int) -> float:
    """get rounding length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_negative_width(element_id: int) -> float:
    """get cross correction negative width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_positive_width(element_id: int) -> float:
    """get cross correction positive width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_negative_height(element_id: int) -> float:
    """get cross correction negative height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_positive_height(element_id: int) -> float:
    """get cross correction positive height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_negative_length(element_id: int) -> float:
    """get cross correction negative length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_cross_correction_positive_length(element_id: int) -> float:
    """get cross correction positive length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_weight(element_id: int) -> float:
    """get weight

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_list_weight(element_id: int) -> float:
    """get list weight

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_volume(element_id: int) -> float:
    """get volume

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_list_volume(element_id: int) -> float:
    """get list volume

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_xl(element_id: int) -> point_3d:
    """get xl

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_yl(element_id: int) -> point_3d:
    """get yl

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_zl(element_id: int) -> point_3d:
    """get zl

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_center_of_gravity(element_id: int) -> point_3d:
    """get center of gravity

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """


def get_reference_side(element_id: int) -> int:
    """get reference side

    Parameters:
        element_id: element_id

    Returns:
        int
    """


def get_element_vertices(element_id: int) -> List[point_3d]:
    """get element vertices

    Parameters:
        element_id: element_id

    Returns:
        List[point_3d]
    """


def get_element_facets(element_id: int) -> facet_list:
    """get element facets

    Parameters:
        element_id: element_id

    Returns:
        facet_list
    """


def get_list_width(element_id: int) -> float:
    """get list width

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_list_height(element_id: int) -> float:
    """get list height

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_list_length(element_id: int) -> float:
    """get list length

    Parameters:
        element_id: element_id

    Returns:
        float
    """


def get_minimum_distance_between_elements(first_id: int, second_id: int) -> float:
    """get minimum distance between elements

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        float
    """


def get_total_area_of_all_faces(element: int) -> float:
    """get total area of all faces

    Parameters:
        element: element

    Returns:
        float
    """


def get_area_of_front_face(element: int) -> float:
    """get area of front face

    Parameters:
        element: element

    Returns:
        float
    """


def get_door_surface(elements: List[int]) -> float:
    """get door surface

    Parameters:
        elements: elements

    Returns:
        float
    """


def get_window_surface(elements: List[int]) -> float:
    """get window surface

    Parameters:
        elements: elements

    Returns:
        float
    """


def get_local_x() -> point_3d:
    """get local x

    Returns:
        point_3d
    """


def get_local_z() -> point_3d:
    """get local z

    Returns:
        point_3d
    """


def get_local_y() -> point_3d:
    """get local y

    Returns:
        point_3d
    """


def get_drilling_tolerance(element: int) -> float:
    """get drilling tolerance

    Parameters:
        element: element

    Returns:
        float
    """


def get_element_reference_face_vertices(element_id: int) -> List[point_3d]:
    """get element reference face vertices

    Parameters:
        element_id: element_id

    Returns:
        List[point_3d]
    """


def get_element_reference_face_area(element_id: int) -> float:
    """get element reference face area

    Parameters:
        element_id: element_id

    Returns:
        float
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


def get_actual_physical_weight(element: int) -> float:
    """get actual physical weight

    Parameters:
        element: element

    Returns:
        float
    """


def get_actual_physical_volume(element_id: int) -> float:
    """Gets actual physical volume (includes negative geometry operations, such as end-types, drillings, connectors,
    openings, and MEP elements) (it might also take into account different drilling
    bodies and counterbores in a connector)


    Parameters:
        element_id: element_id

    Returns:
        float
    """


def are_facets_coplanar(first_facet: List[point_3d], second_facet: List[point_3d]) -> bool:
    """are facets coplanar

    Parameters:
        first_facet: first_facet
        second_facet: second_facet

    Returns:
        bool
    """


def get_round_machine_rough_part_negative_width(element_id: int) -> bool:
    """get round machine rough part negative width

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_negative_width(elements: List[int], value: bool) -> None:
    """set round machine rough part negative width

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_round_machine_rough_part_positive_width(element_id: int) -> bool:
    """get round machine rough part positive width

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_positive_width(elements: List[int], value: bool) -> None:
    """set round machine rough part positive width

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_round_machine_rough_part_negative_height(element_id: int) -> bool:
    """get round machine rough part negative height

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_negative_height(elements: List[int], value: bool) -> None:
    """set round machine rough part negative height

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_round_machine_rough_part_positive_height(element_id: int) -> bool:
    """get round machine rough part positive height

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_positive_height(elements: List[int], value: bool) -> None:
    """set round machine rough part positive height

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_round_machine_rough_part_negative_length(element_id: int) -> bool:
    """get round machine rough part negative length

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_negative_length(elements: List[int], value: bool) -> None:
    """set round machine rough part negative length

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_round_machine_rough_part_positive_length(element_id: int) -> bool:
    """get round machine rough part positive length

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def set_round_machine_rough_part_positive_length(elements: List[int], value: bool) -> None:
    """set round machine rough part positive length

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """


def get_standard_element_width_from_guid(standard_element_guid: str) -> float:
    """get standard element width from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """


def get_standard_element_height_from_guid(standard_element_guid: str) -> float:
    """get standard element height from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """


def get_standard_element_length_from_guid(standard_element_guid: str) -> float:
    """get standard element length from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """


def get_standard_element_width_from_name(standard_element_name: str) -> float:
    """get standard element width from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """


def get_standard_element_height_from_name(standard_element_name: str) -> float:
    """get standard element height from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """


def get_standard_element_length_from_name(standard_element_name: str) -> float:
    """get standard element length from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """
