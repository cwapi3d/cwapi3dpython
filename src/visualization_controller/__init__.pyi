from typing import List
from cadwork import camera_data
from cadwork import point_3d
from cadwork import rgb_color

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def set_color(element_id_list: List[int], color_id: int) -> None:
    """Sets the element color

    Parameters:
        element_id_list: element_id_list
        color_id: color_id

    Returns:
        None
    """

def set_opengl_color(element_id_list: List[int], color: None) -> None:
    """Sets the element OpenGL color

    Parameters:
        element_id_list: element_id_list
        color: color

    Returns:
        None
    """

def is_active(element_id: int) -> bool:
    """Tests if element is active

    Parameters:
        element_id: element_id

    Returns:
        is element active
    """

def set_active(element_id_list: List[int]) -> None:
    """Sets element active

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_inactive(element_id_list: List[int]) -> None:
    """Sets the element inactive

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def is_visible(element_id: int) -> bool:
    """Tests if element is visible

    Parameters:
        element_id: element_id

    Returns:
        is element visible
    """

def set_visible(element_id_list: List[int]) -> None:
    """Sets the element visible

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_invisible(element_id_list: List[int]) -> None:
    """Sets the element invisible

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def is_immutable(element_id: int) -> bool:
    """Tests if the element is immutable

    Parameters:
        element_id: element_id

    Returns:
        is element immutable
    """

def set_immutable(element_id_list: List[int]) -> None:
    """Sets the element immutable

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_mutable(element_id_list: List[int]) -> None:
    """Sets the element mutable

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def show_all_elements() -> None:
    """Shows all elements

    Returns:
        None
    """

def hide_all_elements() -> None:
    """Hides all elements

    Returns:
        None
    """

def zoom_all_elements() -> None:
    """Zooms on all elements

    Returns:
        None
    """

def zoom_active_elements() -> None:
    """Zooms on all active elements

    Returns:
        None
    """

def refresh() -> None:
    """Refresh the drawing area

    Returns:
        None
    """

def set_material(element_id_list: List[int], element_id: int) -> None:
    """Sets the element material

    Parameters:
        element_id_list: element_id_list
        element_id: element_id

    Returns:
        None
    """

def save_visibility_state() -> visibility_state:
    """Saves the visibility state

    Returns:
        visibility state
    """

def restore_visibility_state(state: None) -> None:
    """Restores the visibility state

    Parameters:
        state: state

    Returns:
        None
    """

def save_activation_state() -> activation_state:
    """Saves the activation state

    Returns:
        activation state
    """

def restore_activation_state(state: None) -> None:
    """Restores the activation state

    Parameters:
        state: state

    Returns:
        None
    """

def show_view_positive_x() -> None:
    """Sets the view to +X

    Returns:
        None
    """

def show_view_negative_x() -> None:
    """Sets the view to -X

    Returns:
        None
    """

def show_view_positive_y() -> None:
    """Sets the view to +Y

    Returns:
        None
    """

def show_view_negative_y() -> None:
    """Sets the view to -Y

    Returns:
        None
    """

def show_view_positive_z() -> None:
    """Sets the view to +Z

    Returns:
        None
    """

def show_view_negative_z() -> None:
    """Sets the view to -Z

    Returns:
        None
    """

def show_view_standard_axo() -> None:
    """Sets the view to standard axonometry

    Returns:
        None
    """

def show_view_wireframe() -> None:
    """Sets the view to wireframe

    Returns:
        None
    """

def show_view_hidden_lines() -> None:
    """Sets the view to hidden lines

    Returns:
        None
    """

def show_view_dashed_hidden_lines() -> None:
    """Sets the view to dashed hidden lines

    Returns:
        None
    """

def show_view_shaded2() -> None:
    """Sets the view to shaded 2

    Returns:
        None
    """

def show_view_shaded1() -> None:
    """Sets the view to shaded 1

    Returns:
        None
    """

def is_selectable(element_id: int) -> bool:
    """Returns if the element is selectable

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

def set_unselectable(element_id_list: List[int]) -> None:
    """Sets a list of elements unselectable

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def set_selectable(element_id_list: List[int]) -> None:
    """Sets a list of elements selectable

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def load_marking_settings(settings_file_path: str) -> None:
    """Loads marking settings file

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """

def is_plane_2d() -> bool:
    """returns if plane 2d is active

    Returns:
        bool
    """

def set_camera(position: point_3d, target: point_3d) -> None:
    """Sets the position of the camera, pointing to a target.

    Parameters:
        position: position
        target: target

    Returns:
        None
    """

def show_perspective_central() -> None:
    """changes the viewmode to Perpective

    Returns:
        None
    """

def set_color_without_material(a0: List[int], a1: int) -> None:
    """set color without material

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def set_texture_rotated(a0: List[int], a1: bool) -> None:
    """set texture rotated

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def show_reference_side_beam(show: bool) -> None:
    """show reference side beam

    Parameters:
        show: show

    Returns:
        None
    """

def show_reference_side_panel(show: bool) -> None:
    """show reference side panel

    Parameters:
        show: show

    Returns:
        None
    """

def show_reference_side_wall(show: bool) -> None:
    """show reference side wall

    Parameters:
        show: show

    Returns:
        None
    """

def show_view_axo() -> None:
    """changes the viewmode to Axo

    Returns:
        None
    """

def get_color(element_id: int) -> int:
    """Gets the element color

    Parameters:
        element_id: element_id

    Returns:
        color ID
    """

def get_opengl_color(element_id: int) -> rgb_color:
    """Gets the element OpenGL color

    Parameters:
        element_id: element_id

    Returns:
        RBG color
    """

def get_material(element_id: int) -> int:
    """Gets the element material

    Parameters:
        element_id: element_id

    Returns:
        material ID
    """

def get_rgb_from_cadwork_color_id(color_id: None) -> rgb_color:
    """get rgb from cadwork color id

    Parameters:
        color_id: color_id

    Returns:
        colorRGB
    """

def is_texture_rotated(a0: int) -> bool:
    """is texture rotated

    Parameters:
        a0: a0

    Returns:
        bool
    """

def get_camera_data() -> camera_data:
    """Get the camera data

    Returns:
        camera data
    """

def set_camera_data(camera_data: None) -> None:
    """Set the camera data - this will override the current camera data

    Parameters:
        camera_data: camera_data

    Returns:
        None
    """

def is_cadwork_window_in_light_mode() -> bool:
    """Check if Cadwork window is in light mode

    Returns:
        window is in light mode
    """

def is_cadwork_window_in_dark_mode() -> bool:
    """Check if Cadwork window is in dark mode

    Returns:
        window is in dark mode
    """

