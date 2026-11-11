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
    """Set the color of elements and reset their material to that color.

    Changes the display color of every listed element and also replaces the element's material with
    the one that belongs to that color number, so a previous material is lost. Use
    `visualization_controller.set_color_without_material()` to keep the material. The elements are
    rebuilt immediately. Read the color back with `visualization_controller.get_color()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        color_id: cadwork color number as shown in the color palette.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_color(element_ids, 3)
    """

def set_opengl_color(element_id_list: list[ElementId], color: rgb_color) -> None:
    """Set the OpenGL color of elements (currently has no effect).

    In the current implementation this function does not change any element; it only triggers the
    display refresh. To color elements use `visualization_controller.set_color()` or
    `visualization_controller.set_color_without_material()`.

    Parameters:
        element_id_list: List of element IDs. Ignored by the current implementation.
        color: `rgb_color` to apply. Ignored by the current implementation.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_opengl_color(element_ids, cadwork.rgb_color(255, 0, 0))
    """

def is_active(element_id: ElementId) -> bool:
    """Test whether an element is active.

    Active elements are the elements currently selected as the working set in the model; most
    element functions operate on them. Returns False for an ID that does not exist. Change the state
    with `visualization_controller.set_active()` and `visualization_controller.set_inactive()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_visible_identifiable_element_ids():
        ...     if vc.is_active(element_id):
        ...         print(element_id)

    Returns:
        True if the element is active, otherwise False. False if the element does not exist.
    """

def set_active(element_id_list: list[ElementId]) -> None:
    """Activate elements.

    Makes the listed elements part of the active set, which most other functions work on (see
    `element_controller.get_active_identifiable_element_ids()`). Other elements keep their current
    state. The display is refreshed if automatic display refresh is on. Reverse with
    `visualization_controller.set_inactive()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_all_identifiable_element_ids()`. Pass IDs of existing elements
            only.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_all_identifiable_element_ids()
        >>> vc.set_active(element_ids)
    """

def set_inactive(element_id_list: list[ElementId]) -> None:
    """Deactivate elements.

    Removes the listed elements from the active set. Other elements keep their state and the
    elements stay visible. IDs that do not exist are skipped. Reverse with
    `visualization_controller.set_active()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_inactive(element_ids)
    """

def is_visible(element_id: ElementId) -> bool:
    """Test whether an element is visible.

    Checks the current display state of the element in the active document. Returns False for an ID
    that does not exist. Change the state with `visualization_controller.set_visible()` and
    `visualization_controller.set_invisible()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_all_identifiable_element_ids()
        >>> hidden = [i for i in element_ids if not vc.is_visible(i)]
        >>> print(len(hidden))

    Returns:
        True if the element is visible, otherwise False. False if the element does not exist.
    """

def set_visible(element_id_list: list[ElementId]) -> None:
    """Show hidden elements.

    Makes the listed elements visible again. Only elements (construction elements), auxiliary
    objects, export solids and containers are affected; other object kinds in the list are not
    shown. The display is refreshed if automatic display refresh is on. Hide elements with
    `visualization_controller.set_invisible()`; to show everything use
    `visualization_controller.show_all_elements()`.

    Parameters:
        element_id_list: List of element IDs of hidden elements, e.g. IDs remembered before calling
            `visualization_controller.set_invisible()`. Pass IDs of existing elements only.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_invisible(element_ids)
        >>> vc.set_visible(element_ids)
    """

def set_invisible(element_id_list: list[ElementId]) -> None:
    """Hide elements.

    Hides the listed elements. Active elements in the list are deactivated first, so hidden elements
    are never active. The display is refreshed if automatic display refresh is on. Show them again
    with `visualization_controller.set_visible()`; check the state with
    `visualization_controller.is_visible()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Pass IDs of existing
            elements only.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_invisible(element_ids)
    """

def is_immutable(element_id: ElementId) -> bool:
    """Test whether an element is protected against modification.

    Returns True if the element is marked immutable for any reason, not only by the API.
    `visualization_controller.set_mutable()` removes just the API mark, so this can still return
    True afterwards. Returns False for an ID that does not exist.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if vc.is_immutable(element_id):
        ...         print(element_id)

    Returns:
        True if the element is immutable, otherwise False. False if the element does not exist.
    """

def set_immutable(element_id_list: list[ElementId]) -> None:
    """Mark elements as immutable.

    Sets the API immutability mark on the listed elements and shows them with the immutable
    appearance in the view. IDs that do not exist are skipped. Remove the mark with
    `visualization_controller.set_mutable()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_immutable(element_ids)
    """

def set_mutable(element_id_list: list[ElementId]) -> None:
    """Remove the API immutability mark from elements.

    Clears only the immutability mark set through `visualization_controller.set_immutable()`. An
    element that is immutable for another reason stays immutable and keeps its immutable appearance.
    IDs that do not exist are skipped.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_mutable(element_ids)
        >>> print([vc.is_immutable(i) for i in element_ids])
    """

def show_all_elements() -> None:
    """Show all hidden elements.

    Makes every hidden object in the document visible again, regardless of which function hid it.
    Activation is not changed. The display is refreshed if automatic display refresh is on.
    Counterpart of `visualization_controller.hide_all_elements()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_all_elements()
    """

def hide_all_elements() -> None:
    """Hide all elements and deactivate them.

    Hides practically every visible object in the document (elements, dimensions, text documents,
    point clouds, clipping boxes and others) and deactivates them. Use it to start from an empty
    view, then show selected elements with `visualization_controller.set_visible()`. Restore
    everything with `visualization_controller.show_all_elements()`, or save the state first with
    `visualization_controller.save_visibility_state()`.

    Examples:
        >>> import visualization_controller as vc

        >>> state = vc.save_visibility_state()
        >>> vc.hide_all_elements()
    """

def zoom_all_elements() -> None:
    """Zoom the view to fit all elements.

    Changes only the camera so that the whole model is in view. Use
    `visualization_controller.zoom_active_elements()` to fit only the active elements.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.zoom_all_elements()
    """

def zoom_active_elements() -> None:
    """Zoom the view to fit the active elements.

    Changes only the camera so that the active elements fill the view. Activate elements first with
    `visualization_controller.set_active()`. Use `visualization_controller.zoom_all_elements()` to
    fit the whole model.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> vc.set_active(ec.get_all_identifiable_element_ids()[:1])
        >>> vc.zoom_active_elements()
    """

def refresh() -> None:
    """Redraw the 3D view.

    Forces an immediate redraw of the drawing area. Call it at the end of a script that changed
    colors, visibility or camera when the result must be visible before the script ends.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.refresh()
    """

def set_material(element_id_list: list[ElementId], element_id: ElementId) -> None:
    """Assign a material to elements.

    Sets the material of every listed element; the element is marked as modified and redrawn if
    automatic display refresh is on. Elements without material attributes and IDs that do not exist
    are skipped. Read the current material with `visualization_controller.get_material()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        element_id: Material ID (not an element ID, despite the name), e.g. from
            `material_controller.get_material_id()`.

    Examples:
        >>> import element_controller as ec
        >>> import material_controller as mtc
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> material_id = mtc.get_material_id('Spruce')
        >>> vc.set_material(element_ids, material_id)
    """

def save_visibility_state() -> 'visibility_state':
    """Save which elements are currently visible or hidden.

    Records the visible/hidden state of every element in the document and returns it as an object.
    Pass it to `visualization_controller.restore_visibility_state()` after temporarily hiding or
    showing elements. Activation is not stored; use
    `visualization_controller.save_activation_state()` for that.

    Examples:
        >>> import visualization_controller as vc

        >>> state = vc.save_visibility_state()
        >>> vc.hide_all_elements()
        >>> vc.restore_visibility_state(state)

    Returns:
        Visibility state object for all visible and hidden elements.
    """

def restore_visibility_state(state: None) -> None:
    """Restore a visibility state saved earlier.

    Shows or hides each recorded element as stored by
    `visualization_controller.save_visibility_state()`. Elements that no longer exist are skipped;
    elements created since the save are not touched. Activation is not changed. The state that is
    restored is always the one from the most recent call of
    `visualization_controller.save_visibility_state()`, whichever object is passed in.

    Parameters:
        state: Object returned by `visualization_controller.save_visibility_state()`.

    Examples:
        >>> import visualization_controller as vc

        >>> state = vc.save_visibility_state()
        >>> vc.hide_all_elements()
        >>> vc.restore_visibility_state(state)
    """

def save_activation_state() -> 'activation_state':
    """Save which elements are currently active.

    Records the active/inactive state of every element in the document and returns it as an object.
    Pass it to `visualization_controller.restore_activation_state()` after changing the active set.
    Visibility is not stored; use `visualization_controller.save_visibility_state()` for that.

    Examples:
        >>> import visualization_controller as vc

        >>> state = vc.save_activation_state()
        >>> vc.restore_activation_state(state)

    Returns:
        Activation state object for all visible and hidden elements.
    """

def restore_activation_state(state: None) -> None:
    """Restore an activation state saved earlier.

    Activates or deactivates each recorded element as stored by
    `visualization_controller.save_activation_state()`. Elements that no longer exist are skipped;
    elements created since the save are not touched. The state that is restored is always the one
    from the most recent call of `visualization_controller.save_activation_state()`, whichever
    object is passed in.

    Parameters:
        state: Object returned by `visualization_controller.save_activation_state()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> state = vc.save_activation_state()
        >>> vc.set_active(ec.get_all_identifiable_element_ids())
        >>> vc.restore_activation_state(state)
    """

def show_view_positive_x() -> None:
    """Switch the view to look along the positive X axis.

    Same as choosing the +X view in the cadwork view menu. Changes only the camera orientation, no
    model data. Other standard views: `visualization_controller.show_view_negative_x()`,
    `visualization_controller.show_view_positive_y()`,
    `visualization_controller.show_view_positive_z()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_positive_x()
    """

def show_view_negative_x() -> None:
    """Switch the view to look along the negative X axis.

    Same as choosing the opposite X view in the cadwork view menu. Changes only the camera
    orientation, no model data. Counterpart of `visualization_controller.show_view_positive_x()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_negative_x()
    """

def show_view_positive_y() -> None:
    """Switch the view to look along the positive Y axis.

    Same as choosing the +Y view in the cadwork view menu. Changes only the camera orientation, no
    model data. Counterpart of `visualization_controller.show_view_negative_y()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_positive_y()
    """

def show_view_negative_y() -> None:
    """Switch the view to look along the negative Y axis.

    Same as choosing the opposite Y view in the cadwork view menu. Changes only the camera
    orientation, no model data. Counterpart of `visualization_controller.show_view_positive_y()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_negative_y()
    """

def show_view_positive_z() -> None:
    """Switch the view to look along the positive Z axis.

    Same as choosing the +Z view in the cadwork view menu. Changes only the camera orientation, no
    model data. Counterpart of `visualization_controller.show_view_negative_z()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_positive_z()
    """

def show_view_negative_z() -> None:
    """Switch the view to look along the negative Z axis.

    Same as choosing the opposite Z view in the cadwork view menu. Changes only the camera
    orientation, no model data. Counterpart of `visualization_controller.show_view_positive_z()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_negative_z()
    """

def show_view_standard_axo() -> None:
    """Switch the view to the standard axonometric view.

    Same as choosing the standard axonometry in the cadwork view menu. Changes only the camera, no
    model data. See also `visualization_controller.show_view_axo()` and
    `visualization_controller.show_perspective_central()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_standard_axo()
    """

def show_view_wireframe() -> None:
    """Switch the render mode to wireframe.

    Same as choosing the wireframe render mode in the cadwork view menu. Affects only how the model
    is drawn; the camera is unchanged. Other render modes:
    `visualization_controller.show_view_hidden_lines()`,
    `visualization_controller.show_view_shaded1()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_wireframe()
    """

def show_view_hidden_lines() -> None:
    """Switch the render mode to hidden lines.

    Same as choosing the hidden-line render mode in the cadwork view menu. Affects only how the
    model is drawn; the camera is unchanged. Variant with dashed hidden edges:
    `visualization_controller.show_view_dashed_hidden_lines()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_hidden_lines()
    """

def show_view_dashed_hidden_lines() -> None:
    """Switch the render mode to hidden lines shown dashed.

    Same as choosing the dashed hidden-line render mode in the cadwork view menu. Affects only how
    the model is drawn; the camera is unchanged. Variant without dashes:
    `visualization_controller.show_view_hidden_lines()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_dashed_hidden_lines()
    """

def show_view_shaded2() -> None:
    """Switch the render mode to shaded mode 2.

    Same as choosing the shaded 2 entry in the cadwork view menu. Affects only how the model is
    drawn; the camera is unchanged. The other shaded mode is
    `visualization_controller.show_view_shaded1()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_shaded2()
    """

def show_view_shaded1() -> None:
    """Switch the render mode to shaded mode 1.

    Same as choosing the shaded 1 entry in the cadwork view menu. Affects only how the model is
    drawn; the camera is unchanged. The other shaded mode is
    `visualization_controller.show_view_shaded2()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_shaded1()
    """

def is_selectable(element_id: ElementId) -> bool:
    """Test whether an element can be selected by the user.

    Returns the selectable flag of the element. Elements made unselectable cannot be picked
    interactively. Returns False for an ID that does not exist. Change the flag with
    `visualization_controller.set_selectable()` and `visualization_controller.set_unselectable()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, vc.is_selectable(element_id))

    Returns:
        True if the element is selectable, otherwise False. False if the element does not exist.
    """

def set_unselectable(element_id_list: list[ElementId]) -> None:
    """Make elements unselectable by the user.

    Clears the selectable flag of the listed elements so they cannot be picked interactively.
    Visibility and activation are unchanged. IDs that do not exist are skipped. Reverse with
    `visualization_controller.set_selectable()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_unselectable(element_ids)
    """

def set_selectable(element_id_list: list[ElementId]) -> None:
    """Make elements selectable by the user again.

    Sets the selectable flag of the listed elements. IDs that do not exist are skipped. Reverse with
    `visualization_controller.set_unselectable()`; check with
    `visualization_controller.is_selectable()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_all_identifiable_element_ids()
        >>> vc.set_selectable(element_ids)
    """

def clear_errors() -> None:
    """Clear the stored API error messages.

    Empties the error message stack kept by the visualization controller. Call it before a series of
    calls if you want to ignore errors recorded earlier. Does not affect the model or the view.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.clear_errors()
    """

def load_marking_settings(settings_file_path: str) -> None:
    """Load marking definitions from a settings file.

    Reads marking definitions from an XML settings file. If the file contains no definitions or they
    are identical to the current ones, nothing changes. Otherwise all current marking definitions
    are deleted and replaced by those from the file, and the affected markings are invalidated.

    Parameters:
        settings_file_path: Full path of the marking settings file, with forward slashes, e.g.
            'C:/Data/marking.xml'.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.load_marking_settings('C:/Data/marking.xml')
    """

def is_plane_2d() -> bool:
    """Test whether the view is in 2D plane mode.

    Reports the state of the current view in the active document. Useful before calling view
    functions that only make sense in a 3D view.

    Examples:
        >>> import visualization_controller as vc

        >>> if vc.is_plane_2d():
        ...     print('2D plane view is active')

    Returns:
        True if the 2D plane view is active, otherwise False.
    """

def set_camera(position: point_3d, target: point_3d) -> None:
    """Place the camera at a position looking at a target point.

    Moves the camera to `position` and aims it at `target`. Both points are in model coordinates
    (mm). The view is redrawn if automatic display refresh is on. Read the full camera with
    `visualization_controller.get_camera_data()`.

    Parameters:
        position: `point_3d` camera position in mm.
        target: `point_3d` point the camera looks at, in mm.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc

        >>> position = cadwork.point_3d(10000.0, -10000.0, 8000.0)
        >>> target = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> vc.set_camera(position, target)
    """

def show_perspective_central() -> None:
    """Switch the view to central perspective.

    Same as defining the central perspective in the cadwork view menu. Changes only how the model is
    projected, no model data. For an axonometric view use
    `visualization_controller.show_view_axo()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_perspective_central()
    """

def set_color_without_material(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Set the color of elements and keep their material.

    Changes the display color of every listed element and rebuilds it, without touching the
    material. Use `visualization_controller.set_color()` to also replace the material. IDs that do
    not exist are skipped. Read the color back with `visualization_controller.get_color()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        color_id: cadwork color number as shown in the color palette.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_color_without_material(element_ids, 5)
    """

def set_texture_rotated(element_id_list: list[ElementId], flag: bool) -> None:
    """Rotate or reset the texture of elements by 90 degrees.

    Sets the texture rotation to 90 degrees (True) or 0 degrees (False) and rebuilds the element.
    Only elements that have a texture are changed; IDs that do not exist are skipped. Read the state
    back with `visualization_controller.is_texture_rotated()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        flag: True to rotate the texture by 90 degrees, False to reset it to 0 degrees.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_texture_rotated(element_ids, True)
    """

def show_reference_side_beam(show: bool) -> None:
    """Show or hide the reference side marker of beams.

    Turns the display of the reference side of beams on or off in the view. This is a global display
    option, not a property of individual elements. The view is redrawn if automatic display refresh
    is on. Equivalent switches: `visualization_controller.show_reference_side_panel()` and
    `visualization_controller.show_reference_side_wall()`.

    Parameters:
        show: True to show the reference side of beams, False to hide it.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_reference_side_beam(True)
    """

def show_reference_side_panel(show: bool) -> None:
    """Show or hide the reference side marker of panels.

    Turns the display of the reference side of panels on or off in the view. This is a global
    display option, not a property of individual elements. The view is redrawn if automatic display
    refresh is on. Equivalent switches: `visualization_controller.show_reference_side_beam()` and
    `visualization_controller.show_reference_side_wall()`.

    Parameters:
        show: True to show the reference side of panels, False to hide it.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_reference_side_panel(True)
    """

def show_reference_side_wall(show: bool) -> None:
    """Show or hide the reference side marker of walls.

    Turns the display of the reference side of walls on or off in the view. This is a global display
    option, not a property of individual elements. The view is redrawn if automatic display refresh
    is on. Equivalent switches: `visualization_controller.show_reference_side_beam()` and
    `visualization_controller.show_reference_side_panel()`.

    Parameters:
        show: True to show the reference side of walls, False to hide it.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_reference_side_wall(True)
    """

def show_view_axo() -> None:
    """Switch the view to the axonometric view.

    Same as choosing the axonometric view in the cadwork view menu. Changes only the camera, no
    model data. See also `visualization_controller.show_view_standard_axo()` and
    `visualization_controller.show_perspective_central()`.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.show_view_axo()
    """

def get_color(element_id: ElementId) -> int:
    """Get the color number of an element.

    Returns the cadwork color number the element is displayed with. Returns 0 for an ID that does
    not exist. Set colors with `visualization_controller.set_color()` or
    `visualization_controller.set_color_without_material()`; convert to RGB with
    `visualization_controller.get_rgb_from_cadwork_color_id()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     color_id = vc.get_color(element_id)
        ...     print(element_id, color_id)

    Returns:
        cadwork color number of the element, 0 if the element does not exist.
    """

def get_opengl_color(element_id: ElementId) -> rgb_color:
    """Get the OpenGL color of an element (currently always default).

    In the current implementation this function does not read the element and always returns a
    default-constructed `rgb_color`. To read an element's color use
    `visualization_controller.get_color()`, then
    `visualization_controller.get_rgb_from_cadwork_color_id()` to get RGB values.

    Parameters:
        element_id: Element ID. Ignored by the current implementation.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> color = vc.get_opengl_color(element_id)

    Returns:
        Default-constructed `rgb_color`, regardless of the element.
    """

def get_material(element_id: ElementId) -> MaterialId:
    """Get the material ID of an element.

    Returns the ID of the material assigned to the element. Returns 0 for an ID that does not exist.
    Assign materials with `visualization_controller.set_material()`; resolve names with the
    `material_controller` module.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An ID that does not exist
            gives the failure value.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     material_id = vc.get_material(element_id)
        ...     print(element_id, material_id)

    Returns:
        Material ID of the element, 0 if the element does not exist.
    """

def get_rgb_from_cadwork_color_id(color_id: ColorId) -> rgb_color:
    """Convert a cadwork color number to its RGB color.

    cadwork colors are numbered entries of the color palette. Use this to get the red, green and
    blue components of such a number, for example to reuse an element's color elsewhere. Read an
    element's color number with `visualization_controller.get_color()`.

    Parameters:
        color_id: cadwork color number, as shown in the color palette and returned by
            `visualization_controller.get_color()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> color_id = vc.get_color(element_ids[0])
        >>> rgb = vc.get_rgb_from_cadwork_color_id(color_id)
        >>> print(rgb.r, rgb.g, rgb.b)

    Returns:
        `rgb_color` with components `r`, `g`, `b` (0 to 255) for the palette entry.
    """

def is_texture_rotated(element_id: ElementId) -> bool:
    """Check whether the texture of an element is rotated by 90 degrees.

    True only when the element's texture rotation is 90 degrees. Set the rotation with
    `visualization_controller.set_texture_rotated()`.

    Parameters:
        element_id: ID of the element to test, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if vc.is_texture_rotated(element_id):
        ...         print(element_id, 'has a rotated texture')

    Returns:
        `True` if the texture is rotated by 90 degrees. `False` if it is not rotated, the element
        has no texture data, or the ID is invalid or deleted.
    """

def get_camera_data() -> camera_data:
    """Get a snapshot of the current 3d camera.

    Returns position, target, up vector, projection type and field size of the active 3d view. The
    object is a copy: changing it does not move the camera until you pass it to
    `visualization_controller.set_camera_data()`. For perspective projection the field of view is
    included and is never smaller than 0.0001.

    Examples:
        >>> import visualization_controller as vc

        >>> camera = vc.get_camera_data()
        >>> position = camera.get_position()
        >>> target = camera.get_target()
        >>> print(position.x, position.y, position.z)
        >>> print(target.x, target.y, target.z)

    Returns:
        `camera_data` with position, target and up vector as `point_3d` (model coordinates, mm), the
        projection type, field width and height and, for perspective projection, the field of view.
    """

def set_camera_data(camera_data: camera_data) -> None:
    """Move the 3d camera to the values of a camera_data object.

    Overrides the position, target, up vector, field size and projection type of the 3d view with
    the values in `camera_data`. Typically read the current camera with
    `visualization_controller.get_camera_data()`, change single values and set it back. For
    perspective projection the field of view is also applied (it is a program-wide setting); for
    orthographic projection it is ignored.

    Parameters:
        camera_data: Camera settings, from `visualization_controller.get_camera_data()`.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc

        >>> camera = vc.get_camera_data()
        >>> camera.set_position(cadwork.point_3d(5000.0, -8000.0, 4000.0))
        >>> camera.set_target(cadwork.point_3d(0.0, 0.0, 0.0))
        >>> vc.set_camera_data(camera)
    """

def is_cadwork_window_in_light_mode() -> bool:
    """Check whether the cadwork window uses the light color scheme.

    Reads the frame style of the graphics options. Useful to pick readable colors for your own
    output. Counterpart of `visualization_controller.is_cadwork_window_in_dark_mode()`.

    Examples:
        >>> import visualization_controller as vc

        >>> if vc.is_cadwork_window_in_light_mode():
        ...     print('light theme')
        ... else:
        ...     print('not light')

    Returns:
        `True` if the window frame style is light, otherwise `False`.
    """

def is_cadwork_window_in_dark_mode() -> bool:
    """Check whether the cadwork window uses the dark color scheme.

    Reads the frame style of the graphics options. Useful to pick readable colors for your own
    output. Counterpart of `visualization_controller.is_cadwork_window_in_light_mode()`.

    Examples:
        >>> import visualization_controller as vc

        >>> if vc.is_cadwork_window_in_dark_mode():
        ...     print('dark theme')
        ... else:
        ...     print('not dark')

    Returns:
        `True` if the window frame style is dark, otherwise `False`.
    """

def enter_working_plane(plane_normal: point_3d, plane_origin: point_3d) -> None:
    """Switch the view into a 2d working plane.

    Opens the 2d working plane defined by a normal vector and an origin point, like starting a
    working plane in the cadwork GUI. Leave it again with
    `visualization_controller.leave_working_plane()`. The normal is passed on as given and is not
    normalized here, so pass a unit vector.

    Parameters:
        plane_normal: Direction perpendicular to the plane as a `point_3d` vector of unit length,
            e.g. `point_3d(0, 0, 1)` for a horizontal plane.
        plane_origin: A point on the plane in model coordinates (mm).

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc

        >>> normal = cadwork.point_3d(0.0, 0.0, 1.0)
        >>> origin = cadwork.point_3d(0.0, 0.0, 3000.0)
        >>> vc.enter_working_plane(normal, origin)
    """

def get_element_transparency(element_id: ElementId) -> int:
    """Get the transparency of an element.

    Transparency of the element's own color, as a percentage. Elements that display their material
    texture have no own transparency and report 0, see
    `visualization_controller.get_use_material_texture()`. Change it with
    `visualization_controller.set_element_transparency()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> transparency = vc.get_element_transparency(element_ids[0])
        >>> print(f'Transparency: {transparency} %')

    Returns:
        Transparency in percent. 0 when the element uses its material texture, has no texture data,
        or the ID is invalid or deleted.
    """

def set_element_transparency(element_id_list: list[ElementId], value: int) -> None:
    """Set the transparency of elements.

    Applies the same transparency to every listed element and recreates its display. Elements that
    display their material texture, elements without texture data and invalid or deleted IDs are
    skipped silently, so call `visualization_controller.set_use_material_texture()` with `False`
    first if needed. Read the value back with `visualization_controller.get_element_transparency()`.
    The display is refreshed afterwards unless automatic display refresh is switched off.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An empty list does nothing.
        value: Transparency in percent. The value is passed on without a range check.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_use_material_texture(element_ids, False)
        >>> vc.set_element_transparency(element_ids, 50)
        >>> print(vc.get_element_transparency(element_ids[0]))
    """

def get_use_material_texture(element_id: ElementId) -> bool:
    """Check whether an element is shown with its material texture.

    Elements are drawn either with their own color or with the texture of their material. Change the
    setting with `visualization_controller.set_use_material_texture()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     if vc.get_use_material_texture(element_id):
        ...         print(element_id, 'shows the material texture')

    Returns:
        `True` if the element uses its material texture. `False` if it uses its own color, has no
        texture data, or the ID is invalid or deleted.
    """

def set_use_material_texture(element_id_list: list[ElementId], value: bool) -> None:
    """Switch elements between material texture and own color display.

    With `True` the elements are drawn with the texture of their material, with `False` with their
    own color and transparency. Each element is recreated in the view. Invalid or deleted IDs and
    elements without texture data are skipped silently. The display is refreshed afterwards unless
    automatic display refresh is switched off. Read back with
    `visualization_controller.get_use_material_texture()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An empty list does nothing.
        value: `True` to show the material texture, `False` to show the element's own color.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.set_use_material_texture(element_ids, False)
    """

def display_bitmaps_as_texture_representation_in_shaded1(flag: bool) -> None:
    """Show or hide bitmap textures in the Shaded 1 render view.

    Sets the graphics option that draws surface images (bitmaps) as textures in the Shaded 1 render
    view and rebuilds the shading mode. It is a global graphics setting, not tied to elements. The
    other shaded view is set with
    `visualization_controller.display_bitmaps_as_texture_representation_in_shaded2()`.

    Parameters:
        flag: `True` to display bitmaps as textures in Shaded 1, `False` to turn it off.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.display_bitmaps_as_texture_representation_in_shaded1(True)
    """

def display_bitmaps_as_texture_representation_in_shaded2(flag: bool) -> None:
    """Show or hide bitmap textures in the Shaded 2 render view.

    Sets the graphics option that draws surface images (bitmaps) as textures in the Shaded 2 render
    view and rebuilds the shading mode. It is a global graphics setting, not tied to elements. The
    other shaded view is set with
    `visualization_controller.display_bitmaps_as_texture_representation_in_shaded1()`.

    Parameters:
        flag: `True` to display bitmaps as textures in Shaded 2, `False` to turn it off.

    Examples:
        >>> import visualization_controller as vc

        >>> vc.display_bitmaps_as_texture_representation_in_shaded2(True)
    """

def leave_working_plane(exit_view: working_plane_exit_view) -> None:
    """Leave the 2d working plane and restore a 3d view.

    Does nothing when the 2d working plane is not active, so it can be called unconditionally.
    Otherwise it triggers the same action as the matching button of the cadwork left menu and
    refreshes the display unless automatic refresh is off. The action is not forced: when cadwork is
    in an interactive mode that disables it, nothing happens. Enter a working plane with
    `visualization_controller.enter_working_plane()`.

    Parameters:
        exit_view: Which 3d view to show afterwards, a `cadwork.working_plane_exit_view` member:
            `previous_view`, `standard_axonometry`, `view_positive_x`, `view_positive_y`,
            `view_positive_z` or `keep_current_camera`.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc

        >>> vc.leave_working_plane(cadwork.working_plane_exit_view.previous_view)
    """

def is_permanently_hidden(element_id: ElementId) -> bool:
    """Check whether an element is permanently hidden.

    Permanently hidden elements are taken out of the model's working set and stay hidden until shown
    again. This reports the flag for any element, including elements cadwork hid for its own
    purposes. Hide elements with `visualization_controller.hide_permanently()`.

    Parameters:
        element_id: ID of the element to test, e.g. from
            `element_controller.get_all_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> for element_id in ec.get_all_identifiable_element_ids():
        ...     if vc.is_permanently_hidden(element_id):
        ...         print(element_id, 'is permanently hidden')

    Returns:
        `True` if the element is permanently hidden. `False` otherwise, and `False` when the ID is
        invalid or deleted.
    """

def hide_permanently(element_id_list: list[ElementId]) -> None:
    """Hide elements permanently and remember that this API hid them.

    Only construction elements, auxiliary objects, export solids and containers are hidden; other
    elements in the list, invalid IDs and elements that are already permanently hidden are ignored.
    Hidden elements are deactivated first, and the fact that this API hid them is stored with the
    drawing. Show them again with `visualization_controller.show_permanently_hidden()` and list them
    with `visualization_controller.get_permanently_hidden_elements()`. The display is refreshed
    unless automatic refresh is off.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An empty list does nothing.

    Examples:
        >>> import element_controller as ec
        >>> import visualization_controller as vc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> vc.hide_permanently(element_ids)
        >>> print(vc.get_permanently_hidden_elements())
    """

def show_permanently_hidden(element_id_list: list[ElementId]) -> None:
    """Show elements again that were hidden with hide_permanently.

    Only elements that `visualization_controller.hide_permanently()` hid are shown; other IDs,
    including elements cadwork hid itself, and invalid IDs are ignored. Shown elements are marked as
    modified and the display is refreshed unless automatic refresh is off. Elements still hidden can
    be listed with `visualization_controller.get_permanently_hidden_elements()`.

    Parameters:
        element_id_list: List of element IDs to show, typically from
            `visualization_controller.get_permanently_hidden_elements()`. An empty list does
            nothing.

    Examples:
        >>> import visualization_controller as vc

        >>> hidden_ids = vc.get_permanently_hidden_elements()
        >>> vc.show_permanently_hidden(hidden_ids)
    """

def get_permanently_hidden_elements() -> list[ElementId]:
    """Get the elements hidden with hide_permanently that are still hidden.

    The marker is stored with the drawing, so the list also covers elements hidden in an earlier
    session. Elements cadwork hid for its own purposes are not included, and deleted elements are
    dropped. Pass the result to `visualization_controller.show_permanently_hidden()` to restore
    them.

    Examples:
        >>> import visualization_controller as vc

        >>> hidden_ids = vc.get_permanently_hidden_elements()
        >>> print(f'{len(hidden_ids)} elements hidden through the API')

    Returns:
        List of element IDs, empty when there are none. Order is not specified.
    """

def get_background_color(render_view: render_view_type) -> rgb_color:
    """Get the background color a render view displays.

    Each render view keeps its own background. The result is the color actually shown: black or
    white for plain backgrounds, the stored color for a user background and black for an image
    background. Use `visualization_controller.get_background_type()` to tell a user color from a
    plain background.

    Parameters:
        render_view: The render view to query, a `cadwork.render_view_type` member. It need not be
            the one currently displayed.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> color = vc.get_background_color(cadwork.render_view_type.shading1)
        >>> print(f"Shading 1 background: {color.r} {color.g} {color.b}")

    Returns:
        The displayed background color, components 0 to 255; black when `render_view` is not a
        defined render view.
    """

def set_background_color(render_view: render_view_type, color: rgb_color) -> None:
    """Set a user background color for a render view.

    Stores the color and switches the background type of the render view to user, so the color is
    shown immediately. The background is saved with the drawing. Setting the values the render view
    already has, or an undefined `render_view`, changes nothing.

    Parameters:
        render_view: The render view to change, a `cadwork.render_view_type` member.
        color: The new color, components 0 to 255; larger values are clamped to 255.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> vc.set_background_color(cadwork.render_view_type.wireframe, cadwork.rgb_color(40, 40, 60))
    """

def get_background_type(render_view: render_view_type) -> background_type:
    """Get how the background of a render view is filled.

    Returns black, white, user or image. Read the color of a user background with
    `visualization_controller.get_background_color()`.

    Parameters:
        render_view: The render view to query, a `cadwork.render_view_type` member. It need not be
            the one currently displayed.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> if vc.get_background_type(cadwork.render_view_type.hidden_line) == cadwork.background_type.image:
        ...     print("Hidden line view uses a background image")

    Returns:
        The fill type; `cadwork.background_type.black` when `render_view` is not a defined render
        view.
    """

def set_background_type(render_view: render_view_type, type: background_type) -> None:
    """Set how the background of a render view is filled.

    Switching to user shows the color last stored for that render view, see
    `visualization_controller.set_background_color()`. The image type cannot be set through the API;
    passing it, or an undefined `render_view`, changes nothing. The background is saved with the
    drawing.

    Parameters:
        render_view: The render view to change, a `cadwork.render_view_type` member.
        type: The new fill type: black, white or user.

    Examples:
        >>> import cadwork
        >>> import visualization_controller as vc
        >>> vc.set_background_type(cadwork.render_view_type.shading2, cadwork.background_type.white)
    """
