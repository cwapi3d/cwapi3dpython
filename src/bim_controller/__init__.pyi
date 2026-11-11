"""Building Information Modeling (BIM) workflows.

Covers the IFC ecosystem and the building-structural metadata that
goes with it: IFC import/export in its supported schema versions,
configuration of IFC export options (properties, project data,
aggregation, element combination), and assignment of building and
storey information to elements. The module to use whenever the model
needs to interoperate with IFC-based BIM tooling.
"""

from cadwork.ifc_2x3_element_type import ifc_2x3_element_type
from cadwork.ifc_options import ifc_options
from cadwork.ifc_predefined_type import ifc_predefined_type
from cadwork.api_types import *

def get_ifc_guid(element_id: ElementId) -> str:
    """Get the IFC GUID of an element as a standard GUID string.

    Returns the element's IFC GUID in the usual 36-character GUID notation, not the 22-character
    form used inside IFC files; use `bim_controller.get_ifc_base64_guid()` for that. If the element
    has no IFC GUID yet, one is generated and stored on the element, so the call can modify the
    document. Requires an IFC license; without it a message is printed to the console and an empty
    string is returned.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_guid = bc.get_ifc_guid(element)
        >>> print(f"IFC GUID: {ifc_guid}")

    Returns:
        The GUID string, or an empty string if the element ID is invalid or no IFC license is
        available.
    """

def get_ifc2x3_element_type(element_id: ElementId) -> ifc_2x3_element_type:
    """Get the IFC entity type assigned to an element.

    The IFC entity type (for example wall, beam, member) decides which IFC class the element is
    exported as. Use `bim_controller.get_ifc2x3_element_type_string()` to turn the result into the
    IFC entity name, and `bim_controller.set_ifc2x3_element_type()` to change it. Requires an IFC
    license.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork # needed for ifc_2x3_element_type

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element)

    Returns:
        The element's IFC entity type. For an invalid element ID, an element without IFC data or a
        missing IFC license, a type with value 0 (nothing set) is returned, never None.
    """

def set_ifc2x3_element_type(element_id_list: list[ElementId], ifc_type: ifc_2x3_element_type) -> None:
    """Assign an IFC entity type to elements.

    Sets the IFC class that the listed elements are exported as. Elements without IFC data are
    skipped silently, and an empty list does nothing. Requires an IFC license; without it nothing
    happens. Read the value back with `bim_controller.get_ifc2x3_element_type()`.

    Parameters:
        element_id_list: List of element IDs to modify, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Pass IDs of existing
            elements only.
        ifc_type: The IFC entity type to assign to every listed element, built with
            `cadwork.ifc_2x3_element_type` and one of its `set_ifc_*` methods.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_entity_type = cadwork.ifc_2x3_element_type()
        >>> ifc_entity_type.set_ifc_member()
        >>> bc.set_ifc2x3_element_type(selected_elements, ifc_entity_type)
    """

def import_ifc_as_graphical_object(file_path: str) -> bool:
    """Import an IFC file into the document as a graphical object.

    The IFC content is added as one graphical (exchange) object that is shown but not converted to
    cadwork elements. To get the individual exchange objects and convert them, use
    `bim_controller.import_ifc_return_exchange_objects()` and
    `bim_controller.convert_exchange_objects()` instead. Requires an IFC license.

    Parameters:
        file_path: Path of the IFC file to import.

    Examples:
        >>> import bim_controller as bc

        >>> ifc_file_path = r"C:/imports/building_model.ifc"
        >>> success = bc.import_ifc_as_graphical_object(ifc_file_path)
        >>> if success:
        >>>     print("IFC imported as graphical object successfully")

    Returns:
        True if the import produced an object, False otherwise (including a missing IFC license).
    """

def import_bcf(file_path: str) -> bool:
    """Import a BCF (BIM collaboration format) file.

    Hands the file to the application's BCF import and returns without checking whether it could be
    read. Requires a BIM Manager license; without it a message is printed to the console. Use
    `bim_controller.export_bcf()` for the opposite direction.

    Parameters:
        file_path: Path of the BCF file to import.

    Examples:
        >>> import bim_controller as bc

        >>> bcf_file_path = r"C:/imports/issues.bcf"
        >>> success = bc.import_bcf(bcf_file_path)
        >>> if success:
        >>>     print("BCF file imported successfully")

    Returns:
        False if the path is empty or no BIM Manager license is available. Otherwise True once the
        import was requested, even if the file is missing or invalid.
    """

def export_bcf(file_path: str) -> bool:
    """Export the BCF (BIM collaboration format) issues to a file.

    Hands the target path to the application's BCF export and returns without checking that the file
    was written. Requires a BIM Manager license; without it a message is printed to the console. Use
    `bim_controller.import_bcf()` for the opposite direction.

    Parameters:
        file_path: Path of the BCF file to write.

    Examples:
        >>> import bim_controller as bc

        >>> bcf_output_path = r"C:/exports/project_issues.bcf"
        >>> success = bc.export_bcf(bcf_output_path)
        >>> if success:
        >>>     print("BCF file exported successfully")

    Returns:
        False if no BIM Manager license is available. Otherwise True once the export was requested,
        even for an empty path or if writing fails.
    """

def export_ifc(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export the active elements to an IFC2x3 file, showing a progress bar.

    The export uses the elements that are active when the function is called; the list is not passed
    to the export. If no element is active, the listed elements are only activated (and stay
    active), and that same call still exports the empty selection that was read before the
    activation. Uses the IFC export settings stored in the document and shows a progress window with
    a cancel button. To export a specific list of elements, use `bim_controller.export_ifc2x3()` or
    `bim_controller.export_ifc2x3_silently()`. Requires an IFC license.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Only used to activate
            elements when nothing is active; it does not select what is exported.
        file_path: Path of the IFC file to write.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_output_path = r"C:/exports/building_model.ifc"
        >>> success = bc.export_ifc(selected_elements, ifc_output_path)
        >>> if success:
        >>>     print("IFC file exported successfully")

    Returns:
        False without an IFC license. Otherwise True once the export ran, even if it was canceled or
        the file could not be written.
    """

def import_ifc_return_exchange_objects(file_path: str) -> list[ElementId]:
    """Import an IFC file and return the IDs of the created exchange objects.

    The IFC file is imported as a graphical object; its parts become exchange objects that can be
    turned into cadwork elements with `bim_controller.convert_exchange_objects()`. Requires an IFC
    license.

    Parameters:
        file_path: Path of an existing IFC file.

    Examples:
        >>> import bim_controller as bc

        >>> ifc_path = 'C:/imports/building_model.ifc'
        >>> exchange_ids = bc.import_ifc_return_exchange_objects(ifc_path)
        >>> if exchange_ids:
        ...     element_ids = bc.convert_exchange_objects(exchange_ids)
        ...     print(f'Created {len(element_ids)} elements')

    Returns:
        List of exchange object IDs (the children of the imported object, not the imported object
        itself). Empty list if the file does not exist, the import fails or no IFC license is
        available.
    """

def set_storey_height(building: str, storey: str, height: float) -> None:
    """Set the elevation (height level) of a storey.

    The value is the storey's elevation in the building, not its floor-to-floor height. If the
    building or storey does not exist, nothing is changed and no exception is raised. Marks the
    document as modified and refreshes the BIM structure view. Read the value back with
    `bim_controller.get_storey_height()`. Requires an IFC license.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of an existing storey of that building, e.g. from
            `bim_controller.get_all_storeys()`.
        height: New elevation of the storey in model units (mm).

    Examples:
        >>> import bim_controller as bc

        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> height_millimeters = 3_500
        >>> bc.set_storey_height(building_name, storey_name, height_millimeters)
    """

def convert_exchange_objects(exchange_objects: list[ElementId]) -> list[ElementId]:
    """Convert exchange objects from an IFC import into cadwork elements.

    Invalid IDs are skipped. The display is refreshed if automatic refresh is on, and the BIM
    structure is updated. Objects that cannot be converted produce no element. Requires an IFC
    license.

    Parameters:
        exchange_objects: List of exchange object IDs, as returned by
            `bim_controller.import_ifc_return_exchange_objects()`.

    Examples:
        >>> import bim_controller as bc

        >>> exchange_ids = bc.import_ifc_return_exchange_objects('C:/imports/model.ifc')
        >>> new_elements = bc.convert_exchange_objects(exchange_ids)
        >>> if not new_elements:
        ...     print('Nothing was converted')

    Returns:
        List of the newly created cadwork element IDs (the inputs are not included). Empty list if
        nothing could be converted or no IFC license is available.
    """

def export_ifc2x3_silently(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC2x3 file without a progress window.

    Exports the listed elements, independent of which elements are active, using the IFC export
    settings stored in the document and the Coordination View. The element activation is not
    changed. An element ID of 0 is skipped. Requires an IFC license. For a progress window use
    `bim_controller.export_ifc2x3()`; to override the settings use
    `bim_controller.export_ifc2x3_silently_with_options()`.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ok = bc.export_ifc2x3_silently(element_ids, 'C:/exports/model_2x3.ifc')
        >>> if not ok:
        ...     print('Nothing exported: empty list or no IFC license')

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if the file could not be written.
    """

def export_ifc4_silently(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC4 file without a progress window.

    Exports the listed elements, independent of which elements are active, using the IFC export
    settings stored in the document and the Reference View. The element activation is not changed.
    An element ID of 0 is skipped. Requires an IFC license. For a progress window use
    `bim_controller.export_ifc4()`; to override the settings use
    `bim_controller.export_ifc4_silently_with_options()`.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ok = bc.export_ifc4_silently(element_ids, 'C:/exports/model_ifc4.ifc')
        >>> if not ok:
        ...     print('Nothing exported: empty list or no IFC license')

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if the file could not be written.
    """

def export_ifc2x3_silently_with_options(element_id_list: list[ElementId], file_path: str, options: ifc_options) -> bool:
    """Export elements to an IFC2x3 file with explicit options, without a progress window.

    Every setting in the given options replaces the corresponding IFC export setting stored in the
    document, and the result is saved back into the document, so the options also apply to later
    exports, including the dialog-based ones. The listed elements are exported regardless of which
    elements are active. An element ID of 0 is skipped. Unlike the other silent exports, no IFC
    license check and no empty-list check is done here.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.
        options: IFC export options, typically obtained from `bim_controller.get_ifc_options()` and
            then modified.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> options = bc.get_ifc_options()
        >>> options.get_ifc_options_properties().set_export_quantity_sets(True)
        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> bc.export_ifc2x3_silently_with_options(element_ids, 'C:/exports/q.ifc', options)

    Returns:
        True once the export ran, even if the file could not be written. An empty element list is
        not rejected.
    """

def export_ifc4_silently_with_options(element_id_list: list[ElementId], file_path: str, options: ifc_options) -> bool:
    """Export elements to an IFC4 file with explicit options, without a progress window.

    Every setting in the given options replaces the corresponding IFC export setting stored in the
    document, and the result is saved back into the document, so the options also apply to later
    exports, including the dialog-based ones. The listed elements are exported regardless of which
    elements are active. An element ID of 0 is skipped. Unlike the other silent exports, no IFC
    license check and no empty-list check is done here.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.
        options: IFC export options, typically obtained from `bim_controller.get_ifc_options()` and
            then modified.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> options = bc.get_ifc_options()
        >>> options.get_ifc_options_properties().set_export_quantity_sets(True)
        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> bc.export_ifc4_silently_with_options(element_ids, 'C:/exports/q4.ifc', options)

    Returns:
        True once the export ran, even if the file could not be written. An empty element list is
        not rejected.
    """

def update_bmt_structure_created_elements(element_id_list: list[ElementId]) -> None:
    """Register newly created elements in the BIM structure under the active building and storey.

    Use after creating elements by script so they appear in the BIM structure view. Only notifies
    the BIM structure of the elements; it does not assign a building or storey itself. To assign a
    specific storey, use `bim_controller.set_building_and_storey()` and then
    `bim_controller.update_bmt_structure_building_storey()`.

    Parameters:
        element_id_list: List of IDs of the newly created elements.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> new_elements = ec.get_active_identifiable_element_ids()
        >>> bc.update_bmt_structure_created_elements(new_elements)
    """

def update_bmt_structure_building_storey(element_id_list: list[ElementId]) -> None:
    """Update the BIM structure view for elements whose building and storey were changed.

    Use after assigning building and storey with `bim_controller.set_building_and_storey()` so the
    BIM structure view reflects the assignment. Sends an update request for the listed elements; no
    assignment is changed.

    Parameters:
        element_id_list: List of IDs of the elements to update.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> bc.set_building_and_storey(element_ids, 'Building A', 'Level 1')
        >>> bc.update_bmt_structure_building_storey(element_ids)
    """

def get_ifc_options() -> ifc_options:
    """Get the IFC export options stored in the document.

    Returns a snapshot of the document's current IFC export settings (project data, properties,
    level of detail, aggregation). Changing the returned object does not alter the document unless
    you pass it to `bim_controller.export_ifc2x3_silently_with_options()` or
    `bim_controller.export_ifc4_silently_with_options()`. Each call reads the settings anew and
    replaces the previous snapshot, so do not keep using an object from an earlier call after
    calling this function again. No dialog is shown and no license is required.

    Examples:
        >>> import bim_controller as bc

        >>> options = bc.get_ifc_options()
        >>> properties = options.get_ifc_options_properties()
        >>> print(properties.get_export_quantity_sets())

    Returns:
        An ifc_options object with the document's current IFC export settings.
    """

def set_building_and_storey(element_id_list: list[ElementId], building: str, storey: str) -> None:
    """Assign elements to a building and storey.

    The building and storey are created if they do not exist yet. An element belongs to one storey
    only, so it is removed from its previous storey. Container blocks bring their contents along,
    and IFC container elements that the listed elements belong to are assigned as well. IDs of
    non-existent elements are skipped. Requires an IFC license; without it nothing happens. Read the
    assignment back with `bim_controller.get_building()` and `bim_controller.get_storey()`; call
    `bim_controller.update_bmt_structure_building_storey()` to refresh the BIM structure view.

    Parameters:
        element_id_list: List of element IDs to assign, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        building: Name of the building; created if missing.
        storey: Name of the storey within the building; created if missing.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> bc.set_building_and_storey(selected_elements, building_name, storey_name)
    """

def get_building(element_id: ElementId) -> str:
    """Get the name of the building an element is assigned to.

    Looks up the building through the element's storey assignment. Assign elements with
    `bim_controller.set_building_and_storey()`. No license is required.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     building = bc.get_building(element_id)
        ...     print(element_id, building or '(not assigned)')

    Returns:
        The building name, or an empty string if the element ID is invalid or the element has no
        building assignment.
    """

def get_storey(element_id: ElementId) -> str:
    """Get the name of the storey an element is assigned to.

    Storey names are only unique within one building, so combine the result with
    `bim_controller.get_building()` to identify the storey. No license is required.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     building = bc.get_building(element_id)
        ...     storey = bc.get_storey(element_id)
        ...     print(element_id, building, storey)

    Returns:
        The storey name, or an empty string if the element ID is invalid or the element has no
        storey assignment.
    """

def get_storey_height(building: str, storey: str) -> float:
    """Get the elevation (height level) of a storey.

    The value is the storey's elevation in the building, not its floor-to-floor height. Change it
    with `bim_controller.set_storey_height()`. Requires an IFC license.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of a storey of that building, e.g. from `bim_controller.get_all_storeys()`.

    Examples:
        >>> import bim_controller as bc

        >>> building = bc.get_all_buildings()[0]
        >>> storey = bc.get_all_storeys(building)[0]
        >>> elevation = bc.get_storey_height(building, storey)
        >>> print(f'{building} / {storey}: {elevation} mm')

    Returns:
        The elevation in model units (mm). -1.0 if the building or storey does not exist, 0.0
        without an IFC license.
    """

def get_ifc2x3_element_type_string(entity_type: ifc_2x3_element_type) -> str:
    """Get the IFC entity name of an IFC entity type.

    Converts a type, for example from `bim_controller.get_ifc2x3_element_type()`, into the IFC
    entity name written to IFC files. Pure lookup; no element is involved. Use
    `bim_controller.get_ifc2x3_element_type_display_string()` for the readable name. Requires an IFC
    license.

    Parameters:
        entity_type: The IFC entity type to convert, e.g. from
            `bim_controller.get_ifc2x3_element_type()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element_id)
        >>> print(bc.get_ifc2x3_element_type_string(ifc_type))

    Returns:
        The IFC entity name string for the type, or an empty string without an IFC license.
    """

def get_ifc2x3_element_type_display_string(entity_type: ifc_2x3_element_type) -> str:
    """Get the display name of an IFC entity type.

    Converts a type, for example from `bim_controller.get_ifc2x3_element_type()`, into the name
    shown to users in the cadwork interface. Pure lookup; no element is involved. Use
    `bim_controller.get_ifc2x3_element_type_string()` for the IFC entity name. Requires an IFC
    license.

    Parameters:
        entity_type: The IFC entity type to convert, e.g. from
            `bim_controller.get_ifc2x3_element_type()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element_id)
        >>> print(bc.get_ifc2x3_element_type_display_string(ifc_type))

    Returns:
        The display name string for the type, or an empty string without an IFC license.
    """

def get_all_buildings() -> list[str]:
    """Get the names of all buildings in the document.

    Use the names with `bim_controller.get_all_storeys()` and the other building and storey
    functions. No license is required.

    Examples:
        >>> import bim_controller as bc

        >>> for building in bc.get_all_buildings():
        ...     print(building, bc.get_all_storeys(building))

    Returns:
        List of building names in document order; empty list if there are none.
    """

def get_all_storeys(building: str) -> list[str]:
    """Get the names of all storeys of a building.

    Get the building names from `bim_controller.get_all_buildings()`. No license is required.

    Parameters:
        building: Name of an existing building.

    Examples:
        >>> import bim_controller as bc

        >>> storeys = bc.get_all_storeys('Building A')
        >>> if not storeys:
        ...     print('Unknown building or no storeys')

    Returns:
        List of storey names; empty list if the building does not exist.
    """

def get_element_id_from_base64_ifc_guid(base_64_ifc_guid: str) -> ElementId:
    """Find the element with a given 22-character IFC GUID.

    Use it to map a GUID from an IFC file back to a cadwork element. Only elements that carry an IFC
    GUID can be found; `bim_controller.get_ifc_base64_guid()` creates one if missing. If several
    elements match, the first one is returned. A console message is printed if the GUID does not
    have exactly 22 characters. No license is required.

    Parameters:
        base_64_ifc_guid: IFC GUID in its 22-character base64 form, as returned by
            `bim_controller.get_ifc_base64_guid()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> guid = bc.get_ifc_base64_guid(element_id)
        >>> found_id = bc.get_element_id_from_base64_ifc_guid(guid)
        >>> print(found_id == element_id)

    Returns:
        The element ID, or 0 if the string is empty, not 22 characters long or no element has that
        GUID.
    """

def get_ifc_base64_guid(element_id: ElementId) -> str:
    """Get the IFC GUID of an element in its 22-character base64 form.

    This is the form used inside IFC files. If the element has no IFC GUID yet, one is generated and
    stored on the element. Use `bim_controller.get_element_id_from_base64_ifc_guid()` to look the
    element up again. No license is required.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, bc.get_ifc_base64_guid(element_id))

    Returns:
        The 22-character GUID string, or an empty string if the element ID is invalid.
    """

def get_ifc_predefined_type(element_id: ElementId) -> 'ifc_predefined_type':
    """Get the IFC predefined type of an element.

    The predefined type refines the element's IFC class, for example a beam versus a joist. Change
    it with `bim_controller.set_ifc_predefined_type()`. Requires an IFC license.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> predefined_type = bc.get_ifc_predefined_type(element_id)

    Returns:
        The element's ifc_predefined_type. For an invalid element ID, an element without IFC data or
        a missing IFC license, the returned ifc_predefined_type holds no type.
    """

def set_ifc_predefined_type(element_id_list: list[ElementId], predefined_type: ifc_predefined_type) -> None:
    """Set the IFC predefined type on elements.

    The type is written without any validation against the element's IFC class, so make sure it is
    valid for each element. Pass only IDs of existing elements that carry IFC data. Requires an IFC
    license; without it nothing happens. Read the value back with
    `bim_controller.get_ifc_predefined_type()`.

    Parameters:
        element_id_list: List of element IDs to modify, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        predefined_type: The ifc_predefined_type to set on every listed element, created with
            `cadwork.ifc_predefined_type` and one of its `set_*` methods.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> predefined_type = cadwork.ifc_predefined_type()
        >>> predefined_type.set_member()
        >>> bc.set_ifc_predefined_type(selected_elements, predefined_type)
    """

def delete_storey(building: str, storey: str) -> bool:
    """Delete a storey from a building.

    A storey cannot be deleted if it is the last storey of its building, still has elements
    assigned, or is the active storey. Updates the BIM structure view and marks the document as
    modified. Move elements to another storey with `bim_controller.set_building_and_storey()` first,
    and change the active storey with `bim_controller.set_active_storey()` if needed. No license is
    required.

    Parameters:
        building: Name of the building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of the storey to delete, e.g. from `bim_controller.get_all_storeys()`.

    Examples:
        >>> import bim_controller as bc

        >>> if bc.delete_storey('Building A', 'Level 2'):
        ...     print('Storey deleted')
        ... else:
        ...     print('Not deleted: missing, last, in use or active storey')

    Returns:
        True if the storey was deleted. False if the building or storey does not exist or a
        restriction above applies.
    """

def delete_building(building: str) -> bool:
    """Delete a building together with its storeys.

    A building cannot be deleted if elements are assigned to any of its storeys or if it contains
    the active storey. Its storeys are deleted with it. Updates the BIM structure view and marks the
    document as modified. No license is required.

    Parameters:
        building: Name of the building to delete, e.g. from `bim_controller.get_all_buildings()`.

    Examples:
        >>> import bim_controller as bc

        >>> if not bc.delete_building('Old building'):
        ...     print('Not deleted: missing, in use or active building')

    Returns:
        True if the building was deleted. False if the building does not exist, is in use or is the
        active one.
    """

def rename_storey(building: str, storey: str, new_storey: str) -> bool:
    """Rename a storey of a building.

    Fails if the new name is already used by another storey of the same building; the same storey
    name may exist in different buildings. Elements stay assigned. Updates the BIM structure view
    and marks the document as modified. No license is required.

    Parameters:
        building: Name of the building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Current name of the storey, e.g. from `bim_controller.get_all_storeys()`.
        new_storey: New name of the storey.

    Examples:
        >>> import bim_controller as bc

        >>> if not bc.rename_storey('Building A', 'Level 1', 'Ground floor'):
        ...     print('Rename failed: unknown storey or name already used')

    Returns:
        True if the storey was renamed. False if the building or storey does not exist or the new
        name already exists in that building.
    """

def rename_building(building: str, new_building: str) -> bool:
    """Rename a building.

    Fails if the new name is already used by another building. Storeys and element assignments stay
    as they are. Updates the BIM structure view and marks the document as modified. No license is
    required.

    Parameters:
        building: Current name of the building, e.g. from `bim_controller.get_all_buildings()`.
        new_building: New name of the building.

    Examples:
        >>> import bim_controller as bc

        >>> if not bc.rename_building('Building A', 'Main house'):
        ...     print('Rename failed: unknown building or name already used')

    Returns:
        True if the building was renamed. False if the building does not exist or the new name
        already exists.
    """

def set_active_storey(building: str, storey: str) -> None:
    """Set the active building and storey.

    The active storey is the storey that is shown as current in the BIM structure and the cadwork
    toolbar. If the building or storey does not exist, the active storey is left unchanged and no
    error is raised. Marks the document as modified and updates the BIM structure view. Read it back
    with `bim_controller.get_active_storey()` and `bim_controller.get_active_building()`.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of a storey within that building, e.g. from `bim_controller.get_all_storeys()`.

    Examples:
        >>> import bim_controller as bc

        >>> bc.set_active_storey('Building A', 'Level 1')
        >>> print(bc.get_active_building(), bc.get_active_storey())
    """

def get_active_storey() -> str:
    """Get the name of the active storey.

    The active storey is set with `bim_controller.set_active_storey()`. Use
    `bim_controller.get_active_building()` for the building it belongs to. No license is required.

    Examples:
        >>> import bim_controller as bc

        >>> print(bc.get_active_building(), '/', bc.get_active_storey())

    Returns:
        The active storey name.
    """

def get_active_building() -> str:
    """Get the name of the active building.

    The active building is the building that contains the active storey. Change it with
    `bim_controller.set_active_storey()`. No license is required.

    Examples:
        >>> import bim_controller as bc

        >>> active_building = bc.get_active_building()
        >>> print(bc.get_all_storeys(active_building))

    Returns:
        The active building name.
    """

def get_finished_floor_thickness(building: str, storey: str) -> float:
    """Get the finished floor thickness of a storey.

    The finished floor thickness is a property of the storey in the BIM structure. Change it with
    `bim_controller.set_finished_floor_thickness()`. No license is required.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of a storey of that building, e.g. from `bim_controller.get_all_storeys()`.

    Examples:
        >>> import bim_controller as bc

        >>> thickness = bc.get_finished_floor_thickness('Building A', 'Level 1')
        >>> if thickness < 0:
        ...     print('Unknown building or storey')

    Returns:
        The thickness in model units (mm). -1.0 if the building or storey does not exist.
    """

def set_finished_floor_thickness(building: str, storey: str, finished_floor_thickness: float) -> None:
    """Set the finished floor thickness of a storey.

    If the building or storey does not exist, nothing is changed and no exception is raised. Marks
    the document as modified on success. Read the value back with
    `bim_controller.get_finished_floor_thickness()`. No license is required.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of a storey of that building, e.g. from `bim_controller.get_all_storeys()`.
        finished_floor_thickness: New thickness in model units (mm).

    Examples:
        >>> import bim_controller as bc

        >>> bc.set_finished_floor_thickness('Building A', 'Level 1', 50.0)
        >>> print(bc.get_finished_floor_thickness('Building A', 'Level 1'))
    """

def get_elements_for_storey(building: str, storey: str) -> list[ElementId]:
    """Get the IDs of the elements assigned to a storey.

    Returns the elements that were assigned with `bim_controller.set_building_and_storey()` or in
    the BIM structure view. No license is required.

    Parameters:
        building: Name of an existing building, e.g. from `bim_controller.get_all_buildings()`.
        storey: Name of a storey of that building, e.g. from `bim_controller.get_all_storeys()`.

    Examples:
        >>> import bim_controller as bc

        >>> element_ids = bc.get_elements_for_storey('Building A', 'Level 1')
        >>> print(f'{len(element_ids)} elements on Level 1')

    Returns:
        List of element IDs assigned to the storey; empty list if the building or storey does not
        exist or the storey has no elements.
    """

def export_ifc4(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC4 file, showing a progress bar.

    Exports the listed elements, independent of which elements are active, using the IFC export
    settings stored in the document and the Reference View. A progress window with a cancel button
    is shown. An element ID of 0 is skipped. Requires an IFC license. For an export without the
    window use `bim_controller.export_ifc4_silently()`.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if bc.export_ifc4(element_ids, 'C:/exports/model_ifc4.ifc'):
        ...     print('IFC4 export finished')

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if it was canceled or the file could not be written.
    """

def export_ifc2x3(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC2x3 file, showing a progress bar.

    Exports the listed elements, independent of which elements are active, using the IFC export
    settings stored in the document and the Coordination View. A progress window with a cancel
    button is shown. An element ID of 0 is skipped. Requires an IFC license. For an export without
    the window use `bim_controller.export_ifc2x3_silently()`.

    Parameters:
        element_id_list: List of IDs of existing elements to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the IFC file to write.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if bc.export_ifc2x3(element_ids, 'C:/exports/model_2x3.ifc'):
        ...     print('IFC2x3 export finished')

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if it was canceled or the file could not be written.
    """

def load_ifc_export_settings(file_path: str) -> bool:
    """Load an IFC export settings file into the document.

    Has the same effect as pressing Load settings and then OK in the IFC export dialog. The settings
    are stored in the document and used by the next IFC exports, including the silent ones, and the
    file's base name becomes the current settings name shown in the dialog. Call
    `bim_controller.get_ifc_options()` again afterwards to see the loaded values. An option that the
    file omits is read as unchecked, not kept at its previous value. No license is required.

    Parameters:
        file_path: Absolute path of an XML settings file saved with Save settings in the IFC export
            dialog (root element IfcExportSettings).

    Examples:
        >>> import bim_controller as bc

        >>> if bc.load_ifc_export_settings('C:/settings/ifc_export_wood.xml'):
        ...     options = bc.get_ifc_options()
        ...     print(options.get_ifc_options_properties().get_export_quantity_sets())
        ... else:
        ...     print('Settings file rejected')

    Returns:
        True if the settings were applied. False if the file does not exist, cannot be opened (for
        example a directory or locked file), is not valid XML or has a different root element; the
        document settings are then unchanged.
    """
