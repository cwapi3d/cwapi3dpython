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
    """Rotate the local height axis of the elements by 90 degrees.

    Elements without a local axis system and auxiliary elements are skipped. Axis and VBA elements
    are also skipped. Marks the elements as modified and refreshes the display if auto-refresh is
    on. An empty list does nothing.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def rotate_height_axis_180(element_id_list: list[ElementId]) -> None:
    """Rotate the local height axis of the elements by 180 degrees.

    Elements without a local axis system and auxiliary elements are skipped. Axis and VBA elements
    are also skipped. Marks the elements as modified and refreshes the display if auto-refresh is
    on. An empty list does nothing.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def set_over_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the overwidth (list oversize in width direction) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New overwidth, in model units (mm).
    """

def set_over_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the overheight (list oversize in height direction) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New overheight, in model units (mm).
    """

def set_over_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the overlength (list oversize in length direction) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New overlength, in model units (mm).
    """

def set_rounding_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the width rounding value of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New width rounding value, in model units (mm).
    """

def set_rounding_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the height rounding value of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New height rounding value, in model units (mm).
    """

def set_rounding_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the length rounding value of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New length rounding value, in model units (mm).
    """

def set_cross_correction_negative_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative width cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New negative width cross correction, in model units (mm).
    """

def set_cross_correction_positive_width(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive width cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New positive width cross correction, in model units (mm).
    """

def set_cross_correction_negative_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative height cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New negative height cross correction, in model units (mm).
    """

def set_cross_correction_positive_height(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive height cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New positive height cross correction, in model units (mm).
    """

def set_cross_correction_negative_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the negative length cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New negative length cross correction, in model units (mm).
    """

def set_cross_correction_positive_length(element_id_list: list[ElementId], value: float) -> None:
    """Set the positive length cross correction (blank oversize) of the elements.

    Stores the value on each element; the 3D geometry is not changed. Invalid IDs and elements
    without geometry data are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        value: New positive length cross correction, in model units (mm).
    """

def apply_global_scale(element_id_list: list[ElementId], scale: float, origin: point_3d) -> None:
    """Scale the elements around an origin point.

    Applies the scale factor to each element. Marks the elements as modified and refreshes the
    display if auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        scale: Scale factor (1.0 keeps the size).
        origin: Center of scaling, in model coordinates (mm).
    """

def auto_regenerate_axes(element_id_list: list[ElementId]) -> None:
    """Regenerate the local axis systems of the elements.

    Machine data of the elements is deleted first, which may ask the user for confirmation; if that
    fails, no axis is regenerated. Shows a progress dialog that the user can cancel. Invalid IDs
    are skipped. Use auto_regenerate_axes_silently to avoid the dialogs.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def rotate_length_axis_90(element_id_list: list[ElementId]) -> None:
    """Rotate the local length axis of the elements by 90 degrees.

    Elements without a local axis system and auxiliary elements are skipped. Marks the elements as
    modified and refreshes the display if auto-refresh is on. An empty list does nothing.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def rotate_length_axis_180(element_id_list: list[ElementId]) -> None:
    """Rotate the local length axis of the elements by 180 degrees.

    Elements without a local axis system and auxiliary elements are skipped. Marks the elements as
    modified and refreshes the display if auto-refresh is on. An empty list does nothing.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def invert_model(element_id_list: list[ElementId]) -> None:
    """Reverse the orientation of the element bodies.

    Inverts the body of each element. Marks the elements as modified and refreshes the display if
    auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def set_width_real(element_id_list: list[ElementId], width: float) -> None:
    """Resize the width of the elements to a new value.

    Regenerates each element with the new size and keeps the other two dimensions. The reference
    point stays fixed unless a reference element is active, in which case the change may be applied
    from the side nearest to it. Marks the elements as modified and refreshes the display if
    auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        width: New width, in model units (mm).
    """

def set_height_real(element_id_list: list[ElementId], height: float) -> None:
    """Resize the height of the elements to a new value.

    Regenerates each element with the new size and keeps the other two dimensions. The reference
    point stays fixed unless a reference element is active, in which case the change may be applied
    from the side nearest to it. Marks the elements as modified and refreshes the display if
    auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        height: New height, in model units (mm).
    """

def set_length_real(element_id_list: list[ElementId], length: float) -> None:
    """Resize the length of the elements to a new value.

    Regenerates each element with the new size and keeps the other two dimensions. The reference
    point stays fixed unless a reference element is active, in which case the change may be applied
    from the side nearest to it. Marks the elements as modified and refreshes the display if
    auto-refresh is on. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        length: New length, in model units (mm).
    """

def rotate_height_axis_2_points(element_id_list: list[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Align the local height axis (local z) of elements with the direction point1 to point2.

    The local x axis is recomputed from the previous one so that it stays perpendicular to the new
    direction. Elements without a local axis system and auxiliary elements are skipped. Marks the
    elements as modified and refreshes the display if auto-refresh is on.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        point1: Start point of the direction vector.
        point2: End point of the direction vector; must differ from point1.
    """

def clear_errors() -> None:
    """Clear the stored error messages of the geometry controller."""

def set_drilling_tolerance(element_id_list: list[ElementId], tolerance: float) -> None:
    """Set the additional drilling tolerance of bolt elements.

    Only bolt elements are changed; all other elements and invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs of bolts.
        tolerance: Additional drilling tolerance, in model units (mm).
    """

def auto_regenerate_axes_silently(element_id_list: list[ElementId]) -> None:
    """Regenerate the local axis systems of the elements without a dialog.

    Same regeneration as auto_regenerate_axes, but without progress dialog or user interaction,
    and machine data is not deleted. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
    """

def rotate_length_axis_2_points(element_id_list: list[ElementId], point1: point_3d, point2: point_3d) -> None:
    """Align the local length axis (local x) of elements with the direction point1 to point2.

    The local z axis is recomputed from the previous one so that it stays perpendicular to the new
    direction. Elements without a local axis system and auxiliary elements are skipped. Marks the
    elements as modified and refreshes the display if auto-refresh is on.

    Parameters:
        element_id_list: List of element IDs; invalid IDs are skipped.
        point1: Start point of the direction vector.
        point2: End point of the direction vector; must differ from point1.
    """

def get_width(element_id: ElementId) -> float:
    """Get the width of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The width; 0.0 if the element ID is invalid.
    """

def get_height(element_id: ElementId) -> float:
    """Get the height of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The height; 0.0 if the element ID is invalid.
    """

def get_length(element_id: ElementId) -> float:
    """Get the length of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The length; 0.0 if the element ID is invalid.
    """

def get_p1(element_id: ElementId) -> point_3d:
    """Get the start point (P1) of an element.

    For line elements it is the start of the first body edge; otherwise the element's reference
    point P1. Model coordinates (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        point_3d P1; a default point_3d (0, 0, 0) if the element ID is invalid.
    """

def get_p2(element_id: ElementId) -> point_3d:
    """Get the end point (P2) of an element.

    For line elements it is the end of the first body edge; otherwise the element's reference point
    P2. Model coordinates (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        point_3d P2; a default point_3d (0, 0, 0) if the element ID is invalid.
    """

def get_p3(element_id: ElementId) -> point_3d:
    """Get the third reference point (P3) of an element.

    Together with P1 and P2 it defines the local orientation. Model coordinates (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        point_3d P3; a default point_3d (0, 0, 0) if the element ID is invalid.
    """

def get_start_height_cut_angle(element_id: ElementId) -> float:
    """Get the start height cut angle of an element.

    If the end has several cut angles, the first non-zero one is returned.

    Parameters:
        element_id: Element ID.

    Returns:
        The start height cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_start_width_cut_angle(element_id: ElementId) -> float:
    """Get the start width cut angle of an element.

    If the end has several cut angles, the first non-zero one is returned.

    Parameters:
        element_id: Element ID.

    Returns:
        The start width cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_end_height_cut_angle(element_id: ElementId) -> float:
    """Get the end height cut angle of an element.

    If the end has several cut angles, the first non-zero one is returned.

    Parameters:
        element_id: Element ID.

    Returns:
        The end height cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_end_width_cut_angle(element_id: ElementId) -> float:
    """Get the end width cut angle of an element.

    If the end has several cut angles, the first non-zero one is returned.

    Parameters:
        element_id: Element ID.

    Returns:
        The end width cut angle; 0.0 if there is no cut or the element ID is invalid.
    """

def get_over_width(element_id: ElementId) -> float:
    """Get the overwidth (list oversize in width direction) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The overwidth (list oversize in width direction); 0.0 if the element ID is invalid.
    """

def get_over_height(element_id: ElementId) -> float:
    """Get the overheight (list oversize in height direction) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The overheight (list oversize in height direction); 0.0 if the element ID is invalid.
    """

def get_over_length(element_id: ElementId) -> float:
    """Get the overlength (list oversize in length direction) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The overlength (list oversize in length direction); 0.0 if the element ID is invalid.
    """

def get_rounding_width(element_id: ElementId) -> float:
    """Get the width rounding value of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The width rounding value; 0.0 if the element ID is invalid.
    """

def get_rounding_height(element_id: ElementId) -> float:
    """Get the height rounding value of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The height rounding value; 0.0 if the element ID is invalid.
    """

def get_rounding_length(element_id: ElementId) -> float:
    """Get the length rounding value of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The length rounding value; 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_width(element_id: ElementId) -> float:
    """Get the negative width cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The negative width cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_width(element_id: ElementId) -> float:
    """Get the positive width cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The positive width cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_height(element_id: ElementId) -> float:
    """Get the negative height cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The negative height cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_height(element_id: ElementId) -> float:
    """Get the positive height cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The positive height cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_cross_correction_negative_length(element_id: ElementId) -> float:
    """Get the negative length cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The negative length cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_cross_correction_positive_length(element_id: ElementId) -> float:
    """Get the positive length cross correction (blank oversize) of an element.

    Model units (mm).

    Parameters:
        element_id: Element ID.

    Returns:
        The positive length cross correction (blank oversize); 0.0 if the element ID is invalid.
    """

def get_weight(element_id: ElementId) -> float:
    """Get the real weight of an element in kilograms.

    Parameters:
        element_id: Element ID.

    Returns:
        Weight in kg; 0.0 if the element ID is invalid.
    """

def get_list_weight(element_id: ElementId) -> float:
    """Get the weight of the raw part of an element in kg.

    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Weight in kg, or 0.0 if the element is invalid.
    """

def get_volume(element_id: ElementId) -> float:
    """Get the rough volume of an element.

    Negative geometry such as end-types, drillings, connectors, openings and MEP elements is not
    subtracted. Use get_actual_physical_volume for the net volume.

    Parameters:
        element_id: ID of the element.

    Returns:
        Rough volume in mm3, or 0.0 if the element is invalid.
    """

def get_list_volume(element_id: ElementId) -> float:
    """Get the list volume of an element.

    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        List volume in mm3, or 0.0 if the element is invalid.
    """

def get_xl(element_id: ElementId) -> point_3d:
    """Get the length axis direction (XL) of an element.

    Normally the direction from P1 to P2. For a single straight line element it is the start
    direction of that line. Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        XL direction vector, or (0, 0, 0) if the element is invalid.
    """

def get_yl(element_id: ElementId) -> point_3d:
    """Get the width axis direction (YL) of an element.

    Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        YL direction vector, or (0, 0, 0) if the element is invalid.
    """

def get_zl(element_id: ElementId) -> point_3d:
    """Get the height/thickness axis direction (ZL) of an element.

    Normally the direction from P1 to P3. Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        ZL direction vector, or (0, 0, 0) if the element is invalid.
    """

def get_center_of_gravity(element_id: ElementId) -> point_3d:
    """Get the center of gravity of an element.

    Returns (0, 0, 0) for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Center of gravity in global coordinates (mm), or (0, 0, 0) if the element is invalid.
    """

def get_reference_side(element_id: ElementId) -> int:
    """Get the reference side of an element.

    1 is the negative height side (-ZL), 2 the positive width side (+YL), 3 the positive height side
    (+ZL), 4 the negative width side (-YL). Other values (such as -1 or 5) mean the default side
    is used: +YL, or +ZL for panels.

    Parameters:
        element_id: ID of the element.

    Returns:
        Reference side number, or 0 if the element ID is invalid.
    """

def get_element_vertices(element_id: ElementId) -> list[point_3d]:
    """Get all vertices of an element body.

    Returns an empty list for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        List of vertex positions in global coordinates (mm), or an empty list if the element is
        invalid.
    """

def get_element_facets(element_id: ElementId) -> facet_list:
    """Get all facets of an element.

    The returned facet_list also identifies which facets lie on the reference side. Returns an empty
    facet_list for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Facet list of the element, empty if the element is invalid.
    """

def get_list_width(element_id: ElementId) -> float:
    """Get the list width of an element.

    The width as used in element lists. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        List width in mm, or 0.0 if the element is invalid.
    """

def get_list_height(element_id: ElementId) -> float:
    """Get the list height of an element.

    The height as used in element lists. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        List height in mm, or 0.0 if the element is invalid.
    """

def get_list_length(element_id: ElementId) -> float:
    """Get the list length of an element.

    The length as used in element lists. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        List length in mm, or 0.0 if the element is invalid.
    """

def get_minimum_distance_between_elements(first_id: ElementId, second_id: ElementId) -> float:
    """Get the minimum distance between the bodies of two elements.

    If either element ID is invalid, an error is logged and infinity is returned.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Returns:
        Minimum distance in mm, or infinity if either element is invalid.
    """

def get_total_area_of_all_faces(element_id: ElementId) -> float:
    """Get the total area of all faces of an element.

    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Sum of all face areas in mm2, or 0.0 if the element is invalid.
    """

def get_area_of_front_face(element_id: ElementId) -> float:
    """Get the area of the front face of an element.

    Sums the area of all faces flagged as front face. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Front face area in mm2, or 0.0 if the element is invalid.
    """

def get_door_surface(element_id_list: list[ElementId]) -> float:
    """Get the total door opening surface of the given elements.

    Each distinct opening variant found among the elements is counted once (width times height).
    Invalid IDs are skipped; an empty list or no door openings gives 0.0.

    Parameters:
        element_id_list: List of element IDs to search for openings.

    Returns:
        Summed opening area in mm2, 0.0 if none found.
    """

def get_window_surface(element_id_list: list[ElementId]) -> float:
    """Get the total window opening surface of the given elements.

    Each distinct opening variant found among the elements is counted once (width times height).
    Invalid IDs are skipped; an empty list or no window openings gives 0.0.

    Parameters:
        element_id_list: List of element IDs to search for openings.

    Returns:
        Summed opening area in mm2, 0.0 if none found.
    """

def get_local_x() -> point_3d:
    """Get the X' axis of the current rotated coordinate system.

    Describes the user-defined (turned) coordinate system of the model, not an element.

    Returns:
        X' direction vector.
    """

def get_local_z() -> point_3d:
    """Get the Z' axis of the current rotated coordinate system.

    Describes the user-defined (turned) coordinate system of the model, not an element.

    Returns:
        Z' direction vector.
    """

def get_local_y() -> point_3d:
    """Get the Y' axis of the current rotated coordinate system.

    Describes the user-defined (turned) coordinate system of the model, not an element.

    Returns:
        Y' direction vector.
    """

def get_drilling_tolerance(element_id: ElementId) -> float:
    """Get the additional drilling tolerance of a connector element.

    Returns 0.0 for invalid IDs and for elements that are not connectors.

    Parameters:
        element_id: ID of the element.

    Returns:
        Drilling tolerance in mm, or 0.0 if not available.
    """

def get_element_reference_face_vertices(element_id: ElementId) -> list[point_3d]:
    """Get the vertices of the faces on the reference side of an element.

    Vertices of all reference-side facets are concatenated in facet order. Returns an empty list for
    an invalid element or if no facet lies on the reference side.

    Parameters:
        element_id: ID of the element.

    Returns:
        List of vertex positions in global coordinates (mm), possibly empty.
    """

def get_element_reference_face_area(element_id: ElementId) -> float:
    """Get the area of the reference side of an element.

    Sums the area of all facets whose normal equals the reference-side normal. Returns 0.0 for an
    invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Reference face area in mm2, or 0.0 if the element is invalid.
    """

def get_center_of_gravity_for_list(element_id_list: list[ElementId]) -> point_3d:
    """Get the volume-weighted center of gravity of several elements.

    Each element is weighted by its rough volume (elements with practically zero volume count with
    weight 1). Invalid IDs are skipped. An empty list or no valid element gives (0, 0, 0).

    Parameters:
        element_id_list: List of element IDs.

    Returns:
        Combined center of gravity in global coordinates (mm), or (0, 0, 0) if nothing valid was
        given.
    """

def get_center_of_gravity_for_list_considering_materials(element_id_list: list[ElementId]) -> point_3d:
    """Get the weight-weighted center of gravity of several elements.

    Each element is weighted by its material-based weight. Invalid IDs and elements with practically
    zero weight are skipped. An empty list or no valid element gives (0, 0, 0).

    Parameters:
        element_id_list: List of element IDs.

    Returns:
        Combined center of gravity in global coordinates (mm), or (0, 0, 0) if nothing valid was
        given.
    """

def get_element_facet_count(element_id: ElementId) -> UnsignedInt:
    """Get the number of facets of an element.

    Returns 0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Number of facets, or 0 if the element is invalid.
    """

def get_weight_real(element_id: ElementId) -> float:
    """Get the real weight of an element in kg.

    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Weight in kg, or 0.0 if the element is invalid.
    """

def get_actual_physical_weight(element_id: ElementId) -> float:
    """Get the real weight of an element in kg.

    Identical to get_weight_real. Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Weight in kg, or 0.0 if the element is invalid.
    """

def get_actual_physical_volume(element_id: ElementId) -> float:
    """Get the net volume of an element after negative geometry operations.

    Subtracts end-types, drillings of connectors and axes, openings and installation/MEP bodies that
    touch the element's bounding box. Can be slow in large models because all elements are scanned.
    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Net volume in mm3, or 0.0 if the element is invalid.
    """

def are_facets_coplanar(first_facet: list[point_3d], second_facet: list[point_3d]) -> bool:
    """Check whether two facets lie in the same plane.

    Each plane is defined by the first three points of the facet. A facet with fewer than 3 points
    gives False.

    Parameters:
        first_facet: Vertices of the first facet, at least 3 points (mm).
        second_facet: Vertices of the second facet, at least 3 points (mm).

    Returns:
        True if both planes are equal, False otherwise (also for invalid facets).
    """

def get_round_machine_rough_part_negative_width(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartNegativeWidth of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_negative_width(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartNegativeWidth on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_round_machine_rough_part_positive_width(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartPositiveWidth of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_positive_width(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartPositiveWidth on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_round_machine_rough_part_negative_height(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartNegativeHeight of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_negative_height(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartNegativeHeight on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_round_machine_rough_part_positive_height(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartPositiveHeight of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_positive_height(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartPositiveHeight on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_round_machine_rough_part_negative_length(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartNegativeLength of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_negative_length(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartNegativeLength on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_round_machine_rough_part_positive_length(element_id: ElementId) -> bool:
    """Get the option RoundMachineRoughPartPositiveLength of an element.

    Returns False for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Option value, or False if the element is invalid.
    """

def set_round_machine_rough_part_positive_length(element_id_list: list[ElementId], value: bool) -> None:
    """Set the option RoundMachineRoughPartPositiveLength on elements.

    Invalid IDs are skipped and an empty list does nothing. The elements are marked as modified and
    the display is refreshed if needed.

    Parameters:
        element_id_list: List of element IDs to modify.
        value: New value of the option.
    """

def get_standard_element_width_from_guid(standard_element_guid: str) -> float:
    """Get the width of a standard element identified by GUID.

    Returns 0.0 if the GUID is empty, malformed or unknown.

    Parameters:
        standard_element_guid: GUID string of the standard element.

    Returns:
        Standard element width in mm, or 0.0 if not found.
    """

def get_standard_element_height_from_guid(standard_element_guid: str) -> float:
    """Get the height of a standard element identified by GUID.

    Returns 0.0 if the GUID is empty, malformed or unknown.

    Parameters:
        standard_element_guid: GUID string of the standard element.

    Returns:
        Standard element height in mm, or 0.0 if not found.
    """

def get_standard_element_length_from_guid(standard_element_guid: str) -> float:
    """Get the length of a standard element identified by GUID.

    Returns 0.0 if the GUID is empty, malformed or unknown.

    Parameters:
        standard_element_guid: GUID string of the standard element.

    Returns:
        Standard element length in mm, or 0.0 if not found.
    """

def get_standard_element_width_from_name(standard_element_name: str) -> float:
    """Get the width of a standard element identified by name.

    Searches beam-type standard elements by name in the current program language and uses the first
    match. Returns 0.0 if the name is empty or not found.

    Parameters:
        standard_element_name: Name of the standard element.

    Returns:
        Standard element width in mm, or 0.0 if not found.
    """

def get_standard_element_height_from_name(standard_element_name: str) -> float:
    """Get the height of a standard element identified by name.

    Searches beam-type standard elements by name in the current program language and uses the first
    match. Returns 0.0 if the name is empty or not found.

    Parameters:
        standard_element_name: Name of the standard element.

    Returns:
        Standard element height in mm, or 0.0 if not found.
    """

def get_standard_element_length_from_name(standard_element_name: str) -> float:
    """Get the length of a standard element identified by name.

    Searches beam-type standard elements by name in the current program language and uses the first
    match. Returns 0.0 if the name is empty or not found.

    Parameters:
        standard_element_name: Name of the standard element.

    Returns:
        Standard element length in mm, or 0.0 if not found.
    """

def get_length_including_end_types(element_id: ElementId) -> float:
    """Get the length of an element including its end-types.

    Returns 0.0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        Full length in mm, or 0.0 if the element is invalid.
    """

def create_division_zone(element_id: ElementId, point: point_3d, direction: division_zone_direction) -> None:
    """Create a division zone on an element at a given point.

    Modifies the element and refreshes the display if auto refresh is on. An invalid element ID is
    silently ignored.

    Parameters:
        element_id: ID of the element to add the division zone to.
        point: Position of the division zone point, in model units (mm).
        direction: Division zone direction: division_zone_direction.positive, negative or
            no_direction.
    """

def delete_division_zone(element_id: ElementId) -> None:
    """Delete the division zone of an element.

    Recalculates the element and refreshes the display if auto refresh is on. An invalid element ID
    is silently ignored.

    Parameters:
        element_id: ID of the element whose division zone is deleted.
    """

def get_division_zone_points(element_id: ElementId) -> list[point_3d]:
    """Return the division zone points of an element.

    Returns an empty list if the element ID is invalid or the element has no division zone points.

    Parameters:
        element_id: ID of the element to query.

    Returns:
        List of point_3d positions of all division zone points of the element (all horizontal and
        vertical variants); empty list on failure.
    """

def stretch_facet(element_id: ElementId, facet_index: UnsignedInt, distance: float) -> bool:
    """Move one facet of an element along its plane normal, growing or shrinking the body.

    The facet index is only valid for the element's current state: after a successful stretch the
    facet order may change, so re-read the facets (get_element_facets) before stretching another
    facet. Curved facets, non-manifold (multi-part) bodies and out-of-range indices fail.

    Parameters:
        element_id: ID of the element to modify.
        facet_index: Zero-based index into the element's facet list, in the order returned by
            get_element_facets.
        distance: Signed travel in model units (mm) along the facet normal: positive grows the body
            at that face, negative shrinks it, zero is a successful no-op.

    Returns:
        True if the facet was moved or the distance was zero; False if nothing was modified (invalid
        element ID, no facets, index out of range, curved facet, multi-part body or geometry kernel
        failure). The reason is available via get_last_error.
    """

def get_element_collision_type(first_element_id: ElementId, second_element_id: ElementId) -> element_collision_type:
    """Classify how the geometry of two elements relates.

    Read-only: does not modify, activate or highlight anything. Axis and line elements are not
    supported.

    Parameters:
        first_element_id: ID of the first element.
        second_element_id: ID of the second element.

    Returns:
        An element_collision_type: unknown (invalid element ID or axis/line element), none (no
        collision), unclassified (kernel could not classify), contained (one body fully inside the
        other without touching its boundary), contained_and_touching (inside and touching the
        boundary), touching (shared boundary, no overlapping volume), coincident (bodies coincide),
        interlocking (bodies interpenetrate).
    """
