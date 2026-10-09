"""2D shop and workshop drawing generation.

Covers the production of 2D drawings from the 3D model: wireframe
and hidden-line views, layout-based and clipboard-based outputs,
section and detail generation (wall sections and similar), and
export-solid handling for shop-drawing workflows. The 2D-output
counterpart to file_controller's neutral 3D exports.
"""

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

def export_wall_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Exports a wall to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def export_export_solid_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Exports an export solid to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def export_piece_by_piece_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Exports a piece-by-piece to the clipboard.

    Parameters:
        clipboard_number: The clipboard number.
        element_id_list: The elements to export.
    """

def assign_export_solid(ceo_element_id_list: list[ElementId], element_id_list: list[ElementId]) -> None:
    """Assigns elements to an export solid.

    Parameters:
        ceo_element_id_list: The export solid to assign.
        element_id_list: The elements to assign.
    """

def export_container_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
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

def export_wall_with_clipboard_and_presetting(
    clipboard_number: UnsignedInt, element_id_list: list[ElementId], presetting_file: str
) -> None:
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
    """Clears all errors."""

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

def add_wall_section_horizontal_at_relative_position(element: ElementId, relative_position: float) -> bool:
    """Adds a horizontal section to a wall, floor or roof at a relative position across the element's width.

    Parameters:
        element: A cover wall, floor or roof (element envelope).
        relative_position: The relative position t in the open interval (0,1) across the element's width (along yl). 0 and 1 are rejected because they lie on the element's faces.

    Examples:
        >>> import shop_drawing_controller as sdc
        >>> import element_controller as ec
        >>> [wall] = ec.get_active_identifiable_element_ids()
        >>> added = sdc.add_wall_section_horizontal_at_relative_position(wall, 0.5)

    Returns:
        True if the section was added. False if nothing was added; getLastError then returns the reason and one of these error codes: - 1: the element does not exist or is not a wall, floor or roof (e.g. a beam). - 2: t is not in the open interval (0,1), is NaN or infinite, or the element has no width. - 3: a horizontal section already exists at this position (same yl position within the cadwork tolerance).
    """

def add_export_solid_cut(element: ElementId, name: str, normal: point_3d, origin: point_3d) -> bool:
    """Adds a named cut to an export solid or container, defined by a plane normal and an origin point on the plane.

    Parameters:
        element: An export solid or container.
        name: The cut name; it must not be empty and must not already be used by a cut of this element (exact match).
        normal: The plane normal in global coordinates; any non-zero length.
        origin: A point on the plane in global coordinates (mm).

    Examples:
        >>> import cadwork
        >>> import shop_drawing_controller as sdc
        >>> import element_controller as ec
        >>> [export_solid] = ec.get_active_identifiable_element_ids()
        >>> normal = cadwork.point_3d(1., 0., 0.)
        >>> origin = cadwork.point_3d(1500., 0., 0.)
        >>> added = sdc.add_export_solid_cut(export_solid, "A-A", normal, origin)

    Returns:
        True if the cut was added. False if nothing was added; getLastError then returns the reason and one of these error codes: - 1: the element does not exist or is not an export solid or container. - 2: aNormal is a zero-length vector. - 3: the plane does not lie strictly inside the element's extent along the normal. - 5: the element has no extent along the normal. - 6: aName is empty or consists of whitespace only. - 7: a cut with this name already exists on the element. - 8: the element's extent along the normal could not be determined. - 9: the plane lies inside the extent but does not intersect the element's body (e.g. the empty corner of an L-shaped body). - 10: the cut could not be saved.
    """

def add_export_solid_cut_at_relative_position(
    element: ElementId, name: str, normal: point_3d, relative_position: float
) -> bool:
    """Adds a named cut to an export solid or container, defined by a plane normal and a relative position across the element's extent along that normal.

    Parameters:
        element: An export solid or container.
        name: The cut name; it must not be empty and must not already be used by a cut of this element (exact match).
        normal: The plane normal in global coordinates; any non-zero length.
        relative_position: The position of the plane across the element's extent along aNormal, in the open interval (0,1); 0.5 is the middle.

    Examples:
        >>> import cadwork
        >>> import shop_drawing_controller as sdc
        >>> import element_controller as ec
        >>> [container] = ec.get_active_identifiable_element_ids()
        >>> normal = cadwork.point_3d(0., 0., 1.)
        >>> added = sdc.add_export_solid_cut_at_relative_position(container, "Mid height", normal, 0.5)

    Returns:
        True if the cut was added. False if nothing was added; getLastError then returns the reason and one of these error codes: - 1: the element does not exist or is not an export solid or container. - 2: aNormal is a zero-length vector. - 4: aRelativePosition is not inside the open interval (0,1), or is NaN. - 5: the element has no extent along the normal. - 6: aName is empty or consists of whitespace only. - 7: a cut with this name already exists on the element. - 8: the element's extent along the normal could not be determined. - 9: the plane does not intersect the element's body (e.g. the empty corner of an L-shaped body). - 10: the cut could not be saved.
    """
