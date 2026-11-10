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
    """Get the IFC GUID of an element.

    This is not the 22-character form used in IFC files; use get_ifc_base64_guid for that.
    Requires an IFC license; without it a message is printed to the console and an empty string is
    returned.

    Parameters:
        element_id: ID of the element.

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

    Requires an IFC license.

    Parameters:
        element_id: ID of the element.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork # needed for ifc_2x3_element_type

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element)

    Returns:
        The element's IFC entity type. For an invalid element ID, an element without IFC data, or a
        missing IFC license, a type with value 0 is returned.
    """

def set_ifc2x3_element_type(element_id_list: list[ElementId], ifc_type: ifc_2x3_element_type) -> None:
    """Assign an IFC entity type to elements.

    Invalid element IDs and elements without IFC data are skipped silently. Requires an IFC license;
    without it nothing happens.

    Parameters:
        element_id_list: List of element IDs to modify.
        ifc_type: The IFC entity type to assign to every listed element.

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

    The IFC content is added as a single graphical (exchange) object, not converted to cadwork
    elements. Requires an IFC license.

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

    Dispatches an import request to the application and returns without checking whether the file
    could be read. Requires a BIM Manager license.

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

    Dispatches an export request to the application and returns without checking that the file was
    written. Requires a BIM Manager license.

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
    """Export elements to an IFC2x3 file, showing a progress bar.

    The export uses the elements that are active when the function is called, and element_id_list
    is ignored for the export itself. If nothing is active, the listed elements are only activated
    (they stay active afterwards). To export specific elements, use export_ifc2x3. Uses the IFC
    export settings stored in the document and shows a progress window with a cancel button.

    Parameters:
        element_id_list: List of element IDs; activated if no elements are currently active, but
            not passed to the export.
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

    The exchange objects are graphical objects that can be turned into cadwork elements with
    convert_exchange_objects. Requires an IFC license.

    Parameters:
        file_path: Path of the IFC file to import.

    Returns:
        List of exchange object IDs (the children of the imported object, not the imported object
        itself). Empty list if the file does not exist, the import fails or no IFC license is
        available.
    """

def set_storey_height(building: str, storey: str, height: float) -> None:
    """Set the elevation (height level) of a storey.

    The value is the storey's elevation in the building, not the floor-to-floor height. If the
    building or storey does not exist, nothing is changed and no exception is raised. Marks the
    document as modified. Requires an IFC license.

    Parameters:
        building: Name of the building.
        storey: Name of the storey.
        height: New elevation of the storey in model units (mm).

    Examples:
        >>> import bim_controller as bc

        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> height_millimeters = 3_500
        >>> bc.set_storey_height(building_name, storey_name, height_millimeters)
    """

def convert_exchange_objects(exchange_objects: list[ElementId]) -> list[ElementId]:
    """Convert exchange objects into cadwork elements.

    Invalid IDs are skipped. The display is refreshed if automatic refresh is on, and the BIM
    structure is updated. Requires an IFC license.

    Parameters:
        exchange_objects: List of exchange object IDs, as returned by
            import_ifc_return_exchange_objects.

    Returns:
        List of the newly created cadwork element IDs (the inputs are not included). Empty list if
        nothing could be converted or no IFC license is available.
    """

def export_ifc2x3_silently(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC2x3 file without a progress window.

    Uses the IFC export settings stored in the document and the Coordination View. Invalid element
    IDs are skipped. Does not change the element activation.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if the file could not be written.
    """

def export_ifc4_silently(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC4 file without a progress window.

    Uses the IFC export settings stored in the document and the Reference View. Invalid element IDs
    are skipped. Does not change the element activation.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if the file could not be written.
    """

def export_ifc2x3_silently_with_options(element_id_list: list[ElementId], file_path: str, options: ifc_options) -> bool:
    """Export elements to an IFC2x3 file with explicit options, without a progress window.

    The given options are applied on top of the document's IFC export settings and the result is
    saved back into the document, so they also apply to later exports. Invalid element IDs are
    skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.
        options: IFC export options, typically obtained from get_ifc_options and modified.

    Returns:
        True once the export ran, even if the file could not be written.
    """

def export_ifc4_silently_with_options(element_id_list: list[ElementId], file_path: str, options: ifc_options) -> bool:
    """Export elements to an IFC4 file with explicit options, without a progress window.

    The given options are applied on top of the document's IFC export settings and the result is
    saved back into the document, so they also apply to later exports. Invalid element IDs are
    skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.
        options: IFC export options, typically obtained from get_ifc_options and modified.

    Returns:
        True once the export ran, even if the file could not be written.
    """

def update_bmt_structure_created_elements(element_id_list: list[ElementId]) -> None:
    """Register newly created elements in the BIM structure under the active building and storey.

    Use after creating elements by script so they appear in the BIM structure.

    Parameters:
        element_id_list: List of element IDs to register.
    """

def update_bmt_structure_building_storey(element_id_list: list[ElementId]) -> None:
    """Update the BIM structure for elements using their assigned building and storey.

    Use after assigning building and storey (for example with set_building_and_storey) so the
    structure view reflects the assignment.

    Parameters:
        element_id_list: List of element IDs to update.
    """

def get_ifc_options() -> ifc_options:
    """Get the IFC export options stored in the document.

    Returns a copy: changing it does not alter the document unless you pass it to an export function
    with options. Does not show a dialog.

    Returns:
        An ifc_options object with the document's current IFC export settings (aggregation, level of
        detail, project data, properties).
    """

def set_building_and_storey(element_id_list: list[ElementId], building: str, storey: str) -> None:
    """Assign elements to a building and storey.

    The building and storey are created if they do not exist yet. Invalid element IDs are skipped.
    IFC container elements that the listed elements belong to are assigned as well. Requires an IFC
    license; without it nothing happens.

    Parameters:
        element_id_list: List of element IDs to assign.
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

    Parameters:
        element_id: ID of the element.

    Returns:
        The building name, or an empty string if the element ID is invalid or the element has no
        building assignment.
    """

def get_storey(element_id: ElementId) -> str:
    """Get the name of the storey an element is assigned to.

    Parameters:
        element_id: ID of the element.

    Returns:
        The storey name, or an empty string if the element ID is invalid or the element has no
        storey assignment.
    """

def get_storey_height(building: str, storey: str) -> float:
    """Get the elevation (height level) of a storey.

    The value is the storey's elevation in the building, not its floor-to-floor height. Requires an
    IFC license.

    Parameters:
        building: Name of the building.
        storey: Name of the storey.

    Returns:
        The elevation in model units (mm). -1.0 if the building or storey does not exist, 0.0
        without an IFC license.
    """

def get_ifc2x3_element_type_string(entity_type: ifc_2x3_element_type) -> str:
    """Get the IFC entity name of an IFC entity type.

    Pure lookup; no element is involved. Requires an IFC license.

    Parameters:
        entity_type: The IFC entity type to convert.

    Returns:
        The IFC entity name string for the type, or an empty string without an IFC license.
    """

def get_ifc2x3_element_type_display_string(entity_type: ifc_2x3_element_type) -> str:
    """Get the display name of an IFC entity type.

    Pure lookup; no element is involved. Requires an IFC license.

    Parameters:
        entity_type: The IFC entity type to convert.

    Returns:
        The display name string for the type, or an empty string without an IFC license.
    """

def get_all_buildings() -> list[str]:
    """Get the names of all buildings in the document.

    Returns:
        List of building names; empty list if there are none.
    """

def get_all_storeys(building: str) -> list[str]:
    """Get the names of all storeys of a building.

    Parameters:
        building: Name of the building.

    Returns:
        List of storey names; empty list if the building does not exist.
    """

def get_element_id_from_base64_ifc_guid(base_64_ifc_guid: str) -> ElementId:
    """Find the element with a given 22-character IFC GUID.

    If several elements match, the first one is returned. A console message is printed if the GUID
    does not have exactly 22 characters.

    Parameters:
        base_64_ifc_guid: IFC GUID in its 22-character base64 form, as returned by
            get_ifc_base64_guid.

    Returns:
        The element ID, or 0 if the string is empty, not 22 characters long or no element has that
        GUID.
    """

def get_ifc_base64_guid(element_id: ElementId) -> str:
    """Get the IFC GUID of an element in its 22-character base64 form.

    This is the form used inside IFC files.

    Parameters:
        element_id: ID of the element.

    Returns:
        The 22-character GUID string, or an empty string if the element ID is invalid.
    """

def get_ifc_predefined_type(element_id: ElementId) -> 'ifc_predefined_type':
    """Get the IFC predefined type of an element.

    Requires an IFC license.

    Parameters:
        element_id: ID of the element.

    Returns:
        The element's ifc_predefined_type. For an invalid element ID, an element without IFC data or
        a missing IFC license, the returned ifc_predefined_type holds no type.
    """

def set_ifc_predefined_type(element_id_list: list[ElementId], predefined_type: ifc_predefined_type) -> None:
    """Set the IFC predefined type on elements.

    The type is written without any validation against the element's IFC type, so you must make sure
    it is valid for each element. Pass only valid element IDs of elements that carry IFC data.
    Requires an IFC license; without it nothing happens.

    Parameters:
        element_id_list: List of element IDs to modify.
        predefined_type: The ifc_predefined_type to set on every listed element.

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
    modified.

    Parameters:
        building: Name of the building.
        storey: Name of the storey to delete.

    Returns:
        True if the storey was deleted. False if the building or storey does not exist or a
        restriction above applies.
    """

def delete_building(building: str) -> bool:
    """Delete a building.

    A building cannot be deleted if elements are assigned to any of its storeys or if it is the
    active building. Its storeys are deleted with it. Updates the BIM structure view and marks the
    document as modified.

    Parameters:
        building: Name of the building to delete.

    Returns:
        True if the building was deleted. False if the building does not exist, is in use or is the
        active one.
    """

def rename_storey(building: str, storey: str, new_storey: str) -> bool:
    """Rename a storey of a building.

    Fails if the new name is already used by another storey of the same building. Updates the BIM
    structure view and marks the document as modified.

    Parameters:
        building: Name of the building.
        storey: Current name of the storey.
        new_storey: New name of the storey.

    Returns:
        True if the storey was renamed. False if the building or storey does not exist or the new
        name already exists in that building.
    """

def rename_building(building: str, new_building: str) -> bool:
    """Rename a building.

    Fails if the new name is already used by another building. Updates the BIM structure view and
    marks the document as modified.

    Parameters:
        building: Current name of the building.
        new_building: New name of the building.

    Returns:
        True if the building was renamed. False if the building does not exist or the new name
        already exists.
    """

def set_active_storey(building: str, storey: str) -> None:
    """Set the active building and storey.

    If the building or storey does not exist, the active storey is left unchanged and no error is
    raised. Marks the document as modified and updates the BIM structure view.

    Parameters:
        building: Name of the building.
        storey: Name of the storey within that building.
    """

def get_active_storey() -> str:
    """Get the name of the active storey.

    Returns:
        The active storey name.
    """

def get_active_building() -> str:
    """Get the name of the active building.

    Returns:
        The active building name.
    """

def get_finished_floor_thickness(building: str, storey: str) -> float:
    """Get the finished floor thickness of a storey.

    Parameters:
        building: Name of the building.
        storey: Name of the storey.

    Returns:
        The thickness in model units (mm). -1.0 if the building or storey does not exist.
    """

def set_finished_floor_thickness(building: str, storey: str, finished_floor_thickness: float) -> None:
    """Set the finished floor thickness of a storey.

    If the building or storey does not exist, nothing is changed and no exception is raised.

    Parameters:
        building: Name of the building.
        storey: Name of the storey.
        finished_floor_thickness: New thickness in model units (mm).
    """

def get_elements_for_storey(building: str, storey: str) -> list[ElementId]:
    """Get the IDs of the elements assigned to a storey.

    Parameters:
        building: Name of the building.
        storey: Name of the storey.

    Returns:
        List of element IDs assigned to the storey; empty list if the building or storey does not
        exist.
    """

def export_ifc4(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC4 file, showing a progress bar.

    Uses the IFC export settings stored in the document and the Reference View, and shows a progress
    window with a cancel button. Invalid element IDs are skipped. Requires an IFC license.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if it was canceled or the file could not be written.
    """

def export_ifc2x3(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export elements to an IFC2x3 file, showing a progress bar.

    Uses the IFC export settings stored in the document and the Coordination View, and shows a
    progress window with a cancel button. Invalid element IDs are skipped. Requires an IFC license.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Path of the IFC file to write.

    Returns:
        False if the list is empty or no IFC license is available. Otherwise True once the export
        ran, even if it was canceled or the file could not be written.
    """

def load_ifc_export_settings(file_path: str) -> bool:
    """Load an IFC export settings file into the document.

    Has the same effect as pressing Load settings and then OK in the IFC export dialog. The settings
    are stored in the document and used by the next IFC exports, including the silent ones; call
    get_ifc_options again afterwards to see the loaded values. An option that the file omits is read
    as unchecked.

    Parameters:
        file_path: Absolute path of an XML settings file saved with Save settings in the IFC export
            dialog (root element IfcExportSettings).

    Returns:
        True if the settings were applied. False if the file does not exist, cannot be read, is not
        valid XML or has a different root element; the document settings are then unchanged.
    """
