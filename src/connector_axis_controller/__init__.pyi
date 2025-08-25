from typing import List
from cadwork.point_3d import point_3d
from cadwork.api_types import *
from cadwork.vba_catalog_item_type import vba_catalog_item_type

def create_standard_connector(axis_name: str, point1: point_3d, point2: point_3d) -> ElementId:
    """Creates a standard connector axis between two points.

    Parameters:
        axis_name: Name of the standard connector axis.
        point1: The first point defining the connector axis.
        point2: The second point defining the connector axis.

    Returns:
        The element id of the created standard connector axis.
    """


def set_bolt_length(axis_id: ElementId, length: float) -> None:
    """Sets the Bolt Length.

    Parameters:
        axis_id: The id of the axis.
        length: The bolt length.
    """


def set_bolt_length_automatic(axis_id: ElementId, length_automatic: bool) -> None:
    """Sets the Bolt Length Automatic.

    Parameters:
        axis_id: The id of the axis.
        length_automatic: True if the bolt length should be automatic, false otherwise.
    """


def set_diameter(axis_id: ElementId, diameter: float) -> None:
    """Sets the Drilling Diameter for all Sections.

    Parameters:
        axis_id: The id of the axis.
        diameter: The drilling diameter to set for all sections.
    """


def set_section_diameter(axis_id: ElementId, section_index: UnsignedInt, diameter: float) -> None:
    """Sets the Drilling Diameter for a specific Sections.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
        diameter: The drilling diameter to set for the specific section.
    """


def check_axis(axis_id: ElementId) -> bool:
    """Returns if the axis is valid.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        True if the axis is valid, false otherwise.
    """


def clear_errors() -> None:
    """Clear all errors.
    """


def update_axis_cutting_ability(axis_id_list: List[ElementId]) -> None:
    """Updates the Connection Config (CuttingAbility) of Axis/VBAs.

    Parameters:
        axis_id_list: The axis id list.
    """


def set_bolt_item(axis_id: ElementId, item_guid: str) -> None:
    """Sets the Bolt Item.

    Parameters:
        axis_id: The id of the axis.
        item_guid: The bolt item guid to set.
    """


def create_blank_connector(diameter: float, start_point: point_3d, end_point: point_3d) -> ElementId:
    """Creates a blank connector between two points.

    Parameters:
        diameter: The diameter of the connector.
        start_point: The start point of the connector.
        end_point: The end point of the connector.

    Returns:
        The element id of the created blank connector.
    """


def import_from_file(file_path: str) -> None:
    """Import from file.

    Parameters:
        file_path: The path to the file to import.
    """


def start_configuration_dialog() -> None:
    """Starts the ConnectorAxis configuration dialog.
    """


def get_item_guid_by_name(name: str, item_type: vba_catalog_item_type) -> str:
    """Get item guid by name.

    Parameters:
        name: The name of the item.
        item_type: The type of the item.

    Returns:
        The guid of the item.
    """


def get_bolt_length(axis_id: ElementId) -> float:
    """Gets the Bolt Length.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The bolt length.
    """


def get_bolt_over_length(axis_id: ElementId) -> float:
    """Gets the Bolt OverLength.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The bolt over length.
    """


def set_bolt_over_length(axis_id: ElementId, over_length: float) -> None:
    """Sets the Bolt OverLength.

    Parameters:
        axis_id: The id of the axis.
        over_length: The bolt over length.
    """


def get_bolt_length_automatic(axis_id: ElementId) -> bool:
    """Returns if Bolt Length Automatic is set.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        True if the bolt length is automatic, false otherwise.
    """


def get_bolt_item_guid(axis_id: ElementId) -> str:
    """Gets the Guid of the Bolt Item.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The guid of the bolt item.
    """


def get_section_diameter(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Gets the Drilling Diameter of a specific Sections.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The drilling diameter of the specified section.
    """


def get_axis_items_guids(axis_id: ElementId) -> List[str]:
    """Returns a list of GUIDs of all axis items.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The list of GUIDs of all axis items.
    """


def get_axis_item_name(guid: str) -> str:
    """Returns the name of an axis item.

    Parameters:
        guid: The guid of the axis item.

    Returns:
        The name of the axis item.
    """


def get_axis_item_material(guid: str) -> str:
    """Returns the material of an axis item.

    Parameters:
        guid: The guid of the axis item.

    Returns:
        The material of the axis item.
    """


def get_axis_item_norm(guid: str) -> str:
    """Returns the norm of an axis item.

    Parameters:
        guid: The guid of the axis item.

    Returns:
        The norm of the axis item.
    """


def get_axis_item_strength_category(guid: str) -> str:
    """Returns the strength category of an axis item.

    Parameters:
        guid: The guid of the axis item.

    Returns:
        The strength category of the axis item.
    """


def get_axis_item_user_field(guid: str, user_item_number: int) -> str:
    """Returns an userfield value of an axis item.

    Parameters:
        guid: The guid of the axis item.
        user_item_number: The user item number.

    Returns:
        The user field value.
    """


def get_axis_item_order_number(guid: str) -> str:
    """Returns the strength category of an axis item.

    Parameters:
        guid: The guid of the axis item.

    Returns:
        The strength category of the axis item.
    """


def get_bolt_order_number(axis_id: ElementId) -> str:
    """Returns the ordernumber of a bolt item.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The order number of the bolt item.
    """


def get_section_count(axis_id: ElementId) -> int:
    """Returns the number of sections.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The number of sections of the axis.
    """


def get_section_material_name(axis_id: ElementId, section_index: UnsignedInt) -> str:
    """Returns material of a section contact element.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The material of the section contact element.
    """


def get_section_contact_element(axis_id: float, section_index: UnsignedInt) -> ElementId:
    """Gets the section contact element.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The element id of the section contact element.
    """


def get_bolt_diameter(axis_id: ElementId) -> float:
    """Gets the bolt diameter.

    Parameters:
        axis_id: The id of the axis.

    Returns:
        The bolt diameter.
    """

def get_standard_connector_list() -> List[str]:
    """Returns a list of all standard connectors.

    Returns:
        The list of standard connector names.
    """


def get_counterbore_diameter_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Gets the counterbore diameter for the start side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
        diameter: [UNUSED PARAMETER]
        depth: [UNUSED PARAMETER]
        is_conical: [UNUSED PARAMETER]

    Returns:
        The counterbore diameter for the start side.
    """


def get_counterbore_diameter_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Gets the counterbore diameter for the end side of a section.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section.

    Returns:
        The counterbore diameter for the end side.
    """


def get_counterbore_depth_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Gets the counterbore depth for the start side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section.

    Returns:
        The counterbore depth for the start side.
    """


def get_counterbore_depth_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Gets the counterbore depth for the end side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section.

    Returns:
        The counterbore depth for the end side.
    """

def get_counterbore_is_conical_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Get if counterbore is conical for start side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section

    Returns:
        True if the counterbore is conical for the start side, false otherwise.
    """


def get_counterbore_is_conical_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Get if counterbore is conical for end side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section.

    Returns:
        True if the counterbore is conical for the end side, false otherwise.
        """


def set_counterbore_for_start_side(axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float,
                                   is_conical: bool) -> None:
    """Sets the counterbore for the start side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
        diameter: The diameter of the counterbore.
        depth: The depth of the counterbore.
        is_conical: True if the counterbore is conical, false otherwise.
    """


def set_counterbore_for_end_side(axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float,
                                 is_conical: bool) -> None:
    """Sets the counterbore for the end side.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
        diameter: The diameter of the counterbore.
        depth: The depth of the counterbore.
        is_conical: True if the counterbore is conical, false otherwise.
    """


def get_intersection_count(intersection_index: UnsignedInt) -> int:
    """Get the intersection count.

    Parameters:
        intersection_index: The index of the intersection. (0-based index)

    Returns:
        The intersection count.
    """

def get_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt) -> List[str]:
    """Get item GUIDs at intersection.

    Parameters:
        axis_id: The id of the axis.
        intersection_index: The index of the intersection. (0-based index)

    Returns:
        The list of item GUIDs at the intersection.
    """


def set_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt, item_guids: List[str]) -> None:
    """Sets item GUIDs at intersection.

    Parameters:
        axis_id: The id of the axis.
        intersection_index: The index of the intersection. (0-based index)
        item_guids: The item GUIDs to set.
    """

def get_section_length(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get section length.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The length of the section.
    """


def get_section_oblong_drilling_is_enabled(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Get if the section oblong drilling is enabled.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        True if the section oblong drilling is enabled, false otherwise.
    """


def get_section_oblong_drilling_positive_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get section oblong drilling positive value.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The positive value of the section oblong drilling.
    """


def get_section_oblong_drilling_negative_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the section oblong drilling negative value

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The negative value of the section oblong drilling.
    """


def get_section_oblong_drilling_angle(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get section oblong drilling angle.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)

    Returns:
        The angle of the section oblong drilling.
    """


def set_section_oblong_drilling_is_disabled(axis_id: ElementId, section_index: UnsignedInt) -> None:
    """Disable the section oblong drilling.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
    """


def set_section_oblong_drilling_is_enabled(axis_id: ElementId, section_index: UnsignedInt, positive_value: float,
                                           negative_value: float, angle: float) -> None:
    """Enable the section oblong drilling with parameters.

    Parameters:
        axis_id: The id of the axis.
        section_index: The index of the section. (0-based index)
        positive_value: The positive value of the section oblong drilling.
        negative_value: The negative value of the section oblong drilling.
        angle: The angle of the section oblong drilling.
    """
