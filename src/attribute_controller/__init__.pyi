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

    The name is the main label of an element, for example the part designation used in lists and
    drawings. A name that is not yet in the document's name list is added to it (with the element's
    own element type and default settings), and assigning a name applies the settings stored for
    that name (machine settings, cutting set, IFC type) to each element. Read it back with
    `attribute_controller.get_name()`; list the known names with
    `attribute_controller.get_name_list_items()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        name: The name to assign to every element. If it is not yet in the name list it is added.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_name(element_ids, 'Stud')
        >>> if element_ids:
        ...     print(ac.get_name(element_ids[0]))
    """

def set_group(element_id_list: list[ElementId], group: str) -> None:
    """Set the group of the given elements.

    The group is a free text attribute used to organize elements, for example by building section.
    The same value is written to every listed element. To offer a value in the group list without
    assigning it, use `attribute_controller.add_item_to_group_list()`. Read it back with
    `attribute_controller.get_group()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        group: The group text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_group(element_ids, 'Ground floor')
        >>> if element_ids:
        ...     print(ac.get_group(element_ids[0]))
    """

def set_subgroup(element_id_list: list[ElementId], subgroup: str) -> None:
    """Set the subgroup of the given elements.

    The subgroup is a free text attribute that refines the group. The same value is written to every
    listed element. To offer a value in the subgroup list without assigning it, use
    `attribute_controller.add_item_to_subgroup_list()`. Read it back with
    `attribute_controller.get_subgroup()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        subgroup: The subgroup text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_subgroup(element_ids, 'Axis 3')
        >>> if element_ids:
        ...     print(ac.get_subgroup(element_ids[0]))
    """

def set_comment(element_id_list: list[ElementId], comment: str) -> None:
    """Set the comment of the given elements.

    The comment is a free text attribute shown with the element's attributes and available in lists.
    The same value is written to every listed element. To offer a value in the comment list without
    assigning it, use `attribute_controller.add_item_to_comment_list()`. Read it back with
    `attribute_controller.get_comment()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        comment: The comment text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_comment(element_ids, 'check on site')
        >>> if element_ids:
        ...     print(ac.get_comment(element_ids[0]))
    """

def set_user_attribute(element_id_list: list[ElementId], number: UserAttributeId, user_attribute: str) -> None:
    """Set one user attribute of the given elements.

    User attributes are numbered free-text fields (1 to 999) whose titles are defined per document.
    The same text is written to every listed element. Nothing is changed if number is greater than
    999. Read it back with `attribute_controller.get_user_attribute()`; get or set the field title
    with `attribute_controller.get_user_attribute_name()` and
    `attribute_controller.set_user_attribute_name()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        number: User attribute number, 1 to 999. Numbers above 999 are ignored.
        user_attribute: The text to store in that user attribute.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_user_attribute(element_ids, 5, 'checked')
        >>> if element_ids:
        ...     print(ac.get_user_attribute(element_ids[0], 5))
    """

def set_sku(element_id_list: list[ElementId], sku: str) -> None:
    """Set the SKU (article code) of the given elements.

    The SKU is the article number attribute used for ordering and lists. The same value is written
    to every listed element. To offer a value in the SKU list without assigning it, use
    `attribute_controller.add_item_to_sku_list()`. Read it back with
    `attribute_controller.get_sku()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        sku: The SKU text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_sku(element_ids, 'KVH-60x120')
        >>> if element_ids:
        ...     print(ac.get_sku(element_ids[0]))
    """

def set_production_number(element_id_list: list[ElementId], production_number: UnsignedInt) -> None:
    """Set the production list number of the given elements.

    The production list number is the position number used in production lists. Elements that carry
    no production data are skipped. Read it back with
    `attribute_controller.get_production_number()`. `attribute_controller.set_container_number()`
    writes to the same field.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        production_number: The production list number to assign to every element (non-negative
            integer).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_production_number(element_ids, 12)
        >>> if element_ids:
        ...     print(ac.get_production_number(element_ids[0]))
    """

def set_part_number(element_id_list: list[ElementId], part_number: UnsignedInt) -> None:
    """Set the part list number of the given elements.

    The part list number is the position number used in part (timber) lists. Elements that carry no
    part number data are skipped. Read it back with `attribute_controller.get_part_number()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        part_number: The part list number to assign to every element (non-negative integer).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_part_number(element_ids, 7)
        >>> if element_ids:
        ...     print(ac.get_part_number(element_ids[0]))
    """

def set_additional_data(element_id_list: list[ElementId], data_id: str, data_text: str) -> None:
    """Store a text under a data ID on the given elements.

    Additional data lets scripts attach their own key/value text to elements, independent of the
    numbered user attributes. The data ID identifies the entry; an existing entry with the same data
    ID on an element is overwritten. The data is written directly to the document database. Read it
    back with `attribute_controller.get_additional_data()`, list the keys with
    `attribute_controller.get_additional_data_keys()` and remove an entry with
    `attribute_controller.delete_additional_data()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        data_id: Key identifying the data entry, e.g. 'my_script.status'. Use a prefix that is
            unique to your script.
        data_text: The text to store.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_additional_data(element_ids, 'my_script.status', 'done')
        >>> if element_ids:
        ...     print(ac.get_additional_data(element_ids[0], 'my_script.status'))
    """

def delete_additional_data(element_id_list: list[ElementId], data_id: str) -> None:
    """Delete the data stored under a data ID from the given elements.

    Removes the entry that `attribute_controller.set_additional_data()` stored under this key.
    Elements without an entry for the data ID are left unchanged. List the existing keys with
    `attribute_controller.get_additional_data_keys()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        data_id: Key of the data entry to delete.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.delete_additional_data(element_ids, 'my_script.status')
    """

def set_user_attribute_name(number: UserAttributeId, user_attribute_name: str) -> None:
    """Set the display name (title) of a user attribute.

    The title is a document-wide label for the numbered user attribute, not a value on elements; if
    the attribute has no title yet, one is created. Nothing is changed if number is greater than 999
    or the document has no attribute data. Read it back with
    `attribute_controller.get_user_attribute_name()`.

    Parameters:
        number: User attribute number, 1 to 999. Numbers above 999 are ignored.
        user_attribute_name: The new title of the user attribute.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.set_user_attribute_name(5, 'Inspection status')
        >>> print(ac.get_user_attribute_name(5))
    """

def set_process_type_and_extended_settings_from_name(element_id_list: list[ElementId]) -> None:
    """Apply the process type and extended settings stored for each element's name.

    Every name in the document's name list carries a process type, extended settings, machine and
    cutting-set settings and an IFC type. This function copies the settings stored for each
    element's current name onto the element, for example after you changed them with
    `attribute_controller.set_name_process_type()` or
    `attribute_controller.set_name_extended_settings()`. Elements without a name are skipped. No
    undo step is created.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_process_type_and_extended_settings_from_name(element_ids)
    """

def set_name_process_type(name: str, process_type: process_type) -> None:
    """Set the process type stored for an element name in the name list.

    Only the name list entry is changed. Existing elements keep their current process type until
    `attribute_controller.set_process_type_and_extended_settings_from_name()` is called for them.
    Nothing happens if the name is not in the list. Read it back with
    `attribute_controller.get_name_process_type()`.

    Parameters:
        name: Exact name of an existing entry in the name list, e.g. from
            `attribute_controller.get_name_list_items()`. The comparison is exact.
        process_type: The process type to store for that name, e.g. a `cadwork.process_type` with
            `set_stud()` called.

    Examples:
        >>> import cadwork
        >>> import attribute_controller as ac

        >>> process = cadwork.process_type()
        >>> process.set_stud()
        >>> if 'Stud' in ac.get_name_list_items():
        ...     ac.set_name_process_type('Stud', process)
    """

def set_name_extended_settings(name: str, extended_settings: extended_settings) -> None:
    """Set the extended settings stored for an element name in the name list.

    Only the name list entry is changed. Existing elements keep their current settings until
    `attribute_controller.set_process_type_and_extended_settings_from_name()` is called for them.
    Nothing happens if the name is not in the list. Read it back with
    `attribute_controller.get_name_extended_settings()`.

    Parameters:
        name: Exact name of an existing entry in the name list, e.g. from
            `attribute_controller.get_name_list_items()`.
        extended_settings: The extended settings to store for that name. All flags are written, so
            start from `attribute_controller.get_name_extended_settings()` and modify.

    Examples:
        >>> import attribute_controller as ac

        >>> name = 'Stud'
        >>> if name in ac.get_name_list_items():
        ...     settings = ac.get_name_extended_settings(name)
        ...     settings.set_chief_element(True)
        ...     ac.set_name_extended_settings(name, settings)
    """

def set_output_type(element_id_list: list[ElementId], process_type: process_type) -> None:
    """Set the output (process) type of the given elements.

    The output type tells production which kind of component an element is (for example stud, purlin
    or rafter). Elements without production data are skipped. Read it back with
    `attribute_controller.get_output_type()`. The wall, floor and roof classification functions also
    adjust the output type.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        process_type: The process type to assign to every element, e.g. a `cadwork.process_type`
            with `set_stud()` called.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> process = cadwork.process_type()
        >>> process.set_stud()
        >>> ac.set_output_type(element_ids, process)
    """

def set_extended_settings(element_id_list: list[ElementId], extended_settings: extended_settings) -> None:
    """Write the extended settings to the given elements.

    Extended settings are on/off flags that decide in which exports and machine outputs an element
    takes part. All flags of the passed object are written to every element, overwriting flags you
    did not touch, so start from `attribute_controller.get_extended_settings()`. Elements without
    production data are skipped. No undo step is created.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        extended_settings: The settings to write; take them from
            `attribute_controller.get_extended_settings()` and modify.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     settings = ac.get_extended_settings(element_id)
        ...     settings.set_chief_element(True)
        ...     ac.set_extended_settings([element_id], settings)
    """

def set_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed wall.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_framed_wall()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_wall(element_ids)
        >>> if element_ids:
        ...     print(ac.is_framed_wall(element_ids[0]))
    """

def set_floor(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed floor.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_framed_floor()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_floor(element_ids)
        >>> if element_ids:
        ...     print(ac.is_framed_floor(element_ids[0]))
    """

def set_opening(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as openings.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. Openings (cut-outs for
    doors and windows) are excluded from the VBA calculation. If an element was a wall, floor or
    roof, its wall cuts and related wall data are removed and its output type is cleared. Check the
    result with `attribute_controller.is_opening()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_opening(element_ids)
        >>> if element_ids:
        ...     print(ac.is_opening(element_ids[0]))
    """

def set_fastening_attribute(element_id_list: list[ElementId], value: str) -> None:
    """Set the fastening attribute of the given elements.

    The fastening attribute is a panel prefabrication setting stored as text per element. The value
    is only written if the panel prefabrication analysis configuration can be loaded; otherwise the
    call has no effect. Read it back with `attribute_controller.get_fastening_attribute()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        value: The fastening attribute text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_fastening_attribute(element_ids, 'Config A')
        >>> if element_ids:
        ...     print(ac.get_fastening_attribute(element_ids[0]))
    """

def set_element_material(element_id_list: list[ElementId], material: MaterialId) -> None:
    """Set the material of the given elements.

    Elements that cannot carry a material (for example auxiliary objects, containers, export solids,
    dimensions and lines other than installations) are skipped, unless material is 0, which clears
    the material of any element. The ID is not checked against the material list. Read the material
    back with `attribute_controller.get_element_material_name()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        material: Material ID, e.g. from `material_controller.get_material_id()`, or 0 to remove the
            material.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import material_controller as mtc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> material_id = mtc.get_material_id('C24')
        >>> ac.set_element_material(element_ids, material_id)
    """

def set_assembly_number(element_id_list: list[ElementId], assembly_number: str) -> None:
    """Set the assembly number of the given elements.

    The assembly number groups elements into assemblies in lists. Elements without production data
    are skipped. Read it back with `attribute_controller.get_assembly_number()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        assembly_number: The assembly number text to assign to every element.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_assembly_number(element_ids, 'W-01')
        >>> if element_ids:
        ...     print(ac.get_assembly_number(element_ids[0]))
    """

def set_list_quantity(element_id_list: list[ElementId], list_quantity: UnsignedInt) -> None:
    """Set the quantity used in lists for the given elements.

    The list quantity is the piece count of an element in production and part lists. Elements
    without production data are skipped. Read it back with
    `attribute_controller.get_list_quantity()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        list_quantity: The quantity to assign to every element (non-negative integer).

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_list_quantity(element_ids, 4)
        >>> if element_ids:
        ...     print(ac.get_list_quantity(element_ids[0]))
    """

def set_layer_settings(element_id_list: list[ElementId], layer_settings: layer_settings) -> None:
    """Set the prefab-layer output behavior of one layer on the given elements.

    In panel prefabrication each layer of an element can be output with dimensions, without
    dimensions or not at all. The layer number and output mode are taken from the layer_settings
    object. If several modes are set, without-output wins over with-dimensions, which wins over
    without-dimensions; the attributes-output flag is applied for both dimension modes. Nothing
    changes if no mode was set or the layer number is out of range. No undo step is created. Check
    the result with `attribute_controller.get_prefab_layer_with_dimensions()` and the related
    getters.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        layer_settings: A `cadwork.layer_settings` object. Layer 0 is the element's own layer, 1 to
            14 the reference side, -1 to -14 the opposite side. Set one output mode
            (`set_without_output()`, `set_with_dimensions_output()` or
            `set_without_dimensions_output()`) and optionally `set_with_attributes_output()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> settings = cadwork.layer_settings()
        >>> settings.set_layer(1)
        >>> settings.set_with_dimensions_output()
        >>> settings.set_with_attributes_output()
        >>> ac.set_layer_settings(element_ids, settings)
    """

def set_ignore_in_vba_calculation(element_id_list: list[ElementId], ignore: bool) -> None:
    """Set whether the given elements are ignored in the VBA calculation.

    Elements flagged as ignored are left out of the VBA calculation. Elements without production
    data are skipped. Every ID must refer to an existing element. Read the flag back with
    `attribute_controller.get_ignore_in_vba_calculation()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. All IDs must exist; an empty
            list does nothing.
        ignore: True to ignore the elements in the VBA calculation, False to include them.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_ignore_in_vba_calculation(element_ids, True)
        >>> if element_ids:
        ...     print(ac.get_ignore_in_vba_calculation(element_ids[0]))
    """

def clear_errors() -> None:
    """Clear the stored error messages of the attribute controller.

    Some attribute functions, for example `attribute_controller.delete_item_from_comment_list()`,
    record the reason for a failure in an internal error list of this controller. This empties that
    list.

    Examples:
        >>> import attribute_controller as ac

        >>> if not ac.delete_item_from_comment_list('obsolete'):
        ...     ac.clear_errors()
    """

def set_reference_wall_2dc(element_id_list: list[ElementId], _2dc_file_path: str) -> None:
    """Replace the wall definition of the given walls with one read from a 2dc file.

    A 2dc file describes an architectural wall (its layers and thickness). Only wall elements in the
    list are changed; if there is none, nothing happens. The wall definition is read from the file
    and stored in the document, and each wall takes the name, color and material from the file's
    bounding wall rectangle. The wall thickness is changed to that rectangle's width, as an undo
    step. Check with `attribute_controller.is_architecture_wall_2dc()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist or are
            not walls are skipped.
        _2dc_file_path: Path to the 2dc file that defines the wall. Use forward slashes.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_reference_wall_2dc(element_ids, 'C:/data/wall_type_a.2dc')
    """

def get_user_attribute_count() -> UnsignedInt:
    """Return the number of user attributes in the document.

    User attributes are the numbered text fields that can be set per element with
    `attribute_controller.set_user_attribute()`. The count comes from the document's attribute data.

    Examples:
        >>> import attribute_controller as ac

        >>> count = ac.get_user_attribute_count()
        >>> print(count)

    Returns:
        Number of user attributes, 0 if the attribute data is unavailable.
    """

def set_standard_part(element_id_list: list[ElementId]) -> None:
    """Remove the wall, floor, roof or opening classification from the given elements.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. Afterwards the elements are
    ordinary parts again and 'ignore in VBA calculation' is cleared. If an element was a wall, floor
    or roof, its wall cuts and related wall data are removed and its output type is cleared.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_standard_part(element_ids)
        >>> if element_ids:
        ...     print(ac.is_wall(element_ids[0]))
    """

def set_solid_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood wall.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_solid_wall()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_solid_wall(element_ids)
        >>> if element_ids:
        ...     print(ac.is_solid_wall(element_ids[0]))
    """

def set_log_wall(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as log wall.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_log_wall()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_log_wall(element_ids)
        >>> if element_ids:
        ...     print(ac.is_log_wall(element_ids[0]))
    """

def set_solid_floor(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood floor.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_solid_floor()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_solid_floor(element_ids)
        >>> if element_ids:
        ...     print(ac.is_solid_floor(element_ids[0]))
    """

def set_roof(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as framed roof.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_framed_roof()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_roof(element_ids)
        >>> if element_ids:
        ...     print(ac.is_framed_roof(element_ids[0]))
    """

def set_solid_roof(element_id_list: list[ElementId]) -> None:
    """Mark the given elements as solid wood roof.

    Only elements of the beam class (beams, panels and other elements with a beam-like
    cross-section) are changed; all other elements are skipped silently. The element's output type
    is set to match and a previously assigned wall, floor or roof classification is replaced. Check
    the result with `attribute_controller.is_solid_roof()`; remove a classification with
    `attribute_controller.set_standard_part()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_solid_roof(element_ids)
        >>> if element_ids:
        ...     print(ac.is_solid_roof(element_ids[0]))
    """

def get_node_symbol(element_id: ElementId) -> node_symbol:
    """Return the node symbol of an element.

    The node symbol is the marker shape drawn at the position of a node element. Set it with
    `attribute_controller.set_node_symbol()`; check that an element is a node with
    `attribute_controller.is_node()`.

    Parameters:
        element_id: ID of the element to query, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     symbol = ac.get_node_symbol(element_ids[0])
        ...     if symbol == -1:
        ...         print('no node symbol')
        ...     else:
        ...         print(symbol)

    Returns:
        The node symbol of the element (a `cadwork.node_symbol` value), or -1 if the element does
        not exist or has no node symbol data.
    """

def set_node_symbol(element_id_list: list[ElementId], symbol: node_symbol) -> None:
    """Set the node symbol of the given elements.

    The node symbol is the marker shape drawn at a node element's position. Elements without node
    data are skipped. The value is not range-checked. Read it back with
    `attribute_controller.get_node_symbol()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        symbol: A `cadwork.node_symbol` member, e.g. `cadwork.node_symbol.Circle`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_node_symbol(element_ids, cadwork.node_symbol.Circle)
    """

def enable_attribute_display() -> None:
    """Turn on the display of element attributes in the view.

    Attribute display shows the configured attribute labels next to the elements in the model view.
    This rebuilds the labels of all construction elements, updates the toolbar and redraws the view.
    Check the state with `attribute_controller.is_attribute_display_enabled()`; configure what is
    shown with the `attribute_controller.set_attribute_display_settings_for_*` functions.

    Examples:
        >>> import attribute_controller as ac

        >>> if not ac.is_attribute_display_enabled():
        ...     ac.enable_attribute_display()
    """

def disable_attribute_display() -> None:
    """Turn off the display of element attributes in the view.

    Removes the attribute labels shown next to the elements. This rebuilds the labels of all
    construction elements, updates the toolbar and redraws the view. Check the state with
    `attribute_controller.is_attribute_display_enabled()`.

    Examples:
        >>> import attribute_controller as ac

        >>> if ac.is_attribute_display_enabled():
        ...     ac.disable_attribute_display()
    """

def is_attribute_display_enabled() -> bool:
    """Check whether element attributes are displayed in the view.

    Reflects the current on/off state of the attribute display option of the application. Switch it
    with `attribute_controller.enable_attribute_display()` and
    `attribute_controller.disable_attribute_display()`.

    Examples:
        >>> import attribute_controller as ac

        >>> print('attributes shown' if ac.is_attribute_display_enabled() else 'hidden')

    Returns:
        True if attribute display is on, False otherwise.
    """

def update_auto_attribute() -> None:
    """Recalculate the auto-filled attributes of all visible elements.

    Auto attributes are attributes whose value cadwork fills in automatically from the element.
    Hidden elements are not updated. Both manually and automatically configured auto attributes are
    recalculated. Read values afterwards with `attribute_controller.get_auto_attribute()`.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.update_auto_attribute()
    """

def set_additional_guid(element_id_list: list[ElementId], data_id: str, guid: str) -> None:
    """Store a GUID under a data ID on the given elements.

    Like `attribute_controller.set_additional_data()` but for a GUID value, for example to link an
    element to an external system. An existing GUID with the same data ID on an element is
    overwritten. The data is written directly to the document database. Read it back with
    `attribute_controller.get_additional_guid()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        data_id: Key identifying the GUID entry, e.g. 'my_script.external_id'.
        guid: The GUID as text, e.g. '123e4567-e89b-12d3-a456-426614174000'.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> guid = '123e4567-e89b-12d3-a456-426614174000'
        >>> ac.set_additional_guid(element_ids, 'my_script.external_id', guid)
    """

def add_item_to_group_list(item: str) -> None:
    """Add an entry to the document's list of group values.

    The list holds the group values known to the document, so a value can be offered before any
    element uses it. Only the list is changed; no element is modified. Read the list with
    `attribute_controller.get_group_list_items()`; assign a value to elements with
    `attribute_controller.set_group()`.

    Parameters:
        item: The group text to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_group_list('Ground floor')
        >>> print(ac.get_group_list_items())
    """

def add_item_to_subgroup_list(item: str) -> None:
    """Add an entry to the document's list of subgroup values.

    The list holds the subgroup values known to the document, so a value can be offered before any
    element uses it. Only the list is changed; no element is modified. Read the list with
    `attribute_controller.get_subgroup_list_items()`; assign a value to elements with
    `attribute_controller.set_subgroup()`.

    Parameters:
        item: The subgroup text to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_subgroup_list('Axis 3')
        >>> print(ac.get_subgroup_list_items())
    """

def add_item_to_comment_list(item: str) -> None:
    """Add an entry to the document's list of comment values.

    The list holds the comment values known to the document, so a value can be offered before any
    element uses it. Only the list is changed; no element is modified. Read the list with
    `attribute_controller.get_comment_list_items()`; assign a value to elements with
    `attribute_controller.set_comment()`.

    Parameters:
        item: The comment text to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_comment_list('check on site')
        >>> print(ac.get_comment_list_items())
    """

def add_item_to_sku_list(item: str) -> None:
    """Add an entry to the document's list of SKU values.

    The list holds the SKU values known to the document, so a value can be offered before any
    element uses it. Only the list is changed; no element is modified. Read the list with
    `attribute_controller.get_sku_list_items()`; assign a value to elements with
    `attribute_controller.set_sku()`.

    Parameters:
        item: The SKU text to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_sku_list('KVH-60x120')
        >>> print(ac.get_sku_list_items())
    """

def add_item_to_user_attribute_list(attribute_number: UserAttributeId, item: str) -> None:
    """Add an entry to the list of values of one user attribute.

    The list holds the values known for that user attribute, so a value can be offered before any
    element uses it. Only the list is changed; no element is modified. Read the list with
    `attribute_controller.get_user_attribute_list_items()`; assign a value to elements with
    `attribute_controller.set_user_attribute()`.

    Parameters:
        attribute_number: User attribute number, 1 to 999.
        item: The text to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_user_attribute_list(5, 'checked')
        >>> print(ac.get_user_attribute_list_items(5))
    """

def set_container_number(element_id_list: list[ElementId], number: UnsignedInt) -> None:
    """Set the container number of the given elements.

    The number is stored in the element's production list number after a fixed container offset
    (5,000,000) is added, so it replaces the production number. Elements without production data are
    skipped. Read it back with `attribute_controller.get_container_number()` or, with prefix,
    `attribute_controller.get_container_number_with_prefix()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped; an empty list does nothing.
        number: The container number to assign (non-negative integer). The offset is added
            automatically; do not add it yourself.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_container_number(element_ids, 3)
        >>> if element_ids:
        ...     print(ac.get_container_number(element_ids[0]))
    """

def get_name_list_items() -> list[str]:
    """Return all names in the document's name list.

    The name list holds the names that can be assigned to elements with
    `attribute_controller.set_name()`. An empty first entry (the blank name) is left out. Add
    entries with `attribute_controller.add_item_to_name_list()`; to filter by element type use
    `attribute_controller.get_name_list_items_by_element_type()`.

    Examples:
        >>> import attribute_controller as ac

        >>> for name in ac.get_name_list_items():
        ...     print(name)

    Returns:
        List of name strings; an empty list if there are none or the attribute data is unavailable.
    """

def add_item_to_name_list(item: str) -> None:
    """Add a name to the document's name list.

    The name is added with the default element type, default settings and no process type. No
    element is modified. Set the stored process type and settings afterwards with
    `attribute_controller.set_name_process_type()` and
    `attribute_controller.set_name_extended_settings()`; list names with
    `attribute_controller.get_name_list_items()`.

    Parameters:
        item: The name to add.

    Examples:
        >>> import attribute_controller as ac

        >>> ac.add_item_to_name_list('Stud')
        >>> print('Stud' in ac.get_name_list_items())
    """

def delete_item_from_comment_list(item: str) -> bool:
    """Delete an entry from the document's list of comment values.

    Fails if the entry does not exist or is still used as the comment of at least one element; the
    reason is recorded in the controller's error messages and written to the API log. Elements are
    never modified, so reassign their comments first with `attribute_controller.set_comment()`. Add
    entries with `attribute_controller.add_item_to_comment_list()`.

    Parameters:
        item: The comment text to delete.

    Examples:
        >>> import attribute_controller as ac

        >>> if not ac.delete_item_from_comment_list('obsolete'):
        ...     print('not deleted: missing or still in use')

    Returns:
        True if the entry was deleted, False if it was not found, is still in use or the attribute
        data is unavailable.
    """

def delete_item_from_group_list(item: str) -> bool:
    """Delete an unused entry from the group list of the document.

    Removes the entry from the document's list of group values, so it is no longer offered for new
    assignments. Deletion is refused when the entry does not exist or is still assigned to the group
    of at least one element (change those elements first with `attribute_controller.set_group()`);
    the reason is also written to the API log. List the current entries with
    `attribute_controller.get_group_list_items()`.

    Parameters:
        item: Exact text of the group list entry to delete (case-sensitive match against
            `get_group_list_items()`).

    Examples:
        >>> import attribute_controller as ac

        >>> if 'Old group' in ac.get_group_list_items():
        ...     if not ac.delete_item_from_group_list('Old group'):
        ...         print('Still used by an element, not deleted')

    Returns:
        True if the entry was deleted. False if it was not found, is still in use or the attribute
        data is unavailable.
    """

def delete_item_from_sku_list(item: str) -> bool:
    """Delete an unused entry from the SKU list of the document.

    Removes the entry from the document's list of SKU (article code) values, so it is no longer
    offered for new assignments. Deletion is refused when the entry does not exist or is still
    assigned to at least one element (change those elements first with
    `attribute_controller.set_sku()`); the reason is also written to the API log. List the current
    entries with `attribute_controller.get_sku_list_items()`.

    Parameters:
        item: Exact text of the SKU list entry to delete (case-sensitive match against
            `get_sku_list_items()`).

    Examples:
        >>> import attribute_controller as ac

        >>> if 'ART-0042' in ac.get_sku_list_items():
        ...     deleted = ac.delete_item_from_sku_list('ART-0042')
        ...     print('deleted' if deleted else 'still in use')

    Returns:
        True if the entry was deleted. False if it was not found, is still in use or the attribute
        data is unavailable.
    """

def delete_item_from_subgroup_list(item: str) -> bool:
    """Delete an unused entry from the subgroup list of the document.

    Removes the entry from the document's list of subgroup values, so it is no longer offered for
    new assignments. Deletion is refused when the entry does not exist or is still assigned to the
    subgroup of at least one element (change those elements first with
    `attribute_controller.set_subgroup()`); the reason is also written to the API log. List the
    current entries with `attribute_controller.get_subgroup_list_items()`.

    Parameters:
        item: Exact text of the subgroup list entry to delete (case-sensitive match against
            `get_subgroup_list_items()`).

    Examples:
        >>> import attribute_controller as ac

        >>> if 'Old subgroup' in ac.get_subgroup_list_items():
        ...     deleted = ac.delete_item_from_subgroup_list('Old subgroup')
        ...     print('deleted' if deleted else 'still in use')

    Returns:
        True if the entry was deleted. False if it was not found, is still in use or the attribute
        data is unavailable.
    """

def delete_item_from_user_attribute_list(attribute_number: UserAttributeId, item: str) -> bool:
    """Delete an unused entry from the value list of one user attribute.

    Each user attribute has its own list of predefined values. This removes one value from the list
    of the given attribute so it is no longer offered for new assignments. Deletion is refused when
    the entry does not exist or is still assigned to that user attribute on at least one element
    (change those elements first with `attribute_controller.set_user_attribute()`); the reason is
    also written to the API log. List the current entries with
    `attribute_controller.get_user_attribute_list_items()`.

    Parameters:
        attribute_number: Number of the user attribute whose list the entry is removed from (1 to
            999).
        item: Exact text of the list entry to delete (case-sensitive match against the entries of
            that attribute).

    Examples:
        >>> import attribute_controller as ac

        >>> if 'draft' in ac.get_user_attribute_list_items(5):
        ...     deleted = ac.delete_item_from_user_attribute_list(5, 'draft')
        ...     print('deleted' if deleted else 'still in use')

    Returns:
        True if the entry was deleted. False if it was not found, is still in use or the attribute
        data is unavailable.
    """

def set_attribute_display_settings_for_2d(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for normal 2D exports.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    normal 2D exports; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_2d()`, change the values
    you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_2d()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_2d(settings)
    """

def set_attribute_display_settings_for_2d_with_layout(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for 2D exports with layout frame.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for 2D
    exports with layout frame; it is not tied to single elements. Both the absolute value (mm) and
    the percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain
    the object with `attribute_controller.get_attribute_display_settings_for_2d_with_layout()`,
    change the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_2d_with_layout()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d_with_layout()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_2d_with_layout(settings)
    """

def set_attribute_display_settings_for_2d_without_layout(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for 2D exports without layout frame.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for 2D
    exports without layout frame; it is not tied to single elements. Both the absolute value (mm)
    and the percentage value are stored, and the display is refreshed if automatic refresh is on.
    Obtain the object with
    `attribute_controller.get_attribute_display_settings_for_2d_without_layout()`, change the values
    you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_2d_without_layout()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d_without_layout()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_2d_without_layout(settings)
    """

def set_attribute_display_settings_for_3d(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for the 3D view.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    the 3D view; it is not tied to single elements. Both the absolute value (mm) and the percentage
    value are stored, and the display is refreshed if automatic refresh is on. Obtain the object
    with `attribute_controller.get_attribute_display_settings_for_3d()`, change the values you need
    and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_3d()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_3d()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_3d(settings)
    """

def set_attribute_display_settings_for_container(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for containers.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    containers; it is not tied to single elements. Both the absolute value (mm) and the percentage
    value are stored, and the display is refreshed if automatic refresh is on. Obtain the object
    with `attribute_controller.get_attribute_display_settings_for_container()`, change the values
    you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_container()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_container()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_container(settings)
    """

def set_attribute_display_settings_for_export_solid(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for solid exports.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    solid exports; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_export_solid()`, change the
    values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_export_solid()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_export_solid()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_export_solid(settings)
    """

def set_attribute_display_settings_for_framed_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for axes of framed walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    axes of framed walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_framed_wall_axis()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_framed_wall_axis()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_axis()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_framed_wall_axis(settings)
    """

def set_attribute_display_settings_for_framed_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for beams of framed walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    beams of framed walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_framed_wall_beam()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_framed_wall_beam()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_beam()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_framed_wall_beam(settings)
    """

def set_attribute_display_settings_for_framed_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for openings of framed walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    openings of framed walls; it is not tied to single elements. Both the absolute value (mm) and
    the percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain
    the object with `attribute_controller.get_attribute_display_settings_for_framed_wall_opening()`,
    change the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_framed_wall_opening()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_opening()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_framed_wall_opening(settings)
    """

def set_attribute_display_settings_for_framed_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for panels of framed walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    panels of framed walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_framed_wall_panel()`,
    change the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_framed_wall_panel()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_panel()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_framed_wall_panel(settings)
    """

def set_attribute_display_settings_for_log_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for axes of log walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    axes of log walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_log_wall_axis()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_log_wall_axis()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_axis()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_log_wall_axis(settings)
    """

def set_attribute_display_settings_for_log_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for beams of log walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    beams of log walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_log_wall_beam()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_log_wall_beam()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_beam()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_log_wall_beam(settings)
    """

def set_attribute_display_settings_for_log_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for openings of log walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    openings of log walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_log_wall_opening()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_log_wall_opening()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_opening()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_log_wall_opening(settings)
    """

def set_attribute_display_settings_for_log_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for panels of log walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    panels of log walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_log_wall_panel()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_log_wall_panel()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_panel()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_log_wall_panel(settings)
    """

def set_attribute_display_settings_for_machine(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for machine output.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    machine output; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_machine()`, change the
    values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_machine()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_machine()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_machine(settings)
    """

def set_attribute_display_settings_for_nesting_element(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for nesting elements.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    nesting elements; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_nesting_element()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_nesting_element()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_nesting_element()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_nesting_element(settings)
    """

def set_attribute_display_settings_for_nesting_volume(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for nesting volumes.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    nesting volumes; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_nesting_volume()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_nesting_volume()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_nesting_volume()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_nesting_volume(settings)
    """

def set_attribute_display_settings_for_solid_wall_axis(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for axes of solid walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    axes of solid walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_solid_wall_axis()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_solid_wall_axis()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_axis()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_solid_wall_axis(settings)
    """

def set_attribute_display_settings_for_solid_wall_beam(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for beams of solid walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    beams of solid walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_solid_wall_beam()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_solid_wall_beam()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_beam()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_solid_wall_beam(settings)
    """

def set_attribute_display_settings_for_solid_wall_opening(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for openings of solid walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    openings of solid walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_solid_wall_opening()`,
    change the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_solid_wall_opening()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_opening()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_solid_wall_opening(settings)
    """

def set_attribute_display_settings_for_solid_wall_panel(settings: attribute_display_settings) -> None:
    """Set where attribute text is placed for panels of solid walls.

    Attribute text is the text label showing element attributes (name, group, ...) next to an
    element. This stores the text position of the settings object as the program-wide setting for
    panels of solid walls; it is not tied to single elements. Both the absolute value (mm) and the
    percentage value are stored, and the display is refreshed if automatic refresh is on. Obtain the
    object with `attribute_controller.get_attribute_display_settings_for_solid_wall_panel()`, change
    the values you need and pass it back.

    Parameters:
        settings: Settings object, preferably the one returned by
            `attribute_controller.get_attribute_display_settings_for_solid_wall_panel()` with
            `set_text_position_absolute()` (mm) and `set_text_position_percentage()` changed as
            needed.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_panel()
        >>> settings.set_text_position_percentage(50)
        >>> ac.set_attribute_display_settings_for_solid_wall_panel(settings)
    """

def set_framed_floor(element_id_list: list[ElementId]) -> None:
    """Classify elements as framed floor.

    Sets the cover type of each element to framed floor and gives it the matching panel-cover output
    type, so cadwork treats it as part of a timber frame floor. Only elements of the beam class
    (beams, panels and other elements with a beam-like cross-section) are changed; other element
    types, invalid element IDs and an empty list are skipped silently. Identical to
    `attribute_controller.set_floor()`. Use `attribute_controller.set_solid_floor()` for the solid
    variant and `attribute_controller.set_standard_part()` to remove the classification.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_framed_floor(element_ids)
    """

def set_framed_roof(element_id_list: list[ElementId]) -> None:
    """Classify elements as framed roof.

    Sets the cover type of each element to framed roof and gives it the matching panel-cover output
    type, so cadwork treats it as part of a timber frame roof. Only elements of the beam class
    (beams, panels and other elements with a beam-like cross-section) are changed; other element
    types, invalid element IDs and an empty list are skipped silently. Identical to
    `attribute_controller.set_roof()`. Use `attribute_controller.set_solid_roof()` for the solid
    variant and `attribute_controller.set_standard_part()` to remove the classification.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_framed_roof(element_ids)
    """

def set_framed_wall(element_id_list: list[ElementId]) -> None:
    """Classify elements as framed wall.

    Sets the cover type of each element to framed wall and gives it the matching panel-cover output
    type, so cadwork treats it as part of a timber frame wall. Only elements of the beam class
    (beams, panels and other elements with a beam-like cross-section) are changed; other element
    types, invalid element IDs and an empty list are skipped silently. Identical to
    `attribute_controller.set_wall()`. Use `attribute_controller.set_solid_wall()` for the solid
    variant and `attribute_controller.set_standard_part()` to remove the classification.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ac.set_framed_wall(element_ids)
    """

def get_name_list_items_by_element_type(element_type: element_type) -> list[str]:
    """Return the entries of the document's name list for one element type.

    The name list holds the predefined element names of the document; each name is registered for
    one or more element types. This returns the names matching the given type, in the order of the
    name list. Use `attribute_controller.get_name_list_items()` for all names regardless of type and
    `attribute_controller.get_element_type()` to obtain a type from an element.

    Parameters:
        element_type: Element type to filter by, e.g. the result of
            `attribute_controller.get_element_type()` for an existing element.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     element_type = ac.get_element_type(element_ids[0])
        ...     print(ac.get_name_list_items_by_element_type(element_type))

    Returns:
        List of name strings; an empty list if no name is registered for the type.
    """

def get_name(element_id: ElementId) -> str:
    """Return the name of an element.

    Reads the name attribute that is shown in element lists and labels. For imported exchange
    objects (not yet converted to native cadwork elements) the name is taken from the imported
    product structure instead. Set it with `attribute_controller.set_name()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_name(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Name of the element. An empty string if the element ID is invalid or the element has no
        name.
    """

def get_group(element_id: ElementId) -> str:
    """Return the group text of an element.

    The group is a free text attribute used to organise elements, typically together with the
    subgroup. Set it with `attribute_controller.set_group()`; the values already used in the
    document are listed by `attribute_controller.get_group_list_items()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_group(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Group text of the element. An empty string if the element ID is invalid or no group is set.
    """

def get_subgroup(element_id: ElementId) -> str:
    """Return the subgroup text of an element.

    The subgroup is a free text attribute refining the group of an element. Set it with
    `attribute_controller.set_subgroup()`; the values already used in the document are listed by
    `attribute_controller.get_subgroup_list_items()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_subgroup(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Subgroup text of the element. An empty string if the element ID is invalid or no subgroup is
        set.
    """

def get_comment(element_id: ElementId) -> str:
    """Return the comment text of an element.

    The comment is a free text attribute of the element. Set it with
    `attribute_controller.set_comment()`; the values already used in the document are listed by
    `attribute_controller.get_comment_list_items()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_comment(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Comment text of the element. An empty string if the element ID is invalid or no comment is
        set.
    """

def get_user_attribute(element_id: ElementId, number: UserAttributeId) -> str:
    """Return the value of one user attribute of an element.

    User attributes are numbered free text fields (1 to 999) whose titles are defined per document.
    Numbers above 999 are rejected and give an empty string. Set a value with
    `attribute_controller.set_user_attribute()`; get the title of the field with
    `attribute_controller.get_user_attribute_name()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        number: Number of the user attribute to read, 1 to 999.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_user_attribute(element_id, 1)
        ...     title = ac.get_user_attribute_name(1)
        ...     print(element_id, title, repr(value))

    Returns:
        Value of the user attribute as text. An empty string if the element ID is invalid, the
        number is above 999 or the attribute is not set.
    """

def get_sku(element_id: ElementId) -> str:
    """Return the SKU (article code) of an element.

    The SKU is the article or EDP code attribute of the element, used to link it to external article
    data. Set it with `attribute_controller.set_sku()`; the values already used in the document are
    listed by `attribute_controller.get_sku_list_items()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_sku(element_id)
        ...     print(element_id, repr(value))

    Returns:
        SKU text of the element. An empty string if the element ID is invalid or no SKU is set.
    """

def get_production_number(element_id: ElementId) -> UnsignedInt:
    """Return the production list number of an element.

    The production list number is the position number of the element in the production list. Set it
    with `attribute_controller.set_production_number()`; the number in the timber (part) list is
    read with `attribute_controller.get_part_number()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_production_number(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Production list number. 0 if the element ID is invalid, the element kind has no list
        numbers, or no number is assigned.
    """

def get_part_number(element_id: ElementId) -> UnsignedInt:
    """Return the part number (timber list number) of an element.

    The part number is the position number of the element in the timber list. Set it with
    `attribute_controller.set_part_number()`; the production list number is read with
    `attribute_controller.get_production_number()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_part_number(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Part number. 0 if the element ID is invalid, the element kind has no list numbers, or no
        number is assigned.
    """

def get_additional_data(element_id: ElementId, data_id: str) -> str:
    """Return the custom text stored on an element under a key.

    Additional data is custom text that scripts attach to elements under a self-chosen key; it is
    stored in the document together with the element. Write it with
    `attribute_controller.set_additional_data()`, remove it with
    `attribute_controller.delete_additional_data()` and list the keys of an element with
    `attribute_controller.get_additional_data_keys()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        data_id: Key under which the data was stored.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     text = ac.get_additional_data(element_id, 'my_script_note')
        ...     if text:
        ...         print(element_id, text)

    Returns:
        The stored text. An empty string if the element ID is invalid or nothing is stored under the
        key.
    """

def get_user_attribute_name(number: UserAttributeId) -> str:
    """Return the title of a user attribute.

    User attributes are numbered free text fields (1 to 999) of each element. The title is a
    document-wide label for the field, not a value of any element. Change it with
    `attribute_controller.set_user_attribute_name()`; read an element's value with
    `attribute_controller.get_user_attribute()`.

    Parameters:
        number: Number of the user attribute, 1 to 999.

    Examples:
        >>> import attribute_controller as ac

        >>> for number in range(1, 6):
        ...     print(number, repr(ac.get_user_attribute_name(number)))

    Returns:
        Title of the user attribute. An empty string if the number has no title or the attribute
        data is unavailable.
    """

def get_wall_situation(element_id: ElementId) -> str:
    """Return the wall situation text of an element.

    The wall situation is a plain text attribute stored on the element, used with wall elements.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_wall_situation(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Wall situation text. An empty string if the element ID is invalid or none is set.
    """

def get_element_material_name(element_id: ElementId) -> str:
    """Return the name of the material assigned to an element.

    Looks up the material of the element in the document's material list and returns its name.
    Assign a material with `attribute_controller.set_element_material()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_element_material_name(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Material name. An empty string if the element ID is invalid or the element has no material
        name.
    """

def get_prefab_layer(element_id: ElementId) -> str:
    """Return the prefab layer assignment of an element as text.

    Prefab layers are the layers of a prefabricated wall, floor or roof element used for output.
    Layer 0 is the framework layer, positive numbers are layers on the reference side and negative
    numbers layers on the opposite side. The text lists the layers in three groups: those output
    with dimensions, those output without dimensions and those whose attributes are shown. Use
    `attribute_controller.get_prefab_layer_with_dimensions()` and its siblings if you need the layer
    numbers as lists of integers.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_prefab_layer(element_id)
        ...     print(element_id, repr(value))

    Returns:
        String of the form 'WithDimensions[2,1,0] WithoutDimensions[] ShowAttributes[]'; each group
        lists its layer numbers in descending order and is '[]' when empty. An empty string if the
        element ID is invalid or the element kind has no layer data.
    """

def get_machine_calculation_set(element_id: ElementId) -> str:
    """Return the name of the machine calculation set of an element.

    The machine calculation set is the named set of machine calculation settings assigned to the
    element for machine output. Related state is available from
    `attribute_controller.get_machine_calculation_state()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_machine_calculation_set(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Name of the machine calculation set. An empty string if the element ID is invalid or no set
        is assigned.
    """

def get_cutting_set(element_id: ElementId) -> str:
    """Return the name of the cutting set of an element.

    The cutting set is the named set of extra cutting settings assigned to the element for machine
    output.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_cutting_set(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Name of the cutting set. An empty string if the element ID is invalid or no cutting set is
        assigned.
    """

def get_name_process_type(name: str) -> process_type:
    """Return the process type stored for an entry of the name list.

    Each entry of the document's name list can carry a process type, which is applied to elements
    that get that name (see
    `attribute_controller.set_process_type_and_extended_settings_from_name()`). The name is looked
    up in the whole name list, across all element types. Read the extended settings of the same
    entry with `attribute_controller.get_name_extended_settings()`.

    Parameters:
        name: Exact name from the name list, e.g. from `attribute_controller.get_name_list_items()`.

    Examples:
        >>> import attribute_controller as ac

        >>> for name in ac.get_name_list_items():
        ...     process_type = ac.get_name_process_type(name)
        ...     print(name, process_type.is_none())

    Returns:
        Process type of the name. A default process type (value 0) if the name is not found or the
        attribute data is unavailable.
    """

def get_name_extended_settings(name: str) -> extended_settings:
    """Return the extended settings stored for an entry of the name list.

    Each entry of the document's name list can carry extended settings (export and processing
    flags), which are applied to elements that get that name (see
    `attribute_controller.set_process_type_and_extended_settings_from_name()`). The name is looked
    up in the whole name list, across all element types. Read the process type of the same entry
    with `attribute_controller.get_name_process_type()`.

    Parameters:
        name: Exact name from the name list, e.g. from `attribute_controller.get_name_list_items()`.

    Examples:
        >>> import attribute_controller as ac

        >>> for name in ac.get_name_list_items():
        ...     settings = ac.get_name_extended_settings(name)
        ...     print(name, settings.get_mfb_export())

    Returns:
        Extended settings of the name. A default extended_settings object (value 0, no flags set) if
        the name is not found or the attribute data is unavailable.
    """

def get_output_type(element_id: ElementId) -> process_type:
    """Return the output (process) type of an element.

    The output type tells cadwork how the element is treated in output and lists (for example
    purlin, stud or rafter). Change it with `attribute_controller.set_output_type()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     process_type = ac.get_output_type(element_id)
        ...     print(element_id, process_type.is_stud())

    Returns:
        Process type of the element. A default process type (value 0) if the element ID is invalid
        or the element kind has no output type.
    """

def get_extended_settings(element_id: ElementId) -> extended_settings:
    """Return the extended settings of an element.

    Extended settings are a set of per-element export and processing flags (for example MFB or BTL
    export). Change them with `attribute_controller.set_extended_settings()`; the settings defined
    for a name are read with `attribute_controller.get_name_extended_settings()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     settings = ac.get_extended_settings(element_id)
        ...     print(element_id, settings.get_mfb_export())

    Returns:
        Extended settings of the element. A default extended_settings object (value 0, no flags set)
        if the element ID is invalid or the element kind has no such settings.
    """

def get_element_type(element_id: ElementId) -> element_type:
    """Return the element type of an element.

    The element type classifies the element (for example beam, panel, wall, line or node). Test the
    kind with the `is_*()` methods of the returned object. Use the result with
    `attribute_controller.get_name_list_items_by_element_type()` to list the names for that type.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     element_type = ac.get_element_type(element_id)
        ...     print(element_id, element_type.is_wall(), element_type.is_panel())

    Returns:
        The element_type of the element. For an invalid element ID an element_type whose `is_none()`
        is True.
    """

def get_fastening_attribute(element_id: ElementId) -> str:
    """Return the prefab fastening attribute text of an element.

    The fastening attribute is a text attribute used in prefab (MFB) configuration, stored as a
    document-wide list entry that elements refer to. Set it with
    `attribute_controller.set_fastening_attribute()`.

    Parameters:
        element_id: ID of the element to read, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_fastening_attribute(element_id)
        ...     print(element_id, repr(value))

    Returns:
        Fastening attribute text. An empty string if the element ID is invalid, no value is set or
        the attribute data is unavailable.
    """

def get_assembly_number(element_id: ElementId) -> str:
    """Get the assembly list number of an element.

    The assembly number is the element's position number in the assembly list. Returns an empty
    string for an invalid element ID or an element without element data. Change it with
    `attribute_controller.set_assembly_number()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     number = ac.get_assembly_number(element_id)
        ...     print(element_id, number or '(none)')

    Returns:
        The assembly number as text, or an empty string if the element ID is invalid.
    """

def get_list_quantity(element_id: ElementId) -> UnsignedInt:
    """Get the list quantity of an element.

    The list quantity is the number of pieces the element stands for in the lists. Returns 0 for an
    invalid element ID. Change it with `attribute_controller.set_list_quantity()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> total = 0
        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     total += ac.get_list_quantity(element_id)
        >>> print('Total pieces:', total)

    Returns:
        The quantity used in lists, or 0 if the element ID is invalid.
    """

def get_ignore_in_vba_calculation(element_id: ElementId) -> bool:
    """Check whether an element is excluded from the connector (VBA) calculation.

    Elements flagged here are skipped by the connector (VBA) calculation. Pass the ID of an existing
    element, because an invalid ID is not checked and can fail. Set the flag with
    `attribute_controller.set_ignore_in_vba_calculation()`.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.get_ignore_in_vba_calculation(element_id):
        ...         print('Ignored by connector calculation:', element_id)

    Returns:
        True if the element is ignored in the connector calculation, False otherwise (also when the
        element has no element data).
    """

def get_standard_element_name(element_id: ElementId) -> str:
    """Get the standard element name assigned to an element.

    A standard element is a reusable element definition an element can be linked to. Returns an
    empty string if the element has no standard element assigned or the ID is invalid.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     name = ac.get_standard_element_name(element_id)
        ...     if name:
        ...         print(element_id, name)

    Returns:
        The standard element name, or an empty string.
    """

def get_steel_shape_name(element_id: ElementId) -> str:
    """Get the steel shape (profile) name of an element.

    The name is looked up in the steel shape database and returned in the current program language.
    Returns an empty string if the element has no steel shape assigned or the ID is invalid.
    `attribute_controller.is_metal()` tells whether an element has a steel cross-section.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     shape = ac.get_steel_shape_name(element_id)
        ...     if shape:
        ...         print(element_id, shape)

    Returns:
        The steel shape name, or an empty string.
    """

def is_beam(element_id: ElementId) -> bool:
    """Check whether an element belongs to the beam class.

    Beams, panels and other elements with a beam-like cross-section all count; use
    `attribute_controller.is_panel()` to tell panels apart.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_beam(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if it is a beam-class element (beam, panel or other beam-like element), False otherwise
        (including an invalid element ID).
    """

def is_panel(element_id: ElementId) -> bool:
    """Check whether an element is a panel.

    True only for elements with a rectangular panel cross-section. Such elements also count as beam
    class for `attribute_controller.is_beam()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_panel(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a panel, False otherwise (including an invalid element ID).
    """

def is_opening(element_id: ElementId) -> bool:
    """Check whether an element is an opening.

    True for elements marked as an opening. Use `attribute_controller.is_envelope()` to test for any
    building envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_opening(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is an opening, False otherwise (including an invalid element ID).
    """

def is_wall(element_id: ElementId) -> bool:
    """Check whether an element is a wall.

    True for framed, solid and log walls. For one specific wall type use
    `attribute_controller.is_framed_wall()`, `attribute_controller.is_solid_wall()` or
    `attribute_controller.is_log_wall()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_wall(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a wall, False otherwise (including an invalid element ID).
    """

def is_floor(element_id: ElementId) -> bool:
    """Check whether an element is a floor.

    True for framed and solid floors. For one specific type use
    `attribute_controller.is_framed_floor()` or `attribute_controller.is_solid_floor()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_floor(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a floor, False otherwise (including an invalid element ID).
    """

def is_roof(element_id: ElementId) -> bool:
    """Check whether an element is a roof.

    True for framed and solid roofs. For one specific type use
    `attribute_controller.is_framed_roof()` or `attribute_controller.is_solid_roof()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_roof(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a roof, False otherwise (including an invalid element ID).
    """

def is_metal(element_id: ElementId) -> bool:
    """Check whether an element has a steel (metal) cross-section.

    Use `attribute_controller.get_steel_shape_name()` to read the profile name of such an element.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_metal(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element has a metal cross-section, False otherwise (including an invalid element
        ID).
    """

def is_export_solid(element_id: ElementId) -> bool:
    """Check whether an element is an export solid.

    Export solids are solid bodies that are generated for export rather than ordinary timber
    elements.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_export_solid(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is an export solid, False otherwise (including an invalid element ID).
    """

def is_container(element_id: ElementId) -> bool:
    """Check whether an element is a container.

    A container groups other elements and carries its own container number. Read the number with
    `attribute_controller.get_container_number()` or
    `attribute_controller.get_container_number_with_prefix()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_container(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a container, False otherwise (including an invalid element ID).
    """

def is_connector_axis(element_id: ElementId) -> bool:
    """Check whether an element is a connector axis.

    Connector axes are the axis elements that represent connectors (VBA). Use
    `attribute_controller.is_drilling()` for the drilling (bolt) kind of axis.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_connector_axis(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a connector axis, False otherwise (including an invalid element ID).
    """

def is_drilling(element_id: ElementId) -> bool:
    """Check whether an element is a drilling.

    True for axis elements of the drilling (bolt) kind.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_drilling(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a drilling, False otherwise (including an invalid element ID).
    """

def is_node(element_id: ElementId) -> bool:
    """Check whether an element is a node.

    Nodes are point-like construction elements.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_node(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a node, False otherwise (including an invalid element ID).
    """

def is_auxiliary(element_id: ElementId) -> bool:
    """Check whether an element is an auxiliary element.

    Auxiliary elements are construction helpers and not part of the timber construction.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_auxiliary(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is an auxiliary element, False otherwise (including an invalid element
        ID).
    """

def is_roof_surface(element_id: ElementId) -> bool:
    """Check whether an element is a roof surface.

    Roof surfaces are the planes that define a roof, as opposed to its timber elements.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_roof_surface(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a roof surface, False otherwise (including an invalid element ID).
    """

def is_caddy_object(element_id: ElementId) -> bool:
    """Check whether an element is a caddy object.

    Caddy objects are elements generated by cadwork's Caddy modules.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_caddy_object(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a caddy object, False otherwise (including an invalid element ID).
    """

def is_envelope(element_id: ElementId) -> bool:
    """Check whether an element has a building envelope type assigned.

    True if any envelope type (for example framed or solid wall, floor, roof or opening) is set on
    the element, that is, if its cover type differs from the default. See
    `attribute_controller.is_wall()`, `attribute_controller.is_floor()` and
    `attribute_controller.is_roof()` for the individual kinds.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_envelope(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if an envelope type is assigned, False otherwise (including an invalid element ID).
    """

def is_architecture_wall_2dc(element_id: ElementId) -> bool:
    """Check whether an element is a wall linked to a 2dc architecture wall.

    Only walls can be true. Use `attribute_controller.is_architecture_wall_xml()` for the XML
    variant. Pass the ID of an existing element.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_architecture_wall_2dc(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a wall linked to a 2dc architecture wall, False otherwise.
    """

def is_architecture_wall_xml(element_id: ElementId) -> bool:
    """Check whether an element is a wall linked to XML architecture wall data.

    Only walls can be true. Use `attribute_controller.is_architecture_wall_2dc()` for the 2dc
    variant. Pass the ID of an existing element.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_architecture_wall_xml(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a wall with XML architecture wall data, False otherwise.
    """

def is_surface(element_id: ElementId) -> bool:
    """Check whether an element is a surface.

    Surfaces are planar faces, as opposed to beams and panels.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_surface(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a surface, False otherwise (including an invalid element ID).
    """

def is_line(element_id: ElementId) -> bool:
    """Check whether an element is a line.

    Lines are line elements without a cross-section, as opposed to beams and panels.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_line(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a line, False otherwise (including an invalid element ID).
    """

def get_auto_attribute(element_id: ElementId, number: UnsignedInt) -> str:
    """Get the value of an auto attribute of an element.

    Auto attributes are attributes whose text cadwork fills in from other element data. Call
    `attribute_controller.update_auto_attribute()` first if values may be stale. Returns an empty
    string for an invalid element ID or a number above 999. The title of the attribute comes from
    `attribute_controller.get_auto_attribute_name()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        number: Auto attribute number, counted from 1. Numbers above 999 return an empty string.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> ac.update_auto_attribute()
        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     value = ac.get_auto_attribute(element_id, 1)
        ...     print(element_id, ac.get_auto_attribute_name(1), value)

    Returns:
        The auto attribute value, or an empty string.
    """

def get_auto_attribute_name(number: UnsignedInt) -> str:
    """Get the display name of an auto attribute.

    Returns the title of the auto attribute as configured in the open document. Combine with
    `attribute_controller.get_auto_attribute()` to label values.

    Parameters:
        number: Auto attribute number, counted from 1.

    Examples:
        >>> import attribute_controller as ac

        >>> for number in range(1, 4):
        ...     print(number, ac.get_auto_attribute_name(number))

    Returns:
        The auto attribute name.
    """

def is_framed_wall(element_id: ElementId) -> bool:
    """Check whether an element is a framed wall.

    True only if the envelope type of the element is exactly framed wall. Use
    `attribute_controller.is_wall()` to test for any wall type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_framed_wall(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a framed wall, False otherwise (including an invalid element ID).
    """

def is_solid_wall(element_id: ElementId) -> bool:
    """Check whether an element is a solid wall.

    True only if the envelope type of the element is exactly solid wall. Use
    `attribute_controller.is_wall()` to test for any wall type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_solid_wall(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a solid wall, False otherwise (including an invalid element ID).
    """

def is_log_wall(element_id: ElementId) -> bool:
    """Check whether an element is a log wall.

    True only if the envelope type of the element is exactly log wall. Use
    `attribute_controller.is_wall()` to test for any wall type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_log_wall(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a log wall, False otherwise (including an invalid element ID).
    """

def is_framed_floor(element_id: ElementId) -> bool:
    """Check whether an element is a framed floor.

    True only if the envelope type of the element is exactly framed floor. Use
    `attribute_controller.is_floor()` to test for any floor type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_framed_floor(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a framed floor, False otherwise (including an invalid element ID).
    """

def is_solid_floor(element_id: ElementId) -> bool:
    """Check whether an element is a solid floor.

    True only if the envelope type of the element is exactly solid floor. Use
    `attribute_controller.is_floor()` to test for any floor type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_solid_floor(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a solid floor, False otherwise (including an invalid element ID).
    """

def is_framed_roof(element_id: ElementId) -> bool:
    """Check whether an element is a framed roof.

    True only if the envelope type of the element is exactly framed roof. Use
    `attribute_controller.is_roof()` to test for any roof type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_framed_roof(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a framed roof, False otherwise (including an invalid element ID).
    """

def is_solid_roof(element_id: ElementId) -> bool:
    """Check whether an element is a solid roof.

    True only if the envelope type of the element is exactly solid roof. Use
    `attribute_controller.is_roof()` to test for any roof type, or
    `attribute_controller.is_envelope()` for any envelope type.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_solid_roof(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a solid roof, False otherwise (including an invalid element ID).
    """

def get_additional_guid(element_id: ElementId, data_id: str) -> str:
    """Get the external GUID stored on an element for a given data ID.

    Elements can carry GUIDs from external data sets, each stored under its own data ID. Returns an
    empty string if the element ID is invalid. Store a GUID with
    `attribute_controller.set_additional_guid()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        data_id: Identifier of the external data set the GUID belongs to, as used when the GUID was
            stored with `attribute_controller.set_additional_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     guid = ac.get_additional_guid(element_id, 'my_system')
        ...     print(element_id, guid or '(no GUID)')

    Returns:
        The GUID as text, or an empty string.
    """

def get_prefab_layer_all_assigned(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers assigned to an element, with and without dimensions.

    Prefab layers are the numbered output layers of an element used for prefabrication output.
    Deprecated: emits a DeprecationWarning, use
    `attribute_controller.get_prefab_layer_info_all_assigned()` instead. Layers are returned in
    descending order. Pass a valid element ID; invalid IDs are not handled safely.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     layers = ac.get_prefab_layer_info_all_assigned(element_id)
        ...     print(element_id, layers)

    Returns:
        List of layer numbers of both kinds combined, highest first; empty if none are assigned.
    """

def get_prefab_layer_with_dimensions(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers of an element that output dimensions.

    Prefab layers are the numbered output layers of an element used for prefabrication output.
    Deprecated: emits a DeprecationWarning, use
    `attribute_controller.get_prefab_layer_info_with_dimensions()` instead. Layers are returned in
    descending order. Pass a valid element ID; invalid IDs are not handled safely.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     layers = ac.get_prefab_layer_info_with_dimensions(element_id)
        ...     print(element_id, layers)

    Returns:
        List of layer numbers with dimension output, highest first; empty if none.
    """

def get_prefab_layer_without_dimensions(element_id: ElementId) -> list[int]:
    """Get the prefab layer numbers of an element that output without dimensions.

    Prefab layers are the numbered output layers of an element used for prefabrication output.
    Deprecated: emits a DeprecationWarning, use
    `attribute_controller.get_prefab_layer_info_without_dimensions()` instead. Layers are returned
    in descending order. Pass a valid element ID; invalid IDs are not handled safely.

    Parameters:
        element_id: Element ID of an existing element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     layers = ac.get_prefab_layer_info_without_dimensions(element_id)
        ...     print(element_id, layers)

    Returns:
        List of layer numbers without dimension output, highest first; empty if none.
    """

def is_nesting_parent(element_id: ElementId) -> bool:
    """Check whether an element is a nesting parent.

    Nesting is the automatic layout of parts on raw stock; a nesting parent is the raw part on which
    parts are arranged. Use `attribute_controller.is_nesting_raw_part()` for the wider test that
    includes optimization bars.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_nesting_parent(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a nesting parent, False otherwise (including an invalid element ID).
    """

def is_nesting_raw_part(element_id: ElementId) -> bool:
    """Check whether an element is a nesting raw part.

    True for nesting parents and for optimization bar elements used as raw stock.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_nesting_raw_part(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a nesting raw part, False otherwise (including an invalid element
        ID).
    """

def get_container_number(element_id: ElementId) -> UnsignedInt:
    """Get the container number of a container element.

    A container groups other elements and has its own running number. Returns 0 for non-container
    elements, invalid IDs, or containers without a valid container number. Use
    `attribute_controller.get_container_number_with_prefix()` for the number including its prefix
    and `attribute_controller.is_container()` to test the element first.

    Parameters:
        element_id: Element ID of a container, e.g. from
            `element_controller.get_active_identifiable_element_ids()` filtered with
            `attribute_controller.is_container()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_container(element_id):
        ...         print(element_id, ac.get_container_number(element_id))

    Returns:
        The container number, or 0.
    """

def get_container_number_with_prefix(element_id: ElementId) -> str:
    """Get the container number of a container element including its prefix.

    The prefix is derived from the document settings for containers and put in front of the number
    returned by `attribute_controller.get_container_number()`. Returns an empty string for
    non-container elements, invalid IDs, or containers without a valid container number.

    Parameters:
        element_id: Element ID of a container, e.g. from
            `element_controller.get_active_identifiable_element_ids()` filtered with
            `attribute_controller.is_container()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_container(element_id):
        ...         print(ac.get_container_number_with_prefix(element_id))

    Returns:
        Prefix followed by the container number, or an empty string.
    """

def get_group_list_items() -> list[str]:
    """Get the entries of the group list.

    Returns the predefined values of the group list stored in the open document, in list order. A
    leading empty entry (the blank choice) is left out. Returns an empty list if there are no
    entries. Assign a group with `attribute_controller.set_group()`, read it with
    `attribute_controller.get_group()`.

    Examples:
        >>> import attribute_controller as ac

        >>> groups = ac.get_group_list_items()
        >>> for entry in groups:
        ...     print(entry)

    Returns:
        List of the entries, empty if there are none.
    """

def get_subgroup_list_items() -> list[str]:
    """Get the entries of the subgroup list.

    Returns the predefined values of the subgroup list stored in the open document, in list order. A
    leading empty entry (the blank choice) is left out. Returns an empty list if there are no
    entries. Read an element's value with `attribute_controller.get_subgroup()`.

    Examples:
        >>> import attribute_controller as ac

        >>> subgroups = ac.get_subgroup_list_items()
        >>> for entry in subgroups:
        ...     print(entry)

    Returns:
        List of the entries, empty if there are none.
    """

def get_comment_list_items() -> list[str]:
    """Get the entries of the comment list.

    Returns the predefined values of the comment list stored in the open document, in list order. A
    leading empty entry (the blank choice) is left out. Returns an empty list if there are no
    entries. Read an element's value with `attribute_controller.get_comment()`.

    Examples:
        >>> import attribute_controller as ac

        >>> comments = ac.get_comment_list_items()
        >>> for entry in comments:
        ...     print(entry)

    Returns:
        List of the entries, empty if there are none.
    """

def get_sku_list_items() -> list[str]:
    """Get the entries of the SKU list.

    Returns the predefined values of the SKU list stored in the open document, in list order. A
    leading empty entry (the blank choice) is left out. Returns an empty list if there are no
    entries. Read an element's value with `attribute_controller.get_sku()`.

    Examples:
        >>> import attribute_controller as ac

        >>> skus = ac.get_sku_list_items()
        >>> for entry in skus:
        ...     print(entry)

    Returns:
        List of the entries, empty if there are none.
    """

def get_user_attribute_list_items(number: UserAttributeId) -> list[str]:
    """Get the list entries of a user attribute.

    Returns the predefined values of the list of a user attribute stored in the open document, in
    list order. A leading empty entry (the blank choice) is left out. Returns an empty list if there
    are no entries. Read an element's value with `attribute_controller.get_user_attribute()` and the
    attribute title with `attribute_controller.get_user_attribute_name()`.

    Parameters:
        number: User attribute number, counted from 1; the count is
            `attribute_controller.get_user_attribute_count()`.

    Examples:
        >>> import attribute_controller as ac

        >>> for number in range(1, ac.get_user_attribute_count() + 1):
        ...     items = ac.get_user_attribute_list_items(number)
        ...     print(ac.get_user_attribute_name(number), items)

    Returns:
        List of the entries, empty if there are none.
    """

def is_circular_mep(element_id: ElementId) -> bool:
    """Check whether an element is a circular MEP (installation) line.

    MEP (mechanical, electrical, plumbing) installation lines are pipes and ducts; circular ones
    have a round cross-section. Use `attribute_controller.is_rectangular_mep()` for the rectangular
    kind.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_circular_mep(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a circular MEP line, False otherwise (including an invalid element
        ID).
    """

def is_rectangular_mep(element_id: ElementId) -> bool:
    """Check whether an element is a rectangular MEP (installation) element.

    MEP (mechanical, electrical, plumbing) installations are pipes and ducts; rectangular ones have
    a rectangular cross-section. Use `attribute_controller.is_circular_mep()` for the round kind.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid or deleted ID
            returns False.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if ac.is_rectangular_mep(element_id):
        ...         print(element_id, ac.get_name(element_id))

    Returns:
        True if the element is a rectangular MEP element, False otherwise (including an invalid
        element ID).
    """

def get_machine_calculation_state(element_id: ElementId) -> str:
    """Get the machine calculation state of an element as a display text.

    The machine calculation state tells whether the machining of the element is calculated, checked
    or confirmed as OK. The text names this state, optionally followed by a locked marker and a
    blocked-for-export marker, separated by commas. The wording follows the cadwork UI language, so
    do not compare it with fixed strings in scripts. Returns an empty string for an invalid element
    ID or an element without element data.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     state = ac.get_machine_calculation_state(element_id)
        ...     print(element_id, state or '(no state)')

    Returns:
        State text, or an empty string for an invalid element ID or an element without element data.
    """

def get_machine_calculation_set_machine_type(element_id: ElementId) -> str:
    """Get the machine type of an element's machine calculation set as a display text.

    A machine calculation set is the machine configuration assigned to an element for production
    calculation. The returned text is the machine name as shown in cadwork 3D, so it follows the
    user interface language. Read the name of the set itself with
    `attribute_controller.get_machine_calculation_set()` and change the set with
    `attribute_controller.set_machine_calculation_set()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     set_name = ac.get_machine_calculation_set(element_id)
        ...     machine = ac.get_machine_calculation_set_machine_type(element_id)
        ...     print(element_id, set_name, machine)

    Returns:
        Machine name as text, or an empty string for an invalid element ID.
    """

def is_btl_processing_group(element_id: ElementId) -> bool:
    """Check whether an element is a BTL processing group.

    A BTL processing group is an element that stands for a BTL machining: it carries the BTL
    processing group attribute and the matching BTL reference points. Both must be present. Use it
    to filter such elements before reading their machining data with functions such as
    `machine_controller.get_element_btl_processings()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> groups = [e for e in element_ids if ac.is_btl_processing_group(e)]
        >>> print(len(groups), 'BTL processing groups')

    Returns:
        True if the element has the BTL processing group attribute and the BTL reference points,
        otherwise False (also for an invalid element ID).
    """

def is_hundegger_processing_group(element_id: ElementId) -> bool:
    """Check whether an element is a Hundegger processing group.

    A Hundegger processing group is an element that stands for a Hundegger machining: it carries the
    Hundegger processing group attribute and the matching Hundegger reference points. Both must be
    present. Use it to filter such elements before reading their machining data with
    `machine_controller.get_element_hundegger_processings()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> groups = [e for e in element_ids if ac.is_hundegger_processing_group(e)]
        >>> print(len(groups), 'Hundegger processing groups')

    Returns:
        True if the element has the Hundegger processing group attribute and the Hundegger reference
        points, otherwise False (also for an invalid element ID).
    """

def get_element_grouping_type() -> element_grouping_type:
    """Get whether the element builder uses the group or the subgroup attribute.

    The element builder collects elements by either their group or their subgroup attribute. This is
    an application option and not a property of any element. Change it with
    `attribute_controller.set_element_grouping_type()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import cadwork

        >>> if ac.get_element_grouping_type() == cadwork.element_grouping_type.group:
        ...     print('Element builder works with the group attribute')
        ... else:
        ...     print('Element builder works with the subgroup attribute')

    Returns:
        `cadwork.element_grouping_type.group` or `cadwork.element_grouping_type.subgroup`.
    """

def set_element_grouping_type(element_grouping_type: element_grouping_type) -> None:
    """Set whether the element builder uses the group or the subgroup attribute.

    Changes the application option read by `attribute_controller.get_element_grouping_type()`. It
    affects the element builder as a whole, not a single element. Any value other than `group` is
    treated as `subgroup`.

    Parameters:
        element_grouping_type: `cadwork.element_grouping_type.group` or
            `cadwork.element_grouping_type.subgroup`.

    Examples:
        >>> import attribute_controller as ac
        >>> import cadwork

        >>> ac.set_element_grouping_type(cadwork.element_grouping_type.subgroup)
    """

def get_associated_nesting_name(element_id: ElementId) -> str:
    """Get the name of the nesting group an element belongs to.

    Nesting arranges parts on raw material; the elements of one nesting result form a nesting group
    with a name. Use it to find out which nesting an element belongs to. See also
    `attribute_controller.get_associated_nesting_number()`,
    `attribute_controller.is_nesting_parent()` and `attribute_controller.is_nesting_raw_part()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     nesting_name = ac.get_associated_nesting_name(element_id)
        ...     if nesting_name:
        ...         print(element_id, 'is nested in', nesting_name)

    Returns:
        Name of the nesting group, or an empty string for an invalid element ID or an element that
        is not part of a nesting group.
    """

def get_associated_nesting_number(element_id: ElementId) -> str:
    """Get the production list number of the nesting parent of an element.

    Looks up the parent of the element in a nesting first and, if there is none, in a linear
    optimization. Returns the production list number of that parent, converted to text. Related:
    `attribute_controller.get_associated_nesting_name()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     number = ac.get_associated_nesting_number(element_id)
        ...     print(element_id, number or '-')

    Returns:
        Production list number of the parent as a string, or an empty string for an invalid element
        ID or an element without such a parent.
    """

def get_attribute_display_settings_for_2d() -> attribute_display_settings:
    """Get the attribute text position settings for normal 2D export.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_2d()`. Related:
    `attribute_controller.get_attribute_display_settings_for_2d_with_layout()` and
    `attribute_controller.get_attribute_display_settings_for_2d_without_layout()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_2d_with_layout() -> attribute_display_settings:
    """Get the attribute text position settings for 2D export with frame.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_2d_with_layout()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d_with_layout()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_2d_without_layout() -> attribute_display_settings:
    """Get the attribute text position settings for 2D export without frame.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_2d_without_layout()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_2d_without_layout()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_3d() -> attribute_display_settings:
    """Get the attribute text position settings for the 3D view.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_3d()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_3d()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_container() -> attribute_display_settings:
    """Get the attribute text position settings for containers.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_container()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_container()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_export_solid() -> attribute_display_settings:
    """Get the attribute text position settings for solid export.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_export_solid()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_export_solid()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_framed_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall axes.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_framed_wall_axis()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_axis()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_framed_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall beams.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_framed_wall_beam()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_beam()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_framed_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall openings.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_framed_wall_opening()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_opening()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_framed_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for framed wall panels.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_framed_wall_panel()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_framed_wall_panel()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_log_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for log wall axes.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_log_wall_axis()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_axis()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_log_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for log wall beams.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_log_wall_beam()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_beam()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_log_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for log wall openings.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_log_wall_opening()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_opening()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_log_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for log wall panels.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_log_wall_panel()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_log_wall_panel()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_machine() -> attribute_display_settings:
    """Get the attribute text position settings for machine output.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_machine()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_machine()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_nesting_element() -> attribute_display_settings:
    """Get the attribute text position settings for nesting elements.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_nesting_element()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_nesting_element()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_nesting_volume() -> attribute_display_settings:
    """Get the attribute text position settings for nesting volumes.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to `attribute_controller.set_attribute_display_settings_for_nesting_volume()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_nesting_volume()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_solid_wall_axis() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall axes.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_solid_wall_axis()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_axis()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_solid_wall_beam() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall beams.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_solid_wall_beam()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_beam()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_solid_wall_opening() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall openings.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_solid_wall_opening()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_opening()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def get_attribute_display_settings_for_solid_wall_panel() -> attribute_display_settings:
    """Get the attribute text position settings for solid wall panels.

    Attribute text is the label with element attributes that cadwork 3D places next to an element
    for this target. The settings say whether its distance is given in millimetres or in percent and
    hold both values. The result is a copy of the stored settings: changing it does not write back
    until you pass it to
    `attribute_controller.set_attribute_display_settings_for_solid_wall_panel()`.

    Examples:
        >>> import attribute_controller as ac

        >>> settings = ac.get_attribute_display_settings_for_solid_wall_panel()
        >>> if settings.is_text_position_type_percentage():
        ...     print('Text position:', settings.get_text_position_percentage(), '%')
        ... else:
        ...     print('Text position:', settings.get_text_position_absolute(), 'mm')

    Returns:
        attribute_display_settings. Use `is_text_position_type_percentage()` to see which type is
        active, then read `get_text_position_percentage()` (percent) or
        `get_text_position_absolute()` (mm).
    """

def is_processing(element_id: ElementId) -> bool:
    """Check whether a processing with the given ID exists on a visible element.

    Despite the parameter name, the value is compared with the database ID of a processing
    (machining), not with an element ID. Only the processings of currently visible elements are
    searched, so hidden elements never match. Processing IDs come from
    `machine_controller.get_element_hundegger_processings()` or
    `machine_controller.get_element_btl_processings()`.

    Parameters:
        element_id: ID of the processing to look for.

    Examples:
        >>> import attribute_controller as ac
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> machine = cadwork.hundegger_machine_type.k2.value
        >>> for processing_id in mc.get_element_hundegger_processings(element_id, machine):
        ...     print(processing_id, ac.is_processing(processing_id))

    Returns:
        True if a visible element carries a processing with this ID, otherwise False.
    """

def delete_user_attribute(number: UserAttributeId) -> bool:
    """Delete a user attribute definition from the document.

    Removes the user attribute (its name/title) with the given number. Nothing is deleted while the
    attribute still has list entries; remove them first with
    `attribute_controller.delete_item_from_user_attribute_list()`. Read the entries with
    `attribute_controller.get_user_attribute_list_items()` and the name with
    `attribute_controller.get_user_attribute_name()`.

    Parameters:
        number: User attribute number, counted from 1.

    Examples:
        >>> import attribute_controller as ac

        >>> number = 12
        >>> if ac.delete_user_attribute(number):
        ...     print('User attribute', number, 'deleted')
        ... else:
        ...     print('User attribute', number, 'is still in use')

    Returns:
        True if the attribute definition is gone afterwards, False if it still has list entries or
        could not be deleted.
    """

def is_attribute_visible_in_modify_window(number: UnsignedInt) -> bool:
    """Check whether a user attribute is shown in the Modify window.

    The Modify window is the cadwork 3D dialog in which attributes of the selected elements are
    edited. Visibility is a document setting per user attribute. Change it with
    `attribute_controller.set_attribute_visibility_in_modify_window()`. A number outside the user
    attribute range returns False and writes an error line to the cadwork console.

    Parameters:
        number: User attribute number (1 to 10000).

    Examples:
        >>> import attribute_controller as ac

        >>> number = 3
        >>> if not ac.is_attribute_visible_in_modify_window(number):
        ...     print('User attribute', number, 'is hidden in the Modify window')

    Returns:
        True if the attribute is visible in the Modify window, otherwise False.
    """

def set_attribute_visibility_in_modify_window(number: UnsignedInt, visibility: bool) -> None:
    """Show or hide a user attribute in the Modify window.

    The Modify window is the cadwork 3D dialog in which attributes of the selected elements are
    edited. The setting is stored in the document per user attribute. A number outside the user
    attribute range does nothing apart from an error line in the cadwork console. Read the state
    back with `attribute_controller.is_attribute_visible_in_modify_window()`.

    Parameters:
        number: User attribute number (1 to 10000).
        visibility: True to show the attribute, False to hide it.

    Examples:
        >>> import attribute_controller as ac

        >>> number = 3
        >>> ac.set_attribute_visibility_in_modify_window(number, False)
        >>> print(ac.is_attribute_visible_in_modify_window(number))
    """

def set_cutting_set(element_id_list: list[ElementId], cutting_set_name: str) -> bool:
    """Assign a cutting set to elements by name.

    A cutting set holds the cut offsets of an element and is stored in the document. The name is
    matched case-insensitively. For each element the sets of the document are searched first, then
    the user profile sets (timber) or the standard sets (steel and round beams). A set found outside
    the document is copied into it once and shared by all elements. Invalid IDs are skipped. Read
    the current set with `attribute_controller.get_cutting_set()`.

    Parameters:
        element_id_list: List of element IDs to assign to, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        cutting_set_name: Name of the cutting set, compared case-insensitively.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if not ac.set_cutting_set(element_ids, 'Standard'):
        ...     print('No applicable cutting set named Standard')

    Returns:
        True if the set was assigned to at least one element, False if no element resolved or the
        name matches no set applicable to the elements.
    """

def get_standard_element_material_id(element_id: ElementId) -> int:
    """Get the material ID of a standard element.

    A standard element is an element created from the standard element library, so it has a standard
    element assigned. The ID returned is the material assigned to the element. Read the standard
    element name with `attribute_controller.get_standard_element_name()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     material_id = ac.get_standard_element_material_id(element_id)
        ...     if material_id:
        ...         print(element_id, ac.get_standard_element_name(element_id), material_id)

    Returns:
        Material ID, or 0 for an invalid element ID or an element that is not a standard element.
    """

def set_machine_calculation_set(element_ids: list[ElementId], name: str) -> bool:
    """Assign a machine calculation set to elements by name.

    A machine calculation set is the machine configuration used to calculate the production of an
    element. If several sets share the name, the first one is used and a warning is written to the
    API log. Invalid IDs and elements that cannot hold the set are skipped; an empty list is a no-op
    that still returns True when the set exists. Read the current set with
    `attribute_controller.get_machine_calculation_set()`.

    Parameters:
        element_ids: List of element IDs to assign to, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        name: Name of an existing machine calculation set.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec
        >>> [element] = ec.get_active_identifiable_element_ids()
        >>> current_set = ac.get_machine_calculation_set(element)
        >>> success = ac.set_machine_calculation_set([element], "xyz_hundegger K2_BVN")

    Returns:
        True if a set with this name exists, False if no set with this name is found (the error is
        also written to the API log).
    """

def delete_item_from_name_list(item: str) -> bool:
    """Delete an entry from the Name attribute list.

    The Name list holds the values offered for the Name attribute of elements. An entry that does
    not exist or that is still used by at least one element is not deleted; the reason is written to
    the API log. See also `attribute_controller.get_name_list_items()` and
    `attribute_controller.add_item_to_name_list()`.

    Parameters:
        item: Exact text of the list entry to delete, e.g. an entry from
            `attribute_controller.get_name_list_items()`.

    Examples:
        >>> import attribute_controller as ac

        >>> item = 'Old name'
        >>> if item in ac.get_name_list_items():
        ...     if not ac.delete_item_from_name_list(item):
        ...         print('Entry is still used by elements')

    Returns:
        True if the entry was deleted, False if it does not exist, is still in use or the attribute
        database is unavailable.
    """

def get_additional_data_keys(element_id: ElementId) -> list[str]:
    """List the additional data keys stored on an element.

    Additional data is free text stored per element under a key, written with
    `attribute_controller.set_additional_data()`. Keys that cadwork 3D writes for its own purposes
    (for example multi layer, hoisting, BTL or Revit data) are left out. Read a value with
    `attribute_controller.get_additional_data()` and remove one with
    `attribute_controller.delete_additional_data()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> for key in ac.get_additional_data_keys(element_id):
        ...     print(key, '=', ac.get_additional_data(element_id, key))

    Returns:
        List of keys; empty for an invalid element ID or an element without such keys.
    """

def get_prefab_layer_info_all_assigned(element_id: ElementId) -> list[prefab_layer_info]:
    """Get all prefab layers assigned to an element, with and without dimensions.

    Prefab layers are the construction layers of a prefabricated wall or roof element (the element's
    own framework plus layers on the reference side and the opposite side). The list holds the
    layers output with dimensions followed by the layers output without dimensions; the two parts
    are not merged or sorted. Each item has `get_layer_number()` and `get_side()`: the side is the
    element itself (layer 0), the reference side or the opposite side, and for the opposite side the
    layer number is given as a positive count. Related:
    `attribute_controller.get_prefab_layer_info_with_dimensions()`,
    `attribute_controller.get_prefab_layer_info_without_dimensions()`;
    `attribute_controller.get_prefab_layer_all_assigned()` is the deprecated variant returning plain
    numbers.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> for info in ac.get_prefab_layer_info_all_assigned(element_id):
        ...     print(info.get_layer_number(), info.get_side())

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """

def get_prefab_layer_info_with_dimensions(element_id: ElementId) -> list[prefab_layer_info]:
    """Get the prefab layers of an element that are output with dimensions.

    Prefab layers are the construction layers of a prefabricated wall or roof element (the element's
    own framework plus layers on the reference side and the opposite side). This list contains only
    the layers that are output with dimensions. Each item has `get_layer_number()` and `get_side()`:
    the side is the element itself (layer 0), the reference side or the opposite side, and for the
    opposite side the layer number is given as a positive count. The order is: the element itself
    first, then reference-side layers 1, 2, ..., then opposite-side layers 1, 2, .... Related:
    `attribute_controller.get_prefab_layer_info_without_dimensions()` and
    `attribute_controller.get_prefab_layer_info_all_assigned()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> for info in ac.get_prefab_layer_info_with_dimensions(element_id):
        ...     print(info.get_layer_number(), info.get_side())

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """

def get_prefab_layer_info_without_dimensions(element_id: ElementId) -> list[prefab_layer_info]:
    """Get the prefab layers of an element that are output without dimensions.

    Prefab layers are the construction layers of a prefabricated wall or roof element (the element's
    own framework plus layers on the reference side and the opposite side). This list contains only
    the layers that are output without dimensions. Each item has `get_layer_number()` and
    `get_side()`: the side is the element itself (layer 0), the reference side or the opposite side,
    and for the opposite side the layer number is given as a positive count. The order is: the
    element itself first, then reference-side layers 1, 2, ..., then opposite-side layers 1, 2, ....
    Related: `attribute_controller.get_prefab_layer_info_with_dimensions()` and
    `attribute_controller.get_prefab_layer_info_all_assigned()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> for info in ac.get_prefab_layer_info_without_dimensions(element_id):
        ...     print(info.get_layer_number(), info.get_side())

    Returns:
        List of prefab_layer_info; empty for an invalid element ID or an element without layers.
    """
