from typing import List
from cadwork import point_3d
from cadwork import rhino_options

def get_last_error(error_code: int) -> str:
    """Gets the last error 
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def export_stl_file(element_id_list: List[int], file_path: str) -> None:
    """Exports an STL file 
    Args:
        element_id_list ( List[int]): element_id_list
        file_path ( str): file_path

    Returns:
        None
    """

def import_step_file(file_path: str, scale_factor: float) -> List[int]:
    """Imports a STEP file 
    Args:
        file_path ( str): file_path
        scale_factor ( float): scale_factor

    Returns:
        imported element ID list (List[int])
    """

def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> List[int]:
    """Imports a STEP file 
    Args:
        file_path ( str): file_path
        scale_factor ( float): scale_factor
        hide_message ( bool): hide_message

    Returns:
        imported element ID list (List[int])
    """

def export_webgl(element_id_list: List[int], file_path: str) -> bool:
    """Exports a WebGL file 
    Args:
        element_id_list ( List[int]): element_id_list
        file_path ( str): file_path

    Returns:
        did operation succeed (bool)
    """

def export_3d_file(element_id_list: List[int], file_path: str) -> bool:
    """Exports a 3D file 
    Args:
        element_id_list ( List[int]): element_id_list
        file_path ( str): file_path

    Returns:
        did operation succeed (bool)
    """

def import_sat_file(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports an SAT file 
    Args:
        file_path ( str): file_path
        scale_factor ( float): scale_factor
        binary ( bool): binary

    Returns:
        imported element ID list (List[int])
    """

def import_3dc_file(file_path: str) -> List[int]:
    """Imports a 3DC file 
    Args:
        file_path ( str): file_path

    Returns:
        imported element ID list (List[int])
    """

def import_rhino_file(file_path: str, without_dialog: bool) -> List[int]:
    """Imports a Rhino file 
    Args:
        file_path ( str): file_path
        without_dialog ( bool): without_dialog

    Returns:
        imported element ID list (List[int])
    """

def export_step_file(element_list: List[int], file_path: str, scale_factor: float, version: int, text_mode: bool) -> None:
    """Exports a STEP file 
    Args:
        element_list ( List[int]): element_list
        file_path ( str): file_path
        scale_factor ( float): scale_factor
        version ( int): version
        text_mode ( bool): text_mode

    Returns:
        None
    """

def import_3dz_file(file_path: str) -> None:
    """Imports a 3DZ file 
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_obj_file(elements: List[int], file_path: str) -> None:
    """Exports a OBJ file 
    Args:
        elements ( List[int]): elements
        file_path ( str): file_path

    Returns:
        None
    """

def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports a SAT File without messages 
    Args:
        file_path ( str): file_path
        scale_factor ( float): scale_factor
        binary ( bool): binary

    Returns:
        List[int]
    """

def export_fbx_file(elements: List[int], file_path: str, fbx_format: int) -> None:
    """Exports a FBX file 
    Args:
        elements ( List[int]): elements
        file_path ( str): file_path
        fbx_format ( int): fbx_format

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def import_3dc_file_with_glide(file_path: str) -> List[int]:
    """Imports a 3DC file with glide 
    Args:
        file_path ( str): file_path

    Returns:
        imported element ID list (List[int])
    """

def import_btl_file(file_path: str) -> None:
    """Imports a BTL file 
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_3dc_file(element_id_list: List[int], file_path: str) -> None:
    """Exports a 3D file 
    Args:
        element_id_list ( List[int]): element_id_list
        file_path ( str): file_path

    Returns:
        None
    """

def import_btl_file_for_nesting(file_path: str) -> None:
    """Imports a BTL file for nesting 
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_btl_file_for_nesting(file_path: str) -> None:
    """Exports a BTL file for nesting 
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_rhino_file(element_id_list: List[int], file_path: str, version: int, use_default_assignment: bool, write_standard_attributes: bool) -> None:
    """Exports a 3dm rhino file 
    Args:
        element_id_list ( List[int]): element_id_list
        file_path ( str): file_path
        version ( int): version
        use_default_assignment ( bool): use_default_assignment
        write_standard_attributes ( bool): write_standard_attributes

    Returns:
        None
    """

def import_bxf_file(file_path: str, insert_position: point_3d) -> List[int]:
    """import bxf file
    Args:
        file_path ( str): file_path
        insert_position ( point_3d): insert_position

    Returns:
        List[int]
    """

def get_blum_export_path() -> str:
    """get blum export path
    Args:

    Returns:
        str
    """

def set_blum_export_path(path: str) -> None:
    """set blum export path
    Args:
        path ( str): path

    Returns:
        None
    """

def export_sat_file(elements: List[int], file_path: str, scale_factor: float, binary: bool, version: int) -> None:
    """exports a SAT File 
    Args:
        elements ( List[int]): elements
        file_path ( str): file_path
        scale_factor ( float): scale_factor
        binary ( bool): binary
        version ( int): version

    Returns:
        None
    """

def export_glb_file(elements: List[int], file_path: str) -> None:
    """exports a GLB File 
    Args:
        elements ( List[int]): elements
        file_path ( str): file_path

    Returns:
        None
    """

def import_variant_file(file_path: str, insert_position: point_3d) -> List[int]:
    """imports a variant by .val-File 
    Args:
        file_path ( str): file_path
        insert_position ( point_3d): insert_position

    Returns:
        imported element ID list (List[int])
    """

def import_element_light(a0: str, a1: point_3d) -> int:
    """import element light
    Args:
        a0 ( str): a0
        a1 ( point_3d): a1

    Returns:
        int
    """

def export_rhino_file_with_options(a0: List[int], a1: str, a2: int, a3: bool, a4: bool, a5: rhino_options) -> None:
    """export rhino file with options
    Args:
        a0 ( List[int]): a0
        a1 ( str): a1
        a2 ( int): a2
        a3 ( bool): a3
        a4 ( bool): a4
        a5 ( rhino_options): a5

    Returns:
        None
    """

