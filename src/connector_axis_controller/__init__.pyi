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

    A standard connector is a predefined bolt, screw or dowel configuration from the connector
    catalog (see the connector configuration dialog). The new axis starts at point1, points towards
    point2 and has the length of their distance. It is inserted into the model, made visible and the
    display is refreshed if auto refresh is on. Returns 0 if no standard connector with that name
    exists or the element could not be created. Use
    `connector_axis_controller.get_standard_connector_list()` to list valid names.

    Parameters:
        axis_name: Name of a standard connector, e.g. from
            `connector_axis_controller.get_standard_connector_list()`. The name is looked up in the
            current cadwork language; the first match is used.
        point1: Start point of the axis in model units (mm); becomes the origin of the axis.
        point2: End point of the axis in model units (mm); only defines the direction and the length
            (distance to point1). The two points must differ.

    Examples:
        >>> import cadwork
        >>> import connector_axis_controller as cac

        >>> names = cac.get_standard_connector_list()
        >>> if names:
        ...     start = cadwork.point_3d(0.0, 0.0, 0.0)
        ...     end = cadwork.point_3d(0.0, 0.0, 200.0)
        ...     axis_id = cac.create_standard_connector(names[0], start, end)
        ...     if axis_id == 0:
        ...         print('Connector axis could not be created')

    Returns:
        Element ID of the created connector axis, or 0 if the name is unknown or creation fails.
    """

def set_bolt_length(axis_id: ElementId, length: float) -> None:
    """Set the bolt length of a connector axis and switch off automatic bolt length.

    The given length is used as the bolt length from now on; automatic length determination is
    turned off for this axis. The change is stored on the axis and the display is refreshed if auto
    refresh is on. Does nothing if the element ID is invalid or the axis data cannot be read. Read
    the value back with `connector_axis_controller.get_bolt_length()`, or switch back to cadwork's
    own length with `connector_axis_controller.set_bolt_length_automatic()`.

    Parameters:
        axis_id: Element ID of a connector axis, e.g. from
            `connector_axis_controller.create_standard_connector()`.
        length: Bolt length in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         cac.set_bolt_length(element_id, 240.0)
        ...         print(cac.get_bolt_length_automatic(element_id))  # False
    """

def set_bolt_length_automatic(axis_id: ElementId, length_automatic: bool) -> None:
    """Switch automatic bolt length of a connector axis on or off.

    With automatic length on, cadwork determines the bolt length from the connected elements; with
    it off, the length set by `connector_axis_controller.set_bolt_length()` is used. Does nothing if
    the element ID is invalid or the element is not a connector axis. The display is refreshed if
    auto refresh is on. Check the current state with
    `connector_axis_controller.get_bolt_length_automatic()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        length_automatic: True to let cadwork determine the bolt length, False to use the manually
            set length.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         cac.set_bolt_length_automatic(element_id, True)
        ...         print(cac.get_bolt_length(element_id))
    """

def set_diameter(axis_id: ElementId, diameter: float) -> None:
    """Set the drilling diameter of all sections of a connector axis.

    A connector axis is divided into sections (stretches inside different elements or in air), each
    with its own drilling diameter. This writes the same absolute diameter to every section and
    refreshes the display if auto refresh is on. Does nothing if the element ID is invalid or the
    axis data cannot be read. To change a single section use
    `connector_axis_controller.set_section_diameter()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        diameter: Drilling diameter in model units (mm), stored as an absolute value (not relative
            to the bolt) in every section.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         cac.set_diameter(element_id, 14.0)
    """

def set_section_diameter(axis_id: ElementId, section_index: UnsignedInt, diameter: float) -> None:
    """Set the drilling diameter of one section of a connector axis.

    Sections are the stretches of the axis inside different elements or in air;
    `connector_axis_controller.get_section_count()` gives their number. The diameter is stored as an
    absolute value and the display is refreshed if auto refresh is on. Does nothing if the element
    ID is invalid or the axis data cannot be read; an out-of-range section index changes nothing.
    Read it back with `connector_axis_controller.get_section_diameter()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.
        diameter: Drilling diameter in model units (mm), stored as an absolute value.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id) > 0:
        ...         cac.set_section_diameter(element_id, 0, 16.0)
        ...         print(cac.get_section_diameter(element_id, 0))
    """

def check_axis(axis_id: ElementId) -> bool:
    """Check whether a connector axis has a valid cutting ability.

    The cutting ability (connection configuration) tells whether the axis, with its current catalog
    items and the elements it passes through, can be machined. Read-only check; nothing is modified.
    Use `connector_axis_controller.update_axis_cutting_ability()` to re-evaluate and refresh axes
    after changes.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and not cac.check_axis(element_id):
        ...         print('Connector axis with invalid cutting ability:', element_id)

    Returns:
        True if the element is a connector axis with valid cutting ability. False if its cutting
        ability is not valid, if the element is not a connector axis, or if the element ID is
        invalid.
    """

def clear_errors() -> None:
    """Clear the stored connector axis error messages.

    Empties the error message list kept by the connector axis controller, so earlier errors are not
    reported again. Has no effect on the model.

    Examples:
        >>> import connector_axis_controller as cac

        >>> cac.clear_errors()
    """

def update_axis_cutting_ability(axis_id_list: list[ElementId]) -> None:
    """Re-evaluate the cutting ability of connector axes and refresh them.

    For each axis the connection configuration is checked again. Axes that are still valid are
    recreated (regenerated in the model) only when auto display refresh is on. Axes whose cutting
    ability is invalid are passed to cadwork's cutting ability check, which tries to correct them.
    IDs that are invalid or not connector axes are skipped. Use
    `connector_axis_controller.check_axis()` to only test a single axis.

    Parameters:
        axis_id_list: List of element IDs of connector axes, e.g. the active elements for which
            `attribute_controller.is_connector_axis()` is True.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> axis_ids = [e for e in ec.get_active_identifiable_element_ids()
        ...             if ac.is_connector_axis(e)]
        >>> cac.update_axis_cutting_ability(axis_ids)
    """

def set_bolt_item(axis_id: ElementId, item_guid: str) -> None:
    """Set the bolt catalog item of a connector axis.

    The bolt item defines the type and dimensions of the bolt (for example a bolt with head or a lag
    bolt). It is looked up by GUID in the user catalog and assigned to the axis; the display is
    refreshed if auto refresh is on. Does nothing if the element ID is invalid or the axis data
    cannot be read. Read the current item back with
    `connector_axis_controller.get_bolt_item_guid()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        item_guid: GUID of a bolt item in the user catalog, e.g. from
            `connector_axis_controller.get_item_guid_by_name()` with a bolt type such as
            `vba_catalog_item_type.bolt_with_head`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> bolt_type = cadwork.vba_catalog_item_type.bolt_with_head
        >>> guid = cac.get_item_guid_by_name('M16', bolt_type)
        >>> if guid:
        ...     for element_id in ec.get_active_identifiable_element_ids():
        ...         if ac.is_connector_axis(element_id):
        ...             cac.set_bolt_item(element_id, guid)
    """

def create_blank_connector(diameter: float, start_point: point_3d, end_point: point_3d) -> ElementId:
    """Create an empty connector axis with a given diameter between two points.

    A blank connector is a plain connector axis (green, no standard connector configuration) that
    you can then equip with a bolt item and other settings. The axis runs from start_point to
    end_point, is inserted into the model, made visible, and the display is refreshed if auto
    refresh is on. Returns 0 if creation fails or the resulting axis lies outside the valid model
    range. For a predefined bolt or screw use
    `connector_axis_controller.create_standard_connector()` instead.

    Parameters:
        diameter: Drilling diameter of the axis in model units (mm).
        start_point: Start point of the axis in model units (mm).
        end_point: End point of the axis in model units (mm).

    Examples:
        >>> import cadwork
        >>> import connector_axis_controller as cac

        >>> start = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> end = cadwork.point_3d(300.0, 0.0, 0.0)
        >>> axis_id = cac.create_blank_connector(16.0, start, end)
        >>> if axis_id:
        ...     print('Sections:', cac.get_section_count(axis_id))

    Returns:
        Element ID of the created connector axis, or 0 on failure.
    """

def import_from_file(file_path: str) -> None:
    """Import standard connector definitions from a file.

    Adds the standard connectors stored in the file to the standard connector catalog. Entries that
    are duplicates of existing ones are ignored, existing entries are never overwritten. Returns
    nothing, so check the result with `connector_axis_controller.get_standard_connector_list()`.

    Parameters:
        file_path: Full path of the standard connector file to import. Use forward slashes or a raw
            string.

    Examples:
        >>> import connector_axis_controller as cac

        >>> before = len(cac.get_standard_connector_list())
        >>> cac.import_from_file('C:/temp/standard_connectors.xml')
        >>> print(len(cac.get_standard_connector_list()) - before, 'connectors added')
    """

def start_configuration_dialog() -> None:
    """Open the connector axis configuration dialog.

    Shows cadwork's configuration dialog where standard connectors are defined and edited. Intended
    for interactive scripts: it needs a user at the screen. Standard connectors changed there are
    afterwards visible via `connector_axis_controller.get_standard_connector_list()`.

    Examples:
        >>> import connector_axis_controller as cac

        >>> cac.start_configuration_dialog()
        >>> print(cac.get_standard_connector_list())
    """

def get_item_guid_by_name(name: str, item_type: vba_catalog_item_type) -> str:
    """Find a catalog item of a given type by name and return its GUID.

    Catalog items are the parts a connector is built from: bolts, nuts, washers and so on. Searches
    the user catalog for items of the given type and returns the GUID of the first item whose name
    matches, ignoring case. The GUID can be passed to `connector_axis_controller.set_bolt_item()` or
    `connector_axis_controller.set_items_at_intersection()`.

    Parameters:
        name: Name of the catalog item; compared case-insensitively and in full.
        item_type: Catalog item type to search in, e.g. `vba_catalog_item_type.nut` or
            `vba_catalog_item_type.bolt_with_head`.

    Examples:
        >>> import cadwork
        >>> import connector_axis_controller as cac

        >>> guid = cac.get_item_guid_by_name('M16', cadwork.vba_catalog_item_type.nut)
        >>> if not guid:
        ...     print('No nut named M16 in the user catalog')

    Returns:
        GUID of the first matching item, or an empty string if none matches.
    """

def get_bolt_length(axis_id: ElementId) -> float:
    """Get the bolt length of a connector axis.

    Returns the bolt length currently used by the axis, whether it was set manually with
    `connector_axis_controller.set_bolt_length()` or determined automatically (see
    `connector_axis_controller.get_bolt_length_automatic()`). Returns 0.0 if the element ID is
    invalid.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(element_id, cac.get_bolt_length(element_id))

    Returns:
        Bolt length in model units (mm); 0.0 if the element ID is invalid.
    """

def get_bolt_over_length(axis_id: ElementId) -> float:
    """Get the bolt over-length of a connector axis.

    The over-length is the extra length of the bolt beyond the length required by the connection.
    Set it with `connector_axis_controller.set_bolt_over_length()`. Returns 0.0 if the element ID is
    invalid.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(cac.get_bolt_over_length(element_id))

    Returns:
        Bolt over-length in model units (mm); 0.0 if the element ID is invalid.
    """

def set_bolt_over_length(axis_id: ElementId, over_length: float) -> None:
    """Set the bolt over-length of a connector axis.

    The over-length is the extra length of the bolt beyond the length required by the connection.
    The value is stored on the axis and the display is refreshed if auto refresh is on. Does nothing
    if the element ID is invalid or the axis data cannot be read. Read it back with
    `connector_axis_controller.get_bolt_over_length()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        over_length: Bolt over-length in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         cac.set_bolt_over_length(element_id, 10.0)
    """

def get_bolt_length_automatic(axis_id: ElementId) -> bool:
    """Check whether the bolt length of a connector axis is determined automatically.

    When automatic length is on, cadwork derives the bolt length from the connected elements;
    setting a length with `connector_axis_controller.set_bolt_length()` switches it off. Change it
    with `connector_axis_controller.set_bolt_length_automatic()`.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(element_id, cac.get_bolt_length_automatic(element_id))

    Returns:
        True if automatic bolt length is on; False if it is off or the element ID is invalid.
    """

def get_bolt_item_guid(axis_id: ElementId) -> str:
    """Get the GUID of the bolt catalog item of a connector axis.

    Returns the GUID of the bolt item assigned to the axis. Use it with
    `connector_axis_controller.get_axis_item_name()` and the other `get_axis_item_*` functions to
    read the item's name, material, norm and order data. Assign a different bolt with
    `connector_axis_controller.set_bolt_item()`.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         guid = cac.get_bolt_item_guid(element_id)
        ...         print(cac.get_axis_item_name(guid))

    Returns:
        GUID of the bolt item; an empty string if the element ID is invalid.
    """

def get_section_diameter(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the drilling diameter of one section of a connector axis.

    Sections are the stretches of the axis inside different elements or in air;
    `connector_axis_controller.get_section_count()` gives their number. Returns 0.0 for an invalid
    element ID or an out-of-range section index. Change the value with
    `connector_axis_controller.set_section_diameter()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_section_count(element_id)):
        ...             print(i, cac.get_section_diameter(element_id, i))

    Returns:
        Drilling diameter in model units (mm); 0.0 if the element ID or section index is invalid.
    """

def get_axis_items_guids(axis_id: ElementId) -> list[str]:
    """Get the GUIDs of the catalog items attached to a connector axis.

    Collects the items of all intersections of the axis, such as nuts, washers and other fittings;
    the bolt item itself is not included (use `connector_axis_controller.get_bolt_item_guid()` for
    it). Returns an empty list if the element ID is invalid or the element has no connector axis
    data. Feed the GUIDs to `connector_axis_controller.get_axis_item_name()` and the related
    `get_axis_item_*` functions.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for guid in cac.get_axis_items_guids(element_id):
        ...             print(cac.get_axis_item_name(guid))

    Returns:
        List of item GUIDs (nuts, washers, etc., without the bolt); an empty list on failure or if
        the axis has no items.
    """

def get_axis_item_name(guid: str) -> str:
    """Get the name of a catalog item attached to an axis.

    The item is looked up by GUID among the items stored in the current document, not in the user
    catalog, so it works for items already used on axes of this document. Get GUIDs from
    `connector_axis_controller.get_axis_items_guids()` or
    `connector_axis_controller.get_bolt_item_guid()`.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         guid = cac.get_bolt_item_guid(element_id)
        ...         print(cac.get_axis_item_name(guid))

    Returns:
        Name of the item; typically an empty string if no item with that GUID is stored in the
        document.
    """

def get_axis_item_material(guid: str) -> str:
    """Get the material of a catalog item attached to an axis.

    The item is looked up by GUID among the items stored in the current document, so it works for
    items already used on axes of this document. The material is the text stored in the catalog
    entry (for example a steel grade), not a cadwork material ID.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for guid in cac.get_axis_items_guids(element_id):
        ...             print(cac.get_axis_item_material(guid))

    Returns:
        Material of the item; typically an empty string if no item with that GUID is stored in the
        document.
    """

def get_axis_item_norm(guid: str) -> str:
    """Get the standard (norm) designation of a catalog item attached to an axis.

    The item is looked up by GUID among the items stored in the current document, so it works for
    items already used on axes of this document. The norm is the standard number stored in the
    catalog entry, for example a DIN or ISO designation.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for guid in cac.get_axis_items_guids(element_id):
        ...             print(cac.get_axis_item_norm(guid))

    Returns:
        Norm of the item; typically an empty string if no item with that GUID is stored in the
        document.
    """

def get_axis_item_strength_category(guid: str) -> str:
    """Get the strength category of a catalog item attached to an axis.

    The item is looked up by GUID among the items stored in the current document, so it works for
    items already used on axes of this document. The strength category is the text stored in the
    catalog entry, for example a property class such as 8.8.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         guid = cac.get_bolt_item_guid(element_id)
        ...         print(cac.get_axis_item_strength_category(guid))

    Returns:
        Strength category of the item; typically an empty string if no item with that GUID is stored
        in the document.
    """

def get_axis_item_user_field(guid: str, user_item_number: int) -> str:
    """Get one of the five user fields of a catalog item attached to an axis.

    Catalog items carry five free text fields that can be used for custom data. The item is looked
    up by GUID among the items stored in the current document. Returns an empty string for a number
    outside 1 to 5.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.
        user_item_number: Number of the user field, 1 to 5.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for guid in cac.get_axis_items_guids(element_id):
        ...             print(cac.get_axis_item_user_field(guid, 1))

    Returns:
        Value of the user field; an empty string if the field is empty or the number is outside 1 to
        5 (an unknown GUID usually gives an empty string as well).
    """

def get_axis_item_order_number(guid: str) -> str:
    """Get the order number of a catalog item attached to an axis.

    The item is looked up by GUID among the items stored in the current document. For the order
    number of the bolt in the length actually used on an axis, use
    `connector_axis_controller.get_bolt_order_number()`, since bolts have one order number per
    available length.

    Parameters:
        guid: GUID of an item, e.g. from `connector_axis_controller.get_axis_items_guids()` or
            `connector_axis_controller.get_bolt_item_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for guid in cac.get_axis_items_guids(element_id):
        ...             print(cac.get_axis_item_order_number(guid))

    Returns:
        Order number of the item; typically an empty string if no item with that GUID is stored in
        the document.
    """

def get_bolt_order_number(axis_id: ElementId) -> str:
    """Get the order number of the bolt in its current length.

    A bolt item in the catalog lists the available lengths, each with its own order number. This
    returns the order number of the entry whose length equals the bolt length of the axis. Returns
    an empty string if the element ID is invalid, the axis data cannot be read, or no catalog length
    matches the current bolt length. Set the bolt length with
    `connector_axis_controller.set_bolt_length()` to a catalog length to get a result.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         order_number = cac.get_bolt_order_number(element_id)
        ...         print(cac.get_bolt_length(element_id), order_number or 'no match')

    Returns:
        Order number of the bolt; an empty string if the element ID is invalid or no catalog length
        matches the bolt length.
    """

def get_section_count(axis_id: ElementId) -> int:
    """Get the number of sections of a connector axis.

    A connector axis is divided into sections: the stretches inside different elements or in air,
    each with its own drilling diameter, counterbore and oblong drilling settings. Valid section
    indices for the other `*_section_*` functions are 0 to count - 1. Returns 0 if the element ID is
    invalid or has no connector axis data.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(element_id, cac.get_section_count(element_id), 'sections')

    Returns:
        Number of sections; 0 if the element ID is invalid.
    """

def get_section_material_name(axis_id: ElementId, section_index: UnsignedInt) -> str:
    """Get the material name of the element in contact with a section of a connector axis.

    Each section of the axis passes through an element (or air). This returns the material name
    stored for that section; find the element itself with
    `connector_axis_controller.get_section_contact_element()`. Returns an empty string for an
    invalid element ID, an out-of-range section index, or a section without material.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_section_count(element_id)):
        ...             print(i, cac.get_section_material_name(element_id, i))

    Returns:
        Material name; an empty string if the element ID or section index is invalid.
    """

def get_section_contact_element(axis_id: ElementId, section_index: UnsignedInt) -> ElementId:
    """Get the element in contact with a section of a connector axis.

    Each section of the axis passes through an element; this returns the first element found in that
    section. Sections in air have no element and give 0. Use
    `connector_axis_controller.get_section_material_name()` for the material of that section.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_section_count(element_id)):
        ...             contact_id = cac.get_section_contact_element(element_id, i)
        ...             print(i, contact_id)

    Returns:
        Element ID of the first element in that section; 0 if the axis ID or section index is
        invalid or the section has no element.
    """

def get_bolt_diameter(axis_id: ElementId) -> float:
    """Get the bolt diameter of a connector axis.

    Returns the inner diameter of the bolt item if the axis has one, otherwise the diameter of the
    axis itself. This is the bolt dimension, not the drilling diameter of a section; read that with
    `connector_axis_controller.get_section_diameter()`.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(cac.get_bolt_diameter(element_id))

    Returns:
        Bolt diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_standard_connector_list() -> list[str]:
    """Get the names of all available standard connectors.

    Standard connectors are the predefined bolt, screw and dowel configurations of the connector
    catalog. The names are returned in the current cadwork language; pass one to
    `connector_axis_controller.create_standard_connector()` or
    `connector_axis_controller.get_connector_axis_guid_by_name()`. New entries can be added with
    `connector_axis_controller.import_from_file()`.

    Examples:
        >>> import connector_axis_controller as cac

        >>> for name in cac.get_standard_connector_list():
        ...     print(name)

    Returns:
        List of standard connector names; empty if the catalog has none.
    """

def get_counterbore_diameter_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore diameter at the start side of a section.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The start side is the side of the section towards the start of the axis. Returns 0.0 for an
    invalid element ID. Pass a valid section index (below
    `connector_axis_controller.get_section_count()`); out-of-range indices are not handled safely.
    Set the counterbore with `connector_axis_controller.set_counterbore_for_start_side()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_diameter_for_start_side(element_id, 0))

    Returns:
        Counterbore diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_diameter_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore diameter at the end side of a section.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The end side is the side of the section towards the end of the axis. Returns 0.0 for an invalid
    element ID. Pass a valid section index (below `connector_axis_controller.get_section_count()`);
    out-of-range indices are not handled safely. Set the counterbore with
    `connector_axis_controller.set_counterbore_for_end_side()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_diameter_for_end_side(element_id, 0))

    Returns:
        Counterbore diameter in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_depth_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore depth at the start side of a section.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The start side is the side of the section towards the start of the axis. Returns the stored
    depth, which is the value set with `connector_axis_controller.set_counterbore_for_start_side()`.
    Returns 0.0 for an invalid element ID; pass a valid section index (below
    `connector_axis_controller.get_section_count()`), as out-of-range indices are not handled
    safely.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_depth_for_start_side(element_id, 0))

    Returns:
        Counterbore depth in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_depth_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the counterbore depth at the end side of a section.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The end side is the side of the section towards the end of the axis. Returns the stored depth,
    which is the value set with `connector_axis_controller.set_counterbore_for_end_side()`. Returns
    0.0 for an invalid element ID; pass a valid section index (below
    `connector_axis_controller.get_section_count()`), as out-of-range indices are not handled
    safely.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_depth_for_end_side(element_id, 0))

    Returns:
        Counterbore depth in model units (mm); 0.0 if the element ID is invalid.
    """

def get_counterbore_is_conical_for_start_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether the counterbore at the start side of a section is conical.

    A conical counterbore is a countersink with tapered walls, for example for a countersunk screw
    head; otherwise the recess is cylindrical. The start side is the side of the section towards the
    start of the axis. Pass a valid section index (below
    `connector_axis_controller.get_section_count()`), as out-of-range indices are not handled
    safely. Set it with `connector_axis_controller.set_counterbore_for_start_side()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_is_conical_for_start_side(element_id, 0))

    Returns:
        True if the counterbore is conical; False if it is not or if the element ID is invalid.
    """

def get_counterbore_is_conical_for_end_side(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether the counterbore at the end side of a section is conical.

    A conical counterbore is a countersink with tapered walls, for example for a countersunk screw
    head; otherwise the recess is cylindrical. The end side is the side of the section towards the
    end of the axis. Pass a valid section index (below
    `connector_axis_controller.get_section_count()`), as out-of-range indices are not handled
    safely. Set it with `connector_axis_controller.set_counterbore_for_end_side()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         print(cac.get_counterbore_is_conical_for_end_side(element_id, 0))

    Returns:
        True if the counterbore is conical; False if it is not or if the element ID is invalid.
    """

def set_counterbore_for_start_side(
    axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float, is_conical: bool
) -> None:
    """Set the counterbore at the start side of a section of a connector axis.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The start side is the side of the section towards the start of the axis. Diameter, depth and
    shape are replaced together and the display is refreshed if auto refresh is on. Does nothing if
    the element ID is invalid or the section index is out of range. Read the values back with the
    `get_counterbore_*_for_start_side` functions.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.
        diameter: Counterbore diameter in model units (mm).
        depth: Counterbore depth in model units (mm).
        is_conical: True for a conical counterbore (countersink), False for a cylindrical one.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         cac.set_counterbore_for_start_side(element_id, 0, 30.0, 12.0, False)
    """

def set_counterbore_for_end_side(
    axis_id: ElementId, section_index: UnsignedInt, diameter: float, depth: float, is_conical: bool
) -> None:
    """Set the counterbore at the end side of a section of a connector axis.

    A counterbore is a widened recess at the end of a section, for example for a bolt head or nut.
    The end side is the side of the section towards the end of the axis. Diameter, depth and shape
    are replaced together and the display is refreshed if auto refresh is on. Does nothing if the
    element ID is invalid or the section index is out of range. Read the values back with the
    `get_counterbore_*_for_end_side` functions.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.
        diameter: Counterbore diameter in model units (mm).
        depth: Counterbore depth in model units (mm).
        is_conical: True for a conical counterbore (countersink), False for a cylindrical one.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         last = cac.get_section_count(element_id) - 1
        ...         cac.set_counterbore_for_end_side(element_id, last, 30.0, 12.0, False)
    """

def get_intersection_count(axis_id: ElementId) -> int:
    """Get the number of intersection points of a connector axis.

    Intersection points are the positions along the axis where it meets the surrounding elements;
    catalog items such as nuts and washers are attached to them. Valid intersection indices for
    `connector_axis_controller.get_item_guids_at_intersection()` and
    `connector_axis_controller.set_items_at_intersection()` are 0 to count - 1. Returns 0 if the
    element ID is invalid.

    Parameters:
        axis_id: Element ID of a connector axis.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(element_id, cac.get_intersection_count(element_id))

    Returns:
        Number of intersection points; 0 if the element ID is invalid.
    """

def get_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt) -> list[str]:
    """Get the GUIDs of the catalog items at an intersection of a connector axis.

    Returns the items (nuts, washers and similar fittings) placed at one intersection point of the
    axis. Returns an empty list if the element ID or the intersection index is invalid, or if the
    intersection has no items. Resolve a GUID to a name with
    `connector_axis_controller.get_axis_item_name()`; replace the items with
    `connector_axis_controller.set_items_at_intersection()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        intersection_index: 0-based index of the intersection, smaller than
            `connector_axis_controller.get_intersection_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_intersection_count(element_id)):
        ...             print(i, cac.get_item_guids_at_intersection(element_id, i))

    Returns:
        List of item GUIDs; an empty list if the element ID or intersection index is invalid.
    """

def set_item_guids_at_intersection(axis_id: ElementId, intersection_index: UnsignedInt, item_guids: list[str]) -> None:
    """Replace the items at an intersection of a connector axis by items with given GUIDs.

    Intended to place the listed items at the intersection, all with position 0. In the current
    implementation this function does not reliably apply the items and may fail, so use
    `connector_axis_controller.set_items_at_intersection()` instead, which also lets you give each
    item its position.

    Parameters:
        axis_id: Element ID of a connector axis.
        intersection_index: 0-based index of the intersection, smaller than
            `connector_axis_controller.get_intersection_count()`.
        item_guids: List of GUIDs of the items to set, e.g. from
            `connector_axis_controller.get_item_guid_by_name()`.

    Examples:
        >>> import connector_axis_controller as cac

        ... # Prefer set_items_at_intersection(), which also sets the item positions.
        ... # Reading the items at the first intersection of an axis:
        >>> axis_id = 0  # replace with the element ID of a connector axis
        >>> print(cac.get_item_guids_at_intersection(axis_id, 0))
    """

def get_section_length(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the length of a section of a connector axis.

    Sections are the stretches of the axis inside different elements or in air. An out-of-range
    section index is clamped to the nearest valid section (first or last), so it does not fail.
    Returns 0.0 for an invalid element ID and 1.0 if the axis has no sections.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`. Values outside the range are clamped to
            the first or last section.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_section_count(element_id)):
        ...             print(i, cac.get_section_length(element_id, i))

    Returns:
        Section length in model units (mm); 0.0 if the element ID is invalid, 1.0 if the axis has no
        sections.
    """

def get_section_oblong_drilling_is_enabled(axis_id: ElementId, section_index: UnsignedInt) -> bool:
    """Check whether a section of a connector axis has an oblong (slotted) drilling.

    An oblong drilling is a slot instead of a round hole, used to give a connection tolerance. When
    enabled, its extent and orientation are available through the other
    `get_section_oblong_drilling_*` functions. Switch it with
    `connector_axis_controller.set_section_oblong_drilling_is_enabled()` or
    `connector_axis_controller.set_section_oblong_drilling_is_disabled()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         for i in range(cac.get_section_count(element_id)):
        ...             print(i, cac.get_section_oblong_drilling_is_enabled(element_id, i))

    Returns:
        True if oblong drilling is enabled for the section; False if not or if the element ID or
        section index is invalid.
    """

def get_section_oblong_drilling_positive_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the positive oblong drilling extension of a section of a connector axis.

    An oblong drilling is a slot whose length is given by an extension in the positive and one in
    the negative direction of its orientation angle. Only meaningful while oblong drilling is
    enabled for the section (see
    `connector_axis_controller.get_section_oblong_drilling_is_enabled()`); otherwise 0.0 is
    returned. Also 0.0 for an invalid element ID or section index.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         if cac.get_section_oblong_drilling_is_enabled(element_id, 0):
        ...             print(cac.get_section_oblong_drilling_positive_value(element_id, 0))

    Returns:
        Positive oblong extension in model units (mm); 0.0 if oblong drilling is not enabled, or the
        element ID or section index is invalid.
    """

def get_section_oblong_drilling_negative_value(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the negative oblong drilling extension of a section of a connector axis.

    An oblong drilling is a slot whose length is given by an extension in the positive and one in
    the negative direction of its orientation angle. Only meaningful while oblong drilling is
    enabled for the section (see
    `connector_axis_controller.get_section_oblong_drilling_is_enabled()`); otherwise 0.0 is
    returned. Also 0.0 for an invalid element ID or section index.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         if cac.get_section_oblong_drilling_is_enabled(element_id, 0):
        ...             print(cac.get_section_oblong_drilling_negative_value(element_id, 0))

    Returns:
        Negative oblong extension in model units (mm); 0.0 if oblong drilling is not enabled, or the
        element ID or section index is invalid.
    """

def get_section_oblong_drilling_angle(axis_id: ElementId, section_index: UnsignedInt) -> float:
    """Get the orientation angle of the oblong drilling of a section of a connector axis.

    The angle defines in which direction around the axis the slot of an oblong drilling points. Only
    meaningful while oblong drilling is enabled for the section (see
    `connector_axis_controller.get_section_oblong_drilling_is_enabled()`); otherwise 0.0 is
    returned. Also 0.0 for an invalid element ID or section index.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         if cac.get_section_oblong_drilling_is_enabled(element_id, 0):
        ...             print(cac.get_section_oblong_drilling_angle(element_id, 0))

    Returns:
        Oblong drilling angle as stored on the section; 0.0 if oblong drilling is not enabled, or
        the element ID or section index is invalid.
    """

def set_section_oblong_drilling_is_disabled(axis_id: ElementId, section_index: UnsignedInt) -> None:
    """Disable the oblong drilling of a section of a connector axis.

    Turns the slot off so the section is drilled round again. The extension and angle values of an
    enabled slot stay stored on the section. The display is refreshed if auto refresh is on. Does
    nothing if the element ID is invalid or the section index is out of range. Re-enable with
    `connector_axis_controller.set_section_oblong_drilling_is_enabled()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         cac.set_section_oblong_drilling_is_disabled(element_id, 0)
    """

def set_section_oblong_drilling_is_enabled(
    axis_id: ElementId, section_index: UnsignedInt, positive_value: float, negative_value: float, angle: float
) -> None:
    """Enable the oblong drilling of a section of a connector axis with the given values.

    Turns the section's round drilling into a slot defined by the two extensions and the angle, and
    refreshes the display if auto refresh is on. Does nothing if the element ID is invalid or the
    section index is out of range. Read the values back with the `get_section_oblong_drilling_*`
    functions, or turn the slot off with
    `connector_axis_controller.set_section_oblong_drilling_is_disabled()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        section_index: 0-based index of the section, smaller than
            `connector_axis_controller.get_section_count()`.
        positive_value: Slot extension in the positive direction in model units (mm).
        negative_value: Slot extension in the negative direction in model units (mm).
        angle: Orientation angle of the slot (unit as used by cadwork for oblong drillings).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_section_count(element_id):
        ...         cac.set_section_oblong_drilling_is_enabled(element_id, 0, 5.0, 5.0, 0.0)
        ...         print(cac.get_section_oblong_drilling_is_enabled(element_id, 0))
    """

def set_items_at_intersection(
    axis_id: ElementId, intersection_index: UnsignedInt, items: list[connector_axis_item]
) -> None:
    """Replace the catalog items at an intersection of a connector axis.

    All existing items at the intersection are removed first, then each connector_axis_item is
    looked up by its GUID in the user catalog and placed with its position value. Passing an empty
    list removes all items. Does nothing if the element ID is invalid or the intersection index is
    out of range. The display is refreshed if auto refresh is on. Read the result back with
    `connector_axis_controller.get_item_guids_at_intersection()`.

    Parameters:
        axis_id: Element ID of a connector axis.
        intersection_index: 0-based index of the intersection, smaller than
            `connector_axis_controller.get_intersection_count()`.
        items: List of `cadwork.connector_axis_item`; set each item's GUID (e.g. from
            `connector_axis_controller.get_item_guid_by_name()`) with `set_guid()` and its position
            with `set_position()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import connector_axis_controller as cac

        >>> guid = cac.get_item_guid_by_name('M16', cadwork.vba_catalog_item_type.nut)
        >>> item = cadwork.connector_axis_item()
        >>> item.set_guid(guid)
        >>> item.set_position(0)
        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id) and cac.get_intersection_count(element_id):
        ...         cac.set_items_at_intersection(element_id, 0, [item])
    """

def get_connector_axis_guid_by_name(name: str) -> str:
    """Get the GUID of a standard connector by its name.

    Looks the name up among the standard connectors in the current cadwork language and returns the
    GUID of the first match. Names come from
    `connector_axis_controller.get_standard_connector_list()`. This is the GUID of the catalog entry
    (the connector definition), not of an element in the model, and not the GUID of a bolt, nut or
    washer item.

    Parameters:
        name: Name of the standard connector, as listed by
            `connector_axis_controller.get_standard_connector_list()`.

    Examples:
        >>> import connector_axis_controller as cac

        >>> for name in cac.get_standard_connector_list()[:3]:
        ...     print(name, cac.get_connector_axis_guid_by_name(name))

    Returns:
        GUID of the standard connector, or an empty string if no connector has that name.
    """
