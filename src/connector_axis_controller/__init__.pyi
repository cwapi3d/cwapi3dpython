from typing import List
from cadwork.point_3d import point_3d


def get_last_error(error_code: int) -> str:
    """get last error

    Parameters:
        error_code: error_code

    Returns:
        str
    """


def create_standard_connector(axis_name: str, point1: point_3d, point2: point_3d) -> int:
    """Creates a standard connector axis between two points.

    Parameters:
        axis_name: axis_name
        point1: point1
        point2: point2

    Returns:
        int
    """


def set_bolt_length(axis_id: int, length: float) -> None:
    """Sets the Bolt Length

    Parameters:
        axis_id: axis_id
        length: length

    Returns:
        None
    """


def set_bolt_length_automatic(axis_id: int, length_automatic: bool) -> None:
    """Sets the Bolt Length Automatic

    Parameters:
        axis_id: axis_id
        length_automatic: length_automatic

    Returns:
        None
    """


def set_diameter(axis_id: int, diameter: float) -> None:
    """Sets the Drilling Diameter for all Sections

    Parameters:
        axis_id: axis_id
        diameter: diameter

    Returns:
        None
    """


def set_section_diameter(axis_id: int, section_nr: int, diameter: float) -> None:
    """Sets the Drilling Diameter for a specific Sections

    Parameters:
        axis_id: axis_id
        section_nr: section_nr
        diameter: diameter

    Returns:
        None
    """


def check_axis(axis_id: int) -> bool:
    """Returns if the axis is valid.

    Parameters:
        axis_id: axis_id

    Returns:
        bool
    """


def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """


def update_axis_cutting_ability(axis_i_ds: List[int]) -> None:
    """updates the Connection Config (CuttingAbility) of Axis/VBAs

    Parameters:
        axis_i_ds: axis_i_ds

    Returns:
        None
    """


def set_bolt_item(axis_id: int, item_guid: str) -> None:
    """Sets the Bolt Item

    Parameters:
        axis_id: axis_id
        item_guid: item_guid

    Returns:
        None
    """


def create_blank_connector(diameter: float, start_point: point_3d, end_point: point_3d) -> int:
    """create blank connector

    Parameters:
        diameter: diameter
        start_point: start_point
        end_point: end_point

    Returns:
        int
    """


def import_from_file(file_path: str) -> None:
    """import from file

    Parameters:
        file_path: file_path

    Returns:
        None
    """


def start_configuration_dialog() -> None:
    """Starts the ConnectorAxis configuration dialog.

    Returns:
        None
    """


def get_item_guid_by_name(name: str, item_type: int) -> str:
    """get item guid by name

    Parameters:
        name: name
        item_type: item_type

    Returns:
        str
    """


def get_bolt_length(axis_id: int) -> float:
    """Gets the Bolt Length

    Parameters:
        axis_id: axis_id

    Returns:
        float
    """


def get_bolt_over_length(axis_id: int) -> float:
    """Gets the Bolt OverLength

    Parameters:
        axis_id: axis_id

    Returns:
        float
    """


def set_bolt_over_length(axis_id: int, over_length: float) -> None:
    """Sets the Bolt OverLength

    Parameters:
        axis_id: axis_id
        over_length: over_length

    Returns:
        None
    """


def get_bolt_length_automatic(axis_id: int) -> bool:
    """Returns if Bolt Length Automatic is set

    Parameters:
        axis_id: axis_id

    Returns:
        bool
    """


def get_bolt_item_guid(axis_id: int) -> str:
    """Gets the Guid of the Bolt Item

    Parameters:
        axis_id: axis_id

    Returns:
        str
    """


def get_section_diameter(axis_id: int, section_nr: int) -> float:
    """Gets the Drilling Diameter of a specific Sections

    Parameters:
        axis_id: axis_id
        section_nr: section_nr

    Returns:
        float
    """


def get_axis_items_guids(axis_id: int) -> List[str]:
    """Returns a list of GUIDs of all axis items.

    Parameters:
        axis_id: axis_id

    Returns:
        List[str]
    """


def get_axis_item_name(guid: str) -> str:
    """Returns the name of an axis item.

    Parameters:
        guid: guid

    Returns:
        str
    """


def get_axis_item_material(guid: str) -> str:
    """Returns the material of an axis item.

    Parameters:
        guid: guid

    Returns:
        str
    """


def get_axis_item_norm(guid: str) -> str:
    """Returns the norm of an axis item.

    Parameters:
        guid: guid

    Returns:
        str
    """


def get_axis_item_strength_category(guid: str) -> str:
    """Returns the strength category of an axis item.

    Parameters:
        guid: guid

    Returns:
        str
    """


def get_axis_item_user_field(guid: str, user_item_nr: int) -> str:
    """Returns an userfield value of an axis item.

    Parameters:
        guid: guid
        user_item_nr: user_item_nr

    Returns:
        str
    """


def get_axis_item_order_number(guid: str) -> str:
    """Returns the strength category of an axis item.

    Parameters:
        guid: guid

    Returns:
        str
    """


def get_bolt_order_number(axis_id: int) -> str:
    """Returns the ordernumber of a bolt item.

    Parameters:
        axis_id: axis_id

    Returns:
        str
    """


def get_section_count(axis_id: int) -> int:
    """Returns the number of sections.

    Parameters:
        axis_id: axis_id

    Returns:
        int
    """


def get_section_material_name(axis_id: int, section_nr: int) -> str:
    """Returns material of a section contact element.

    Parameters:
        axis_id: axis_id
        section_nr: section_nr

    Returns:
        str
    """


def get_section_contact_element(axis_id: float, section_nr: int) -> int:
    """get section contact element

    Parameters:
        axis_id: axis_id
        section_nr: section_nr

    Returns:
        int
    """


def get_bolt_diameter(axis_id: int) -> float:
    """get bolt diameter

    Parameters:
        axis_id: axis_id

    Returns:
        float
    """


def get_standard_connector_list() -> List[str]:
    """Returns a list of all standard connectors.

    Returns:
        List[str]
    """


def get_counterbore_diameter_for_start_side(axis_id: int, section_index: int, diameter: float, depth: float,
                                            is_conical: bool) -> float:
    """get counterbore diameter for start side

    Parameters:
        axis_id: axis_id
        section_index: section_index
        diameter: diameter
        depth: depth
        is_conical: is_conical

    Returns:
        float
    """


def get_counterbore_diameter_for_end_side(axis_id: int, section_index: int) -> float:
    """Gets the counterbore diameter for the end side of a section.

    Parameters:
        axis_id: The ID of the axis.
        section_index: The index of the section.

    Returns:
        float: The counterbore diameter for the end side.
    """


def get_counterbore_depth_for_start_side(axis_id: int, section_index: int) -> float:
    """get counterbore depth for start side

    Parameters:
        axis_id: The ID of the axis.
        section_index: The index of the section.

    Returns:
        float
    """


def get_counterbore_depth_for_end_side(axis_id: int, section_index: int) -> float:
    """get counterbore depth for end side

    Parameters:
        axis_id: The ID of the axis.
        section_index: The index of the section

    Returns:
        float
    """


def get_counterbore_is_conical_for_start_side(axis_id: int, section_index: int) -> bool:
    """get counterbore is conical for start side

    Parameters:
        axis_id: The ID of the axis.
        section_index: The index of the section

    Returns:
        bool
    """


def get_counterbore_is_conical_for_end_side(axis_id: int, section_index: int) -> bool:
    """get counterbore is conical for end side

    Parameters:
        axis_id: The ID of the axis.
        section_index: The index of the section

    Returns:
        bool
    """


def set_counterbore_for_start_side(axis_id: int, section_index: int, diameter: float, depth: float,
                                   is_conical: bool) -> None:
    """set counterbore for start side

    Parameters:
        axis_id: axis_id
        section_index: section_index
        diameter: diameter
        depth: depth
        is_conical: is_conical

    Returns:
        None
    """


def set_counterbore_for_end_side(axis_id: int, section_index: int, diameter: float, depth: float,
                                 is_conical: bool) -> None:
    """set counterbore for end side

    Parameters:
        axis_id: axis_id
        section_index: section_index
        diameter: diameter
        depth: depth
        is_conical: is_conical

    Returns:
        None
    """


def get_intersection_count(intersection_index: int) -> int:
    """get intersection count

    Parameters:
        intersection_index: intersection_index

    Returns:
        int
    """


def get_item_guids_at_intersection(axis_id: int, intersection_index: int) -> List[str]:
    """get item guids at intersection

    Parameters:
        axis_id: axis_id
        intersection_index: intersection_index

    Returns:
        List[str]
    """


def set_item_guids_at_intersection(axis_id: int, intersection_index: int, item_guids: List[str]) -> None:
    """set item guids at intersection

    Parameters:
        axis_id: axis_id
        intersection_index: intersection_index
        item_guids: item_guids

    Returns:
        None
    """


def get_section_length(axis_id: int, section_index: int) -> float:
    """get section length

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        float
    """


def get_section_oblong_drilling_is_enabled(axis_id: int, section_index: int) -> bool:
    """get section oblong drilling is enabled

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        bool
    """


def get_section_oblong_drilling_positive_value(axis_id: int, section_index: int) -> float:
    """get section oblong drilling positive value

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        float
    """


def get_section_oblong_drilling_negative_value(axis_id: int, section_index: int) -> float:
    """get section oblong drilling negative value

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        float
    """


def get_section_oblong_drilling_angle(axis_id: int, section_index: int) -> float:
    """get section oblong drilling angle

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        float
    """


def set_section_oblong_drilling_is_disabled(axis_id: int, section_index: int) -> None:
    """set section oblong drilling is disabled

    Parameters:
        axis_id: axis_id
        section_index: section_index

    Returns:
        None
    """


def set_section_oblong_drilling_is_enabled(axis_id: int, section_index: int, positive_value: float,
                                           negative_value: float, angle: float) -> None:
    """set section oblong drilling is enabled

    Parameters:
        axis_id: axis_id
        section_index: section_index
        positive_value: positive_value
        negative_value: negative_value
        angle: angle

    Returns:
        None
    """
