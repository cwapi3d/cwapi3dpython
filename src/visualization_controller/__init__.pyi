"""On-screen presentation and viewing state.

Controls how the model is displayed without altering the underlying
data: visibility and activation of elements, view modes and camera
orientation, color overrides, and the saving/restoring of viewing
states. Strictly visual — nothing in this module changes element
properties or geometry persistently.
"""

from cadwork.camera_data import camera_data
from cadwork.point_3d import point_3d
from cadwork.api_types import *
from cadwork.rgb_color import rgb_color
from cadwork.working_plane_exit_view import working_plane_exit_view
from cadwork.background_type import background_type
from cadwork.render_view_type import render_view_type

def set_color(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Sets the element color.

    Parameters:
        element_id_list: The list of element id.
        color_id: The color ID to set.
    """

def set_opengl_color(element_id_list: list[ElementId], color: rgb_color) -> None:
    """Sets the element OpenGL color.

    Parameters:
        element_id_list: The list of element id.
        color: The OpenGL color to set.
    """

def is_active(element_id: ElementId) -> bool:
    """Tests if element is active.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is active, false otherwise.
    """

def set_active(element_id_list: list[ElementId]) -> None:
    """Sets element active.

    Parameters:
        element_id_list: The list of element id.
    """

def set_inactive(element_id_list: list[ElementId]) -> None:
    """Sets the element inactive.

    Parameters:
        element_id_list: The list of element id.
    """

def is_visible(element_id: ElementId) -> bool:
    """Tests if element is visible.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is visible, false otherwise.
    """

def set_visible(element_id_list: list[ElementId]) -> None:
    """Sets the element visible.

    Parameters:
        element_id_list: The list of element id.
    """

def set_invisible(element_id_list: list[ElementId]) -> None:
    """Sets the element invisible.

    Parameters:
        element_id_list: The list of element id.
    """

def is_immutable(element_id: ElementId) -> bool:
    """Tests if the element is immutable.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is immutable, false otherwise.
    """

def set_immutable(element_id_list: list[ElementId]) -> None:
    """Sets the element immutable.

    Parameters:
        element_id_list: The list of element id.
    """

def set_mutable(element_id_list: list[ElementId]) -> None:
    """Sets the element mutable.

    Parameters:
        element_id_list: The list of element id.
    """

def show_all_elements() -> None:
    """Shows all elements."""

def hide_all_elements() -> None:
    """Hides all elements."""

def zoom_all_elements() -> None:
    """Zooms on all elements."""

def zoom_active_elements() -> None:
    """Zooms on all active elements."""

def refresh() -> None:
    """Refresh the drawing area."""

def set_material(element_id_list: list[ElementId], element_id: ElementId) -> None:
    """Sets the element material.

    Parameters:
        element_id_list: The list of element id.
        element_id: The material ID to set.
    """

def save_visibility_state() -> 'visibility_state':
    """Saves the visibility state.

    Returns:
        The visibility state.
    """

def restore_visibility_state(state: None) -> None:
    """Restores the visibility state.

    Parameters:
        state: The visibility state to restore.
    """

def save_activation_state() -> 'activation_state':
    """Saves the activation state.

    Returns:
        The activation state.
    """

def restore_activation_state(state: None) -> None:
    """Restores the activation state.

    Parameters:
        state: The activation state to restore.
    """

def show_view_positive_x() -> None:
    """Sets the view to +X."""

def show_view_negative_x() -> None:
    """Sets the view to -X."""

def show_view_positive_y() -> None:
    """Sets the view to +Y."""

def show_view_negative_y() -> None:
    """Sets the view to -Y."""

def show_view_positive_z() -> None:
    """Sets the view to +Z."""

def show_view_negative_z() -> None:
    """Sets the view to -Z."""

def show_view_standard_axo() -> None:
    """Sets the view to standard axonometry."""

def show_view_wireframe() -> None:
    """Sets the view to wireframe."""

def show_view_hidden_lines() -> None:
    """Sets the view to hidden lines."""

def show_view_dashed_hidden_lines() -> None:
    """Sets the view to dashed hidden lines."""

def show_view_shaded2() -> None:
    """Sets the view to shaded 2."""

def show_view_shaded1() -> None:
    """Sets the view to shaded 1."""

def is_selectable(element_id: ElementId) -> bool:
    """Returns if the element is selectable.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is selectable, false otherwise.
    """

def set_unselectable(element_id_list: list[ElementId]) -> None:
    """Sets a list of elements unselectable.

    Parameters:
        element_id_list: The list of element id.
    """

def set_selectable(element_id_list: list[ElementId]) -> None:
    """Sets a list of elements selectable.

    Parameters:
        element_id_list: The list of element id.
    """

def clear_errors() -> None:
    """Clears all errors."""

def load_marking_settings(settings_file_path: str) -> None:
    """Loads marking settings file.

    Parameters:
        settings_file_path: The path to the settings file.
    """

def is_plane_2d() -> bool:
    """returns if plane 2d is active.

    Returns:
        True if plane 2D is active, false otherwise.
    """

def set_camera(position: point_3d, target: point_3d) -> None:
    """Sets the position of the camera, pointing to a target.

    Parameters:
        position: The position of the camera.
        target: The target the camera is pointing at.
    """

def show_perspective_central() -> None:
    """changes the viewmode to Perspective."""

def set_color_without_material(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Sets the color of a list of elements without changing their material.

    Parameters:
        element_id_list: A list of element id.
        color_id: The color ID to set.
    """

def set_texture_rotated(element_id_list: list[ElementId], flag: bool) -> None:
    """Sets the rotation of the texture for a list of elements.

    Parameters:
        element_id_list: A list of element id.
        flag: True to rotate the texture, false to not rotate it.
    """

def show_reference_side_beam(show: bool) -> None:
    """Shows or hides the reference side beam.

    Parameters:
        show: True to show the reference side beam, false to hide it.
    """

def show_reference_side_panel(show: bool) -> None:
    """Shows or hides the reference side panel.

    Parameters:
        show: True to show the reference side panel, false to hide it.
    """

def show_reference_side_wall(show: bool) -> None:
    """Shows or hides the reference side wall.

    Parameters:
        show: True to show the reference side wall, false to hide it.
    """

def show_view_axo() -> None:
    """changes the viewmode to Axo."""

def get_color(element_id: ElementId) -> int:
    """Gets the element color.

    Parameters:
        element_id: The element id.

    Returns:
        The color ID of the element.
    """

def get_opengl_color(element_id: ElementId) -> rgb_color:
    """Gets the element OpenGL color.

    Parameters:
        element_id: The element id.

    Returns:
        The OpenGL color of the element.
    """

def get_material(element_id: ElementId) -> MaterialId:
    """Gets the element material.

    Parameters:
        element_id: The element id.

    Returns:
        The material id.
    """

def get_rgb_from_cadwork_color_id(color_id: ColorId) -> rgb_color:
    """Gets the RGB color from a Cadwork color ID.

    Parameters:
        color_id: The Cadwork color ID.

    Returns:
        The RGB color corresponding to the Cadwork color ID.
    """

def is_texture_rotated(element_id: ElementId) -> bool:
    """Checks if the texture of an element is rotated.

    Parameters:
        element_id: The element id.

    Returns:
        True if the texture is rotated, false otherwise.
    """

def get_camera_data() -> camera_data:
    """Get the camera data.

    Returns:
        The camera data.
    """

def set_camera_data(camera_data: camera_data) -> None:
    """Set the camera data - this will override the current camera data.

    Parameters:
        camera_data: The camera data to set.
    """

def is_cadwork_window_in_light_mode() -> bool:
    """Check if Cadwork window is in light mode.

    Returns:
        True if the window is in light mode, false otherwise.
    """

def is_cadwork_window_in_dark_mode() -> bool:
    """Check if Cadwork window is in dark mode.

    Returns:
        True if the window is in dark mode, false otherwise.
    """

def enter_working_plane(plane_normal: point_3d, plane_origin: point_3d) -> None:
    """Enter 2d working plane.

    Parameters:
        plane_normal: A normalized plane vector.
        plane_origin: A plane origin.
    """

def get_element_transparency(element_id: ElementId) -> int:
    """Gets the element transparency.

    Parameters:
        element_id: The element id.

    Returns:
        Transparency value as percentage.
    """

def set_element_transparency(element_id_list: list[ElementId], value: int) -> None:
    """Sets the element transparency.

    Parameters:
        element_id_list: The element id list.
        value: Transparency value as percentage.
    """

def get_use_material_texture(element_id: ElementId) -> bool:
    """Check if element is using material texture.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is using material texture, false otherwise.
    """

def set_use_material_texture(element_id_list: list[ElementId], value: bool) -> None:
    """Sets element to use material texture.

    Parameters:
        element_id_list: The element id list.
        value: True to use material texture, false otherwise.
    """

def display_bitmaps_as_texture_representation_in_shaded1(flag: bool) -> None:
    """Set the graphic option to display bitmaps as textures in shaded 1.

    Parameters:
        flag: True to display bitmaps as textures in shaded 1, false otherwise.
    """

def display_bitmaps_as_texture_representation_in_shaded2(flag: bool) -> None:
    """Set the graphic option to display bitmaps as textures in shaded 2.

    Parameters:
        flag: True to display bitmaps as textures in shaded 2, false otherwise.
    """

def leave_working_plane(exit_view: working_plane_exit_view) -> None:
    """Leaves the 2d working plane and restores a 3d view. Does nothing when the 2d working plane is not currently active.

    Parameters:
        exit_view: The 3d view to restore on leaving.

    Note:
        When the working plane was entered from inside a container block, only workingPlaneExitView::previous_view returns into that container block; every other value leaves it and switches to the plain 3d model view.
    """

def is_permanently_hidden(element_id: ElementId) -> bool:
    """Tests whether an element is permanently hidden.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is permanently hidden, false otherwise, and false when the id does not resolve to an element.
    """

def hide_permanently(element_id_list: list[ElementId]) -> None:
    """Takes elements out of the model's working set and keeps them there.

    Parameters:
        element_id_list: The elements to hide permanently.
    """

def show_permanently_hidden(element_id_list: list[ElementId]) -> None:
    """Brings elements this API hid permanently back into the working set.

    Parameters:
        element_id_list: The elements to show again.
    """

def get_permanently_hidden_elements() -> list[ElementId]:
    """Gets the elements this API hid permanently and has not shown again.

    Returns:
        The permanently hidden elements owned by this API, empty when there are none.
    """

def get_background_color(render_view: render_view_type) -> rgb_color:
    """Gets the background color a render view displays.

    Each render view keeps its own background, as set in the graphics options dialog. The result is the color actually shown: black for a [`cadwork.background_type.black`][cadwork.background_type.background_type.black] background, white for [`cadwork.background_type.white`][cadwork.background_type.background_type.white], the stored color for [`cadwork.background_type.user`][cadwork.background_type.background_type.user], and black for [`cadwork.background_type.image`][cadwork.background_type.background_type.image], which has no single color. Use [`get_background_type`][visualization_controller.get_background_type] to tell a user color from a plain black or white background.

    Parameters:
        render_view: The render view to query. Need not be the render view currently displayed.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> color = vc.get_background_color(cadwork.render_view_type.shading1)
        >>> print(f"Shading 1 background: {color.r} {color.g} {color.b}")

    Returns:
        The displayed background color, components 0 to 255; black when `render_view` is not a defined render view.
    """

def set_background_color(render_view: render_view_type, color: rgb_color) -> None:
    """Sets a user background color for a render view.

    Stores the color and switches the render view's background type to [`cadwork.background_type.user`][cadwork.background_type.background_type.user], so the color is shown immediately. When `render_view` is the render view currently displayed, the 3d view is repainted. The background is saved with the drawing, so the active document is marked modified. Setting the color and type the render view already has, or an undefined `render_view`, changes nothing.

    Parameters:
        render_view: The render view to change.
        color: The new color, components 0 to 255; larger values are clamped to 255.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> vc.set_background_color(cadwork.render_view_type.wireframe, cadwork.rgb_color(40, 40, 60))
    """

def get_background_type(render_view: render_view_type) -> background_type:
    """Gets how the background of a render view is filled.

    Parameters:
        render_view: The render view to query. Need not be the render view currently displayed.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> if vc.get_background_type(cadwork.render_view_type.hidden_line) == cadwork.background_type.image:
        ...     print("Hidden line view uses a background image")

    Returns:
        The fill type; [`cadwork.background_type.black`][cadwork.background_type.background_type.black] when `render_view` is not a defined render view.
    """

def set_background_type(render_view: render_view_type, type: background_type) -> None:
    """Sets how the background of a render view is filled.

    Switching to [`cadwork.background_type.user`][cadwork.background_type.background_type.user] shows the color last stored for that render view (see [`set_background_color`][visualization_controller.set_background_color]); switching away from it keeps that color for later. When `render_view` is the render view currently displayed, the 3d view is repainted, and the active document is marked modified. Setting the type the render view already has changes nothing.

    **[`cadwork.background_type.image`][cadwork.background_type.background_type.image] cannot be set through the API**: an image background needs an image chosen in the graphics options dialog. Passing it, or an undefined `render_view`, changes nothing.

    Parameters:
        render_view: The render view to change.
        type: The new fill type: black, white or user.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> vc.set_background_type(cadwork.render_view_type.shading2, cadwork.background_type.white)
    """
