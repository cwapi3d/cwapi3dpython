"""Lifecycle and structural manipulation of model elements.

Domain of element existence: creation of every kind of element from
parameters or geometry, duplication and mirroring, deletion, type
conversion between element kinds, selection and identification, GUID
management, grouping into details/containers, and high-level structural
edits (processes, end-profile cuts, joinery operations). This is the
entry point for any operation that adds, removes, or fundamentally
transforms what exists in the model.
"""

from cadwork.edge_list import edge_list
from cadwork.element_module_properties import element_module_properties
from cadwork.facet_list import facet_list
from cadwork.point_2d import point_2d
from cadwork.point_3d import point_3d
from cadwork.standard_element_type import standard_element_type
from cadwork.text_object_options import text_object_options
from cadwork.coordinate_system_data import coordinate_system_data
from cadwork.element_map_query import element_map_query
from cadwork.element_filter import element_filter
from cadwork.hit_result import hit_result
from cadwork.active_point_result import active_point_result
from cadwork.vertex_list import vertex_list
from cadwork.shoulder_options import shoulder_options
from cadwork.heel_shoulder_options import heel_shoulder_options
from cadwork.double_shoulder_options import double_shoulder_options
from cadwork.api_types import *
from cadwork.element_segment import element_segment
from cadwork.spline_surface_order import spline_surface_order

def delete_elements(element_id_list: list[ElementId]) -> None:
    """Delete the given elements permanently.

    Not added to the undo stack; use delete_elements_with_undo for an undoable deletion. Invalid or
    already deleted IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to delete.
    """

def join_elements(element_id_list: list[ElementId]) -> None:
    """Join the given elements into one group.

    Needs at least two elements. A yes/no confirmation may be shown to the user, and problems (for
    example a single element or elements already in the same group) are reported in the command bar
    instead of raising an error. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to join.
    """

def join_top_level_elements(element_id_list: list[ElementId]) -> None:
    """Join the top-level groups of the given elements into one group.

    Like join_elements, but joins at one level only: existing groups of the given elements are kept
    as sub-groups instead of being merged. A yes/no confirmation may be shown to the user. Invalid
    IDs are skipped.

    Parameters:
        element_id_list: List of element IDs whose top-level groups are joined.
    """

def create_rectangular_beam_points(
    width: float, height: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a rectangular beam from three points.

    The beam axis runs from first_point to second_point, so its length is the distance between them.
    The new element is inserted and shown.

    Parameters:
        width: Cross-section width in mm (local Y direction).
        height: Cross-section height in mm (local Z direction).
        first_point: Start point of the beam axis, also the origin of the beam.
        second_point: End point of the beam axis; its direction from first_point is the local X
            direction.
        third_point: Point whose direction from first_point defines the local Z direction (the
            height direction).

    Examples:
        >>> beam_width = 200.
        >>> beam_height = 400.
        >>> beam_axis_start_pt =  cadwork.point_3d(300., 0., 0.)
        >>> beam_axis_end_pt = cadwork.point_3d(300., 0., 4000.)
        >>> length_vector = (beam_axis_end_pt - beam_axis_start_pt).normalized()
        >>> beam_axis_y = cadwork.point_3d(1., 0., 0.)
        >>> beam_axis_z = length_vector.cross(beam_axis_y).normalized()
        >>> beam_height_axis_pt = beam_axis_start_pt + beam_axis_z
        >>> beam_id = ec.create_rectangular_beam_points(beam_width, beam_height, beam_axis_start_pt,  beam_axis_end_pt,  beam_height_axis_pt )

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_circular_beam_points(
    diameter: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a circular beam from three points.

    The beam axis runs from first_point to second_point, so its length is the distance between them.
    The new element is inserted and shown.

    Parameters:
        diameter: Diameter of the beam in mm.
        first_point: Start point of the beam axis, also the origin of the beam.
        second_point: End point of the beam axis; its direction from first_point is the local X
            direction.
        third_point: Point whose direction from first_point defines the local Z direction
            (rotational orientation of the beam).

    Examples:
        >>> beam_diameter = 120.
        >>> beam_axis_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> beam_axis_end_pt = cadwork.point_3d(0., 0., 3000.)
        >>> length_vector = (beam_axis_end_pt - beam_axis_start_pt).normalized()
        >>> beam_axis_y = cadwork.point_3d(1., 0., 0.)
        >>> beam_axis_z = length_vector.cross(beam_axis_y).normalized()
        >>> beam_orientation_pt = beam_axis_start_pt + beam_axis_z
        >>> beam_id = ec.create_circular_beam_points(beam_diameter, beam_axis_start_pt, beam_axis_end_pt, beam_orientation_pt)

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_square_beam_points(
    width: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a square beam from three points.

    The beam axis runs from first_point to second_point, so its length is the distance between them.
    The new element is inserted and shown.

    Parameters:
        width: Side length of the square cross-section in mm.
        first_point: Start point of the beam axis, also the origin of the beam.
        second_point: End point of the beam axis; its direction from first_point is the local X
            direction.
        third_point: Point whose direction from first_point defines the local Z direction
            (orientation of the cross-section).

    Examples:
        >>> beam_width = 100.
        >>> beam_axis_start_pt = cadwork.point_3d(500., 500., 0.)
        >>> beam_axis_end_pt = cadwork.point_3d(500., 500., 2500.)
        >>> length_vector = (beam_axis_end_pt - beam_axis_start_pt).normalized()
        >>> reference_vector = cadwork.point_3d(0., 1., 0.)
        >>> beam_axis_z = length_vector.cross(reference_vector).normalized()
        >>> orientation_pt = beam_axis_start_pt + beam_axis_z
        >>> beam_id = ec.create_square_beam_points(beam_width, beam_axis_start_pt, beam_axis_end_pt, orientation_pt)

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_rectangular_beam_vectors(
    width: float,
    height: float,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a rectangular beam from a start point, directions and dimensions.

    The beam extends from starting_point along x_local_direction for the given length. The new
    element is inserted and shown.

    Parameters:
        width: Cross-section width in mm (local Y direction).
        height: Cross-section height in mm (local Z direction).
        length: Beam length in mm, measured along the local X direction.
        starting_point: Start point of the beam (origin of the local coordinate system).
        x_local_direction: Direction of the beam axis (local X).
        z_local_direction: Direction of the cross-section height (local Z); should be perpendicular
            to x_local_direction.

    Examples:
        >>> beam_width = 150.
        >>> beam_height = 300.
        >>> beam_length = 4000.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Direction along height
        >>> beam_id = ec.create_rectangular_beam_vectors(beam_width, beam_height, beam_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_circular_beam_vectors(
    diameter: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a circular beam from a start point, directions and dimensions.

    The beam extends from starting_point along x_local_direction for the given length. The new
    element is inserted and shown.

    Parameters:
        diameter: Diameter of the beam in mm.
        length: Beam length in mm, measured along the local X direction.
        starting_point: Start point of the beam (origin of the local coordinate system).
        x_local_direction: Direction of the beam axis (local X).
        z_local_direction: Direction of the local Z axis; only fixes the rotational orientation of
            the beam.

    Examples:
        >>> beam_diameter = 100.
        >>> beam_length = 3500.
        >>> origin_point = cadwork.point_3d(200., 200., 200.)
        >>> x_direction = cadwork.point_3d(0., 1., 0.)  # Beam aligned with Y axis
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Z orientation (arbitrary for circular beam)
        >>> beam_id = ec.create_circular_beam_vectors(beam_diameter, beam_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_square_beam_vectors(
    width: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a square beam from a start point, directions and dimensions.

    The beam extends from starting_point along x_local_direction for the given length. The new
    element is inserted and shown.

    Parameters:
        width: Side length of the square cross-section in mm.
        length: Beam length in mm, measured along the local X direction.
        starting_point: Start point of the beam (origin of the local coordinate system).
        x_local_direction: Direction of the beam axis (local X).
        z_local_direction: Direction of the local Z axis; should be perpendicular to
            x_local_direction.

    Examples:
        >>> beam_width = 120.
        >>> beam_length = 2800.
        >>> origin_point = cadwork.point_3d(0., 0., 500.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Direction for orientation
        >>> beam_id = ec.create_square_beam_vectors(beam_width, beam_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the created beam, or 0 if creation failed.
    """

def create_rectangular_panel_points(
    width: float, thickness: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a rectangular panel from three points.

    The panel length runs from first_point to second_point, so it equals the distance between them.
    The new element is inserted and shown.

    Parameters:
        width: Panel width in mm (local Y direction).
        thickness: Panel thickness in mm (local Z direction).
        first_point: Start point of the panel length, also the origin of the panel.
        second_point: End point of the panel length; its direction from first_point is the local X
            direction.
        third_point: Point whose direction from first_point defines the local Z direction (the
            thickness direction, i.e. the panel normal).

    Examples:
        >>> panel_width = 1200.
        >>> panel_thickness = 27.
        >>> panel_corner_pt = cadwork.point_3d(0., 0., 0.)
        >>> panel_length_pt = cadwork.point_3d(0., 2400., 0.)
        >>> # Calculate a point to define panel orientation
        >>> normal_vector = cadwork.point_3d(0., 0., 1.)  # Panel normal in Z direction
        >>> orientation_pt = panel_corner_pt + normal_vector
        >>> panel_id = ec.create_rectangular_panel_points(panel_width, panel_thickness, panel_corner_pt, panel_length_pt, orientation_pt)

    Returns:
        ID of the created panel, or 0 if creation failed.
    """

def create_rectangular_panel_vectors(
    width: float,
    thickness: float,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a rectangular panel from a start point, directions and dimensions.

    The panel extends from starting_point along x_local_direction for the given length. The new
    element is inserted and shown.

    Parameters:
        width: Panel width in mm (local Y direction).
        thickness: Panel thickness in mm (local Z direction).
        length: Panel length in mm, measured along the local X direction.
        starting_point: Start point of the panel (origin of the local coordinate system).
        x_local_direction: Direction of the panel length (local X).
        z_local_direction: Direction of the panel thickness / normal (local Z); should be
            perpendicular to x_local_direction.

    Examples:
        >>> panel_width = 1000.
        >>> panel_thickness = 20.
        >>> panel_length = 2000.
        >>> origin_point = cadwork.point_3d(0., 0., 100.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Panel normal direction
        >>> panel_id = ec.create_rectangular_panel_vectors(panel_width, panel_thickness, panel_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the created panel, or 0 if creation failed.
    """

def create_drilling_points(diameter: float, first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a drilling between two points.

    The drilling runs from first_point to second_point, so its length is the distance between them.

    Parameters:
        diameter: Diameter of the drilling in mm.
        first_point: Start point of the drilling.
        second_point: End point of the drilling.

    Examples:
        >>> drill_diameter = 30.
        >>> drill_start_pt = cadwork.point_3d(100., 100., 0.)
        >>> drill_end_pt = cadwork.point_3d(100., 100., 200.)
        >>> drilling_id = ec.create_drilling_points(drill_diameter, drill_start_pt, drill_end_pt)

    Returns:
        ID of the created drilling, or 0 if creation failed.
    """

def create_drilling_vectors(
    diameter: float, length: float, starting_point: point_3d, drilling_direction: point_3d
) -> ElementId:
    """Create a drilling from a start point, direction and length.

    The end point is starting_point + drilling_direction * length. The direction is not normalized
    internally, so a non-unit vector changes the drilling length.

    Parameters:
        diameter: Diameter of the drilling in mm.
        length: Length of the drilling in mm.
        starting_point: Start point of the drilling.
        drilling_direction: Direction of the drilling; must be a unit vector.

    Examples:
        >>> drill_diameter = 12.
        >>> drill_length = 180.
        >>> drill_start_pt = cadwork.point_3d(200., 200., 50.)
        >>> drill_direction = cadwork.point_3d(0., 0., 1.)  # Drilling in Z direction
        >>> drilling_id = ec.create_drilling_vectors(drill_diameter, drill_length, drill_start_pt, drill_direction)

    Returns:
        ID of the created drilling, or 0 if creation failed.
    """

def create_line_points(first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a line between two points.

    Parameters:
        first_point: Start point of the line.
        second_point: End point of the line.

    Examples:
        >>> line_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> line_end_pt = cadwork.point_3d(500., 500., 0.)
        >>> line_id = ec.create_line_points(line_start_pt, line_end_pt)

    Returns:
        ID of the created line, or 0 if creation failed.
    """

def create_line_vectors(length: float, starting_point: point_3d, line_direction: point_3d) -> ElementId:
    """Create a line from a start point, direction and length.

    The end point is starting_point + line_direction * length. The direction is not normalized
    internally, so a non-unit vector changes the line length.

    Parameters:
        length: Length of the line in mm.
        starting_point: Start point of the line.
        line_direction: Direction of the line; must be a unit vector.

    Examples:
        >>> line_length = 1000.
        >>> line_start_pt = cadwork.point_3d(200., 0., 200.)
        >>> line_direction = cadwork.point_3d(1., 1., 0.).normalized()  # 45 degree line in XY plane
        >>> line_id = ec.create_line_vectors(line_length, line_start_pt, line_direction)

    Returns:
        ID of the created line, or 0 if creation failed.
    """

def create_node(node_position: point_3d) -> ElementId:
    """Create a node at the given position.

    Parameters:
        node_position: Position of the node.

    Examples:
        >>> node_position = cadwork.point_3d(250., 250., 100.)
        >>> node_id = ec.create_node(node_position)

    Returns:
        ID of the created node, or 0 if creation failed.
    """

def solder_elements(element_id_list: list[ElementId]) -> list[ElementId]:
    """Solder the given elements together where possible.

    Only elements that can be soldered are processed; the others are ignored, as are invalid IDs.

    Parameters:
        element_id_list: List of element IDs to solder.

    Returns:
        List of IDs of the soldered elements; empty if nothing was soldered.
    """

def convert_beam_to_panel(element_id_list: list[ElementId]) -> None:
    """Convert beams to panels in place.

    The elements keep their IDs. Successfully converted elements are deactivated. Elements that
    cannot be converted are left unchanged; invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the beams to convert.
    """

def convert_panel_to_beam(element_id_list: list[ElementId]) -> None:
    """Convert panels to beams in place.

    The elements keep their IDs. Successfully converted elements are deactivated. Elements that
    cannot be converted are left unchanged; invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the panels to convert.
    """

def delete_all_element_end_types(element_id_list: list[ElementId]) -> None:
    """Remove all end types from the given elements.

    Elements without end types and invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to clear.
    """

def delete_all_element_processes(element_id_list: list[ElementId]) -> None:
    """Remove all processes (machining) from the given elements.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to clear.
    """

def move_element(element_id_list: list[ElementId], move_vector: point_3d) -> None:
    """Move the given elements by a vector.

    Elements are moved in place and keep their IDs. Invalid IDs are skipped. Not added to the undo
    stack.

    Parameters:
        element_id_list: List of element IDs to move.
        move_vector: Displacement applied to every element, in mm.
    """

def create_polygon_beam(
    polygon_vertices: vertex_list, thickness: float, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a beam by extruding a 3D polygon along its face normal.

    The polygon is closed automatically and must be planar. It is extruded along its own face normal
    (derived from the vertex order, right-hand rule), and the polygon plane ends up in the middle of
    the beam. x_local_direction and z_local_direction only label the local axes of the new beam;
    they do not steer the extrusion. Prefer create_polygon_beam_vectors, which is independent of
    vertex order. Failures return 0 and no error message is recorded.

    Parameters:
        polygon_vertices: Vertices of the polygon in world coordinates, at least 3, coplanar and
            enclosing a non-zero area.
        thickness: Extrusion distance in mm along the polygon normal (beam length).
        x_local_direction: Direction assigned to the local X axis of the beam.
        z_local_direction: Direction assigned to the local Z axis of the beam.

    Examples:
        >>> # Create a triangular beam
        >>> vertices = cadwork.vertex_list()
        >>> vertices.append(cadwork.point_3d(0., 0., 0.))
        >>> vertices.append(cadwork.point_3d(200., 0., 0.))
        >>> vertices.append(cadwork.point_3d(100., 173.2, 0.))  # Equilateral triangle
        >>> beam_thickness = 1000.  # Length of the beam
        >>> extrusion_vector = cadwork.point_3d(0., 0., 1.)  # Direction of extrusion
        >>> z_vector = cadwork.point_3d(1., 0., 0.)  # Orientation vector
        >>> polygon_beam_id = ec.create_polygon_beam(vertices, beam_thickness, extrusion_vector, z_vector)

    Returns:
        ID of the created beam, or 0 on failure (fewer than 3 vertices, non-planar polygon,
        modelling error).
    """

def create_polygon_beam_vectors(
    polygon_vertices: list[point_2d | tuple[float, float]],
    thickness: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a beam by extruding a 2D profile along the local X direction.

    The profile is given in (u, v) coordinates in the plane normal to x_local_direction. Point (u,
    v) maps to starting_point + u * local Y + v * local Z, where local Y and Z are derived from the
    two directions; the profile is not re-centred. The beam extends from starting_point along
    x_local_direction for thickness. Vertex order does not matter. On failure an error message
    naming the offending argument is recorded.

    Parameters:
        polygon_vertices: Profile as an open loop of at least 3 point_2d or (u, v) tuples; do not
            repeat the first point. Must enclose a non-zero area.
        thickness: Extrusion length in mm along x_local_direction; must be greater than 0.
        starting_point: 3D position of profile coordinate (0, 0), lying on the start face of the
            beam.
        x_local_direction: Direction of the beam axis; the extrusion follows it.
        z_local_direction: Orientation hint for the local Z axis; need not be exactly perpendicular
            to x_local_direction.

    Examples:
        >>> # Create a triangular beam from a 2D profile
        >>> profile = [cadwork.point_2d(0., 0.), cadwork.point_2d(200., 0.), cadwork.point_2d(100., 173.2)]
        >>> beam_thickness = 1000.  # Length of the beam
        >>> start_point = cadwork.point_3d(0., 0., 0.)
        >>> extrusion_vector = cadwork.point_3d(1., 0., 0.)  # Direction of extrusion
        >>> z_vector = cadwork.point_3d(0., 0., 1.)  # Orientation vector
        >>> polygon_beam_id = ec.create_polygon_beam_vectors(profile, beam_thickness, start_point, extrusion_vector, z_vector)
        >>> # Tuples are implicitly converted to point_2d
        >>> polygon_beam_id = ec.create_polygon_beam_vectors([(0., 0.), (200., 0.), (100., 173.2)], beam_thickness, start_point, extrusion_vector, z_vector)

    Returns:
        ID of the created beam, or 0 on failure.
    """

def create_text_object(
    text: str, position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, size: float
) -> ElementId:
    """Create a text object using the default font (Tahoma).

    The text consists of one element per letter; the returned ID is that of the last letter element.
    The text lies in the plane perpendicular to z_local_direction, with its baseline along
    x_local_direction.

    Parameters:
        text: The text content.
        position: Insertion point (origin) of the text.
        x_local_direction: Direction of the text baseline (local X).
        z_local_direction: Normal of the plane the text lies in (local Z).
        size: Text height in mm.

    Examples:
        >>> text_content = "Cadwork API"
        >>> text_position = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Text direction
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Text orientation
        >>> text_height = 200.
        >>> text_id = ec.create_text_object(text_content, text_position, x_direction, z_direction, text_height)

    Returns:
        ID of the last created letter element, or 0 if the text object could not be created.
    """

def copy_elements(element_id_list: list[ElementId], copy_vector: point_3d) -> list[int]:
    """Copy elements and move the copies by a vector.

    The originals are not changed. Invalid IDs are skipped. Group, container and variant assignments
    are copied; the copies are assigned to the active building storey unless the user's copy
    settings keep the storey of the originals.

    Parameters:
        element_id_list: List of element IDs to copy.
        copy_vector: Offset of the copies relative to the originals, in mm.

    Returns:
        List of IDs of the new copies only; empty if nothing was copied.
    """

def rotate_elements(
    element_id_list: list[ElementId], origin: point_3d, rotation_axis: point_3d, rotation_angle: float
) -> None:
    """Rotate elements around an axis.

    Elements are rotated in place and keep their IDs. If rotation_axis has zero length, a message is
    printed and nothing is rotated. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to rotate.
        origin: Point the rotation axis passes through.
        rotation_axis: Direction of the rotation axis; must not be the zero vector.
        rotation_angle: Rotation angle in radians.
    """

def subtract_elements(hard_elements: list[ElementId], soft_elements: list[ElementId]) -> list[ElementId]:
    """Subtract the volume of hard_elements from soft_elements (boolean difference).

    Soft elements are cut in place and keep their IDs; hard elements are not modified. The operation
    is added to the undo stack as one step. Invalid IDs are skipped.

    Parameters:
        hard_elements: List of IDs of the cutting elements.
        soft_elements: List of IDs of the elements to be cut.

    Returns:
        List of IDs of additional elements created when a soft element is split into several
        disconnected pieces; does not include the IDs in soft_elements. Empty if nothing was split
        or the operation failed.
    """

def check_element_id(element_id: ElementId) -> bool:
    """Check whether an element with the given ID exists.

    Parameters:
        element_id: Element ID to check.

    Returns:
        True if the element exists, False otherwise.
    """

def start_element_module_calculation(covers: list[ElementId]) -> None:
    """Run the element module calculation for the given cover elements.

    Only cover elements (walls, floors, roofs, openings) are used; other elements and invalid IDs
    are ignored. Does nothing if the element module is not licensed. Creates the resulting elements
    and refreshes the display.

    Parameters:
        covers: List of IDs of the cover elements.
    """

def set_element_detail_path(path: str) -> None:
    """Set the folder used for element details.

    An empty path is ignored.

    Parameters:
        path: Path of the element detail folder.
    """

def get_element_from_cadwork_guid(cadwork_guid: str) -> ElementId:
    """Find the element with the given cadwork GUID.

    Searches visible and hidden elements.

    Parameters:
        cadwork_guid: GUID string of the element.

    Returns:
        ID of the matching element, or 0 if the GUID is invalid or no element matches.
    """

def add_elements_to_undo(element_id_list: list[ElementId], cmd: int) -> None:
    """Register elements as one undo step.

    cmd 1 registers the elements as created (undo deletes them); cmd 2 registers them as modified,
    storing their current state and attributes, so call it before changing them. Any other cmd does
    nothing. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to register.
        cmd: 1 = elements were created, 2 = elements are modified.
    """

def make_undo() -> None:
    """Undo the last undo step.

    Operations that do not register an undo step (for example delete_elements) cannot be undone this
    way.
    """

def make_redo() -> None:
    """Redo the last undone step."""

def split_elements(element_id_list: list[ElementId]) -> None:
    """Split joined element groups.

    Reverses a join: the given elements are separated from their groups. An error is shown in the
    command bar (not raised) if the selection is an incomplete group. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to split.
    """

def set_line_to_marking_line(element_id_list: list[ElementId]) -> None:
    """Turn line elements into marking lines.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the line elements.
    """

def set_line_to_normal_line(element_id_list: list[ElementId]) -> None:
    """Turn marking lines back into normal lines.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the line elements.
    """

def create_auto_export_solid_from_standard(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str
) -> ElementId:
    """Create an auto export solid around elements from a standard export solid.

    The new export solid encloses the given elements (bounding box aligned to the world axes, with a
    10 mm offset) and takes their assignment. All elements are deactivated first. Standard element
    names are not unique, only GUIDs are: if several standard elements share this name, the first
    match is used. Folders of the standard element library are not handled by the API and cannot be
    used to select one.

    Parameters:
        element_id_list: List of IDs of the elements to enclose; invalid IDs are skipped.
        output_name: Name given to the new export solid.
        standard_element_name: Name of a standard element of type export solid.

    Returns:
        ID of the created export solid, or 0 if no standard export solid with that name exists.
    """

def set_element_module_properties_for_elements(
    element_id_list: list[ElementId], properties: element_module_properties
) -> None:
    """Set the element module properties of the given elements.

    All module properties of each element are replaced by the values in properties, so properties
    not set in it are cleared. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the elements to modify.
        properties: The module properties to apply.
    """

def create_text_object_with_font(
    text: str, position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, size: float, font_name: str
) -> ElementId:
    """Create a text object using a given font.

    The text consists of one element per letter; the returned ID is that of the last letter element.
    The text lies in the plane perpendicular to z_local_direction, with its baseline along
    x_local_direction.

    Parameters:
        text: The text content.
        position: Insertion point (origin) of the text.
        x_local_direction: Direction of the text baseline (local X).
        z_local_direction: Normal of the plane the text lies in (local Z).
        size: Text height in mm.
        font_name: Name of an installed font, for example Arial.

    Examples:
        >>> text_content = "Custom Text"
        >>> text_position = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Text direction
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Text orientation
        >>> text_height = 150.
        >>> font = "Arial"
        >>> text_id = ec.create_text_object_with_font(text_content, text_position, x_direction, z_direction, text_height, font)

    Returns:
        ID of the last created letter element, or 0 if the text object could not be created.
    """

def apply_transformation_coordinate(
    element_id_list: list[ElementId],
    old_point: point_3d,
    old_x_local_direction: point_3d,
    old_y_local_direction: point_3d,
    new_point: point_3d,
    new_x_local_direction: point_3d,
    new_y_local_direction: point_3d,
) -> None:
    """Transform elements from one coordinate system to another.

    The elements are moved and rotated in place so that the old coordinate system maps onto the new
    one. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the elements to transform.
        old_point: Origin of the source coordinate system.
        old_x_local_direction: X axis direction of the source coordinate system.
        old_y_local_direction: Y axis direction of the source coordinate system.
        new_point: Origin of the target coordinate system.
        new_x_local_direction: X axis direction of the target coordinate system.
        new_y_local_direction: Y axis direction of the target coordinate system.
    """

def delete_elements_with_undo(element_id_list: list[ElementId]) -> None:
    """Delete the given elements as one undoable step.

    Invalid IDs are skipped. Use make_undo to restore the elements.

    Parameters:
        element_id_list: List of element IDs to delete.
    """

def add_created_elements_to_undo(element_id_list: list[ElementId]) -> None:
    """Register already created elements as one undo step.

    After this, make_undo removes the elements again. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the elements that were created.
    """

def add_modified_elements_to_undo(element_id_list: list[ElementId]) -> None:
    """Register elements as modified in one undo step.

    Stores the current state and attributes of the elements as the state to restore on undo, so call
    it before modifying them. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the elements to be modified.
    """

def recreate_elements(element_id_list: list[ElementId]) -> None:
    """Rebuild the display representation of the given elements.

    Visibility states are preserved and the view is redrawn. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of IDs of the elements to recreate.
    """

def create_multi_wall(element_id_list: list[ElementId]) -> None:
    """Couple wall, roof and floor elements into a multi-wall structure.

    Only walls, roofs and floors among the given elements are used; at least two are needed,
    otherwise nothing happens. Elements within the configured coupling distance are coupled.

    Parameters:
        element_id_list: List of IDs of the wall, roof or floor elements to couple.
    """

def get_user_element_ids() -> list[ElementId]:
    """Let the user select elements interactively and return their IDs.

    Blocks until the user finishes the selection in the 3D view. If the user presses Esc, an error
    is recorded and the list contains whatever was selected (possibly empty).

    Returns:
        List of IDs of the elements selected by the user; empty if none were selected.
    """

def get_user_element_ids_with_existing(element_id_list: list[ElementId]) -> list[ElementId]:
    """Let the user select elements interactively, with the given elements pre-marked.

    The given elements are shown as marked during the selection and visibility is restored
    afterwards. Blocks until the user finishes. If the user presses Esc, an error is recorded and
    the list contains whatever was selected (possibly empty).

    Parameters:
        element_id_list: List of IDs of the elements to mark at the start of the selection; invalid
            IDs are skipped.

    Returns:
        List of IDs of the elements selected by the user; empty if none were selected.
    """

def clear_errors() -> None:
    """Clear the recorded API error messages.

    Errors are recorded, for example, when the user cancels an interactive selection with Esc.
    """

def glide_elements(element_id_list: list[ElementId], glide_origin_point: point_3d) -> None:
    """Move elements interactively; the user picks the destination.

    Blocks until the user confirms or cancels. If the user presses Esc, an error is recorded.
    Invalid IDs are skipped. In 2D plane mode the elements are additionally moved by the glide point
    projected onto the working plane.

    Parameters:
        element_id_list: List of IDs of the elements to move.
        glide_origin_point: Reference point from which the elements are glided.
    """

def cut_elements_with_miter(first_id: ElementId, second_id: ElementId) -> bool:
    """Cut two elements with a miter joint.

    Both elements are modified in place. Always returns True, even if an ID is invalid (then nothing
    is cut) or the cut failed.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Returns:
        True (also when nothing was cut).
    """

def cut_element_with_plane(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> bool:
    """Cut an element in place with a plane.

    Modifies the element directly and is not added to undo. The plane consists of all points p where
    the dot product of p and the normal equals the distance.

    Parameters:
        element_id: ID of the element to cut.
        cut_plane_normal_vector: Normal vector of the cut plane; pass a unit vector.
        distance_from_global_origin: Signed distance of the plane from the global origin, measured
            along the normal (model units, mm).

    Examples:
        >>> import math
        >>> beam_height = 240.
        >>> beam_id = ec.create_rectangular_beam_vectors(120., beam_height, 3000., cadwork.point_3d(0., 0., 0.),
        ...                                             cadwork.point_3d(0., 0., 1.), cadwork.point_3d(0., 1., 0.))
        >>> # Define plane normal vector (30° from vertical in Y-Z plane)
        >>> angle_rad = math.radians(30)
        >>> plane_normal = cadwork.point_3d(0., -math.sin(angle_rad), math.cos(angle_rad)).normalized()
        >>> # Calculate distance from origin to plane
        >>> plane_point = cadwork.point_3d(0., beam_height * .5, 1500.)  # Point for the cut plane
        >>> distance = plane_point.dot(plane_normal)  # Distance from origin to plane
        >>> # To measure (check result) the distance correctly in cadwork, create a parallel plane to the cut plane
        >>> # with the result of distance as the offset. This plane should hit through the origin (0, 0, 0).
        >>> print(f"Plane normal: {plane_normal}, Distance: {distance}")
        >>> result = ec.cut_element_with_plane(beam_id, plane_normal, distance)
        >>> print(f"Cut operation successful: {result}")

    Returns:
        True once the cut was issued. This does not guarantee that the element was changed.
    """

def create_circular_mep(diameter: float, points: list[point_3d]) -> ElementId:
    """Create a circular MEP (installation) element along a polyline.

    The element follows the straight segments between consecutive points. It is created with a fixed
    colour and added to the active scene.

    Parameters:
        diameter: Diameter of the round installation (mm).
        points: Ordered points of the path; consecutive points are joined by straight segments.

    Returns:
        ID of the new element, or 0 if a segment could not be built (for example two identical
        consecutive points).
    """

def create_rectangular_mep(width: float, depth: float, points: list[point_3d]) -> ElementId:
    """Create a rectangular MEP (installation) element along a polyline.

    The element follows the straight segments between consecutive points. It is created with a fixed
    colour and added to the active scene.

    Parameters:
        width: Width of the rectangular cross-section (mm).
        depth: Depth of the rectangular cross-section (mm).
        points: Ordered points of the path; consecutive points are joined by straight segments.

    Returns:
        ID of the new element, or 0 if a segment could not be built (for example two identical
        consecutive points).
    """

def slice_element_with_plane(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> bool:
    """Slice an element into parts with a plane.

    The slice is added to undo. Newly created parts are not returned by this function.

    Parameters:
        element_id: ID of the element to slice.
        cut_plane_normal_vector: Normal vector of the slicing plane; pass a unit vector.
        distance_from_global_origin: Signed distance of the plane from the global origin, measured
            along the normal (model units, mm).

    Examples:
        >>> import math
        >>> # Create a panel to slice
        >>> panel_width = 1200.
        >>> panel_thickness = 20.
        >>> panel_length = 2400.
        >>> panel_id = ec.create_rectangular_panel_vectors(panel_width, panel_thickness, panel_length,
        ...                                              cadwork.point_3d(0., 0., 0.),
        ...                                              cadwork.point_3d(1., 0., 0.),
        ...                                              cadwork.point_3d(0., 0., 1.))
        >>> # Define plane normal vector (45° in XY plane)
        >>> angle_rad = math.radians(45)
        >>> plane_normal = cadwork.point_3d(math.cos(angle_rad), math.sin(angle_rad), 0.).normalized()
        >>> # Calculate distance from origin to plane - slice through center of panel
        >>> panel_center = cadwork.point_3d(panel_length/2., panel_width/2., 0.)
        >>> ec.create_node(panel_center)  # Create a node at the center of the panel
        >>> distance = panel_center.dot(plane_normal)  # Distance from origin to plane
        >>> # Verify plane equation: dot(point_on_plane, normal) = distance
        >>> # Any point on the plane should satisfy this equation
        >>> print(f"Plane normal: {plane_normal}, Distance: {distance}")
        >>> # Slice the panel
        >>> result = ec.slice_element_with_plane(panel_id, plane_normal, distance)
        >>> print(f"Slice operation successful: {result}")
        >>> # Note: slice_element_with_plane keeps both parts as a joined element

    Returns:
        True once the slice was issued. This does not guarantee that the element was changed.
    """

def create_auto_container_from_standard(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str
) -> ElementId:
    """Create a container from a standard container and assign the given elements to it.

    The container is sized to the bounding box of the elements (10 mm offset), aligned to the world
    axes, and is inserted and shown. All currently active elements are deactivated. The first
    standard container with a matching name is used.

    Parameters:
        element_id_list: IDs of the elements to put into the container; invalid IDs are skipped.
        output_name: Name given to the new container.
        standard_element_name: Name of the standard container to use.

    Returns:
        ID of the new container, or 0 if no standard container with that name exists.
    """

def create_auto_export_solid_from_standard_with_reference(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId
) -> ElementId:
    """Create an export solid from a standard export solid, oriented on a reference element.

    The export solid is sized to the bounding box of the elements (10 mm offset), aligned to the
    local axes of the reference element, and is inserted and shown. The standard element's
    properties are taken from the reference element. All currently active elements are deactivated.

    Parameters:
        element_id_list: IDs of the elements to put into the export solid; invalid IDs are skipped.
        output_name: Name for the new export solid. Currently not applied.
        standard_element_name: Name of the standard export solid to use.
        reference_id: ID of the reference element whose local X and Z axes orient the export solid;
            must exist.

    Returns:
        ID of the new export solid, or 0 if the standard export solid name is unknown or the
        reference element does not exist.
    """

def create_auto_container_from_standard_with_reference(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId
) -> ElementId:
    """Create a container from a standard container, oriented on a reference element.

    The container is sized to the bounding box of the elements (10 mm offset), aligned to the local
    axes of the reference element, and is inserted and shown. The standard element's properties are
    taken from the reference element. All currently active elements are deactivated.

    Parameters:
        element_id_list: IDs of the elements to put into the container; invalid IDs are skipped.
        output_name: Name for the new container. Currently not applied.
        standard_element_name: Name of the standard container to use.
        reference_id: ID of the reference element whose local X and Z axes orient the container;
            must exist.

    Returns:
        ID of the new container, or 0 if the standard container name is unknown or the reference
        element does not exist.
    """

def create_surface(surface_vertices: vertex_list) -> ElementId:
    """Create a surface element from a closed polygon of vertices.

    The polygon is closed automatically (do not repeat the first vertex). The new element is
    inserted and shown.

    Parameters:
        surface_vertices: Ordered corner points of the polygon; at least 3 are required.

    Examples:
        >>> # Create a rectangular surface
        >>> vertices = cadwork.vertex_list()
        >>> vertices.append(cadwork.point_3d(0., 0., 0.))
        >>> vertices.append(cadwork.point_3d(1000., 0., 0.))
        >>> vertices.append(cadwork.point_3d(1000., 800., 0.))
        >>> vertices.append(cadwork.point_3d(0., 800., 0.))
        >>> surface_id = ec.create_surface(vertices)

    Returns:
        ID of the new surface, or 0 if fewer than 3 vertices are given or the surface could not be
        built.
    """

def stretch_start_facet(element_id_list: list[ElementId], stretch_vector: point_3d) -> None:
    """Move the start face of linear elements such as beams and panels by a vector.

    Works on all elements with a beam-like cross-section along their axis (beams, panels, ...);
    elements without a start face, such as free volumes, and invalid IDs are left unchanged.
    Elements are modified in place; end types are kept and the element axis is updated.

    Parameters:
        element_id_list: IDs of the elements to stretch.
        stretch_vector: Displacement applied to the start face (direction and distance, mm).
    """

def stretch_end_facet(element_id_list: list[ElementId], stretch_vector: point_3d) -> None:
    """Move the end face of linear elements such as beams and panels by a vector.

    Works on all elements with a beam-like cross-section along their axis (beams, panels, ...);
    elements without an end face, such as free volumes, and invalid IDs are left unchanged. Elements
    are modified in place; end types are kept and the element axis is updated.

    Parameters:
        element_id_list: IDs of the elements to stretch.
        stretch_vector: Displacement applied to the end face (direction and distance, mm).
    """

def set_export_solid_contents(export_solid_id: ElementId, element_id_list: list[ElementId]) -> None:
    """Set the elements contained in an export solid.

    Does nothing if the export solid ID is invalid or is not an export solid. Invalid element IDs in
    the list are skipped.

    Parameters:
        export_solid_id: ID of the export solid.
        element_id_list: IDs of the elements to assign as its contents.
    """

def set_container_contents(container_id: ElementId, element_id_list: list[ElementId]) -> None:
    """Set the elements contained in a container.

    Does nothing if the container ID is invalid, is not a container, or is a container block.
    Invalid element IDs in the list are skipped.

    Parameters:
        container_id: ID of the container.
        element_id_list: IDs of the elements to assign as its contents.
    """

def set_parent_opening_variants_opening_angle(element_id_list: list[ElementId], angle: float) -> None:
    """Set the opening angle of opening elements that have a variant.

    Only opening elements with a variant are affected; all others and invalid IDs are skipped. The
    variant is recalculated.

    Parameters:
        element_id_list: IDs of the opening elements.
        angle: Opening angle to set (applied to the 2D, 3D and general opening angle).
    """

def mirror_move_elements(element_id_list: list[ElementId], plane: point_3d, plane_distance: float) -> None:
    """Mirror elements in place across a plane.

    Elements are modified in place (not copied). Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to mirror.
        plane: Normal vector of the mirror plane; pass a unit vector.
        plane_distance: Distance of the mirror plane from the global origin, measured along the
            normal (mm).
    """

def mirror_copy_elements(element_id_list: list[ElementId], plane: point_3d, plane_distance: float) -> list[ElementId]:
    """Create mirrored copies of elements across a plane.

    The originals are left unchanged. Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to copy and mirror.
        plane: Normal vector of the mirror plane; pass a unit vector.
        plane_distance: Distance of the mirror plane from the global origin, measured along the
            normal (mm).

    Returns:
        IDs of the new mirrored copies, in input order (originals not included). Empty list if no
        element was copied.
    """

def reset_element_cadwork_guid(element_id: ElementId) -> None:
    """Clear the cadwork GUID and IFC GUID of an element.

    Does nothing if the ID is invalid.

    Parameters:
        element_id: ID of the element.
    """

def create_standard_beam_points(
    standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard beam from a start point, an end point and a point defining its orientation.

    Length is the distance from first_point to second_point. The new beam is inserted and shown.
    Uses the first standard beam with a matching name.

    Parameters:
        standard_element_name: Name of the standard beam.
        first_point: Start point of the beam.
        second_point: End point of the beam; the direction first_point to second_point is the local
            X axis.
        third_point: Point whose direction from first_point defines the local Z direction.

    Examples:
        >>> std_beam_name = "Standard-Timber-120x240"  # Name as found in standard elements library
        >>> beam_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> beam_end_pt = cadwork.point_3d(0., 0., 3000.)
        >>> # Calculate orientation point
        >>> length_vector = (beam_end_pt - beam_start_pt).normalized()
        >>> ref_vector = cadwork.point_3d(1., 0., 0.)
        >>> orientation_vector = length_vector.cross(ref_vector).normalized()
        >>> orientation_pt = beam_start_pt + orientation_vector
        >>> std_beam_id = ec.create_standard_beam_points(std_beam_name, beam_start_pt, beam_end_pt, orientation_pt)

    Returns:
        ID of the new beam, or 0 if the name is unknown or the beam could not be created (for
        example zero length).
    """

def create_standard_beam_vectors(
    standard_element_name: str,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a standard beam from a start point, a length and local axis directions.

    The new beam is inserted and shown. Uses the first standard beam with a matching name.

    Parameters:
        standard_element_name: Name of the standard beam.
        length: Beam length in model units (mm); must be greater than 0.
        starting_point: Start point of the beam.
        x_local_direction: Direction of the beam axis (local X).
        z_local_direction: Local Z direction; must differ from x_local_direction.

    Examples:
        >>> std_beam_name = "Standard-Timber-100x100"  # Name as found in standard elements library
        >>> beam_length = 2500.
        >>> origin_point = cadwork.point_3d(100., 100., 100.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Orientation vector
        >>> std_beam_id = ec.create_standard_beam_vectors(std_beam_name, beam_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the new beam, or 0 if the name is unknown, the length is not positive, the two
        directions are identical or creation failed.
    """

def create_standard_panel_points(
    standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard panel from a start point, an end point and a point defining its
    orientation.

    Length is the distance from first_point to second_point. The new panel is inserted and shown.
    Uses the first standard panel with a matching name.

    Parameters:
        standard_element_name: Name of the standard panel.
        first_point: Start point (origin) of the panel.
        second_point: End point of the panel; the direction first_point to second_point is the local
            X axis.
        third_point: Point whose direction from first_point defines the local Z direction.

    Examples:
        >>> std_panel_name = "Standard-Panel-27mm"  # Name as found in standard elements library
        >>> panel_corner_pt = cadwork.point_3d(0., 0., 0.)
        >>> panel_width_pt = cadwork.point_3d(1200., 0., 0.)
        >>> # Calculate normal point for panel orientation (assuming Z is up)
        >>> panel_normal = cadwork.point_3d(0., 0., 1.)
        >>> orientation_pt = panel_corner_pt + panel_normal
        >>> std_panel_id = ec.create_standard_panel_points(std_panel_name, panel_corner_pt, panel_width_pt, orientation_pt)

    Returns:
        ID of the new panel, or 0 if the name is unknown or the panel could not be created (for
        example zero length).
    """

def create_standard_panel_vectors(
    standard_element_name: str,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a standard panel from a start point, a length and local axis directions.

    The new panel is inserted and shown. Uses the first standard panel with a matching name.

    Parameters:
        standard_element_name: Name of the standard panel.
        length: Panel length in model units (mm); must be greater than 0.
        starting_point: Start point (origin) of the panel.
        x_local_direction: Direction of the panel length (local X).
        z_local_direction: Local Z direction; must differ from x_local_direction.

    Examples:
        >>> std_panel_name = "Standard-Panel-20mm"  # Name as found in standard elements library
        >>> panel_length = 2400.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Panel normal direction
        >>> std_panel_id = ec.create_standard_panel_vectors(std_panel_name, panel_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the new panel, or 0 if the name is unknown, the length is not positive, the two
        directions are identical or creation failed.
    """

def create_standard_steel_points(
    standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard steel element from a start point, an end point and a point defining its
    orientation.

    Length is the distance from first_point to second_point. The new element is inserted and shown.
    If several profiles match, a European/American/British/Oceanic/Russian/Swiss profile is
    preferred.

    Parameters:
        standard_element_name: Name of the steel profile (cadwork notation).
        first_point: Start point of the element.
        second_point: End point of the element; the direction first_point to second_point is the
            local X axis.
        third_point: Point whose direction from first_point defines the local Z direction.

    Examples:
        >>> std_steel_name = "IPE 200"  # Name of standard steel profile from library
        >>> steel_start_pt = cadwork.point_3d(0., 0., 500.)
        >>> steel_end_pt = cadwork.point_3d(3000., 0., 500.)
        >>> # Calculate orientation point
        >>> length_vector = (steel_end_pt - steel_start_pt).normalized()
        >>> up_vector = cadwork.point_3d(0., 0., 1.)
        >>> side_vector = length_vector.cross(up_vector).normalized()
        >>> orientation_pt = steel_start_pt + up_vector
        >>> steel_id = ec.create_standard_steel_points(std_steel_name, steel_start_pt, steel_end_pt, orientation_pt)

    Returns:
        ID of the new element, or 0 if no profile matches the name or the element could not be
        created (for example zero length).
    """

def create_standard_steel_vectors(
    standard_element_name: str,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a standard steel element from a start point, a length and local axis directions.

    The new element is inserted and shown. If several profiles match, a
    European/American/British/Oceanic/Russian/Swiss profile is preferred.

    Parameters:
        standard_element_name: Name of the steel profile (cadwork notation).
        length: Element length in model units (mm); must be greater than 0.
        starting_point: Start point of the element.
        x_local_direction: Direction of the element axis (local X).
        z_local_direction: Local Z direction; must differ from x_local_direction.

    Examples:
        >>> std_steel_name = "HEA 220"  # Name of standard steel profile from library
        >>> steel_length = 4500.
        >>> origin_point = cadwork.point_3d(200., 0., 200.)
        >>> x_direction = cadwork.point_3d(0., 1., 0.)  # Direction along Y axis
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Up direction
        >>> steel_id = ec.create_standard_steel_vectors(std_steel_name, steel_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the new element, or 0 if no profile matches the name, the length is not positive, the
        two directions are identical or creation failed.
    """

def move_element_with_undo(element_id_list: list[ElementId], vector: point_3d) -> None:
    """Move elements by a vector as one undoable step.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to move.
        vector: Translation (direction and distance, mm).
    """

def create_normal_axis_points(first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a normal axis (line) between two points.

    The element is created with a fixed colour and added to the active scene.

    Parameters:
        first_point: Start point of the axis.
        second_point: End point of the axis.

    Examples:
        >>> axis_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> axis_end_pt = cadwork.point_3d(0., 0., 2000.)
        >>> axis_id = ec.create_normal_axis_points(axis_start_pt, axis_end_pt)

    Returns:
        ID of the new axis, or 0 on failure.
    """

def create_normal_axis_vectors(length: float, starting_point: point_3d, axis_direction: point_3d) -> ElementId:
    """Create a normal axis (line) from a start point, a direction and a length.

    The end point is starting_point + axis_direction * length; the direction is not normalized, so
    pass a unit vector. The element is created with a fixed colour and added to the active scene.

    Parameters:
        length: Length of the axis (mm), applied as a multiplier of axis_direction.
        starting_point: Start point of the axis.
        axis_direction: Direction of the axis; pass a unit vector.

    Examples:
        >>> axis_length = 1500.
        >>> axis_start_pt = cadwork.point_3d(200., 200., 0.)
        >>> axis_direction = cadwork.point_3d(1., 0., 0.)  # Direction along X axis
        >>> axis_id = ec.create_normal_axis_vectors(axis_length, axis_start_pt, axis_direction)

    Returns:
        ID of the new axis, or 0 on failure.
    """

def convert_bolt_to_standardconnector(element_id_list: list[ElementId], standard_element_name: str) -> None:
    """Convert bolts into a standard connector.

    The bolts are converted to connector axes in place. Does nothing if the standard connector name
    is unknown. Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the bolts to convert.
        standard_element_name: Name of the standard connector.
    """

def extrude_surface_to_auxiliary_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into an auxiliary element.

    The original surface is deleted and replaced by the new element, which inherits its properties
    and colour. Not added to undo.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface.
        vector: Extrusion direction and distance (mm); becomes the local X axis of the new element.

    Returns:
        ID of the new auxiliary element, or 0 if the element is not a surface or the extrusion
        failed.
    """

def extrude_surface_to_panel_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into a panel.

    The original surface is deleted and replaced by the new panel, which inherits its properties and
    colour. Not added to undo.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface.
        vector: Extrusion direction and distance (mm); becomes the local X axis of the new panel.

    Returns:
        ID of the new panel, or 0 if the element is not a surface or the extrusion failed.
    """

def extrude_surface_to_beam_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into a beam.

    The original surface is deleted and replaced by the new beam, which inherits its properties and
    colour. Not added to undo.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface.
        vector: Extrusion direction and distance (mm); becomes the length axis (local X) of the new
            beam.

    Returns:
        ID of the new beam, or 0 if the element is not a surface or the extrusion failed.
    """

def convert_container_to_container_block(element_id_list: list[ElementId]) -> None:
    """Convert containers into container blocks.

    Elements that are not containers and invalid IDs are skipped. The contained elements become part
    of the block.

    Parameters:
        element_id_list: IDs of the containers to convert.
    """

def create_bounding_box_local(reference_element: ElementId, element_id_list: list[ElementId]) -> ElementId:
    """Create a panel as bounding box of elements, aligned to a reference element's local axes.

    The box is created as a panel in the reference element's colour, inserted and shown. Elements
    without geometry are skipped.

    Parameters:
        reference_element: ID of the element whose origin and local axes orient the box; must exist
            and carry geometry.
        element_id_list: IDs of the elements to enclose.

    Returns:
        ID of the new bounding box panel, or 0 if the reference element is invalid, no valid element
        or body is given, or creation failed.
    """

def create_bounding_box_global(element_id_list: list[ElementId]) -> ElementId:
    """Create a panel as bounding box of elements, aligned to the global axes.

    The box is created as a panel with a fixed colour, inserted and shown. Elements without geometry
    are skipped.

    Parameters:
        element_id_list: IDs of the elements to enclose.

    Returns:
        ID of the new bounding box panel, or 0 if no valid element or body is given or creation
        failed.
    """

def convert_auxiliary_to_panel(element_id_list: list[ElementId]) -> None:
    """Convert auxiliary elements into panels.

    Elements are converted in place and keep their ID. Elements that are not auxiliary and invalid
    IDs are skipped.

    Parameters:
        element_id_list: IDs of the auxiliary elements to convert.
    """

def convert_auxiliary_to_beam(element_id_list: list[ElementId]) -> None:
    """Convert auxiliary elements into beams.

    Elements are converted in place and keep their ID; the auxiliary flag is removed. The shape is
    converted only for elements without a beam-like cross-section, so an auxiliary panel becomes a
    regular panel. Elements that are not auxiliary and invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the auxiliary elements to convert.
    """

def auto_set_rough_volume_situation(element_id_list: list[ElementId]) -> None:
    """Automatically determine the rough volume situation between elements.

    Pairs the given elements as rough volume partners. At least two valid elements are needed;
    otherwise nothing happens.

    Parameters:
        element_id_list: IDs of the elements to relate to each other.
    """

def rough_volume_situation_manual(
    cover: ElementId, add_partner: list[ElementId], remove_partner: list[ElementId]
) -> None:
    """Manually set rough volume partners of a cover element.

    Does nothing if the cover ID is invalid. Invalid IDs in the lists are skipped.

    Parameters:
        cover: ID of the cover element.
        add_partner: IDs of the partner elements to add.
        remove_partner: IDs of the partner elements to remove.
    """

def auto_set_parts_situation(element_id_list: list[ElementId]) -> None:
    """Automatically determine the parts situation for elements.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to process.
    """

def parts_situation_manual(cover: ElementId, add_childs: list[ElementId], remove_childs: list[ElementId]) -> None:
    """Manually set the child elements (parts) of a cover element.

    Does nothing if the cover ID is invalid. Added children are first detached from any previous
    cover. Invalid IDs in the lists are skipped.

    Parameters:
        cover: ID of the cover element.
        add_childs: IDs of the elements to add as children of the cover.
        remove_childs: IDs of the elements to remove from their cover.
    """

def activate_rv_without_situation() -> list[ElementId]:
    """Activate all cover elements that have no rough volume situation.

    The found elements become active.

    Returns:
        IDs of the activated elements. Empty list if there are none.
    """

def activate_parts_without_situation() -> list[ElementId]:
    """Activate all elements that have no parts situation.

    The found elements become active.

    Returns:
        IDs of the activated elements. Empty list if there are none.
    """

def add_elements_to_detail(element_id_list: list[ElementId], detail: int) -> None:
    """Assign elements to an element-module detail group.

    Only works in the drawing file all.3dc; otherwise nothing happens. Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to assign.
        detail: Detail group number: 0 none, 1 angle, 2 area, 3 cross, 4 edge, 5 end, 6 line, 7
            open, 8 T, 9 floor area, 10 floor end, 11 floor line, 12 floor open.
    """

def subtract_elements_with_undo(
    hard_element_id_list: list[ElementId], soft_element_id_list: list[ElementId], with_undo: bool
) -> list[ElementId]:
    """Subtract the volume of hard elements from soft elements (boolean difference).

    Soft elements are cut in place and keep their IDs; hard elements are not modified. Invalid IDs
    are skipped.

    Parameters:
        hard_element_id_list: IDs of the cutter elements.
        soft_element_id_list: IDs of the elements to be cut.
        with_undo: If True, the operation is added to the undo stack.

    Returns:
        IDs of the elements newly created by the operation (for example when a soft element is split
        into several volumes). Empty list if nothing was created or the operation failed.
    """

def create_linear_optimization(
    element_id_list: list[ElementId],
    optimization_number: int,
    total_length: float,
    start_cut: float,
    end_cut: float,
    saw_kerf: float,
    is_production_list: bool,
) -> ElementId:
    """Create a linear optimization bar (nesting raw part) holding the given elements in order.

    The elements are laid out in list order along the bar, starting start_cut from its start, each
    followed by saw_kerf. The bar takes its cross-section and material from the first element and is
    added to the matching nesting group (created if missing). The bar element is hidden.

    Parameters:
        element_id_list: IDs of the elements placed on the bar, in order; invalid IDs are skipped.
        optimization_number: Number of the optimization bar.
        total_length: Total length of the bar (mm).
        start_cut: Length cut off at the start of the bar before the first element (mm).
        end_cut: Length cut off at the end of the bar (mm); only reduces the remaining length.
        saw_kerf: Saw kerf between consecutive elements (mm).
        is_production_list: Currently ignored; the list type follows the global cadwork setting.

    Returns:
        ID of the created bar element, or 0 if no valid element is given.
    """

def start_element_module_calculation_silently(covers: list[ElementId]) -> None:
    """Run the element module calculation for cover elements without user interaction.

    Does nothing if the element module licence is not available. Only cover elements in the list are
    processed; they are activated during the calculation and deactivated afterwards. Invalid IDs are
    skipped.

    Parameters:
        covers: IDs of the cover elements to calculate.
    """

def replace_physical_drillings_with_drilling_axes(
    element_id_list: list[ElementId], mininum_diameter: float, maximum_diameter: float
) -> list[ElementId]:
    """Replace drillings in beams, panels and other linear elements with drilling axes (bolt
    elements).

    Works on all elements with a beam-like cross-section (beams, panels, ...); other elements are
    skipped. Drillings whose diameter lies in the given range are removed from the element and
    replaced by new axis elements, which are inserted and shown. All active elements are
    deactivated. If the two diameters are swapped they are reordered.

    Parameters:
        element_id_list: IDs of the elements to process.
        mininum_diameter: Smallest drilling diameter to replace (mm); must not be negative.
        maximum_diameter: Largest drilling diameter to replace (mm); must not be negative.

    Returns:
        IDs of the new drilling axis elements. Empty list if nothing was replaced, no valid element
        was given or a diameter is negative.
    """

def cut_element_with_processing_group(soft_element: ElementId, processing: ElementId) -> None:
    """Cut an element with a processing group.

    Does nothing if either ID is invalid. The element is modified in place.

    Parameters:
        soft_element: ID of the element to be cut.
        processing: ID of the processing group that performs the cut.
    """

def add_element_to_detail(element_id_list: list[ElementId], detail: int) -> None:
    """Assign elements to an element-module detail group.

    Only works in the drawing file all.3dc; otherwise nothing happens. Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to assign.
        detail: Detail group number: 0 none, 1 angle, 2 area, 3 cross, 4 edge, 5 end, 6 line, 7
            open, 8 T, 9 floor area, 10 floor end, 11 floor line, 12 floor open.
    """

def convert_elements_to_auxiliary_elements(element_id_list: list[ElementId]) -> None:
    """Convert elements into auxiliary elements.

    Elements are converted in place and keep their ID; panels are converted to beams first. Invalid
    IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to convert.
    """

def create_circular_axis_points(diameter: float, first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a circular axis (round bar axis) between two points.

    The element is added to the active scene.

    Parameters:
        diameter: Diameter of the circular axis (mm).
        first_point: Start point of the axis.
        second_point: End point of the axis.

    Examples:
        >>> axis_diameter = 50.
        >>> axis_start_pt = cadwork.point_3d(100., 100., 0.)
        >>> axis_end_pt = cadwork.point_3d(100., 100., 300.)
        >>> circular_axis_id = ec.create_circular_axis_points(axis_diameter, axis_start_pt, axis_end_pt)

    Returns:
        ID of the new axis, or 0 on failure.
    """

def create_circular_axis_vector(
    diameter: float, length: float, starting_point: point_3d, axis_direction: point_3d
) -> ElementId:
    """Create a circular axis (round bar axis) from a start point, a direction and a length.

    The end point is starting_point + axis_direction * length; the direction is not normalized, so
    pass a unit vector. The element is added to the active scene.

    Parameters:
        diameter: Diameter of the circular axis (mm).
        length: Length of the axis (mm), applied as a multiplier of axis_direction.
        starting_point: Start point of the axis.
        axis_direction: Direction of the axis; pass a unit vector.

    Examples:
        >>> axis_diameter = 60.
        >>> axis_length = 400.
        >>> axis_start_pt = cadwork.point_3d(200., 200., 200.)
        >>> axis_direction = cadwork.point_3d(0., 1., 0.)  # Direction along Y axis
        >>> circular_axis_id = ec.create_circular_axis_vector(axis_diameter, axis_length, axis_start_pt, axis_direction)

    Returns:
        ID of the new axis, or 0 on failure.
    """

def create_polygon_panel(
    polygon_vertices: vertex_list, thickness: float, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a panel by extruding a 3D polygon along its own face normal.

    The extrusion direction is the polygon's face normal (right-hand rule over the vertex order),
    not z_local_direction; reversing the vertex order flips the panel. The polygon plane lies at
    mid-thickness. The last vertex in the list is dropped and the loop is closed automatically, so
    repeat the first vertex at the end. The panel is inserted and shown.

    Parameters:
        polygon_vertices: Corner points of the polygon in world coordinates; they must be coplanar
            and enclose a non-zero area.
        thickness: Extrusion distance along the face normal (mm).
        x_local_direction: Only labels the local X axis of the new panel; does not steer the
            extrusion.
        z_local_direction: Only labels the local Z axis of the new panel; does not steer the
            extrusion.

    Examples:
        >>> # Create a hexagonal panel
        >>> vertices = cadwork.vertex_list()
        >>> import math
        >>> radius = 500.
        >>> sides = 6
        >>> for i in range(sides):
        ...     angle = 2 * math.pi * i / sides
        ...     vertices.append(cadwork.point_3d(radius * math.cos(angle), radius * math.sin(angle), 0.))
        >>> vertices.append(vertices[0]) # Close the polygon
        >>> panel_thickness = 20.
        >>> extrusion_vector = cadwork.point_3d(0., 0., 1.)  # Normal direction
        >>> z_vector = cadwork.point_3d(1., 0., 0.)  # Orientation vector
        >>> polygon_panel_id = ec.create_polygon_panel(vertices, panel_thickness, extrusion_vector, z_vector)

    Returns:
        ID of the new panel, or 0 if fewer than 3 vertices are given, the polygon is not planar or
        creation failed.
    """

def create_polygon_panel_vectors(
    polygon_vertices: list[point_2d | tuple[float, float]],
    thickness: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a panel from a 2D outline in the panel's local plane, extruded along its normal.

    The outline lies in the local X/Y plane of the panel and is extruded along the local Z axis from
    the starting point (not centered). The outline is closed automatically (do not repeat the first
    vertex) and may be given in either winding order. The panel is inserted and shown.

    Parameters:
        polygon_vertices: Outline vertices as point_2d or (u, v) tuples; u runs along the local X
            axis, v along the local Y axis, (0, 0) is the starting point. At least 3 vertices with
            non-zero area.
        thickness: Panel thickness, i.e. the extrusion length along local Z (mm); must be greater
            than 0.
        starting_point: 3D position of the outline origin (u=0, v=0).
        x_local_direction: Local X axis direction; must not be zero.
        z_local_direction: Hint for the local Z side; the Y axis is derived as Z cross X and Z is
            then made perpendicular. Must not be parallel to x_local_direction.

    Examples:
        >>> # Create a hexagonal panel from a 2D profile
        >>> import math
        >>> radius = 500.
        >>> sides = 6
        >>> profile = [cadwork.point_2d(radius * math.cos(2 * math.pi * i / sides), radius * math.sin(2 * math.pi * i / sides)) for i in range(sides)]
        >>> panel_thickness = 20.
        >>> start_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Local X: profile u axis
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Local Z: panel normal / extrusion direction
        >>> polygon_panel_id = ec.create_polygon_panel_vectors(profile, panel_thickness, start_point, x_direction, z_direction)

    Returns:
        ID of the new panel, or 0 if the outline is invalid (fewer than 3 points, zero area),
        thickness is not positive, a direction is zero or the two directions are parallel, or
        creation failed.
    """

def cut_elements_with_overmeasure(hard_element_id_list: list[ElementId], soft_element_id_list: list[ElementId]) -> None:
    """Cut soft elements with hard elements, applying an overmeasure.

    Invalid IDs are skipped. Does nothing if either list ends up empty, or if none of the hard
    elements has overmeasure settings. A settings dialog or query may appear and must be accepted
    for the cut to run.

    Parameters:
        hard_element_id_list: Element IDs of the cutting (hard) elements.
        soft_element_id_list: IDs of the elements to be cut (soft elements).
    """

def cut_log_corner_joint(settings_name: str, element_id_list: list[ElementId]) -> None:
    """Cut a log corner joint on elements using a named settings preset.

    Invalid IDs are skipped. Marks the elements as modified and refreshes the display. The settings
    name is not validated by the API.

    Parameters:
        settings_name: Name of the log corner joint settings to use.
        element_id_list: Element IDs of the log beams to cut.
    """

def get_edge_selection(element_id_list: list[ElementId]) -> edge_list:
    """Let the user pick edges of the given elements and return them.

    Interactive: waits for the user to select edges in the 3D view (restricted to the edges of the
    given elements) and confirm. Invalid IDs are skipped. Returns an empty list if the user presses
    Esc or selects nothing.

    Parameters:
        element_id_list: Element IDs whose edges may be selected.

    Returns:
        The selected edges, each given by its start point and end point. Empty if cancelled or
        nothing was selected.
    """

def get_facets_with_lasso(element_id_list: list[ElementId]) -> facet_list:
    """Let the user pick faces of the given elements and return them as facets.

    Interactive: waits for the user to select faces in the 3D view (restricted to the faces of the
    given elements) and confirm. Invalid IDs are skipped. Returns an empty list if the user presses
    Esc or selects nothing.

    Parameters:
        element_id_list: Element IDs whose faces may be selected.

    Returns:
        The selected faces, each as the list of vertices of its outer boundary (curves are
        discretized into segments). Empty if cancelled or nothing was selected.
    """

def create_standard_element_from_guid_points(
    guid: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard element from its GUID, placed by three points.

    The GUID identifies the standard element unambiguously, unlike its name. Folders of the standard
    element library are not handled by the API. The new element is inserted and shown. Returns 0 on
    failure (unknown GUID, or first and second point coincide).

    Parameters:
        guid: GUID of the standard element.
        first_point: Start point of the element; origin of its local coordinate system.
        second_point: Defines the length and the local X axis: the length is the distance from
            first_point to second_point, and X points from first_point towards it.
        third_point: Defines the local Z axis direction: Z points from first_point towards this
            point.

    Returns:
        The ID of the created element, or 0 on failure.
    """

def create_standard_element_from_guid_vectors(
    guid: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a standard element from its GUID, placed by a start point and directions.

    The GUID identifies the standard element unambiguously, unlike its name. Folders of the standard
    element library are not handled by the API. The new element is inserted and shown. Returns 0 on
    failure (unknown GUID, length of zero or less, or identical X and Z directions).

    Parameters:
        guid: GUID of the standard element.
        length: Length of the element along its local X axis, in mm. Must be greater than 0.
        starting_point: Start point of the element; origin of its local coordinate system.
        x_local_direction: Direction of the local X axis (length axis).
        z_local_direction: Direction of the local Z axis. Must differ from x_local_direction.

    Returns:
        The ID of the created element, or 0 on failure.
    """

def fillet_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, radius: float) -> None:
    """Round an edge of an element with a fillet.

    The edge is found by exact match of its two end points (in either order); if no edge matches, or
    the operation fails, nothing happens and no error is reported. Invalid element ID is silently
    ignored.

    Parameters:
        element_id: ID of the element that owns the edge.
        edge_start: One end point of the edge, in global coordinates.
        edge_end: The other end point of the edge, in global coordinates.
        radius: Fillet radius in mm.
    """

def chamfer_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, length: float) -> None:
    """Bevel an edge of an element with a 45 degree chamfer.

    The edge is found by exact match of its two end points (in either order); if no edge matches, or
    the operation fails, nothing happens and no error is reported. Invalid element ID is silently
    ignored.

    Parameters:
        element_id: ID of the element that owns the edge.
        edge_start: One end point of the edge, in global coordinates.
        edge_end: The other end point of the edge, in global coordinates.
        length: Chamfer length in mm.
    """

def convert_drilling_to_circular_beam(element_id_list: list[ElementId]) -> None:
    """Replace elements with circular beams.

    Each element's machining data is deleted first (a confirmation may be requested from the user),
    then it is replaced by a cylindrical beam of the same start point, length and orientation, with
    diameter equal to the element's height. Colour and other properties are copied; the original
    element is deleted. Invalid IDs are skipped.

    Parameters:
        element_id_list: Element IDs of the drilling elements to convert.
    """

def convert_lines_to_surfaces(element_id_list: list[ElementId]) -> list[ElementId]:
    """Convert closed line (axis) elements into surface elements.

    Invalid IDs are skipped. New surfaces are inserted and shown, and the operation is added to
    undo. The source elements are not described as deleted by the API.

    Parameters:
        element_id_list: Element IDs of the line elements to convert.

    Returns:
        The IDs of the newly created surface elements. Empty list if the conversion failed or
        produced nothing.
    """

def convert_surfaces_to_volume(element_id_list: list[ElementId]) -> ElementId:
    """Create one volume (solid) element from a set of surface elements.

    Invalid IDs are skipped. The new volume is inserted and shown. The surfaces must form a closed
    shell; otherwise nothing is created and 0 is returned.

    Parameters:
        element_id_list: Element IDs of the surface elements that enclose the volume.

    Returns:
        The ID of the created volume element, or 0 on failure.
    """

def cut_corner_lap(
    element_id_list: list[ElementId],
    depth: float,
    clearance_base: float,
    clearance_side: float,
    backcut: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a corner lap joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped;
    nothing happens if no partners are found. All dimensions are in mm.

    Parameters:
        element_id_list: IDs of the elements to join; they must meet in a corner.
        depth: Depth of the lap cut in each element.
        clearance_base: Extra clearance at the bottom of the cut.
        clearance_side: Extra clearance at the side faces of the cut.
        backcut: Undercut applied to the outer face of the cut.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def cut_t_lap(
    element_id_list: list[ElementId],
    depth: float,
    clearance_base: float,
    clearance_side: float,
    backcut: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a T lap joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped;
    nothing happens if no partners are found. All dimensions are in mm.

    Parameters:
        element_id_list: IDs of the elements to join; one element ends against the side of another.
        depth: Depth of the lap cut where the intersecting element is placed.
        clearance_base: Extra clearance at the bottom of the cut.
        clearance_side: Extra clearance at the side faces of the cut.
        backcut: Undercut applied to improve fitting.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def cut_cross_lap(
    element_id_list: list[ElementId],
    depth: float,
    clearance_base: float,
    clearance_side: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a cross lap joint between crossing linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped;
    nothing happens if no partners are found. All dimensions are in mm.

    Parameters:
        element_id_list: IDs of the crossing elements.
        depth: Depth of the lap cut in each element, typically half the element thickness.
        clearance_base: Extra clearance at the bottom of the cut.
        clearance_side: Extra clearance at the side walls of the cut.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def delete_processes_keep_cutting_bodies(
    element_id_list: list[ElementId], keep_cutting_elements_only: bool
) -> list[ElementId]:
    """Remove machining processes from elements and keep their cutting bodies as elements.

    Works like Ctrl+D in cadwork. Invalid IDs are skipped. A confirmation may be requested from the
    user before machine data is deleted. The display is refreshed.

    Parameters:
        element_id_list: Element IDs to remove processes from.
        keep_cutting_elements_only: If True, only bodies of cutting elements are kept and
            returned; if False, all removed process geometry is kept.

    Returns:
        The IDs of the cutting body elements that were created. Empty list if there were none.
    """

def cut_double_tenon(
    element_id_list: list[ElementId],
    depth1: float,
    depth2: float,
    clearance: float,
    backcut: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a double tenon joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped.
    All dimensions are in mm.

    Parameters:
        element_id_list: IDs of the elements to join.
        depth1: Depth of the first tenon shoulder.
        depth2: Depth of the second tenon shoulder.
        clearance: Extra clearance around the tenons.
        backcut: Undercut applied to avoid surface interference.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def get_coordinate_system_data_nesting_child(
    nesting_parent_id: ElementId, nesting_child_id: ElementId
) -> coordinate_system_data:
    """Get the placement of a nested child element inside its nesting parent.

    Returns an empty coordinate_system_data if either ID is invalid or the child is not nested in
    that parent.

    Parameters:
        nesting_parent_id: ID of the nesting parent (raw part).
        nesting_child_id: ID of the nested child element.

    Returns:
        A coordinate_system_data with three points: the child's origin (point 1), a point along its
        length axis at the child's length from the origin (point 2), and a point one unit along its
        Z axis from the origin (point 3). Empty on failure.
    """

def cut_half_lap(
    element_id_list: list[ElementId],
    length: float,
    clearance_length: float,
    clearance_depth: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a half lap joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped.
    All dimensions are in mm.

    Parameters:
        element_id_list: IDs of the elements to join.
        length: Length of the half lap along the element axis.
        clearance_length: Extra clearance along the length of the cut.
        clearance_depth: Extra clearance in the depth direction.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def cut_simple_scarf(
    element_id_list: list[ElementId],
    length: float,
    depth: float,
    clearance_length: float,
    clearance_depth: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a simple scarf joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped.
    All dimensions are in mm. Machine data of the elements is deleted first (a confirmation may be
    requested) and the cut is added to undo.

    Parameters:
        element_id_list: IDs of the elements to join end to end.
        length: Distance between the two starting points of the cut.
        depth: Depth of the initial straight cut before the diagonal cut begins.
        clearance_length: Extra length clearance applied along the initial (depth) cut.
        clearance_depth: Extra depth clearance applied along the diagonal cut.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def cut_diagonal_cut(
    element_id_list: list[ElementId],
    length: float,
    clearance_length: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a diagonal (mitre-like) cut joint between linear elements (beams, panels, ...).

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped.
    All dimensions are in mm. Machine data of the elements is deleted first (a confirmation may be
    requested) and the cut is added to undo.

    Parameters:
        element_id_list: IDs of the elements to join end to end.
        length: Length of the diagonal cut along the element.
        clearance_length: Extra clearance along the cut length.
        drilling_count: Number of drill holes for fasteners.
        drilling_diameter: Diameter of each drill hole.
        drilling_tolerance: Extra tolerance added to the hole size.
    """

def get_all_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all elements in the model.

    Excludes permanently hidden elements.

    Returns:
        List of element IDs; empty if the model has none.
    """

def get_visible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all currently visible elements.

    Ignores graphical objects that exist only for IFC import.

    Returns:
        List of element IDs; empty if none are visible.
    """

def get_invisible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all currently invisible elements.

    Returns:
        List of element IDs; empty if none.
    """

def get_active_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all active (selected) elements.

    Also includes active container blocks and containers whose contents are active.

    Returns:
        List of element IDs; empty if nothing is active.
    """

def get_inactive_all_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all inactive elements, visible or not.

    Excludes permanently hidden elements.

    Returns:
        List of element IDs; empty if none.
    """

def get_inactive_visible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all elements that are visible but not active.

    Ignores graphical objects that exist only for IFC import. The returned list may be padded at the
    end with 0 values; ignore (filter out) any ID equal to 0.

    Returns:
        List of element IDs, possibly followed by trailing 0 entries; empty if none.
    """

def check_if_point_is_in_element(point: point_3d, element_id: ElementId) -> bool:
    """Check whether a point lies inside an element's body.

    Returns False for an invalid element ID. A point exactly on the surface is not inside; use
    check_if_point_is_on_element for that.

    Parameters:
        point: Point to test, in global coordinates.
        element_id: ID of the element to test against.

    Returns:
        True if the point is strictly inside the element, otherwise False.
    """

def check_if_point_is_on_element(point: point_3d, element_id: ElementId) -> bool:
    """Check whether a point lies on the surface of an element.

    Returns False for an invalid element ID.

    Parameters:
        point: Point to test, in global coordinates.
        element_id: ID of the element to test against.

    Returns:
        True if the point is on the element's surface, otherwise False (also if inside or outside).
    """

def get_element_contact_facets(first_id: ElementId, second_id: ElementId) -> facet_list:
    """Get the faces where two elements touch each other.

    Returns an empty list if an ID is invalid, an element has no body, or the elements do not touch.
    The reason is written to the API log only.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Returns:
        The contact faces as facets; empty if none.
    """

def get_element_raw_interface_vertices(first_id: ElementId, second_id: ElementId) -> list[point_3d]:
    """Get the corner points of the interface where two elements clash.

    Vertices are collected from the intersection of the clashing faces of the two bodies, without
    duplicates. The result is empty if the elements do not interpenetrate or touch. Both IDs must be
    valid.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Returns:
        List of unique interface points in global coordinates; empty if none.
    """

def get_standard_export_solid_list() -> list[str]:
    """Get the names of all standard export solids.

    Names are in the current cadwork language.

    Returns:
        List of standard export solid names.
    """

def get_standard_container_list() -> list[str]:
    """Get the names of all standard containers.

    Names are in the current cadwork language.

    Returns:
        List of standard container names.
    """

def get_standard_beam_list() -> list[str]:
    """Get the names of all standard beams.

    Names are not unique, only GUIDs are, so the list can contain the same name several times.
    Folders of the standard element library are not handled by the API and are not part of the
    names. Use `get_standard_beam_guid_list` to identify standard beams unambiguously.

    Returns:
        List of standard beam names.
    """

def get_standard_panel_list() -> list[str]:
    """Get the names of all standard panels.

    Names are not unique, only GUIDs are, so the list can contain the same name several times.
    Folders of the standard element library are not handled by the API and are not part of the
    names. Use `get_standard_panel_guid_list` to identify standard panels unambiguously.

    Returns:
        List of standard panel names.
    """

def get_variant_sibling_element_ids(element_id: ElementId) -> list[ElementId]:
    """Get the IDs of all elements that belong to the same variant as an element.

    Returns an empty list if the ID is invalid or the element is not part of a variant.

    Parameters:
        element_id: ID of an element that belongs to a variant.

    Returns:
        List of element IDs of the variant; empty if none.
    """

def get_reference_element(element_id: ElementId) -> ElementId:
    """Get the reference element of an element.

    Returns 0 for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        The ID of the reference element, or 0 if the element ID is invalid.
    """

def get_element_contact_vertices(first_id: ElementId, second_id: ElementId) -> list[point_3d]:
    """Get the corner points of the faces where two elements touch.

    Returns an empty list if an ID is invalid, an element has no body, or the elements do not touch.
    The reason is written to the API log only.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Returns:
        List of contact points in global coordinates, for all touching face pairs together
        (duplicates possible); empty if none.
    """

def get_nesting_parent_id(element_id: ElementId) -> ElementId:
    """Get the nesting parent (raw part) of a nested element.

    For a panel this is its nesting parent; for any other element it is its linear optimization
    parent (raw beam). Returns 0 if the ID is invalid or the element is not nested.

    Parameters:
        element_id: ID of the nested element.

    Returns:
        The ID of the parent element, or 0 if none.
    """

def check_if_elements_are_in_collision(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check whether two elements overlap each other.

    Returns False if an ID is invalid or an element is a point cloud, caddy object or graphical
    object. Merely touching elements are not a collision; use check_if_elements_are_in_contact for
    that. The reason for False is written to the API log.

    Parameters:
        first_element_id: ID of the first element.
        second_element_id: ID of the second element.

    Returns:
        True if the elements overlap (including one containing or coinciding with the other),
        otherwise False.
    """

def check_if_elements_are_in_contact(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check whether two elements touch each other.

    Returns False if an ID is invalid or an element is a point cloud, caddy object or graphical
    object. The reason for False is written to the API log.

    Parameters:
        first_element_id: ID of the first element.
        second_element_id: ID of the second element.

    Returns:
        True if the elements are in contact, otherwise False.
    """

def get_element_module_properties_for_element(element_id: ElementId) -> element_module_properties:
    """Get the element module (detail) properties of an element.

    Returns a properties object with all flags unset if the element ID is invalid.

    Parameters:
        element_id: ID of the element.

    Returns:
        The element_module_properties of the element (only the properties that are set on it are
        filled in).
    """

def get_element_type_description(element_id: ElementId) -> str:
    """Get the localized type description of an element.

    Returns an empty string for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        The element type description (e.g. beam, panel) in the current cadwork language; empty
        string if the ID is invalid.
    """

def get_opening_variant_ids(element_id_list: list[ElementId], opening_type: int) -> list[int]:
    """Get the variant IDs of window or door variants used by the given elements.

    Elements that are not part of a variant are skipped, as are invalid IDs. Each variant appears at
    most once.

    Parameters:
        element_id_list: Element IDs to look at.
        opening_type: Opening type to keep: 0 = unknown, 1 = window, 2 = door.

    Returns:
        List of variant IDs (not element IDs) whose opening type matches; empty if none.
    """

def get_parent_container_id(element_id: ElementId) -> ElementId:
    """Get the container that holds an element.

    Returns 0 if the ID is invalid or the element is not in a container.

    Parameters:
        element_id: ID of the element.

    Returns:
        The ID of the parent container, or 0 if none.
    """

def get_export_solid_content_elements(element_id: ElementId) -> list[ElementId]:
    """Get the elements contained in an export solid.

    Returns an empty list if the ID is invalid or the element has no children.

    Parameters:
        element_id: ID of the export solid element.

    Returns:
        List of IDs of the child elements; empty if none.
    """

def get_container_content_elements(element_id: ElementId) -> list[ElementId]:
    """Get the elements contained in a container.

    Returns an empty list if the ID is invalid or the element has no children.

    Parameters:
        element_id: ID of the container element.

    Returns:
        List of IDs of the child elements; empty if none.
    """

def get_element_detail_path() -> str:
    """Get the folder path where element module (detail) files are stored.

    Returns:
        The element detail path of the current document.
    """

def get_element_cadwork_guid(element_id: ElementId) -> str:
    """Get the cadwork GUID of an element.

    If the element has no GUID yet, a new one is created and assigned to it. Returns an empty string
    for an invalid element ID.

    Parameters:
        element_id: ID of the element.

    Returns:
        The GUID as a string, or an empty string if the ID is invalid.
    """

def get_bounding_box_vertices_local(reference_element: ElementId, element_id_list: list[ElementId]) -> list[point_3d]:
    """Get the corner points of the bounding box of elements, aligned to a reference element.

    The box is aligned with the local axes of the reference element, not with the world axes.
    Returns an empty list if the reference element ID is invalid, no element ID in the list is
    valid, or the box cannot be computed. The reason is written to the API log only.

    Parameters:
        reference_element: ID of the element whose local coordinate system orients the box.
        element_id_list: Element IDs to enclose.

    Returns:
        The 8 corner points of the box; empty list on failure.
    """

def get_bounding_box_vertices_global(element_id_list: list[ElementId]) -> list[point_3d]:
    """Get the corner points of the bounding box of elements, aligned to the world axes.

    Returns an empty list if no element ID in the list is valid or the box cannot be computed. The
    reason is written to the API log only.

    Parameters:
        element_id_list: Element IDs to enclose.

    Returns:
        The 8 corner points of the box; empty list on failure.
    """

def get_all_nesting_raw_parts() -> list[ElementId]:
    """Get the IDs of all nesting raw parts in the model.

    Returns:
        List of element IDs of the raw parts; empty if there are none.
    """

def get_joined_elements(element_id: ElementId) -> list[ElementId]:
    """Get the elements that are joined (grouped) with an element.

    The given element is included in the result. Returns an empty list if the ID is invalid.

    Parameters:
        element_id: ID of the element.

    Returns:
        List of element IDs of the group, including element_id; empty if the ID is invalid.
    """

def check_element_duplicates(element_id_list: list[ElementId]) -> list[ElementId]:
    """Find elements that are exact geometric duplicates of other elements in the list.

    Only visible elements are checked. Two elements count as duplicates when they have the same
    geometry at the same position; of each such pair only the element with the higher ID is
    reported, so the originals are not in the result. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to compare with each other.

    Returns:
        List of element IDs of the duplicates, without repeats. Empty list if none are found.
    """

def get_elements_in_contact(element_id: ElementId) -> list[ElementId]:
    """Get the elements that are in contact with an element.

    Returns an empty list if the element ID is invalid.

    Parameters:
        element_id: ID of the element to check.

    Returns:
        List of IDs of the elements in contact with the element. Empty list if there are none.
    """

def create_text_object_with_options(
    position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, text_options: text_object_options
) -> ElementId:
    """Create a 3D text object from a set of text options.

    The text is built from one element per letter, placed and shown in the model. Both direction
    vectors are normalized internally; the local Y axis is derived from them.

    Parameters:
        position: Origin of the text object in global coordinates.
        x_local_direction: Direction of the text baseline (local X axis).
        z_local_direction: Local Z axis of the text, i.e. the direction the text faces; should be
            perpendicular to x_local_direction.
        text_options: Text content, font, height and other settings.

    Examples:
        >>> text_position = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Text direction
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Text orientation
        >>> options = cadwork.text_object_options()
        >>> options.set_text("Advanced Text")
        >>> options.set_height(200.)
        >>> options.set_font_name("Verdana")
        >>> options.set_bold(True)
        >>> text_id = ec.create_text_object_with_options(text_position, x_direction, z_direction, options)

    Returns:
        ID of the last letter element of the created text, or 0 if the text could not be created.
    """

def convert_surfaces_to_roof_surfaces(element_id_list: list[ElementId], roof_name: str) -> None:
    """Convert surface elements to roof surfaces of a named roof.

    Elements that are neither surfaces nor roof surfaces are skipped, as are invalid IDs. The
    converted surfaces are assigned to the group named roof_name (created if needed). If all given
    elements are already roof surfaces, nothing is converted. A new coordinate system may be set up
    for the roof.

    Parameters:
        element_id_list: List of surface element IDs to convert.
        roof_name: Name of the roof; also used as the group name of the converted surfaces.
    """

def start_standard_element_dialog(standard_element_type: standard_element_type) -> str:
    """Open the standard element selection dialog and return the chosen element.

    Blocks until the user closes the dialog.

    Parameters:
        standard_element_type: Kind of standard element to choose from (beam, panel, vba, export
            solid, container or metal).

    Returns:
        GUID of the selected standard element in braces, or an empty string if nothing was selected.
    """

def remove_standard_connector_axis(guid: str) -> None:
    """Delete a standard connector axis from the standard element library.

    Parameters:
        guid: GUID of the standard connector axis, in braces.
    """

def remove_standard_beam(guid: str) -> None:
    """Delete a standard beam from the standard element library.

    Parameters:
        guid: GUID of the standard beam, in braces.
    """

def remove_standard_panel(guid: str) -> None:
    """Delete a standard panel from the standard element library.

    Parameters:
        guid: GUID of the standard panel, in braces.
    """

def remove_standard_container(guid: str) -> None:
    """Delete a standard container from the standard element library.

    Parameters:
        guid: GUID of the standard container, in braces.
    """

def remove_standard_export_solid(guid: str) -> None:
    """Delete a standard export solid from the standard element library.

    Parameters:
        guid: GUID of the standard export solid, in braces.
    """

def get_user_element_ids_with_count(count: int) -> list[ElementId]:
    """Let the user pick elements interactively and return their IDs.

    Blocks until the user has finished selecting. Any element type can be picked. If the user
    presses Esc, the elements picked so far (possibly none) are returned.

    Parameters:
        count: Maximum number of elements the user may select.

    Returns:
        List of the selected element IDs. Empty list if nothing was selected.
    """

def cut_scarf_straight(
    element_id_list: list[ElementId],
    length: float,
    depth: float,
    clearance_length: float,
    clearance_depth: float,
    clearance_hook: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a straight lengthwise scarf joint on the given elements.

    Existing machining on the elements is deleted first. The operation is added to undo. Invalid IDs
    are skipped.

    Parameters:
        element_id_list: List of element IDs to cut.
        length: Total length of the scarf joint along the element axis.
        depth: Depth of the vertical cut where the two sides meet.
        clearance_length: Extra clearance in the length direction.
        clearance_depth: Extra clearance in the depth direction.
        clearance_hook: Extra clearance at the hook of the joint.
        drilling_count: Number of holes (e.g. for bolts or dowels) to drill through the joint; 0 for
            none.
        drilling_diameter: Diameter of each hole.
        drilling_tolerance: Tolerance added to the hole diameter.
    """

def cut_scarf_diagonal(
    element_id_list: list[ElementId],
    length: float,
    depth: float,
    clearance_length: float,
    clearance_depth: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a diagonal lengthwise scarf joint on the given elements.

    Existing machining on the elements is deleted first. The operation is added to undo. Invalid IDs
    are skipped.

    Parameters:
        element_id_list: List of element IDs to cut.
        length: Total length of the scarf joint along the element axis.
        depth: Depth of the straight section before the diagonal cut begins.
        clearance_length: Extra clearance in the length direction.
        clearance_depth: Extra clearance in the depth direction.
        drilling_count: Number of holes (e.g. for bolts or dowels) to drill through the joint; 0 for
            none.
        drilling_diameter: Diameter of each hole.
        drilling_tolerance: Tolerance added to the hole diameter.
    """

def cut_scarf_with_wedge(
    element_id_list: list[ElementId],
    length: float,
    depth: float,
    clearance_length: float,
    clearance_depth: float,
    wedge_width: float,
    drilling_count: UnsignedInt,
    drilling_diameter: float,
    drilling_tolerance: float,
) -> None:
    """Cut a diagonal lengthwise scarf joint with a wedge on the given elements.

    Existing machining on the elements is deleted first. The operation is added to undo. Invalid IDs
    are skipped.

    Parameters:
        element_id_list: List of element IDs to cut.
        length: Total length of the scarf joint along the element axis.
        depth: Depth of the straight section before the diagonal cut begins.
        clearance_length: Extra clearance in the length direction.
        clearance_depth: Extra clearance in the depth direction.
        wedge_width: Width of the wedge.
        drilling_count: Number of holes (e.g. for bolts or dowels) to drill through the joint; 0 for
            none.
        drilling_diameter: Diameter of each hole.
        drilling_tolerance: Tolerance added to the hole diameter.
    """

def cut_beam_end_profile(
    element_id_list: list[ElementId], profile_name: str, on_start_face: bool, on_end_face: bool
) -> None:
    """Apply a named end profile to the start and/or end face of elements such as beams and panels.

    The profile is looked up by name in the profile library; if no profile has that name, nothing
    changes. Invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the elements to modify.
        profile_name: Name of the end profile, matched exactly (compared in natural sort order).
        on_start_face: True to apply the profile on the start face of each element.
        on_end_face: True to apply the profile on the end face of each element.
    """

def create_truncated_cone_beam_points(
    start_diameter: float, end_diameter: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a round beam that tapers from a start to an end diameter, defined by points.

    The beam axis runs from first_point to second_point. The local X axis is the direction
    first_point to second_point and the local Z axis points from first_point toward third_point; if
    the two are collinear the orientation is chosen automatically. The beam is inserted and shown.

    Parameters:
        start_diameter: Diameter at first_point.
        end_diameter: Diameter at second_point.
        first_point: Start point of the beam axis.
        second_point: End point of the beam axis.
        third_point: Point that sets the local Z orientation; direction from first_point to this
            point.

    Examples:
        >>> start_dia = 200.
        >>> end_dia = 150.
        >>> cone_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> cone_end_pt = cadwork.point_3d(0., 0., 3000.)
        >>> # Calculate orientation point
        >>> length_vector = (cone_end_pt - cone_start_pt).normalized()
        >>> ref_vector = cadwork.point_3d(1., 0., 0.)
        >>> orientation_vector = length_vector.cross(ref_vector).normalized()
        >>> orientation_pt = cone_start_pt + orientation_vector
        >>> cone_id = ec.create_truncated_cone_beam_points(start_dia, end_dia, cone_start_pt, cone_end_pt, orientation_pt)

    Returns:
        ID of the created beam, or 0 on failure.
    """

def create_truncated_cone_beam_vectors(
    start_diameter: float,
    end_diameter: float,
    length: float,
    starting_point: point_3d,
    x_local_direction: point_3d,
    z_local_direction: point_3d,
) -> ElementId:
    """Create a round beam that tapers from a start to an end diameter, defined by vectors.

    The beam axis runs from starting_point along x_local_direction for the given length. If
    x_local_direction and z_local_direction are collinear the orientation is chosen automatically.
    The beam is inserted and shown.

    Parameters:
        start_diameter: Diameter at starting_point.
        end_diameter: Diameter at the far end of the beam.
        length: Length of the beam along x_local_direction.
        starting_point: Start point of the beam axis.
        x_local_direction: Direction of the beam axis (local X axis); should be a unit vector, since
            it is multiplied by length.
        z_local_direction: Direction of the local Z axis.

    Examples:
        >>> start_dia = 120.
        >>> end_dia = 80.
        >>> cone_length = 2500.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(0., 0., 1.)  # Direction along Z axis
        >>> z_direction = cadwork.point_3d(1., 0., 0.)  # Orientation vector
        >>> cone_id = ec.create_truncated_cone_beam_vectors(start_dia, end_dia, cone_length, origin_point, x_direction, z_direction)

    Returns:
        ID of the created beam, or 0 on failure.
    """

def create_spline_line(spline_points: vertex_list) -> ElementId:
    """Create a spline line through a list of points.

    The line is inserted and shown. At least two points are required.

    Parameters:
        spline_points: Points the spline passes through, in order.

    Examples:
        >>> # Create a spline through multiple points
        >>> points = cadwork.vertex_list()
        >>> points.append(cadwork.point_3d(0., 0., 0.))
        >>> points.append(cadwork.point_3d(500., 200., 0.))
        >>> points.append(cadwork.point_3d(1000., 0., 200.))
        >>> points.append(cadwork.point_3d(1500., -100., 100.))
        >>> spline_id = ec.create_spline_line(points)

    Returns:
        ID of the created spline line, or 0 if fewer than two points are given.
    """

def unjoin_elements(element_id_list: list[ElementId]) -> bool:
    """Dissolve the join groups of the given elements completely.

    Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs whose join groups are to be dissolved.

    Returns:
        True if the groups were split successfully, False otherwise.
    """

def unjoin_top_level_elements(element_id_list: list[ElementId]) -> bool:
    """Dissolve only the top-level join group of the given elements.

    Nested groups inside the top-level group remain joined. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs whose top-level join group is to be dissolved.

    Returns:
        True if the group was split successfully, False otherwise.
    """

def set_element_group_single_select_mode() -> None:
    """Make single elements of a group selectable.

    Changes the program-wide selection mode, which also affects interactive selection.
    """

def set_element_group_multi_select_mode() -> None:
    """Select all elements of a group when one of them is selected.

    Changes the program-wide selection mode, which also affects interactive selection.
    """

def convert_circular_beam_to_drilling(element_id_list: list[ElementId]) -> None:
    """Replace circular beams with drilling elements.

    Machine data on the beams is deleted first, which may ask the user for confirmation. Each beam
    is replaced by a new drilling element with the same dimensions and properties, so the original
    element IDs become invalid. Invalid IDs are skipped.

    Parameters:
        element_id_list: List of circular beam element IDs to convert.
    """

def slice_elements_with_plane_and_get_new_elements(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> list[ElementId]:
    """Slice an element with a plane and return the newly created elements.

    The plane consists of all points p with dot(p, normal) = distance_from_global_origin. The
    operation is added to undo.

    Parameters:
        element_id: ID of the element to slice (volume or surface).
        cut_plane_normal_vector: Normal vector of the cutting plane; use a unit vector.
        distance_from_global_origin: Signed distance of the plane from the global origin along the
            normal, in model units (mm).

    Examples:
        >>> import math
        >>> # Create a beam to slice
        >>> beam_width = 150.
        >>> beam_height = 300.
        >>> beam_length = 4000.
        >>> beam_id = ec.create_rectangular_beam_vectors(beam_width, beam_height, beam_length,
        ...                                            cadwork.point_3d(0., 0., 0.),
        ...                                            cadwork.point_3d(1., 0., 0.),
        ...                                            cadwork.point_3d(0., 0., 1.))
        >>> # Define a vertical cutting plane through the middle of the beam
        >>> plane_normal = cadwork.point_3d(1., 0., 0.)  # Normal vector points along X-axis
        >>> # A point on the plane (midpoint of the beam)
        >>> plane_point = cadwork.point_3d(beam_length/2., 0., 0.)
        >>> distance = plane_point.dot(plane_normal)  # Distance from origin to plane
        >>> # Verify with additional points on the plane
        >>> test_point = cadwork.point_3d(beam_length/2., 100., 200.)
        >>> on_plane = abs(test_point.dot(plane_normal) - distance) < 0.001
        >>> print(f"Test point is on plane: {on_plane}")
        >>> # Slice the beam at the midpoint and get the resulting pieces
        >>> new_element_ids = ec.slice_elements_with_plane_and_get_new_elements(beam_id, plane_normal, distance)
        >>> print(f"Created {len(new_element_ids)} new element_id_list: {new_element_ids}")
        >>> # Visualization: different pen colors for the new elements
        >>> for i, new_id in enumerate(new_element_ids):
        ...     vc.set_color([new_id], i+5)

    Returns:
        List of IDs of the elements created by the cut. Empty list if the plane does not cut the
        element.
    """

def get_elements_in_collision(element_id: ElementId) -> list[ElementId]:
    """Get the elements that collide with an element.

    Narrower than get_elements_in_contact: only elements that overlap, are contained in, or coincide
    with the element are returned, not those that merely touch. Returns an empty list if the element
    ID is invalid.

    Parameters:
        element_id: ID of the element to check.

    Returns:
        List of IDs of the colliding elements. Empty list if there are none.
    """

def get_text_object_options(element_id: ElementId) -> 'text_object_options':
    """Get the text options of a text object.

    element_id must be the ID of a text object element, as returned by
    create_text_object_with_options.

    Parameters:
        element_id: ID of the text object element.

    Returns:
        The text options (content, font, height, ...) of the text object.
    """

def get_is_element_group_single_select_mode() -> bool:
    """Check whether single elements of a group are selectable.

    Returns:
        True if single-select mode is active, False if the whole group is selected together.
    """

def get_is_element_group_multi_select_mode() -> bool:
    """Check whether selecting an element selects its whole group.

    Returns:
        True if multi-select mode is active, False if single-select mode is active.
    """

def set_shoulder_options(options: shoulder_options) -> None:
    """Set the options used by subsequent cut_shoulder calls.

    The options replace the current shoulder cut settings of the program. If the end type name in
    the options is not found, no end type is assigned.

    Parameters:
        options: Shoulder cut options.
    """

def set_heel_shoulder_options(options: heel_shoulder_options) -> None:
    """Set the options used by subsequent cut_heel_shoulder calls.

    The options replace the current heel shoulder cut settings of the program. If the end type name
    in the options is not found, no end type is assigned.

    Parameters:
        options: Heel shoulder cut options.
    """

def set_double_shoulder_options(options: double_shoulder_options) -> None:
    """Set the options used by subsequent cut_double_shoulder calls.

    The options replace the current double shoulder cut settings of the program.

    Parameters:
        options: Double shoulder cut options.
    """

def cut_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut shoulder joints using the current shoulder options.

    Set the options first with set_shoulder_options. Invalid IDs are skipped. Both lists are marked
    as modified.

    Parameters:
        element_id_list: List of element IDs to cut.
        connecting_element_id_list: List of the connecting (counterpart) element IDs that determine
            the cut geometry.
    """

def cut_heel_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut heel shoulder joints using the current heel shoulder options.

    Set the options first with set_heel_shoulder_options. Invalid IDs are skipped. Both lists are
    marked as modified.

    Parameters:
        element_id_list: List of element IDs to cut.
        connecting_element_id_list: List of the connecting (counterpart) element IDs that determine
            the cut geometry.
    """

def cut_double_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut double shoulder joints using the current double shoulder options.

    Set the options first with set_double_shoulder_options. Invalid IDs are skipped. Both lists are
    marked as modified.

    Parameters:
        element_id_list: List of element IDs to cut.
        connecting_element_id_list: List of the connecting (counterpart) element IDs that determine
            the cut geometry.
    """

def filter_elements(element_id_list: list[ElementId], element_filter: element_filter) -> list[ElementId]:
    """Return the elements of a list that match an element filter.

    Text filters (name, group, subgroup, comment, user attribute, SKU) match the complete value
    exactly. Part and production number filters match the number. Invalid IDs are skipped; a filter
    with no criterion returns an empty list.

    Parameters:
        element_id_list: List of element IDs to filter.
        element_filter: Filter that defines the attribute and the value to match.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_element_filter = cadwork.element_filter()
        >>> your_element_filter.set_name("beam")
        >>> filtered_elements = ec.filter_elements(ec.get_active_identifiable_element_ids(), your_element_filter)
        >>> print(filtered_elements)

    Returns:
        List of the element IDs that pass the filter, in input order. Empty list if none match.
    """

def map_elements(element_id_list: list[ElementId], map_query: element_map_query) -> dict[str, list[ElementId]]:
    """Group the elements of a list by an attribute value.

    Elements are grouped by the attribute selected in the query (name, group, subgroup, comment,
    user attribute, SKU, production number, part number, building or storey). Numbers are used as
    text keys. Elements with an empty attribute value are grouped under the empty string. Invalid
    IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to group.
        map_query: Query that defines the attribute to group by.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_map_query = cadwork.element_map_query()
        >>> your_map_query.set_by_subgroup()
        >>> mapped_items = ec.map_elements(ec.get_active_identifiable_element_ids(), your_map_query)
        >>> print(mapped_items)

    Returns:
        Dictionary mapping each attribute value to the list of element IDs having that value. Empty
        dictionary if there is nothing to map.
    """

def cast_ray_and_get_element_intersections(
    element_id_list: list[ElementId], ray_start_position: point_3d, ray_end_position: point_3d, radius: float
) -> hit_result:
    """Cast a ray through the model and get the intersection points per element.

    Only the segment from ray_start_position to ray_end_position is tested, and only against the
    given elements. Intersection points lie on the ray centre line.

    Parameters:
        element_id_list: List of element IDs to test against the ray.
        ray_start_position: Start point of the ray in global coordinates.
        ray_end_position: End point of the ray; sets the direction and the maximum length.
        radius: Radius of the ray cylinder in model units (mm); allows testing against a volume
            instead of a thin line.

    Examples:
        >>> import element_controller as ec
        >>> from cadwork import point_3d
        >>> ray_start = point_3d(0, 0, 0)
        >>> ray_end = point_3d(1000, 0, 0)
        >>> hits = ec.cast_ray_and_get_element_intersections(ec.get_active_identifiable_element_ids(), ray_start, ray_end, 40.0)
        >>> print(hits.get_hit_element_ids())
        >>> for element in hits.get_hit_element_ids():
        ...     print(f"ElementID {element}: {hits.get_hit_vertices_by_element(element)}")
        ...     for pos in hits.get_hit_vertices_by_element(element):
        ...         ec.create_node(pos)

    Returns:
        A hit_result with the IDs of the elements hit and, per element ID, the list of hit points.
        Empty if nothing is hit.
    """

def get_element_active_point(element_id: ElementId) -> active_point_result:
    """Get the active (snapped) point if it belongs to the given element.

    The active point is the point currently picked or highlighted by the user in the 3D view. It is
    only returned if that point lies on the given element; otherwise has_point is False.

    Parameters:
        element_id: ID of the element the active point must belong to.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> result = ec.get_element_active_point(element_id)
        >>> if result:
        ...     ec.create_node(result.point)
        ... else:
        ...     print("No active point set for element.")

    Returns:
        An active_point_result with has_point and point attributes. It evaluates to False when there
        is no active point for the element; point is then (0, 0, 0).
    """

def get_standard_beam_guid_list() -> list[str]:
    """Get the GUIDs of all standard beams.

    Returns:
        List of GUID strings. Empty list if there are none.
    """

def get_standard_panel_guid_list() -> list[str]:
    """Get the GUIDs of all standard panels.

    Returns:
        List of GUID strings. Empty list if there are none.
    """

def import_standard_beam_from_file(file_path: str) -> None:
    """Import standard beams from a file into the standard element library.

    If the file does not exist, nothing is imported and an error is logged. Entries that already
    exist in the library are ignored.

    Parameters:
        file_path: Full path of the file to import.
    """

def import_standard_panel_from_file(file_path: str) -> None:
    """Import standard panels from a file into the standard element library.

    If the file does not exist, nothing is imported and an error is logged. Entries that already
    exist in the library are ignored.

    Parameters:
        file_path: Full path of the file to import.
    """

def export_as_standard_element(element_id: ElementId, name: str) -> str:
    """Export an existing element as a new standard element.

    Make sure no standard element with this name exists first (see
    get_standard_element_guid_from_name); otherwise a count suffix such as (2) is appended to the
    name. Read the final name with get_standard_element_name_from_guid. Library folders are not
    supported; to order entries, use separators in the name, e.g. Walls - Exterior - 160mm. Metal
    elements are not supported.

    Parameters:
        element_id: ID of the element to export.
        name: Name of the new standard element.

    Returns:
        GUID of the new standard element, or an empty string if the element ID is invalid, the
        element type is unsupported or the export failed.
    """

def create_rotation_element(
    surface_element_id: ElementId, axis_point: point_3d, axis_direction: point_3d, angle_rad: float, segmentation: int
) -> ElementId:
    """Create a solid by rotating a surface element around an axis.

    The source surface is left unchanged. The new element is flagged as auxiliary. Returns 0 if the
    element is not a surface or the angle is outside the allowed range.

    Parameters:
        surface_element_id: ID of the surface element to rotate.
        axis_point: A point on the rotation axis.
        axis_direction: Direction of the rotation axis.
        angle_rad: Rotation angle in radians; must be between 1 degree (about 0.0175) and 360
            degrees (2*pi).
        segmentation: Number of division steps for the rotation; 0 creates a smooth solid, values
            above 0 a faceted one.

    Examples:
        >>> import math
        >>> # Create a rectangular surface and rotate it 360° around an axis to form a cylinder
        >>> radius = 200.0
        >>> height = 1000.0
        >>> # Define a rectangular surface profile in the XZ plane
        >>> vertices = cadwork.vertex_list()
        >>> vertices.append(cadwork.point_3d(0.0, 0.0, 0.0))
        >>> vertices.append(cadwork.point_3d(0.0, 0.0, height))
        >>> vertices.append(cadwork.point_3d(radius, 0.0, height))
        >>> vertices.append(cadwork.point_3d(radius, 0.0, 0.0))
        >>> surface_id = ec.create_surface(vertices)
        >>> # Rotate the surface 360° around the Z axis to create a cylinder
        >>> axis_point = cadwork.point_3d(0.0, 0.0, 0.0)
        >>> axis_direction = cadwork.point_3d(0.0, 0.0, 1.0)
        >>> full_rotation = 2.0 * math.pi  # 360 degrees
        >>> discretization_steps = 0  # automatic
        >>> cylinder_id = ec.create_rotation_element(surface_id, axis_point, axis_direction, full_rotation, discretization_steps)

    Returns:
        ID of the created element, or 0 on failure.
    """

def apply_image_to_surface(
    element: ElementId, image_file_path: str, alignment_start: point_3d, alignment_end: point_3d
) -> bool:
    """Apply an image as texture to a surface element.

    The image is placed on the surface using the two alignment points. Returns False without changes
    if the element is not a valid surface, the file path is invalid, or the two points are
    identical.

    Parameters:
        element: ID of the surface element.
        image_file_path: Full path of the image file (.jpg, .png, .bmp or .tif).
        alignment_start: First alignment point for placing the image on the surface.
        alignment_end: Second alignment point; must differ from alignment_start.

    Returns:
        True if the image was applied, False otherwise.
    """

def create_line_from_segments(segments: list[element_segment]) -> ElementId:
    """Create a line element from straight, arc and spline segments.

    The first entry must be of type straight and only gives the start point. Each later entry
    continues from the previous end point: straight draws a straight line to position; arc draws an
    arc ending at position and passing through support_position; consecutive spline entries are
    joined into one spline through their positions. The line is inserted and shown.

    Parameters:
        segments: Ordered list of at least two element_segment entries.

    Returns:
        ID of the created line, or 0 if there are fewer than two entries or the first entry is not
        straight.
    """

def get_line_segments(element_id: ElementId) -> list[element_segment]:
    """Get the segments that define a line element.

    The first entry (type straight) is the start point; each following entry is the end point of one
    straight or arc segment, or a spline point. Arc entries carry a point on the arc in
    support_position. Can be passed to create_line_from_segments to rebuild the line.

    Parameters:
        element_id: ID of the line element.

    Returns:
        List of element_segment entries. Empty list if the ID is invalid, the element is not a line,
        or the line contains an edge that is not straight, circular or a spline.
    """

def create_spline_from_surfaces(surface_ids: list[ElementId], order: spline_surface_order, no_twist: bool) -> ElementId:
    """Create a spline volume by skinning a series of surface elements.

    Works like the Spline command of the user interface. The sections are sorted internally
    according to order. The volume is inserted and shown; the surfaces are left unchanged.

    Parameters:
        surface_ids: IDs of the section surfaces; at least two, all must be surface elements.
        order: Linear if the sections are arranged along a run, circular if they are arranged around
            a centre.
        no_twist: True to keep the skin from twisting between consecutive sections.

    Returns:
        ID of the created volume, or 0 if fewer than two IDs are given, an ID is not a surface, or
        the geometry cannot be skinned.
    """

def create_spline_from_surface_and_line(surface_id: ElementId, line_id: ElementId) -> ElementId:
    """Create a spline volume by sweeping a surface element along a line element.

    The volume is inserted and shown; the surface and the line are left unchanged.

    Parameters:
        surface_id: ID of the section surface; must be a surface element.
        line_id: ID of the path; must be a line element.

    Returns:
        ID of the created volume, or 0 if surface_id is not a surface, line_id is not a line, or the
        sweep fails.
    """

def get_standard_element_guid_from_name(name: str, type: standard_element_type) -> str:
    """Get the GUID of a standard element from its name.

    The name is matched in the current cadwork language. If several standard elements share the
    name, the first match is returned; this is the one the create_standard_* functions use for that
    name. Steel profile names use cadwork notation.

    Parameters:
        name: Name of the standard element.
        type: Kind of standard element to search: beam, panel, vba, export solid, container or metal
            (steel).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> guid = ec.get_standard_element_guid_from_name("KVH 60x120", cadwork.standard_element_type.beam)
        >>> if guid:
        ...     print(f"GUID: {guid}")

    Returns:
        GUID in braces, e.g. {1B4E28BA-2FA1-11D2-883F-0016D3CCA427}, or an empty string if the name
        is empty or no standard element of that kind has this name.
    """

def get_standard_element_name_from_guid(guid: str) -> str:
    """Get the name of a standard element from its GUID.

    Works for every kind of standard element, including steel profiles. The name is returned in the
    current cadwork language.

    Parameters:
        guid: GUID of the standard element, in braces, e.g. {1B4E28BA-2FA1-11D2-883F-0016D3CCA427}.

    Examples:
        >>> import element_controller as ec
        >>> for guid in ec.get_standard_beam_guid_list():
        ...     name = ec.get_standard_element_name_from_guid(guid)
        ...     print(f"{guid}: {name}")

    Returns:
        Name of the standard element, or an empty string if the GUID is malformed or unknown.
    """
