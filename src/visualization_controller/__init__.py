from typing import List
from cadwork import (rgb_color,
                     visibility_state,
                     activation_state)


def get_color(element: int) -> int: 
    """
    
    !!! Info
            Available in script filled attributes

    Args:
        number (int): element ID

    Returns:
        int: color number
    """
def set_color(element: int, color: int) -> None: 
    """

    Args:
        element (int): element ID
        color (int): color number
    """
def get_opengl_color(element: int) -> rgb_color: 
    """
    
    !!! Info
            Available in script filled attributes

    Args:
        element (int): element ID

    Returns:
        rgb_color: rgb color 
    """
def set_opengl_color(element: int, color: rgb_color) -> None: 
    """_summary_

    Args:
        element (int): element ID
        color (rgb_color): rgb color
    """
def is_active(element: int) -> bool: 
    """Tests if element is active

    Args:
        element (int): element ID

    Returns:
        bool: result
    """
def set_active(elements: List[int]) -> None: 
    """Set elements active

    Args:
        elements (List[int]): element IDs
    """
def set_inactive(elements: List[int]) -> None: 
    """Set elements inactive

    Args:
        elements (List[int]): element IDs
    """
def is_visible(element: int) -> bool: 
    """Check if element is visible

    Args:
        element (int): element ID

    Returns:
        bool: result
    """
def set_visible(elements: List[int]) -> None: 
    """Sets the element visible

    Args:
        elements (List[int]): element IDs
    """
def set_invisible(elements: List[int]) -> None: 
    """Sets the element invisible

    Args:
        elements (List[int]): element IDs
    """
def is_immutable(element: int) -> bool: 
    """ests if the element is immutable

    Args:
        element (int): element ID

    Returns:
        bool: result
    """
def set_immutable(elements: List[int]) -> None: 
    """Sets the element immutable

    Args:
        elements (List[int]): element IDs
    """
def set_mutable(elements: List[int]) -> None: 
    """Sets the element mutable

    Args:
        elements (List[int]): element IDs
    """
def show_all_elements() -> None: 
    """Shows all elements
    """
def hide_all_elements() -> None: 
    """Hide all elements
    """
def zoom_all_elements() -> None: 
    """zoom all elements
    """
def zoom_active_elements() -> None: 
    """zoom only active elements
    """
def refresh() -> None: 
    """Refresh the drawing area
    """
def set_material(elements: List[int], element: int) -> None: 
    """Sets the element material

    Args:
        elements (List[int]): element IDs
        element (int): element ID
    """
def get_material(element: int) -> int: 
    """Gets the element material
    
    !!! Info
            Available in script filled attributes

    Args:
        element (int): element ID

    Returns:
        int: material ID
    """
def save_visibility_state() -> visibility_state: 
    """Saves the visibility state

    Returns:
        visibility_state: visibility state
    """
def restore_visibility_state(state: visibility_state) -> None: 
    """Restores the visibility state

    Args:
        state (visibility_state): visibility state
    """
def save_activation_state() -> activation_state: 
    """_summary_

    Returns:
        activation_state: _description_
    """
def restore_activation_state(state: activation_state) -> None: 
    """Saves the activation state

    Args:
        state (activation_state): activation state
    """
def show_view_positive_x() -> None: 
    """
    """
def show_view_negative_x() -> None: 
    """
    """
def show_view_positive_y() -> None: 
    """
    """
def show_view_negative_y() -> None: 
    """
    """
def show_view_positive_z() -> None: 
    """
    """
def show_view_negative_z() -> None: 
    """
    """
def show_view_standard_axo() -> None: 
    """
    """
def show_view_wireframe() -> None: 
    """
    """
def show_view_hidden_lines() -> None: 
    """
    """
def show_view_dashed_hidden_lines() -> None: 
    """
    """
def show_view_shaded2() -> None: 
    """
    """
def show_view_shaded1() -> None: 
    """
    """
def is_selectable(element: int) -> bool: 
    """Returns if the element is selectable

    Args:
        element (int): element ID

    Returns:
        bool: result
    """
def set_unselectable(elements: List[int]) -> None: 
    """Sets a list of elements unselectable

    Args:
        elements (List[int]): element IDs
    """
def set_selectable(elements: List[int]) -> None: 
    """Sets a list of elements selectable

    Args:
        elements (List[int]): element IDs
    """

