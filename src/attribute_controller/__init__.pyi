"""Non-geometric properties and classification of elements.

Covers everything that describes an element without changing its shape:
identification and labelling (name, group, comment, production data),
user-defined attributes and their lists, element-type classification
(beam, panel, auxiliary, wall, roof, floor, drilling, export-solid, ...),
and the configuration of how these attributes are displayed in the
different views of the application.
"""

from cadwork.api_types import *
from cadwork.attribute_display_settings import attribute_display_settings
from cadwork.element_grouping_type import element_grouping_type
from cadwork.element_type import element_type
from cadwork.extended_settings import extended_settings
from cadwork.layer_settings import layer_settings
from cadwork.node_symbol import node_symbol
from cadwork.process_type import process_type
from cadwork.prefab_layer_info import prefab_layer_info

def set_name(element_id_list: list[ElementId], name: str) -> None:
    """Set the name of the given elements.

    A name that is not yet in the document's name list is added to it. Assigning a name also applies
    the machine, cutting-set and IFC settings stored for that name to each element.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        name: The name to assign to every element.
    """

def set_group(element_id_list: list[ElementId], group: str) -> None:
    """Set the group of the given elements.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        group: The group text to assign to every element.
    """

def set_subgroup(element_id_list: list[ElementId], subgroup: str) -> None:
    """Set the subgroup of the given elements.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        subgroup: The subgroup text to assign to every element.
    """

def set_comment(element_id_list: list[ElementId], comment: str) -> None:
    """Set the comment of the given elements.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        comment: The comment text to assign to every element.
    """

def set_user_attribute(element_id_list: list[ElementId], number: UserAttributeId, user_attribute: str) -> None:
    """Set one user attribute of the given elements.

    Nothing is changed if number is greater than 999.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        number: User attribute number, 1 to 999.
        user_attribute: The text to store in that user attribute.
    """

def set_sku(element_id_list: list[ElementId], sku: str) -> None:
    """Set the SKU (article code) of the given elements.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        sku: The SKU text to assign to every element.
    """

def set_production_number(element_id_list: list[ElementId], production_number: UnsignedInt) -> None:
    """Set the production list number of the given elements.

    Elements that have no production number data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        production_number: The production list number to assign to every element.
    """

def set_part_number(element_id_list: list[ElementId], part_number: UnsignedInt) -> None:
    """Set the part list number of the given elements.

    Elements that have no part number data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        part_number: The part list number to assign to every element.
    """

def set_additional_data(element_id_list: list[ElementId], data_id: str, data_text: str) -> None:
    """Store a text under a data ID on the given elements.

    An existing entry with the same data ID on an element is overwritten. The data is written
    directly to the document database.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        data_id: Key identifying the data entry (acts as owner of the entry).
        data_text: The text to store.
    """

def delete_additional_data(element_id_list: list[ElementId], data_id: str) -> None:
    """Delete the data stored under a data ID from the given elements.

    Elements that have no entry for the data ID are left unchanged.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        data_id: Key of the data entry to delete.
    """

def set_user_attribute_name(number: UserAttributeId, user_attribute_name: str) -> None:
    """Set the display name (title) of a user attribute.

    This is a document-wide label, not a value on elements. Nothing is changed if number is greater
    than 999.

    Parameters:
        number: User attribute number, 1 to 999.
        user_attribute_name: The new title of the user attribute.
    """

def set_process_type_and_extended_settings_from_name(element_id_list: list[ElementId]) -> None:
    """Apply the process type and extended settings defined for each element's name.

    For each element, the settings stored for its current name (process type, extended settings,
    related machine and cutting-set settings, IFC type) are copied onto the element. Elements
    without a name are skipped. The change is not added to the undo history.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_name_process_type(name: str, process_type: process_type) -> None:
    """Set the process type stored for an element name in the name list.

    Only the name list entry is changed; existing elements keep their current process type until
    set_process_type_and_extended_settings_from_name is called. Nothing happens if the name is not
    in the list.

    Parameters:
        name: Exact name of an existing entry in the name list.
        process_type: The process type to store for that name.
    """

def set_name_extended_settings(name: str, extended_settings: extended_settings) -> None:
    """Set the extended settings stored for an element name in the name list.

    Only the name list entry is changed; existing elements keep their current settings until
    set_process_type_and_extended_settings_from_name is called. Nothing happens if the name is not
    in the list.

    Parameters:
        name: Exact name of an existing entry in the name list.
        extended_settings: The extended settings to store for that name; all flags are written.
    """

def set_output_type(element_id_list: list[ElementId], process_type: process_type) -> None:
    """Set the output (process) type of the given elements.

    Elements without production data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        process_type: The process type to assign to every element.
    """

def set_extended_settings(element_id_list: list[ElementId], extended_settings: extended_settings) -> None:
    """Write the extended settings to the given elements.

    All flags of extended_settings are written to every element, overwriting flags you did not
    touch; start from get_extended_settings. Not added to the undo history.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        extended_settings: The settings to write; take them from get_extended_settings and modify.
    """

def set_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed wall.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous floor, roof
    or wall classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_floor(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed floor.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous wall, roof
    or floor classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_opening(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as openings.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. If an element was a wall, floor or roof, its wall cuts and
    related wall data are removed and its output type is cleared.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_fastening_attribute(element_id_list: list[ElementId], value: str) -> None:
    """Set the fastening attribute of the given elements.

    The value is only written if the panel prefabrication analysis configuration can be loaded;
    otherwise the call has no effect.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        value: The fastening attribute text to assign to every element.
    """

def set_element_material(element_id_list: list[ElementId], material: MaterialId) -> None:
    """Set the material of the given elements.

    Elements that cannot carry a material (for example auxiliary objects, containers, export solids,
    dimensions, lines other than installations) are skipped, unless material is 0, which clears the
    material of any element.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        material: Material ID, or 0 to remove the material. The ID is not checked against the
            material list.
    """

def set_assembly_number(element_id_list: list[ElementId], assembly_number: str) -> None:
    """Set the assembly number of the given elements.

    Elements without production data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        assembly_number: The assembly number text to assign to every element.
    """

def set_list_quantity(element_id_list: list[ElementId], list_quantity: UnsignedInt) -> None:
    """Set the quantity used in lists for the given elements.

    Elements without production data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        list_quantity: The quantity to assign to every element.
    """

def set_layer_settings(element_id_list: list[ElementId], layer_settings: layer_settings) -> None:
    """Set the prefab-layer output behavior of one layer on the given elements.

    The layer number and output mode are taken from layer_settings. Without-output wins over
    with-dimensions, which wins over without-dimensions; attributes output is applied for both
    dimension modes. Nothing changes if no mode was set or the layer number is out of range. Not
    added to the undo history.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        layer_settings: Layer number (0 = the element's own layer, 1 to 14 = reference side, -1 to
            -14 = opposite side) plus the output mode and attributes flag.
    """

def set_ignore_in_vba_calculation(element_id_list: list[ElementId], ignore: bool) -> None:
    """Set whether the given elements are ignored in the VBA calculation.

    All IDs must refer to existing elements. Elements without production data are skipped.

    Parameters:
        element_id_list: List of element IDs; all must exist. An empty list does nothing.
        ignore: True to ignore the elements in the VBA calculation, False to include them.
    """

def clear_errors() -> None:
    """Clear the stored error messages of the attribute controller."""

def set_reference_wall_2dc(element_id_list: list[ElementId], _2dc_file_path: str) -> None:
    """Replace the wall definition of the given walls with one read from a 2dc file.

    Only wall elements in the list are changed; if there is none, nothing happens. Each wall also
    takes the name, color and material from the file's bounding wall rectangle, and the wall
    thickness is changed to that rectangle's width.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist or are not walls are skipped.
        _2dc_file_path: Path to the 2dc file that defines the wall.
    """

def get_user_attribute_count() -> UnsignedInt:
    """Return the number of user attributes in the document.

    Returns:
        Number of user attributes, 0 if the attribute data is unavailable.
    """

def set_standard_part(element_id_list: list[ElementId]) -> None:
    """Remove the wall, floor, roof or opening classification from the given elements.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. If an element was a wall, floor or roof, its wall cuts and
    related wall data are removed and its output type is cleared.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_solid_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood wall.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous
    classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_log_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as log wall.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous
    classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_solid_floor(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood floor.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous
    classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_roof(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed roof.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous
    classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def set_solid_roof(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood roof.

    Only beam-class elements (beams, panels and other elements with a beam-like cross-section) are
    changed; other elements are skipped. The output type is set to match, and a previous
    classification is replaced.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
    """

def get_node_symbol(element_id: ElementId) -> node_symbol:
    """Return the node symbol of an element.

    Parameters:
        element_id: ID of the element to query.

    Returns:
        The node symbol of the element, or -1 if the element does not exist or has no node symbol
        data.
    """

def set_node_symbol(element_id_list: list[ElementId], symbol: node_symbol) -> None:
    """Set the node symbol of the given elements.

    Elements without node data are skipped. The value is not range-checked.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        symbol: The node symbol to assign.
    """

def enable_attribute_display() -> None:
    """Turn on the display of element attributes in the view.

    Rebuilds the attribute labels of all construction elements, updates the toolbar and redraws the
    view.
    """

def disable_attribute_display() -> None:
    """Turn off the display of element attributes in the view.

    Rebuilds the attribute labels of all construction elements, updates the toolbar and redraws the
    view.
    """

def is_attribute_display_enabled() -> bool:
    """Check whether element attributes are displayed in the view.

    Returns:
        True if attribute display is on, False otherwise.
    """

def update_auto_attribute() -> None:
    """Recalculate the auto-filled attributes of all visible elements.

    Hidden elements are not updated. Both manually and automatically configured auto attributes are
    recalculated.
    """

def set_additional_guid(element_id_list: list[ElementId], data_id: str, guid: str) -> None:
    """Store a GUID under a data ID on the given elements.

    An existing GUID with the same data ID on an element is overwritten. The data is written
    directly to the document database.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        data_id: Key identifying the GUID entry (acts as owner of the entry).
        guid: The GUID as text.
    """

def add_item_to_group_list(item: str) -> None:
    """Add an entry to the document's list of group values.

    Only the list is changed; no element is modified.

    Parameters:
        item: The group text to add.
    """

def add_item_to_subgroup_list(item: str) -> None:
    """Add an entry to the document's list of subgroup values.

    Only the list is changed; no element is modified.

    Parameters:
        item: The subgroup text to add.
    """

def add_item_to_comment_list(item: str) -> None:
    """Add an entry to the document's list of comment values.

    Only the list is changed; no element is modified.

    Parameters:
        item: The comment text to add.
    """

def add_item_to_sku_list(item: str) -> None:
    """Add an entry to the document's list of SKU values.

    Only the list is changed; no element is modified.

    Parameters:
        item: The SKU text to add.
    """

def add_item_to_user_attribute_list(attribute_number: UserAttributeId, item: str) -> None:
    """Add an entry to the list of values of one user attribute.

    Only the list is changed; no element is modified.

    Parameters:
        attribute_number: User attribute number (1-based).
        item: The text to add.
    """

def set_container_number(element_id_list: list[ElementId], number: UnsignedInt) -> None:
    """Set the container number of the given elements.

    The number is stored in the element's production list number, so it replaces the production
    number. Elements without production data are skipped.

    Parameters:
        element_id_list: List of element IDs; IDs that do not exist are skipped. An empty list does
            nothing.
        number: The container number to assign.
    """

def get_name_list_items() -> list[str]:
    """Return all names in the document's name list.

    An empty first entry (the blank name) is left out.

    Returns:
        List of name strings; an empty list if there are none or the attribute data is unavailable.
    """

def add_item_to_name_list(item: str) -> None:
    """Add a name to the document's name list.

    The name is added with default element type and settings, no process type. No element is
    modified.

    Parameters:
        item: The name to add.
    """

def delete_item_from_comment_list(item: str) -> bool:
    """Delete an entry from the document's list of comment values.

    Fails if the entry does not exist or is still used as comment by at least one element. The
    reason is recorded in the controller's error messages (see clear_errors).

    Parameters:
        item: The comment text to delete.

    Returns:
        True if the entry was deleted, False if it was not found, is in use or the attribute data is
        unavailable.
    """

def delete_item_from_group_list(item: str) -> bool:
    """Delete an entry from the group list of the document.

    Fails if the entry does not exist or is still assigned to any element in the document; the
    failure is also written to the API log.

    Parameters:
        item: Exact text of the group list entry to delete.

    Returns:
        True if the entry was deleted, False if it was not found, is still in use or the attribute
        database is unavailable.
    """

def delete_item_from_sku_list(item: str) -> bool:
    """Delete an entry from the SKU list of the document.

    Fails if the entry does not exist or is still assigned to any element in the document; the
    failure is also written to the API log.

    Parameters:
        item: Exact text of the SKU list entry to delete.

    Returns:
        True if the entry was deleted, False if it was not found, is still in use or the attribute
        database is unavailable.
    """

def delete_item_from_subgroup_list(item: str) -> bool:
    """Delete an entry from the subgroup list of the document.

    Fails if the entry does not exist or is still assigned to any element in the document; the
    failure is also written to the API log.

    Parameters:
        item: Exact text of the subgroup list entry to delete.

    Returns:
        True if the entry was deleted, False if it was not found, is still in use or the attribute
        database is unavailable.
    """

def delete_item_from_user_attribute_list(attribute_number: UserAttributeId, item: str) -> bool:
    """Delete an entry from the list of one user attribute.

    Fails if the entry does not exist or is still assigned to any element in the document; the
    failure is also written to the API log.

    Parameters:
        attribute_number: Number of the user attribute whose list the entry is removed from.
        item: Exact text of the list entry to delete.

    Returns:
        True if the entry was deleted, False if it was not found, is still in use or the attribute
        database is unavailable.
    """

def set_attribute_display_settings_for_2d(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for normal 2D exports.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_2d_with_layout(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for 2D exports with layout frame.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_2d_without_layout(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for 2D exports without layout frame.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_3d(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for the 3D view.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_container(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for containers.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_export_solid(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid exports.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_framed_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for framed wall axes.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_framed_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for framed wall beams.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_framed_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for framed wall openings.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_framed_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for framed wall panels.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_log_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for log wall axes.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_log_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for log wall beams.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_log_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for log wall openings.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_log_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for log wall panels.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_machine(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for machine output.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_nesting_element(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for nesting elements.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_nesting_volume(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for nesting volumes.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_solid_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid wall axes.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_solid_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid wall beams.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_solid_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid wall openings.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_attribute_display_settings_for_solid_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid wall panels.

    Applies the position type (percentage or absolute) and both position values of the settings
    object, stores them as a global setting for this target and refreshes the display if automatic
    refresh is on.

    Parameters:
        settings: Settings object; its position type decides whether the percentage or the absolute
            value (mm) is used.
    """

def set_framed_floor(element_id_list: list[ElementId]) -> None:
    """Mark elements as framed floor.

    Sets the wall/floor/roof type of each element. Invalid element IDs are skipped; an empty list
    does nothing. Same function as set_floor.

    Parameters:
        element_id_list: List of element IDs to mark.
    """

def set_framed_roof(element_id_list: list[ElementId]) -> None:
    """Mark elements as framed roof.

    Sets the wall/floor/roof type of each element. Invalid element IDs are skipped; an empty list
    does nothing. Same function as set_roof.

    Parameters:
        element_id_list: List of element IDs to mark.
    """

def set_framed_wall(element_id_list: list[ElementId]) -> None:
    """Mark elements as framed wall.

    Sets the wall/floor/roof type of each element. Invalid element IDs are skipped; an empty list
    does nothing. Same function as set_wall.

    Parameters:
        element_id_list: List of element IDs to mark.
    """

def get_name_list_items_by_element_type(element_type: element_type) -> list[str]:
    """Get the entries of the element name list for an element type.

    Reads the name list of the document, filtered by element type.

    Parameters:
        element_type: Element type (for example beam or panel) to filter the names by.

    Returns:
        List of name strings; empty if there are none.
    """

def get_name(element_id: ElementId) -> str:
    """Get the name of an element.

    For imported exchange objects the name is taken from the imported product structure.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Name of the element. Empty string if the element ID is invalid.
    """

def get_group(element_id: ElementId) -> str:
    """Get the group of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Group text of the element. Empty string if the element ID is invalid.
    """

def get_subgroup(element_id: ElementId) -> str:
    """Get the subgroup of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Subgroup text of the element. Empty string if the element ID is invalid.
    """

def get_comment(element_id: ElementId) -> str:
    """Get the comment of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Comment text of the element. Empty string if the element ID is invalid.
    """

def get_user_attribute(element_id: ElementId, number: UserAttributeId) -> str:
    """Get the value of one user attribute of an element.

    Numbers above 999 return an empty string.

    Parameters:
        element_id: ID of the element to read.
        number: Number of the user attribute to read.

    Returns:
        Value of the user attribute. Empty string if the element ID is invalid, the number is above
        999 or the attribute is not set.
    """

def get_sku(element_id: ElementId) -> str:
    """Get the SKU (article code) of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        SKU text of the element. Empty string if the element ID is invalid.
    """

def get_production_number(element_id: ElementId) -> UnsignedInt:
    """Get the production list number of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Production list number of the element. 0 if the element ID is invalid or the element has
        none.
    """

def get_part_number(element_id: ElementId) -> UnsignedInt:
    """Get the part number (timber list number) of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Part number of the element. 0 if the element ID is invalid or the element has none.
    """

def get_additional_data(element_id: ElementId, data_id: str) -> str:
    """Get the additional data stored on an element under a key.

    Additional data is custom text stored per element with set_additional_data.

    Parameters:
        element_id: ID of the element to read.
        data_id: Key under which the data is stored.

    Returns:
        Stored text. Empty string if the element ID is invalid or nothing is stored under the key.
    """

def get_user_attribute_name(number: UserAttributeId) -> str:
    """Get the display name of a user attribute.

    The name is a document-wide title, not a value of an element.

    Parameters:
        number: Number of the user attribute.

    Returns:
        Name of the user attribute. Empty string if the number has no name.
    """

def get_wall_situation(element_id: ElementId) -> str:
    """Get the wall situation text of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Wall situation text. Empty string if the element ID is invalid.
    """

def get_element_material_name(element_id: ElementId) -> str:
    """Get the name of the material assigned to an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Material name. Empty string if the element ID is invalid.
    """

def get_prefab_layer(element_id: ElementId) -> str:
    """Get the prefab layer assignment of an element as text.

    Layer 0 is the framework layer, positive numbers are layers on the reference side and negative
    numbers layers on the opposite side.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        String of the form WithDimensions[2,1,0] WithoutDimensions[] ShowAttributes[], layer numbers
        sorted in descending order. Empty string if the element ID is invalid or the element has no
        layer data.
    """

def get_machine_calculation_set(element_id: ElementId) -> str:
    """Get the name of the machine calculation set of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Name of the machine calculation set. Empty string if the element ID is invalid.
    """

def get_cutting_set(element_id: ElementId) -> str:
    """Get the name of the cutting set of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Name of the cutting set. Empty string if the element ID is invalid.
    """

def get_name_process_type(name: str) -> process_type:
    """Get the process type stored for an element name.

    The name is looked up in the name list of the document, across all element types.

    Parameters:
        name: Exact name from the name list.

    Returns:
        Process type of the name. A default-constructed process type (value 0) if the name is not
        found.
    """

def get_name_extended_settings(name: str) -> extended_settings:
    """Get the extended settings stored for an element name.

    The name is looked up in the name list of the document, across all element types.

    Parameters:
        name: Exact name from the name list.

    Returns:
        Extended settings of the name. A default-constructed extended_settings (value 0) if the name
        is not found.
    """

def get_output_type(element_id: ElementId) -> process_type:
    """Get the output (process) type of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Process type of the element. A default-constructed process type (value 0) if the element ID
        is invalid.
    """

def get_extended_settings(element_id: ElementId) -> extended_settings:
    """Get the extended settings of an element.

    Parameters:
        element_id: ID of the element to read.

    Returns:
        Extended settings of the element. A default-constructed extended_settings (value 0) if the
        element ID is invalid.
    """

def get_element_type(element_id: ElementId) -> element_type:
    """Get the element type of an element.

    Returns an element_type object; use its is_*() methods to test the kind. An invalid ID gives an
    element_type for which is_none() is True.

    Parameters:
        element_id: Element ID.

    Returns:
        The element_type of the element.
    """

def get_fastening_attribute(element_id: ElementId) -> str:
    """Get the prefab fastening attribute text of an element.

    The value comes from the document attribute table. Returns an empty string if the element ID is
    invalid or no value is set.

    Parameters:
        element_id: Element ID.

    Returns:
        The fastening attribute text, or an empty string.
    """

def get_assembly_number(element_id: ElementId) -> str:
    """Get the assembly list number of an element.

    Parameters:
        element_id: Element ID.

    Returns:
        The assembly number as text, or an empty string if the element ID is invalid.
    """

def get_list_quantity(element_id: ElementId) -> UnsignedInt:
    """Get the list quantity of an element.

    Parameters:
        element_id: Element ID.

    Returns:
        The quantity used in lists, or 0 if the element ID is invalid.
    """

def get_ignore_in_vba_calculation(element_id: ElementId) -> bool:
    """Check whether an element is excluded from the connector (VBA) calculation.

    Pass a valid element ID; invalid IDs are not handled safely.

    Parameters:
        element_id: Element ID of an existing element.

    Returns:
        True if the element is ignored in the connector calculation, False otherwise.
    """

def get_standard_element_name(element_id: ElementId) -> str:
    """Get the standard element name assigned to an element.

    Returns an empty string if the element has no standard element assigned or the ID is invalid.

    Parameters:
        element_id: Element ID.

    Returns:
        The standard element name, or an empty string.
    """

def get_steel_shape_name(element_id: ElementId) -> str:
    """Get the steel shape (profile) name of an element.

    The name is returned in the current program language. Returns an empty string if the element has
    no steel shape assigned or the ID is invalid.

    Parameters:
        element_id: Element ID.

    Returns:
        The steel shape name, or an empty string.
    """

def is_beam(element_id: ElementId) -> bool:
    """Check whether an element belongs to the beam class.

    Beams, panels and other elements with a beam-like cross-section all count; use is_panel to tell
    panels apart.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if it is a beam-class element (beam, panel or other beam-like element), False otherwise
        (including an invalid element ID).
    """

def is_panel(element_id: ElementId) -> bool:
    """Check whether an element is a panel.

    True only for elements with a rectangular panel cross-section.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a panel, False otherwise (including an invalid element ID).
    """

def is_opening(element_id: ElementId) -> bool:
    """Check whether an element is an opening.

    True for elements marked as an opening.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is an opening, False otherwise (including an invalid element ID).
    """

def is_wall(element_id: ElementId) -> bool:
    """Check whether an element is a wall.

    True for framed, solid and log walls.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a wall, False otherwise (including an invalid element ID).
    """

def is_floor(element_id: ElementId) -> bool:
    """Check whether an element is a floor.

    True for framed and solid floors.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a floor, False otherwise (including an invalid element ID).
    """

def is_roof(element_id: ElementId) -> bool:
    """Check whether an element is a roof.

    True for framed and solid roofs.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a roof, False otherwise (including an invalid element ID).
    """

def is_metal(element_id: ElementId) -> bool:
    """Check whether an element has a steel (metal) cross-section.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element has a metal cross-section, False otherwise (including an invalid element
        ID).
    """

def is_export_solid(element_id: ElementId) -> bool:
    """Check whether an element is an export solid.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is an export solid, False otherwise (including an invalid element ID).
    """

def is_container(element_id: ElementId) -> bool:
    """Check whether an element is a container.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a container, False otherwise (including an invalid element ID).
    """

def is_connector_axis(element_id: ElementId) -> bool:
    """Check whether an element is a connector axis.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a connector axis, False otherwise (including an invalid element ID).
    """

def is_drilling(element_id: ElementId) -> bool:
    """Check whether an element is a drilling.

    True for axis elements of the drilling (bolt) kind.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a drilling, False otherwise (including an invalid element ID).
    """

def is_node(element_id: ElementId) -> bool:
    """Check whether an element is a node.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a node, False otherwise (including an invalid element ID).
    """

def is_auxiliary(element_id: ElementId) -> bool:
    """Check whether an element is an auxiliary element.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is an auxiliary element, False otherwise (including an invalid element
        ID).
    """

def is_roof_surface(element_id: ElementId) -> bool:
    """Check whether an element is a roof surface.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a roof surface, False otherwise (including an invalid element ID).
    """

def is_caddy_object(element_id: ElementId) -> bool:
    """Check whether an element is a caddy object.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a caddy object, False otherwise (including an invalid element ID).
    """

def is_envelope(element_id: ElementId) -> bool:
    """Check whether an element has a building envelope type assigned.

    True if any envelope type (for example wall, floor, roof or opening) is set on the element.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if an envelope type is assigned, False otherwise (including an invalid element ID).
    """

def is_architecture_wall_2dc(element_id: ElementId) -> bool:
    """Check whether an element is a wall linked to a 2dc architecture wall.

    Only walls can be true.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a wall linked to a 2dc architecture wall, False otherwise (including
        an invalid element ID).
    """

def is_architecture_wall_xml(element_id: ElementId) -> bool:
    """Check whether an element is a wall linked to XML architecture wall data.

    Only walls can be true.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a wall with XML architecture wall data, False otherwise (including an
        invalid element ID).
    """

def is_surface(element_id: ElementId) -> bool:
    """Check whether an element is a surface.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a surface, False otherwise (including an invalid element ID).
    """

def is_line(element_id: ElementId) -> bool:
    """Check whether an element is a line.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a line, False otherwise (including an invalid element ID).
    """

def get_auto_attribute(element_id: ElementId, number: UnsignedInt) -> str:
    """Get the value of an auto attribute of an element.

    Auto attributes are calculated texts; call update_auto_attribute first if values may be stale.
    Returns an empty string for an invalid element ID or a number above 999.

    Parameters:
        element_id: Element ID.
        number: Auto attribute number, counted from 1. Numbers above 999 return an empty string.

    Returns:
        The auto attribute value, or an empty string.
    """

def get_auto_attribute_name(number: UnsignedInt) -> str:
    """Get the display name of an auto attribute.

    Parameters:
        number: Auto attribute number, counted from 1.

    Returns:
        The auto attribute name.
    """

def is_framed_wall(element_id: ElementId) -> bool:
    """Check whether an element is a framed wall.

    True only if the envelope type of the element is exactly framed wall.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a framed wall, False otherwise (including an invalid element ID).
    """

def is_solid_wall(element_id: ElementId) -> bool:
    """Check whether an element is a solid wall.

    True only if the envelope type of the element is exactly solid wall.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a solid wall, False otherwise (including an invalid element ID).
    """

def is_log_wall(element_id: ElementId) -> bool:
    """Check whether an element is a log wall.

    True only if the envelope type of the element is exactly log wall.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a log wall, False otherwise (including an invalid element ID).
    """

def is_framed_floor(element_id: ElementId) -> bool:
    """Check whether an element is a framed floor.

    True only if the envelope type of the element is exactly framed floor.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a framed floor, False otherwise (including an invalid element ID).
    """

def is_solid_floor(element_id: ElementId) -> bool:
    """Check whether an element is a solid floor.

    True only if the envelope type of the element is exactly solid floor.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a solid floor, False otherwise (including an invalid element ID).
    """

def is_framed_roof(element_id: ElementId) -> bool:
    """Check whether an element is a framed roof.

    True only if the envelope type of the element is exactly framed roof.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a framed roof, False otherwise (including an invalid element ID).
    """

def is_solid_roof(element_id: ElementId) -> bool:
    """Check whether an element is a solid roof.

    True only if the envelope type of the element is exactly solid roof.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a solid roof, False otherwise (including an invalid element ID).
    """

def get_additional_guid(element_id: ElementId, data_id: str) -> str:
    """Get the external GUID stored on an element for a given data ID.

    Returns an empty string if the element ID is invalid.

    Parameters:
        element_id: Element ID.
        data_id: Identifier of the external data set the GUID belongs to.

    Returns:
        The GUID as text, or an empty string.
    """

def get_prefab_layer_all_assigned(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers assigned to an element, with and without dimensions.

    Deprecated: emits a DeprecationWarning, use get_prefab_layer_info_all_assigned instead. Layers
    are returned in descending order. Pass a valid element ID; invalid IDs are not handled safely.

    Parameters:
        element_id: Element ID of an existing element.

    Returns:
        List of layer numbers, highest first; empty if none are assigned.
    """

def get_prefab_layer_with_dimensions(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers of an element that output dimensions.

    Deprecated: emits a DeprecationWarning, use get_prefab_layer_info_with_dimensions instead.
    Layers are returned in descending order. Pass a valid element ID; invalid IDs are not handled
    safely.

    Parameters:
        element_id: Element ID of an existing element.

    Returns:
        List of layer numbers with dimension output, highest first; empty if none.
    """

def get_prefab_layer_without_dimensions(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers of an element that output without dimensions.

    Deprecated: emits a DeprecationWarning, use get_prefab_layer_info_without_dimensions instead.
    Layers are returned in descending order. Pass a valid element ID; invalid IDs are not handled
    safely.

    Parameters:
        element_id: Element ID of an existing element.

    Returns:
        List of layer numbers without dimension output, highest first; empty if none.
    """

def is_nesting_parent(element_id: ElementId) -> bool:
    """Check whether an element is a nesting parent.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a nesting parent, False otherwise (including an invalid element ID).
    """

def is_nesting_raw_part(element_id: ElementId) -> bool:
    """Check whether an element is a nesting raw part.

    True for nesting parents and for optimization bar elements used as raw stock.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a nesting raw part, False otherwise (including an invalid element
        ID).
    """

def get_container_number(element_id: ElementId) -> UnsignedInt:
    """Get the container number of a container element.

    Returns 0 for non-container elements, invalid IDs, or containers without a valid container
    number.

    Parameters:
        element_id: Element ID of a container.

    Returns:
        The container number, or 0.
    """

def get_container_number_with_prefix(element_id: ElementId) -> str:
    """Get the container number of a container element including its prefix.

    Returns an empty string for non-container elements, invalid IDs, or containers without a valid
    container number.

    Parameters:
        element_id: Element ID of a container.

    Returns:
        Prefix followed by the container number, or an empty string.
    """

def get_group_list_items() -> list[str]:
    """Get the entries of the group list.

    Reads the list of the open document.

    Returns:
        List of the entries, empty if there are none.
    """

def get_subgroup_list_items() -> list[str]:
    """Get the entries of the subgroup list.

    Reads the list of the open document.

    Returns:
        List of the entries, empty if there are none.
    """

def get_comment_list_items() -> list[str]:
    """Get the entries of the comment list.

    Reads the list of the open document.

    Returns:
        List of the entries, empty if there are none.
    """

def get_sku_list_items() -> list[str]:
    """Get the entries of the SKU list.

    Reads the list of the open document.

    Returns:
        List of the entries, empty if there are none.
    """

def get_user_attribute_list_items(number: UserAttributeId) -> list[str]:
    """Get the list entries of a user attribute.

    Reads the list of the open document.

    Parameters:
        number: User attribute number, counted from 1.

    Returns:
        List of the entries, empty if there are none.
    """

def is_circular_mep(element_id: ElementId) -> bool:
    """Check whether an element is a circular MEP (installation) line.

    Parameters:
        element_id: Element ID. An invalid or deleted ID returns False.

    Returns:
        True if the element is a circular MEP line, False otherwise (including an invalid element
        ID).
    """

def is_rectangular_mep(element_id: ElementId) -> bool:
    """Check whether an element is a rectangular MEP (installation) element.

    Returns False for an invalid or deleted element ID.

    Parameters:
        element_id: Element ID.

    Returns:
        True if the element is a rectangular MEP element, otherwise False.
    """

def get_machine_calculation_state(element_id: ElementId) -> str:
    """Get the machine calculation state of an element as a display text.

    The text describes whether the position is calculated, checked or confirmed as OK, optionally
    followed by locked and blocked-for-export markers. The wording follows the cadwork UI language.

    Parameters:
        element_id: Element ID.

    Returns:
        State text, or an empty string for an invalid element ID or an element without machine data.
    """

def get_machine_calculation_set_machine_type(element_id: ElementId) -> str:
    """Get the machine type of an element's machine calculation set as a display text.

    The text is the machine name as shown in cadwork 3D (localized).

    Parameters:
        element_id: Element ID.

    Returns:
        Machine name, or an empty string for an invalid element ID or when no machine type is set.
    """

def is_btl_processing_group(element_id: ElementId) -> bool:
    """Check whether an element is a BTL processing group.

    An element qualifies when it has the BTL processing group attribute and the BTL processing group
    reference points. Returns False for an invalid element ID.

    Parameters:
        element_id: Element ID.

    Returns:
        True if the element is a BTL processing group, otherwise False.
    """

def is_hundegger_processing_group(element_id: ElementId) -> bool:
    """Check whether an element is a Hundegger processing group.

    An element qualifies when it has the Hundegger processing group attribute and the Hundegger
    processing group reference points. Returns False for an invalid element ID.

    Parameters:
        element_id: Element ID.

    Returns:
        True if the element is a Hundegger processing group, otherwise False.
    """

def get_element_grouping_type() -> element_grouping_type:
    """Get whether the element builder uses the group or subgroup attribute.

    Reads an application option; it is not tied to a single element.

    Returns:
        element_grouping_type.group or element_grouping_type.subgroup.
    """

def set_element_grouping_type(element_grouping_type: element_grouping_type) -> None:
    """Set whether the element builder uses the group or subgroup attribute.

    Changes an application option, not a single element. Any value other than group is treated as
    subgroup.

    Parameters:
        element_grouping_type: element_grouping_type.group or element_grouping_type.subgroup.
    """

def get_associated_nesting_name(element_id: ElementId) -> str:
    """Get the name of the nesting group an element belongs to.

    Returns an empty string for an invalid element ID or an element that is not part of a nesting
    group.

    Parameters:
        element_id: Element ID.

    Returns:
        Nesting group name, or an empty string.
    """

def get_associated_nesting_number(element_id: ElementId) -> str:
    """Get the production list number of the nesting parent of an element.

    The parent is looked up as nesting parent first, then as linear optimization parent. The number
    is returned as text.

    Parameters:
        element_id: Element ID.

    Returns:
        Production list number of the parent as a string, or an empty string if the element is
        invalid or has no such parent.
    """

def get_attribute_display_settings_for_2d() -> attribute_display_settings:
    """Get the attribute text position settings for 2D export (normal).

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_2d_with_layout() -> attribute_display_settings:
    """Get the attribute text position settings for 2D export with frame.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_2d_without_layout() -> attribute_display_settings:
    """Get the attribute text position settings for 2D export without frame.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_3d() -> attribute_display_settings:
    """Get the attribute text position settings for the 3D view.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_container() -> attribute_display_settings:
    """Get the attribute text position settings for containers.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_export_solid() -> attribute_display_settings:
    """Get the attribute text position settings for solid export.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_framed_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall axes.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_framed_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall beams.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_framed_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall openings.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_framed_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall panels.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_log_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for log wall axes.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_log_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for log wall beams.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_log_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for log wall openings.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_log_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for log wall panels.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_machine() -> attribute_display_settings:
    """Get the attribute text position settings for machine output.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_nesting_element() -> attribute_display_settings:
    """Get the attribute text position settings for nesting elements.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_nesting_volume() -> attribute_display_settings:
    """Get the attribute text position settings for nesting volumes.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_solid_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall axes.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_solid_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall beams.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_solid_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall openings.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def get_attribute_display_settings_for_solid_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall panels.

    The result is a snapshot of the stored settings; changing it does not write back. It tells
    whether the text position is given in mm or in percent, and holds both values.

    Returns:
        attribute_display_settings with the text position type (absolute in mm, or percentage) and
        both position values.
    """

def is_processing(element_id: ElementId) -> bool:
    """Check whether a processing with the given ID exists on a visible element.

    Despite the parameter name, the value is compared with the ID of a processing (machining), not
    an element ID. Only processings of currently visible elements are searched.

    Parameters:
        element_id: ID of the processing to look for.

    Returns:
        True if a visible element carries a processing with this ID, otherwise False.
    """

def delete_user_attribute(number: UserAttributeId) -> bool:
    """Delete a user attribute definition from the attribute list.

    Deleted only if its list has no items; otherwise nothing is deleted and False is returned.

    Parameters:
        number: User attribute number (1-based).

    Returns:
        True if the attribute was deleted, False if it still has list items or could not be deleted.
    """

def is_attribute_visible_in_modify_window(number: UnsignedInt) -> bool:
    """Check whether a user attribute is shown in the Modify window.

    Returns False for a number outside the user attribute range.

    Parameters:
        number: User attribute number (1 to 10000).

    Returns:
        True if the attribute is visible in the Modify window, otherwise False.
    """

def set_attribute_visibility_in_modify_window(number: UnsignedInt, visibility: bool) -> None:
    """Show or hide a user attribute in the Modify window.

    Silently does nothing for a number outside the user attribute range.

    Parameters:
        number: User attribute number (1 to 10000).
        visibility: True to show the attribute, False to hide it.
    """

def set_cutting_set(element_id_list: list[ElementId], cutting_set_name: str) -> bool:
    """Assign a cutting set to elements by name.

    The name is matched case-insensitively. Per element, the document sets are searched first, then
    the user profile sets (timber) or the standard sets (steel and round beams). Sets found outside
    the document are copied into it once. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to assign to.
        cutting_set_name: Name of the cutting set.

    Returns:
        True if the set was assigned to at least one element, False if no element resolved or the
        name matches no applicable set.
    """

def get_standard_element_material_id(element_id: ElementId) -> int:
    """Get the material ID of a standard element.

    Returns 0 for an invalid element ID or an element that is not a standard element.

    Parameters:
        element_id: Element ID.

    Returns:
        Material ID, or 0.
    """

def set_machine_calculation_set(element_ids: list[ElementId], name: str) -> bool:
    """Assign a machine calculation set to elements by name.

    If several sets share the name, the first one is used. Invalid IDs and elements without machine
    data are skipped; an empty list is a no-op that still returns True when the set exists.

    Parameters:
        element_ids: List of element IDs to assign to.
        name: Name of the machine calculation set.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec
        >>> [element] = ec.get_active_identifiable_element_ids()
        >>> current_set = ac.get_machine_calculation_set(element)
        >>> success = ac.set_machine_calculation_set([element], "xyz_hundegger K2_BVN")

    Returns:
        True if a set with this name exists, False if no set with this name is found.
    """

def delete_item_from_name_list(item: str) -> bool:
    """Delete an entry from the Name attribute list.

    Not deleted when the item does not exist or is still used by elements.

    Parameters:
        item: Text of the list entry to delete.

    Returns:
        True if deleted, False otherwise.
    """

def get_additional_data_keys(element_id: ElementId) -> list[str]:
    """List the additional data keys set on an element through this API.

    Keys written internally by cadwork 3D are excluded.

    Parameters:
        element_id: Element ID.

    Returns:
        List of keys, empty if the element is invalid or has no such keys.
    """

def get_prefab_layer_info_all_assigned(element_id: ElementId) -> list[prefab_layer_info]:
    """Get all prefab layers assigned to an element.

    Contains the layers output with dimensions followed by the layers output without dimensions.
    Each item holds a layer number and a side (element itself, reference side or opposite side).

    Parameters:
        element_id: Element ID.

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """

def get_prefab_layer_info_with_dimensions(element_id: ElementId) -> list[prefab_layer_info]:
    """Get the prefab layers of an element that are output with dimensions.

    Items are in ascending layer order; each holds a layer number and a side (element itself,
    reference side or opposite side).

    Parameters:
        element_id: Element ID.

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """

def get_prefab_layer_info_without_dimensions(element_id: ElementId) -> list[prefab_layer_info]:
    """Get the prefab layers of an element that are output without dimensions.

    Items are in ascending layer order; each holds a layer number and a side (element itself,
    reference side or opposite side).

    Parameters:
        element_id: Element ID.

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """
