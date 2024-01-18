from typing import List
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        strerror string
    """

def export_2d_wireframe_with_clipboard(clipboard_number: int) -> None:
    """export 2d wireframe with clipboard
    Args:
        clipboard_number ( int): clipboard_number

    Returns:
        None
    """

def export_2d_hidden_lines_with_clipboard(clipboard_number: int) -> None:
    """export 2d hidden lines with clipboard
    Args:
        clipboard_number ( int): clipboard_number

    Returns:
        None
    """

def export_2d_wireframe_with_2dc(file_path: str) -> None:
    """export 2d wireframe with 2dc
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_2d_hidden_lines_with_2dc(file_path: str) -> None:
    """export 2d hidden lines with 2dc
    Args:
        file_path ( str): file_path

    Returns:
        None
    """

def export_wall_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """export wall with clipboard
    Args:
        clipboard_number ( int): clipboard_number
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def export_export_solid_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """export export solid with clipboard
    Args:
        clipboard_number ( int): clipboard_number
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def export_piece_by_piece_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """export piece by piece with clipboard
    Args:
        clipboard_number ( int): clipboard_number
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def assign_export_solid(ceo_element: List[int], element_id_list: List[int]) -> None:
    """assign export solid
    Args:
        ceo_element ( List[int]): ceo_element
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def export_container_with_clipboard(clipboard_number: int, elements: List[int]) -> None:
    """export container with clipboard
    Args:
        clipboard_number ( int): clipboard_number
        elements ( List[int]): elements

    Returns:
        None
    """

def add_wall_section_horizontal(element: int, position: point_3d) -> None:
    """add wall section horizontal
    Args:
        element ( int): element
        position ( point_3d): position

    Returns:
        None
    """

def add_wall_section_vertical(element: int, position: point_3d) -> None:
    """add wall section vertical
    Args:
        element ( int): element
        position ( point_3d): position

    Returns:
        None
    """

def export_wall_with_clipboard_and_presetting(clipboard_number: int, element_id_list: List[int], presetting_file: str) -> None:
    """export wall with clipboard and presetting
    Args:
        clipboard_number ( int): clipboard_number
        element_id_list ( List[int]): element_id_list
        presetting_file ( str): presetting_file

    Returns:
        None
    """

def load_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """load export piece by piece settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

def save_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """save export piece by piece settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def load_export_wall_settings(settings_file_path: str) -> None:
    """load export wall settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

def load_export_solid_settings(settings_file_path: str) -> None:
    """load export solid settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

def load_export_container_settings(settings_file_path: str) -> None:
    """load export container settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

