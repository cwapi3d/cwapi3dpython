"""Fastener and connector axes.

Domain of the linear assemblies that represent bolts, screws, dowels
and similar connectors: their creation, validation, the catalog items
attached to them (bolt, nut, washer, ...), per-item user fields, and
the configuration UI for connector axes. Distinct from connector
*nodes* and from drillings, which live in element_controller.
"""

from cadwork.point_3d import point_3d
from cadwork.connector_axis_item import connector_axis_item
from cadwork.api_types import *
from cadwork.vba_catalog_item_type import vba_catalog_item_type

def create_standard_connector(axis_name: str, point1: point_3d, point2: point_3d) -> ElementId:
    """Create a connector axis from a named standard connector between two points.

    The new axis starts at point1, runs towards point2 and has the length of their distance. It is
    added to the model, made visible and the display is refreshed if auto refresh is on. Returns 0
    if no standard connector with that name exists or creation fails.

    Parameters:
        axis_name: Name of the standard connector, as listed by get_standard_connector_list (looked
            up in the current cadwork language); the first match is used.
        point1: Start point of the axis in model units (mm).
        point2: End point of the axis in model units (mm); only gives the direction and length.

    Returns:
        Element ID of the created connector axis, or 0 on failure.
    """

def set_bolt_length(axis_id: ElementId, length: float) -> None:
    """Set the bolt length of a connector axis and switch off automatic bolt length.

    Silently does nothing if the element ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.
        length: Bolt length in model units (mm).
    """

def set_bolt_length_automatic(axis_id: ElementId, length_automatic: bool) -> None:
    """Switch automatic bolt length of a connector axis on or off.

    Does nothing if the element ID is invalid or the element is not a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.
        length_automatic: True to let cadwork determine the bolt length, False to use the manually
            set length.
    """

def set_diameter(axis_id: ElementId, diameter: float) -> None:
    """Set the drilling diameter of all sections of a connector axis.

    Silently does nothing if the element ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.
        diameter: Drilling diameter in model units (mm), applied as an absolute value to every
            section.
    """

def set_section_diameter(axis_id: ElementId, section_index: UnsignedInt, diameter: float) -> None:
    """Set the drilling diameter of one section of a connector axis.

    Silently does nothing if the element ID is invalid. An out-of-range section index changes
    nothing.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.
        diameter: Drilling diameter in model units (mm), as an absolute value.
    """

def check_axis(axis_id: ElementId) -> bool:
    """Check whether a connector axis has a valid cutting ability (connection config).

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        True if the element is a connector axis with valid cutting ability. False if it is invalid,
        not a connector axis, or the ID is invalid.
    """

def clear_errors() -> None:
    """Clear the stored connector axis error messages."""

def update_axis_cutting_ability(axis_id_list: list[ElementId]) -> None:
    """Re-evaluate the cutting ability (connection config) of connector axes.

    Invalid IDs and elements that are not connector axes are skipped. Axes that are still valid are
    only recreated when auto display refresh is on; axes whose cutting ability is invalid are handed
    to cadwork's cutting ability check.

    Parameters:
        axis_id_list: List of element IDs of connector axes.
    """

def set_bolt_item(axis_id: ElementId, item_guid: str) -> None:
    """Set the bolt catalog item of a connector axis.

    The item is looked up in the user catalog. Silently does nothing if the element ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.
        item_guid: GUID of a bolt item from the user catalog, e.g. from get_item_guid_by_name.
    """

def create_blank_connector(diameter: float, start_point: point_3d, end_point: point_3d) -> ElementId:
    """Create an empty connector axis with a given diameter between two points.

    The axis is added to the model, made visible and the display is refreshed if auto refresh is on.
    Returns 0 if creation fails or the result is out of range.

    Parameters:
        diameter: Drilling diameter in model units (mm).
        start_point: Start point of the axis in model units (mm).
        end_point: End point of the axis in model units (mm).

    Returns:
        Element ID of the created connector axis, or 0 on failure.
    """

def import_from_file(file_path: str) -> None:
    """Import standard connector definitions from a file.

    Entries whose name already exists are ignored, not overwritten.

    Parameters:
        file_path: Path of the file to import.
    """

def start_configuration_dialog() -> None:
    """Open the connector axis configuration dialog."""

def get_item_guid_by_name(name: str, item_type: vba_catalog_item_type) -> str:
    """Find a catalog item of a given type by name and return its GUID.

    Searches the user catalog; the name comparison ignores case and the first match is returned.

    Parameters:
        name: Name of the catalog item.
        item_type: Item type to search in, e.g. vba_catalog_item_type.nut.

    Returns:
        GUID of the first matching item, or an empty string if none matches.
    """

def get_bolt_length(axis_id: ElementId) -> float:
    """Get the bolt length of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        Bolt length in model units (mm); 0.0 if the element ID is invalid.
    """

def get_bolt_over_length(axis_id: ElementId) -> float:
    """Get the bolt over-length of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        Bolt over-length in model units (mm); 0.0 if the element ID is invalid.
    """

def set_bolt_over_length(axis_id: ElementId, over_length: float) -> None:
    """Set the bolt over-length of a connector axis.

    Silently does nothing if the element ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.
        over_length: Bolt over-length in model units (mm).
    """

def get_bolt_length_automatic(axis_id: ElementId) -> bool:
    """Check whether the bolt length of a connector axis is determined automatically.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        True if automatic bolt length is on; False if it is off or the element ID is invalid.
    """

def get_bolt_item_guid(axis_id: ElementId) -> str:
    """Get the GUID of the bolt catalog item of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        GUID of the bolt item; an empty string if the element ID is invalid.
    """

def get_section_diameter(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the drilling diameter of one section of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Drilling diameter in model units (mm); 0.0 if the element ID or section index is invalid.
    """

def get_axis_items_guids(axis_id: ElementId) -> list[str]:
    """Get the GUIDs of the catalog items attached to a connector axis.

    The bolt item is not included. Returns an empty list if the element ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        List of item GUIDs (nuts, washers, etc., without the bolt); empty list on failure.
    """

def get_axis_item_name(guid: str) -> str:
    """Get the name of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.

    Returns:
        Name of the item.
    """

def get_axis_item_material(guid: str) -> str:
    """Get the material of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.

    Returns:
        Material of the item.
    """

def get_axis_item_norm(guid: str) -> str:
    """Get the standard (norm) designation of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.

    Returns:
        Norm of the item.
    """

def get_axis_item_strength_category(guid: str) -> str:
    """Get the strength category of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.

    Returns:
        Strength category of the item.
    """

def get_axis_item_user_field(guid: str, user_item_number: int) -> str:
    """Get one of the five user fields of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.
        user_item_number: Number of the user field, 1 to 5.

    Returns:
        Value of the user field; empty string if the field is empty, the number is outside 1-5, or
        the item is not found.
    """

def get_axis_item_order_number(guid: str) -> str:
    """Get the order number of a catalog item attached to an axis.

    The item is read from the items stored in the current document.

    Parameters:
        guid: GUID of the item, e.g. from get_axis_items_guids or get_bolt_item_guid.

    Returns:
        Order number of the item.
    """

def get_bolt_order_number(axis_id: ElementId) -> str:
    """Get the order number of the bolt in its current length.

    Looks up the length entry of the bolt item that matches the axis' bolt length.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        Order number of the bolt; empty string if the element ID is invalid or no catalog length
        matches the bolt length.
    """

def get_section_count(axis_id: ElementId) -> int:
    """Get the number of sections of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        Number of sections; 0 if the element ID is invalid.
    """

def get_section_material_name(axis_id: ElementId, section_index: UnsignedInt) -> str:
    """Get the material name of the element in contact with a section of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Material name; empty string if the element ID or section index is invalid.
    """

def get_section_contact_element(axis_id: float, section_index: UnsignedInt) -> ElementId:
    """Get the element in contact with a section of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Element ID of the first element in that section; 0 if the axis ID or section index is
        invalid or the section has no element.
    """

def get_bolt_diameter(axis_id: ElementId) -> float:
    """Get the bolt diameter of a connector axis.

    Uses the inner diameter of the bolt item if one is set, otherwise the axis diameter.

    Parameters:
        axis_id: Element ID of the connector axis.

    Returns:
        Bolt diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_standard_connector_list() -> list[str]:
    """Get the names of all available standard connectors.

    Names are those of the current cadwork language and can be used with create_standard_connector.

    Returns:
        List of standard connector names.
    """

def get_counterbore_diameter_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore diameter at the start side of a section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Counterbore diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_diameter_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore diameter at the end side of a section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Counterbore diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_depth_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore depth at the start side of a section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Counterbore depth in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_depth_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore depth at the end side of a section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Counterbore depth in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_is_conical_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether the counterbore at the start side of a section is conical.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        True if conical; False if not or if the element ID is invalid.
    """

def get_counterbore_is_conical_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether the counterbore at the end side of a section is conical.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        True if conical; False if not or if the element ID is invalid.
    """

def set_counterbore_for_start_side(
    axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float, is_conical: bool
) -> None:
    """Set the counterbore at the start side of a section of a connector axis.

    Silently does nothing if the element ID is invalid or the section index is out of range.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.
        diameter: Counterbore diameter in model units (mm).
        depth: Counterbore depth in model units (mm).
        is_conical: True for a conical counterbore, False for a non-conical one.
    """

def set_counterbore_for_end_side(
    axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float, is_conical: bool
) -> None:
    """Set the counterbore at the end side of a section of a connector axis.

    Silently does nothing if the element ID is invalid or the section index is out of range.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.
        diameter: Counterbore diameter in model units (mm).
        depth: Counterbore depth in model units (mm).
        is_conical: True for a conical counterbore, False for a non-conical one.
    """

def get_intersection_count(intersection_index: UnsignedInt) -> int:
    """Get the number of intersection points of a connector axis.

    Note that the single argument is the element ID of the connector axis.

    Parameters:
        intersection_index: Element ID of the connector axis (despite its name, this is not an
            index).

    Returns:
        Number of intersection points; 0 if the element ID is invalid.
    """

def get_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt) -> list[str]:
    """Get the GUIDs of the catalog items at an intersection of a connector axis.

    Parameters:
        axis_id: Element ID of the connector axis.
        intersection_index: 0-based index of the intersection; see get_intersection_count.

    Returns:
        List of item GUIDs; empty list if the element ID or intersection index is invalid.
    """

def set_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt, item_guids: list[str]) -> None:
    """Replace the items at an intersection of a connector axis by items with the given GUIDs.

    Prefer set_items_at_intersection, which is the reliable way to set items and their positions.

    Parameters:
        axis_id: Element ID of the connector axis.
        intersection_index: 0-based index of the intersection; see get_intersection_count.
        item_guids: List of GUIDs of the items to set.
    """

def get_section_length(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the length of a section of a connector axis.

    An out-of-range section index is clamped to the nearest valid section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Section length in model units (mm); 0.0 if the element ID is invalid, 1.0 if the axis has no
        sections.
    """

def get_section_oblong_drilling_is_enabled(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether a section of a connector axis has an oblong (slotted) drilling.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        True if oblong drilling is enabled; False if not or if the element ID or section index is
        invalid.
    """

def get_section_oblong_drilling_positive_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the positive oblong drilling extension of a section of a connector axis.

    Only meaningful while oblong drilling is enabled for the section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Positive oblong value; 0.0 if oblong drilling is not enabled, or the element ID or section
        index is invalid.
    """

def get_section_oblong_drilling_negative_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the negative oblong drilling extension of a section of a connector axis.

    Only meaningful while oblong drilling is enabled for the section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Negative oblong value; 0.0 if oblong drilling is not enabled, or the element ID or section
        index is invalid.
    """

def get_section_oblong_drilling_angle(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the orientation angle of the oblong drilling of a section of a connector axis.

    Only meaningful while oblong drilling is enabled for the section.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.

    Returns:
        Oblong drilling angle; 0.0 if oblong drilling is not enabled, or the element ID or section
        index is invalid.
    """

def set_section_oblong_drilling_is_disabled(axis_id: ElementId, section_index: UnsignedInt) -> None:
    """Disable the oblong drilling of a section of a connector axis.

    Silently does nothing if the element ID is invalid or the section index is out of range.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.
    """

def set_section_oblong_drilling_is_enabled(
    axis_id: ElementId, section_index: UnsignedInt, positive_value: float, negative_value: float, angle: float
) -> None:
    """Enable the oblong drilling of a section of a connector axis with the given values.

    Silently does nothing if the element ID is invalid or the section index is out of range.

    Parameters:
        axis_id: Element ID of the connector axis.
        section_index: 0-based index of the section; see get_section_count.
        positive_value: Oblong extension in the positive direction.
        negative_value: Oblong extension in the negative direction.
        angle: Orientation angle of the oblong drilling.
    """

def set_items_at_intersection(
    axis_id: ElementId, intersection_index: UnsignedInt, items: list[connector_axis_item]
) -> None:
    """Replace the catalog items at an intersection of a connector axis.

    All existing items at the intersection are removed first. Each connector_axis_item is looked up
    by its GUID in the user catalog and placed at its position. Silently does nothing if the element
    ID is invalid.

    Parameters:
        axis_id: Element ID of the connector axis.
        intersection_index: 0-based index of the intersection; see get_intersection_count.
        items: Items to set, each a connector_axis_item with a GUID and a position.
    """

def get_connector_axis_guid_by_name(name: str) -> str:
    """Get the GUID of a standard connector by its name.

    The name is looked up in the current cadwork language; the first match is used.

    Parameters:
        name: Name of the standard connector, as listed by get_standard_connector_list.

    Returns:
        GUID of the standard connector, or an empty string if no connector has that name.
    """
