"""3D dimension annotations on the model.

Domain of dimension elements as first-class objects in the model:
their creation on a defined plane, the points they measure, their
formatting and orientation, and visualisation options such as
overall dimensions. Distinct from shop-drawing dimensions, which
are produced as part of 2D output.
"""

from cadwork.point_3d import point_3d
from cadwork.dimension_base_format import dimension_base_format
from cadwork.api_types import *

def create_dimension(
    xl: point_3d, plane_normal: point_3d, distance: point_3d, dimension_points: list[point_3d]
) -> ElementId:
    """Create a dimension element on a plane and return its element ID.

    A dimension is a 3D annotation element that shows the distances between measuring points along a
    dimension line. Each entry of dimension_points becomes a measuring point; the points are sorted
    along xl and the dimension gets the default display settings (change them afterwards with the
    `dimension_controller.set_*` functions). Right after creation the plane is oriented as if viewed
    against plane_normal, so the stored plane normal may be the reverse of the vector you passed;
    read it back with `dimension_controller.get_plane_normal()`. The display is refreshed if
    automatic refresh is enabled. Add further points with `dimension_controller.add_segment()`.

    Parameters:
        xl: Direction of the dimension line (local X of the dimension plane).
        plane_normal: Normal of the dimension plane. The plane's local Y direction is derived as the
            cross product of xl and plane_normal, so xl and plane_normal must not be parallel.
        distance: Point on the dimension line, in model coordinates (mm); it sets the line's offset
            from the measured points along the plane's local Y direction.
        dimension_points: Points to measure, in model coordinates (mm). An empty list creates a
            dimension without measuring points.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> # Create a list of dimension points
        >>> list_points = []
        >>> list_points.append(cadwork.point_3d(0., 0., 0.))
        >>> list_points.append(cadwork.point_3d(1000., 0., 0.))
        >>> list_points.append(cadwork.point_3d(2000., 500., 0.))
        >>> list_points.append(cadwork.point_3d(3000., 200., 0.))
        >>> list_points.append(cadwork.point_3d(4000., 360., 0.))
        >>> list_points.append(cadwork.point_3d(6000., 451., 0.))

        >>> # Create the dimension element
        >>> id_dimension = dc.create_dimension(
        >>>     cadwork.point_3d(1., 0., 0.),  # xl - dimension arrow direction
        >>>     cadwork.point_3d(0., 1., 0.),  # plane_normal
        >>>     cadwork.point_3d(0., 0., 500.),  # distance - offset from geometry
        >>>     list_points  # dimension_points
        >>> )

    Returns:
        The element ID of the new dimension element; 0 if the API is not available.
    """

def set_orientation(element_id_list: list[ElementId], view_dir: point_3d, view_dir_up: point_3d) -> None:
    """Orient dimension elements so that their texts read correctly from a given view.

    Use it after creating or moving dimensions so that the texts face the viewer of a given view.
    The dimension line positions are not moved; only the stored plane normal and local Y direction
    are flipped where needed: the normal is flipped so that it points against view_dir, and the
    local Y direction is flipped to match view_dir_up (the text-side sum label orientation is also
    adjusted). IDs that are invalid or not dimension elements are skipped; an empty list does
    nothing. The display is refreshed once at the end if automatic refresh is enabled.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        view_dir: Viewing direction of the view the dimensions are read from (pointing from the
            viewer into the model).
        view_dir_up: Up direction of that view.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        ... # read the dimension from the front (looking along +Y), Z up
        >>> dc.set_orientation([dim_id], cadwork.point_3d(0., 1., 0.), cadwork.point_3d(0., 0., 1.))
    """

def add_segment(element_id: ElementId, segment: point_3d) -> None:
    """Add a measuring point to a dimension element.

    The new point is added to the existing points and all points are re-sorted, so a new dimension
    measure appears between the neighbouring points. It adds a free point only; it does not attach
    to element geometry. Does nothing if element_id is invalid or not a dimension. The display is
    refreshed if automatic refresh is enabled. Read the points back with
    `dimension_controller.get_dimension_points()`.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.
        segment: Point to add, in model coordinates (mm).

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.add_segment(dim_id, cadwork.point_3d(1000., 0., 0.))
        >>> print(dc.get_segment_count(dim_id))
    """

def set_precision(element_id_list: list[ElementId], precision: UnsignedInt) -> None:
    """Set the number of decimal places shown in dimension texts.

    The value is stored in the display settings of each dimension and applies to all its texts. IDs
    that are invalid or not dimension elements are skipped; an empty list does nothing. The display
    is refreshed once at the end if automatic refresh is enabled.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        precision: Number of decimal places (non-negative integer), e.g. 0 for whole millimetres.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000.5, 0., 0.)],
        ... )
        >>> dc.set_precision([dim_id], 1)
    """

def set_text_size(element_id_list: list[ElementId], text_size: float) -> None:
    """Set the text size of dimension elements.

    The value is stored in the display settings of each dimension. IDs that are invalid or not
    dimension elements are skipped; an empty list does nothing. The display is refreshed once at the
    end if automatic refresh is enabled. New dimensions start with the default text size.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        text_size: Text size value, as in the dimension settings of cadwork 3D.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_text_size([dim_id], 100.)
    """

def set_line_thickness(element_id_list: list[ElementId], thickness: float) -> None:
    """Set the line thickness of dimension elements.

    The value is stored in each dimension and applies to its dimension and extension lines. IDs that
    are invalid or not dimension elements are skipped; an empty list does nothing. The display is
    refreshed once at the end if automatic refresh is enabled. Set the line color with
    `dimension_controller.set_line_color()`.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        thickness: Line thickness value.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_line_thickness([dim_id], 2.)
    """

def set_total_dimension(element_id_list: list[ElementId], total: bool) -> None:
    """Show or hide the overall (total) dimension of dimension elements.

    The overall dimension is one extra measure spanning from the first to the last measuring point.
    IDs that are invalid or not dimension elements are skipped; an empty list does nothing. The
    display is refreshed once at the end if automatic refresh is enabled. Read the state back with
    `dimension_controller.get_total_dimension()`.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        total: True to show the overall dimension, False to hide it.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_total_dimension([dim_id], True)
        >>> print(dc.get_total_dimension(dim_id))
    """

def set_text_color(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Set the text color of dimension elements.

    The color number is converted to the RGB value of the cadwork color palette and stored in each
    dimension. IDs that are invalid or not dimension elements are skipped; an empty list does
    nothing. The display is refreshed once at the end if automatic refresh is enabled. Use
    `dimension_controller.set_line_color()` for the lines.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        color_id: cadwork color number from the color palette, e.g. 3.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_text_color([dim_id], 3)
    """

def set_line_color(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Set the line color of dimension elements.

    The color number is converted to the RGB value of the cadwork color palette and stored in each
    dimension. IDs that are invalid or not dimension elements are skipped; an empty list does
    nothing. The display is refreshed once at the end if automatic refresh is enabled. Use
    `dimension_controller.set_text_color()` for the texts.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        color_id: cadwork color number from the color palette, e.g. 5.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_line_color([dim_id], 5)
    """

def set_default_anchor_length(element_id_list: list[ElementId], length: float) -> None:
    """Set the default anchor length of dimension elements.

    Anchors are the extension lines that connect each measuring point to the dimension line; this
    sets their default length. The anchors are recomputed immediately. IDs that are invalid or not
    dimension elements are skipped; an empty list does nothing. The display is refreshed once at the
    end if automatic refresh is enabled. Read the value back with
    `dimension_controller.get_default_anchor_length()`.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        length: Anchor length in model units (mm).

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_default_anchor_length([dim_id], 50.)
        >>> print(dc.get_default_anchor_length(dim_id))
    """

def set_distance(element_id_list: list[ElementId], distance: point_3d) -> None:
    """Set the offset of the dimension line from the measured points.

    The given point is projected onto the dimension's own plane before it is stored, so only its
    in-plane position matters. IDs that are invalid or not dimension elements are skipped; an empty
    list does nothing. The display is refreshed once at the end if automatic refresh is enabled.
    Read the value back with `dimension_controller.get_distance()`.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        distance: Point on the dimension line, in model coordinates (mm); it is projected onto the
            dimension plane.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_distance([dim_id], cadwork.point_3d(0., 300., 500.))
        >>> print(dc.get_distance(dim_id))
    """

def shift_distance_and_texts(element_id_list: list[ElementId], shifted: bool) -> None:
    """Mark the distance and texts of dimension elements as shifted or not shifted.

    Sets the moved-text flag of the dimension's labeling; there is no getter for it in this module.
    IDs that are invalid or not dimension elements are skipped; an empty list does nothing. The
    display is refreshed once at the end if automatic refresh is enabled. The function does not move
    any text itself; it only stores the flag.

    Parameters:
        element_id_list: List of dimension element IDs, e.g. returned by
            `dimension_controller.create_dimension()`.
        shifted: True to mark the texts as moved, False to clear the flag.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.shift_distance_and_texts([dim_id], True)
    """

def get_dimension_points(element_id: ElementId) -> list[point_3d]:
    """Get the measuring points of a dimension element.

    Returns one point per measuring point, in segment order (the sorted order along the dimension).
    For measuring points attached to an element edge, one point per edge is returned (the point on
    the dimension line side, not on the edge), so the list can be shorter than
    `dimension_controller.get_segment_count()`. Returns an empty list if element_id is invalid or
    not a dimension. Add points with `dimension_controller.add_segment()`.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> for point in dc.get_dimension_points(dim_id):
        ...     print(point.x, point.y, point.z)

    Returns:
        List of point_3d in model coordinates (mm), in segment order; empty list on failure.
    """

def get_default_anchor_length(element_id: ElementId) -> float:
    """Get the default anchor length of a dimension element.

    Anchors are the extension lines between the measuring points and the dimension line. Set the
    value with `dimension_controller.set_default_anchor_length()`. Returns 0.0 for invalid IDs and
    non-dimension elements, which is indistinguishable from an actual length of 0.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> print(dc.get_default_anchor_length(dim_id))

    Returns:
        Anchor length in mm; 0.0 if element_id is invalid or not a dimension.
    """

def get_distance(element_id: ElementId) -> point_3d:
    """Get the offset of the dimension line from the measured points.

    Returns the point on the dimension line that was given to
    `dimension_controller.create_dimension()` or `dimension_controller.set_distance()` (after
    projection onto the dimension plane for the latter). Returns a default point_3d (0, 0, 0) for
    invalid IDs and non-dimension elements, which is indistinguishable from a real point at the
    origin.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> line_point = dc.get_distance(dim_id)
        >>> print(line_point.x, line_point.y, line_point.z)

    Returns:
        Point on the dimension line, in model coordinates (mm); default point_3d (0, 0, 0) if
        element_id is invalid or not a dimension.
    """

def get_plane_normal(element_id: ElementId) -> point_3d:
    """Get the normal of the dimension plane.

    The normal may differ in sign from the one passed to `dimension_controller.create_dimension()`,
    because the plane is oriented towards the viewer on creation and by
    `dimension_controller.set_orientation()`. Returns a default point_3d (0, 0, 0) for invalid IDs
    and non-dimension elements.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> normal = dc.get_plane_normal(dim_id)
        >>> print(normal.x, normal.y, normal.z)

    Returns:
        point_3d normal of the dimension plane; default point_3d (0, 0, 0) if element_id is invalid
        or not a dimension.
    """

def get_plane_xl(element_id: ElementId) -> point_3d:
    """Get the direction of the dimension line (local X of the plane).

    This is the xl direction passed to `dimension_controller.create_dimension()`. Returns a default
    point_3d (0, 0, 0) for invalid IDs and non-dimension elements.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> xl = dc.get_plane_xl(dim_id)
        >>> print(xl.x, xl.y, xl.z)

    Returns:
        point_3d direction of the dimension line; default point_3d (0, 0, 0) if element_id is
        invalid or not a dimension.
    """

def get_segment_count(element_id: ElementId) -> int:
    """Get the number of segments of a dimension element.

    A segment is one stored measuring point together with its anchor and text position; use it as
    the upper bound for the segment_index of `dimension_controller.get_segment_distance()` and
    `dimension_controller.get_segment_direction()`. The count includes every stored point, so it can
    be larger than the length of `dimension_controller.get_dimension_points()`, which merges edge
    segments. Returns 0 for invalid IDs and non-dimension elements.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> for index in range(dc.get_segment_count(dim_id)):
        ...     print(index, dc.get_segment_distance(dim_id, index))

    Returns:
        Number of segments; 0 if element_id is invalid or not a dimension.
    """

def get_segment_distance(element_id: ElementId, segment_index: int) -> float:
    """Get the distance from the measured point to the dimension line for a segment.

    The distance is measured from the segment's measuring point to the dimension line along the
    plane's local Y direction and is signed, so it is negative for a point on the other side of the
    line. Valid indices are 0 to `dimension_controller.get_segment_count()` minus 1. Returns 0.0 for
    invalid IDs, non-dimension elements and indices at or above the segment count.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.
        segment_index: Zero-based segment index, in the range 0 to get_segment_count() - 1.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> if dc.get_segment_count(dim_id) > 0:
        ...     print(dc.get_segment_distance(dim_id, 0))

    Returns:
        Signed distance in mm; 0.0 if element_id is invalid, not a dimension, or segment_index is
        too large.
    """

def get_segment_direction(element_id: ElementId, segment_index: int) -> point_3d:
    """Get the unit direction from the measured point toward the dimension line for a segment.

    The vector points from the segment's measuring point to the matching point on the dimension line
    (the anchor direction) and has length 1. Valid indices are 0 to
    `dimension_controller.get_segment_count()` minus 1. Returns a default point_3d (0, 0, 0) for
    invalid IDs, non-dimension elements and indices at or above the segment count. Pair it with
    `dimension_controller.get_segment_distance()` to get the full offset vector.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.
        segment_index: Zero-based segment index, in the range 0 to get_segment_count() - 1.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> if dc.get_segment_count(dim_id) > 0:
        ...     direction = dc.get_segment_direction(dim_id, 0)
        ...     print(direction.x, direction.y, direction.z)

    Returns:
        Normalized point_3d; default point_3d (0, 0, 0) if element_id is invalid, not a dimension,
        or segment_index is too large.
    """

def get_total_dimension(element_id: ElementId) -> bool:
    """Check whether the overall (total) dimension is shown.

    Set the state with `dimension_controller.set_total_dimension()`. Returns False for invalid IDs
    and non-dimension elements, which is indistinguishable from a dimension that has the overall
    dimension hidden.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> dc.set_total_dimension([dim_id], True)
        >>> print(dc.get_total_dimension(dim_id))

    Returns:
        True if the overall dimension is shown; False otherwise, including if element_id is invalid
        or not a dimension.
    """

def get_dimension_base_format(element_id: ElementId) -> dimension_base_format:
    """Get the base format (distance, sum or both) of a dimension element.

    The base format says whether the dimension texts show the single distances, the running sum, or
    both; sum_moved is the sum variant with moved text. There is no setter in this module. Returns
    dimension_base_format.none for invalid IDs, non-dimension elements and unknown formats.

    Parameters:
        element_id: Element ID of a dimension, e.g. returned by
            `dimension_controller.create_dimension()`.

    Examples:
        >>> import cadwork
        >>> import dimension_controller as dc

        >>> dim_id = dc.create_dimension(
        ...     cadwork.point_3d(1., 0., 0.),
        ...     cadwork.point_3d(0., 0., 1.),
        ...     cadwork.point_3d(0., 0., 500.),
        ...     [cadwork.point_3d(0., 0., 0.), cadwork.point_3d(2000., 0., 0.)],
        ... )
        >>> base_format = dc.get_dimension_base_format(dim_id)
        >>> if base_format == cadwork.dimension_base_format.none:
        ...     print('no dimension')

    Returns:
        A dimension_base_format value (distance_only, sum_only, distance_and_sum, sum_moved);
        dimension_base_format.none if element_id is invalid or not a dimension.
    """
