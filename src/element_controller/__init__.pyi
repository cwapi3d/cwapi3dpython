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
    """Delete elements permanently, without an undo step.

    Removes the elements from the model. Nothing is registered on the undo stack, so
    `element_controller.make_undo()` cannot bring them back; use
    `element_controller.delete_elements_with_undo()` for a deletion the user can undo. IDs that do
    not exist (or were already deleted) are skipped, and an empty list does nothing.

    Parameters:
        element_id_list: Element IDs to delete, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.delete_elements(element_ids)
    """

def join_elements(element_id_list: list[ElementId]) -> None:
    """Join elements into one group.

    Groups the given elements the same way as the join command in the cadwork 3D user interface, so
    they are selected and moved together afterwards. Existing groups of the given elements are
    merged into the new group; use `element_controller.join_top_level_elements()` to keep them as
    sub-groups. A yes/no confirmation may be shown to the user, and problems (for example a single
    element, or elements that are already in the same group) are reported in the command bar instead
    of raising an error. Reverse with `element_controller.split_elements()`. IDs that do not exist
    are skipped.

    Parameters:
        element_id_list: Element IDs to join (at least two), e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     ec.join_elements(element_ids)
    """

def join_top_level_elements(element_id_list: list[ElementId]) -> None:
    """Join the top-level groups of elements into one group.

    Like `element_controller.join_elements()`, but joins at one level only: groups that the given
    elements already belong to are kept as sub-groups of the new group instead of being merged into
    it. A yes/no confirmation may be shown to the user, which blocks the script until answered. IDs
    that do not exist are skipped. Reverse with `element_controller.split_elements()`.

    Parameters:
        element_id_list: Element IDs whose top-level groups are joined, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     ec.join_top_level_elements(element_ids)
    """

def create_rectangular_beam_points(
    width: float, height: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a rectangular beam from three points.

    Builds a beam whose axis runs from first_point to second_point, so its length is the distance
    between them. The orientation of the cross-section is taken from third_point. The new element is
    inserted into the model, shown, assigned to the active scene and building storey, and the
    display is refreshed (unless auto refresh is disabled with
    `utility_controller.disable_auto_display_refresh()`). Give the beam a name and other attributes
    afterwards with the `attribute_controller` setters.

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

    Builds a round beam whose axis runs from first_point to second_point, so its length is the
    distance between them. third_point only fixes the rotational orientation of the beam about its
    axis. The new element is inserted into the model, shown, assigned to the active scene and
    building storey, and the display is refreshed (unless auto refresh is disabled with
    `utility_controller.disable_auto_display_refresh()`).

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

    Builds a beam with a square cross-section whose axis runs from first_point to second_point, so
    its length is the distance between them. third_point fixes the orientation of the cross-section.
    The new element is inserted into the model, shown, assigned to the active scene and building
    storey, and the display is refreshed (unless auto refresh is disabled with
    `utility_controller.disable_auto_display_refresh()`).

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

    The beam extends from starting_point along x_local_direction for the given length;
    z_local_direction fixes the orientation of the cross-section. Unlike
    `element_controller.create_rectangular_beam_points()` the length is given explicitly, and the
    directions are passed on as given (not computed from points). The new element is inserted into
    the model, shown, assigned to the active scene and building storey, and the display is
    refreshed.

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

    The beam extends from starting_point along x_local_direction for the given length.
    z_local_direction only fixes the rotational orientation about the beam axis, which has no
    visible effect on the round cross-section but sets the local axes of the element. The new
    element is inserted into the model, shown, assigned to the active scene and building storey, and
    the display is refreshed.

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

    The beam extends from starting_point along x_local_direction for the given length;
    z_local_direction fixes the orientation of the square cross-section. The new element is inserted
    into the model, shown, assigned to the active scene and building storey, and the display is
    refreshed.

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

    Builds a panel whose length runs from first_point to second_point, so it equals the distance
    between them. third_point defines the thickness direction (the panel normal). The new element is
    inserted into the model, shown, assigned to the active scene and building storey, and the
    display is refreshed (unless auto refresh is disabled with
    `utility_controller.disable_auto_display_refresh()`).

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

    The panel extends from starting_point along x_local_direction for the given length;
    z_local_direction is the thickness direction (panel normal). The new element is inserted into
    the model, shown, assigned to the active scene and building storey, and the display is
    refreshed.

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
    It is created as a free drilling (bolt-type element) in the model, not cut into any other
    element. It is assigned to the active scene and building storey and the display is refreshed.

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
    internally, so a non-unit vector changes the drilling length. It is created as a free drilling
    in the model, assigned to the active scene and building storey, and the display is refreshed.
    Use `element_controller.create_drilling_points()` when both end points are known.

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
    """Create a line element between two points.

    Creates a line element running from first_point to second_point. Lines are helper geometry
    without a cross-section; turn one into a marking line with
    `element_controller.set_line_to_marking_line()` if needed. The new line is assigned to the
    active scene and building storey and the display is refreshed.

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
    """Create a line element from a start point, direction and length.

    The end point is starting_point + line_direction * length. The direction is not normalized
    internally, so a non-unit vector changes the line length. The new line is assigned to the active
    scene and building storey and the display is refreshed. Use
    `element_controller.create_line_points()` when both end points are known.

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
    """Create a node element at a position.

    Creates a normal node (a point element) at node_position. The new node is assigned to the active
    scene and building storey and the display is refreshed.

    Parameters:
        node_position: Position of the node in mm.

    Examples:
        >>> node_position = cadwork.point_3d(250., 250., 100.)
        >>> node_id = ec.create_node(node_position)

    Returns:
        ID of the created node, or 0 if creation failed.
    """

def solder_elements(element_id_list: list[ElementId]) -> list[ElementId]:
    """Solder elements together where possible.

    Solders the given elements that are eligible, like the solder command in the user interface.
    Elements that cannot be soldered are left unchanged and are ignored, as are IDs that do not
    exist. The operation is not registered as an undo step by this function.

    Parameters:
        element_id_list: Element IDs to solder, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> soldered_ids = ec.solder_elements(element_ids)
        >>> print(len(soldered_ids), 'soldered elements')

    Returns:
        List of IDs of the soldered elements as reported by the soldering operation; empty if
        nothing was soldered.
    """

def convert_beam_to_panel(element_id_list: list[ElementId]) -> None:
    """Convert beams to panels in place.

    Replaces the geometry of each element by the equivalent panel representation; the element keeps
    its ID. Successfully converted elements are deactivated, so re-activate them if the script
    continues to work on them. Elements that cannot be converted are left unchanged, and IDs that do
    not exist are skipped. The display is refreshed unless auto refresh is disabled. Reverse with
    `element_controller.convert_panel_to_beam()`.

    Parameters:
        element_id_list: IDs of the beams to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_beam_to_panel(element_ids)
        >>> converted = [i for i in element_ids if ac.is_panel(i)]
    """

def convert_panel_to_beam(element_id_list: list[ElementId]) -> None:
    """Convert panels to beams in place.

    Replaces the geometry of each element by the equivalent beam representation; the element keeps
    its ID. Successfully converted elements are deactivated, so re-activate them if the script
    continues to work on them. Elements that cannot be converted are left unchanged, and IDs that do
    not exist are skipped. The display is refreshed unless auto refresh is disabled. Reverse with
    `element_controller.convert_beam_to_panel()`.

    Parameters:
        element_id_list: IDs of the panels to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_panel_to_beam(element_ids)
        >>> converted = [i for i in element_ids if ac.is_beam(i)]
    """

def delete_all_element_end_types(element_id_list: list[ElementId]) -> None:
    """Remove all end types from elements.

    Deletes every end type from each element, leaving the plain end. Elements without end types and
    IDs that do not exist are skipped. This function does not register an undo step and does not
    refresh the display.

    Parameters:
        element_id_list: Element IDs to clear, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.delete_all_element_end_types(element_ids)
    """

def delete_all_element_processes(element_id_list: list[ElementId]) -> None:
    """Remove all processes (machining) from elements.

    Deletes every process attached to each element, such as drillings, cuts and other machining
    operations. IDs that do not exist are skipped. This function does not register an undo step and
    does not refresh the display.

    Parameters:
        element_id_list: Element IDs to clear, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.delete_all_element_processes(element_ids)
    """

def move_element(element_id_list: list[ElementId], move_vector: point_3d) -> None:
    """Move elements by a vector.

    Translates every element in place by move_vector; the elements keep their IDs. IDs that do not
    exist are skipped. The move is not registered on the undo stack (use
    `element_controller.move_element_with_undo()` for that), and the display is refreshed unless
    auto refresh is disabled. Use `element_controller.copy_elements()` to leave the originals in
    place.

    Parameters:
        element_id_list: Element IDs to move, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        move_vector: Displacement applied to every element, in mm (world axes).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.move_element(element_ids, cadwork.point_3d(1000., 0., 0.))
    """

def create_polygon_beam(
    polygon_vertices: vertex_list, thickness: float, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a beam by extruding a 3D polygon along its face normal.

    The polygon is closed automatically and must be planar. It is extruded along its own face normal
    (derived from the vertex order, right-hand rule), and the polygon plane ends up in the middle of
    the beam. x_local_direction and z_local_direction only label the local axes of the new beam;
    they do not steer the extrusion. Prefer `element_controller.create_polygon_beam_vectors()`,
    which is independent of vertex order. Failures return 0 and no error message is recorded.

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
        x_local_direction: Direction of the beam axis; the extrusion follows it. Must not be the
            zero vector or parallel to z_local_direction.
        z_local_direction: Orientation hint for the local Z axis; need not be exactly perpendicular
            to x_local_direction, but must not be the zero vector or parallel to it.

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
    x_local_direction. Use `element_controller.create_text_object_with_font()` to choose another
    font. The letters are assigned to the active scene and building storey and the display is
    refreshed.

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

    The originals are not changed. IDs that do not exist are skipped. Group, container and variant
    assignments are copied. The copies are assigned to the active building storey, unless the user's
    copy settings say to keep the storey of the originals. The copy is not registered as an undo
    step. The display is refreshed unless auto refresh is disabled.

    Parameters:
        element_id_list: Element IDs to copy, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        copy_vector: Offset of the copies relative to the originals, in mm (world axes).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> copy_ids = ec.copy_elements(element_ids, cadwork.point_3d(0., 2000., 0.))
        >>> print(len(copy_ids), 'copies created')

    Returns:
        List of IDs of the new copies only (the originals are not included); empty if nothing was
        copied.
    """

def rotate_elements(
    element_id_list: list[ElementId], origin: point_3d, rotation_axis: point_3d, rotation_angle: float
) -> None:
    """Rotate elements around an axis.

    Rotates every element in place about the axis through origin with direction rotation_axis; the
    elements keep their IDs. If rotation_axis has zero length, a message is printed in the command
    bar and nothing is rotated; an angle of 0 also changes nothing. IDs that do not exist are
    skipped. The rotation is not registered on the undo stack, and the display is refreshed unless
    auto refresh is disabled.

    Parameters:
        element_id_list: Element IDs to rotate, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        origin: Point the rotation axis passes through, in mm.
        rotation_axis: Direction of the rotation axis; must not be the zero vector.
        rotation_angle: Rotation angle in radians; use `math.radians()` to convert from degrees.

    Examples:
        >>> import math
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> origin = cadwork.point_3d(0., 0., 0.)
        >>> z_axis = cadwork.point_3d(0., 0., 1.)
        >>> ec.rotate_elements(element_ids, origin, z_axis, math.radians(90.))
    """

def subtract_elements(hard_elements: list[ElementId], soft_elements: list[ElementId]) -> list[ElementId]:
    """Subtract the volume of hard elements from soft elements (boolean difference).

    Cuts the soft elements with the hard elements, like the cut command in the user interface. Soft
    elements are changed in place and keep their IDs; hard elements are not modified. If a soft
    element falls apart into several disconnected pieces, the extra pieces become new elements. The
    operation is added to the undo stack as one step only if the cut succeeds. IDs that do not exist
    are skipped. See `element_controller.subtract_elements_with_undo()` for a variant with an
    explicit undo flag.

    Parameters:
        hard_elements: IDs of the cutting elements, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        soft_elements: IDs of the elements to be cut.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     cutter_ids = element_ids[:1]
        ...     new_piece_ids = ec.subtract_elements(cutter_ids, element_ids[1:])
        ...     print(len(new_piece_ids), 'new pieces')

    Returns:
        List of IDs of additional elements created when a soft element is split into several
        disconnected pieces; does not include the IDs in soft_elements. Empty if nothing was split
        or the operation failed.
    """

def check_element_id(element_id: ElementId) -> bool:
    """Check whether an element with the given ID exists.

    Looks the ID up in the current model. Use it before working with an ID that may be stale, for
    example one stored earlier in the script or read from a file after elements were deleted.
    Visibility and activation do not matter, only whether the element exists. The invalid ID 0 never
    exists.

    Parameters:
        element_id: Element ID to check.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> existing_ids = [i for i in element_ids if ec.check_element_id(i)]
        >>> print(ec.check_element_id(0))  # False: 0 is the invalid ID

    Returns:
        True if the element exists, False otherwise.
    """

def start_element_module_calculation(covers: list[ElementId]) -> None:
    """Run the element module calculation for cover elements.

    The element module fills walls, floors and roofs (framed, solid or log covers) with the beams,
    panels and other parts defined in their element module setup. Only cover elements in the list
    are used; other elements and IDs that do not exist are ignored, and if no cover remains nothing
    happens. Does nothing at all if the element module is not licensed. The covers are activated for
    the calculation and deactivated again afterwards, so they are inactive when the call returns.
    The resulting elements are created in the model and the display is refreshed.

    Parameters:
        covers: IDs of the cover elements (walls, floors, roofs), e.g. the walls among
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> covers = [i for i in element_ids if ac.is_wall(i) or ac.is_floor(i)]
        >>> ec.start_element_module_calculation(covers)
    """

def set_element_detail_path(path: str) -> None:
    """Set the folder used for element details.

    Sets the folder from which element details are read and to which they are written. An empty path
    is ignored and leaves the current folder unchanged. Read the current value back with
    `element_controller.get_element_detail_path()`.

    Parameters:
        path: Path of the element detail folder; use forward slashes or a raw string for Windows
            paths.

    Examples:
        >>> import element_controller as ec

        >>> ec.set_element_detail_path('C:/cadwork/details')
        >>> print(ec.get_element_detail_path())
    """

def get_element_from_cadwork_guid(cadwork_guid: str) -> ElementId:
    """Find the element with the given cadwork GUID.

    Every element has a cadwork GUID that stays the same when its ID changes, for example after the
    document is merged into another one. Searches visible and hidden elements. Read the GUID of an
    element with `element_controller.get_element_cadwork_guid()`.

    Parameters:
        cadwork_guid: GUID string of the element, as returned by
            `element_controller.get_element_cadwork_guid()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> guid = ec.get_element_cadwork_guid(element_ids[0])
        >>> element_id = ec.get_element_from_cadwork_guid(guid)
        >>> print(element_id == element_ids[0])

    Returns:
        ID of the matching element, or 0 if the GUID is invalid (also an empty or null GUID) or no
        element matches.
    """

def add_elements_to_undo(element_id_list: list[ElementId], cmd: int) -> None:
    """Register elements as one undo step.

    Lets a script make its own changes undoable with `element_controller.make_undo()` or the undo
    button. cmd 1 registers the elements as created (undo deletes them); cmd 2 registers them as
    modified and stores their current state and attributes, so call it before changing them. Any
    other cmd does nothing. Registering is one step on the undo stack regardless of the number of
    elements. IDs that do not exist are skipped. `element_controller.add_created_elements_to_undo()`
    and `element_controller.add_modified_elements_to_undo()` do the same without the cmd number.

    Parameters:
        element_id_list: Element IDs to register, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        cmd: 1 = the elements were created, 2 = the elements are about to be modified. Other values
            are ignored.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.add_elements_to_undo(element_ids, 2)  # store the state before the change
        >>> ec.move_element(element_ids, cadwork.point_3d(0., 0., 100.))
        >>> ec.make_undo()  # moves the elements back
    """

def make_undo() -> None:
    """Undo the last undo step.

    Applies the undo stack of the current document, the same as the undo command in the user
    interface. It undoes whatever the latest step is, including steps made by the user and steps
    registered by other script calls. Operations that do not register an undo step (for example
    `element_controller.delete_elements()` or `element_controller.move_element()`) cannot be undone
    this way. Redo with `element_controller.make_redo()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.delete_elements_with_undo(element_ids)
        >>> ec.make_undo()  # the elements are back
    """

def make_redo() -> None:
    """Redo the last undone step.

    Re-applies the step most recently reverted by `element_controller.make_undo()` or the undo
    command in the user interface. Has no effect when there is nothing to redo, as is the case after
    a new undo step was registered following the undo.

    Examples:
        >>> import element_controller as ec

        >>> ec.make_undo()
        >>> ec.make_redo()  # restores the step that was just undone
    """

def split_elements(element_id_list: list[ElementId]) -> None:
    """Split joined element groups.

    Reverses `element_controller.join_elements()`: the given elements are separated from their
    groups. An error is shown in the command bar (not raised) if the selection is an incomplete
    group. IDs that do not exist are skipped.

    Parameters:
        element_id_list: Element IDs to split off their groups, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.split_elements(element_ids)
    """

def set_line_to_marking_line(element_id_list: list[ElementId]) -> None:
    """Turn line elements into marking lines.

    Sets the marking flag on each element. Marking lines are lines that serve as markings instead of
    normal geometry lines. Reverse with `element_controller.set_line_to_normal_line()`. IDs that do
    not exist are skipped. No check is made that the elements really are lines, so pass only line
    elements, e.g. created with `element_controller.create_line_points()`. The display is not
    refreshed by this function.

    Parameters:
        element_id_list: IDs of the line elements.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> line_ids = [i for i in element_ids if ac.is_line(i)]
        >>> ec.set_line_to_marking_line(line_ids)
    """

def set_line_to_normal_line(element_id_list: list[ElementId]) -> None:
    """Turn marking lines back into normal lines.

    Clears the marking flag on each element. Reverses
    `element_controller.set_line_to_marking_line()`. IDs that do not exist are skipped. No check is
    made that the elements really are lines, so pass only line elements. The display is not
    refreshed by this function.

    Parameters:
        element_id_list: IDs of the line elements.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> line_ids = [i for i in element_ids if ac.is_line(i)]
        >>> ec.set_line_to_normal_line(line_ids)
    """

def create_auto_export_solid_from_standard(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str
) -> ElementId:
    """Create an auto export solid around elements from a standard export solid.

    An export solid is a container element that encloses a group of elements for export. The new one
    encloses the given elements (bounding box aligned to the world axes, with a 10 mm offset), is
    named output_name and takes the elements as its contents (read them back with
    `element_controller.get_export_solid_content_elements()`). All active elements in the model are
    deactivated first, not only those in the list. Standard element names are not unique, only GUIDs
    are: if several standard elements share this name, the first match is used. Folders of the
    standard element library are not handled by the API and cannot be used to select one. The new
    element is inserted and shown.

    Parameters:
        element_id_list: IDs of the elements to enclose; IDs that do not exist are skipped.
        output_name: Name given to the new export solid.
        standard_element_name: Name of a standard element of type export solid in the current
            cadwork language, e.g. from `element_controller.get_standard_export_solid_list()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> names = ec.get_standard_export_solid_list()
        >>> if names:
        ...     solid_id = ec.create_auto_export_solid_from_standard(
        ...         element_ids, 'Export 1', names[0]
        ...     )
        ...     print(solid_id)

    Returns:
        ID of the created export solid, or 0 if no standard export solid with that name exists.
    """

def set_element_module_properties_for_elements(
    element_id_list: list[ElementId], properties: element_module_properties
) -> None:
    """Set the element module properties of elements.

    Element module properties control how an element is treated when the element module fills a
    wall, floor or roof (stretching, distribution, plates, cutting priority, layer names and so on).
    All module properties of each element are replaced by the values in properties, so properties
    not set in it are cleared, including the distances, counts, cutting priority and layer names.
    Take a copy from an existing element with
    `element_controller.get_element_module_properties_for_element()`, change what you need and apply
    it. IDs that do not exist are skipped. No undo step is registered.

    Parameters:
        element_id_list: IDs of the elements to modify, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        properties: The `element_module_properties` object to apply to every element in the list.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> source_id, *target_ids = element_ids
        >>> props = ec.get_element_module_properties_for_element(source_id)
        >>> props.set_bottom_plate(True)
        >>> ec.set_element_module_properties_for_elements(target_ids, props)
    """

def create_text_object_with_font(
    text: str, position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, size: float, font_name: str
) -> ElementId:
    """Create a text object using a given font.

    The text consists of one element per letter; the returned ID is that of the last letter element.
    The text lies in the plane perpendicular to z_local_direction, with its baseline along
    x_local_direction. The letters are assigned to the active scene and building storey and the
    display is refreshed. Use `element_controller.create_text_object()` for the default font.

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
    one, i.e. an element that sat at a certain position relative to the old origin and axes ends up
    at the same relative position in the new system. Each coordinate system is defined by an origin
    and its X and Y directions. IDs that do not exist are skipped. No undo step is registered, and
    the display is refreshed unless auto refresh is disabled.

    Parameters:
        element_id_list: IDs of the elements to transform, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        old_point: Origin of the source coordinate system.
        old_x_local_direction: X axis direction of the source coordinate system.
        old_y_local_direction: Y axis direction of the source coordinate system.
        new_point: Origin of the target coordinate system.
        new_x_local_direction: X axis direction of the target coordinate system.
        new_y_local_direction: Y axis direction of the target coordinate system.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> origin = cadwork.point_3d(0., 0., 0.)
        >>> x_axis = cadwork.point_3d(1., 0., 0.)
        >>> y_axis = cadwork.point_3d(0., 1., 0.)
        >>> new_origin = cadwork.point_3d(5000., 0., 0.)
        >>> new_x = cadwork.point_3d(0., 1., 0.)
        >>> new_y = cadwork.point_3d(-1., 0., 0.)
        >>> ec.apply_transformation_coordinate(
        ...     element_ids, origin, x_axis, y_axis, new_origin, new_x, new_y
        ... )
    """

def delete_elements_with_undo(element_id_list: list[ElementId]) -> None:
    """Delete elements as one undoable step.

    Removes the elements from the model and registers the deletion as a single undo step, so
    `element_controller.make_undo()` (or the user's undo) brings them all back. IDs that do not
    exist are skipped. Use `element_controller.delete_elements()` when no undo step is wanted. The
    menu state is updated afterwards.

    Parameters:
        element_id_list: Element IDs to delete, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.delete_elements_with_undo(element_ids)
        >>> ec.make_undo()  # restores the deleted elements
    """

def add_created_elements_to_undo(element_id_list: list[ElementId]) -> None:
    """Register already created elements as one undo step.

    Call it after creating elements with a function that does not register an undo step, so that the
    user can remove them again with undo. After this, `element_controller.make_undo()` removes the
    elements. IDs that do not exist are skipped. Equivalent to
    `element_controller.add_elements_to_undo()` with cmd 1.

    Parameters:
        element_id_list: IDs of the elements that were created, e.g. the IDs returned by the
            creation functions.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> node_id = ec.create_node(cadwork.point_3d(0., 0., 0.))
        >>> line_id = ec.create_line_points(
        ...     cadwork.point_3d(0., 0., 0.), cadwork.point_3d(1000., 0., 0.)
        ... )
        >>> ec.add_created_elements_to_undo([node_id, line_id])
    """

def add_modified_elements_to_undo(element_id_list: list[ElementId]) -> None:
    """Register elements as modified in one undo step.

    Stores the current state of the elements (geometry plus name, group, subgroup, comment, EDP code
    and user texts) as the state that undo restores, so call it before modifying them. All elements
    go into one undo step. IDs that do not exist are skipped. Equivalent to
    `element_controller.add_elements_to_undo()` with cmd 2.

    Parameters:
        element_id_list: IDs of the elements that are about to be modified, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.add_modified_elements_to_undo(element_ids)
        >>> ec.move_element(element_ids, cadwork.point_3d(0., 0., 100.))
    """

def recreate_elements(element_id_list: list[ElementId]) -> None:
    """Rebuild the display representation of elements.

    Recreates how the elements are drawn and redraws the view. Visibility states are preserved. Call
    it after changing many elements while `utility_controller.disable_auto_display_refresh()` was
    active, or when the display is out of date. IDs that do not exist are skipped. It does not
    change the element data.

    Parameters:
        element_id_list: IDs of the elements to recreate, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import utility_controller as uc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> uc.disable_auto_display_refresh()
        >>> try:
        ...     pass  # many modifications of element_ids here
        ... finally:
        ...     uc.enable_auto_display_refresh()
        >>> ec.recreate_elements(element_ids)
    """

def create_multi_wall(element_id_list: list[ElementId]) -> None:
    """Couple wall, roof and floor elements into a multi-wall structure.

    Couples the given walls, roofs and floors into a multi-wall structure, like the multi-wall
    coupling command in the user interface. Only walls, roofs and floors among the given elements
    are used; at least two are needed, otherwise nothing happens. Elements within the coupling
    distance configured in cadwork 3D are coupled; the distance cannot be passed as a parameter.

    Parameters:
        element_id_list: IDs of the wall, roof or floor elements to couple, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import attribute_controller as ac

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> covers = [i for i in element_ids if ac.is_wall(i) or ac.is_roof(i) or ac.is_floor(i)]
        >>> ec.create_multi_wall(covers)
    """

def get_user_element_ids() -> list[ElementId]:
    """Let the user select elements interactively and return their IDs.

    Prompts the user in the 3D view and blocks the script until the selection is finished. Elements
    of any type can be picked. If the user presses Esc, an error is recorded (no exception is
    raised) and the list contains whatever was selected up to then, possibly nothing. Clear recorded
    errors with `element_controller.clear_errors()`. Use
    `element_controller.get_user_element_ids_with_existing()` to start with some elements
    pre-marked.

    Examples:
        >>> import element_controller as ec
        >>> import utility_controller as uc

        >>> element_ids = ec.get_user_element_ids()
        >>> if not element_ids:
        ...     uc.print_error('No elements selected.')

    Returns:
        List of IDs of the elements selected by the user; empty if none were selected.
    """

def get_user_element_ids_with_existing(element_id_list: list[ElementId]) -> list[ElementId]:
    """Let the user select elements interactively, with some elements pre-marked.

    Like `element_controller.get_user_element_ids()`, but the given elements are shown as marked
    during the selection, for example to let the user extend or correct an earlier selection.
    Visibility is restored afterwards and the marks are removed. Blocks until the user finishes. If
    the user presses Esc, an error is recorded (no exception is raised) and the list contains
    whatever was selected up to then, possibly nothing. The pre-marked elements are not
    automatically part of the result; only what the user picks is returned.

    Parameters:
        element_id_list: IDs of the elements to mark at the start of the selection; IDs that do not
            exist are skipped.

    Examples:
        >>> import element_controller as ec

        >>> premarked_ids = ec.get_active_identifiable_element_ids()
        >>> element_ids = ec.get_user_element_ids_with_existing(premarked_ids)
        >>> print(len(element_ids), 'elements selected')

    Returns:
        List of IDs of the elements selected by the user; empty if none were selected.
    """

def clear_errors() -> None:
    """Clear the recorded API error messages.

    Empties the error list of the element controller. Errors are recorded, for example, when the
    user cancels an interactive selection with Esc in `element_controller.get_user_element_ids()`,
    or when a creation function such as `element_controller.create_polygon_beam_vectors()` rejects
    its arguments. Call it before an operation whose errors you want to inspect separately.

    Examples:
        >>> import element_controller as ec

        >>> ec.clear_errors()
        >>> element_ids = ec.get_user_element_ids()
    """

def glide_elements(element_id_list: list[ElementId], glide_origin_point: point_3d) -> None:
    """Move elements interactively; the user picks the destination.

    Starts an interactive move in the 3D view and blocks the script until the user confirms a
    position or cancels. If the user cancels with Esc, an error is recorded (see
    `element_controller.clear_errors()`). Invalid IDs are skipped. In 2D plane mode (a working plane
    is active) the elements are additionally moved by the glide origin point projected onto the
    working plane. To move by a fixed vector without user interaction use
    `element_controller.move_element_with_undo()`.

    Parameters:
        element_id_list: IDs of the elements to move, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        glide_origin_point: Reference point in global coordinates (mm) from which the elements are
            glided.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> origin = cadwork.point_3d(0., 0., 0.)
        >>> ec.glide_elements(element_ids, origin)  # blocks until the user picks a position
    """

def cut_elements_with_miter(first_id: ElementId, second_id: ElementId) -> bool:
    """Cut two elements against each other with a miter joint.

    Trims both elements so that they meet in a miter joint. Both elements are modified in place and
    the step is added to undo. If either ID is invalid, nothing is cut. The result is always `True`,
    so it cannot be used to detect whether the cut worked; check the geometry instead.

    Parameters:
        first_id: ID of the first element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        second_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) == 2:
        ...     ec.cut_elements_with_miter(element_ids[0], element_ids[1])

    Returns:
        Always `True`, also when an ID is invalid or the cut failed.
    """

def cut_element_with_plane(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> bool:
    """Cut an element in place with a plane.

    Cuts the element with the plane of all points p where the dot product of p and the normal equals
    the distance. The element is modified directly and the change is not added to undo. Pass the ID
    of an existing element. Use `element_controller.slice_element_with_plane()` to split an element
    into parts instead.

    Parameters:
        element_id: ID of the element to cut, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
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
        `True` once the cut was issued. This does not guarantee that the element was changed.
    """

def create_circular_mep(diameter: float, points: list[point_3d]) -> ElementId:
    """Create a round MEP (installation) element along a polyline.

    MEP elements are installation objects such as pipes and ducts. The element follows the straight
    segments between consecutive points and gets the given diameter. It is created with a fixed
    color and added to the active scene. For a rectangular cross-section use
    `element_controller.create_rectangular_mep()`.

    Parameters:
        diameter: Diameter of the round installation (mm).
        points: Ordered path points (global coordinates, mm); consecutive points are joined by
            straight segments, so at least two distinct points are needed.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> path = [
        ...     cadwork.point_3d(0., 0., 2500.),
        ...     cadwork.point_3d(3000., 0., 2500.),
        ...     cadwork.point_3d(3000., 2000., 2500.),
        ... ]
        >>> pipe_id = ec.create_circular_mep(100., path)
        >>> if pipe_id == 0:
        ...     print('Path could not be built')

    Returns:
        ID of the new element, or 0 if a segment could not be built (for example two identical
        consecutive points).
    """

def create_rectangular_mep(width: float, depth: float, points: list[point_3d]) -> ElementId:
    """Create a rectangular MEP (installation) element along a polyline.

    MEP elements are installation objects such as ducts and cable trays. The element follows the
    straight segments between consecutive points and gets the given rectangular cross-section. It is
    created with a fixed color and added to the active scene. For a round cross-section use
    `element_controller.create_circular_mep()`.

    Parameters:
        width: Width of the rectangular cross-section (mm).
        depth: Depth of the rectangular cross-section (mm).
        points: Ordered path points (global coordinates, mm); consecutive points are joined by
            straight segments, so at least two distinct points are needed.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> path = [cadwork.point_3d(0., 0., 2800.), cadwork.point_3d(4000., 0., 2800.)]
        >>> duct_id = ec.create_rectangular_mep(300., 150., path)
        >>> if duct_id == 0:
        ...     print('Path could not be built')

    Returns:
        ID of the new element, or 0 if a segment could not be built (for example two identical
        consecutive points).
    """

def slice_element_with_plane(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> bool:
    """Slice an element into parts with a plane.

    Divides the element along the plane of all points p where the dot product of p and the normal
    equals the distance. The operation is added to undo. The newly created parts are not returned by
    this function; use `element_controller.slice_elements_with_plane_and_get_new_elements()` to get
    them. Pass the ID of an existing element.

    Parameters:
        element_id: ID of the element to slice, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
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
        `True` once the slice was issued. This does not guarantee that the element was changed.
    """

def create_auto_container_from_standard(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str
) -> ElementId:
    """Create a container around elements from a standard container.

    A container groups elements, for example for export or production. The container is taken from
    the standard element library, sized to the bounding box of the given elements (10 mm offset),
    aligned to the global axes, inserted and shown, and the elements are assigned to it. All
    currently active elements are deactivated, even when the call fails. The first standard
    container with a matching name is used. Use
    `element_controller.create_auto_container_from_standard_with_reference()` to orient the
    container on an element's local axes.

    Parameters:
        element_id_list: IDs of the elements to put into the container, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; invalid IDs are skipped.
        output_name: Name given to the new container.
        standard_element_name: Name of a standard container, e.g. from
            `element_controller.get_standard_container_list()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> container_names = ec.get_standard_container_list()
        >>> if element_ids and container_names:
        ...     container_id = ec.create_auto_container_from_standard(
        ...         element_ids, 'My container', container_names[0]
        ...     )

    Returns:
        ID of the new container, or 0 if no standard container with that name exists.
    """

def create_auto_export_solid_from_standard_with_reference(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId
) -> ElementId:
    """Create an export solid around elements, oriented on a reference element.

    An export solid is a volume that marks elements for export. It is taken from the standard
    element library, sized to the bounding box of the given elements (10 mm offset) and aligned to
    the local axes of the reference element, then inserted and shown. Its properties are taken from
    the reference element. All currently active elements are deactivated, even when the call fails.
    Use `element_controller.create_auto_export_solid_from_standard()` when no reference element is
    needed.

    Parameters:
        element_id_list: IDs of the elements to put into the export solid, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; invalid IDs are skipped.
        output_name: Name for the new export solid. Currently not applied.
        standard_element_name: Name of a standard export solid, e.g. from
            `element_controller.get_standard_export_solid_list()`.
        reference_id: ID of the reference element whose local X and Z axes orient the export solid;
            must exist.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> solid_names = ec.get_standard_export_solid_list()
        >>> if element_ids and solid_names:
        ...     solid_id = ec.create_auto_export_solid_from_standard_with_reference(
        ...         element_ids, 'Export', solid_names[0], element_ids[0]
        ...     )

    Returns:
        ID of the new export solid, or 0 if the standard export solid name is unknown or the
        reference element does not exist.
    """

def create_auto_container_from_standard_with_reference(
    element_id_list: list[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId
) -> ElementId:
    """Create a container around elements, oriented on a reference element.

    A container groups elements, for example for export or production. It is taken from the standard
    element library, sized to the bounding box of the given elements (10 mm offset) and aligned to
    the local axes of the reference element, then inserted and shown, and the elements are assigned
    to it. Its properties are taken from the reference element. All currently active elements are
    deactivated, even when the call fails. Use
    `element_controller.create_auto_container_from_standard()` when no reference element is needed.

    Parameters:
        element_id_list: IDs of the elements to put into the container, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; invalid IDs are skipped.
        output_name: Name for the new container. Currently not applied.
        standard_element_name: Name of a standard container, e.g. from
            `element_controller.get_standard_container_list()`.
        reference_id: ID of the reference element whose local X and Z axes orient the container;
            must exist.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> container_names = ec.get_standard_container_list()
        >>> if element_ids and container_names:
        ...     container_id = ec.create_auto_container_from_standard_with_reference(
        ...         element_ids, 'My container', container_names[0], element_ids[0]
        ...     )

    Returns:
        ID of the new container, or 0 if the standard container name is unknown or the reference
        element does not exist.
    """

def create_surface(surface_vertices: vertex_list) -> ElementId:
    """Create a surface element from a closed polygon of vertices.

    The polygon is closed automatically, so do not repeat the first vertex. The new surface element
    is inserted, shown and added to the active scene. Surfaces can be turned into volumes with
    `element_controller.extrude_surface_to_panel_vector()`,
    `element_controller.extrude_surface_to_beam_vector()` or
    `element_controller.extrude_surface_to_auxiliary_vector()`.

    Parameters:
        surface_vertices: Ordered corner points of the polygon (global coordinates, mm), as a
            `cadwork.vertex_list`; at least 3 are required.

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

    Works on beams, panels and other elements with a beam-like cross-section along their axis. The
    start face is the face at the beginning of the element axis (local X). Elements without such a
    face, such as free volumes, and invalid IDs are left unchanged. Elements are modified in place;
    end types are kept and the element axis is updated. Use `element_controller.stretch_end_facet()`
    for the opposite end.

    Parameters:
        element_id_list: IDs of the elements to stretch, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        stretch_vector: Displacement applied to the start face (direction and distance, mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        ... # for elements lying along global X, this lengthens them by 100 mm at the start
        >>> ec.stretch_start_facet(element_ids, cadwork.point_3d(-100., 0., 0.))
    """

def stretch_end_facet(element_id_list: list[ElementId], stretch_vector: point_3d) -> None:
    """Move the end face of linear elements such as beams and panels by a vector.

    Works on beams, panels and other elements with a beam-like cross-section along their axis. The
    end face is the face at the far end of the element axis. Elements without such a face, such as
    free volumes, and invalid IDs are left unchanged. Elements are modified in place; end types are
    kept and the element axis is updated. Use `element_controller.stretch_start_facet()` for the
    opposite end.

    Parameters:
        element_id_list: IDs of the elements to stretch, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        stretch_vector: Displacement applied to the end face (direction and distance, mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        ... # for elements lying along global X, this lengthens them by 100 mm at the end
        >>> ec.stretch_end_facet(element_ids, cadwork.point_3d(100., 0., 0.))
    """

def set_export_solid_contents(export_solid_id: ElementId, element_id_list: list[ElementId]) -> None:
    """Set the elements contained in an export solid.

    An export solid is a volume that marks the elements to be exported. The given elements are
    assigned as its contents. Does nothing if the export solid ID is invalid or the element is not
    an export solid; invalid IDs in the list are skipped. Read the current contents with
    `element_controller.get_export_solid_content_elements()`.

    Parameters:
        export_solid_id: ID of an existing export solid, e.g. from
            `element_controller.create_auto_export_solid_from_standard()`.
        element_id_list: IDs of the elements to assign as its contents.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> solid_names = ec.get_standard_export_solid_list()
        >>> if element_ids and solid_names:
        ...     solid_id = ec.create_auto_export_solid_from_standard(
        ...         element_ids[:1], 'Export', solid_names[0]
        ...     )
        ...     if solid_id:
        ...         ec.set_export_solid_contents(solid_id, element_ids)
        ...         print(ec.get_export_solid_content_elements(solid_id))
    """

def set_container_contents(container_id: ElementId, element_id_list: list[ElementId]) -> None:
    """Set the elements contained in a container.

    A container groups elements, for example for export or production. The given elements are
    assigned as its contents. Does nothing if the container ID is invalid, the element is not a
    container, or it is a container block; invalid IDs in the list are skipped. Read the current
    contents with `element_controller.get_container_content_elements()`.

    Parameters:
        container_id: ID of an existing container, e.g. from
            `element_controller.create_auto_container_from_standard()`.
        element_id_list: IDs of the elements to assign as its contents.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> container_names = ec.get_standard_container_list()
        >>> if element_ids and container_names:
        ...     container_id = ec.create_auto_container_from_standard(
        ...         element_ids[:1], 'My container', container_names[0]
        ...     )
        ...     if container_id:
        ...         ec.set_container_contents(container_id, element_ids)
        ...         print(ec.get_container_content_elements(container_id))
    """

def set_parent_opening_variants_opening_angle(element_id_list: list[ElementId], angle: float) -> None:
    """Set the opening angle of opening elements that have a variant.

    Only opening elements (doors, windows) that have a variant are affected; all other elements and
    invalid IDs are skipped. The same angle is applied to the general, 2D and 3D opening angle of
    the variant, and the variant is then recalculated. Use
    `element_controller.get_opening_variant_ids()` to find the variants of openings.

    Parameters:
        element_id_list: IDs of the opening elements, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        angle: Opening angle to set.

    Examples:
        >>> import element_controller as ec

        >>> opening_ids = ec.get_active_identifiable_element_ids()
        >>> ec.set_parent_opening_variants_opening_angle(opening_ids, 45.)
    """

def mirror_move_elements(element_id_list: list[ElementId], plane: point_3d, plane_distance: float) -> None:
    """Mirror elements in place across a plane.

    The elements themselves are reflected (not copied); the change is not added to undo. Invalid IDs
    are skipped. Use `element_controller.mirror_copy_elements()` to keep the originals.

    Parameters:
        element_id_list: IDs of the elements to mirror, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        plane: Normal vector of the mirror plane; pass a unit vector.
        plane_distance: Distance of the mirror plane from the global origin, measured along the
            normal (mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        ... # mirror across the plane x = 1000
        >>> ec.mirror_move_elements(element_ids, cadwork.point_3d(1., 0., 0.), 1000.)
    """

def mirror_copy_elements(element_id_list: list[ElementId], plane: point_3d, plane_distance: float) -> list[ElementId]:
    """Create mirrored copies of elements across a plane.

    Each valid element is copied and the copy is reflected; the originals stay unchanged. The copies
    are not kept in a group, even if the originals were grouped. Invalid IDs are skipped. Use
    `element_controller.mirror_move_elements()` to mirror the elements themselves.

    Parameters:
        element_id_list: IDs of the elements to copy and mirror, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        plane: Normal vector of the mirror plane; pass a unit vector.
        plane_distance: Distance of the mirror plane from the global origin, measured along the
            normal (mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        ... # mirror across the plane x = 0
        >>> copy_ids = ec.mirror_copy_elements(element_ids, cadwork.point_3d(1., 0., 0.), 0.)
        >>> print(len(copy_ids), 'copies created')

    Returns:
        IDs of the new mirrored copies, in input order (originals not included). Empty list if no
        element was copied.
    """

def reset_element_cadwork_guid(element_id: ElementId) -> None:
    """Clear the cadwork GUID and IFC GUID of an element.

    Both identifiers are set to empty values. Does nothing if the ID is invalid. Read the cadwork
    GUID with `element_controller.get_element_cadwork_guid()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     ec.reset_element_cadwork_guid(element_id)
        ...     print(repr(ec.get_element_cadwork_guid(element_id)))
    """

def create_standard_beam_points(
    standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard beam from a start point, an end point and an orientation point.

    Standard beams are cross-section templates from the standard element library. The beam length is
    the distance from first_point to second_point. The new beam is inserted and shown and added to
    the active scene. The first standard beam with a matching name is used. Use
    `element_controller.create_standard_beam_vectors()` to specify length and directions instead of
    points.

    Parameters:
        standard_element_name: Name of a standard beam, e.g. from
            `element_controller.get_standard_beam_list()`.
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

    Standard beams are cross-section templates from the standard element library. The new beam is
    inserted and shown and added to the active scene. The first standard beam with a matching name
    is used. Use `element_controller.create_standard_beam_points()` to specify the beam by points
    instead.

    Parameters:
        standard_element_name: Name of a standard beam, e.g. from
            `element_controller.get_standard_beam_list()`.
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
    """Create a standard panel from a start point, an end point and an orientation point.

    Standard panels are templates from the standard element library. The panel length is the
    distance from first_point to second_point. The new panel is inserted and shown and added to the
    active scene. The first standard panel with a matching name is used. Use
    `element_controller.create_standard_panel_vectors()` to specify length and directions instead of
    points.

    Parameters:
        standard_element_name: Name of a standard panel, e.g. from
            `element_controller.get_standard_panel_list()`.
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

    Standard panels are templates from the standard element library. The new panel is inserted and
    shown and added to the active scene. The first standard panel with a matching name is used. Use
    `element_controller.create_standard_panel_points()` to specify the panel by points instead.

    Parameters:
        standard_element_name: Name of a standard panel, e.g. from
            `element_controller.get_standard_panel_list()`.
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
    """Create a standard steel element from a start point, an end point and an orientation point.

    Steel elements are profiles (for example IPE or HEA) from the steel profile library. The element
    length is the distance from first_point to second_point. The new element is inserted and shown
    and added to the active scene. If several profiles match the name, a European, American,
    British, Oceanic, Russian or Swiss profile is preferred, otherwise the first match is used. Use
    `element_controller.create_standard_steel_vectors()` to specify length and directions instead of
    points.

    Parameters:
        standard_element_name: Name of the steel profile in cadwork notation, e.g. 'IPE 200'.
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

    Steel elements are profiles (for example IPE or HEA) from the steel profile library. The new
    element is inserted and shown and added to the active scene. If several profiles match the name,
    a European, American, British, Oceanic, Russian or Swiss profile is preferred, otherwise the
    first match is used. Use `element_controller.create_standard_steel_points()` to specify the
    element by points instead.

    Parameters:
        standard_element_name: Name of the steel profile in cadwork notation, e.g. 'HEA 220'.
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

    All valid elements are translated by the vector and recorded in a single undo step. Invalid IDs
    are skipped. The display is refreshed afterwards. Use `element_controller.glide_elements()` to
    let the user pick the destination instead.

    Parameters:
        element_id_list: IDs of the elements to move, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        vector: Translation (direction and distance, mm).

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.move_element_with_undo(element_ids, cadwork.point_3d(0., 0., 500.))  # 500 mm up
    """

def create_normal_axis_points(first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a normal axis (line) between two points.

    A normal axis is a simple line element. It is created with a fixed color and added to the active
    scene.

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

    A normal axis is a simple line element. The end point is starting_point + axis_direction *
    length; the direction is not normalized, so pass a unit vector. It is created with a fixed color
    and added to the active scene.

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

    Each element is first converted to a connector axis and then redefined as the standard
    connector, keeping its position, length, orientation and color. The elements are modified in
    place. Does nothing if the standard connector name is unknown; invalid IDs are skipped.

    Parameters:
        element_id_list: IDs of the bolts to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        standard_element_name: Name of a standard connector, e.g. from
            `connector_axis_controller.get_standard_connector_list()`.

    Examples:
        >>> import connector_axis_controller as cac
        >>> import element_controller as ec

        >>> connector_names = cac.get_standard_connector_list()
        >>> bolt_ids = ec.get_active_identifiable_element_ids()
        >>> if connector_names and bolt_ids:
        ...     ec.convert_bolt_to_standardconnector(bolt_ids, connector_names[0])
    """

def extrude_surface_to_auxiliary_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into an auxiliary element.

    The surface is swept along the vector to form an auxiliary (construction) volume. The original
    surface is deleted and replaced by the new element, which inherits its properties and color. The
    change is not added to undo. A surface made of a single full circle becomes a round section.
    Create surfaces with `element_controller.create_surface()`.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface, e.g. from
            `element_controller.create_surface()`.
        vector: Extrusion direction and distance (mm); becomes the local X axis of the new element.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> vertices = cadwork.vertex_list()
        >>> for x, y in ((0., 0.), (1000., 0.), (1000., 800.), (0., 800.)):
        ...     vertices.append(cadwork.point_3d(x, y, 0.))
        >>> surface_id = ec.create_surface(vertices)
        >>> if surface_id:
        ...     aux_id = ec.extrude_surface_to_auxiliary_vector(
        ...         surface_id, cadwork.point_3d(0., 0., 100.)
        ...     )

    Returns:
        ID of the new auxiliary element, or 0 if the element is not a surface or the extrusion
        failed.
    """

def extrude_surface_to_panel_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into a panel.

    The surface is swept along the vector to form a panel. The original surface is deleted and
    replaced by the new panel, which inherits its properties and color. The change is not added to
    undo. A surface made of a single full circle becomes a round section. Create surfaces with
    `element_controller.create_surface()`.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface, e.g. from
            `element_controller.create_surface()`.
        vector: Extrusion direction and distance (mm); becomes the local X axis of the new panel.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> vertices = cadwork.vertex_list()
        >>> for x, y in ((0., 0.), (1000., 0.), (1000., 800.), (0., 800.)):
        ...     vertices.append(cadwork.point_3d(x, y, 0.))
        >>> surface_id = ec.create_surface(vertices)
        >>> if surface_id:
        ...     panel_id = ec.extrude_surface_to_panel_vector(
        ...         surface_id, cadwork.point_3d(0., 0., 20.)
        ...     )

    Returns:
        ID of the new panel, or 0 if the element is not a surface or the extrusion failed.
    """

def extrude_surface_to_beam_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrude a surface into a beam.

    The surface is swept along the vector to form a beam. The original surface is deleted and
    replaced by the new beam, which inherits its properties and color. The change is not added to
    undo. A surface made of a single full circle becomes a round section. Create surfaces with
    `element_controller.create_surface()`.

    Parameters:
        surface: ID of the surface element to extrude; must be a surface, e.g. from
            `element_controller.create_surface()`.
        vector: Extrusion direction and distance (mm); becomes the length axis (local X) of the new
            beam.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> vertices = cadwork.vertex_list()
        >>> for x, y in ((0., 0.), (200., 0.), (200., 100.), (0., 100.)):
        ...     vertices.append(cadwork.point_3d(x, y, 0.))
        >>> surface_id = ec.create_surface(vertices)
        >>> if surface_id:
        ...     beam_id = ec.extrude_surface_to_beam_vector(
        ...         surface_id, cadwork.point_3d(0., 0., 3000.)
        ...     )

    Returns:
        ID of the new beam, or 0 if the element is not a surface or the extrusion failed.
    """

def convert_container_to_container_block(element_id_list: list[ElementId]) -> None:
    """Convert containers into container blocks.

    A container block is a container whose contents are locked together as one block. The contained
    elements become part of the block and are marked accordingly. Elements that are not containers
    and invalid IDs are skipped. Containers are created for example with
    `element_controller.create_auto_container_from_standard()`.

    Parameters:
        element_id_list: IDs of the containers to convert.

    Examples:
        >>> import element_controller as ec

        >>> container_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_container_to_container_block(container_ids)
    """

def create_bounding_box_local(reference_element: ElementId, element_id_list: list[ElementId]) -> ElementId:
    """Create a panel as bounding box of elements, aligned to a reference element.

    The box encloses the given elements, is oriented on the origin and local axes of the reference
    element and is created as a panel in the reference element's color, inserted and shown. Elements
    without geometry are skipped. To only read the corner points without creating an element use
    `element_controller.get_bounding_box_vertices_local()`.

    Parameters:
        reference_element: ID of the element whose origin and local axes orient the box; must exist
            and carry geometry.
        element_id_list: IDs of the elements to enclose, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     box_id = ec.create_bounding_box_local(element_ids[0], element_ids)
        ...     print('failed' if box_id == 0 else box_id)

    Returns:
        ID of the new bounding box panel, or 0 if the reference element is invalid, no valid element
        or body is given, or creation failed.
    """

def create_bounding_box_global(element_id_list: list[ElementId]) -> ElementId:
    """Create a panel as bounding box of elements, aligned to the global axes.

    The box encloses the given elements, is aligned to the global X, Y and Z axes and is created as
    a panel with a fixed color, inserted and shown. Elements without geometry are skipped. To only
    read the corner points without creating an element use
    `element_controller.get_bounding_box_vertices_global()`.

    Parameters:
        element_id_list: IDs of the elements to enclose, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> box_id = ec.create_bounding_box_global(element_ids)
        >>> print('failed' if box_id == 0 else box_id)

    Returns:
        ID of the new bounding box panel, or 0 if no valid element or body is given or creation
        failed.
    """

def convert_auxiliary_to_panel(element_id_list: list[ElementId]) -> None:
    """Convert auxiliary elements into panels.

    Auxiliary elements are construction volumes that are not counted as real parts. The auxiliary
    flag is removed and the element is converted to a panel in place, keeping its ID. Elements that
    are not auxiliary and invalid IDs are skipped. Use
    `element_controller.convert_auxiliary_to_beam()` to convert to beams, or
    `element_controller.convert_elements_to_auxiliary_elements()` for the reverse direction.

    Parameters:
        element_id_list: IDs of the auxiliary elements to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> aux_ids = [i for i in element_ids if ac.is_auxiliary(i)]
        >>> ec.convert_auxiliary_to_panel(aux_ids)
    """

def convert_auxiliary_to_beam(element_id_list: list[ElementId]) -> None:
    """Convert auxiliary elements into beams.

    Auxiliary elements are construction volumes that are not counted as real parts. The auxiliary
    flag is removed and the element is converted in place, keeping its ID. The shape is converted
    only for elements without a beam-like cross-section, so an auxiliary panel becomes a regular
    panel, not a beam. Elements that are not auxiliary and invalid IDs are skipped. Use
    `element_controller.convert_auxiliary_to_panel()` to convert to panels.

    Parameters:
        element_id_list: IDs of the auxiliary elements to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> aux_ids = [i for i in element_ids if ac.is_auxiliary(i)]
        >>> ec.convert_auxiliary_to_beam(aux_ids)
    """

def auto_set_rough_volume_situation(element_id_list: list[ElementId]) -> None:
    """Automatically determine the rough volume situation between elements.

    The rough volume situation links neighbouring cover elements (for example walls) as rough volume
    partners for the element module. With exactly two valid elements they are paired; with more,
    every element is paired with every other one. With fewer than two valid elements nothing
    happens. Use `element_controller.rough_volume_situation_manual()` to set partners of one cover
    explicitly, or `element_controller.activate_rv_without_situation()` to find covers that have
    none yet.

    Parameters:
        element_id_list: IDs of the cover elements to relate to each other, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec

        >>> cover_ids = ec.get_active_identifiable_element_ids()
        >>> ec.auto_set_rough_volume_situation(cover_ids)
    """

def rough_volume_situation_manual(
    cover: ElementId, add_partner: list[ElementId], remove_partner: list[ElementId]
) -> None:
    """Manually set rough volume partners of a cover element.

    Pairs the cover element with each element in add_partner as rough volume partners (see
    `element_controller.auto_set_rough_volume_situation()`). Does nothing if the cover ID is
    invalid; invalid IDs in the lists are skipped. remove_partner is currently not evaluated.

    Parameters:
        cover: ID of the cover element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        add_partner: IDs of the partner elements to add.
        remove_partner: IDs of partner elements to remove. Currently has no effect.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     ec.rough_volume_situation_manual(element_ids[0], element_ids[1:], [])
    """

def auto_set_parts_situation(element_id_list: list[ElementId]) -> None:
    """Automatically determine the parts situation for elements.

    The parts situation assigns elements (parts) to the cover element they belong to; the assignment
    is calculated automatically from the given elements. Invalid IDs are skipped. Use
    `element_controller.parts_situation_manual()` to assign parts to one cover explicitly, or
    `element_controller.activate_parts_without_situation()` to find parts that have none yet.

    Parameters:
        element_id_list: IDs of the elements to process, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.auto_set_parts_situation(element_ids)
    """

def parts_situation_manual(cover: ElementId, add_childs: list[ElementId], remove_childs: list[ElementId]) -> None:
    """Manually set the child elements (parts) of a cover element.

    Elements in remove_childs are detached from their cover. Elements in add_childs are first
    detached from any previous cover and then attached to the given cover. Does nothing if the cover
    ID is invalid; invalid IDs in the lists are skipped. Use
    `element_controller.auto_set_parts_situation()` for the automatic assignment.

    Parameters:
        cover: ID of the cover element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        add_childs: IDs of the elements to add as children of the cover.
        remove_childs: IDs of the elements to remove from their cover.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     ec.parts_situation_manual(element_ids[0], element_ids[1:], [])
    """

def activate_rv_without_situation() -> list[ElementId]:
    """Activate all cover elements that have no rough volume situation.

    Searches the document for cover elements without rough volume partners and activates them, so
    that they can be processed further. Nothing is activated if none is found. Fix the situation
    with `element_controller.auto_set_rough_volume_situation()` or
    `element_controller.rough_volume_situation_manual()`.

    Examples:
        >>> import element_controller as ec

        >>> cover_ids = ec.activate_rv_without_situation()
        >>> print(len(cover_ids), 'covers without rough volume situation')

    Returns:
        IDs of the activated elements. Empty list if there are none.
    """

def activate_parts_without_situation() -> list[ElementId]:
    """Activate all elements that have no parts situation.

    Searches the document for elements that are not assigned to any cover and activates them.
    Nothing is activated if none is found. Fix the situation with
    `element_controller.auto_set_parts_situation()` or
    `element_controller.parts_situation_manual()`.

    Examples:
        >>> import element_controller as ec

        >>> orphan_ids = ec.activate_parts_without_situation()
        >>> print(len(orphan_ids), 'parts without parts situation')

    Returns:
        IDs of the activated elements. Empty list if there are none.
    """

def add_elements_to_detail(element_id_list: list[ElementId], detail: int) -> None:
    """Assign elements to an element-module detail group.

    Detail groups are used by the element module to calculate one detail file at a time. The
    elements are assigned to the group and added to its detail scene. Only works in the drawing file
    all.3dc; in any other file nothing happens. Invalid IDs are skipped.
    `element_controller.add_element_to_detail()` does the same.

    Parameters:
        element_id_list: IDs of the elements to assign, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        detail: Detail group number as a plain integer: 0 none, 1 angle, 2 area, 3 cross, 4 edge, 5
            end, 6 line, 7 open, 8 T, 9 floor area, 10 floor end, 11 floor line, 12 floor open.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.add_elements_to_detail(element_ids, 2)  # 2 = area detail
    """

def subtract_elements_with_undo(
    hard_element_id_list: list[ElementId], soft_element_id_list: list[ElementId], with_undo: bool
) -> list[ElementId]:
    """Subtract the volume of hard elements from soft elements (boolean difference).

    The hard elements act as cutting tools and the soft elements are cut by them. Soft elements that
    fall apart into several volumes produce new elements. Invalid IDs are skipped. Whether the
    operation can be undone is controlled by with_undo.

    Parameters:
        hard_element_id_list: IDs of the cutter elements, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        soft_element_id_list: IDs of the elements to be cut.
        with_undo: If `True`, the operation is added to the undo stack; if `False` it cannot be
            undone.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> hard_ids, soft_ids = element_ids[:1], element_ids[1:]
        >>> new_ids = ec.subtract_elements_with_undo(hard_ids, soft_ids, True)
        >>> print(len(new_ids), 'new elements')

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

    A linear optimization bar is a raw stock bar on which parts are laid out one after another, as
    used for cutting lists. The elements are placed in list order along the bar, starting start_cut
    from its start, each followed by saw_kerf. The bar takes its cross-section and material from the
    first element and is added to the matching nesting group, which is created if missing. The bar
    element is hidden. Use `element_controller.get_all_nesting_raw_parts()` to list existing bars.

    Parameters:
        element_id_list: IDs of the elements placed on the bar, in order, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; invalid IDs are skipped.
        optimization_number: Number of the optimization bar.
        total_length: Total length of the bar (mm).
        start_cut: Length cut off at the start of the bar before the first element (mm).
        end_cut: Length cut off at the end of the bar (mm); only reduces the remaining length.
        saw_kerf: Saw kerf between consecutive elements (mm).
        is_production_list: Currently ignored; the list type follows the global cadwork setting.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> bar_id = ec.create_linear_optimization(
        ...     element_ids, 1, 6000., 20., 20., 4., False
        ... )
        >>> if bar_id == 0:
        ...     print('No valid elements given')

    Returns:
        ID of the created bar element, or 0 if no valid element is given.
    """

def start_element_module_calculation_silently(covers: list[ElementId]) -> None:
    """Run the element module calculation for cover elements without user interaction.

    The element module generates the wall, roof and floor structure of cover elements. Only cover
    elements in the list are processed; they are activated during the calculation and deactivated
    afterwards. Does nothing if the element module license is not available or if the list contains
    no cover. Invalid IDs are skipped. Use `element_controller.start_element_module_calculation()`
    for the interactive variant.

    Parameters:
        covers: IDs of the cover elements to calculate, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; other elements are ignored.

    Examples:
        >>> import element_controller as ec

        >>> cover_ids = ec.get_active_identifiable_element_ids()
        >>> ec.start_element_module_calculation_silently(cover_ids)
    """

def replace_physical_drillings_with_drilling_axes(
    element_id_list: list[ElementId], mininum_diameter: float, maximum_diameter: float
) -> list[ElementId]:
    """Replace drillings in beams, panels and other linear elements with drilling axes.

    Drillings whose diameter lies between the two given diameters are removed from the element and
    replaced by new axis elements (bolt elements), which are inserted and shown. Only beams, panels
    and other elements with a beam-like cross-section are processed; other elements are skipped. All
    active elements are deactivated. If the two diameters are swapped they are reordered.

    Parameters:
        element_id_list: IDs of the elements to process, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        mininum_diameter: Smallest drilling diameter to replace (mm); must not be negative.
        maximum_diameter: Largest drilling diameter to replace (mm); must not be negative.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> axis_ids = ec.replace_physical_drillings_with_drilling_axes(element_ids, 8., 30.)
        >>> print(len(axis_ids), 'drilling axes created')

    Returns:
        IDs of the new drilling axis elements. Empty list if nothing was replaced, no valid element
        was given or a diameter is negative.
    """

def cut_element_with_processing_group(soft_element: ElementId, processing: ElementId) -> None:
    """Cut an element with a processing group.

    The processing group performs the cut on the element. Does nothing if either ID is invalid. The
    element is modified in place.

    Parameters:
        soft_element: ID of the element to be cut.
        processing: ID of the processing group that performs the cut.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if len(element_ids) >= 2:
        ...     ec.cut_element_with_processing_group(element_ids[0], element_ids[1])
    """

def add_element_to_detail(element_id_list: list[ElementId], detail: int) -> None:
    """Assign elements to an element-module detail group.

    Detail groups are used by the element module to calculate one detail file at a time. The
    elements are assigned to the group and added to its detail scene. Only works in the drawing file
    all.3dc; in any other file nothing happens. Invalid IDs are skipped.
    `element_controller.add_elements_to_detail()` does the same.

    Parameters:
        element_id_list: IDs of the elements to assign, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        detail: Detail group number as a plain integer: 0 none, 1 angle, 2 area, 3 cross, 4 edge, 5
            end, 6 line, 7 open, 8 T, 9 floor area, 10 floor end, 11 floor line, 12 floor open.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.add_element_to_detail(element_ids, 2)  # 2 = area detail
    """

def convert_elements_to_auxiliary_elements(element_id_list: list[ElementId]) -> None:
    """Convert elements into auxiliary elements.

    Auxiliary elements are construction volumes that are not counted as real parts. Elements are
    converted in place and keep their ID; their cover type is reset, and panels are converted to
    beams first. Invalid IDs are skipped. Use `element_controller.convert_auxiliary_to_beam()` or
    `element_controller.convert_auxiliary_to_panel()` for the reverse direction.

    Parameters:
        element_id_list: IDs of the elements to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_elements_to_auxiliary_elements(element_ids)
    """

def create_circular_axis_points(diameter: float, first_point: point_3d, second_point: point_3d) -> ElementId:
    """Create a circular axis (round bar axis) between two points.

    A circular axis is a line element with a round cross-section that runs from the first to the
    second point. The new element is assigned to the active scene. Use
    `create_circular_axis_vector()` when you have a start point, a direction and a length instead of
    two points.

    Parameters:
        diameter: Diameter of the axis cross-section in mm.
        first_point: Start point of the axis, in global coordinates.
        second_point: End point of the axis, in global coordinates.

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

    The end point is calculated as starting_point + axis_direction * length. The direction is not
    normalized, so pass a unit vector or the axis gets a different length than requested. The new
    element is assigned to the active scene. Use `create_circular_axis_points()` when you know both
    end points.

    Parameters:
        diameter: Diameter of the axis cross-section in mm.
        length: Length of the axis in mm, applied as a multiplier of axis_direction (equals the real
            length only for a unit vector).
        starting_point: Start point of the axis, in global coordinates.
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
    """Create a panel by extruding a planar 3D polygon along its own face normal.

    The extrusion direction is the polygon's face normal (right-hand rule over the vertex order),
    not z_local_direction, and reversing the vertex order flips the panel. The polygon plane lies at
    mid-thickness of the panel. The last vertex in the list is dropped and the outline is closed
    automatically, so repeat the first vertex at the end. The panel is inserted, shown and assigned
    to the active scene. To describe the outline in the panel's own 2D plane instead, use
    `create_polygon_panel_vectors()`.

    Parameters:
        polygon_vertices: Corner points of the polygon in global coordinates, at least 3; they must
            be coplanar and enclose a non-zero area. Repeat the first vertex as the last entry (the
            last entry is ignored).
        thickness: Extrusion distance along the face normal in mm; the panel extends half of it to
            each side of the polygon plane.
        x_local_direction: Local X axis direction assigned to the new panel; does not steer the
            extrusion.
        z_local_direction: Local Z axis direction assigned to the new panel; does not steer the
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

    The outline lies in the local X/Y plane of the panel and is extruded along the local Z axis
    starting at the outline plane (not centered). The outline is closed automatically (do not repeat
    the first vertex) and may be given in either winding order. The panel is inserted, shown and
    assigned to the active scene. For an outline given as 3D points use `create_polygon_panel()`.

    Parameters:
        polygon_vertices: Outline vertices as point_2d or (u, v) tuples in mm; u runs along the
            local X axis, v along the local Y axis, (0, 0) is the starting point. At least 3
            vertices enclosing a non-zero area.
        thickness: Panel thickness in mm, i.e. the extrusion length along local Z; must be greater
            than 0.
        starting_point: 3D position in global coordinates of the outline origin (u=0, v=0).
        x_local_direction: Local X axis direction; must not be a zero vector.
        z_local_direction: Hint for the local Z side; the Y axis is derived as Z cross X and Z is
            then made perpendicular. Must not be zero and must not be parallel to x_local_direction.

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
    """Cut soft elements with hard elements, leaving an overmeasure.

    The soft elements are cut by the hard (cutting) elements and the cut is enlarged by the
    overmeasure stored in the hard elements' cut settings. Invalid IDs are skipped. Does nothing if
    either list ends up empty, or if none of the hard elements has overmeasure settings. A cadwork
    cut dialog is shown and must be confirmed, so the script waits for the user; nothing is cut if
    it is cancelled.

    Parameters:
        hard_element_id_list: IDs of the cutting (hard) elements, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Only those with overmeasure
            settings are used.
        soft_element_id_list: IDs of the elements to be cut (soft elements).

    Examples:
        >>> import element_controller as ec

        >>> hard_ids = ec.get_active_identifiable_element_ids()
        >>> soft_ids = ec.get_inactive_visible_identifiable_element_ids()
        >>> soft_ids = [element_id for element_id in soft_ids if element_id != 0]
        >>> ec.cut_elements_with_overmeasure(hard_ids, soft_ids)
    """

def cut_log_corner_joint(settings_name: str, element_id_list: list[ElementId]) -> None:
    """Cut a log corner joint on log beams using a named settings preset.

    Cuts the corner joint into the given log beams using a saved log corner joint settings preset.
    Invalid IDs are skipped. The elements are marked as modified and the display is refreshed. An
    unknown settings name is not reported by the API.

    Parameters:
        settings_name: Name of the saved log corner joint settings, as defined in the cadwork log
            corner joint dialog.
        element_id_list: IDs of the log beams to cut, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_log_corner_joint('Standard', beam_ids)
    """

def get_edge_selection(element_id_list: list[ElementId]) -> edge_list:
    """Let the user pick edges of the given elements and return them.

    Interactive: the script waits while the user selects edges in the 3D view (only the edges of the
    given elements can be picked) and confirms. Invalid IDs are skipped. Returns an empty list if
    the user presses Esc or selects nothing. The picked edges can be passed to `fillet_edge()` or
    `chamfer_edge()`.

    Parameters:
        element_id_list: IDs of the elements whose edges may be selected, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> edges = ec.get_edge_selection(element_ids)
        >>> if edges.count() == 0:
        ...     print('No edge selected')

    Returns:
        The selected edges, each given by its start point and end point in global coordinates. Empty
        if cancelled or nothing was selected.
    """

def get_facets_with_lasso(element_id_list: list[ElementId]) -> facet_list:
    """Let the user pick faces of the given elements and return them as facets.

    Interactive: the script waits while the user selects faces in the 3D view (only the faces of the
    given elements can be picked) and confirms. Invalid IDs are skipped. Returns an empty list if
    the user presses Esc or selects nothing.

    Parameters:
        element_id_list: IDs of the elements whose faces may be selected, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> facets = ec.get_facets_with_lasso(element_ids)
        >>> for index in range(facets.count()):
        ...     print(index, len(facets.at(index)))

    Returns:
        The selected faces, each given by the vertices of its outer boundary in global coordinates
        (curved boundaries are approximated by line segments; holes are not included). Empty if
        cancelled or nothing was selected.
    """

def create_standard_element_from_guid_points(
    guid: str, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a standard element from its GUID, placed by three points.

    A standard element is an entry of the cadwork standard element library (beam, panel, container
    ...). The GUID identifies it unambiguously, unlike its name, which may exist several times;
    folders of the library are not handled by the API. The new element is inserted, shown and
    assigned to the active scene. Get GUIDs from `element_controller.get_standard_beam_guid_list()`
    or `element_controller.get_standard_panel_guid_list()`. Use
    `create_standard_element_from_guid_vectors()` to place it by start point, length and directions.

    Parameters:
        guid: GUID of the standard element as a string.
        first_point: Start point of the element; origin of its local coordinate system.
        second_point: Defines the length and the local X axis: the length is the distance from
            first_point to second_point, and X points from first_point towards it. Must differ from
            first_point.
        third_point: Defines the local Z axis direction: Z points from first_point towards this
            point.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guids = ec.get_standard_beam_guid_list()
        >>> start = cadwork.point_3d(0., 0., 0.)
        >>> end = cadwork.point_3d(3000., 0., 0.)
        >>> up = cadwork.point_3d(0., 0., 1000.)
        >>> beam_id = ec.create_standard_element_from_guid_points(guids[0], start, end, up)

    Returns:
        The ID of the created element, or 0 on failure (unknown GUID, or first and second point
        coincide).
    """

def create_standard_element_from_guid_vectors(
    guid: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d
) -> ElementId:
    """Create a standard element from its GUID, placed by a start point and directions.

    A standard element is an entry of the cadwork standard element library (beam, panel, container
    ...). The GUID identifies it unambiguously, unlike its name; folders of the library are not
    handled by the API. The new element is inserted, shown and assigned to the active scene. Get
    GUIDs from `element_controller.get_standard_beam_guid_list()` or
    `element_controller.get_standard_panel_guid_list()`. Use
    `create_standard_element_from_guid_points()` to place it by three points.

    Parameters:
        guid: GUID of the standard element as a string.
        length: Length of the element along its local X axis in mm. Must be greater than 0.
        starting_point: Start point of the element; origin of its local coordinate system.
        x_local_direction: Direction of the local X axis (length axis); not normalized by the
            function.
        z_local_direction: Direction of the local Z axis. Must differ from x_local_direction.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guids = ec.get_standard_beam_guid_list()
        >>> origin = cadwork.point_3d(0., 0., 0.)
        >>> x_dir = cadwork.point_3d(1., 0., 0.)
        >>> z_dir = cadwork.point_3d(0., 0., 1.)
        >>> beam_id = ec.create_standard_element_from_guid_vectors(
        ...     guids[0], 3000., origin, x_dir, z_dir
        ... )

    Returns:
        The ID of the created element, or 0 on failure (unknown GUID, length of zero or less, or
        identical X and Z directions).
    """

def fillet_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, radius: float) -> None:
    """Round an edge of an element with a fillet.

    The edge is found by its two end points (in either order). If no edge matches or the operation
    fails, nothing happens and no error is reported. On success the element is marked as modified
    and the display is refreshed. An invalid element ID is silently ignored. Use
    `get_edge_selection()` to let the user pick an edge, and `chamfer_edge()` for a bevel instead of
    a round.

    Parameters:
        element_id: ID of the element that owns the edge.
        edge_start: One end point of the edge, in global coordinates.
        edge_end: The other end point of the edge, in global coordinates.
        radius: Fillet radius in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> edges = ec.get_edge_selection([element_id])
        >>> if edges.count() > 0:
        ...     edge = edges[0]
        ...     ec.fillet_edge(element_id, edge[0], edge[1], 10.)
    """

def chamfer_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, length: float) -> None:
    """Bevel an edge of an element with a 45 degree chamfer.

    The edge is found by its two end points (in either order). If no edge matches or the operation
    fails, nothing happens and no error is reported. On success the element is marked as modified
    and the display is refreshed. An invalid element ID is silently ignored. Use
    `get_edge_selection()` to let the user pick an edge, and `fillet_edge()` for a round instead of
    a bevel.

    Parameters:
        element_id: ID of the element that owns the edge.
        edge_start: One end point of the edge, in global coordinates.
        edge_end: The other end point of the edge, in global coordinates.
        length: Chamfer length in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> edges = ec.get_edge_selection([element_id])
        >>> if edges.count() > 0:
        ...     edge = edges[0]
        ...     ec.chamfer_edge(element_id, edge[0], edge[1], 10.)
    """

def convert_drilling_to_circular_beam(element_id_list: list[ElementId]) -> None:
    """Replace drilling elements with circular beams.

    Each element's machining data is deleted first (cadwork may ask the user for confirmation, which
    blocks the script), then it is replaced by a cylindrical beam with the same start point, length
    and orientation and a diameter equal to the element's height. Colour and other properties are
    copied and the original element is deleted. Invalid IDs are skipped, and nothing is converted if
    the machine data deletion is declined. The reverse operation is
    `convert_circular_beam_to_drilling()`.

    Parameters:
        element_id_list: IDs of the drilling elements to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> drilling_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_drilling_to_circular_beam(drilling_ids)
    """

def convert_lines_to_surfaces(element_id_list: list[ElementId]) -> list[ElementId]:
    """Convert closed line (axis) elements into surface elements.

    Edges of the given line elements are covered with planar surfaces; edges that form closed
    outlines become surfaces. Invalid IDs are skipped. The new surfaces are inserted, shown and
    registered in undo. Use `convert_surfaces_to_volume()` to turn a closed set of surfaces into a
    solid.

    Parameters:
        element_id_list: IDs of the line elements to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> line_ids = ec.get_active_identifiable_element_ids()
        >>> surface_ids = ec.convert_lines_to_surfaces(line_ids)
        >>> print(len(surface_ids), 'surfaces created')

    Returns:
        The IDs of the newly created surface elements. Empty list if the conversion failed or
        produced nothing.
    """

def convert_surfaces_to_volume(element_id_list: list[ElementId]) -> ElementId:
    """Create one volume (solid) element from a set of surface elements.

    The surfaces are sewn together into one solid. Invalid IDs are skipped. The surfaces must form a
    closed shell; otherwise nothing is created and 0 is returned. The new volume is inserted and
    shown. Create suitable surfaces with `create_surface()` or `convert_lines_to_surfaces()`.

    Parameters:
        element_id_list: IDs of the surface elements that together enclose the volume.

    Examples:
        >>> import element_controller as ec

        >>> surface_ids = ec.get_active_identifiable_element_ids()
        >>> volume_id = ec.convert_surfaces_to_volume(surface_ids)
        >>> if volume_id == 0:
        ...     print('The surfaces do not form a closed shell')

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
    nothing happens if no partners are found. All lengths are in mm. The cut is added to undo. A
    corner lap joins two elements that meet at their ends in a corner.

    Parameters:
        element_id_list: IDs of the elements to join, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; they must meet in a corner.
        depth: Depth of the lap cut in each element, in mm.
        clearance_base: Extra clearance at the bottom of the cut, in mm.
        clearance_side: Extra clearance at the side faces of the cut, in mm.
        backcut: Undercut applied to the outer face of the cut, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_corner_lap(element_ids, 40., 1., 1., 0., 0, 0., 0.)
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
    nothing happens if no partners are found. All lengths are in mm. The cut is added to undo. In a
    T lap one element ends against the side of another.

    Parameters:
        element_id_list: IDs of the elements to join, e.g. from
            `element_controller.get_active_identifiable_element_ids()`; one element ends against the
            side of another.
        depth: Depth of the lap cut where the intersecting element is placed, in mm.
        clearance_base: Extra clearance at the bottom of the cut, in mm.
        clearance_side: Extra clearance at the side faces of the cut, in mm.
        backcut: Undercut applied to improve fitting, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_t_lap(element_ids, 40., 1., 1., 0., 0, 0., 0.)
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
    nothing happens if no partners are found. All lengths are in mm. The cut is added to undo. In a
    cross lap two elements cross each other and both are notched.

    Parameters:
        element_id_list: IDs of the crossing elements, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        depth: Depth of the lap cut in each element, in mm; typically half the element thickness.
        clearance_base: Extra clearance at the bottom of the cut, in mm.
        clearance_side: Extra clearance at the side walls of the cut, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_cross_lap(element_ids, 40., 1., 1., 0, 0., 0.)
    """

def delete_processes_keep_cutting_bodies(
    element_id_list: list[ElementId], keep_cutting_elements_only: bool
) -> list[ElementId]:
    """Remove machining processes from elements and keep their cutting bodies as elements.

    Works like Ctrl+D in cadwork: the cuts, drillings and other processes are removed from the
    elements and the removed geometry can be kept as separate elements. Invalid IDs are skipped. A
    confirmation may be requested from the user before machine data is deleted. The elements are
    marked as modified and the display is refreshed.

    Parameters:
        element_id_list: IDs of the elements to remove processes from, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        keep_cutting_elements_only: If True, only the bodies of cutting elements are kept and
            returned; if False, all removed process geometry is kept.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> body_ids = ec.delete_processes_keep_cutting_bodies(element_ids, True)
        >>> print(len(body_ids), 'cutting bodies kept')

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

    Joint partners are detected automatically among the listed elements. Invalid IDs are skipped,
    and nothing happens if fewer than two elements are given. All lengths are in mm.

    Parameters:
        element_id_list: IDs of the elements to join (at least 2), e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        depth1: Depth of the first tenon shoulder, in mm.
        depth2: Depth of the second tenon shoulder, in mm.
        clearance: Extra clearance around the tenons, in mm.
        backcut: Undercut applied to avoid surface interference, in mm.
        drilling_count: Number of drill holes (bolts) for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_double_tenon(element_ids, 20., 20., 1., 0., 0, 0., 0.)
    """

def get_coordinate_system_data_nesting_child(
    nesting_parent_id: ElementId, nesting_child_id: ElementId
) -> coordinate_system_data:
    """Get the placement of a nested child element inside its nesting parent.

    Nesting places parts (children) on raw parts (parents) for production. This returns where the
    child sits on the parent as three points. Returns an empty coordinate_system_data if either ID
    is invalid or the child is not nested in that parent. Use `get_nesting_parent_id()` to find the
    parent of a child.

    Parameters:
        nesting_parent_id: ID of the nesting parent (raw part), e.g. from
            `element_controller.get_nesting_parent_id()`.
        nesting_child_id: ID of the nested child element.

    Examples:
        >>> import element_controller as ec

        >>> child_id = ec.get_active_identifiable_element_ids()[0]
        >>> parent_id = ec.get_nesting_parent_id(child_id)
        >>> if parent_id != 0:
        ...     data = ec.get_coordinate_system_data_nesting_child(parent_id, child_id)
        ...     origin = data.get_p1()

    Returns:
        A coordinate_system_data with three points: the child's origin on the parent (point 1), a
        point along its length axis at the child's length from the origin (point 2), and a point one
        unit along its Z axis from the origin (point 3). Empty on failure.
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

    Joint partners are detected automatically among the listed elements and joined end to end.
    Machine data of the elements is deleted first (a confirmation may be requested), invalid IDs are
    skipped and all lengths are in mm. The cut is added to undo and the view is redrawn.

    Parameters:
        element_id_list: IDs of the elements to join, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Length of the half lap along the element axis, in mm.
        clearance_length: Extra clearance along the length of the cut, in mm.
        clearance_depth: Extra clearance in the depth direction, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_half_lap(element_ids, 200., 1., 1., 0, 0., 0.)
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

    Joint partners are detected automatically among the listed elements and joined end to end.
    Machine data of the elements is deleted first (a confirmation may be requested), invalid IDs are
    skipped and all lengths are in mm. The cut is added to undo and the view is redrawn.

    Parameters:
        element_id_list: IDs of the elements to join end to end, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Distance between the two starting points of the cut, in mm.
        depth: Depth of the initial straight cut before the diagonal cut begins, in mm.
        clearance_length: Extra length clearance applied along the initial (depth) cut, in mm.
        clearance_depth: Extra depth clearance applied along the diagonal cut, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_simple_scarf(element_ids, 300., 30., 1., 1., 0, 0., 0.)
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

    Joint partners are detected automatically among the listed elements and joined end to end.
    Machine data of the elements is deleted first (a confirmation may be requested), invalid IDs are
    skipped and all lengths are in mm. The cut is added to undo and the view is redrawn.

    Parameters:
        element_id_list: IDs of the elements to join end to end, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Length of the diagonal cut along the element, in mm.
        clearance_length: Extra clearance along the cut length, in mm.
        drilling_count: Number of drill holes for fasteners; 0 for none.
        drilling_diameter: Diameter of each drill hole, in mm.
        drilling_tolerance: Extra tolerance added to the hole size, in mm.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_diagonal_cut(element_ids, 300., 1., 0, 0., 0.)
    """

def get_all_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all elements in the model.

    Returns every element of the current document regardless of visibility or activation, except
    permanently hidden elements. Use `get_visible_identifiable_element_ids()` or
    `get_active_identifiable_element_ids()` to restrict the result.

    Examples:
        >>> import element_controller as ec

        >>> all_ids = ec.get_all_identifiable_element_ids()
        >>> print(len(all_ids), 'elements in the model')

    Returns:
        List of element IDs; empty if the model has none.
    """

def get_visible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all currently visible elements.

    Returns the elements that are shown in the 3D view, whether active or not. Graphical objects
    that exist only for IFC import are ignored. Use `get_invisible_identifiable_element_ids()` for
    the opposite set.

    Examples:
        >>> import element_controller as ec

        >>> visible_ids = ec.get_visible_identifiable_element_ids()
        >>> print(len(visible_ids), 'visible elements')

    Returns:
        List of element IDs; empty if none are visible.
    """

def get_invisible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all currently invisible elements.

    Returns the elements that are currently hidden in the 3D view. Use
    `get_visible_identifiable_element_ids()` for the opposite set, and
    `visualization_controller.set_visible()` to show elements again.

    Examples:
        >>> import element_controller as ec

        >>> hidden_ids = ec.get_invisible_identifiable_element_ids()
        >>> print(len(hidden_ids), 'hidden elements')

    Returns:
        List of element IDs; empty if none.
    """

def get_active_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all active (selected) elements.

    Active elements are the elements currently selected in cadwork. Also includes active container
    blocks, and the container blocks that hold active elements. This is the usual starting point for
    scripts that operate on the user's selection. Use `get_inactive_all_identifiable_element_ids()`
    for the opposite set.

    Examples:
        >>> import element_controller as ec

        >>> active_ids = ec.get_active_identifiable_element_ids()
        >>> if not active_ids:
        ...     print('Nothing selected')

    Returns:
        List of element IDs; empty if nothing is active.
    """

def get_inactive_all_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all inactive elements, visible or not.

    Returns all elements that are not active (not selected), except permanently hidden elements. Use
    `get_inactive_visible_identifiable_element_ids()` to restrict it to visible elements.

    Examples:
        >>> import element_controller as ec

        >>> inactive_ids = ec.get_inactive_all_identifiable_element_ids()
        >>> print(len(inactive_ids), 'inactive elements')

    Returns:
        List of element IDs; empty if none.
    """

def get_inactive_visible_identifiable_element_ids() -> list[ElementId]:
    """Get the IDs of all elements that are visible but not active.

    Graphical objects that exist only for IFC import are ignored. The returned list may be padded at
    the end with 0 values; filter out every ID equal to 0 before using the result. Use
    `get_inactive_all_identifiable_element_ids()` to include hidden elements.

    Examples:
        >>> import element_controller as ec

        >>> ids = ec.get_inactive_visible_identifiable_element_ids()
        >>> inactive_visible_ids = [element_id for element_id in ids if element_id != 0]

    Returns:
        List of element IDs, possibly followed by trailing 0 entries; empty if none.
    """

def check_if_point_is_in_element(point: point_3d, element_id: ElementId) -> bool:
    """Check whether a point lies inside an element's body.

    A point exactly on the surface is not inside; use `check_if_point_is_on_element()` for that.
    Returns False for an invalid element ID.

    Parameters:
        point: Point to test, in global coordinates (mm).
        element_id: ID of the element to test against, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> point = cadwork.point_3d(500., 50., 100.)
        >>> if ec.check_if_point_is_in_element(point, element_id):
        ...     print('Point is inside the element')

    Returns:
        True if the point is strictly inside the element, otherwise False.
    """

def check_if_point_is_on_element(point: point_3d, element_id: ElementId) -> bool:
    """Check whether a point lies on the surface of an element.

    A point inside the body or outside of it gives False; use `check_if_point_is_in_element()` to
    test for inside. Returns False for an invalid element ID.

    Parameters:
        point: Point to test, in global coordinates (mm).
        element_id: ID of the element to test against, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> point = cadwork.point_3d(0., 0., 0.)
        >>> on_surface = ec.check_if_point_is_on_element(point, element_id)

    Returns:
        True if the point is on the element's surface, otherwise False (also if inside or outside).
    """

def get_element_contact_facets(first_id: ElementId, second_id: ElementId) -> facet_list:
    """Get the faces where two elements touch each other.

    Returns the contact areas between the two bodies, one facet per touching face pair. Returns an
    empty list if an ID is invalid, an element has no body, or the elements do not touch; the reason
    is written to the API log only. Use `check_if_elements_are_in_contact()` for a simple yes/no,
    and `get_element_contact_vertices()` for the corner points only.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> first_id, second_id = ec.get_active_identifiable_element_ids()[:2]
        >>> facets = ec.get_element_contact_facets(first_id, second_id)
        >>> print(facets.count(), 'contact faces')

    Returns:
        The contact faces as facets; empty if none.
    """

def get_element_raw_interface_vertices(first_id: ElementId, second_id: ElementId) -> list[point_3d]:
    """Get the corner points of the interface where two elements clash.

    Vertices are collected from the intersection of the clashing faces of the two bodies, without
    duplicates. The result is empty if the elements neither interpenetrate nor touch in a face
    intersection. Both IDs must be valid element IDs; invalid IDs are not checked by this function.
    Use `check_if_elements_are_in_collision()` first if unsure, and `get_element_contact_vertices()`
    for elements that only touch.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> first_id, second_id = ec.get_active_identifiable_element_ids()[:2]
        >>> if ec.check_if_elements_are_in_collision(first_id, second_id):
        ...     points = ec.get_element_raw_interface_vertices(first_id, second_id)

    Returns:
        List of unique interface points in global coordinates; empty if none.
    """

def get_standard_export_solid_list() -> list[str]:
    """Get the names of all standard export solids.

    Standard export solids are entries of the cadwork standard element library. Names are in the
    current cadwork language.

    Examples:
        >>> import element_controller as ec

        >>> names = ec.get_standard_export_solid_list()
        >>> print(len(names), 'standard export solids')

    Returns:
        List of standard export solid names.
    """

def get_standard_container_list() -> list[str]:
    """Get the names of all standard containers.

    Standard containers are entries of the cadwork standard element library. Names are in the
    current cadwork language.

    Examples:
        >>> import element_controller as ec

        >>> names = ec.get_standard_container_list()
        >>> print(len(names), 'standard containers')

    Returns:
        List of standard container names.
    """

def get_standard_beam_list() -> list[str]:
    """Get the names of all standard beams.

    Standard beams are entries of the cadwork standard element library. Names are in the current
    cadwork language and are not unique (only GUIDs are), so the list can contain the same name
    several times. Folders of the library are not handled by the API and are not part of the names.
    Use `get_standard_beam_guid_list()` to identify standard beams unambiguously, e.g. for
    `create_standard_element_from_guid_vectors()`.

    Examples:
        >>> import element_controller as ec

        >>> names = ec.get_standard_beam_list()
        >>> print(len(names), 'standard beams')

    Returns:
        List of standard beam names.
    """

def get_standard_panel_list() -> list[str]:
    """Get the names of all standard panels.

    Standard panels are entries of the cadwork standard element library. Names are in the current
    cadwork language and are not unique (only GUIDs are), so the list can contain the same name
    several times. Folders of the library are not handled by the API and are not part of the names.
    Use `get_standard_panel_guid_list()` to identify standard panels unambiguously, e.g. for
    `create_standard_element_from_guid_vectors()`.

    Examples:
        >>> import element_controller as ec

        >>> names = ec.get_standard_panel_list()
        >>> print(len(names), 'standard panels')

    Returns:
        List of standard panel names.
    """

def get_variant_sibling_element_ids(element_id: ElementId) -> list[ElementId]:
    """Get the IDs of all elements that belong to the same variant as an element.

    A variant is a group of elements that belong together, for example a window or door inserted as
    one unit. The result contains all elements of the variant. Returns an empty list if the ID is
    invalid or the element is not part of a variant.

    Parameters:
        element_id: ID of an element that belongs to a variant, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> sibling_ids = ec.get_variant_sibling_element_ids(element_id)
        >>> print(len(sibling_ids), 'elements in the variant')

    Returns:
        List of element IDs of the variant; empty if none.
    """

def get_reference_element(element_id: ElementId) -> ElementId:
    """Get the reference element of an element.

    Elements that share a production list position number form a group with one reference element,
    the one that carries the machining data. If the element has no such number or no other reference
    is found, the element itself is returned. Returns 0 for an invalid element ID.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> reference_id = ec.get_reference_element(element_id)
        >>> if reference_id == element_id:
        ...     print('The element is its own reference')

    Returns:
        The ID of the reference element (the element's own ID if it is its own reference), or 0 if
        the element ID is invalid.
    """

def get_element_contact_vertices(first_id: ElementId, second_id: ElementId) -> list[point_3d]:
    """Get the corner points of the faces where two elements touch.

    Returns the corner points of the intersection of each touching face pair. Returns an empty list
    if an ID is invalid, an element has no body, or the elements do not touch; the reason is written
    to the API log only. Use `get_element_contact_facets()` for the faces themselves.

    Parameters:
        first_id: ID of the first element.
        second_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> first_id, second_id = ec.get_active_identifiable_element_ids()[:2]
        >>> points = ec.get_element_contact_vertices(first_id, second_id)
        >>> print(len(points), 'contact points')

    Returns:
        List of contact points in global coordinates, for all touching face pairs together
        (duplicates possible); empty if none.
    """

def get_nesting_parent_id(element_id: ElementId) -> ElementId:
    """Get the nesting parent (raw part) of a nested element.

    Nesting places parts on raw parts for production. For a panel this is its nesting parent; for
    any other element it is its linear optimization parent (the raw beam it is cut from). Returns 0
    if the ID is invalid or the element is not nested. Use
    `get_coordinate_system_data_nesting_child()` to get the placement on the parent.

    Parameters:
        element_id: ID of the nested element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> parent_id = ec.get_nesting_parent_id(element_id)
        >>> if parent_id == 0:
        ...     print('The element is not nested')

    Returns:
        The ID of the parent element, or 0 if none.
    """

def check_if_elements_are_in_collision(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check whether two elements overlap each other.

    Returns False if an ID is invalid or an element is a point cloud, caddy object or graphical
    object. Merely touching elements are not a collision; use `check_if_elements_are_in_contact()`
    for that. The reason for False is written to the API log.

    Parameters:
        first_element_id: ID of the first element.
        second_element_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> first_id, second_id = ec.get_active_identifiable_element_ids()[:2]
        >>> if ec.check_if_elements_are_in_collision(first_id, second_id):
        ...     print('The elements overlap')

    Returns:
        True if the elements overlap (including one containing or coinciding with the other, or
        interlocking), otherwise False.
    """

def check_if_elements_are_in_contact(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check whether two elements touch each other.

    Returns False if an ID is invalid or an element is a point cloud, caddy object or graphical
    object. The reason for False is written to the API log. Use `get_element_contact_facets()` to
    get the touching faces and `check_if_elements_are_in_collision()` to test for overlap.

    Parameters:
        first_element_id: ID of the first element.
        second_element_id: ID of the second element.

    Examples:
        >>> import element_controller as ec

        >>> first_id, second_id = ec.get_active_identifiable_element_ids()[:2]
        >>> if ec.check_if_elements_are_in_contact(first_id, second_id):
        ...     print('The elements touch')

    Returns:
        True if the elements are in contact, otherwise False.
    """

def get_element_module_properties_for_element(element_id: ElementId) -> element_module_properties:
    """Get the element module (detail) properties of an element.

    Element modules (details) are reusable element groups that cadwork inserts into walls and roofs.
    Each element of a module carries properties such as 'top plate', 'cutting element' or
    'distribute in axis direction' that control how it is placed. Returns a properties object with
    all flags unset if the element ID is invalid. Change the properties with
    `set_element_module_properties_for_elements()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> props = ec.get_element_module_properties_for_element(element_id)
        >>> if props.is_auxiliary():
        ...     print('Auxiliary element')

    Returns:
        The element_module_properties of the element; only the properties that are set on it are
        filled in.
    """

def get_element_type_description(element_id: ElementId) -> str:
    """Get the localized type description of an element.

    Returns the type as human readable text in the current cadwork language, for example for a beam
    or a panel. Returns an empty string for an invalid element ID. The text depends on the cadwork
    language, so do not compare it with fixed strings in scripts that run on several installations.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> print(ec.get_element_type_description(element_id))

    Returns:
        The element type description in the current cadwork language; empty string if the ID is
        invalid.
    """

def get_opening_variant_ids(element_id_list: list[ElementId], opening_type: int) -> list[int]:
    """Get the variant IDs of window or door variants used by the given elements.

    A variant is a group of elements, e.g. a window or door, that carries an opening type. Elements
    that are not part of a variant are skipped, as are invalid IDs. Each variant appears at most
    once, in the order of first occurrence. Use `get_variant_sibling_element_ids()` to list the
    elements of one variant.

    Parameters:
        element_id_list: IDs of the elements to look at, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        opening_type: Opening type to keep: 0 = unknown, 1 = window, 2 = door.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> window_variant_ids = ec.get_opening_variant_ids(element_ids, 1)
        >>> print(len(window_variant_ids), 'window variants')

    Returns:
        List of variant IDs (not element IDs) whose opening type matches; empty if none.
    """

def get_parent_container_id(element_id: ElementId) -> ElementId:
    """Get the container that holds an element.

    A container is an element that groups other elements. Returns 0 if the ID is invalid or the
    element is not in a container. Use `get_container_content_elements()` for the reverse direction.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_id = ec.get_active_identifiable_element_ids()[0]
        >>> container_id = ec.get_parent_container_id(element_id)
        >>> if container_id == 0:
        ...     print('The element is not in a container')

    Returns:
        The ID of the parent container, or 0 if none.
    """

def get_export_solid_content_elements(element_id: ElementId) -> list[ElementId]:
    """Get the elements contained in an export solid.

    An export solid is an element that groups other elements for export. Returns an empty list if
    the ID is invalid or the element has no children. There is no type check: for any element the
    list of its child elements is returned. Use `get_standard_export_solid_list()` for the library
    names of standard export solids.

    Parameters:
        element_id: ID of the export solid element.

    Examples:
        >>> import element_controller as ec

        >>> export_solid_id = ec.get_active_identifiable_element_ids()[0]
        >>> child_ids = ec.get_export_solid_content_elements(export_solid_id)
        >>> print(len(child_ids), 'elements in the export solid')

    Returns:
        List of IDs of the child elements; empty if none.
    """

def get_container_content_elements(element_id: ElementId) -> list[ElementId]:
    """Get the elements contained in a container.

    A container is an element that groups other elements. Returns an empty list if the ID is invalid
    or the element has no children. There is no type check: for any element the list of its child
    elements is returned. Use `get_parent_container_id()` for the reverse direction.

    Parameters:
        element_id: ID of the container element.

    Examples:
        >>> import element_controller as ec

        >>> container_id = ec.get_active_identifiable_element_ids()[0]
        >>> child_ids = ec.get_container_content_elements(container_id)
        >>> print(len(child_ids), 'elements in the container')

    Returns:
        List of IDs of the child elements; empty if none.
    """

def get_element_detail_path() -> str:
    """Get the folder where the current document stores its element module (detail) files.

    The path belongs to the currently open document, so it differs between projects. Use it when a
    script has to read or write element module files next to the project data. The folder is not
    created or checked by this call.

    Examples:
        >>> import element_controller as ec

        >>> detail_path = ec.get_element_detail_path()
        >>> print(detail_path)

    Returns:
        Folder path as a string, taken from the paths of the current document.
    """

def get_element_cadwork_guid(element_id: ElementId) -> str:
    """Get the persistent cadwork GUID of an element.

    The GUID stays with the element when the document is saved and reopened, unlike the element ID.
    If the element has no GUID yet, a new one is created and stored on the element, so the first
    call can change the element. Returns an empty string for an invalid element ID. Look an element
    up again by GUID with `element_controller.get_element_from_cadwork_guid()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> for element_id in ec.get_active_identifiable_element_ids():
        ...     guid = ec.get_element_cadwork_guid(element_id)
        ...     if guid:
        ...         print(element_id, guid)
        ...         assert ec.get_element_from_cadwork_guid(guid) == element_id

    Returns:
        The GUID as a string, or an empty string if the element ID is invalid.
    """

def get_bounding_box_vertices_local(reference_element: ElementId, element_id_list: list[ElementId]) -> list[point_3d]:
    """Get the 8 corner points of the bounding box of elements, aligned to a reference element.

    The box edges run along the local axes of the reference element, not along the world axes, and
    the box is measured in that coordinate system. This is useful to get the true oriented size of a
    tilted group of elements. Elements without a solid body (for example dimensions or text) are
    measured by their extent points. Returns an empty list if the reference element ID is invalid or
    has no usable coordinate system, if no element ID in the list is valid, or if the box cannot be
    computed; the reason is written to the API log only. The world-aligned counterpart is
    `element_controller.get_bounding_box_vertices_global()`.

    Parameters:
        reference_element: ID of the element whose local coordinate system orients the box, e.g.
            from `element_controller.get_active_identifiable_element_ids()`.
        element_id_list: List of element IDs to enclose. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> corners = ec.get_bounding_box_vertices_local(element_ids[0], element_ids)
        >>> if corners:
        ...     for corner in corners:
        ...         ec.create_node(corner)

    Returns:
        List of 8 point_3d corner points in global coordinates (model units, mm); empty list on
        failure.
    """

def get_bounding_box_vertices_global(element_id_list: list[ElementId]) -> list[point_3d]:
    """Get the 8 corner points of the bounding box of elements, aligned to the world axes.

    The box edges run along the global X, Y and Z axes and enclose all given elements. Elements
    without a solid body (for example dimensions or text) are measured by their extent points.
    Returns an empty list if no element ID in the list is valid or the box cannot be computed; the
    reason is written to the API log only. For a box oriented on an element use
    `element_controller.get_bounding_box_vertices_local()`.

    Parameters:
        element_id_list: List of element IDs to enclose, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. Invalid IDs are skipped.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> corners = ec.get_bounding_box_vertices_global(element_ids)
        >>> if corners:
        ...     print(f'{len(corners)} corners, first: {corners[0]}')

    Returns:
        List of 8 point_3d corner points in global coordinates (model units, mm); empty list on
        failure.
    """

def get_all_nesting_raw_parts() -> list[ElementId]:
    """Get the IDs of all nesting raw parts in the model.

    Nesting raw parts are the raw boards or sheets that a panel nesting run places parts on. All raw
    parts of the current document are returned, whether or not they are visible or active. Returns
    an empty list when there are none.

    Examples:
        >>> import element_controller as ec

        >>> raw_part_ids = ec.get_all_nesting_raw_parts()
        >>> print(f'{len(raw_part_ids)} nesting raw parts')

    Returns:
        List of element IDs of the raw parts; empty list if there are none.
    """

def get_joined_elements(element_id: ElementId) -> list[ElementId]:
    """Get all elements that are joined (grouped) with an element.

    Joined elements form a join group, which can be selected and moved together. The result contains
    the group partners of the element and the element itself. Returns an empty list if the element
    ID is invalid. Dissolve groups with `element_controller.unjoin_elements()`.

    Parameters:
        element_id: ID of the element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> group_ids = ec.get_joined_elements(element_id)
        >>> print(f'{len(group_ids)} elements in the group of {element_id}')

    Returns:
        List of element IDs of the group including element_id (appended last); empty list if the ID
        is invalid. An element that is not joined returns a list containing only itself.
    """

def check_element_duplicates(element_id_list: list[ElementId]) -> list[ElementId]:
    """Find elements that are exact geometric duplicates of other elements in the list.

    Only visible elements with a valid extent are compared. Two elements count as duplicates when
    they have the same geometry at the same position; of each such pair only the element with the
    higher ID is reported, so the originals are not in the result. Invalid IDs are skipped and the
    elements are not changed. Delete the result with `element_controller.delete_elements()` to
    remove the copies.

    Parameters:
        element_id_list: List of element IDs to compare with each other, e.g. from
            `element_controller.get_visible_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_visible_identifiable_element_ids()
        >>> duplicate_ids = ec.check_element_duplicates(element_ids)
        >>> if duplicate_ids:
        ...     ec.delete_elements(duplicate_ids)

    Returns:
        List of element IDs of the duplicates, without repeats. Empty list if none are found.
    """

def get_elements_in_contact(element_id: ElementId) -> list[ElementId]:
    """Get the elements that are in contact with an element.

    Contact means the other elements touch or overlap the given element; the search runs over the
    elements of the current document. Use `element_controller.get_elements_in_collision()` for the
    narrower set of elements that really clash. Returns an empty list if the element ID is invalid.

    Parameters:
        element_id: ID of the element to check, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> contact_ids = ec.get_elements_in_contact(element_id)
        >>> print(f'{len(contact_ids)} elements touch {element_id}')

    Returns:
        List of IDs of the elements in contact with the element. Empty list if there are none.
    """

def create_text_object_with_options(
    position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, text_options: text_object_options
) -> ElementId:
    """Create a 3D text object from a set of text options.

    For the line, surface and volume text types the text is built from one element per letter, which
    are placed, shown and added to the current scenes. For the raster type a single raster text
    element is created instead. Both direction vectors are normalized internally; the local Y axis
    is derived as Z cross X. Read the options back with
    `element_controller.get_text_object_options()`.

    Parameters:
        position: Origin of the text object in global coordinates (model units, mm).
        x_local_direction: Direction of the text baseline (local X axis).
        z_local_direction: Local Z axis of the text, i.e. the direction the text faces; should be
            perpendicular to x_local_direction.
        text_options: Text content, font, height, element type and other settings, built with
            `cadwork.text_object_options()`.

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
        ID of the last letter element of the created text (raster type: ID of the raster text
        element), or 0 if the text could not be created.
    """

def convert_surfaces_to_roof_surfaces(element_id_list: list[ElementId], roof_name: str) -> None:
    """Convert surface elements to roof surfaces of a named roof.

    Surfaces become roof surfaces of one roof and are assigned to the group named roof_name (the
    group is created if needed). Elements that are neither surfaces nor roof surfaces are skipped,
    as are invalid IDs. If all given elements are already roof surfaces, nothing is converted. After
    conversion a new local coordinate system is created for the roof surfaces, which deletes
    existing machining data on them (this may ask the user for confirmation) and shows a progress
    bar while it runs.

    Parameters:
        element_id_list: List of surface element IDs to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        roof_name: Name of the roof; also used as the group name of the converted surfaces.

    Examples:
        >>> import element_controller as ec

        >>> surface_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_surfaces_to_roof_surfaces(surface_ids, 'Main roof')
    """

def start_standard_element_dialog(standard_element_type: standard_element_type) -> str:
    """Open the standard element selection dialog and return the chosen element.

    Shows the same dialog as the cadwork standard element library and blocks the script until the
    user closes it. The dialog is limited to the given kind of standard element. Use the returned
    GUID with the create_standard_* functions or look up its name with
    `element_controller.get_standard_element_name_from_guid()`.

    Parameters:
        standard_element_type: Kind of standard element to choose from:
            `cadwork.standard_element_type` beam, panel, vba, exportSolid, container or metal.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.start_standard_element_dialog(cadwork.standard_element_type.beam)
        >>> if guid:
        ...     print(ec.get_standard_element_name_from_guid(guid))

    Returns:
        GUID of the selected standard element in braces, or an empty string if nothing was selected
        or the type is unknown.
    """

def remove_standard_connector_axis(guid: str) -> None:
    """Delete a standard connector axis from the standard element library.

    The entry is removed permanently from the library, not only from the current document. Elements
    already created from it stay in the model. Nothing is reported when the GUID is unknown. Look up
    GUIDs with `element_controller.get_standard_element_guid_from_name()` using
    `cadwork.standard_element_type.vba`.

    Parameters:
        guid: GUID of the standard connector axis, in braces, e.g. from
            `element_controller.start_standard_element_dialog()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.get_standard_element_guid_from_name(
        ...     'My axis', cadwork.standard_element_type.vba
        ... )
        >>> if guid:
        ...     ec.remove_standard_connector_axis(guid)
    """

def remove_standard_beam(guid: str) -> None:
    """Delete a standard beam from the standard element library.

    The entry is removed permanently from the library; beams already created from it stay in the
    model. Nothing is reported when the GUID is unknown. Get GUIDs with
    `element_controller.get_standard_beam_guid_list()` or
    `element_controller.get_standard_element_guid_from_name()`.

    Parameters:
        guid: GUID of the standard beam, in braces, e.g. from
            `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.get_standard_element_guid_from_name(
        ...     'My beam', cadwork.standard_element_type.beam
        ... )
        >>> if guid:
        ...     ec.remove_standard_beam(guid)
    """

def remove_standard_panel(guid: str) -> None:
    """Delete a standard panel from the standard element library.

    The entry is removed permanently from the library; panels already created from it stay in the
    model. Nothing is reported when the GUID is unknown. Get GUIDs with
    `element_controller.get_standard_panel_guid_list()` or
    `element_controller.get_standard_element_guid_from_name()`.

    Parameters:
        guid: GUID of the standard panel, in braces, e.g. from
            `element_controller.get_standard_panel_guid_list()`.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.get_standard_element_guid_from_name(
        ...     'My panel', cadwork.standard_element_type.panel
        ... )
        >>> if guid:
        ...     ec.remove_standard_panel(guid)
    """

def remove_standard_container(guid: str) -> None:
    """Delete a standard container from the standard element library.

    The entry is removed permanently from the library; containers already created from it stay in
    the model. Nothing is reported when the GUID is unknown. Get a GUID with
    `element_controller.get_standard_element_guid_from_name()` or
    `element_controller.start_standard_element_dialog()`.

    Parameters:
        guid: GUID of the standard container, in braces.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.get_standard_element_guid_from_name(
        ...     'My container', cadwork.standard_element_type.container
        ... )
        >>> if guid:
        ...     ec.remove_standard_container(guid)
    """

def remove_standard_export_solid(guid: str) -> None:
    """Delete a standard export solid from the standard element library.

    The entry is removed permanently from the library; export solids already created from it stay in
    the model. Nothing is reported when the GUID is unknown. Get a GUID with
    `element_controller.get_standard_element_guid_from_name()` or
    `element_controller.start_standard_element_dialog()`.

    Parameters:
        guid: GUID of the standard export solid, in braces.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> guid = ec.get_standard_element_guid_from_name(
        ...     'My solid', cadwork.standard_element_type.exportSolid
        ... )
        >>> if guid:
        ...     ec.remove_standard_export_solid(guid)
    """

def get_user_element_ids_with_count(count: int) -> list[ElementId]:
    """Let the user pick elements in the 3D view and return their IDs.

    Blocks the script until the user has finished selecting; a prompt is shown in cadwork. Any
    element type can be picked. If the user presses Esc, the elements picked so far (possibly none)
    are returned and an error entry is added to the API error list. Use it for interactive scripts
    that need the user to point at elements instead of using the active selection.

    Parameters:
        count: Maximum number of elements the user may select.

    Examples:
        >>> import element_controller as ec

        >>> picked_ids = ec.get_user_element_ids_with_count(2)
        >>> if len(picked_ids) == 2:
        ...     print('Picked', picked_ids)
        ... else:
        ...     print('Selection cancelled')

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
    """Cut a straight lengthwise scarf joint between elements that meet end to end.

    A lengthwise (scarf) joint connects two timbers that lie on one common axis. The list must
    contain such partners: beams or panels with the same cross-section whose axes are collinear;
    elements without a partner in the list are not cut. Existing machining on the elements is
    deleted first, which may ask the user for confirmation, and the operation is added to undo.
    Invalid IDs are skipped.

    Parameters:
        element_id_list: List of element IDs to cut, containing the end-to-end partners, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Total length of the scarf joint, measured along the element axis (model units, mm).
        depth: Depth of the vertical cut where both sides join (mm).
        clearance_length: Additional clearance in the length direction (mm).
        clearance_depth: Additional clearance in the depth direction (mm).
        clearance_hook: Clearance at the hook or notch feature of the joint (mm).
        drilling_count: Number of holes (for example for bolts or dowels) to drill through the
            joint; 0 for none.
        drilling_diameter: Diameter of each hole (mm).
        drilling_tolerance: Tolerance added to the hole diameter (mm).

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_scarf_straight(
        ...     beam_ids, 400., 60., 2., 2., 5., 2, 16., 1.
        ... )
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
    """Cut a diagonal lengthwise scarf joint between elements that meet end to end.

    A lengthwise (scarf) joint connects two timbers that lie on one common axis. The list must
    contain such partners: beams or panels with the same cross-section whose axes are collinear;
    elements without a partner in the list are not cut. Existing machining on the elements is
    deleted first, which may ask the user for confirmation, and the operation is added to undo.
    Invalid IDs are skipped. Use `element_controller.cut_scarf_with_wedge()` for the variant with a
    wedge.

    Parameters:
        element_id_list: List of element IDs to cut, containing the end-to-end partners, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Total length of the scarf joint, measured along the element axis (model units, mm).
        depth: Depth of the straight section before the diagonal cut begins (mm).
        clearance_length: Additional clearance in the length direction (mm).
        clearance_depth: Additional clearance in the depth direction (mm).
        drilling_count: Number of holes (for example for bolts or dowels) to drill through the
            joint; 0 for none.
        drilling_diameter: Diameter of each hole (mm).
        drilling_tolerance: Tolerance added to the hole diameter (mm).

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_scarf_diagonal(beam_ids, 500., 50., 2., 2., 2, 16., 1.)
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
    """Cut a diagonal lengthwise scarf joint with a wedge between elements that meet end to end.

    A lengthwise (scarf) joint connects two timbers that lie on one common axis. The list must
    contain such partners: beams or panels with the same cross-section whose axes are collinear;
    elements without a partner in the list are not cut. Existing machining on the elements is
    deleted first, which may ask the user for confirmation, and the operation is added to undo.
    Invalid IDs are skipped. Use `element_controller.cut_scarf_diagonal()` for the variant without a
    wedge.

    Parameters:
        element_id_list: List of element IDs to cut, containing the end-to-end partners, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        length: Total length of the scarf joint, measured along the element axis (model units, mm).
        depth: Depth of the straight section before the diagonal cut begins (mm).
        clearance_length: Additional clearance in the length direction (mm).
        clearance_depth: Additional clearance in the depth direction (mm).
        wedge_width: Width of the wedge (mm).
        drilling_count: Number of holes (for example for bolts or dowels) to drill through the
            joint; 0 for none.
        drilling_diameter: Diameter of each hole (mm).
        drilling_tolerance: Tolerance added to the hole diameter (mm).

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_scarf_with_wedge(
        ...     beam_ids, 500., 50., 2., 2., 20., 2, 16., 1.
        ... )
    """

def cut_beam_end_profile(
    element_id_list: list[ElementId], profile_name: str, on_start_face: bool, on_end_face: bool
) -> None:
    """Apply a named end profile to the start and/or end face of beams and panels.

    End profiles are shaped ends (for example rounded or notched) stored in the cadwork profile
    library. The profile is looked up by name; if no profile has that name, nothing changes. The
    profile is set on the start face, the end face or both, depending on the flags. Elements without
    a beam-like face data are skipped, as are invalid IDs. The elements are marked as modified and
    the display is refreshed.

    Parameters:
        element_id_list: List of element IDs to modify, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        profile_name: Name of the end profile in the profile library. Names are compared in natural
            sort order (digits compared as numbers), not by plain text.
        on_start_face: True to apply the profile on the start face of each element.
        on_end_face: True to apply the profile on the end face of each element.

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.cut_beam_end_profile(beam_ids, 'Rounded', True, False)
    """

def create_truncated_cone_beam_points(
    start_diameter: float, end_diameter: float, first_point: point_3d, second_point: point_3d, third_point: point_3d
) -> ElementId:
    """Create a round beam that tapers from a start to an end diameter, defined by points.

    The beam axis runs from first_point to second_point. The local X axis is the direction
    first_point to second_point and the local Z axis points from first_point toward third_point; if
    the two are collinear the orientation is chosen automatically. The beam is inserted, shown and
    added to the current scenes. For vector input use
    `element_controller.create_truncated_cone_beam_vectors()`.

    Parameters:
        start_diameter: Diameter at first_point (model units, mm).
        end_diameter: Diameter at second_point (mm).
        first_point: Start point of the beam axis in global coordinates.
        second_point: End point of the beam axis; sets the length and the X direction.
        third_point: Point that sets the local Z orientation; the direction from first_point to this
            point is used.

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
    The beam is inserted, shown and added to the current scenes. For point input use
    `element_controller.create_truncated_cone_beam_points()`.

    Parameters:
        start_diameter: Diameter at starting_point (model units, mm).
        end_diameter: Diameter at the far end of the beam (mm).
        length: Length of the beam along x_local_direction (mm).
        starting_point: Start point of the beam axis in global coordinates.
        x_local_direction: Direction of the beam axis (local X axis). Use a unit vector: it is
            multiplied by length as given, not normalized.
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

    The spline passes through all given points in order. The line is inserted, shown and added to
    the current scenes. At least two points are required. Build a line from mixed straight, arc and
    spline pieces with `element_controller.create_line_from_segments()`.

    Parameters:
        spline_points: Points the spline passes through, in order, as a `cadwork.vertex_list()`.

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

    Joined (grouped) elements are selected and moved together. This removes the elements from their
    group including all nested groups, so every element becomes independent. Invalid IDs are
    skipped. To keep nested groups intact use `element_controller.unjoin_top_level_elements()`.
    Query a group with `element_controller.get_joined_elements()`.

    Parameters:
        element_id_list: List of element IDs whose join groups are to be dissolved, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if not ec.unjoin_elements(element_ids):
        ...     print('Nothing was unjoined')

    Returns:
        True if the groups were split successfully, False otherwise (for example when nothing could
        be split).
    """

def unjoin_top_level_elements(element_id_list: list[ElementId]) -> bool:
    """Dissolve only the top-level join group of the given elements.

    Joined (grouped) elements are selected and moved together. This dissolves only the outermost
    group of each element; groups nested inside it stay joined. Invalid IDs are skipped. To dissolve
    all levels use `element_controller.unjoin_elements()`.

    Parameters:
        element_id_list: List of element IDs whose top-level join group is to be dissolved, e.g.
            from `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if not ec.unjoin_top_level_elements(element_ids):
        ...     print('Nothing was unjoined')

    Returns:
        True if the group was split successfully, False otherwise.
    """

def set_element_group_single_select_mode() -> None:
    """Make single elements of a group selectable.

    In single-select mode clicking an element selects only that element, even when it is joined to a
    group. The setting is program-wide, not per document, so it also affects interactive selection
    by the user until it is changed back with
    `element_controller.set_element_group_multi_select_mode()`. Read the current mode with
    `element_controller.get_is_element_group_single_select_mode()`.

    Examples:
        >>> import element_controller as ec

        >>> was_single = ec.get_is_element_group_single_select_mode()
        >>> ec.set_element_group_single_select_mode()
        ... # ... let the user pick single elements ...
        >>> if not was_single:
        ...     ec.set_element_group_multi_select_mode()
    """

def set_element_group_multi_select_mode() -> None:
    """Select all elements of a group when one of them is selected.

    In multi-select mode clicking an element of a joined group selects the whole group. The setting
    is program-wide, not per document, so it also affects interactive selection by the user until it
    is changed back with `element_controller.set_element_group_single_select_mode()`. Read the
    current mode with `element_controller.get_is_element_group_multi_select_mode()`.

    Examples:
        >>> import element_controller as ec

        >>> ec.set_element_group_multi_select_mode()
        >>> print(ec.get_is_element_group_multi_select_mode())
    """

def convert_circular_beam_to_drilling(element_id_list: list[ElementId]) -> None:
    """Replace circular beams with drilling elements.

    A drilling is a round hole element; the circular beam is turned into one that has the same
    dimensions, color and properties. Machining on the beams is deleted first, which may ask the
    user for confirmation; if the user declines, nothing is converted. Each beam is replaced by a
    new element, so the original element IDs become invalid and the new elements are not returned.
    Invalid IDs are skipped. The reverse is
    `element_controller.convert_drilling_to_circular_beam()`.

    Parameters:
        element_id_list: List of circular beam element IDs to convert, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> beam_ids = ec.get_active_identifiable_element_ids()
        >>> ec.convert_circular_beam_to_drilling(beam_ids)
        ... # the old IDs are gone; read the new elements from the model again
    """

def slice_elements_with_plane_and_get_new_elements(
    element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float
) -> list[ElementId]:
    """Slice an element with a plane and return the newly created elements.

    The element is cut along the plane and split into separate pieces. The plane consists of all
    points p with dot(p, normal) = distance_from_global_origin. The operation is added to undo,
    except while nesting is active. Only the one given element is cut, even though the function name
    is plural.

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

    Narrower than `element_controller.get_elements_in_contact()`: from the elements in contact, only
    those that overlap, are contained in, abut while contained, or coincide with the element are
    returned, not those that merely touch. Returns an empty list if the element ID is invalid.

    Parameters:
        element_id: ID of the element to check, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> clash_ids = ec.get_elements_in_collision(element_id)
        >>> print(f'{len(clash_ids)} elements collide with {element_id}')

    Returns:
        List of IDs of the colliding elements. Empty list if there are none.
    """

def get_text_object_options(element_id: ElementId) -> 'text_object_options':
    """Get the text options of a text object.

    Reads the content, font, height and other settings that were used to create a text object.
    element_id must be one of the letter elements of a text object, such as the ID returned by
    `element_controller.create_text_object_with_options()`. For any other element no options are
    available and the returned object cannot be used.

    Parameters:
        element_id: ID of a letter element of the text object.

    Examples:
        >>> import element_controller as ec

        >>> [letter_id] = ec.get_active_identifiable_element_ids()
        >>> options = ec.get_text_object_options(letter_id)
        >>> print(options.get_text())

    Returns:
        A `cadwork.text_object_options` with the settings of the text object.
    """

def get_is_element_group_single_select_mode() -> bool:
    """Check whether single elements of a group are selectable.

    Reads the program-wide group selection mode. It is the opposite of
    `element_controller.get_is_element_group_multi_select_mode()`. Change it with
    `element_controller.set_element_group_single_select_mode()`.

    Examples:
        >>> import element_controller as ec

        >>> if ec.get_is_element_group_single_select_mode():
        ...     print('Single elements of a group can be selected')

    Returns:
        True if single-select mode is active, False if selecting an element selects its whole group.
    """

def get_is_element_group_multi_select_mode() -> bool:
    """Check whether selecting an element selects its whole group.

    Reads the program-wide group selection mode. It is the opposite of
    `element_controller.get_is_element_group_single_select_mode()`. Change it with
    `element_controller.set_element_group_multi_select_mode()`.

    Examples:
        >>> import element_controller as ec

        >>> if ec.get_is_element_group_multi_select_mode():
        ...     print('Selecting one element selects its group')

    Returns:
        True if multi-select mode is active, False if single-select mode is active.
    """

def set_shoulder_options(options: shoulder_options) -> None:
    """Set the options used by subsequent cut_shoulder calls.

    A shoulder is a notch in a rafter or strut where it rests on a supporting timber. The options
    replace the stored shoulder cut settings of the program (the same settings as in the shoulder
    joint dialog), which stay in effect until changed again. If the end type name in the options is
    not found among the end types, no end type is assigned. Apply the cut with
    `element_controller.cut_shoulder()`.

    Parameters:
        options: Shoulder cut options, built with `cadwork.shoulder_options()`: depth, toe offset,
            drilling, end type and further settings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> options = cadwork.shoulder_options()
        >>> options.set_shoulder_depth(30.)
        >>> options.set_toe_offset(0.)
        >>> options.set_add_drilling_axis(False)
        >>> ec.set_shoulder_options(options)
    """

def set_heel_shoulder_options(options: heel_shoulder_options) -> None:
    """Set the options used by subsequent cut_heel_shoulder calls.

    A heel shoulder is a combined notch and heel cut at the support of a rafter. The options replace
    the stored heel shoulder cut settings of the program (the same settings as in the joint dialog),
    which stay in effect until changed again. If the end type name in the options is not found among
    the end types, no end type is assigned. Apply the cut with
    `element_controller.cut_heel_shoulder()`.

    Parameters:
        options: Heel shoulder cut options, built with `cadwork.heel_shoulder_options()`: geometry,
            shoulder depth, gap, end type and further settings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> options = cadwork.heel_shoulder_options()
        >>> options.set_shoulder_depth(30.)
        >>> options.set_gap(5.)
        >>> ec.set_heel_shoulder_options(options)
    """

def set_double_shoulder_options(options: double_shoulder_options) -> None:
    """Set the options used by subsequent cut_double_shoulder calls.

    A double shoulder is a stepped notch with two shoulder levels at the support of a rafter. The
    options replace the stored double shoulder cut settings of the program (the same settings as in
    the joint dialog), which stay in effect until changed again. Unlike the other shoulder options
    no end type is part of these settings. Apply the cut with
    `element_controller.cut_double_shoulder()`.

    Parameters:
        options: Double shoulder cut options, built with `cadwork.double_shoulder_options()`: double
            shoulder depth, heel shoulder depth, drilling and further settings.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> options = cadwork.double_shoulder_options()
        >>> options.set_double_shoulder_depth(20.)
        >>> options.set_heel_shoulder_depth(40.)
        >>> ec.set_double_shoulder_options(options)
    """

def cut_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut shoulder joints using the current shoulder options.

    Set the options first with `element_controller.set_shoulder_options()`; the cut uses whatever
    settings are currently stored in the program. Each element is cut against the connecting
    elements. Invalid IDs are skipped. Both lists are marked as modified and the display is
    refreshed.

    Parameters:
        element_id_list: List of element IDs to cut, e.g. rafters.
        connecting_element_id_list: List of the connecting (counterpart) element IDs, e.g. the
            supporting beam, that determine the cut geometry.

    Examples:
        >>> import element_controller as ec

        ... # options set earlier with ec.set_shoulder_options(...)
        >>> rafter_ids = ec.get_active_identifiable_element_ids()
        >>> support_ids = ec.get_visible_identifiable_element_ids()
        >>> ec.cut_shoulder(rafter_ids, support_ids)
    """

def cut_heel_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut heel shoulder joints using the current heel shoulder options.

    Set the options first with `element_controller.set_heel_shoulder_options()`; the cut uses
    whatever settings are currently stored in the program. Each element is cut against the
    connecting elements. Invalid IDs are skipped. Both lists are marked as modified and the display
    is refreshed.

    Parameters:
        element_id_list: List of element IDs to cut, e.g. rafters.
        connecting_element_id_list: List of the connecting (counterpart) element IDs, e.g. the
            supporting beam, that determine the cut geometry.

    Examples:
        >>> import element_controller as ec

        ... # options set earlier with ec.set_heel_shoulder_options(...)
        >>> rafter_ids = ec.get_active_identifiable_element_ids()
        >>> support_ids = ec.get_visible_identifiable_element_ids()
        >>> ec.cut_heel_shoulder(rafter_ids, support_ids)
    """

def cut_double_shoulder(element_id_list: list[ElementId], connecting_element_id_list: list[ElementId]) -> None:
    """Cut double shoulder joints using the current double shoulder options.

    Set the options first with `element_controller.set_double_shoulder_options()`; the cut uses
    whatever settings are currently stored in the program. Each element is cut against the
    connecting elements. Invalid IDs are skipped. Both lists are marked as modified and the display
    is refreshed.

    Parameters:
        element_id_list: List of element IDs to cut, e.g. rafters.
        connecting_element_id_list: List of the connecting (counterpart) element IDs, e.g. the
            supporting beam, that determine the cut geometry.

    Examples:
        >>> import element_controller as ec

        ... # options set earlier with ec.set_double_shoulder_options(...)
        >>> rafter_ids = ec.get_active_identifiable_element_ids()
        >>> support_ids = ec.get_visible_identifiable_element_ids()
        >>> ec.cut_double_shoulder(rafter_ids, support_ids)
    """

def filter_elements(element_id_list: list[ElementId], element_filter: element_filter) -> list[ElementId]:
    """Return the elements of a list that match an element filter.

    Text filters (name, group, subgroup, comment, user attribute, SKU) match the complete value
    exactly, with case. Part and production number filters match the number. Invalid IDs are
    skipped, the input list is not changed, and a filter with no criterion returns an empty list.
    Use `element_controller.map_elements()` to group elements by an attribute instead.

    Parameters:
        element_id_list: List of element IDs to filter, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        element_filter: Filter that defines the attribute and the value to match, built with
            `cadwork.element_filter()` and one of its set_* methods.

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
    IDs are skipped, and a query without a selected attribute returns an empty dictionary. Use
    `element_controller.filter_elements()` to keep only elements with one value.

    Parameters:
        element_id_list: List of element IDs to group, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        map_query: Query that defines the attribute to group by, built with
            `cadwork.element_map_query()` and one of its set_by_* methods.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_map_query = cadwork.element_map_query()
        >>> your_map_query.set_by_subgroup()
        >>> mapped_items = ec.map_elements(ec.get_active_identifiable_element_ids(), your_map_query)
        >>> print(mapped_items)

    Returns:
        Dictionary mapping each attribute value (text) to the list of element IDs having that value.
        Empty dictionary if there is nothing to map.
    """

def cast_ray_and_get_element_intersections(
    element_id_list: list[ElementId], ray_start_position: point_3d, ray_end_position: point_3d, radius: float
) -> hit_result:
    """Cast a ray through the model and get the intersection points per element.

    Only the segment from ray_start_position to ray_end_position is tested, and only against the
    given elements; hits beyond the end point are ignored. Intersection points lie on the ray centre
    line. The result is empty when nothing is hit, so check `get_hit_element_ids()` before reading
    points.

    Parameters:
        element_id_list: List of element IDs to test against the ray, e.g. from
            `element_controller.get_visible_identifiable_element_ids()`.
        ray_start_position: Start point of the ray in global coordinates.
        ray_end_position: End point of the ray; sets the direction and the maximum length.
        radius: Radius of the ray cylinder in model units (mm); a value above 0 tests against a
            thick ray instead of a thin line.

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
        A `cadwork.hit_result` with the IDs of the elements hit and, per element ID, the list of hit
        points. Empty if nothing is hit.
    """

def get_element_active_point(element_id: ElementId) -> active_point_result:
    """Get the active (snapped) point if it belongs to the given element.

    The active point is the snap point that is currently highlighted under the mouse cursor in the
    3D view. It is only returned if the element under the cursor is the given element; otherwise
    has_point is False. Because it depends on the live cursor position, it is mainly useful in
    interactive scripts that run while the user hovers over an element.

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
        An `cadwork.active_point_result` with has_point and point attributes. It evaluates to False
        when there is no active point for the element; point is then (0, 0, 0).
    """

def get_standard_beam_guid_list() -> list[str]:
    """Get the GUIDs of all standard beams.

    Standard beams are the beam entries of the cadwork standard element library. Use the GUIDs with
    `element_controller.get_standard_element_name_from_guid()` to read the display names, or to
    delete an entry with `element_controller.remove_standard_beam()`. Panels are listed by
    `element_controller.get_standard_panel_guid_list()`.

    Examples:
        >>> import element_controller as ec

        >>> for guid in ec.get_standard_beam_guid_list():
        ...     print(guid, ec.get_standard_element_name_from_guid(guid))

    Returns:
        List of GUID strings. Empty list if there are none.
    """

def get_standard_panel_guid_list() -> list[str]:
    """Get the GUIDs of all standard panels.

    Standard panels are the panel entries of the cadwork standard element library. Use the GUIDs
    with `element_controller.get_standard_element_name_from_guid()` to read the display names, or to
    delete an entry with `element_controller.remove_standard_panel()`. Beams are listed by
    `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import element_controller as ec

        >>> for guid in ec.get_standard_panel_guid_list():
        ...     print(guid, ec.get_standard_element_name_from_guid(guid))

    Returns:
        List of GUID strings. Empty list if there are none.
    """

def import_standard_beam_from_file(file_path: str) -> None:
    """Import standard beams from a file into the standard element library.

    Adds the beams stored in the file to the library so they can be used like any other standard
    beam. If the file does not exist, nothing is imported and an error is written to the API log.
    Entries that already exist in the library are ignored, not overwritten. Nothing is returned;
    list the library afterwards with `element_controller.get_standard_beam_guid_list()`.

    Parameters:
        file_path: Full path of the standard element export file to import; use forward slashes or a
            raw string.

    Examples:
        >>> import element_controller as ec

        >>> before = len(ec.get_standard_beam_guid_list())
        >>> ec.import_standard_beam_from_file('C:/exports/my_beams.cwstd')
        >>> after = len(ec.get_standard_beam_guid_list())
        >>> print(f'{after - before} beams imported')
    """

def import_standard_panel_from_file(file_path: str) -> None:
    """Import standard panels from a file into the standard element library.

    Adds the panels stored in the file to the library so they can be used like any other standard
    panel. If the file does not exist, nothing is imported and an error is written to the API log.
    Entries that already exist in the library are ignored, not overwritten. Nothing is returned;
    list the library afterwards with `element_controller.get_standard_panel_guid_list()`.

    Parameters:
        file_path: Full path of the standard element export file to import; use forward slashes or a
            raw string.

    Examples:
        >>> import element_controller as ec

        >>> before = len(ec.get_standard_panel_guid_list())
        >>> ec.import_standard_panel_from_file('C:/exports/my_panels.cwstd')
        >>> after = len(ec.get_standard_panel_guid_list())
        >>> print(f'{after - before} panels imported')
    """

def export_as_standard_element(element_id: ElementId, name: str) -> str:
    """Export an existing element as a new standard element in the library.

    Creates a library entry from the element so it can be reused with the create_standard_*
    functions. Make sure no standard element with this name exists first (see
    `element_controller.get_standard_element_guid_from_name()`); otherwise a count suffix such as
    (2) is appended to the name. Read the final name with
    `element_controller.get_standard_element_name_from_guid()`. Library folders are not supported;
    to order entries, use separators in the name, e.g. Walls - Exterior - 160mm. Metal elements are
    not supported.

    Parameters:
        element_id: ID of the element to export, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        name: Name of the new standard element.

    Examples:
        >>> import element_controller as ec

        >>> [element_id] = ec.get_active_identifiable_element_ids()
        >>> guid = ec.export_as_standard_element(element_id, 'Walls - Exterior - 160mm')
        >>> if guid:
        ...     print(ec.get_standard_element_name_from_guid(guid))

    Returns:
        GUID of the new standard element, or an empty string if the element ID is invalid, the
        element type is unsupported or the export failed. The reason is written to the API log.
    """

def create_rotation_element(
    surface_element_id: ElementId, axis_point: point_3d, axis_direction: point_3d, angle_rad: float, segmentation: int
) -> ElementId:
    """Create a solid by rotating a surface element around an axis.

    The surface is swept around the axis by the given angle, like a lathe. The source surface is
    left unchanged. The new element is created as an auxiliary element, added to the current scenes,
    and gets a local axis whose X axis is the rotation axis. Returns 0 if the element is not a
    surface, the angle is outside the allowed range, or the solid cannot be built.

    Parameters:
        surface_element_id: ID of the surface element to rotate, e.g. created with
            `element_controller.create_surface()`.
        axis_point: A point on the rotation axis in global coordinates.
        axis_direction: Direction of the rotation axis.
        angle_rad: Rotation angle in radians; must be between 1 degree (about 0.0175) and 360
            degrees (2*pi), otherwise 0 is returned.
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

    The image is stored in the document and placed on the surface using the two alignment points,
    which are added to the surface as special additional points. The change is added to undo.
    Returns False without changes if the element is not a surface, the file path is empty or the two
    points are identical (within the default tolerance).

    Parameters:
        element: ID of the surface element, e.g. created with `element_controller.create_surface()`.
        image_file_path: Full path of the image file (.jpg, .png, .bmp or .tif). An empty path is
            rejected; the file type and existence are checked by the image library, not here.
        alignment_start: First alignment point for placing the image on the surface (global
            coordinates).
        alignment_end: Second alignment point; must differ from alignment_start.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> [surface_id] = ec.get_active_identifiable_element_ids()
        >>> start = cadwork.point_3d(0., 0., 0.)
        >>> end = cadwork.point_3d(1000., 0., 0.)
        >>> if not ec.apply_image_to_surface(surface_id, 'C:/images/logo.png', start, end):
        ...     print('Image was not applied')

    Returns:
        True if the image was applied, False otherwise.
    """

def create_line_from_segments(segments: list[element_segment]) -> ElementId:
    """Create a line element from straight, arc and spline segments.

    The first entry must be of type straight and only gives the start point. Each later entry
    continues from the previous end point: straight draws a straight line to position; arc draws an
    arc ending at position and passing through support_position; consecutive spline entries are
    joined into one spline through their positions. The line is inserted, shown and added to the
    current scenes. Read an existing line back with `element_controller.get_line_segments()`.

    Parameters:
        segments: Ordered list of at least two `cadwork.element_segment` entries. Each entry has a
            type (`cadwork.element_segment_type`), a position and, for arcs, a support position.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> straight = cadwork.element_segment_type.straight
        >>> arc = cadwork.element_segment_type.arc
        >>> zero = cadwork.point_3d(0., 0., 0.)
        >>> segments = [
        ...     cadwork.element_segment(straight, zero, zero),
        ...     cadwork.element_segment(straight, cadwork.point_3d(1000., 0., 0.), zero),
        ...     cadwork.element_segment(
        ...         arc, cadwork.point_3d(1500., 500., 0.), cadwork.point_3d(1354., 146., 0.)
        ...     ),
        ... ]
        >>> line_id = ec.create_line_from_segments(segments)
        >>> print(line_id)

    Returns:
        ID of the created line, or 0 if there are fewer than two entries or the first entry is not
        straight.
    """

def get_line_segments(element_id: ElementId) -> list[element_segment]:
    """Get the segments that define a line element.

    The first entry (type straight) is the start point; each following entry is the end point of one
    straight or arc segment, or a spline point. Arc entries carry a point on the arc in
    support_position. The result can be passed to `element_controller.create_line_from_segments()`
    to rebuild the line.

    Parameters:
        element_id: ID of the line element, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec

        >>> [line_id] = ec.get_active_identifiable_element_ids()
        >>> for segment in ec.get_line_segments(line_id):
        ...     print(segment)

    Returns:
        List of `cadwork.element_segment` entries. Empty list if the ID is invalid, the element is
        not a line, or the line contains an edge that is not straight, circular or a spline.
    """

def create_spline_from_surfaces(surface_ids: list[ElementId], order: spline_surface_order, no_twist: bool) -> ElementId:
    """Create a spline volume by skinning a series of surface elements.

    Works like the Spline command of the user interface: a smooth solid is fitted through the
    section surfaces. The sections are sorted internally according to order. The volume is inserted,
    shown and added to the current scenes; the surfaces are left unchanged. Returns 0 and writes the
    reason to the API log on failure. To sweep one section along a path use
    `element_controller.create_spline_from_surface_and_line()`.

    Parameters:
        surface_ids: IDs of the section surfaces, e.g. created with
            `element_controller.create_surface()`; at least two, and all must be surface elements.
        order: `cadwork.spline_surface_order.linear` if the sections follow each other along a run,
            `cadwork.spline_surface_order.circular` if they are arranged around a centre.
        no_twist: True to keep the skin from twisting between consecutive sections.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec

        >>> section_ids = ec.get_active_identifiable_element_ids()
        >>> volume_id = ec.create_spline_from_surfaces(
        ...     section_ids, cadwork.spline_surface_order.linear, True
        ... )
        >>> if volume_id == 0:
        ...     print('Could not create the spline volume')

    Returns:
        ID of the created volume, or 0 if fewer than two IDs are given, an ID is not a surface, or
        the geometry cannot be skinned.
    """

def create_spline_from_surface_and_line(surface_id: ElementId, line_id: ElementId) -> ElementId:
    """Create a spline volume by sweeping a surface element along a line element.

    A copy of the section surface is swept along the path line, producing a solid. The volume is
    inserted, shown and added to the current scenes; the surface and the line are left unchanged.
    Returns 0 and writes the reason to the API log on failure. To skin several sections instead use
    `element_controller.create_spline_from_surfaces()`.

    Parameters:
        surface_id: ID of the section surface; must be a surface element, e.g. created with
            `element_controller.create_surface()`.
        line_id: ID of the path; must be a line element, e.g. created with
            `element_controller.create_spline_line()`.

    Examples:
        >>> import element_controller as ec

        >>> surface_id, line_id = ec.get_active_identifiable_element_ids()
        >>> volume_id = ec.create_spline_from_surface_and_line(surface_id, line_id)
        >>> if volume_id == 0:
        ...     print('Sweep failed, check the section and the path')

    Returns:
        ID of the created volume, or 0 if surface_id is not a surface, line_id is not a line, or the
        sweep fails.
    """

def get_standard_element_guid_from_name(name: str, type: standard_element_type) -> str:
    """Get the GUID of a standard element from its name.

    The name is matched in the current cadwork language. If several standard elements share the
    name, the first match is returned; this is the one the create_standard_* functions use for that
    name. Steel profile names use cadwork notation. Use it before
    `element_controller.export_as_standard_element()` to check that a name is free.

    Parameters:
        name: Name of the standard element. An empty name returns an empty string.
        type: Kind of standard element to search: `cadwork.standard_element_type` beam, panel, vba,
            exportSolid, container or metal (steel).

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
    current cadwork language. Get GUIDs from `element_controller.get_standard_beam_guid_list()`,
    `element_controller.get_standard_panel_guid_list()` or
    `element_controller.start_standard_element_dialog()`.

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
