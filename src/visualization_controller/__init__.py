from typing import List
from cadwork import camera_data
from cadwork import point_3d
from cadwork import rgb_color

def get_last_error(error_code: int) -> str:
    """Gets the last error 
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def set_color(element_id_list: List[int], color_id: int) -> None:
    """Sets the element color 
    Args:
        element_id_list ( List[int]): element_id_list
        color_id ( int): color_id

    Returns:
        None
    """

def set_opengl_color(element_id_list: List[int], color: None) -> None:
    """Sets the element OpenGL color 
    Args:
        element_id_list ( List[int]): element_id_list
        color ( None): color

    Returns:
        None
    """

def is_active(element_id: int) -> bool:
    """Tests if element is active 
    Args:
        element_id ( int): element_id

    Returns:
        is element active (bool)
    """

def set_active(element_id_list: List[int]) -> None:
    """Sets element active 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_inactive(element_id_list: List[int]) -> None:
    """Sets the element inactive 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def is_visible(element_id: int) -> bool:
    """Tests if element is visible 
    Args:
        element_id ( int): element_id

    Returns:
        is element visible (bool)
    """

def set_visible(element_id_list: List[int]) -> None:
    """Sets the element visible 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_invisible(element_id_list: List[int]) -> None:
    """Sets the element invisible 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def is_immutable(element_id: int) -> bool:
    """Tests if the element is immutable 
    Args:
        element_id ( int): element_id

    Returns:
        is element immutable (bool)
    """

def set_immutable(element_id_list: List[int]) -> None:
    """Sets the element immutable 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_mutable(element_id_list: List[int]) -> None:
    """Sets the element mutable 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def show_all_elements() -> None:
    """Shows all elements
    Args:

    Returns:
        None
    """

def hide_all_elements() -> None:
    """Hides all elements
    Args:

    Returns:
        None
    """

def zoom_all_elements() -> None:
    """Zooms on all elements
    Args:

    Returns:
        None
    """

def zoom_active_elements() -> None:
    """Zooms on all active elements
    Args:

    Returns:
        None
    """

def refresh() -> None:
    """Refresh the drawing area
    Args:

    Returns:
        None
    """

def set_material(element_id_list: List[int], element_id: int) -> None:
    """Sets the element material 
    Args:
        element_id_list ( List[int]): element_id_list
        element_id ( int): element_id

    Returns:
        None
    """

def save_visibility_state() -> 'visibility_state':
    """Saves the visibility state 
    Args:

    Returns:
        visibility state (visibility_state)
    """

def restore_visibility_state(state: None) -> None:
    """Restores the visibility state 
    Args:
        state ( None): state

    Returns:
        None
    """

def save_activation_state() -> 'activation_state':
    """Saves the activation state 
    Args:

    Returns:
        activation state (activation_state)
    """

def restore_activation_state(state: None) -> None:
    """Restores the activation state 
    Args:
        state ( None): state

    Returns:
        None
    """

def show_view_positive_x() -> None:
    """Sets the view to +X
    Args:

    Returns:
        None
    """

def show_view_negative_x() -> None:
    """Sets the view to -X
    Args:

    Returns:
        None
    """

def show_view_positive_y() -> None:
    """Sets the view to +Y
    Args:

    Returns:
        None
    """

def show_view_negative_y() -> None:
    """Sets the view to -Y
    Args:

    Returns:
        None
    """

def show_view_positive_z() -> None:
    """Sets the view to +Z
    Args:

    Returns:
        None
    """

def show_view_negative_z() -> None:
    """Sets the view to -Z
    Args:

    Returns:
        None
    """

def show_view_standard_axo() -> None:
    """Sets the view to standard axonometry
    Args:

    Returns:
        None
    """

def show_view_wireframe() -> None:
    """Sets the view to wireframe
    Args:

    Returns:
        None
    """

def show_view_hidden_lines() -> None:
    """Sets the view to hidden lines
    Args:

    Returns:
        None
    """

def show_view_dashed_hidden_lines() -> None:
    """Sets the view to dashed hidden lines
    Args:

    Returns:
        None
    """

def show_view_shaded2() -> None:
    """Sets the view to shaded 2
    Args:

    Returns:
        None
    """

def show_view_shaded1() -> None:
    """Sets the view to shaded 1
    Args:

    Returns:
        None
    """

def is_selectable(element_id: int) -> bool:
    """Returns if the element is selectable 
    Args:
        element_id ( int): element_id

    Returns:
        bool
    """

def set_unselectable(element_id_list: List[int]) -> None:
    """Sets a list of elements unselectable 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def set_selectable(element_id_list: List[int]) -> None:
    """Sets a list of elements selectable 
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def load_marking_settings(settings_file_path: str) -> None:
    """Loads marking settings file 
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """

def is_plane_2d() -> bool:
    """returns if plane 2d is active 
    Args:

    Returns:
        bool
    """

def set_camera(position: point_3d, target: point_3d) -> None:
    """Sets the position of the camera, pointing to a target. 
    Args:
        position ( point_3d): position
        target ( point_3d): target

    Returns:
        None
    """

def show_perspective_central() -> None:
    """changes the viewmode to Perpective
    Args:

    Returns:
        None
    """

def set_color_without_material(a0: List[int], a1: int) -> None:
    """set color without material
    Args:
        a0 ( List[int]): a0
        a1 ( int): a1

    Returns:
        None
    """

def set_texture_rotated(a0: List[int], a1: bool) -> None:
    """set texture rotated
    Args:
        a0 ( List[int]): a0
        a1 ( bool): a1

    Returns:
        None
    """

def show_reference_side_beam(show: bool) -> None:
    """show reference side beam
    Args:
        show ( bool): show

    Returns:
        None
    """

def show_reference_side_panel(show: bool) -> None:
    """show reference side panel
    Args:
        show ( bool): show

    Returns:
        None
    """

def show_reference_side_wall(show: bool) -> None:
    """show reference side wall
    Args:
        show ( bool): show

    Returns:
        None
    """

def show_view_axo() -> None:
    """changes the viewmode to Axo
    Args:

    Returns:
        None
    """

def get_color(element_id: int) -> int:
    """Gets the element color 
    Args:
        element_id ( int): element_id

    Returns:
        color ID (int)
    """

def get_opengl_color(element_id: int) -> rgb_color:
    """Gets the element OpenGL color 
    Args:
        element_id ( int): element_id

    Returns:
        RBG color (rgb_color)
    """

def get_material(element_id: int) -> int:
    """Gets the element material 
    Args:
        element_id ( int): element_id

    Returns:
        material ID (int)
    """

def get_rgb_from_cadwork_color_id(color_id: None) -> rgb_color:
    """get rgb from cadwork color id
    Args:
        color_id ( None): color_id

    Returns:
        colorRGB (rgb_color)
    """

def is_texture_rotated(a0: int) -> bool:
    """is texture rotated
    Args:
        a0 ( int): a0

    Returns:
        bool
    """

def get_camera_data() -> camera_data:
    """Get the camera data 
    Args:

    Returns:
        camera data (camera_data)
    """

def set_camera_data(camera_data: None) -> None:
    """Set the camera data - this will override the current camera data 
    Args:
        camera_data ( None): camera_data

    Returns:
        None
    """

