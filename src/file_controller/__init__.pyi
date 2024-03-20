from typing import List
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def export_stl_file(element_id_list: List[int], file_path: str) -> None:
    """Exports an STL file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """

def import_step_file(file_path: str, scale_factor: float) -> List[int]:
    """Imports a STEP file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor

    Returns:
        imported element ID list
    """

def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> List[int]:
    """Imports a STEP file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        hide_message: hide_message

    Returns:
        imported element ID list
    """

def export_webgl(element_id_list: List[int], file_path: str) -> bool:
    """Exports a WebGL file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        did operation succeed
    """

def export_3d_file(element_id_list: List[int], file_path: str) -> bool:
    """Exports a 3D file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        did operation succeed
    """

def import_sat_file(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports an SAT file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        binary: binary

    Returns:
        imported element ID list
    """

def import_3dc_file(file_path: str) -> List[int]:
    """Imports a 3DC file

    Parameters:
        file_path: file_path

    Returns:
        imported element ID list
    """

def import_rhino_file(file_path: str, without_dialog: bool) -> List[int]:
    """Imports a Rhino file

    Parameters:
        file_path: file_path
        without_dialog: without_dialog

    Returns:
        imported element ID list
    """

def export_step_file(element_list: List[int], file_path: str, scale_factor: float, version: int, text_mode: bool) -> None:
    """Exports a STEP file

    Parameters:
        element_list: element_list
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode

    Returns:
        None
    """

def import_3dz_file(file_path: str) -> None:
    """Imports a 3DZ file

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def export_obj_file(elements: List[int], file_path: str) -> None:
    """Exports a OBJ file

    Parameters:
        elements: elements
        file_path: file_path

    Returns:
        None
    """

def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports a SAT File without messages

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        binary: binary

    Returns:
        List[int]
    """

def export_fbx_file(elements: List[int], file_path: str, fbx_format: int) -> None:
    """Exports a FBX file

    Parameters:
        elements: elements
        file_path: file_path
        fbx_format: fbx_format

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def import_3dc_file_with_glide(file_path: str) -> List[int]:
    """Imports a 3DC file with glide

    Parameters:
        file_path: file_path

    Returns:
        imported element ID list
    """

def import_btl_file(file_path: str) -> None:
    """Imports a BTL file

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def export_3dc_file(element_id_list: List[int], file_path: str) -> None:
    """Exports a 3D file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """

def import_btl_file_for_nesting(file_path: str) -> None:
    """Imports a BTL file for nesting

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def export_btl_file_for_nesting(file_path: str) -> None:
    """Exports a BTL file for nesting

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def export_rhino_file(element_id_list: List[int], file_path: str, version: int, use_default_assignment: bool, write_standard_attributes: bool) -> None:
    """Exports a 3dm rhino file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        version: version
        use_default_assignment: use_default_assignment
        write_standard_attributes: write_standard_attributes

    Returns:
        None
    """

def import_bxf_file(file_path: str, insert_position: point_3d) -> List[int]:
    """import bxf file

    Parameters:
        file_path: file_path
        insert_position: insert_position

    Returns:
        List[int]
    """

def get_blum_export_path() -> str:
    """get blum export path

    Returns:
        str
    """

def set_blum_export_path(path: str) -> None:
    """set blum export path

    Parameters:
        path: path

    Returns:
        None
    """

def export_sat_file(elements: List[int], file_path: str, scale_factor: float, binary: bool, version: int) -> None:
    """exports a SAT File

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        binary: binary
        version: version

    Returns:
        None
    """

def export_glb_file(elements: List[int], file_path: str) -> None:
    """exports a GLB File

    Parameters:
        elements: elements
        file_path: file_path

    Returns:
        None
    """

def import_variant_file(file_path: str, insert_position: point_3d) -> List[int]:
    """imports a variant by .val-File

    Parameters:
        file_path: file_path
        insert_position: insert_position

    Returns:
        imported element ID list
    """

def import_element_light(a0: str, a1: point_3d) -> int:
    """import element light

    Parameters:
        a0: a0
        a1: a1

    Returns:
        int
    """

def export_rhino_file_with_options(element_id_list: List[int], file_path: str, version: int, use_default_assignment: bool, write_standard_attributes: bool, rhino_options: None) -> None:
    """exports elements to a rhino 3dm file based on the export options

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        version: version
        use_default_assignment: use_default_assignment
        write_standard_attributes: write_standard_attributes
        rhino_options: rhino_options

    Returns:
        None
    """

def import_3dc_file_with_options(file_path: str, import3dc_options: None) -> List[int]:
    """imports a 3d or a 3dc file depending on the import options

    Parameters:
        file_path: file_path
        import3dc_options: import3dc_options

    Returns:
        imported element ID list
    """

def get_import_3dc_options() -> import_3dc_options:
    """get import 3dc options

    Returns:
        import_3dc_options
    """

def load_webgl_preset_file(file_path: str) -> None:
    """loads a preset file for the WebGl export

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def export_step_file_extrude_drillings(elements: List[int], file_path: str, scale_factor: float, version: int, text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode
        imperial_units: imperial_units

    Returns:
        None
    """

