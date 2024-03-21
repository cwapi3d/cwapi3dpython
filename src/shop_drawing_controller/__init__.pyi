from typing import List
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def export_2d_wireframe_with_clipboard(clipboard_number: int, with_layout: bool) -> None:
    """Exports a 2D wireframe to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        with_layout: with_layout

    Returns:
        None
    """

def export_2d_hidden_lines_with_clipboard(clipboard_number: int, with_layout: bool) -> None:
    """Exports a 2D hidden lines to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        with_layout: with_layout

    Returns:
        None
    """

def export_2d_wireframe_with_2dc(file_path: str, with_layout: bool) -> None:
    """Exports a 2D wireframe to a 2DC file

    Parameters:
        file_path: file_path
        with_layout: with_layout

    Returns:
        None
    """

def export_2d_hidden_lines_with_2dc(file_path: str, with_layout: bool) -> None:
    """Exports a 2D hidden lines to a 2DC file

    Parameters:
        file_path: file_path
        with_layout: with_layout

    Returns:
        None
    """

def export_wall_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports a wall to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    Returns:
        None
    """

def export_export_solid_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports an export solid to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    Returns:
        None
    """

def export_piece_by_piece_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports a piece-by-piece to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    Returns:
        None
    """

def assign_export_solid(ceo_element: List[int], element_id_list: List[int]) -> None:
    """Assigns elements to an export solid

    Parameters:
        ceo_element: ceo_element
        element_id_list: element_id_list

    Returns:
        None
    """

def export_container_with_clipboard(clipboard_number: int, elements: List[int]) -> None:
    """Export a container to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        elements: elements

    Returns:
        None
    """

def add_wall_section_horizontal(element: int, position: point_3d) -> None:
    """Adds a horizontal wall section

    Parameters:
        element: element
        position: position

    Returns:
        None
    """

def add_wall_section_vertical(element: int, position: point_3d) -> None:
    """Adds a vertical wall section

    Parameters:
        element: element
        position: position

    Returns:
        None
    """

def export_wall_with_clipboard_and_presetting(clipboard_number: int, element_id_list: List[int], presetting_file: str) -> None:
    """Exports a wall to the clipboard

    Parameters:
        clipboard_number: clipboard_number
        element_id_list: element_id_list
        presetting_file: presetting_file

    Returns:
        None
    """

def load_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Loads piece by piece export settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

def save_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Saves piece by piece export settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def load_export_wall_settings(settings_file_path: str) -> None:
    """Loads wall export settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

def load_export_solid_settings(settings_file_path: str) -> None:
    """Loads export solid settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

def load_export_container_settings(settings_file_path: str) -> None:
    """Loads container export settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

