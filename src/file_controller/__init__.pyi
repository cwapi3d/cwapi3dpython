"""Interchange with external 3D and CAD file formats.

Handles import and export of geometry between cadwork and third-party
formats (3DC, STEP, SAT, Rhino, BTL, BXF, DXF, DSTV, FBX, OBJ, STL,
GLB, WebGL, variants, ...). Concerned only with neutral-format data
exchange — BIM-specific (IFC) workflows live in bim_controller, and
shop-drawing 2D exports live in shop_drawing_controller.
"""

from cadwork.import_3dc_options import import_3dc_options
from cadwork.point_3d import point_3d
from cadwork.bim_team_upload_result import bim_team_upload_result
from cadwork.dxf_layer_format_type import dxf_layer_format_type
from cadwork.dxf_export_version import dxf_export_version
from cadwork.display_attribute import display_attribute
from cadwork.api_types import *
from cadwork.file_export_options import file_export_options
from cadwork.iges_export_options import iges_export_options
from cadwork.sat_export_options import sat_export_options
from cadwork.step_export_options import step_export_options

def export_stl_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the given elements to an STL file.

    Only beams, panels and other elements with a beam-like cross-section are written; all other
    element types (nodes, lines, surfaces and so on) are left out of the file. The export works on
    the visible model: all visible elements are hidden, the listed elements are shown, the file is
    written, and then the elements that were visible before are shown again. Listed elements that
    were hidden before stay visible afterwards. Element IDs that do not exist are skipped. The
    script gets no feedback: nothing is returned and a failed write is not reported.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the STL file to write. It is used as given, no extension is added.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.stl"
        >>> fc.export_stl_file(selected_elements, output_path)
    """

def import_step_file(file_path: str, scale_factor: float) -> list[ElementId]:
    """Import a STEP file and return the IDs of the new elements.

    Requires a STEP license; without it a message is printed in the cadwork console and an empty
    list is returned. When the reader finishes, a message reports how many elements were imported
    and how many were faulty; use `file_controller.import_step_file_with_message_option()` to
    suppress it. The import is one undo step, and the new elements are shown in the 3D view when
    automatic display refresh is on.

    Parameters:
        file_path: Full path of the existing STEP file to read.
        scale_factor: Factor applied to the coordinates while reading, e.g. 1.0 for a file already
            in mm.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_step_file("C:/Temp/cadwork_import/part.stp", 1.0)
        >>> if new_ids:
        ...     print(f"Imported {len(new_ids)} elements")
        ... else:
        ...     print("Nothing imported (no STEP license, bad path or empty file)")

    Returns:
        List of IDs of the imported elements. Empty list without a STEP license, for an empty path,
        or when the file yields no elements.
    """

def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> list[ElementId]:
    """Import a STEP file and optionally suppress the result message.

    Same as `file_controller.import_step_file()`, with control over the message the reader shows
    when it is finished (number of imported and faulty elements). Requires a STEP license; without
    it an empty list is returned. The import is one undo step.

    Parameters:
        file_path: Full path of the existing STEP file to read.
        scale_factor: Factor applied to the coordinates while reading, e.g. 1.0 for a file already
            in mm.
        hide_message: True to suppress the result message, so the script does not wait for the user.
            False to show it.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_step_file_with_message_option(
        ...     "C:/Temp/cadwork_import/part.stp", 1.0, True
        ... )
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list without a STEP license, for an empty path,
        or when the file yields no elements.
    """

def export_webgl(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export the given elements as a WebGL HTML file.

    The extension .html is appended to the path if it is missing. The camera of the current 3D view,
    the project's geolocation and address and the global WebGL export settings are written into the
    file. Set the settings with `file_controller.load_webgl_preset_file()` and
    `file_controller.set_webgl_hierarchy()` before exporting. Element IDs that do not exist are
    skipped.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the HTML file to write; .html is appended if missing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.html"
        >>> success = fc.export_webgl(selected_elements, output_path)
        >>> if success:
        >>>     print("WebGL export completed successfully")

    Returns:
        True if the model was exported, False otherwise.
    """

def export_3d_file(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export the given elements to a cadwork 3D file.

    The extension .3d is appended to the path if it is missing. Element IDs that do not exist are
    skipped. Use `file_controller.export_3dc_file()` for the 3DC catalog format.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the 3D file to write; .3d is appended if missing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3d"
        >>> success = fc.export_3d_file(selected_elements, output_path)
        >>> if success:
        >>>     print("3D file export completed successfully")

    Returns:
        True if the file was written, False otherwise.
    """

def import_sat_file(file_path: str, scale_factor: float, binary: bool) -> list[ElementId]:
    """Import an ACIS SAT file and return the IDs of the new elements.

    Each body in the file becomes one element. If some bodies cannot be converted, a message box
    reports the number of imported and faulty bodies (unless messages are switched off in the
    document settings, then it is only logged). The import is one undo step, and the new elements
    are shown when automatic display refresh is on. `file_controller.import_sat_file_silently()` is
    the variant for scripts.

    Parameters:
        file_path: Full path of the existing SAT file to read.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling.
        binary: True if the file is a binary SAT file, False if it is a text SAT file.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_sat_file("C:/Temp/cadwork_import/part.sat", 1.0, True)
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list for an empty path or when the file yields
        no elements.
    """

def import_3dc_file(file_path: str) -> list[ElementId]:
    """Import a 3D or 3DC file and return the IDs of the new elements.

    Uses the default import options (saved 2D planes and export solids imported, position numbers
    reset), the same as an untouched `file_controller.get_import_3dc_options()` object; use
    `file_controller.import_3dc_file_with_options()` to change them. The file type comes from the
    extension (.3d or .3dc). Saved scenes in the file are never imported. Additional models,
    auxiliary objects, letter objects and nesting or optimization lists in the file are dropped;
    caddy and graphical objects are inserted but not returned. No undo step is created.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_3dc_file("C:/Temp/cadwork_import/building.3dc")
        >>> if not new_ids:
        ...     print("Nothing imported")

    Returns:
        List of IDs of the imported elements. Empty list for an empty path.
    """

def import_rhino_file(file_path: str, without_dialog: bool) -> list[ElementId]:
    """Import a Rhino 3DM file and return the IDs of the new elements.

    Requires a Rhino license; without it a message is printed in the cadwork console and an empty
    list is returned. With without_dialog=True the file is read directly and the Rhino settings
    dialog and information message boxes are skipped. With False the file chooser (preselected with
    the path), the Rhino settings dialog and message boxes can appear and the script waits until the
    user closes them. The new elements are shown when automatic display refresh is on. No undo step
    is created.

    Parameters:
        file_path: Full path of the existing Rhino (.3dm) file to read.
        without_dialog: True to import without any dialog, False to allow the interactive dialogs.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_rhino_file("C:/Temp/cadwork_import/model.3dm", True)
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list without a Rhino license or for an empty
        path.
    """

def export_step_file(
    element_id_list: list[ElementId], file_path: str, scale_factor: float, version: int, text_mode: bool
) -> None:
    """Export the given elements to a STEP file.

    Requires a STEP license; without it a message is printed in the cadwork console and nothing is
    written. Element IDs that do not exist are skipped. Containers and export solids are skipped
    too. For drillings cut into the bodies use `file_controller.export_step_file_cut_drillings()`,
    for SAT, STEP or IGES with options `file_controller.export_file_with_options()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the STEP file to write.
        scale_factor: Factor applied to the coordinates in the file, e.g. 1.0 for no scaling.
        version: STEP schema: 214 for AP214, 203 for AP203. The value is passed on unchecked.
        text_mode: Has no effect; the writer ignores it.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.stp"
        >>> scale_factor = 1_000.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> fc.export_step_file(selected_elements, output_path, scale_factor, version, text_mode)
    """

def import_3dz_file(file_path: str) -> None:
    """Import a 3DZ file into the current model.

    The file is read by the 3DZ import module. The new elements are shown when automatic display
    refresh is on. Their IDs are not returned; elements the file replaces are not reported either.
    No undo step is created.

    Parameters:
        file_path: Full path of the existing 3DZ file to read.

    Examples:
        >>> import file_controller as fc

        >>> fc.import_3dz_file("C:/Temp/cadwork_import/model.3dz")
    """

def export_obj_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the given elements to an OBJ file.

    The export works on the visible model: all visible elements are hidden, the listed elements are
    shown, the file is written, and then the elements that were visible before are shown again.
    Listed elements that were hidden before stay visible afterwards. Graphical objects (imported
    reference models) and element lights are not written. Textures are written as PNG. Element IDs
    that do not exist are skipped. Nothing is returned, so a failed write is not reported.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the OBJ file to write. It is used as given, no extension is added.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.obj"
        >>> fc.export_obj_file(selected_elements, output_path)
    """

def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> list[ElementId]:
    """Import an ACIS SAT file with silent body conversion and return the new element IDs.

    Same as `file_controller.import_sat_file()`, but the body conversion runs in silent mode so that
    messages raised during conversion are suppressed. The import is one undo step, and the new
    elements are shown when automatic display refresh is on.

    Parameters:
        file_path: Full path of the existing SAT file to read.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling.
        binary: True if the file is a binary SAT file, False if it is a text SAT file.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_sat_file_silently(
        ...     "C:/Temp/cadwork_import/part.sat", 1.0, False
        ... )
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list for an empty path or when the file yields
        no elements.
    """

def export_fbx_file(element_id_list: list[ElementId], file_path: str, fbx_format: int) -> None:
    """Export the visible model to an FBX file.

    The export works on the visible model: all visible elements are hidden, the listed elements are
    shown, the file is written, and then the elements that were visible before are shown again.
    Listed elements that were hidden before stay visible afterwards. Only exportable elements are
    written. An unknown format number falls back to FBX binary. Element IDs that do not exist are
    skipped. Nothing is returned, so a failed write is not reported.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the FBX file to write. Forward slashes are converted.
        fbx_format: FBX variant: 1 = FBX binary, 2 = FBX ascii, 3 = FBX encrypted, 4 = FBX 6.0
            binary, 5 = FBX 6.0 ascii, 6 = FBX 6.0 encrypted. Other values use 1.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.fbx"
        >>> fbx_format = 1  # FBX binary format
        >>> fc.export_fbx_file(selected_elements, output_path, fbx_format)

        >>> # Export as ASCII format
        >>> fbx_format = 2  # FBX ascii format
        >>> fc.export_fbx_file(selected_elements, output_path, fbx_format)
    """

def clear_errors() -> None:
    """Clear the error messages recorded by the file controller.

    Some functions record an error code and message when they cannot do their job;
    `file_controller.export_btl_file_for_nesting()` does so when no BTL license is available. This
    empties that list. It does not affect files or elements.

    Examples:
        >>> import file_controller as fc

        >>> fc.clear_errors()
        >>> fc.export_btl_file_for_nesting("C:/Temp/cadwork_export/nesting.btl")
    """

def import_3dc_file_with_glide(file_path: str) -> list[ElementId]:
    """Import a 3D or 3DC file and let the user place the new elements.

    The elements are inserted and shown, then an interactive move starts from the origin: the user
    picks the new position in the 3D view and the script waits until that is done. The file type
    comes from the extension (.3d or .3dc); for .3dc the materials stored in the file are not
    imported. The returned list is unfiltered, unlike `file_controller.import_3dc_file()`. No undo
    step is created.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.

    Examples:
        >>> import file_controller as fc

        >>> new_ids = fc.import_3dc_file_with_glide("C:/Temp/cadwork_import/module.3dc")
        >>> print(len(new_ids), "elements placed")

    Returns:
        List of IDs of the imported elements. Empty list for an empty path.
    """

def import_btl_file(file_path: str) -> None:
    """Import a BTL file into the current model.

    The file is read by the BTL import module. Nothing happens if that module is not available. The
    created elements are not returned. For nesting use
    `file_controller.import_btl_file_for_nesting()`.

    Parameters:
        file_path: Full path of the existing BTL file to read.

    Examples:
        >>> import file_controller as fc

        >>> fc.import_btl_file("C:/Temp/cadwork_import/beams.btl")
    """

def export_3dc_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the given elements to a 3DC file.

    The extension .3dc is appended to the path if it is missing. Element IDs that do not exist are
    skipped. Use `file_controller.export_3d_file()` for the 3D format; read 3DC files back with
    `file_controller.import_3dc_file()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Path of the 3DC file to write; .3dc is appended if missing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dc"
        >>> fc.export_3dc_file(selected_elements, output_path)
    """

def import_btl_file_for_nesting(file_path: str) -> None:
    """Import a BTL file for nesting.

    The file is read by the BTL import module. Nothing happens if that module is not available. The
    created elements are not returned. `file_controller.export_btl_file_for_nesting()` is the
    matching export.

    Parameters:
        file_path: Full path of the existing BTL file to read.

    Examples:
        >>> import file_controller as fc

        >>> fc.import_btl_file_for_nesting("C:/Temp/cadwork_import/nesting.btl")
    """

def export_btl_file_for_nesting(file_path: str) -> None:
    """Export the active elements to a BTL file for nesting.

    Requires a BTL license; without it nothing is written and an error is recorded (see
    `file_controller.clear_errors()`). Only active, visible construction elements with a beam-like
    cross-section (beams, panels and other elements of the beam class) that have a production list
    number are exported, so activate the wanted elements first.

    Parameters:
        file_path: Full path of the BTL file to write. Forward slashes are accepted.

    Examples:
        >>> import file_controller as fc

        >>> output_path = r"C:/exports/nesting_project.btl"
        >>> fc.export_btl_file_for_nesting(output_path)
    """

def export_rhino_file(
    element_id_list: list[ElementId],
    file_path: str,
    version: int,
    use_default_assignment: bool,
    write_standard_attributes: bool,
) -> None:
    """Export the given elements to a Rhino 3DM file.

    Requires a Rhino license; without it a message is printed in the cadwork console and nothing is
    written. Element IDs that do not exist are skipped. During the export only the listed elements
    are active; the previous activation state is restored afterwards. Use
    `file_controller.export_rhino_file_with_options()` to control how detailed the geometry is.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the 3DM file to write.
        version: Rhino version: 5, 6, 7 or 8. Any other value writes version 5.
        use_default_assignment: True to map the cadwork attributes to Rhino user attributes with the
            default mapping, False for no mapping.
        write_standard_attributes: Has no effect; the value is not read.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dm"
        >>> version = 8  # Rhino version
        >>> use_default_assignment = True
        >>> write_standard_attributes = False
        >>> fc.export_rhino_file(selected_elements, output_path, version, use_default_assignment, write_standard_attributes)
    """

def import_bxf_file(file_path: str, insert_position: point_3d) -> list[ElementId]:
    """Import a Blum BXF file and return the IDs of the new elements.

    Reads the file with the saved Blum exchange settings (see
    `file_controller.get_blum_export_path()`) and moves all imported elements by insert_position.
    The import is one undo step and the file is recorded as an import source of the document.
    Returns an empty list if the file cannot be read.

    Parameters:
        file_path: Full path of the existing BXF file to read.
        insert_position: Offset in mm added to every imported element, as a `point_3d`. Use
            `point_3d(0, 0, 0)` to keep the positions stored in the file.

    Examples:
        >>> import cadwork
        >>> import file_controller as fc

        >>> position = cadwork.point_3d(1000.0, 2000.0, 0.0)
        >>> new_ids = fc.import_bxf_file("C:/Temp/cadwork_import/cabinet.bxf", position)
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list if reading fails.
    """

def get_blum_export_path() -> str:
    """Get the Blum export path from the stored Blum exchange settings.

    The value is read from the saved Blum exchange settings file on every call, so it reflects the
    last `file_controller.set_blum_export_path()` call and the setting in the cadwork Blum dialog.

    Examples:
        >>> import file_controller as fc

        >>> blum_path = fc.get_blum_export_path()
        >>> print("Blum export path:", blum_path)

    Returns:
        The configured export path as a string. A path that was never set is returned as stored
        (likely empty).
    """

def set_blum_export_path(path: str) -> None:
    """Set the Blum export path in the stored Blum exchange settings.

    The path is written to the Blum exchange settings file, so it stays in effect for later sessions
    and documents. No check is made that the folder exists. Read the value back with
    `file_controller.get_blum_export_path()`.

    Parameters:
        path: Folder or path to store as Blum export path.

    Examples:
        >>> import file_controller as fc

        >>> fc.set_blum_export_path("C:/Temp/blum_export")
        >>> print(fc.get_blum_export_path())
    """

def export_sat_file(
    element_id_list: list[ElementId], file_path: str, scale_factor: float, binary: bool, version: int
) -> None:
    """Export the given elements to an ACIS SAT file.

    The file is created or truncated at the path, no extension is added and the folder is not
    created. Element IDs that do not exist are skipped. Unlike the STEP exports there is no license
    check and containers or export solids are not filtered out. Drillings are exported as they are;
    use `file_controller.export_sat_file_cut_drillings()` to cut them into the bodies. Read files
    back with `file_controller.import_sat_file()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the SAT file to write.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling.
        binary: True to write a binary SAT file, False for a human readable text file.
        version: ACIS version as a number: 3400 (v34.0), 3300 (v33.0), 3200 (v32.0) or 2100 (v21.0),
            see `sat_export_options`. The value is passed on unchecked.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.sat"
        >>> scale_factor = 1.0
        >>> binary_format = True
        >>> version = 25000  # SAT version
        >>> fc.export_sat_file(selected_elements, output_path, scale_factor, binary_format, version)
    """

def export_glb_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the visible model to a GLB file.

    The export works on the visible model: all visible elements are hidden, the listed elements are
    shown, the file is written, and then the elements that were visible before are shown again.
    Listed elements that were hidden before stay visible afterwards. Only exportable elements are
    written. The model is exported through a temporary FBX file that is converted to GLB with an
    external converter and deleted afterwards; an existing GLB file is removed first. Element IDs
    that do not exist are skipped. A progress bar is shown during the export. Nothing is returned,
    so a failed conversion is not reported.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the GLB file to write. Forward slashes are converted.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.glb"
        >>> fc.export_glb_file(selected_elements, output_path)
    """

def import_variant_file(file_path: str, insert_position: point_3d) -> list[ElementId]:
    """Import a variant (.val) file, build it and return the new element IDs.

    Variants are parametric element groups defined in a .val file. The variant is built with the
    parameters stored in the file, added to the document and moved by insert_position; the new
    elements are shown when automatic display refresh is on. Only .val files are supported: other
    extensions and files that cannot be loaded return an empty list.

    Parameters:
        file_path: Full path of the existing .val file to read.
        insert_position: Offset in mm applied to the variant, as a `point_3d`.

    Examples:
        >>> import cadwork
        >>> import file_controller as fc

        >>> position = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> new_ids = fc.import_variant_file("C:/Temp/cadwork_import/stair.val", position)
        >>> if not new_ids:
        ...     print("Variant could not be imported")

    Returns:
        List of IDs of the created elements. Empty list on failure.
    """

def import_element_light(file_path: str, insert_position: point_3d) -> int:
    """Import a lightweight visualization element from a file and return its ID.

    An element light is a display-only model (for example from an OBJ file) that carries no cadwork
    geometry. The element is created, loaded and moved by insert_position. OBJ files are prepared
    first with a progress bar, which can take a while. Returns 0 for an empty path or an unsupported
    file format.

    Parameters:
        file_path: Full path of the existing model file to read.
        insert_position: Offset in mm the element is moved by, as a `point_3d`.

    Examples:
        >>> import cadwork
        >>> import file_controller as fc

        >>> position = cadwork.point_3d(500.0, 0.0, 0.0)
        >>> element_id = fc.import_element_light("C:/Temp/cadwork_import/furniture.obj", position)
        >>> if element_id == 0:
        ...     print("Import failed")

    Returns:
        ID of the new element, or 0 on failure.
    """

def export_rhino_file_with_options(
    element_id_list: list[ElementId],
    file_path: str,
    version: int,
    use_default_assignment: bool,
    write_standard_attributes: bool,
    rhino_options: None,
) -> None:
    """Export the given elements to a Rhino 3DM file with level-of-detail options.

    Like `file_controller.export_rhino_file()`, plus a `cadwork.rhino_options` object that controls
    how detailed the geometry is. Requires a Rhino license; without it nothing is written. Element
    IDs that do not exist are skipped. During the export only the listed elements are active; the
    previous activation state is restored afterwards. The options object must be valid; passing None
    is not supported.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the 3DM file to write.
        version: Rhino version: 5, 6, 7 or 8. Any other value writes version 5.
        use_default_assignment: True to map the cadwork attributes to Rhino user attributes with the
            default mapping, False for no mapping.
        write_standard_attributes: Has no effect; the value is not read.
        rhino_options: `cadwork.rhino_options` object. Its flags decide whether end types
            (lengthenings and tenons) are materialized, and whether end type counterparts
            (mortises), drillings, MEP installations and openings are cut into the bodies.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dm"
        >>> version = 8  # Rhino version
        >>> use_default_assignment = True
        >>> write_standard_attributes = False
        >>> rhino_options = None  # Use default options
        >>> fc.export_rhino_file_with_options(selected_elements, output_path, version, use_default_assignment, write_standard_attributes, rhino_options)
    """

def import_3dc_file_with_options(file_path: str, import_3dc_options: import_3dc_options) -> list[ElementId]:
    """Import a 3D or 3DC file using import options.

    The file type comes from the extension (.3d or .3dc). Saved scenes in the file are never
    imported, whatever the options say. Additional models, auxiliary objects, letter objects and
    nesting or optimization lists are dropped; caddy and graphical objects are inserted but not
    returned. No undo step is created.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.
        import_3dc_options: Options object from `file_controller.get_import_3dc_options()`, with the
            flags you want changed.

    Examples:
        >>> import file_controller as fc

        >>> options = fc.get_import_3dc_options()
        >>> options.set_reset_position_numbers(False)
        >>> new_ids = fc.import_3dc_file_with_options(
        ...     "C:/Temp/cadwork_import/building.3dc", options
        ... )
        >>> print(len(new_ids), "elements imported")

    Returns:
        List of IDs of the imported elements. Empty list for an empty path.
    """

def get_import_3dc_options() -> import_3dc_options:
    """Create a 3DC import options object with default values.

    Defaults: import saved 2D planes on, import export solids on, reset position numbers on, import
    saved scenes on (the last has no effect, scenes are never imported). Change the flags with the
    setters of the returned object and pass it to `file_controller.import_3dc_file_with_options()`.
    This function does not read any file.

    Examples:
        >>> import file_controller as fc

        >>> options = fc.get_import_3dc_options()
        >>> options.set_import_export_solids(False)
        >>> new_ids = fc.import_3dc_file_with_options(
        ...     "C:/Temp/cadwork_import/building.3dc", options
        ... )

    Returns:
        A new `import_3dc_options` object.
    """

def load_webgl_preset_file(file_path: str) -> None:
    """Load a WebGL export preset (XML) into the global WebGL export settings.

    Applies the toolbar options, hierarchy stages, logo and export options stored in the preset file
    to the global WebGL export settings. They apply to every later `file_controller.export_webgl()`
    call; the stages can also be set with `file_controller.set_webgl_hierarchy()`. Nothing happens
    if the file cannot be opened. Unknown entries are ignored.

    Parameters:
        file_path: Full path of the existing preset XML file to read.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> fc.load_webgl_preset_file("C:/Temp/cadwork_export/webgl_preset.xml")
        >>> element_ids = ec.get_visible_identifiable_element_ids()
        >>> fc.export_webgl(element_ids, "C:/Temp/cadwork_export/model.html")
    """

def export_step_file_extrude_drillings(
    element_id_list: list[ElementId],
    file_path: str,
    scale_factor: float,
    version: int,
    text_mode: bool,
    imperial_units: bool,
) -> None:
    """Export the given elements to a STEP file with drillings cut into the bodies.

    Requires a STEP license; without it a message is printed in the cadwork console and nothing is
    written. Beams, panels and other elements with a beam-like cross-section are exported as
    temporary copies with drillings and the installations that generate processing cut into the
    body; other elements are exported as they are. Containers and export solids are skipped, as are
    IDs that do not exist. The global STEP export settings are restored after the call. Identical to
    `file_controller.export_step_file_cut_drillings()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the STEP file to write.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling. Multiplied by 100
            / 2.54 when imperial_units is True.
        version: STEP schema: 214 for AP214, 203 for AP203. Passed on unchecked.
        text_mode: Has no effect; the writer ignores it.
        imperial_units: True to write the file in imperial units, False for metric.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model_with_drillings.step"
        >>> scale_factor = 1.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> imperial_units = False
        >>> fc.export_step_file_extrude_drillings(selected_elements, output_path, scale_factor, version, text_mode, imperial_units)
    """

def export_step_file_cut_drillings(
    element_id_list: list[ElementId],
    file_path: str,
    scale_factor: float,
    version: int,
    text_mode: bool,
    imperial_units: bool,
) -> None:
    """Export the given elements to a STEP file with drillings cut into the bodies.

    Requires a STEP license; without it a message is printed in the cadwork console and nothing is
    written. Beams, panels and other elements with a beam-like cross-section are exported as
    temporary copies with drillings and the installations that generate processing cut into the
    body; other elements are exported as they are. Containers and export solids are skipped, as are
    IDs that do not exist. The global STEP export settings are restored after the call. Identical to
    `file_controller.export_step_file_extrude_drillings()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the STEP file to write.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling. Multiplied by 100
            / 2.54 when imperial_units is True.
        version: STEP schema: 214 for AP214, 203 for AP203. Passed on unchecked.
        text_mode: Has no effect; the writer ignores it.
        imperial_units: True to write the file in imperial units, False for metric.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model_cut_drillings.step"
        >>> scale_factor = 1.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> imperial_units = False
        >>> fc.export_step_file_cut_drillings(selected_elements, output_path, scale_factor, version, text_mode, imperial_units)
    """

def export_sat_file_cut_drillings(
    element_id_list: list[ElementId], file_path: str, scale_factor: float, binary: bool, version: int
) -> None:
    """Export the given elements to a SAT file with drillings cut into the bodies.

    The file is created or truncated at the path. Beams, panels and other elements with a beam-like
    cross-section are exported as temporary copies with drillings and the installations that
    generate processing cut into the body; other elements are exported as they are. IDs that do not
    exist are skipped. There is no license check. For a SAT file without cut drillings use
    `file_controller.export_sat_file()`.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the SAT file to write.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling.
        binary: True to write a binary SAT file, False for a human readable text file.
        version: ACIS version as a number: 3400 (v34.0), 3300, 3200 or 2100. Passed on unchecked.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> fc.export_sat_file_cut_drillings(
        ...     element_ids, "C:/Temp/cadwork_export/model.sat", 1.0, True, 3400
        ... )
    """

def upload_to_bim_team_and_create_share_link(element_id_list: list[ElementId]) -> bim_team_upload_result:
    """Upload the given elements to BIMteam and create a share link.

    Exports the elements to a temporary folder and uploads them to BIMteam under the name of the
    current project file. The script waits for the upload. Element IDs that do not exist are
    skipped. Check `upload_result_code` of the result: only `cadwork.bim_team_upload_result_code.ok`
    means that `share_link` holds a valid link.

    Parameters:
        element_id_list: List of element IDs to upload, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> result = fc.upload_to_bim_team_and_create_share_link(element_ids)
        >>> if result.upload_result_code == cadwork.bim_team_upload_result_code.ok:
        ...     print("Share link:", result.share_link)
        ... else:
        ...     print("Upload failed:", result.upload_result_code)

    Returns:
        A `bim_team_upload_result` with `upload_result_code` and `share_link`. On failure the code
        is not `ok` and the link is empty.
    """

def export_dxf_file(
    file_path: str, dxf_layer_format_type: dxf_layer_format_type, dxf_export_version: dxf_export_version
) -> bool:
    """Export all visible elements to a DXF file.

    Writes every visible element of the active document, regardless of the active state; hide the
    elements you do not want first. Dimensions are in mm. If nothing is visible no file is written,
    but True is returned. Failures are logged, not raised.

    Parameters:
        file_path: Full path of the DXF file to write.
        dxf_layer_format_type: `cadwork.dxf_layer_format_type`: how elements are distributed to
            layers: all on one layer, or by color, material, name, group or subgroup.
        dxf_export_version: `cadwork.dxf_export_version`: `auto_cad_r10` writes the simplified older
            format of beams and surfaces, `auto_cad_r27` the newer format.

    Examples:
        >>> import cadwork
        >>> import file_controller as fc

        >>> fc.export_dxf_file(
        ...     "C:/Temp/cadwork_export/plan.dxf",
        ...     cadwork.dxf_layer_format_type.color,
        ...     cadwork.dxf_export_version.auto_cad_r27,
        ... )

    Returns:
        True if the export succeeded, False for an unknown layer format type or a failed export.
    """

def export_dstv_file(file_path: str) -> bool:
    """Export the active elements to a DSTV file.

    Uses the saved DSTV export settings of the document and writes the elements that are active, so
    activate the elements you want first. Returns False only when the DSTV export module cannot be
    loaded; True does not guarantee that a file was written.

    Parameters:
        file_path: Full path of the file to write. The extension is not changed.

    Examples:
        >>> import file_controller as fc

        >>> if fc.export_dstv_file("C:/Temp/cadwork_export/steel.stp"):
        ...     print("DSTV export module ran")
        ... else:
        ...     print("DSTV export module not available")

    Returns:
        True if the export module ran, False if it is not available.
    """

def set_webgl_hierarchy(stage: int, attribute: display_attribute) -> None:
    """Set the display attribute used for one stage of the WebGL export hierarchy.

    The WebGL model viewer shows its element tree grouped by up to six levels. This sets which
    attribute defines one level. The setting is global and applies to later
    `file_controller.export_webgl()` calls. Stages outside 1 to 6 are silently ignored.

    Parameters:
        stage: Hierarchy level, 1 to 6.
        attribute: `cadwork.display_attribute` object whose set_* method has been called to pick the
            attribute (name, group, material, ...).

    Examples:
        >>> import cadwork
        >>> import file_controller as fc

        >>> name_attribute = cadwork.display_attribute()
        >>> name_attribute.set_name()
        >>> fc.set_webgl_hierarchy(1, name_attribute)
    """

def export_step_file_ex(
    element_list: list[ElementId], file_path: str, scale_factor: float, substract_drillings: bool
) -> None:
    """Export the given elements to a STEP file via a temporary SAT file.

    Requires a STEP license; without it a message is printed in the cadwork console and nothing is
    written. The elements are written to a temporary text SAT file (ACIS v34.0), which is converted
    to STEP and deleted. Nothing is written if the temporary file cannot be created. Element IDs
    that do not exist are skipped. Containers and export solids are not filtered out.

    Parameters:
        element_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the STEP file to write.
        scale_factor: Factor applied to the coordinates, e.g. 1.0 for no scaling.
        substract_drillings: True to cut drillings (and installations) into the bodies, False to
            export the bodies as they are.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> fc.export_step_file_ex(
        ...     element_ids, "C:/Temp/cadwork_export/model.stp", 1.0, True
        ... )
    """

def get_sat_export_options() -> sat_export_options:
    """Create a SAT export options object with default values.

    The returned `sat_export_options` holds scale factor 1.0, binary format and ACIS version 33.0,
    with level-of-detail options off. Change them with the setters, then pass the object to
    `file_controller.export_file_with_options()` to write a SAT file. This function writes nothing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> options = fc.get_sat_export_options()
        >>> options.set_binary(False)
        >>> options.set_version(options.ACIS_V34_0)
        >>> fc.export_file_with_options(element_ids, "C:/Temp/cadwork_export/model.sat", options)

    Returns:
        A new `sat_export_options` object.
    """

def get_step_export_options() -> step_export_options:
    """Create a STEP export options object with default values.

    The returned `step_export_options` holds scale factor 1.0, schema AP214 and metric units, with
    level-of-detail options off. Change them with the setters, then pass the object to
    `file_controller.export_file_with_options()` to write a STEP file (STEP license required). This
    function writes nothing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> options = fc.get_step_export_options()
        >>> options.set_version(options.AP203)
        >>> fc.export_file_with_options(element_ids, "C:/Temp/cadwork_export/model.stp", options)

    Returns:
        A new `step_export_options` object.
    """

def get_iges_export_options() -> iges_export_options:
    """Create an IGES export options object with default values.

    The returned `iges_export_options` holds scale factor 1.0 with level-of-detail options off.
    Change them with the setters, then pass the object to
    `file_controller.export_file_with_options()` to write an IGES file. This function writes
    nothing.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> options = fc.get_iges_export_options()
        >>> options.set_scale_factor(1.0)
        >>> fc.export_file_with_options(element_ids, "C:/Temp/cadwork_export/model.igs", options)

    Returns:
        A new `iges_export_options` object.
    """

def export_file_with_options(element_id_list: list[ElementId], file_path: str, options: file_export_options) -> bool:
    """Export the given elements to SAT, STEP or IGES using an options object.

    The class of the options object selects the format (`file_controller.get_sat_export_options()`,
    `file_controller.get_step_export_options()` or `file_controller.get_iges_export_options()`); the
    options also carry the level-of-detail settings (cut drillings, end types, openings, MEP). The
    path is used as given, no extension is added. Element IDs that do not exist are skipped.
    Containers and export solids are skipped. STEP needs a license. Failures, user aborts and
    warnings are written to the log, not raised.

    Parameters:
        element_id_list: List of element IDs to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        file_path: Full path of the file to write.
        options: Options object from one of the `get_*_export_options()` functions of this module.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> # Export a STEP file with all level of detail options activated
        >>> options = fc.get_step_export_options()
        >>> lod = options.get_level_of_detail_options()
        >>> lod.set_cut_drillings(True)
        >>> lod.set_materialize_end_types(True)
        >>> lod.set_cut_end_type_counterparts(True)
        >>> lod.set_cut_openings(True)
        >>> lod.set_materialize_mep_elements(True)
        >>> lod.set_cut_mep_elements(True)

        >>> options.set_scale_factor(1.0)
        >>> options.set_version(options.AP214)
        >>> options.set_imperial_units(False)

        >>> elements = ec.get_all_identifiable_element_ids()
        >>> success = fc.export_file_with_options(elements, r"C:/exports/model.stp", options)

    Returns:
        True if the file was exported, False otherwise (no STEP license, export failed or aborted by
        the user).
    """
