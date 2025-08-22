from typing import List
from cadwork.import_3dc_options import import_3dc_options
from cadwork.point_3d import point_3d
from cadwork.bim_team_upload_result import bim_team_upload_result
from cadwork.dxf_layer_format_type import dxf_layer_format_type
from cadwork.dxf_export_version import dxf_export_version
from cadwork.api_types import *

def export_stl_file(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports an STL file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.stl"
        >>> fc.export_stl_file(selected_elements, output_path)
    """


def import_step_file(file_path: str, scale_factor: float) -> List[ElementId]:
    """Imports a STEP file.

    Parameters:
        file_path: The input file path.
        scale_factor: The file scale factor.

    Returns:
        The imported list of element id.
    """


def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> List[ElementId]:
    """Imports a STEP file with message option.

    Parameters:
        file_path: The input file path.
        scale_factor: The file scale factor.
        hide_message: Hide message.

    Returns:
        The imported list of element id.
    """


def export_webgl(element_id_list: List[ElementId], file_path: str) -> bool:
    """Exports a WebGL file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.html"
        >>> success = fc.export_webgl(selected_elements, output_path)
        >>> if success:
        >>>     print("WebGL export completed successfully")

    Returns:
        True on successful export, false otherwise.
    """


def export_3d_file(element_id_list: List[ElementId], file_path: str) -> bool:
    """Exports a 3D file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3d"
        >>> success = fc.export_3d_file(selected_elements, output_path)
        >>> if success:
        >>>     print("3D file export completed successfully")

    Returns:
        True on successful export, false otherwise.
    """


def import_sat_file(file_path: str, scale_factor: float, binary: bool) -> List[ElementId]:
    """Imports an SAT file.

    Parameters:
        file_path: The input file path.
        scale_factor: The scale factor.
        binary: Is the import file binary.

    Returns:
        The imported list of element id.
    """


def import_3dc_file(file_path: str) -> List[ElementId]:
    """Imports a 3DC file.

    Parameters:
        file_path: The input file path.

    Returns:
        The imported list of element id.
    """


def import_rhino_file(file_path: str, without_dialog: bool) -> List[ElementId]:
    """Imports a Rhino file.

    Parameters:
        file_path: The input file path.
        without_dialog: Import without dialog?

    Returns:
        The imported list of element id.
    """


def export_step_file(element_id_list: List[ElementId], file_path: str, scale_factor: float, version: int,
                     text_mode: bool) -> None:
    """Exports a STEP file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        scale_factor: The file scale factor.
        version: The file export version :
                    - 214 = STEP AP214
                    - 203 = STEP AP203 (default value)
        text_mode: Use text mode. PARAMETER UNUSED

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
    """Imports a 3DZ file.

    Parameters:
        file_path: The input file path.
    """


def export_obj_file(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a OBJ file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.obj"
        >>> fc.export_obj_file(selected_elements, output_path)
    """


def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> List[ElementId]:
    """Imports a SAT File without messages.

    Parameters:
        file_path: The input file path.
        scale_factor: The scale factor.
        binary: Is the import file binary.

    Returns:
        The imported list of element id.
    """


def export_fbx_file(element_id_list: List[ElementId], file_path: str, fbx_format: int) -> None:
    """Exports a FBX file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        fbx_format: The FBX format. 
        
            Available values :
            
            
            - 1 = "FBX binary(*.fbx)";
            - 2 = "FBX ascii(*.fbx)";
            - 3 = "FBX encrypted(*.fbx)";
            - 4 = "FBX 6.0 binary(*.fbx)";
            - 5 = "FBX 6.0 ascii(*.fbx)";
            - 6 = "FBX 6.0 encrypted(*.fbx)";

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
    """Clears all errors.
    """


def import_3dc_file_with_glide(file_path: str) -> List[ElementId]:
    """Imports a 3DC file with glide.

    Parameters:
        file_path: The input file path.

    Returns:
        The imported list of element id.
    """


def import_btl_file(file_path: str) -> None:
    """Imports a BTL file.

    Parameters:
        file_path: The input file path.
    """


def export_3dc_file(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a 3D file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dc"
        >>> fc.export_3dc_file(selected_elements, output_path)
    """


def import_btl_file_for_nesting(file_path: str) -> None:
    """Imports a BTL file for nesting.

    Parameters:
        file_path: The input file path.
    """


def export_btl_file_for_nesting(file_path: str) -> None:
    """Exports a BTL file for nesting.

    Parameters:
        file_path: The output file path.

    Examples:
        >>> import file_controller as fc

        >>> output_path = r"C:/exports/nesting_project.btl"
        >>> fc.export_btl_file_for_nesting(output_path)
    """


def export_rhino_file(element_id_list: List[ElementId], file_path: str, version: int, use_default_assignment: bool,
                      write_standard_attributes: bool) -> None:
    """Exports a 3dm rhino file.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        version: The rhino version :


            - 5 = V5.0,
            - 6 = V6.0,
            - 7 = V7.0,
            - 8 = V8.0
        use_default_assignment: True if default assignment is used. False if no attributes are exported.
        write_standard_attributes: True if exported with standard attribute, false otherwise.

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


def import_bxf_file(file_path: str, insert_position: point_3d) -> List[ElementId]:
    """Imports a BXF file.

    Parameters:
        file_path: The import file path.
        insert_position: The position where the imported elements will be inserted.

    Returns:
        The list of IDs of the imported elements.
    """


def get_blum_export_path() -> str:
    """Gets the path of the Blum export.

    Returns:
        The path of the Blum export.
    """


def set_blum_export_path(path: str) -> None:
    """Sets the path of the Blum export.

    Parameters:
        path: The new path for the Blum export.
    """


def export_sat_file(element_id_list: List[ElementId], file_path: str, scale_factor: float, binary: bool, version: int) -> None:
    """Exports a SAT File.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        scale_factor: The file scale factor.
        binary: Whether to write the SAT file in binary or a human readable format.
        version: The ACIS version to use :


            - 3400 = v34.0
            - 3200 = v32.0
            - 2100 = v21.0

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


def export_glb_file(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a GLB File.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.glb"
        >>> fc.export_glb_file(selected_elements, output_path)
    """


def import_variant_file(file_path: str, insert_position: point_3d) -> List[ElementId]:
    """Imports a variant (.val-File).

    Parameters:
        file_path: The import file path.
        insert_position: The position where the imported variant elements will be inserted.

    Returns:
        The imported list of element id.
    """


def import_element_light(file_path: str, insert_position: point_3d) -> int:
    """Imports a light element from a file.

    Parameters:
        file_path: The import file path.
        insert_position: The position where the imported light element will be inserted.

    Returns:
        The ID of the imported light element.
    """


def export_rhino_file_with_options(element_id_list: List[ElementId], file_path: str, version: int,
                                   use_default_assignment: bool, write_standard_attributes: bool,
                                   rhino_options: None) -> None:
    """Exports elements to a rhino 3dm file based on the export options.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        version: The rhino version :


            - 5 = V5.0,
            - 6 = V6.0,
            - 7 = V7.0,
            - 8 = V8.0
        use_default_assignment: True if default assignment is used. False if no attributes are exported.
        write_standard_attributes: True if exported with standard attribute, false otherwise.
        rhino_options: The Rhino export option.

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


def import_3dc_file_with_options(file_path: str, import_3dc_options: import_3dc_options) -> List[ElementId]:
    """Imports a 3d or a 3dc file depending on the import options.

    Parameters:
        file_path: The input file path.
        import_3dc_options: The 3dc import options.

    Returns:
        The imported list of element id.
    """


def get_import_3dc_options() -> import_3dc_options:
    """Get the 3dc import options.

    Returns:
        The 3dc import options.
    """


def load_webgl_preset_file(file_path: str) -> None:
    """Loads a preset file for the WebGl export.

    Parameters:
        file_path: The preset file path.
    """


def export_step_file_extrude_drillings(element_id_list: List[ElementId], file_path: str, scale_factor: float, version: int,
                                       text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        scale_factor: The file scale factor.
        version: The file export version :
                    - 214 = STEP AP214
                    - 203 = STEP AP203 (default value)
        text_mode: Use text mode. PARAMETER UNUSED
        imperial_units: Use imperial units.

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


def export_step_file_cut_drillings(element_id_list: List[ElementId], file_path: str, scale_factor: float, version: int,
                                   text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings.

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        scale_factor: The file scale factor.
        version: The file export version :
                    - 214 = STEP AP214
                    - 203 = STEP AP203 (default value)
        text_mode: Use text mode. PARAMETER UNUSED
        imperial_units: Use imperial units.

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


def export_sat_file_cut_drillings(element_id_list: List[ElementId], file_path: str,
                                  scale_factor: float, binary: bool, version: int) -> None:
    """Exports a SAT File with extruded drillings (cut drilling holes into bodies).

    Parameters:
        element_id_list: The list of element id to export.
        file_path: The output file path.
        scale_factor: The file scale factor.
        binary: Whether to write the SAT file in binary or a human readable format.
        version: The ACIS version to use :


            - 3400 = v34.0
            - 3200 = v32.0
            - 2100 = v21.0
    """


def upload_to_bim_team_and_create_share_link(element_id_list: List[ElementId]) -> bim_team_upload_result:
    """Exports the elements to BIMteam and creates a share link.

    Parameters:
        element_id_list: The list of element id to export.

    Returns:
        The result object with a result code and a share link. If the code is not ok (0), the share link string is empty.
    """


def export_dxf_file(file_path: str, dxf_layer_format_type: dxf_layer_format_type,
                    dxf_export_version: dxf_export_version) -> bool:
    """Exports visible elements in the scene to a DXF file.

    Parameters:
        file_path: The output file path.
        dxf_layer_format_type: The format type of how to organize layers.
        dxf_export_version: The dxf version to use for the export.

    Returns:
        True on successful export, false otherwise.
    """


def export_dstv_file(file_path: str) -> bool:
    """Exports active elements in the scene to a DSTV (.stp) file.

    Parameters:
        file_path: The output file path.

    Returns:
        True on successful export, false otherwise.
    """
