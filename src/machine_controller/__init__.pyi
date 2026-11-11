"""CNC and woodworking-machine output.

Covers the calculation and export of machine data for fabrication:
BTL / BTLx in their supported versions, the Hundegger family and
its variants (with optional preset files and silent operation),
and the inspection of per-element machine processings. The bridge
between the cadwork model and the shop floor.
"""

from cadwork import vertex_list
from cadwork.api_types import ElementId
from cadwork.btl_version import btl_version
from cadwork.hundegger_machine_type import hundegger_machine_type
from cadwork.panel_prefab_element_data import panel_prefab_element_data
from cadwork.panel_prefab_element_settings import panel_prefab_element_settings
from cadwork.weinmann_mfb_version import weinmann_mfb_version
from cadwork.btl_version import btl_version

def export_btl(btl_version: btl_version, file_path: str) -> None:
    """Export the visible elements to a BTL/BTLx file.

    Exports visible elements that belong to a production list (beams, panels and other elements with
    a beam-like cross-section). Missing folders are created. Nothing is exported if file_path is
    empty, the folder cannot be created or no licence exists for the version. The export may ask the
    user whether to consider multiparts or nestings, which blocks the script.

    Parameters:
        btl_version: BTL/BTLx version to export (value of cadwork.btl_version).
        file_path: Full path of the target file. The folder part is created if missing; any
            extension given here is not used.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = "C:/exports/timber_project.btlx"
        >>> mc.export_btl(btl_version, output_path)
    """

def export_weinmann_mfb(mfb_version: weinmann_mfb_version) -> None:
    """Export the visible elements to a Weinmann MFB (.wup) file.

    The file is written to the folder of the current document and named after it. Does nothing
    without a wall prefabrication licence. Visible elements are first converted to composite data.

    Parameters:
        mfb_version: Weinmann MFB version to export (value of cadwork.weinmann_mfb_version).

    Examples:
        >>> import machine_controller as mc

        >>> mfb_version = cadwork.weinmann_mfb_version.wup_3_4.value
        >>> mc.export_weinmann_mfb(mfb_version)
    """

def export_hundegger(hundeggertype: hundegger_machine_type) -> None:
    """Export the visible elements to a Hundegger file next to the current document.

    The file is written with the path and name of the current document. Same behavior as
    export_hundegger_with_file_path with that path.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.export_hundegger(hundegger_type)
    """

def export_hundegger_with_file_path(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Export the visible elements to a Hundegger file at the given path.

    Exports visible elements that belong to a production list (beams, panels and other elements with
    a beam-like cross-section). Missing folders are created. Nothing is exported if file_path is
    empty or the folder cannot be created. May show dialogs, including an overwrite prompt; use the
    silent variant to avoid them.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).
        file_path: Target path. The folder part is created if missing; the last part is used as the
            file name.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = "C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path(hundegger_type, output_path)
    """

def export_hundegger_with_file_path_and_presetting(
    hundeggertype: hundegger_machine_type, file_path: str, presetting: str
) -> None:
    """Export the visible elements to a Hundegger file using a presetting file.

    Same as export_hundegger_with_file_path, with export settings taken from a presetting. May show
    dialogs; use the silent variant to avoid them.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).
        file_path: Target path. The folder part is created if missing; the last part is used as the
            file name.
        presetting: Full path of an existing presetting .xml file, or the name of a presetting in
            the machine's MachineExport folder (.xml is appended if no extension is given).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting(hundegger_type, output_path, presetting_file)
    """

def export_btl_with_presetting(btl_version: btl_version, file_path: str, presetting: str) -> None:
    """Export the visible elements to a BTL/BTLx file using a presetting file.

    Same as export_btl, with export settings taken from a presetting. Nothing is exported if
    file_path is empty, the folder cannot be created or no licence exists for the version. May ask
    the user about multiparts or nestings, which blocks the script.

    Parameters:
        btl_version: BTL/BTLx version to export (value of cadwork.btl_version).
        file_path: Full path of the target file. The folder part is created if missing.
        presetting: Full path of an existing presetting .xml file, or the name of a presetting in
            the machine's MachineExport folder (.xml is appended if no extension is given).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = r"C:/exports/timber_project.btlx"
        >>> presetting_file = r"...3d/Machine/BTL/btl_settings.xml"
        >>> mc.export_btl_with_presetting(btl_version, output_path, presetting_file)
    """

def calculate_btl_machine_data(element_id_list: list[ElementId], btl_version: btl_version) -> None:
    """Calculate BTL/BTLx machine data (processings) for elements.

    If element_id_list is empty, all visible elements that belong to a production list are used
    instead. Does nothing without a licence for the version. Shows a progress display while running.

    Parameters:
        element_id_list: List of element IDs to calculate. Empty list means all visible
            production-list elements.
        btl_version: BTL/BTLx version (value of cadwork.btl_version).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> mc.calculate_btl_machine_data(beam_elements, btl_version)
    """

def calculate_hundegger_machine_data(element_id_list: list[ElementId], hundeggertype: hundegger_machine_type) -> None:
    """Calculate Hundegger machine data (processings) for elements.

    If element_id_list is empty, all visible elements that belong to a production list are used
    instead. Does nothing without a licence for the machine type. Shows a progress display while
    running.

    Parameters:
        element_id_list: List of element IDs to calculate. Empty list means all visible
            production-list elements.
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.calculate_hundegger_machine_data(beam_elements, hundegger_type)
    """

def load_hundegger_calculation_set(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Load a Hundegger calculation set from a file and make it the standard set.

    The loaded set is saved as the standard configuration for that machine type. Nothing is loaded
    if the file cannot be read, the machine type is invalid or no licence exists.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).
        file_path: Path of the calculation set file.
    """

def export_hundegger_with_file_path_silent(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Export the visible elements to a Hundegger file without dialogs.

    Like export_hundegger_with_file_path, but suppresses the overwrite prompt (existing files are
    overwritten) and user input while the export runs. Nothing is exported if file_path is empty or
    the folder cannot be created.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).
        file_path: Target path. The folder part is created if missing; the last part is used as the
            file name.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path_silent(hundegger_type, output_path)
    """

def export_hundegger_with_file_path_and_presetting_silent(
    hundeggertype: hundegger_machine_type, file_path: str, presetting: str
) -> None:
    """Export to a Hundegger file using a presetting, without dialogs.

    Like export_hundegger_with_file_path_and_presetting, but suppresses the overwrite prompt
    (existing files are overwritten) and user input while the export runs.

    Parameters:
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).
        file_path: Target path. The folder part is created if missing; the last part is used as the
            file name.
        presetting: Full path of an existing presetting .xml file, or the name of a presetting in
            the machine's MachineExport folder (.xml is appended if no extension is given).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting_silent(hundegger_type, output_path, presetting_file)
    """

def get_element_hundegger_processings(element_id: ElementId, hundeggertype: hundegger_machine_type) -> list[ElementId]:
    """Get the Hundegger processings of an element.

    Computes the processings for the machine type, replacing any previously computed ones on the
    element. Returns an empty list if the element ID is invalid or the processings cannot be
    computed.

    Parameters:
        element_id: ID of the element to inspect.
        hundeggertype: Hundegger machine type (value of cadwork.hundegger_machine_type).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> processings = mc.get_element_hundegger_processings(element, hundegger_type)
        >>> print(f"Found {len(processings)} Hundegger processings")

    Returns:
        List of processing IDs. Pass them as processing_id (together with this element as
        reference_element_id) to the get_processing_* functions. Empty list on failure.
    """

def get_element_btl_processings(element_id: ElementId, btl_version: btl_version) -> list[ElementId]:
    """Get the BTL/BTLx processings of an element.

    Computes the processings for the BTL version, replacing any previously computed ones on the
    element. Returns an empty list if the element ID is invalid or the processings cannot be
    computed.

    Parameters:
        element_id: ID of the element to inspect.
        btl_version: BTL/BTLx version (value of cadwork.btl_version).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> processings = mc.get_element_btl_processings(element, btl_version)
        >>> print(f"Found {len(processings)} BTL processings")

    Returns:
        List of processing IDs. Pass them as processing_id (together with this element as
        reference_element_id) to the get_processing_* functions. Empty list on failure.
    """

def get_processing_name(reference_element_id: ElementId, processing_id: ElementId) -> str:
    """Get the name of a processing of an element.

    Returns an empty string if the element ID is invalid or the element has no processing with that
    ID.

    Parameters:
        reference_element_id: ID of the element that owns the processing.
        processing_id: Processing ID from get_element_btl_processings or
            get_element_hundegger_processings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     name = mc.get_processing_name(element, processing)

    Returns:
        Name of the processing, or an empty string if not found.
    """

def get_processing_code(reference_element_id: ElementId, processing_id: ElementId) -> str:
    """Get the processing code of a processing of an element.

    Returns an empty string if the element ID is invalid or the element has no processing with that
    ID.

    Parameters:
        reference_element_id: ID of the element that owns the processing.
        processing_id: Processing ID from get_element_btl_processings or
            get_element_hundegger_processings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     code = mc.get_processing_code(element, processing)

    Returns:
        Processing code string, or an empty string if not found.
    """

def get_processing_points(reference_element_id: ElementId, processing_id: ElementId) -> vertex_list:
    """Get the points of a drilling processing.

    Only drilling processings return points: the start and end point of the drill hole. All other
    processing types, invalid IDs and unknown processing IDs return an empty list.

    Parameters:
        reference_element_id: ID of the element that owns the processing.
        processing_id: Processing ID from get_element_btl_processings or
            get_element_hundegger_processings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     points = mc.get_processing_points(element, processing)

    Returns:
        List of two points (start, end of the drilling), or an empty list.
    """

def get_processing_btl_parameter_set(reference_element_id: ElementId, processing_id: ElementId) -> list[str]:
    """Get the BTL parameter values of a processing as strings.

    Each string has the form ' Pnn:value': the two-digit parameter number and the value rounded to
    two decimals, written as an integer (value times 100) padded to 8 characters. Values out of
    range are written as 0. Returns an empty list if the element ID is invalid or the processing is
    not found.

    Parameters:
        reference_element_id: ID of the element that owns the processing.
        processing_id: Processing ID from get_element_btl_processings or
            get_element_hundegger_processings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     parameters = mc.get_processing_btl_parameter_set(element, processing)

    Returns:
        List of parameter strings, or an empty list if not found.
    """

def get_panel_prefab_element_data(element_id: ElementId) -> panel_prefab_element_data:
    """Get the panel prefabrication data of an element.

    Contains the panel prefab element type, the optional layer location and the machine calculation
    set (MFB prefab config) name. For an element without panel prefabrication data, the type is
    the none value and no layer is set. For an invalid element ID, no layer is set and the
    calculation set is an empty string.

    Parameters:
        element_id: ID of the element to read.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> data = mc.get_panel_prefab_element_data(element)
        >>> element_type = data.get_element_type()
        >>> if data.has_layer():
        >>>     layer = data.get_layer()
        >>> config = data.get_machine_calculation_set()

    Returns:
        A panel_prefab_element_data object; never None.
    """

def set_panel_prefab_element_data(element_id_list: list[ElementId], settings: panel_prefab_element_settings) -> None:
    """Set panel prefabrication data on elements.

    Only fields explicitly set on the settings object are applied; unset fields stay unchanged.
    Invalid IDs and elements without panel prefabrication data are skipped (the calculation set is
    still written to any valid element). The display is refreshed if auto refresh is on.

    Parameters:
        element_id_list: List of element IDs to modify.
        settings: Settings object with the fields to apply.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> elements = ec.get_active_identifiable_element_ids()
        >>> settings = cadwork.panel_prefab_element_settings()
        >>> settings.set_element_type(cadwork.panel_prefab_element_type.batten)
        >>> settings.set_layer(2)
        >>> settings.set_machine_calculation_set("MyMfbConfig")
        >>> mc.set_panel_prefab_element_data(elements, settings)
    """

def load_btl_calculation_set(btl_type: btl_version, file_path: str) -> None:
    """Load a BTL calculation set from a file and make it the standard set.

    The loaded set is saved as the standard configuration for that BTL version. Nothing is loaded if
    the file cannot be read, the version is invalid or no licence exists.

    Parameters:
        btl_type: BTL/BTLx version (value of cadwork.btl_version).
        file_path: Path of the calculation set file.
    """
