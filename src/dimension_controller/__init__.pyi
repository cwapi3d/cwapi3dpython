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

    Each point in dimension_points becomes a measuring point, sorted along xl. The dimension uses
    default display settings. The display is refreshed if automatic refresh is enabled. Further
    points can be added with add_segment.

    Parameters:
        xl: Direction of the dimension line (local X of the dimension plane).
        plane_normal: Normal of the dimension plane. The plane's local Y direction is derived as the
            cross product of xl and plane_normal.
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
        The element ID of the new dimension.
    """

def set_orientation(element_id_list: list[ElementId], view_dir: point_3d, view_dir_up: point_3d) -> None:
    """Orient dimension elements so that their texts read correctly from a given view.

    The dimension plane is not changed; its normal and local Y direction are flipped where needed
    to face the view. Elements in the list that are invalid IDs or not dimension elements are
    skipped; an empty list does nothing. The display is refreshed if automatic refresh is enabled.

    Parameters:
        element_id_list: List of dimension element IDs.
        view_dir: Viewing direction of the view the dimensions are read from.
        view_dir_up: Up direction of that view.
    """

def add_segment(element_id: ElementId, segment: point_3d) -> None:
    """Add a measuring point to a dimension element.

    The points are re-sorted and segments between consecutive points are updated. Does nothing if
    element_id is invalid or not a dimension.

    Parameters:
        element_id: Element ID of the dimension.
        segment: Point to add, in model coordinates (mm).
    """

def set_precision(element_id_list: list[ElementId], precision: UnsignedInt) -> None:
    """Set the number of decimal places shown in dimension texts.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        precision: Number of decimal places (non-negative integer).
    """

def set_text_size(element_id_list: list[ElementId], text_size: float) -> None:
    """Set the text size of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        text_size: Text size value.
    """

def set_line_thickness(element_id_list: list[ElementId], thickness: float) -> None:
    """Set the line thickness of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        thickness: Line thickness value.
    """

def set_total_dimension(element_id_list: list[ElementId], total: bool) -> None:
    """Show or hide the overall (total) dimension of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        total: True to show the overall dimension, False to hide it.
    """

def set_text_color(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Set the text color of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        color_id: Cadwork color ID from the color palette.
    """

def set_line_color(element_id_list: list[ElementId], color_id: ColorId) -> None:
    """Set the line color of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing.

    Parameters:
        element_id_list: List of dimension element IDs.
        color_id: Cadwork color ID from the color palette.
    """

def set_default_anchor_length(element_id_list: list[ElementId], length: float) -> None:
    """Set the default anchor length of dimension elements.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing. The anchors are updated immediately.

    Parameters:
        element_id_list: List of dimension element IDs.
        length: Anchor length in mm.
    """

def set_distance(element_id_list: list[ElementId], distance: point_3d) -> None:
    """Set the offset of the dimension line from the measured points.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing. The given point is projected onto the dimension's plane before being stored.

    Parameters:
        element_id_list: List of dimension element IDs.
        distance: Point on the dimension line, in model coordinates (mm); it is projected onto the
            dimension plane.
    """

def shift_distance_and_texts(element_id_list: list[ElementId], shifted: bool) -> None:
    """Set whether the distance and texts of dimension elements are shifted.

    Elements in the list that are invalid IDs or not dimension elements are skipped; an empty list
    does nothing. Sets the moved-text flag of the dimension labeling.

    Parameters:
        element_id_list: List of dimension element IDs.
        shifted: True to mark the texts as shifted, False otherwise.
    """

def get_dimension_points(element_id: ElementId) -> list[point_3d]:
    """Get the measuring points of a dimension element.

    For segments attached to an edge, only one point per edge is returned (its cross position).
    Returns an empty list if element_id is invalid or not a dimension.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        List of point_3d in segment order; empty list on failure.
    """

def get_default_anchor_length(element_id: ElementId) -> float:
    """Get the default anchor length of a dimension element.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        Anchor length; 0.0 if element_id is invalid or not a dimension.
    """

def get_distance(element_id: ElementId) -> point_3d:
    """Get the offset of the dimension line from the measured points.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        Point on the dimension line, in model coordinates (mm); a default point_3d (0, 0, 0) if
        element_id is invalid or not a dimension.
    """

def get_plane_normal(element_id: ElementId) -> point_3d:
    """Get the normal of the dimension plane.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        point_3d normal; default point_3d (0, 0, 0) if element_id is invalid or not a dimension.
    """

def get_plane_xl(element_id: ElementId) -> point_3d:
    """Get the direction of the dimension line (local X of the plane).

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        point_3d direction; default point_3d (0, 0, 0) if element_id is invalid or not a dimension.
    """

def get_segment_count(element_id: ElementId) -> int:
    """Get the number of segments of a dimension element.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        Number of segments; 0 if element_id is invalid or not a dimension.
    """

def get_segment_distance(element_id: ElementId, segment_index: int) -> float:
    """Get the distance from the measured point to the dimension line for a segment.

    Parameters:
        element_id: Element ID of the dimension.
        segment_index: Zero-based segment index (non-negative).

    Returns:
        Signed distance in mm, measured along the dimension's local Y direction; 0.0 if element_id is invalid, not a dimension, or segment_index is out of
        range.
    """

def get_segment_direction(element_id: ElementId, segment_index: int) -> point_3d:
    """Get the unit direction from the measured point toward the dimension line for a segment.

    Parameters:
        element_id: Element ID of the dimension.
        segment_index: Zero-based segment index (non-negative).

    Returns:
        Normalized point_3d; default point_3d (0, 0, 0) if element_id is invalid, not a dimension,
        or segment_index is out of range.
    """

def get_total_dimension(element_id: ElementId) -> bool:
    """Check whether the overall (total) dimension is shown.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        True if the overall dimension is shown; False otherwise, including if element_id is invalid
        or not a dimension.
    """

def get_dimension_base_format(element_id: ElementId) -> dimension_base_format:
    """Get the base format (distance, sum or both) of a dimension element.

    Parameters:
        element_id: Element ID of the dimension.

    Returns:
        A dimension_base_format value (distance_only, sum_only, distance_and_sum, sum_moved);
        dimension_base_format.none if element_id is invalid or not a dimension.
    """
