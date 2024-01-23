from typing import List

from cadwork import camera_data
from cadwork import point_3d
from cadwork import rgb_color


def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """


def set_color(element_id_list: List[int], color_id: int) -> None:
    """set color
    Args:
        element_id_list ( List[int]): element_id_list
        color_id ( int): color_id

    Returns:
        None
    """


def set_opengl_color(element_id_list: List[int], color: None) -> None:
    """set opengl color
    Args:
        element_id_list ( List[int]): element_id_list
        color ( None): color

    Returns:
        None
    """


def is_active(element_id: int) -> bool:
    """is active
    Args:
        element_id ( int): element_id

    Returns:
        is element active (bool)
    """


def set_active(element_id_list: List[int]) -> None:
    """set active
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_inactive(element_id_list: List[int]) -> None:
    """set inactive
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def is_visible(element_id: int) -> bool:
    """is visible
    Args:
        element_id ( int): element_id

    Returns:
        is element visible (bool)
    """


def set_visible(element_id_list: List[int]) -> None:
    """set visible
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_invisible(element_id_list: List[int]) -> None:
    """set invisible
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def is_immutable(element_id: int) -> bool:
    """is immutable
    Args:
        element_id ( int): element_id

    Returns:
        is element immutable (bool)
    """


def set_immutable(element_id_list: List[int]) -> None:
    """set immutable
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_mutable(element_id_list: List[int]) -> None:
    """set mutable
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def show_all_elements() -> None:
    """show all elements
    Args:

    Returns:
        None
    """


def hide_all_elements() -> None:
    """hide all elements
    Args:

    Returns:
        None
    """


def zoom_all_elements() -> None:
    """zoom all elements
    Args:

    Returns:
        None
    """


def zoom_active_elements() -> None:
    """zoom active elements
    Args:

    Returns:
        None
    """


def refresh() -> None:
    """refresh
    Args:

    Returns:
        None
    """


def set_material(element_id_list: List[int], element_id: int) -> None:
    """set material
    Args:
        element_id_list ( List[int]): element_id_list
        element_id ( int): element_id

    Returns:
        None
    """


def save_visibility_state() -> 'visibility_state':
    """save visibility state
    Args:

    Returns:
        visibility state (visibility_state)
    """


def restore_visibility_state(state: None) -> None:
    """restore visibility state
    Args:
        state ( None): state

    Returns:
        None
    """


def save_activation_state() -> 'activation_state':
    """save activation state
    Args:

    Returns:
        activation state (activation_state)
    """


def restore_activation_state(state: None) -> None:
    """restore activation state
    Args:
        state ( None): state

    Returns:
        None
    """


def show_view_positive_x() -> None:
    """show view positive x
    Args:

    Returns:
        None
    """


def show_view_negative_x() -> None:
    """show view negative x
    Args:

    Returns:
        None
    """


def show_view_positive_y() -> None:
    """show view positive y
    Args:

    Returns:
        None
    """


def show_view_negative_y() -> None:
    """show view negative y
    Args:

    Returns:
        None
    """


def show_view_positive_z() -> None:
    """show view positive z
    Args:

    Returns:
        None
    """


def show_view_negative_z() -> None:
    """show view negative z
    Args:

    Returns:
        None
    """


def show_view_standard_axo() -> None:
    """show view standard axo
    Args:

    Returns:
        None
    """


def show_view_wireframe() -> None:
    """show view wireframe
    Args:

    Returns:
        None
    """


def show_view_hidden_lines() -> None:
    """show view hidden lines
    Args:

    Returns:
        None
    """


def show_view_dashed_hidden_lines() -> None:
    """show view dashed hidden lines
    Args:

    Returns:
        None
    """


def show_view_shaded2() -> None:
    """show view shaded2
    Args:

    Returns:
        None
    """


def show_view_shaded1() -> None:
    """show view shaded1
    Args:

    Returns:
        None
    """


def is_selectable(element_id: int) -> bool:
    """is selectable
    Args:
        element_id ( int): element_id

    Returns:
        bool
    """


def set_unselectable(element_id_list: List[int]) -> None:
    """set unselectable
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_selectable(element_id_list: List[int]) -> None:
    """set selectable
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
    """load marking settings
    Args:
        settings_file_path ( str): settings_file_path

    Returns:
        None
    """


def is_plane_2d() -> bool:
    """is plane 2d
    Args:

    Returns:
        bool
    """


def set_camera(position: point_3d, target: point_3d) -> None:
    """set camera
    Args:
        position ( point_3d): position
        target ( point_3d): target

    Returns:
        None
    """


def show_perspective_central() -> None:
    """show perspective central
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
    """show view axo
    Args:

    Returns:
        None
    """


def get_color(element_id: int) -> int:
    """get color
    Args:
        element_id ( int): element_id

    Returns:
        color ID (int)
    """


def get_opengl_color(element_id: int) -> rgb_color:
    """get opengl color
    Args:
        element_id ( int): element_id

    Returns:
        RBG color (rgb_color)
    """


def get_material(element_id: int) -> int:
    """get material
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
    """get camera data
    Args:

    Returns:
        camera data (camera_data)
    """


def set_camera_data(camera_data: None) -> None:
    """set camera data
    Args:
        camera_data ( None): camera_data

    Returns:
        None
    """
