"""Spatial and metric properties of elements.

Concerned with the pure geometry of an element: its dimensions,
volumes, areas, weights, local coordinate system (axes and reference
points), facets and edges, and rigid transformations applied to the
element's own frame (axis flips and rotations). Use this module to
*measure* or *reorient* an element's geometry; use element_controller
to create or destroy it.
"""

from cadwork.api_types import ElementId, UnsignedInt
from cadwork.facet_list import facet_list
from cadwork.point_3d import point_3d
from cadwork.division_zone_direction import division_zone_direction
from enum import IntEnum, unique

@unique
class element_collision_type(IntEnum):
    """How the geometry of two elements relates, as returned by get_element_collision_type.

    Examples:
        >>> geometry_controller.element_collision_type.touching
        touching
    """

    unknown = 0
    """Invalid element ID, or an axis or line element."""
    none = 1
    """No collision."""
    unclassified = 2
    """The geometry kernel could not classify the relation."""
    contained = 3
    """One body is fully inside the other without touching its boundary."""
    contained_and_touching = 4
    """One body is inside the other and touches its boundary."""
    touching = 5
    """The bodies share a boundary but no volume."""
    coincident = 6
    """The bodies coincide."""
    interlocking = 7
    """The bodies interpenetrate."""

    def __int__(self) -> int: ...

def rotate_height_axis_90(element_id_list: list[ElementId]) -> None:
    """Rotate the local height axis of the elements by 90 degrees about the length axis.

    Turns the cross-section orientation (a quarter turn) around the element's length axis through
    P1, so the height and width axes swap or flip while the length axis and P1 stay in place.
    Elements without a local axis system, auxiliary elements, axis elements and VBA elements are
    skipped. The elements are marked as modified and the display is refreshed if auto-refresh is on.
    For beams with blank oversize (cross corrections), the values follow the rotated axes; end types
    are adjusted. An empty list does nothing. Use
    `geometry_controller.rotate_height_axis_2_points()` to align the height axis with an arbitrary
    direction.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.rotate_height_axis_90(element_ids)
    """

def rotate_height_axis_180(element_id_list: list[ElementId]) -> None:
    """Rotate the local height axis of the elements by 180 degrees about the length axis.

    Turns the cross-section orientation (a half turn) around the element's length axis through P1,
    so the height and width axes swap or flip while the length axis and P1 stay in place. Elements
    without a local axis system, auxiliary elements, axis elements and VBA elements are skipped. The
    elements are marked as modified and the display is refreshed if auto-refresh is on. For beams
    with blank oversize (cross corrections), the values follow the rotated axes; end types are
    adjusted. An empty list does nothing. Use `geometry_controller.rotate_height_axis_2_points()` to
    align the height axis with an arbitrary direction.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.rotate_height_axis_180(element_ids)
    """

def set_over_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the width oversize (list oversize) of the elements.

    Stores an extra width allowance (local y axis) on each element for list purposes. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_over_width()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New width oversize, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_over_width(element_ids, 20.0)
        >>> print([gc.get_over_width(e) for e in element_ids])
    """

def set_over_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the height oversize (list oversize) of the elements.

    Stores an extra height allowance (local z axis) on each element for list purposes. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_over_height()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New height oversize, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_over_height(element_ids, 20.0)
        >>> print([gc.get_over_height(e) for e in element_ids])
    """

def set_over_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the length oversize (list oversize) of the elements.

    Stores an extra length allowance (local x axis) on each element for list purposes. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_over_length()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New length oversize, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_over_length(element_ids, 20.0)
        >>> print([gc.get_over_length(e) for e in element_ids])
    """

def set_rounding_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the width rounding value of the elements.

    Stores the rounding value for the width dimension (local y axis) on each element. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_rounding_width()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New width rounding value, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_rounding_width(element_ids, 5.0)
        >>> print([gc.get_rounding_width(e) for e in element_ids])
    """

def set_rounding_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the height rounding value of the elements.

    Stores the rounding value for the height dimension (local z axis) on each element. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_rounding_height()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New height rounding value, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_rounding_height(element_ids, 5.0)
        >>> print([gc.get_rounding_height(e) for e in element_ids])
    """

def set_rounding_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the length rounding value of the elements.

    Stores the rounding value for the length dimension (local x axis) on each element. The 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with `geometry_controller.get_rounding_length()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New length rounding value, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_rounding_length(element_ids, 5.0)
        >>> print([gc.get_rounding_length(e) for e in element_ids])
    """

def set_cross_correction_negative_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative width cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    negative side of the local y axis (width direction). The value is stored on each element; the 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_negative_width()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New negative width cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_negative_width(element_ids, 10.0)
        >>> print([gc.get_cross_correction_negative_width(e) for e in element_ids])
    """

def set_cross_correction_positive_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive width cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    positive side of the local y axis (width direction). The value is stored on each element; the 3D
    geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_positive_width()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New positive width cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_positive_width(element_ids, 10.0)
        >>> print([gc.get_cross_correction_positive_width(e) for e in element_ids])
    """

def set_cross_correction_negative_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative height cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    negative side of the local z axis (height direction). The value is stored on each element; the
    3D geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_negative_height()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New negative height cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_negative_height(element_ids, 10.0)
        >>> print([gc.get_cross_correction_negative_height(e) for e in element_ids])
    """

def set_cross_correction_positive_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive height cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    positive side of the local z axis (height direction). The value is stored on each element; the
    3D geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_positive_height()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New positive height cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_positive_height(element_ids, 10.0)
        >>> print([gc.get_cross_correction_positive_height(e) for e in element_ids])
    """

def set_cross_correction_negative_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative length cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    negative side of the local x axis (length direction). The value is stored on each element; the
    3D geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_negative_length()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New negative length cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_negative_length(element_ids, 10.0)
        >>> print([gc.get_cross_correction_negative_length(e) for e in element_ids])
    """

def set_cross_correction_positive_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive length cross correction (blank oversize) of the elements.

    The cross correction is extra material of the raw blank beyond the finished element, here on the
    positive side of the local x axis (length direction). The value is stored on each element; the
    3D geometry is not changed and the display is not refreshed. Invalid IDs and elements without
    geometry data are skipped. Read it back with
    `geometry_controller.get_cross_correction_positive_length()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        value: New positive length cross correction, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_cross_correction_positive_length(element_ids, 10.0)
        >>> print([gc.get_cross_correction_positive_length(e) for e in element_ids])
    """

def apply_global_scale(element_id_list: list[ElementId], scale: float, origin: point_3d) -> None:
    """Scale the elements around an origin point.

    Scales each element by the factor relative to the given center point; with a factor of 1.0
    nothing changes. Elements are marked as modified and the display is refreshed if auto-refresh is
    on. Invalid IDs are skipped; there is no element type restriction.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        scale: Scale factor (1.0 keeps the size).
        origin: Center of scaling, as `cadwork.point_3d` in model coordinates (mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> origin = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> gc.apply_global_scale(element_ids, 0.5, origin)
    """

def auto_regenerate_axes(element_id_list: list[ElementId]) -> None:
    """Regenerate the local axis systems of the elements automatically.

    Recomputes each element's local axes (length, width, height) from its current body, following
    cadwork's standard rules for the element type. Machine data of the elements is deleted first,
    which may ask the user for confirmation; if that fails or is declined, no axis is regenerated. A
    progress dialog is shown while the script waits, and the user can cancel it, which leaves the
    remaining elements untouched. Elements are marked as modified and the display is refreshed if
    auto-refresh is on. Invalid IDs are skipped. Use
    `geometry_controller.auto_regenerate_axes_silently()` to avoid the dialogs and the machine data
    deletion.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.auto_regenerate_axes(element_ids)
    """

def rotate_length_axis_90(element_id_list: list[ElementId]) -> None:
    """Rotate the local length axis of the elements by 90 degrees.

    Turns the element (a quarter turn) around its height axis through P1, so the length axis swings
    within the length/width plane; for surface elements the turn is around the width axis instead.
    Elements without a local axis system and auxiliary elements are skipped. The elements are marked
    as modified and the display is refreshed if auto-refresh is on. An empty list does nothing. Use
    `geometry_controller.rotate_length_axis_2_points()` to align the length axis with an arbitrary
    direction.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.rotate_length_axis_90(element_ids)
    """

def rotate_length_axis_180(element_id_list: list[ElementId]) -> None:
    """Rotate the local length axis of the elements by 180 degrees.

    Turns the element (a half turn) around its height axis through P1, so the length axis swings
    within the length/width plane; for surface elements the turn is around the width axis instead.
    Elements without a local axis system and auxiliary elements are skipped. The elements are marked
    as modified and the display is refreshed if auto-refresh is on. An empty list does nothing. Use
    `geometry_controller.rotate_length_axis_2_points()` to align the length axis with an arbitrary
    direction.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.rotate_length_axis_180(element_ids)
    """

def invert_model(element_id_list: list[ElementId]) -> None:
    """Reverse the orientation of the element bodies.

    Reverses the solid body of each element (face orientation is flipped). Elements are marked as
    modified and the display is refreshed if auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.invert_model(element_ids)
    """

def set_width_real(element_id_list: list[ElementId], width: float) -> None:
    """Resize the width of the elements to a new value.

    Rebuilds each element with the new width (local y axis), keeping the other two dimensions and
    the local axes. By default the size change is split evenly between both sides of the width
    direction; if a reference element is active in cadwork, the change may instead be applied from
    the side nearest to it. Cover elements get their distribution area recalculated. Marks the
    elements as modified and refreshes the display if auto-refresh is on. Invalid IDs and elements
    without geometry data are skipped. Read the current value with
    `geometry_controller.get_width()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        width: New width, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_width_real(element_ids, 200.0)
        >>> print([gc.get_width(e) for e in element_ids])
    """

def set_height_real(element_id_list: list[ElementId], height: float) -> None:
    """Resize the height of the elements to a new value.

    Rebuilds each element with the new height (local z axis), keeping the other two dimensions and
    the local axes. By default the size change is split evenly between both sides of the height
    direction; if a reference element is active in cadwork, the change may instead be applied from
    the side nearest to it. Cover elements get their distribution area recalculated. Marks the
    elements as modified and refreshes the display if auto-refresh is on. Invalid IDs and elements
    without geometry data are skipped. Read the current value with
    `geometry_controller.get_height()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        height: New height, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_height_real(element_ids, 200.0)
        >>> print([gc.get_height(e) for e in element_ids])
    """

def set_length_real(element_id_list: list[ElementId], length: float) -> None:
    """Resize the length of the elements to a new value.

    Rebuilds each element with the new length (local x axis), keeping the other two dimensions and
    the local axes. By default the size change is split evenly between both sides of the length
    direction; if a reference element is active in cadwork, the change may instead be applied from
    the side nearest to it. Cover elements get their distribution area recalculated. Marks the
    elements as modified and refreshes the display if auto-refresh is on. Invalid IDs and elements
    without geometry data are skipped. Read the current value with
    `geometry_controller.get_length()`.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        length: New length, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_length_real(element_ids, 200.0)
        >>> print([gc.get_length(e) for e in element_ids])
    """

def rotate_height_axis_2_points(element_id_list: list[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Align the local height axis (local z) of the elements with the direction point1 to point2.

    The new height axis direction is point2 minus point1; only the direction matters, the positions
    themselves are not used. The local x axis is recomputed from the previous one so that it stays
    perpendicular to the new direction. Elements without a local axis system and auxiliary elements
    are skipped. Marks the elements as modified and refreshes the display if auto-refresh is on. An
    empty list does nothing.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        point1: Start point of the direction vector, in model coordinates (mm).
        point2: End point of the direction vector, in model coordinates (mm). Must differ from
            point1.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> start = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> end = cadwork.point_3d(0.0, 0.0, 1000.0)
        >>> gc.rotate_height_axis_2_points(element_ids, start, end)
    """

def clear_errors() -> None:
    """Clear the stored error messages of the geometry controller.

    Empties the geometry controller's stored error messages so that old ones are not reported later.
    Does nothing else.

    Examples:
        >>> import geometry_controller as gc

        >>> gc.clear_errors()
    """

def set_drilling_tolerance(element_id_list: list[ElementId], tolerance: float) -> None:
    """Set the additional drilling tolerance of bolt elements.

    Stores the extra drilling clearance on each bolt element. Only bolt elements are changed; all
    other elements and invalid IDs are skipped. Read it back with
    `geometry_controller.get_drilling_tolerance()`.

    Parameters:
        element_id_list: List of element IDs of bolts, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        tolerance: Additional drilling tolerance, in model units (mm).

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> bolt_ids = ec.get_active_identifiable_element_ids()
        >>> gc.set_drilling_tolerance(bolt_ids, 1.0)
        >>> print([gc.get_drilling_tolerance(b) for b in bolt_ids])
    """

def auto_regenerate_axes_silently(element_id_list: list[ElementId]) -> None:
    """Regenerate the local axis systems of the elements without a dialog.

    Same regeneration as `geometry_controller.auto_regenerate_axes()`, but with no progress dialog
    or user query, so it suits unattended scripts. Machine data of the elements is not deleted. The
    display is refreshed if auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> gc.auto_regenerate_axes_silently(element_ids)
    """

def rotate_length_axis_2_points(element_id_list: list[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Align the local length axis (local x) of the elements with the direction point1 to point2.

    The new length axis direction is point2 minus point1; only the direction matters, the positions
    themselves are not used. The local z axis is recomputed from the previous one so that it stays
    perpendicular to the new direction. Elements without a local axis system and auxiliary elements
    are skipped. Marks the elements as modified and refreshes the display if auto-refresh is on. An
    empty list does nothing.

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.
        point1: Start point of the direction vector, in model coordinates (mm).
        point2: End point of the direction vector, in model coordinates (mm). Must differ from
            point1.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> start = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> end = cadwork.point_3d(0.0, 0.0, 1000.0)
        >>> gc.rotate_length_axis_2_points(element_ids, start, end)
    """

def get_width(element_id: ElementId) -> float:
    """Get the width of an element.

    The width is the element's extent along its local y axis, in model units (mm). Together with
    `geometry_controller.get_height()` and `geometry_controller.get_length()` it gives the element's
    dimensions.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_width(element_id))

    Returns:
        The width in model units (mm); 0.0 if the element ID is invalid.
    """

def get_height(element_id: ElementId) -> float:
    """Get the height of an element.

    The height is the element's extent along its local z axis, in model units (mm). Together with
    `geometry_controller.get_width()` and `geometry_controller.get_length()` it gives the element's
    dimensions.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_height(element_id))

    Returns:
        The height in model units (mm); 0.0 if the element ID is invalid.
    """

def get_length(element_id: ElementId) -> float:
    """Get the length of an element.

    The length is the element's extent along its local x axis, in model units (mm). Together with
    `geometry_controller.get_width()` and `geometry_controller.get_height()` it gives the element's
    dimensions.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_length(element_id))

    Returns:
        The length in model units (mm); 0.0 if the element ID is invalid.
    """

def get_p1(element_id: ElementId) -> point_3d:
    """Get the start point (P1) of an element.

    P1 is the origin of the element's local axis system and the start of its length axis. For line
    elements it is the start of the first body edge; for all other elements it is the stored
    reference point P1. See also `geometry_controller.get_p2()` and `geometry_controller.get_p3()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     p1 = gc.get_p1(element_id)
        ...     print(element_id, p1.x, p1.y, p1.z)

    Returns:
        A `point_3d` in model coordinates (mm); a default `point_3d` (0, 0, 0) if the element ID is
        invalid or a line element has no edges.
    """

def get_p2(element_id: ElementId) -> point_3d:
    """Get the end point (P2) of an element.

    P2 is the end of the element's length axis, so P1 to P2 runs along the length axis. For line
    elements it is the end of the first body edge; for all other elements it is the stored reference
    point P2.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     p2 = gc.get_p2(element_id)
        ...     print(element_id, p2.x, p2.y, p2.z)

    Returns:
        A `point_3d` in model coordinates (mm); a default `point_3d` (0, 0, 0) if the element ID is
        invalid or a line element has no edges.
    """

def get_p3(element_id: ElementId) -> point_3d:
    """Get the third reference point (P3) of an element.

    P3 defines the direction of the height axis (local z) as seen from P1. Together with P1 and P2
    it fixes the element's local orientation. Line elements get no special handling here.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     p3 = gc.get_p3(element_id)
        ...     print(element_id, p3.x, p3.y, p3.z)

    Returns:
        A `point_3d` in model coordinates (mm); a default `point_3d` (0, 0, 0) if the element ID is
        invalid.
    """

def get_start_height_cut_angle(element_id: ElementId) -> float:
    """Get the start height cut angle of an element.

    Returns the cut angle at the start of the element in height direction. An end can carry several
    cut angles; the first non-zero one is returned. Square (uncut) ends return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_start_height_cut_angle(element_id))

    Returns:
        The start height cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_start_width_cut_angle(element_id: ElementId) -> float:
    """Get the start width cut angle of an element.

    Returns the cut angle at the start of the element in width direction. An end can carry several
    cut angles; the first non-zero one is returned. Square (uncut) ends return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_start_width_cut_angle(element_id))

    Returns:
        The start width cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_end_height_cut_angle(element_id: ElementId) -> float:
    """Get the end height cut angle of an element.

    Returns the cut angle at the end of the element in height direction. An end can carry several
    cut angles; the first non-zero one is returned. Square (uncut) ends return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_end_height_cut_angle(element_id))

    Returns:
        The end height cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_end_width_cut_angle(element_id: ElementId) -> float:
    """Get the end width cut angle of an element.

    Returns the cut angle at the end of the element in width direction. An end can carry several cut
    angles; the first non-zero one is returned. Square (uncut) ends return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_end_width_cut_angle(element_id))

    Returns:
        The end width cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_over_width(element_id: ElementId) -> float:
    """Get the width oversize (list oversize) of an element.

    Returns the width oversize (local y axis) stored on the element, as set with
    `geometry_controller.set_over_width()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_over_width(element_id))

    Returns:
        The width oversize in model units (mm); 0.0 if the element ID is invalid.
    """

def get_over_height(element_id: ElementId) -> float:
    """Get the height oversize (list oversize) of an element.

    Returns the height oversize (local z axis) stored on the element, as set with
    `geometry_controller.set_over_height()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_over_height(element_id))

    Returns:
        The height oversize in model units (mm); 0.0 if the element ID is invalid.
    """

def get_over_length(element_id: ElementId) -> float:
    """Get the length oversize (list oversize) of an element.

    Returns the length oversize (local x axis) stored on the element, as set with
    `geometry_controller.set_over_length()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_over_length(element_id))

    Returns:
        The length oversize in model units (mm); 0.0 if the element ID is invalid.
    """

def get_rounding_width(element_id: ElementId) -> float:
    """Get the width rounding value of an element.

    Returns the rounding value for the width dimension (local y axis) stored on the element, as set
    with `geometry_controller.set_rounding_width()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_rounding_width(element_id))

    Returns:
        The width rounding value in model units (mm); 0.0 if the element ID is invalid.
    """

def get_rounding_height(element_id: ElementId) -> float:
    """Get the height rounding value of an element.

    Returns the rounding value for the height dimension (local z axis) stored on the element, as set
    with `geometry_controller.set_rounding_height()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_rounding_height(element_id))

    Returns:
        The height rounding value in model units (mm); 0.0 if the element ID is invalid.
    """

def get_rounding_length(element_id: ElementId) -> float:
    """Get the length rounding value of an element.

    Returns the rounding value for the length dimension (local x axis) stored on the element, as set
    with `geometry_controller.set_rounding_length()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_rounding_length(element_id))

    Returns:
        The length rounding value in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_width(element_id: ElementId) -> float:
    """Get the negative width cross correction (blank oversize) of an element.

    Returns the blank oversize on the negative side of the local y axis (width direction), as set
    with `geometry_controller.set_cross_correction_negative_width()`. Elements without geometry data
    return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_negative_width(element_id))

    Returns:
        The negative width cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_width(element_id: ElementId) -> float:
    """Get the positive width cross correction (blank oversize) of an element.

    Returns the blank oversize on the positive side of the local y axis (width direction), as set
    with `geometry_controller.set_cross_correction_positive_width()`. Elements without geometry data
    return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_positive_width(element_id))

    Returns:
        The positive width cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_height(element_id: ElementId) -> float:
    """Get the negative height cross correction (blank oversize) of an element.

    Returns the blank oversize on the negative side of the local z axis (height direction), as set
    with `geometry_controller.set_cross_correction_negative_height()`. Elements without geometry
    data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_negative_height(element_id))

    Returns:
        The negative height cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_height(element_id: ElementId) -> float:
    """Get the positive height cross correction (blank oversize) of an element.

    Returns the blank oversize on the positive side of the local z axis (height direction), as set
    with `geometry_controller.set_cross_correction_positive_height()`. Elements without geometry
    data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_positive_height(element_id))

    Returns:
        The positive height cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_length(element_id: ElementId) -> float:
    """Get the negative length cross correction (blank oversize) of an element.

    Returns the blank oversize on the negative side of the local x axis (length direction), as set
    with `geometry_controller.set_cross_correction_negative_length()`. Elements without geometry
    data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_negative_length(element_id))

    Returns:
        The negative length cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_length(element_id: ElementId) -> float:
    """Get the positive length cross correction (blank oversize) of an element.

    Returns the blank oversize on the positive side of the local x axis (length direction), as set
    with `geometry_controller.set_cross_correction_positive_length()`. Elements without geometry
    data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     print(element_id, gc.get_cross_correction_positive_length(element_id))

    Returns:
        The positive length cross correction in model units (mm); 0.0 if the element ID is invalid.
    """

def get_weight(element_id: ElementId) -> float:
    """Get the real weight of an element in kilograms.

    Returns the weight of the element as modelled. For the weight of the raw part, see
    `geometry_controller.get_list_weight()`. Elements without geometry data return 0.0.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc

        >>> total = 0.0
        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     total += gc.get_weight(element_id)
        >>> print(total, 'kg')

    Returns:
        Weight in kg; 0.0 if the element ID is invalid.
    """

def get_list_weight(element_id: ElementId) -> float:
    """Get the weight of the raw part of an element in kg.

    Weight of the raw part as used in element lists and production data. Compare with
    `geometry_controller.get_weight()` (element weight) and `geometry_controller.get_weight_real()`.
    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     weight = gc.get_list_weight(element_id)
        ...     print(element_id, weight)

    Returns:
        Raw part weight in kg, or 0.0 if the element ID is invalid.
    """

def get_volume(element_id: ElementId) -> float:
    """Get the rough volume of an element in mm3.

    Volume of the element body as modelled. Negative geometry such as end-types, drillings of
    connectors, openings and installation (MEP) bodies is not subtracted; use
    `geometry_controller.get_actual_physical_volume()` for the net volume. Returns 0.0 for an
    invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     volume = gc.get_volume(element_id)
        ...     print(element_id, volume)

    Returns:
        Rough volume in mm3, or 0.0 if the element ID is invalid.
    """

def get_list_volume(element_id: ElementId) -> float:
    """Get the list volume of an element in mm3.

    Volume as used in element lists. Element types that do not provide a list volume return 0.0, so
    use `geometry_controller.get_volume()` when you need the geometric volume. Returns 0.0 for an
    invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     volume = gc.get_list_volume(element_id)
        ...     print(element_id, volume)

    Returns:
        List volume in mm3, or 0.0 if the element ID is invalid or the element has no list volume.
    """

def get_xl(element_id: ElementId) -> point_3d:
    """Get the length axis direction (XL) of an element.

    XL is the local x axis along the length of the element, normally pointing from
    `geometry_controller.get_p1()` towards `geometry_controller.get_p2()`. For a line element made
    of one straight edge it is the start direction of that edge. The other local axes are
    `geometry_controller.get_yl()` and `geometry_controller.get_zl()`. Returns (0, 0, 0) for an
    invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     xl = gc.get_xl(element_id)
        ...     print(element_id, xl)

    Returns:
        XL direction vector in global coordinates, or (0, 0, 0) if the element ID is invalid.
    """

def get_yl(element_id: ElementId) -> point_3d:
    """Get the width axis direction (YL) of an element.

    YL is the local y axis along the width of the element. Together with
    `geometry_controller.get_xl()` and `geometry_controller.get_zl()` it forms the local coordinate
    system of the element. Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     yl = gc.get_yl(element_id)
        ...     print(element_id, yl)

    Returns:
        YL direction vector in global coordinates, or (0, 0, 0) if the element ID is invalid.
    """

def get_zl(element_id: ElementId) -> point_3d:
    """Get the height axis direction (ZL) of an element.

    ZL is the local z axis along the height (thickness for panels) of the element, normally pointing
    from `geometry_controller.get_p1()` towards `geometry_controller.get_p3()`. Together with
    `geometry_controller.get_xl()` and `geometry_controller.get_yl()` it forms the local coordinate
    system. Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     zl = gc.get_zl(element_id)
        ...     print(element_id, zl)

    Returns:
        ZL direction vector in global coordinates, or (0, 0, 0) if the element ID is invalid.
    """

def get_center_of_gravity(element_id: ElementId) -> point_3d:
    """Get the center of gravity of an element.

    Center of gravity of the element in global coordinates (model units, mm). For several elements
    at once use `geometry_controller.get_center_of_gravity_for_list()`. Returns (0, 0, 0) for an
    invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     cog = gc.get_center_of_gravity(element_id)
        ...     print(element_id, cog)

    Returns:
        Center of gravity as point_3d in mm, or (0, 0, 0) if the element ID is invalid.
    """

def get_reference_side(element_id: ElementId) -> int:
    """Get the reference side number of an element.

    The reference side is the side of the element used as reference for machining and listing. 1 is
    the negative height side (-ZL), 2 the positive width side (+YL), 3 the positive height side
    (+ZL) and 4 the negative width side (-YL). Other values (such as -1 or 5) mean that the default
    side is used: +YL, or +ZL for panels. Faces on the reference side are used by
    `geometry_controller.get_element_facets()` and
    `geometry_controller.get_element_reference_face_area()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     side = gc.get_reference_side(element_id)
        ...     print(element_id, side)

    Returns:
        Reference side number as described above, or 0 if the element ID is invalid.
    """

def get_element_vertices(element_id: ElementId) -> list[point_3d]:
    """Get all vertices of an element body.

    Returns every vertex of the element's solid body in global coordinates (mm). The order is
    determined by the geometry kernel. For the vertices of single faces use
    `geometry_controller.get_element_facets()`. Returns an empty list for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     vertices = gc.get_element_vertices(element_id)
        ...     print(element_id, len(vertices), 'vertices')

    Returns:
        List of point_3d vertex positions in mm, or an empty list if the element ID is invalid.
    """

def get_element_facets(element_id: ElementId) -> facet_list:
    """Get all facets of an element as a facet_list.

    A facet is one face of the element body. The returned facet_list holds, per facet, its vertices,
    outer polygon, inner polygons (holes) and, for planar facets, the normal vector and distance to
    the origin. Facets that lie on the reference side of the element (see
    `geometry_controller.get_reference_side()`) are also reachable through the reference-face
    methods of the facet_list. The facet index is the one `geometry_controller.stretch_facet()`
    expects. Returns an empty facet_list for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     facets = gc.get_element_facets(element_id)
        ...     print(element_id, len(facets), 'facets')

    Returns:
        facet_list with one entry per facet in kernel order, empty if the element ID is invalid.
    """

def get_list_width(element_id: ElementId) -> float:
    """Get the list width of an element in mm.

    Width as used in element lists and production data: the modelled width
    (`geometry_controller.get_width()`) plus the list over-width of the element, rounded to the
    rounding value of the element if one is set. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     width = gc.get_list_width(element_id)
        ...     print(element_id, width)

    Returns:
        List width in mm, or 0.0 if the element ID is invalid.
    """

def get_list_height(element_id: ElementId) -> float:
    """Get the list height of an element in mm.

    Height as used in element lists and production data: the modelled height
    (`geometry_controller.get_height()`) plus the list over-height of the element, rounded to the
    rounding value of the element if one is set. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     height = gc.get_list_height(element_id)
        ...     print(element_id, height)

    Returns:
        List height in mm, or 0.0 if the element ID is invalid.
    """

def get_list_length(element_id: ElementId) -> float:
    """Get the list length of an element in mm.

    Length as used in element lists and production data: the full length including end-types
    (`geometry_controller.get_length_including_end_types()`) plus the list over-length, rounded to
    the rounding value of the element if one is set. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     length = gc.get_list_length(element_id)
        ...     print(element_id, length)

    Returns:
        List length in mm, or 0.0 if the element ID is invalid.
    """

def get_minimum_distance_between_elements(first_id: ElementId, second_id: ElementId) -> float:
    """Get the minimum distance between the bodies of two elements.

    Measures the shortest distance between the solid bodies of the two elements in mm. If either
    element ID is invalid, an error is written to the log and infinity is returned, so check the
    result with `math.isinf()` before using it. To classify how two bodies relate (touching,
    overlapping, ...) use `geometry_controller.get_element_collision_type()`.

    Parameters:
        first_id: ID of the first element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        second_id: ID of the second element.

    Examples:
        >>> import math
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     first, second = element_ids[0], element_ids[1]
        ...     distance = gc.get_minimum_distance_between_elements(first, second)
        ...     if not math.isinf(distance):
        ...         print('Distance:', distance, 'mm')

    Returns:
        Minimum distance in mm, or infinity (`float('inf')`) if either element ID is invalid.
    """

def get_total_area_of_all_faces(element_id: ElementId) -> float:
    """Get the total surface area of an element in mm2.

    Sums the area of every face of the element body (all sides, including curved faces). Returns 0.0
    for an invalid element ID. For the reference side only use
    `geometry_controller.get_element_reference_face_area()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     area = gc.get_total_area_of_all_faces(element_id)
        ...     print(element_id, area)

    Returns:
        Sum of all face areas in mm2, or 0.0 if the element ID is invalid.
    """

def get_area_of_front_face(element_id: ElementId) -> float:
    """Get the area of the front faces of an element in mm2.

    Sums the area of all faces that the element flags as front face. Returns 0.0 if no face is
    flagged or the element ID is invalid.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     area = gc.get_area_of_front_face(element_id)
        ...     print(element_id, area)

    Returns:
        Front face area in mm2, or 0.0 if the element ID is invalid or no face is flagged.
    """

def get_door_surface(element_id_list: list[ElementId]) -> float:
    """Get the total door opening surface of the given elements in mm2.

    Looks for opening variants among the given elements and adds up width times height of every
    distinct door opening variant found. Elements sharing one variant are counted once, not once per
    element. Invalid IDs are skipped. An empty list or no door opening gives 0.0. The counterpart
    for the other opening type is `geometry_controller.get_window_surface()`.

    Parameters:
        element_id_list: List of element IDs to search for openings, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> area = gc.get_door_surface(element_ids)
        >>> print('Door surface:', area, 'mm2')

    Returns:
        Summed opening area in mm2, or 0.0 if there is none.
    """

def get_window_surface(element_id_list: list[ElementId]) -> float:
    """Get the total window opening surface of the given elements in mm2.

    Looks for opening variants among the given elements and adds up width times height of every
    distinct window opening variant found. Elements sharing one variant are counted once, not once
    per element. Invalid IDs are skipped. An empty list or no window opening gives 0.0. The
    counterpart for the other opening type is `geometry_controller.get_door_surface()`.

    Parameters:
        element_id_list: List of element IDs to search for openings, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> area = gc.get_window_surface(element_ids)
        >>> print('Window surface:', area, 'mm2')

    Returns:
        Summed opening area in mm2, or 0.0 if there is none.
    """

def get_local_x() -> point_3d:
    """Get the X' axis of the rotated coordinate system.

    Returns the X' axis direction of the user-defined (turned) coordinate system of the current
    model, in global coordinates. It does not belong to any element. The three axes are read with
    `geometry_controller.get_local_x()`, `geometry_controller.get_local_y()` and
    `geometry_controller.get_local_z()`.

    Examples:
        >>> import geometry_controller as gc

        >>> x_axis = gc.get_local_x()
        >>> y_axis = gc.get_local_y()
        >>> z_axis = gc.get_local_z()
        >>> print(x_axis, y_axis, z_axis)

    Returns:
        X' direction vector as point_3d.
    """

def get_local_z() -> point_3d:
    """Get the Z' axis of the rotated coordinate system.

    Returns the Z' axis direction of the user-defined (turned) coordinate system of the current
    model, in global coordinates. It does not belong to any element. The three axes are read with
    `geometry_controller.get_local_x()`, `geometry_controller.get_local_y()` and
    `geometry_controller.get_local_z()`.

    Examples:
        >>> import geometry_controller as gc

        >>> x_axis = gc.get_local_x()
        >>> y_axis = gc.get_local_y()
        >>> z_axis = gc.get_local_z()
        >>> print(x_axis, y_axis, z_axis)

    Returns:
        Z' direction vector as point_3d.
    """

def get_local_y() -> point_3d:
    """Get the Y' axis of the rotated coordinate system.

    Returns the Y' axis direction of the user-defined (turned) coordinate system of the current
    model, in global coordinates. It does not belong to any element. The three axes are read with
    `geometry_controller.get_local_x()`, `geometry_controller.get_local_y()` and
    `geometry_controller.get_local_z()`.

    Examples:
        >>> import geometry_controller as gc

        >>> x_axis = gc.get_local_x()
        >>> y_axis = gc.get_local_y()
        >>> z_axis = gc.get_local_z()
        >>> print(x_axis, y_axis, z_axis)

    Returns:
        Y' direction vector as point_3d.
    """

def get_drilling_tolerance(element_id: ElementId) -> float:
    """Get the additional drilling tolerance of a bolt element in mm.

    Reads the extra drilling clearance stored on a bolt (connector) element. Set it with
    `geometry_controller.set_drilling_tolerance()`. Returns 0.0 for invalid IDs and for elements
    that are not bolts.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     tolerance = gc.get_drilling_tolerance(element_id)
        ...     print(element_id, tolerance)

    Returns:
        Drilling tolerance in mm, or 0.0 if the element ID is invalid or the element is not a bolt.
    """

def get_element_reference_face_vertices(element_id: ElementId) -> list[point_3d]:
    """Get the vertices of the reference-side faces of an element.

    Collects the vertices of all facets that lie on the reference side of the element (see
    `geometry_controller.get_reference_side()`) and concatenates them in facet order, so with
    several reference facets the vertices of different faces follow each other. Use
    `geometry_controller.get_element_facets()` if you need the faces separately. Returns an empty
    list for an invalid element ID or when no facet lies on the reference side.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     vertices = gc.get_element_reference_face_vertices(element_id)
        ...     print(element_id, len(vertices), 'vertices on the reference side')

    Returns:
        List of point_3d vertex positions in mm, possibly empty.
    """

def get_element_reference_face_area(element_id: ElementId) -> float:
    """Get the area of the reference side of an element in mm2.

    Sums the area of all facets whose plane normal equals the normal of the reference side (see
    `geometry_controller.get_reference_side()`). Returns 0.0 for an invalid element ID or when no
    facet matches.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     area = gc.get_element_reference_face_area(element_id)
        ...     print(element_id, area)

    Returns:
        Reference face area in mm2, or 0.0 if the element ID is invalid.
    """

def get_center_of_gravity_for_list(element_id_list: list[ElementId]) -> point_3d:
    """Get the volume-weighted center of gravity of several elements.

    Combines the centers of gravity of the elements, each weighted by its volume
    (`geometry_controller.get_volume()`). Elements with practically zero volume count with weight 1.
    Invalid IDs are skipped. For a weighting by material weight use
    `geometry_controller.get_center_of_gravity_for_list_considering_materials()`. An empty list or
    no valid element gives (0, 0, 0).

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> cog = gc.get_center_of_gravity_for_list(element_ids)
        >>> print('Center of gravity:', cog)

    Returns:
        Combined center of gravity as point_3d in mm, or (0, 0, 0) if no valid element was given.
    """

def get_center_of_gravity_for_list_considering_materials(element_id_list: list[ElementId]) -> point_3d:
    """Get the weight-weighted center of gravity of several elements.

    Combines the centers of gravity of the elements, each weighted by its material-based weight, so
    heavier materials pull the result towards them. Invalid IDs and elements with practically zero
    weight are skipped. For a pure volume weighting use
    `geometry_controller.get_center_of_gravity_for_list()`. An empty list or no weighted element
    gives (0, 0, 0).

    Parameters:
        element_id_list: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> cog = gc.get_center_of_gravity_for_list_considering_materials(element_ids)
        >>> print('Center of gravity:', cog)

    Returns:
        Combined center of gravity as point_3d in mm, or (0, 0, 0) if no element had a weight.
    """

def get_element_facet_count(element_id: ElementId) -> UnsignedInt:
    """Get the number of facets of an element.

    Counts the faces of the element body. Use it before `geometry_controller.get_element_facets()`
    or `geometry_controller.stretch_facet()` to know the valid index range (0 to count - 1). Returns
    0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     count = gc.get_element_facet_count(element_id)
        ...     print(element_id, count)

    Returns:
        Number of facets, or 0 if the element ID is invalid.
    """

def get_weight_real(element_id: ElementId) -> float:
    """Get the real weight of an element in kg.

    Weight of the element in kg. `geometry_controller.get_actual_physical_weight()` returns the same
    value. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     weight = gc.get_weight_real(element_id)
        ...     print(element_id, weight)

    Returns:
        Weight in kg, or 0.0 if the element ID is invalid.
    """

def get_actual_physical_weight(element_id: ElementId) -> float:
    """Get the real weight of an element in kg.

    Alias of `geometry_controller.get_weight_real()`: both call the same function and return the
    same value. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     weight = gc.get_actual_physical_weight(element_id)
        ...     print(element_id, weight)

    Returns:
        Weight in kg, or 0.0 if the element ID is invalid.
    """

def get_actual_physical_volume(element_id: ElementId) -> float:
    """Get the net volume of an element in mm3 after negative geometry.

    Starts from the element body together with its end-type bodies and subtracts drillings of
    connector axes and bolts, opening elements, installation (MEP) bodies and penetrating end-types
    whose bounding box overlaps the element. If none of these exist, the rough volume is returned.
    All elements of the model are scanned, so the call can be slow in large models. Returns 0.0 for
    an invalid element ID. For the volume without subtraction use
    `geometry_controller.get_volume()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     volume = gc.get_actual_physical_volume(element_id)
        ...     print(element_id, volume)

    Returns:
        Net volume in mm3, or 0.0 if the element ID is invalid.
    """

def are_facets_coplanar(first_facet: list[point_3d], second_facet: list[point_3d]) -> bool:
    """Check whether two facets lie in the same plane.

    Builds a plane from the first three points of each facet and tests whether the two planes are
    equal. Only the first three points are used, so they must not be collinear; the rest of the
    facet is ignored. A facet with fewer than 3 points gives False. Typical inputs are facets from
    `geometry_controller.get_element_facets()`.

    Parameters:
        first_facet: Vertices of the first facet, at least 3 points in mm.
        second_facet: Vertices of the second facet, at least 3 points in mm.

    Examples:
        >>> import geometry_controller as gc
        >>> import cadwork

        >>> p = cadwork.point_3d
        >>> bottom = [p(0, 0, 0), p(100, 0, 0), p(100, 100, 0)]
        >>> other = [p(0, 200, 0), p(50, 200, 0), p(50, 300, 0)]
        >>> print(gc.are_facets_coplanar(bottom, other))

    Returns:
        True if both planes are equal, False if not or if a facet has fewer than 3 points.
    """

def get_round_machine_rough_part_negative_width(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the negative width side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the negative width side (-YL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_negative_width()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_negative_width(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_negative_width(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the negative width side.

    Enables or disables the machine rough part rounding option on the negative width side (-YL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_negative_width()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_negative_width(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_negative_width(element_ids[0]))
    """

def get_round_machine_rough_part_positive_width(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the positive width side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the positive width side (+YL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_positive_width()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_positive_width(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_positive_width(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the positive width side.

    Enables or disables the machine rough part rounding option on the positive width side (+YL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_positive_width()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_positive_width(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_positive_width(element_ids[0]))
    """

def get_round_machine_rough_part_negative_height(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the negative height side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the negative height side (-ZL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_negative_height()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_negative_height(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_negative_height(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the negative height side.

    Enables or disables the machine rough part rounding option on the negative height side (-ZL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_negative_height()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_negative_height(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_negative_height(element_ids[0]))
    """

def get_round_machine_rough_part_positive_height(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the positive height side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the positive height side (+ZL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_positive_height()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_positive_height(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_positive_height(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the positive height side.

    Enables or disables the machine rough part rounding option on the positive height side (+ZL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_positive_height()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_positive_height(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_positive_height(element_ids[0]))
    """

def get_round_machine_rough_part_negative_length(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the negative length side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the negative length side (-XL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_negative_length()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_negative_length(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_negative_length(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the negative length side.

    Enables or disables the machine rough part rounding option on the negative length side (-XL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_negative_length()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_negative_length(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_negative_length(element_ids[0]))
    """

def get_round_machine_rough_part_positive_length(element_id: ElementId) -> bool:
    """Get the rounding option of the machine rough part on the positive length side.

    Boolean option of the element that controls the rounding of the machine rough part (the raw part
    size used for machining) on the positive length side (+XL). The option is stored on the element.
    Change it with `geometry_controller.set_round_machine_rough_part_positive_length()`. Returns
    False for an invalid element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     enabled = gc.get_round_machine_rough_part_positive_length(element_id)
        ...     print(element_id, enabled)

    Returns:
        True if the option is enabled, False if it is disabled or the element ID is invalid.
    """

def set_round_machine_rough_part_positive_length(element_id_list: list[ElementId], value: bool) -> None:
    """Set the rounding option of the machine rough part on the positive length side.

    Enables or disables the machine rough part rounding option on the positive length side (+XL) for
    every given element. Invalid IDs are skipped and an empty list does nothing. The elements are
    marked as modified and the display is refreshed if auto refresh is on. Read the value back with
    `geometry_controller.get_round_machine_rough_part_positive_length()`.

    Parameters:
        element_id_list: List of element IDs to change, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        value: True to enable the option, False to disable it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     gc.set_round_machine_rough_part_positive_length(element_ids, True)
        ...     print(gc.get_round_machine_rough_part_positive_length(element_ids[0]))
    """

def get_standard_element_width_from_guid(standard_element_guid: str) -> float:
    """Get the width of a standard element identified by GUID in mm.

    Reads the width of the standard element library entry with the given GUID. Get GUIDs with
    `element_controller.get_standard_beam_guid_list()` or
    `element_controller.get_standard_element_guid_from_name()`. Returns 0.0 if the GUID is empty,
    malformed or unknown. To look up by name use
    `geometry_controller.get_standard_element_width_from_name()`.

    Parameters:
        standard_element_guid: GUID string of a standard element, e.g. from
            `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> for guid in ec.get_standard_beam_guid_list():
        ...     value = gc.get_standard_element_width_from_guid(guid)
        ...     print(guid, value)

    Returns:
        Standard element width in mm, or 0.0 if not found.
    """

def get_standard_element_height_from_guid(standard_element_guid: str) -> float:
    """Get the height of a standard element identified by GUID in mm.

    Reads the height of the standard element library entry with the given GUID. Get GUIDs with
    `element_controller.get_standard_beam_guid_list()` or
    `element_controller.get_standard_element_guid_from_name()`. Returns 0.0 if the GUID is empty,
    malformed or unknown. To look up by name use
    `geometry_controller.get_standard_element_height_from_name()`.

    Parameters:
        standard_element_guid: GUID string of a standard element, e.g. from
            `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> for guid in ec.get_standard_beam_guid_list():
        ...     value = gc.get_standard_element_height_from_guid(guid)
        ...     print(guid, value)

    Returns:
        Standard element height in mm, or 0.0 if not found.
    """

def get_standard_element_length_from_guid(standard_element_guid: str) -> float:
    """Get the length of a standard element identified by GUID in mm.

    Reads the length of the standard element library entry with the given GUID. Get GUIDs with
    `element_controller.get_standard_beam_guid_list()` or
    `element_controller.get_standard_element_guid_from_name()`. Returns 0.0 if the GUID is empty,
    malformed or unknown. To look up by name use
    `geometry_controller.get_standard_element_length_from_name()`.

    Parameters:
        standard_element_guid: GUID string of a standard element, e.g. from
            `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> for guid in ec.get_standard_beam_guid_list():
        ...     value = gc.get_standard_element_length_from_guid(guid)
        ...     print(guid, value)

    Returns:
        Standard element length in mm, or 0.0 if not found.
    """

def get_standard_element_width_from_name(standard_element_name: str) -> float:
    """Get the width of a standard element identified by name in mm.

    Looks up a standard beam in the standard element library by its name in the current program
    language and reads its width. If several entries share the name, the first match is used. Only
    beam-type standard elements are searched. Returns 0.0 if the name is empty or not found. To look
    up by GUID use `geometry_controller.get_standard_element_width_from_guid()`.

    Parameters:
        standard_element_name: Name of a standard beam as shown in the standard element library in
            the current program language.

    Examples:
        >>> import geometry_controller as gc

        >>> value = gc.get_standard_element_width_from_name('Beam 60x120')
        >>> if value == 0.0:
        ...     print('Standard element not found')
        ... else:
        ...     print(value)

    Returns:
        Standard element width in mm, or 0.0 if not found.
    """

def get_standard_element_height_from_name(standard_element_name: str) -> float:
    """Get the height of a standard element identified by name in mm.

    Looks up a standard beam in the standard element library by its name in the current program
    language and reads its height. If several entries share the name, the first match is used. Only
    beam-type standard elements are searched. Returns 0.0 if the name is empty or not found. To look
    up by GUID use `geometry_controller.get_standard_element_height_from_guid()`.

    Parameters:
        standard_element_name: Name of a standard beam as shown in the standard element library in
            the current program language.

    Examples:
        >>> import geometry_controller as gc

        >>> value = gc.get_standard_element_height_from_name('Beam 60x120')
        >>> if value == 0.0:
        ...     print('Standard element not found')
        ... else:
        ...     print(value)

    Returns:
        Standard element height in mm, or 0.0 if not found.
    """

def get_standard_element_length_from_name(standard_element_name: str) -> float:
    """Get the length of a standard element identified by name in mm.

    Looks up a standard beam in the standard element library by its name in the current program
    language and reads its length. If several entries share the name, the first match is used. Only
    beam-type standard elements are searched. Returns 0.0 if the name is empty or not found. To look
    up by GUID use `geometry_controller.get_standard_element_length_from_guid()`.

    Parameters:
        standard_element_name: Name of a standard beam as shown in the standard element library in
            the current program language.

    Examples:
        >>> import geometry_controller as gc

        >>> value = gc.get_standard_element_length_from_name('Beam 60x120')
        >>> if value == 0.0:
        ...     print('Standard element not found')
        ... else:
        ...     print(value)

    Returns:
        Standard element length in mm, or 0.0 if not found.
    """

def get_length_including_end_types(element_id: ElementId) -> float:
    """Get the length of an element including its end-types in mm.

    Full length of the element along its length axis, with the extensions of its end-types included.
    It is the basis of `geometry_controller.get_list_length()`. Compare with
    `geometry_controller.get_length()` for the length without end-types. Returns 0.0 for an invalid
    element ID.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. An invalid ID gives the
            failure value.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     length = gc.get_length_including_end_types(element_id)
        ...     print(element_id, length)

    Returns:
        Full length in mm, or 0.0 if the element ID is invalid.
    """

def create_division_zone(element_id: ElementId, point: point_3d, direction: division_zone_direction) -> None:
    """Create a division zone on an element at a given point.

    A division zone marks a division position on the element. The zone is created at the given point
    and the direction sets its orientation. The element is marked as modified and the display is
    refreshed if auto refresh is on. An invalid element ID is silently ignored. Read the points back
    with `geometry_controller.get_division_zone_points()` and remove the zone with
    `geometry_controller.delete_division_zone()`.

    Parameters:
        element_id: ID of the element to add the division zone to, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        point: Position of the division zone point in global coordinates (mm).
        direction: `cadwork.division_zone_direction` member: positive, negative or no_direction.
            Pass the enum member, not a number.

    Examples:
        >>> import cadwork
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     point = cadwork.point_3d(500.0, 0.0, 0.0)
        ...     direction = cadwork.division_zone_direction.positive
        ...     gc.create_division_zone(element_ids[0], point, direction)
    """

def delete_division_zone(element_id: ElementId) -> None:
    """Delete the division zone of an element.

    Removes the division zone from the element and recalculates the element. The element is marked
    as modified and the display is refreshed if auto refresh is on. An invalid element ID is
    silently ignored. Zones are created with `geometry_controller.create_division_zone()`.

    Parameters:
        element_id: ID of the element whose division zone is deleted, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     gc.delete_division_zone(element_id)
    """

def get_division_zone_points(element_id: ElementId) -> list[point_3d]:
    """Get the division zone points of an element.

    Returns the positions of all division zone points of the element: the points of every horizontal
    and vertical variant, whether positive, negative or without direction. Returns an empty list for
    an invalid element ID or an element without division zones. Zones are created with
    `geometry_controller.create_division_zone()`.

    Parameters:
        element_id: ID of the element to query, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     points = gc.get_division_zone_points(element_id)
        ...     print(element_id, len(points), 'division zone points')

    Returns:
        List of point_3d positions in global coordinates (mm), or an empty list if there are none.
    """

def stretch_facet(element_id: ElementId, facet_index: UnsignedInt, distance: float) -> bool:
    """Move one facet of an element along its normal, growing or shrinking the body.

    Shifts the plane of the chosen planar facet by a distance along its own normal, so the body
    grows or shrinks exactly at that face. The index refers to the facet list at the time of the
    call: a successful stretch can renumber the facets, so read
    `geometry_controller.get_element_facets()` again before stretching another facet of the same
    element. A distance of zero is a successful no-op. Curved facets, bodies made of several
    separate parts and out-of-range indices are rejected and the element stays unchanged. On success
    the element is marked as modified and the display is refreshed if auto refresh is on.

    Parameters:
        element_id: ID of the element to modify, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        facet_index: Zero-based index into the facet list in the order of
            `geometry_controller.get_element_facets()`. Must be smaller than
            `geometry_controller.get_element_facet_count()`.
        distance: Signed movement in mm along the facet normal: positive grows the body at that
            face, negative shrinks it.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     element_id = element_ids[0]
        ...     if gc.get_element_facet_count(element_id) > 0:
        ...         if not gc.stretch_facet(element_id, 0, 10.0):
        ...             print('Facet could not be stretched')

    Returns:
        True if the facet was moved or the distance was zero, False if nothing was changed (invalid
        element ID, no facets, index out of range, curved facet, multi-part body or geometry kernel
        failure). The reason is written to the log and to the geometry controller error list.
    """

def get_element_collision_type(first_element_id: ElementId, second_element_id: ElementId) -> element_collision_type:
    """Classify how the bodies of two elements relate.

    Read-only check that does not modify, activate or highlight anything. It compares the solid
    bodies of the two elements and returns one `geometry_controller.element_collision_type` member.
    Axis and line elements are not supported and give unknown, as do invalid element IDs (an error
    is written to the log). For a plain distance use
    `geometry_controller.get_minimum_distance_between_elements()`.

    Parameters:
        first_element_id: ID of the first element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        second_element_id: ID of the second element.

    Examples:
        >>> import geometry_controller as gc
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     result = gc.get_element_collision_type(element_ids[0], element_ids[1])
        ...     if result == gc.element_collision_type.interlocking:
        ...         print('The bodies interpenetrate')
        ...     else:
        ...         print(result)

    Returns:
        An `element_collision_type`: unknown (invalid element ID or axis/line element), none (no
        collision), unclassified (kernel could not classify), contained (one body fully inside the
        other without touching its boundary), contained_and_touching (inside and touching the
        boundary), touching (shared boundary, no overlapping volume), coincident (bodies coincide),
        interlocking (bodies interpenetrate).
    """
