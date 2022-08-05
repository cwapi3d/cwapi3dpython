from typing import List
from cadwork import point_3d

def export_2d_wireframe_with_clipboard(clipboard: int, with_layout: bool) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        with_layout (bool): use layout
    """
def export_2d_hidden_lines_with_clipboard(clipboard: int, with_layout: bool) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        with_layout (bool): use layout
    """
def export_2d_wireframe_with_2dc(file: str, with_layout: bool) -> None: 
    """

    Args:
        file (str): file path
        with_layout (bool): use layout
    """
def export_2d_hidden_lines_with_2dc(file: str, with_layout: bool) -> None: 
    """

    Args:
        file (str): file path
        with_layout (bool): use layout
    """
def export_wall_with_clipboard(clipboard: int, elements: List[int]) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        elements (List[int]): element IDs
    """
def export_export_solid_with_clipboard(clipboard: int, export_solid_ids: List[int]) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        export_solid_ids (List[int]): element IDs
    """
def export_piece_by_piece_with_clipboard(clipboard: int, elements: List[int]) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        elements (List[int]): element IDs
    """
def assign_export_solid(a_export_solid_element: List[int], elements_to_assign: List[int]) -> None: 
    """Assigns elements to an export solid

    Args:
        a_export_solid_element (List[int]): element ID export solid
        other_elements (List[int]): element IDs to assign
    """
def export_container_with_clipboard(clipboard: int, elements: List[int]) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        elements (List[int]): element IDs
    """
def add_wall_section_horizontal(element: int, position: point_3d) -> None: 
    """Adds a horizontal wall section

    Args:
        element (int): element ID
        position (point_3d): position vector
    """
def add_wall_section_vertical(element: int, position: point_3d) -> None: 
    """Adds a vertical wall section

    Args:
        element (int): element ID
        position (point_3d): position vector
    """
def export_wall_with_clipboard_and_presetting(clipboard: int, elements: List[int], file: str) -> None: 
    """

    Args:
        clipboard (int): clipboard element
        elements (List[int]): element IDs
        file (str): file path
    """
def load_export_piece_by_piece_settings(file: str) -> None: 
    """

    Args:
        file (str): file path
    """
def save_export_piece_by_piece_settings(file: str) -> None: 
    """

    Args:
        file (str): file path
    """

