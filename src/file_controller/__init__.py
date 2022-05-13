from typing import List

from cadwork import point_3d

def export_stl_file(elements: List[int], file: str) -> None:
    """ Exports an STL file

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def import_step_file(file: str, scale: float) -> List[int]: 
    """Imports a STEP file

    Args:
        file (str): file path
        scale (float): file scale factor

    Returns:
        List[int]: element IDs
    """
def import_step_file_with_message_option(file: str, scale: float, option: bool) -> List[int]: 
    """Imports a STEP file

    Args:
        file (str): file path
        scale (float): file scale factor
        option (bool): hide message

    Returns:
        List[int]: element IDs
    """
def export_webgl(elements: List[int], file: str) -> None: 
    """_summary_

    Args:
        elements (List[int]): _description_
        file (str): _description_
    """
def export_3d_file(elements: List[int], file: str) -> None: 
    """Exports a WebGL file

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def import_sat_file(file: str, scale: float, option: bool) -> List[int]: 
    """Imports an SAT file

    Args:
        file (str): file path
        scale (float): file scale factor
        option (bool): use binary mode

    Returns:
        List[int]: element IDs
    """
def import_3dc_file(file: str) -> List[int]: 
    """Imports a 3DC file

    Args:
        file (str): file path

    Returns:
        List[int]: element IDs
    """
def import_rhino_file(file: str, option: bool) -> List[int]: 
    """Imports a Rhino file

    Args:
        file (str): file path
        option (bool): import without dialog

    Returns:
        List[int]: element IDs
    """
def export_step_file(elements: List[int], file: str, scale: float, number: int, option: bool) -> None: 
    """Exports a STEP file

    Args:
        elements (List[int]): element IDs
        file (str): file path
        scale (float): file scale factor
        number (int): file version
        option (bool): use text mode
    """
def import_3dz_file(file: str) -> None: 
    """Imports a 3DZ file

    Args:
        file (str): file path
    """
def export_obj_file(elements: List[int], file: str) -> None: 
    """Exports a OBJ file

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def import_sat_file_silently(file: str, scale: float, option: bool) -> List[int]: 
    """_summary_

    Args:
        file (str): _description_
        scale (float): _description_
        option (bool): _description_

    Returns:
        List[int]: _description_
    """
def export_fbx_file(elements: List[int], file: str, number: int) -> None: 
    """Export fbx file

    Args:
        elements (List[int]): element IDs
        file (str): file path
        number (int): fbx format  1 = "FBX binary(*.fbx) ; 2 = "FBX ascii(*.fbx)" ; 3 = "FBX encrypted(*.fbx)" ; 4 = "FBX 6.0 binary(*.fbx)" ; 5 = "FBX 6.0 ascii(*.fbx)" ; 6 = "FBX 6.0 encrypted(*.fbx)"
    """
def import_3dc_file_with_glide(file: str) -> List[int]: 
    """Imports a 3DC file with glide

    Args:
        file (str): file path

    Returns:
        List[int]: element IDs
    """
def import_btl_file(file: str) -> None: 
    """Imports a BTL file

    Args:
        file (str): file path
    """
def export_3dc_file(elements: List[int], file: str) -> None: 
    """Exports a 3D/3DC file

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def import_btl_file_for_nesting(file: str) -> None: 
    """Imports a BTL file for nesting

    Args:
        file (str): file path
    """
def export_btl_file_for_nesting(file: str) -> None: 
    """Exports a BTL file for nesting

    Args:
        file (str): file path
    """
def export_rhino_file(elements: List[int], file: str, version: int, user_efault_assignment: bool, write_standard_attributes: bool) -> None: 
    """Exports a 3dm rhino file

    Args:
        elements (List[int]): element IDs
        file (str): file path
        version (int): Rhino version V5.0 = 5, V6.0 = 6, V7.0 = 7
        user_efault_assignment (bool): true: default assignment is used; false: no attributes are exported
        write_standard_attributes (bool): see checkbox in assignment dialog
    """
def export_sat_file(elements: List[int], file: str, scale: float, option: bool, number: int) -> None: 
    """exports a SAT File

    Args:
        elements (List[int]): element IDs
        file (str): file path
        scale (float): scale factor
        option (bool): binary 
        number (int): version
    """

def import_variant_file(file:str, insert_point:point_3d)-> List[int]:
    """imports a variant by .val-File

    Args:
        file (str): file path
        insert_point (point_3d): insert point

    Returns:
        List[int]: element IDs
    """

def set_blum_export_path(file:str) -> None:
    """Set blum export path

    Args:
        file (str): file path
    """

def get_blum_export_path() -> str:
    """Get blum export path

    Returns:
        str: file path
    """
