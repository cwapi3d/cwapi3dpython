from typing import List
from cadwork.point_3d import point_3d
from cadwork.api_types import *


def export_2d_wireframe_with_clipboard(clipboard_number: UnsignedInt, with_layout: bool) -> None:
    """Exports a 2D wireframe to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        with_layout: Use layout, false by default.
    """

def export_2d_hidden_lines_with_clipboard(clipboard_number: UnsignedInt, with_layout: bool) -> None:
    """Exports a 2D hidden lines to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        with_layout: Use layout, false by default.
    """

def export_2d_wireframe_with_2dc(file_path: str, with_layout: bool) -> None:
    """Exports a 2D wireframe to a 2DC file.

    Parameters:
        file_path: The export file path.
        with_layout: Use layout, false by default.
    """

def export_2d_hidden_lines_with_2dc(file_path: str, with_layout: bool) -> None:
    """Exports a 2D hidden lines to a 2DC file.

    Parameters:
        file_path: The export file path.
        with_layout: Use layout, false by default.
    """

def export_wall_with_clipboard(clipboard_number: UnsignedInt, element_id_list: List[ElementId]) -> None:
    """Exports a wall to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def export_export_solid_with_clipboard(clipboard_number: UnsignedInt, element_id_list: List[ElementId]) -> None:
    """Exports an export solid to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def export_piece_by_piece_with_clipboard(clipboard_number: UnsignedInt, element_id_list: List[ElementId]) -> None:
    """Exports a piece-by-piece to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def assign_export_solid(ceo_element_id_list: List[ElementId], element_id_list: List[ElementId]) -> None:
    """Assigns elements to an export solid.

    Parameters:
        ceo_element_id_list: The export solid to assign.
        element_id_list: The elements to assign.
    """

def export_container_with_clipboard(clipboard_number: UnsignedInt, element_id_list: List[ElementId]) -> None:
    """Export a container to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def add_wall_section_horizontal(element_id: ElementId, position: point_3d) -> None:
    """Adds a horizontal wall section.

    Parameters:
        element_id: The element id.
        position: The section position.
    """

def add_wall_section_vertical(element_id: ElementId, position: point_3d) -> None:
    """Adds a vertical wall section.

    Parameters:
        element_id: The element id.
        position: The section position.
    """

def export_wall_with_clipboard_and_presetting(clipboard_number: UnsignedInt, element_id_list: List[ElementId], presetting_file: str) -> None:
    """Exports a wall to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The element id list to export.
        presetting_file: The presetting file path.
    """

def load_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Loads piece by piece export settings.

    Parameters:
        settings_file_path: The settings file path.
    """

def save_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Saves piece by piece export settings.

    Parameters:
        settings_file_path: The settings file path.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

def load_export_wall_settings(settings_file_path: str) -> None:
    """Loads wall export settings.

    Parameters:
        settings_file_path: The settings file path.
    """

def load_export_solid_settings(settings_file_path: str) -> None:
    """Loads export solid settings.

    Parameters:
        settings_file_path: The settings file path.
    """

def load_export_container_settings(settings_file_path: str) -> None:
    """Loads container export settings.

    Parameters:
        settings_file_path: The settings file path.
    """