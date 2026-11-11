"""2D shop and workshop drawing generation.

Covers the production of 2D drawings from the 3D model: wireframe
and hidden-line views, layout-based and clipboard-based outputs,
section and detail generation (wall sections and similar), and
export-solid handling for shop-drawing workflows. The 2D-output
counterpart to file_controller's neutral 3D exports.
"""

from cadwork.point_3d import point_3d
from cadwork.api_types import *
from cadwork.export_solid_cut import export_solid_cut
from cadwork.wall_section import wall_section

def export_2d_wireframe_with_clipboard(clipboard_number: UnsignedInt, with_layout: bool) -> None:
    """Export the current view as a 2D wireframe drawing to a numbered clipboard.

    Creates a 2D drawing of the visible exportable construction elements, seen from the current 3D
    camera, and writes it to the 2D clipboard with the given number (as a clipboard file in the
    user's temp folder). The drawing shows all edges, including hidden ones. Use
    `export_2d_hidden_lines_with_clipboard()` for a hidden-line view or
    `export_2d_wireframe_with_2dc()` to write to a file instead. If the layout export settings are
    incomplete, cadwork shows a warning and opens the settings dialog.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        with_layout: True to export with the drawing layout (frame and layout settings); False to
            export the plain view without a layout.

    Examples:
        >>> import shop_drawing_controller as sdc

        ... # Export the visible elements, as seen in the current view, to clipboard 5
        >>> sdc.export_2d_wireframe_with_clipboard(5, False)
    """

def export_2d_hidden_lines_with_clipboard(clipboard_number: UnsignedInt, with_layout: bool) -> None:
    """Export the current view as a 2D hidden-line drawing to a numbered clipboard.

    Creates a 2D drawing of the visible exportable construction elements, seen from the current 3D
    camera, with hidden edges removed, and writes it to the 2D clipboard with the given number (as a
    clipboard file in the user's temp folder). Use `export_2d_wireframe_with_clipboard()` to keep
    all edges or `export_2d_hidden_lines_with_2dc()` to write to a file instead. If the layout
    export settings are incomplete, cadwork shows a warning and opens the settings dialog.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        with_layout: True to export with the drawing layout (frame and layout settings); False to
            export the plain view without a layout.

    Examples:
        >>> import shop_drawing_controller as sdc

        ... # Export the visible elements, as seen in the current view, to clipboard 6
        >>> sdc.export_2d_hidden_lines_with_clipboard(6, True)
    """

def export_2d_wireframe_with_2dc(file_path: str, with_layout: bool) -> None:
    """Export the current view as a 2D wireframe drawing to a 2DC file.

    Creates a 2D drawing of the visible exportable construction elements, seen from the current 3D
    camera, and saves it to the given 2DC file. The drawing shows all edges, including hidden ones.
    Use `export_2d_hidden_lines_with_2dc()` for a hidden-line view or
    `export_2d_wireframe_with_clipboard()` to fill a numbered clipboard instead. If the layout
    export settings are incomplete, cadwork shows a warning and opens the settings dialog.

    Parameters:
        file_path: Full path of the 2DC file to write, for example 'C:/temp/view.2dc'. The folder
            must exist; an existing file is replaced.
        with_layout: True to export with the drawing layout (frame and layout settings); False to
            export the plain view without a layout.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.export_2d_wireframe_with_2dc('C:/temp/view_wireframe.2dc', False)
    """

def export_2d_hidden_lines_with_2dc(file_path: str, with_layout: bool) -> None:
    """Export the current view as a 2D hidden-line drawing to a 2DC file.

    Creates a 2D drawing of the visible exportable construction elements, seen from the current 3D
    camera, with hidden edges removed, and saves it to the given 2DC file. Use
    `export_2d_wireframe_with_2dc()` to keep all edges or `export_2d_hidden_lines_with_clipboard()`
    to fill a numbered clipboard instead. If the layout export settings are incomplete, cadwork
    shows a warning and opens the settings dialog.

    Parameters:
        file_path: Full path of the 2DC file to write, for example 'C:/temp/view.2dc'. The folder
            must exist; an existing file is replaced.
        with_layout: True to export with the drawing layout (frame and layout settings); False to
            export the plain view without a layout.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.export_2d_hidden_lines_with_2dc('C:/temp/view_hidden.2dc', False)
    """

def export_wall_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Export the given wall elements as a wall shop drawing to a numbered clipboard.

    Runs the wall (timber frame) shop-drawing export for the listed elements with the currently
    stored wall export settings and writes the result to the 2D clipboard with the given number. IDs
    that do not exist are skipped. If the first valid element is a nesting parent or nesting raw
    part, the export switches to nesting mode and exports each such element together with its
    nesting children. To use settings from a preset file, call `load_export_wall_settings()` first
    or use `export_wall_with_clipboard_and_presetting()`.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        element_id_list: Element IDs of the walls to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> walls = [e for e in element_ids if ac.is_wall(e)]
        >>> if walls:
        ...     sdc.export_wall_with_clipboard(1, walls)
    """

def export_export_solid_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Export the drawings of the given export solids to a numbered clipboard.

    An export solid groups elements into one drawing unit for shop drawings. For each listed element
    that has elements assigned to it, the element is activated, and all active export solids are
    exported with the current export-solid settings to the 2D clipboard with the given number.
    Elements without assigned elements, and IDs that do not exist, are ignored; if none remain,
    nothing is exported. Afterwards all elements are deactivated, including elements that were
    active before the call. Assign elements first with `assign_export_solid()`, and load settings
    with `load_export_solid_settings()`.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        element_id_list: Element IDs of the export solids to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()` filtered with
            `attribute_controller.is_export_solid()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> solids = [e for e in element_ids if ac.is_export_solid(e)]
        >>> sdc.export_export_solid_with_clipboard(2, solids)
    """

def export_piece_by_piece_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Export piece-by-piece drawings of the given elements to a numbered clipboard.

    Runs the piece-by-piece (single part) shop-drawing export for the listed elements with the
    current piece-by-piece settings. IDs that do not exist are skipped. If the clipboard number is
    above 99 or the list is empty, the call prints a red message to the cadwork console and does
    nothing. Load settings beforehand with `load_export_piece_by_piece_settings()`.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill, 0 to 99. Larger values are rejected
            with a console message.
        element_id_list: Element IDs of the parts to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Must not be empty.

    Examples:
        >>> import element_controller as ec
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> sdc.export_piece_by_piece_with_clipboard(3, element_ids)
    """

def assign_export_solid(ceo_element_id_list: list[ElementId], element_id_list: list[ElementId]) -> None:
    """Assign elements to an export solid.

    An export solid groups elements into one drawing unit for shop drawings. The listed elements are
    added to the elements already assigned to the export solid; existing assignments are kept. Only
    the first ID of the first list is used as the export solid. If it does not exist or is not an
    export solid, nothing happens; IDs in the second list that do not exist are skipped. Elements
    are temporarily activated during the call and deactivated afterwards, including elements that
    were active before. Read the assigned elements with
    `element_controller.get_export_solid_content_elements()`.

    Parameters:
        ceo_element_id_list: List whose first entry is the element ID of the export solid; further
            entries are ignored. Must not be empty.
        element_id_list: Element IDs of the elements to add to the export solid, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> solids = [e for e in element_ids if ac.is_export_solid(e)]
        >>> parts = [e for e in element_ids if not ac.is_export_solid(e)]
        >>> if solids:
        ...     sdc.assign_export_solid([solids[0]], parts)
    """

def export_container_with_clipboard(clipboard_number: UnsignedInt, element_id_list: list[ElementId]) -> None:
    """Export the drawings of the given containers to a numbered clipboard.

    A container groups elements into one drawing unit for shop drawings. For each listed element
    that has elements assigned to it, the element is activated, and all active containers are
    exported with the current container settings to the 2D clipboard with the given number. Elements
    without assigned elements, and IDs that do not exist, are ignored; if none remain, nothing is
    exported. Afterwards all elements are deactivated, including elements that were active before
    the call. Load settings beforehand with `load_export_container_settings()`.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        element_id_list: Element IDs of the containers to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()` filtered with
            `attribute_controller.is_container()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> containers = [e for e in element_ids if ac.is_container(e)]
        >>> sdc.export_container_with_clipboard(4, containers)
    """

def add_wall_section_horizontal(element_id: ElementId, position: point_3d) -> None:
    """Add a horizontal section to a wall, floor or roof element at a given position.

    Adds a horizontal section point to the element and rebuilds the element so the section shows. A
    non-existing element ID is ignored. The change is not recorded for undo, and the element type
    and the position are not validated here. To place a section by a relative position across the
    element width, with validation and undo, use
    `add_wall_section_horizontal_at_relative_position()`. Read the existing sections with
    `get_wall_sections()`.

    Parameters:
        element_id: Element ID of a wall, floor or roof, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        position: A point in global coordinates (mm) that the section passes through, e.g. a
            point on the element axis built from `geometry_controller.get_p1()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc
        >>> import shop_drawing_controller as sdc

        >>> [wall] = ec.get_active_identifiable_element_ids()
        >>> axis_middle = (gc.get_p1(wall) + gc.get_p2(wall)) * 0.5
        >>> sdc.add_wall_section_horizontal(wall, axis_middle)
        >>> sections = sdc.get_wall_sections(wall)
    """

def add_wall_section_vertical(element_id: ElementId, position: point_3d) -> None:
    """Add a vertical section to a wall, floor or roof element at a given position.

    Adds a vertical section point to the element and rebuilds the element so the section shows. A
    non-existing element ID is ignored. The change is not recorded for undo, and the element type
    and the position are not validated here. Read the existing sections with `get_wall_sections()`;
    add horizontal sections with `add_wall_section_horizontal()` or
    `add_wall_section_horizontal_at_relative_position()`.

    Parameters:
        element_id: Element ID of a wall, floor or roof, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        position: A point in global coordinates (mm) that the section passes through, e.g. a
            point on the element axis built from `geometry_controller.get_p1()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc
        >>> import shop_drawing_controller as sdc

        >>> [wall] = ec.get_active_identifiable_element_ids()
        >>> axis_middle = (gc.get_p1(wall) + gc.get_p2(wall)) * 0.5
        >>> sdc.add_wall_section_vertical(wall, axis_middle)
        >>> sections = sdc.get_wall_sections(wall)
    """

def export_wall_with_clipboard_and_presetting(
    clipboard_number: UnsignedInt, element_id_list: list[ElementId], presetting_file: str
) -> None:
    """Export wall shop drawings to a numbered clipboard using a presetting file.

    Like `export_wall_with_clipboard()`, but first loads the wall export settings from the given
    presetting file (as `load_export_wall_settings()` does), so the settings stay active afterwards.
    The listed elements are then exported to the 2D clipboard with the given number. IDs that do not
    exist are skipped. If the first valid element is a nesting parent or nesting raw part, the
    export switches to nesting mode and the nesting settings are also read from the presetting file.
    An empty presetting path means no settings are loaded.

    Parameters:
        clipboard_number: Number of the 2D clipboard to fill; it is written with three digits (7
            becomes 007). An existing clipboard with this number is overwritten.
        element_id_list: Element IDs of the walls to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        presetting_file: Full path of a saved wall export presetting file, for example
            'C:/presets/wall.ini'. Pass an empty string to use the current settings.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> import shop_drawing_controller as sdc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> walls = [e for e in element_ids if ac.is_wall(e)]
        >>> if walls:
        ...     sdc.export_wall_with_clipboard_and_presetting(1, walls, 'C:/presets/wall.ini')
    """

def load_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Load the piece-by-piece export settings from a file.

    Reads all piece-by-piece export settings from the given settings file and makes them the current
    settings for later calls to `export_piece_by_piece_with_clipboard()`. Create such a file with
    `save_export_piece_by_piece_settings()`. No result is returned, so check that the path exists
    beforehand.

    Parameters:
        settings_file_path: Full path of a settings file written by
            `save_export_piece_by_piece_settings()`, for example 'C:/settings/pbp.ini'.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.load_export_piece_by_piece_settings('C:/settings/pbp.ini')
    """

def save_export_piece_by_piece_settings(settings_file_path: str) -> None:
    """Save the current piece-by-piece export settings to a file.

    Writes all current piece-by-piece export settings to the given file so they can be restored
    later with `load_export_piece_by_piece_settings()`. Nothing is returned, so a failed write is
    not reported.

    Parameters:
        settings_file_path: Full path of the file to write, for example 'C:/settings/pbp.ini'. The
            folder must exist.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.save_export_piece_by_piece_settings('C:/settings/pbp.ini')
    """

def clear_errors() -> None:
    """Discard the stored error messages of failed shop drawing calls.

    Failed calls such as `add_export_solid_cut()` or
    `add_wall_section_horizontal_at_relative_position()` store the reason for the failure, and
    `get_wall_sections()` and `get_export_solid_cuts()` do so when they return an empty list because
    the element is not supported. This call removes all stored reasons, so that old errors are not
    mistaken for the result of a later call. Call it before a sequence of calls whose errors you
    want to inspect.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.clear_errors()
    """

def load_export_wall_settings(settings_file_path: str) -> None:
    """Load wall export settings from a presetting file.

    Reads the wall shop-drawing settings from the given presetting file and makes them the current
    settings for later wall exports, for example `export_wall_with_clipboard()`. If the file belongs
    to a different wall type than the active one, the active wall type is switched. The presetting
    name is set from the file name, and the names of the four preset buttons are kept. Nothing is
    returned, so an unreadable file is not reported.

    Parameters:
        settings_file_path: Full path of a wall export presetting file saved from cadwork, for
            example 'C:/presets/wall.ini'.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.load_export_wall_settings('C:/presets/wall.ini')
    """

def load_export_solid_settings(settings_file_path: str) -> None:
    """Load export solid settings from a settings file.

    Reads the export solid shop-drawing settings from the given file and stores them as the current
    settings for later calls to `export_export_solid_with_clipboard()`. Nothing is returned, so an
    unreadable file is not reported. Load container settings with
    `load_export_container_settings()`.

    Parameters:
        settings_file_path: Full path of an export solid settings file saved from cadwork, for
            example 'C:/settings/solid.ini'.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.load_export_solid_settings('C:/settings/solid.ini')
    """

def load_export_container_settings(settings_file_path: str) -> None:
    """Load container export settings from a settings file.

    Reads the container shop-drawing settings from the given file and stores them as the current
    settings for later calls to `export_container_with_clipboard()`. Nothing is returned, so an
    unreadable file is not reported. Load export solid settings with `load_export_solid_settings()`.

    Parameters:
        settings_file_path: Full path of a container settings file saved from cadwork, for example
            'C:/settings/container.ini'.

    Examples:
        >>> import shop_drawing_controller as sdc

        >>> sdc.load_export_container_settings('C:/settings/container.ini')
    """

def add_wall_section_horizontal_at_relative_position(element: ElementId, relative_position: float) -> bool:
    """Add a horizontal section across the width of a wall, floor or roof.

    A horizontal section splits a cover wall, floor or roof into layers along its width for the shop
    drawing. The section is placed at the relative position across the element's width and can be
    undone. Returns False and stores the reason (see `clear_errors()`) if nothing was added.

    Parameters:
        element: Element ID of a cover wall, floor or roof (element envelope).
        relative_position: Relative position t strictly between 0 and 1 across the element's width
            (along its local y axis). 0 and 1 are rejected because they lie on the element's faces.

    Examples:
        >>> import shop_drawing_controller as sdc
        >>> import element_controller as ec
        >>> [wall] = ec.get_active_identifiable_element_ids()
        >>> added = sdc.add_wall_section_horizontal_at_relative_position(wall, 0.5)

    Returns:
        True if the section was added. False if nothing was added: the element does not exist or is
        not a wall, floor or roof (e.g. a beam), t is not strictly between 0 and 1 (or is NaN or
        infinite) or the element has no width, or a horizontal section already exists at this
        position.
    """

def add_export_solid_cut(element: ElementId, name: str, normal: point_3d, origin: point_3d) -> bool:
    """Add a named cut plane to an export solid or container from a normal and a point.

    A cut divides an export solid or container into separate views in the shop drawing. The plane is
    given by its normal and a point on it, and it must lie inside the element's extent along the
    normal and intersect the element's body. The cut is saved with the element and can be undone.
    Returns False and stores the reason (see `clear_errors()`) if nothing was added. Use
    `add_export_solid_cut_at_relative_position()` to place the plane by a relative position instead,
    and `get_export_solid_cuts()` to read cuts back.

    Parameters:
        element: Element ID of an export solid or container.
        name: Cut name; it must not be empty or whitespace only, and must not already be used by a
            cut of this element (exact match).
        normal: Plane normal in global coordinates; any non-zero length (it is not required to be
            normalized).
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
        True if the cut was added. False if nothing was added: the element does not exist or is not
        an export solid or container, the normal has zero length, the plane does not lie strictly
        inside the element's extent along the normal (or the extent is zero or unavailable), the
        name is empty or already used, the plane does not intersect the element's body (e.g. the
        empty corner of an L-shaped body), or the cut could not be saved.
    """

def add_export_solid_cut_at_relative_position(
    element: ElementId, name: str, normal: point_3d, relative_position: float
) -> bool:
    """Add a named cut plane to an export solid or container at a relative position.

    A cut divides an export solid or container into separate views in the shop drawing. The plane is
    perpendicular to the given normal and placed at a relative position across the element's extent
    along that normal. It must intersect the element's body. The cut is saved with the element and
    can be undone. Returns False and stores the reason (see `clear_errors()`) if nothing was added.
    Use `add_export_solid_cut()` to define the plane by a point instead.

    Parameters:
        element: Element ID of an export solid or container.
        name: Cut name; it must not be empty or whitespace only, and must not already be used by a
            cut of this element (exact match).
        normal: Plane normal in global coordinates; any non-zero length (it is not required to be
            normalized).
        relative_position: Position of the plane across the element's extent along the normal,
            strictly between 0 and 1; 0.5 is the middle. NaN is rejected.

    Examples:
        >>> import cadwork
        >>> import shop_drawing_controller as sdc
        >>> import element_controller as ec
        >>> [container] = ec.get_active_identifiable_element_ids()
        >>> normal = cadwork.point_3d(0., 0., 1.)
        >>> added = sdc.add_export_solid_cut_at_relative_position(container, "Mid height", normal, 0.5)

    Returns:
        True if the cut was added. False if nothing was added: the element does not exist or is not
        an export solid or container, the normal has zero length, the relative position is not
        strictly between 0 and 1, the element has no extent along the normal, the name is empty or
        already used, the plane does not intersect the element's body (e.g. the empty corner of an
        L-shaped body), or the cut could not be saved.
    """

def get_wall_sections(element: ElementId) -> list[wall_section]:
    """Get the horizontal and vertical sections of a wall, floor or roof as planes.

    Reads the sections stored with a cover wall, floor or roof and returns each as a plane. Sections
    added with `add_wall_section_horizontal()`, `add_wall_section_vertical()` or
    `add_wall_section_horizontal_at_relative_position()` are included. An empty list means the
    element has no sections, the ID does not exist, or the element is not a wall, floor or roof; in
    the last two cases a reason is stored (see `clear_errors()`).

    Parameters:
        element: Element ID of a wall, floor or roof, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import shop_drawing_controller as sdc

        >>> [wall] = ec.get_active_identifiable_element_ids()
        >>> for section in sdc.get_wall_sections(wall):
        ...     print(section.get_type(), section.get_point(), section.get_normal())

    Returns:
        List of `wall_section` objects in global coordinates, ordered by the section reader; each
        gives its type (horizontal or vertical) with `get_type()`, a point on the plane with
        `get_point()` and the plane normal with `get_normal()`. Empty list if there are none or on
        failure.
    """

def get_export_solid_cuts(element: ElementId) -> list[export_solid_cut]:
    """Get the cuts of an export solid or container as planes.

    Reads the cuts stored with an export solid or container, such as those added with
    `add_export_solid_cut()`, and returns each as a plane. An empty list means the element has no
    cuts, the ID does not exist, or the element is not an export solid or container; in the last two
    cases a reason is stored (see `clear_errors()`).

    Parameters:
        element: Element ID of an export solid or container, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import shop_drawing_controller as sdc

        >>> [export_solid] = ec.get_active_identifiable_element_ids()
        >>> for cut in sdc.get_export_solid_cuts(export_solid):
        ...     print(cut.get_name(), cut.get_point(), cut.get_normal())

    Returns:
        List of `export_solid_cut` objects in the order they are stored, in global coordinates. Each
        gives its name with `get_name()`, a point on the plane with `get_point()`, the unit normal
        with `get_normal()` and the unit up vector with `get_up_vector()`. Empty list if there are
        none or on failure.
    """
