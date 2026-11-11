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

    Only the listed elements are written. Element IDs that do not exist are skipped. The current
    element visibility is restored after the export.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the STL file to write.

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
    list is returned. An empty path or a file that yields no elements also returns an empty list.
    The import is added as one undo step.

    Parameters:
        file_path: Full path of the existing STEP file to read.
        scale_factor: Scale factor applied to the geometry while reading the file.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> list[ElementId]:
    """Import a STEP file, optionally suppressing the import message.

    Behaves like import_step_file. Requires a STEP license; without it an empty list is returned.
    The import is added as one undo step.

    Parameters:
        file_path: Full path of the existing STEP file to read.
        scale_factor: Scale factor applied to the geometry while reading the file.
        hide_message: True to suppress the message normally shown during the import, False to show
            it.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def export_webgl(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export the given elements as a WebGL HTML file.

    The extension .html is appended to the path if it is missing. Element IDs that do not exist are
    skipped. The result depends on the global WebGL export settings (see load_webgl_preset_file and
    set_webgl_hierarchy).

    Parameters:
        element_id_list: List of element IDs to export.
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
        True if the export succeeded, False otherwise.
    """

def export_3d_file(element_id_list: list[ElementId], file_path: str) -> bool:
    """Export the given elements to a cadwork 3D file.

    The extension .3d is appended to the path if it is missing. Element IDs that do not exist are
    skipped.

    Parameters:
        element_id_list: List of element IDs to export.
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
    """Import a SAT file and return the IDs of the new elements.

    An empty path or a file that yields no elements returns an empty list. The import is added as
    one undo step.

    Parameters:
        file_path: Full path of the existing SAT file to read.
        scale_factor: Scale factor applied to the geometry while reading the file.
        binary: True if the file is a binary SAT file, False if it is a text SAT file.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def import_3dc_file(file_path: str) -> list[ElementId]:
    """Import a 3D or 3DC file and return the IDs of the new elements.

    Uses the default import options (same as get_import_3dc_options). The file type is taken from
    the extension (.3d or .3dc). Saved scenes in the file are never imported. Auxiliary geometry
    such as caddy and graphical objects is not part of the returned list. An empty path returns an
    empty list.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def import_rhino_file(file_path: str, without_dialog: bool) -> list[ElementId]:
    """Import a Rhino 3DM file and return the IDs of the new elements.

    Requires a Rhino license; without it an empty list is returned. An empty path returns an empty
    list.

    Parameters:
        file_path: Full path of the existing Rhino (.3dm) file to read.
        without_dialog: True to import without showing the import dialog, False to show it (the
            script then waits for the user).

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def export_step_file(
    element_id_list: list[ElementId], file_path: str, scale_factor: float, version: int, text_mode: bool
) -> None:
    """Export the given elements to a STEP file.

    Requires a STEP license; without it a message is printed in the cadwork console and nothing is
    written. Element IDs that do not exist, containers and export solids are skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the STEP file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        version: STEP schema: 214 for AP214, 203 for AP203.
        text_mode: Unused.

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

    The imported elements are shown but their IDs are not returned. No undo step is created by this
    call.

    Parameters:
        file_path: Full path of the existing 3DZ file to read.
    """

def export_obj_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the given elements to an OBJ file.

    Only the listed elements are written. Element IDs that do not exist are skipped. The current
    element visibility is restored after the export.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the OBJ file to write.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.obj"
        >>> fc.export_obj_file(selected_elements, output_path)
    """

def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> list[ElementId]:
    """Import a SAT file without messages and return the IDs of the new elements.

    Same as import_sat_file but message output of the reader is suppressed. An empty path or a file
    that yields no elements returns an empty list. The import is added as one undo step.

    Parameters:
        file_path: Full path of the existing SAT file to read.
        scale_factor: Scale factor applied to the geometry while reading the file.
        binary: True if the file is a binary SAT file, False if it is a text SAT file.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def export_fbx_file(element_id_list: list[ElementId], file_path: str, fbx_format: int) -> None:
    """Export the given elements to an FBX file.

    Only the listed elements are written. Element IDs that do not exist are skipped. The current
    element visibility is restored after the export. An unknown fbx_format falls back to FBX binary.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the FBX file to write.
        fbx_format: FBX variant, 1 to 6: 1 = FBX binary, 2 = FBX ascii, 3 = FBX encrypted, 4 = FBX
            6.0 binary, 5 = FBX 6.0 ascii, 6 = FBX 6.0 encrypted. Other values use 1.

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
    """Clear the stored file controller error messages.

    Empties the error stack that get_last_error reads from.
    """

def import_3dc_file_with_glide(file_path: str) -> list[ElementId]:
    """Import a 3D or 3DC file and start a glide placement of the new elements.

    The file type is taken from the extension (.3d or .3dc). The elements are inserted, shown, and
    then moved interactively starting at the origin, so the script may wait for the user. An empty
    path returns an empty list. No undo step is created.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def import_btl_file(file_path: str) -> None:
    """Import a BTL file into the current model.

    Nothing happens if the BTL import module is not available. The created elements are not
    returned.

    Parameters:
        file_path: Full path of the existing BTL file to read.
    """

def export_3dc_file(element_id_list: list[ElementId], file_path: str) -> None:
    """Export the given elements to a 3DC file.

    The extension .3dc is appended to the path if it is missing. Element IDs that do not exist are
    skipped.

    Parameters:
        element_id_list: List of element IDs to export.
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

    Nothing happens if the BTL import module is not available. The created elements are not
    returned.

    Parameters:
        file_path: Full path of the existing BTL file to read.
    """

def export_btl_file_for_nesting(file_path: str) -> None:
    """Export the active elements to a BTL file for nesting.

    Requires a BTL license; without it nothing is written and an error is stored (readable with
    get_last_error). Only visible, active, beam-like elements (beams, panels and other elements with
    a beam-like cross-section) that belong to a production list are exported. Forward slashes in the
    path are accepted.

    Parameters:
        file_path: Full path of the BTL file to write.

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

    Requires a Rhino license; without it nothing is written. Element IDs that do not exist are
    skipped. The element activation state is changed during the export and restored afterwards.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the 3DM file to write.
        version: Rhino version: 5, 6, 7 or 8. Any other value writes version 5.
        use_default_assignment: True to apply the default attribute mapping, False to apply none.
        write_standard_attributes: Currently has no effect.

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

    Uses the saved Blum exchange settings. The imported elements are moved by insert_position and
    the import is added as one undo step. Returns an empty list if the file cannot be read.

    Parameters:
        file_path: Full path of the existing BXF file to read.
        insert_position: Offset in mm the imported elements are moved by (translation from their
            original position).

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def get_blum_export_path() -> str:
    """Get the Blum export path from the Blum exchange settings.

    The value is read from the stored Blum export settings file each time.

    Returns:
        The configured Blum export path as a string.
    """

def set_blum_export_path(path: str) -> None:
    """Set the Blum export path in the Blum exchange settings.

    The path is written to the stored Blum export settings file and so persists beyond the current
    document.

    Parameters:
        path: New export path.
    """

def export_sat_file(
    element_id_list: list[ElementId], file_path: str, scale_factor: float, binary: bool, version: int
) -> None:
    """Export the given elements to a SAT file.

    An existing file at the path is overwritten. Element IDs that do not exist are skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the SAT file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        binary: True to write a binary SAT file, False for a human readable text file.
        version: ACIS version: 3400 = v34.0, 3200 = v32.0, 2100 = v21.0.

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
    """Export the given elements to a GLB file.

    Only the listed elements are written. Element IDs that do not exist are skipped. The current
    element visibility is restored after the export.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the GLB file to write.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.glb"
        >>> fc.export_glb_file(selected_elements, output_path)
    """

def import_variant_file(file_path: str, insert_position: point_3d) -> list[ElementId]:
    """Import a variant (.val) file and return the IDs of the new elements.

    Only .val files are supported; any other extension returns an empty list, as does a file that
    cannot be loaded as a variant. The variant is built and moved by insert_position.

    Parameters:
        file_path: Full path of the existing .val file.
        insert_position: Offset in mm the variant elements are moved by (translation from their
            built position).

    Returns:
        List of IDs of the created elements; empty list on failure.
    """

def import_element_light(file_path: str, insert_position: point_3d) -> int:
    """Import a light element from a file and return its ID.

    Returns 0 if the path is empty or the file format is not supported. OBJ files are prepared
    first, which can take a moment.

    Parameters:
        file_path: Full path of the existing file to read.
        insert_position: Offset in mm the element is moved by (translation from the origin).

    Returns:
        ID of the new light element, or 0 on failure.
    """

def export_rhino_file_with_options(
    element_id_list: list[ElementId],
    file_path: str,
    version: int,
    use_default_assignment: bool,
    write_standard_attributes: bool,
    rhino_options: None,
) -> None:
    """Export the given elements to a Rhino 3DM file using export options.

    Requires a Rhino license; without it nothing is written. Element IDs that do not exist are
    skipped. The element activation state is changed during the export and restored afterwards.
    rhino_options must be a valid options object.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the 3DM file to write.
        version: Rhino version: 5, 6, 7 or 8. Any other value writes version 5.
        use_default_assignment: True to apply the default attribute mapping, False to apply none.
        write_standard_attributes: Currently has no effect.
        rhino_options: Rhino export options: whether end types are materialized, end type
            counterparts, drillings, MEP elements and openings are cut.

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

    The file type is taken from the extension (.3d or .3dc). Saved scenes are never imported.
    Auxiliary geometry such as caddy and graphical objects is not part of the returned list. An
    empty path returns an empty list. No undo step is created.

    Parameters:
        file_path: Full path of the existing 3D or 3DC file to read.
        import_3dc_options: Import options object from get_import_3dc_options.

    Returns:
        List of IDs of the imported elements; empty list on failure.
    """

def get_import_3dc_options() -> import_3dc_options:
    """Create a 3DC import options object with default values.

    Defaults: import saved 2D planes, import export solids and reset position numbers are all
    enabled, import saved scenes is enabled but has no effect. Adjust the object, then pass it to
    import_3dc_file_with_options.

    Returns:
        A new import options object.
    """

def load_webgl_preset_file(file_path: str) -> None:
    """Load a WebGL export preset file into the global WebGL export settings.

    The settings read from the XML preset apply to later export_webgl calls. Nothing happens if the
    file cannot be opened.

    Parameters:
        file_path: Full path of the existing preset (XML) file.
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

    Requires a STEP license; without it nothing is written. Beam-like elements (beams, panels and
    other elements with a beam-like cross-section) are exported as temporary copies with drillings
    and applicable installations cut out. Element IDs that do not exist, containers and export
    solids are skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the STEP file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        version: STEP schema: 214 for AP214, 203 for AP203.
        text_mode: Unused.
        imperial_units: True to write imperial units; the scale factor is then multiplied by 100 /
            2.54.

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

    Identical to export_step_file_extrude_drillings. Requires a STEP license; without it nothing is
    written. Beam-like elements (beams, panels and other elements with a beam-like cross-section)
    are exported as temporary copies with drillings and applicable installations cut out. Element
    IDs that do not exist, containers and export solids are skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the STEP file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        version: STEP schema: 214 for AP214, 203 for AP203.
        text_mode: Unused.
        imperial_units: True to write imperial units; the scale factor is then multiplied by 100 /
            2.54.

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

    An existing file at the path is overwritten. Beam-like elements (beams, panels and other
    elements with a beam-like cross-section) are exported as temporary copies with drillings and
    applicable installations cut out. Element IDs that do not exist are skipped.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the SAT file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        binary: True to write a binary SAT file, False for a human readable text file.
        version: ACIS version: 3400 = v34.0, 3200 = v32.0, 2100 = v21.0.
    """

def upload_to_bim_team_and_create_share_link(element_id_list: list[ElementId]) -> bim_team_upload_result:
    """Upload the given elements to BIMteam and create a share link.

    Element IDs that do not exist are skipped. The result holds a result code and the link; the code
    0 means success, otherwise the share link is empty.

    Parameters:
        element_id_list: List of element IDs to upload.

    Returns:
        Result object with a result code and the share link; on failure the code is not 0 and the
        link is empty.
    """

def export_dxf_file(
    file_path: str, dxf_layer_format_type: dxf_layer_format_type, dxf_export_version: dxf_export_version
) -> bool:
    """Export all visible elements of the scene to a DXF file.

    Returns False for an unsupported layer format type. If no element is visible, no file is written
    but True is returned. Other failures are logged.

    Parameters:
        file_path: Full path of the DXF file to write.
        dxf_layer_format_type: How layers are assigned: all on one layer, or by colour, material,
            name, group or subgroup.
        dxf_export_version: AutoCAD R10 writes a simplified export; any other value writes the newer
            DXF format.

    Returns:
        True if the export succeeded, False otherwise.
    """

def export_dstv_file(file_path: str) -> bool:
    """Export the active elements to a DSTV file.

    Uses the saved DSTV export settings. Returns False only if the DSTV export module cannot be
    loaded.

    Parameters:
        file_path: Full path of the file to write.

    Returns:
        True if the export module ran, False if it is not available.
    """

def set_webgl_hierarchy(stage: int, attribute: display_attribute) -> None:
    """Set the display attribute used for one stage of the WebGL export hierarchy.

    The setting is global and affects later WebGL exports. Stages outside 1 to 6 are silently
    ignored.

    Parameters:
        stage: Hierarchy stage, 1 to 6.
        attribute: Display attribute to use for that stage.
    """

def export_step_file_ex(
    element_list: list[ElementId], file_path: str, scale_factor: float, substract_drillings: bool
) -> None:
    """Export the given elements to a STEP file through a temporary SAT conversion.

    Requires a STEP license; without it nothing is written. Element IDs that do not exist are
    skipped. Nothing is written if the temporary file cannot be created.

    Parameters:
        element_list: List of element IDs to export.
        file_path: Full path of the STEP file to write.
        scale_factor: Scale factor applied to the geometry in the file.
        substract_drillings: True to cut drillings into the bodies, False to leave them out of the
            geometry.
    """

def get_sat_export_options() -> sat_export_options:
    """Create a SAT export options object with default values.

    Defaults: scale factor 1.0, binary, version sat_export_options.ACIS_V33_0, all level-of-detail
    options disabled.

    Returns:
        A new SAT export options object, to be passed to export_file_with_options.
    """

def get_step_export_options() -> step_export_options:
    """Create a STEP export options object with default values.

    Defaults: scale factor 1.0, version step_export_options.AP214, metric units, all level-of-detail
    options disabled.

    Returns:
        A new STEP export options object, to be passed to export_file_with_options.
    """

def get_iges_export_options() -> iges_export_options:
    """Create an IGES export options object with default values.

    Defaults: scale factor 1.0, all level-of-detail options disabled.

    Returns:
        A new IGES export options object, to be passed to export_file_with_options.
    """

def export_file_with_options(element_id_list: list[ElementId], file_path: str, options: file_export_options) -> bool:
    """Export the given elements to SAT, STEP or IGES using an export options object.

    The type of options decides the file format; the file extension is not changed. Element IDs that
    do not exist, containers and export solids are skipped. Failures, user aborts and warnings are
    written to the log rather than raised.

    Parameters:
        element_id_list: List of element IDs to export.
        file_path: Full path of the file to write.
        options: Options object from get_sat_export_options, get_step_export_options or
            get_iges_export_options.

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
        True if the file was written, False otherwise (for example no STEP license, export failed or
        aborted by the user).
    """
