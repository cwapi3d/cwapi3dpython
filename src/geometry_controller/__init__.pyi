from typing import List
from cadwork.api_types import ElementId, UnsignedInt
from cadwork.facet_list import facet_list
from cadwork.point_3d import point_3d


def rotate_height_axis_90(element_id_list: List[ElementId]) -> None:
    """Rotates the element height axis 90 degrees.

    Parameters:
        element_id_list: The element id list.
    """

def rotate_height_axis_180(element_id_list: List[ElementId]) -> None:
    """Rotates the element height axis 180 degrees.

    Parameters:
        element_id_list: The element id list.
    """

def set_over_width(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element overwidth.

    Parameters:
        element_id_list: The element id list.
        value: The element overwidth.
    """

def set_over_height(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element overheight.

    Parameters:
        element_id_list: The element id list.
        value: The element overheight.
    """

def set_over_length(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element overlength.

    Parameters:
        element_id_list: The element id list.
        value: The element overlength.
    """

def set_rounding_width(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element rounding width.

    Parameters:
        element_id_list: The element id list.
        value: The element rounding width.
    """

def set_rounding_height(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element rounding height.

    Parameters:
        element_id_list: The element id list.
        value: The element rounding height.
    """

def set_rounding_length(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element rounding length.

    Parameters:
        element_id_list: The element id list.
        value: The element rounding length.
    """

def set_cross_correction_negative_width(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element negative width cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element negative width cross correction.
    """

def set_cross_correction_positive_width(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element positive width cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element positive width cross correction.
    """

def set_cross_correction_negative_height(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element negative height cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element negative height cross correction.
    """

def set_cross_correction_positive_height(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element positive height cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element positive height cross correction.
    """

def set_cross_correction_negative_length(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element negative length cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element negative length cross correction.
    """

def set_cross_correction_positive_length(element_id_list: List[ElementId], value: float) -> None:
    """Sets the element positive length cross correction.

    Parameters:
        element_id_list: The element id list.
        value: The element positive length cross correction.
    """

def apply_global_scale(element_id_list: List[ElementId], scale: float, origin: point_3d) -> None:
    """Applies a global scale to element.

    Parameters:
        element_id_list: The element id list.
        scale: The global scale.
        origin: The scaling origin.
    """

def auto_regenerate_axes(element_id_list: List[ElementId]) -> None:
    """Automatically regenerates axes on element.

    Parameters:
        element_id_list: The element id list.
    """

def rotate_length_axis_90(element_id_list: List[ElementId]) -> None:
    """Rotates element length axis 90 degrees.

    Parameters:
        element_id_list: The element id list.
    """

def rotate_length_axis_180(element_id_list: List[ElementId]) -> None:
    """Rotates element length axis 180 degrees.

    Parameters:
        element_id_list: The element id list.
    """

def invert_model(element_id_list: List[ElementId]) -> None:
    """Inverts element model.

    Parameters:
        element_id_list: The element id list.
    """

def set_width_real(element_id_list: List[ElementId], width: float) -> None:
    """Sets the element real width.

    Parameters:
        element_id_list: The element id list.
        width: The element real width.
    """

def set_height_real(element_id_list: List[ElementId], height: float) -> None:
    """Sets the element real height.

    Parameters:
        element_id_list: The element id list.
        height: The element real height.
    """

def set_length_real(element_id_list: List[ElementId], length: float) -> None:
    """Sets the element real length.

    Parameters:
        element_id_list: The element id list.
        length: The element real length.
    """

def rotate_height_axis_2_points(element_id_list: List[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element height axis via 2 points.

    Parameters:
        element_id_list: The element id list.
        point1: The first point.
        point2: The second point.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

def set_drilling_tolerance(element_id_list: List[ElementId], tolerance: float) -> None:
    """Sets the drilling tolerance of the axis.

    Parameters:
        element_id_list: The element id list.
        tolerance: The new drilling tolerance.
    """

def auto_regenerate_axes_silently(element_id_list: List[ElementId]) -> None:
    """Automatically regenerates axes on elements without any user interaction.

    Parameters:
        element_id_list: The list of element IDs for which the axes will be regenerated.
    """

def rotate_length_axis_2_points(element_id_list: List[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Rotates the element length axis via 2 points.

    Parameters:
        element_id_list: The element id list.
        point1: The first point.
        point2: The second point.
    """

def get_width(element_id: ElementId) -> float:
    """Gets the element width.

    Parameters:
        element_id: The element Id.

    Returns:
        The element width.
    """

def get_height(element_id: ElementId) -> float:
    """Gets the element height.

    Parameters:
        element_id: The element Id.

    Returns:
        The element height.
    """

def get_length(element_id: ElementId) -> float:
    """Gets the element length.

    Parameters:
        element_id: The element Id.

    Returns:
        The element length.
    """

def get_p1(element_id: ElementId) -> point_3d:
    """Gets the element P1.

    Parameters:
        element_id: The element Id.

    Returns:
        The element P1.
    """

def get_p2(element_id: ElementId) -> point_3d:
    """Gets the element P2.

    Parameters:
        element_id: The element Id.

    Returns:
        The element P2.
    """

def get_p3(element_id: ElementId) -> point_3d:
    """Gets the element P3.

    Parameters:
        element_id: The element Id.

    Returns:
        The element P3.
    """

def get_start_height_cut_angle(element_id: ElementId) -> float:
    """Gets the element start height cut angle.

    Parameters:
        element_id: The element Id.

    Returns:
        The element start height cut angle.
    """

def get_start_width_cut_angle(element_id: ElementId) -> float:
    """Gets the element start width cut angle.

    Parameters:
        element_id: The element Id.

    Returns:
        The element start width cut angle.
    """

def get_end_height_cut_angle(element_id: ElementId) -> float:
    """Gets the element end height cut angle.

    Parameters:
        element_id: The element Id.

    Returns:
        The element end height cut angle.
    """

def get_end_width_cut_angle(element_id: ElementId) -> float:
    """Gets the element end width cut angle.

    Parameters:
        element_id: The element Id.

    Returns:
        The element end width cut angle.
    """

def get_over_width(element_id: ElementId) -> float:
    """Gets the element overwidth.

    Parameters:
        element_id: The element Id.

    Returns:
        The element overwidth.
    """

def get_over_height(element_id: ElementId) -> float:
    """Gets the element overheight.

    Parameters:
        element_id: The element Id.

    Returns:
        The element overheight.
    """

def get_over_length(element_id: ElementId) -> float:
    """Gets the element overlength.

    Parameters:
        element_id: The element Id.

    Returns:
        The element overlength.
    """

def get_rounding_width(element_id: ElementId) -> float:
    """Gets the element rounding width.

    Parameters:
        element_id: The element Id.

    Returns:
        The element rounding width.
    """

def get_rounding_height(element_id: ElementId) -> float:
    """Gets the element rounding height.

    Parameters:
        element_id: The element Id.

    Returns:
        The element rounding height.
    """

def get_rounding_length(element_id: ElementId) -> float:
    """Gets the element rounding length.

    Parameters:
        element_id: The element Id.

    Returns:
        The element rounding length.
    """

def get_cross_correction_negative_width(element_id: ElementId) -> float:
    """Gets the element negative width cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element negative width cross correction.
    """

def get_cross_correction_positive_width(element_id: ElementId) -> float:
    """Gets the element positive width cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element positive width cross correction.
    """

def get_cross_correction_negative_height(element_id: ElementId) -> float:
    """Gets the element negative height cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element negative height cross correction.
    """

def get_cross_correction_positive_height(element_id: ElementId) -> float:
    """Gets the element positive height cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element positive height cross correction.
    """

def get_cross_correction_negative_length(element_id: ElementId) -> float:
    """Gets the element negative length cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element negative length cross correction.
    """

def get_cross_correction_positive_length(element_id: ElementId) -> float:
    """Gets the element positive length cross correction.

    Parameters:
        element_id: The element Id.

    Returns:
        The element positive length cross correction.
    """

def get_weight(element_id: ElementId) -> float:
    """Gets the element real weight.

    Parameters:
        element_id: The element Id.

    Returns:
        The element real weight.
    """

def get_list_weight(element_id: ElementId) -> float:
    """Gets the element list weight.

    Parameters:
        element_id: The element Id.

    Returns:
        The element list weight.
    """

def get_volume(element_id: ElementId) -> float:
    """Gets the element rough volume (does not include negative geometry operations, such as end-types, drillings, connectors, openings, and MEP elements).

    Parameters:
        element_id: The element Id.

    Returns:
        The element rough volume.
    """

def get_list_volume(element_id: ElementId) -> float:
    """Gets the element list volume.

    Parameters:
        element_id: The element Id.

    Returns:
        The element list volume.
    """

def get_xl(element_id: ElementId) -> point_3d:
    """Gets the element length axis direction (direction from P1 to P2).

    Parameters:
        element_id: The element Id.

    Returns:
        The element XL vector.
    """

def get_yl(element_id: ElementId) -> point_3d:
    """Gets the element width axis direction (ZL cross XL).

    Parameters:
        element_id: The element Id.

    Returns:
        The element YL vector.
    """

def get_zl(element_id: ElementId) -> point_3d:
    """Gets the element height/thickness axis direction (direction from P1 to P3).

    Parameters:
        element_id: The element Id.

    Returns:
        The element ZL vector.
    """

def get_center_of_gravity(element_id: ElementId) -> point_3d:
    """Gets the element center of gravity.

    Parameters:
        element_id: The element Id.

    Returns:
        The element center of gravity position.
    """

def get_reference_side(element_id: ElementId) -> int:
    """Gets the element reference side.

    Parameters:
        element_id: The element Id.

    Returns:
        The element reference side.
    """

def get_element_vertices(element_id: ElementId) -> List[point_3d]:
    """Gets the element vertices.

    Parameters:
        element_id: The element Id.

    Returns:
        The element vertice list.
    """

def get_element_facets(element_id: ElementId) -> facet_list:
    """Gets the element facet list.

    Parameters:
        element_id: The element Id.

    Returns:
        The element facet list.
    """

def get_list_width(element_id: ElementId) -> float:
    """Gets the element list width.

    Parameters:
        element_id: The element Id.

    Returns:
        The element list width.
    """

def get_list_height(element_id: ElementId) -> float:
    """Gets the element list height.

    Parameters:
        element_id: The element Id.

    Returns:
        The element list height.
    """

def get_list_length(element_id: ElementId) -> float:
    """Gets the element list length.

    Parameters:
        element_id: The element Id.

    Returns:
        The element list length.
    """

def get_minimum_distance_between_elements(first_id: ElementId, second_id: ElementId) -> float:
    """Gets the minimum distance between 2 elements.

    Parameters:
        first_id: The first element id.
        second_id: The second element id.

    Returns:
        The minimum distance.
    """

def get_total_area_of_all_faces(element_id: ElementId) -> float:
    """Gets the total area of all faces for element.

    Parameters:
        element_id: The element Id.

    Returns:
        The element total faces area.
    """

def get_area_of_front_face(element_id: ElementId) -> float:
    """Gets the front face area for element.

    Parameters:
        element_id: The element Id.

    Returns:
        The element front face area.
    """

def get_door_surface(element_id_list: List[ElementId]) -> float:
    """Gets the element door surface.

    Parameters:
        element_id_list: The element id list.

    Returns:
        The element door surface.
    """

def get_window_surface(element_id_list: List[ElementId]) -> float:
    """Gets the element window surface.

    Parameters:
        element_id_list: The element id list.

    Returns:
        The element window surface.
    """

def get_local_x() -> point_3d:
    """Gets the rotated global coordinate direction (X').

    Returns:
        The local X vector.
    """

def get_local_z() -> point_3d:
    """Gets the rotated global coordinate direction (Z').

    Returns:
        The local Y vector.
    """

def get_local_y() -> point_3d:
    """Gets the rotated global coordinate direction (Y').

    Returns:
        The local Z vector.
    """

def get_drilling_tolerance(element_id: ElementId) -> float:
    """Gets the drilling tolerance of an axis.

    Parameters:
        element_id: The element Id.

    Returns:
        The drilling tolerance.
    """

def get_element_reference_face_vertices(element_id: ElementId) -> List[point_3d]:
    """Gets the vertices of the reference side.

    Parameters:
        element_id: The element Id.

    Returns:
        The vertexlist of all points.
    """

def get_element_reference_face_area(element_id: ElementId) -> float:
    """Gets the area of the reference side.

    Parameters:
        element_id: The element Id.

    Returns:
        The area(size) of reference face.
    """

def get_center_of_gravity_for_list(element_id_list: List[ElementId]) -> point_3d:
    """Gets the center of gravity for a list of elements.

    Parameters:
        element_id_list: The list of element IDs.

    Returns:
        The center of gravity as a vector3D.
    """

def get_center_of_gravity_for_list_considering_materials(element_id_list: List[ElementId]) -> point_3d:
    """Gets the center of gravity for a list of elements, considering their materials.

    Parameters:
        element_id_list: The list of element IDs.

    Returns:
        The center of gravity as a vector3D.
    """

def get_element_facet_count(element_id: ElementId) -> UnsignedInt:
    """Gets the count of facets for a specific element.

    Parameters:
        element_id: The ID of the element.

    Returns:
        The count of facets.
    """

def get_weight_real(element_id: ElementId) -> float:
    """Gets the real weight of the element.

    Parameters:
        element_id: The ID of the element.

    Returns:
        The real weight of the element.
    """

def get_actual_physical_weight(element_id: ElementId) -> float:
    """Gets the actual physical weight.

    Parameters:
        element_id: The element id.

    Returns:
        The actual physical weight.
    """

def get_actual_physical_volume(element_id: ElementId) -> float:
    """Gets actual physical volume (includes negative geometry operations, such as end-types, drillings, connectors, openings, and MEP elements; it might also take into account different drilling bodies and counterbores in a connector).

    Parameters:
        element_id: The element id.

    Returns:
        The actual physical volume.
    """

def are_facets_coplanar(first_facet: List[point_3d], second_facet: List[point_3d]) -> bool:
    """Tests if facets are coplanar.

    Parameters:
        first_facet: The first facet.
        second_facet: The second facet.

    Returns:
        True if facets are coplanar, false otherwise.
    """

def get_round_machine_rough_part_negative_width(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartNegativeWidth.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartNegativeWidth value.
    """

def set_round_machine_rough_part_negative_width(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartNegativeWidth.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartNegativeWidth value.
    """

def get_round_machine_rough_part_positive_width(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartPositiveWidth.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartPositiveWidth value.
    """

def set_round_machine_rough_part_positive_width(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartPositiveWidth.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartPositiveWidth value.
    """

def get_round_machine_rough_part_negative_height(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartNegativeHeight.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartNegativeHeight value.
    """

def set_round_machine_rough_part_negative_height(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartNegativeHeight.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartNegativeHeight value.
    """

def get_round_machine_rough_part_positive_height(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartPositiveHeight.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartPositiveHeight value.
    """

def set_round_machine_rough_part_positive_height(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartPositiveHeight.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartPositiveHeight options.
    """

def get_round_machine_rough_part_negative_length(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartNegativeLength.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartNegativeLength value.
    """

def set_round_machine_rough_part_negative_length(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartNegativeLength.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartNegativeLength value.
    """

def get_round_machine_rough_part_positive_length(element_id: ElementId) -> bool:
    """Gets the value of option RoundMachineRoughPartPositiveLength.

    Parameters:
        element_id: The element id.

    Returns:
        The option RoundMachineRoughPartPositiveLength value.
    """

def set_round_machine_rough_part_positive_length(element_id_list: List[ElementId], value: bool) -> None:
    """Sets the value of option RoundMachineRoughPartPositiveLength.

    Parameters:
        element_id_list: The element id list.
        value: The new option RoundMachineRoughPartPositiveLength value.
    """

def get_standard_element_width_from_guid(standard_element_guid: str) -> float:
    """Gets the standard element width from guid.

    Parameters:
        standard_element_guid: The standard element guid.

    Returns:
        The standard element width.
    """

def get_standard_element_height_from_guid(standard_element_guid: str) -> float:
    """Gets the standard element height from guid.

    Parameters:
        standard_element_guid: The standard element guid.

    Returns:
        The standard element height.
    """

def get_standard_element_length_from_guid(standard_element_guid: str) -> float:
    """Gets the standard element length from guid.

    Parameters:
        standard_element_guid: The standard element guid.

    Returns:
        The standard element length.
    """

def get_standard_element_width_from_name(standard_element_name: str) -> float:
    """Gets the standard element width from name.

    Parameters:
        standard_element_name: The standard element name.

    Returns:
        The standard element width.
    """

def get_standard_element_height_from_name(standard_element_name: str) -> float:
    """Gets the standard element height from name.

    Parameters:
        standard_element_name: The standard element name.

    Returns:
        The standard element height.
    """

def get_standard_element_length_from_name(standard_element_name: str) -> float:
    """Gets the standard element length from name.

    Parameters:
        standard_element_name: The standard element name.

    Returns:
        The standard element length.
    """
