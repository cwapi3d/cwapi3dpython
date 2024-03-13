from typing import List
from cadwork import point_3d


def get_last_error(error_code: int) -> str:
    """Gets the last error.

    Args:
        error_code: error code

    Returns:
        error string
    """


def export_2d_wireframe_with_clipboard(clipboard_number: int) -> None:
    """Exports a 2D wireframe to the clipboard

    Args:
        clipboard_number: clipboard_number

    """


def export_2d_hidden_lines_with_clipboard(clipboard_number: int) -> None:
    """Exports a 2D hidden lines to the clipboard

    Args:
        clipboard_number: clipboard_number

    """


def export_2d_wireframe_with_2dc(file_path: str) -> None:
    """Exports a 2D wireframe to a 2DC file

    Args:
        file_path: file_path

    """


def export_2d_hidden_lines_with_2dc(file_path: str) -> None:
    """Exports a 2D hidden lines to a 2DC file

    Args:
        file_path: file_path

    """


def export_wall_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports a wall to the clipboard

    Args:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    """


def export_export_solid_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports an export solid to the clipboard

    Args:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    """


def export_piece_by_piece_with_clipboard(clipboard_number: int, element_id_list: List[int]) -> None:
    """Exports a piece-by-piece to the clipboard

    Args:
        clipboard_number: clipboard_number
        element_id_list: element_id_list

    """


def assign_export_solid(ceo_element: List[int], element_id_list: List[int]) -> None:
    """Assigns elements to an export solid

    Args:
        ceo_element: ceo_element
        element_id_list: element_id_list

    """


def export_container_with_clipboard(clipboard_number: int, elements: List[int]) -> None:
    """Export a container to the clipboard

    Args:
        clipboard_number: clipboard_number
        elements: elements

    """


def add_wall_section_horizontal(element: int, position: point_3d) -> None:
    """Adds a horizontal wall section

    Args:
        element: element
        position: position

    """


def add_wall_section_vertical(element: int, position: point_3d) -> None:
    """Adds a vertical wall section

    Args:
        element: element
        position: position

    """


def export_wall_with_clipboard_and_presetting(clipboard_number: int, element_id_list: List[int], presetting_file: str) -> None:
    """Exports a wall to the clipboard

    Args:
        clipboard_number: clipboard_number
        element_id_list: element_id_list
        presetting_file: presetting_file

    """


def load_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Loads piece by piece export settings

    Args:
        settings_file_path: settings_file_path

    """


def save_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Saves piece by piece export settings

    Args:
        settings_file_path: settings_file_path

    """


def clear_errors() -> None:
    """clear errors

    """


def load_export_wall_settings(settings_file_path: str) -> None:
    """Loads wall export settings

    Args:
        settings_file_path: settings_file_path

    """


def load_export_solid_settings(settings_file_path: str) -> None:
    """Loads export solid settings

    Args:
        settings_file_path: settings_file_path

    """


def load_export_container_settings(settings_file_path: str) -> None:
    """Loads container export settings

    Args:
        settings_file_path: settings_file_path

    """
