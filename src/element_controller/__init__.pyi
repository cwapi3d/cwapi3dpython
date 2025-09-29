from typing import List, Dict
from cadwork.edge_list import edge_list
from cadwork.element_module_properties import element_module_properties
from cadwork.facet_list import facet_list
from cadwork.point_3d import point_3d
from cadwork.standard_element_type import standard_element_type
from cadwork.text_object_options import text_object_options
from cadwork.coordinate_system_data import coordinate_system_data
from cadwork.element_map_query import element_map_query
from cadwork.element_filter import element_filter
from cadwork.hit_result import hit_result
from cadwork.vertex_list import vertex_list
from cadwork.shoulder_options import shoulder_options
from cadwork.heel_shoulder_options import heel_shoulder_options
from cadwork.double_shoulder_options import double_shoulder_options
from cadwork.api_types import *

def delete_elements(element_id_list: List[ElementId]) -> None:
    """Deletes the specified elements.

    Parameters:
        element_id_list: The element id list.
    """

def join_elements(element_id_list: List[ElementId]) -> None:
    """Joins the specified elements together.
    
    Parameters:
        element_id_list: The element id list.
    """

def join_top_level_elements(element_id_list: List[ElementId]) -> None:
    """Joins the specified top-level elements together.

    Parameters:
        element_id_list: The element id list.
    """

def create_rectangular_beam_points(width: float, height: float, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a rectangular beam using points.

    Parameters:
        width: The width of the beam.
        height: The height of the beam.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The ID of the created rectangular beam.
    """

def create_circular_beam_points(diameter: float, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a circular beam using points.

    Parameters:
        diameter: The diameter of the beam.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The ID of the created circular beam.
    """

def create_square_beam_points(width: float, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a square beam using points.

    Parameters:
        width: The width of the beam.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The ID of the created square beam.
    """

def create_rectangular_beam_vectors(width: float, height: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a rectangular beam using vectors.

    Parameters:
        width: The width of the beam.
        height: The height of the beam.
        length: The length of the beam.
        starting_point: The starting point.
        x_local_direction: The direction of the X-axis.
        z_local_direction: The direction of the Z-axis.

    Examples:
        >>> beam_width = 150.
        >>> beam_height = 300.
        >>> beam_length = 4000.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Direction along height
        >>> beam_id = ec.create_rectangular_beam_vectors(beam_width, beam_height, beam_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created rectangular beam.
    """

def create_circular_beam_vectors(diameter: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a circular beam using vectors.

    Parameters:
        diameter: The diameter of the beam.
        length: The length of the beam.
        starting_point: The starting point of the beam.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> beam_diameter = 100.
        >>> beam_length = 3500.
        >>> origin_point = cadwork.point_3d(200., 200., 200.)
        >>> x_direction = cadwork.point_3d(0., 1., 0.)  # Beam aligned with Y axis
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Z orientation (arbitrary for circular beam)
        >>> beam_id = ec.create_circular_beam_vectors(beam_diameter, beam_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created circular beam.
    """

def create_square_beam_vectors(width: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a square beam using vectors.

    Parameters:
        width: The width of the beam.
        length: The length of the beam.
        starting_point: The starting point of the beam.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> beam_width = 120.
        >>> beam_length = 2800.
        >>> origin_point = cadwork.point_3d(0., 0., 500.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Direction for orientation
        >>> beam_id = ec.create_square_beam_vectors(beam_width, beam_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created square beam.
    """

def create_rectangular_panel_points(width: float, thickness: float, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Create a rectangular panel using points.

    Parameters:
        width: The width of the panel.
        thickness: The thickness of the panel.
        first_point: The first corner point of the panel.
        second_point: The second corner point of the panel.
        third_point: The third corner point of the panel.

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
        The ID of the created rectangular panel.
    """

def create_rectangular_panel_vectors(width: float, thickness: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Create a rectangular panel using vectors.

    Parameters:
        width: The width of the panel.
        thickness: The thickness of the panel.
        length: The length of the panel.
        starting_point: The starting point of the panel.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> panel_width = 1000.
        >>> panel_thickness = 20.
        >>> panel_length = 2000.
        >>> origin_point = cadwork.point_3d(0., 0., 100.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Panel normal direction
        >>> panel_id = ec.create_rectangular_panel_vectors(panel_width, panel_thickness, panel_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created rectangular panel.
    """

def create_drilling_points(diameter: float, first_point: point_3d, second_point: point_3d) -> ElementId:
    """Creates drilling using points.

    Parameters:
        diameter: The diameter of the drilling.
        first_point: The starting point of the drilling.
        second_point: The ending point of the drilling.

    Examples:
        >>> drill_diameter = 30.
        >>> drill_start_pt = cadwork.point_3d(100., 100., 0.)
        >>> drill_end_pt = cadwork.point_3d(100., 100., 200.)
        >>> drilling_id = ec.create_drilling_points(drill_diameter, drill_start_pt, drill_end_pt)

    Returns:
        The ID of the created drilling.
    """

def create_drilling_vectors(diameter: float, length: float, starting_point: point_3d, drilling_direction: point_3d) -> ElementId:
    """Creates drilling using vectors.

    Parameters:
        diameter: The diameter of the drilling.
        length: The length of the drilling.
        starting_point: The starting point of the drilling.
        drilling_direction: The direction of the drilling.

    Examples:
        >>> drill_diameter = 12.
        >>> drill_length = 180.
        >>> drill_start_pt = cadwork.point_3d(200., 200., 50.)
        >>> drill_direction = cadwork.point_3d(0., 0., 1.)  # Drilling in Z direction
        >>> drilling_id = ec.create_drilling_vectors(drill_diameter, drill_length, drill_start_pt, drill_direction)

    Returns:
        The ID of the created drilling.
    """

def create_line_points(first_point: point_3d, second_point: point_3d) -> ElementId:
    """Creates a line using points.

    Parameters:
        first_point: The first point of the line.
        second_point: The second point of the line.

    Examples:
        >>> line_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> line_end_pt = cadwork.point_3d(500., 500., 0.)
        >>> line_id = ec.create_line_points(line_start_pt, line_end_pt)

    Returns:
        The ID of the created line.
    """

def create_line_vectors(length: float, starting_point: point_3d, line_direction: point_3d) -> ElementId:
    """Creates a line using vectors.

    Parameters:
        length: The length of the line.
        starting_point: The starting point of the line.
        line_direction: The direction of the line.

    Examples:
        >>> line_length = 1000.
        >>> line_start_pt = cadwork.point_3d(200., 0., 200.)
        >>> line_direction = cadwork.point_3d(1., 1., 0.).normalized()  # 45 degree line in XY plane
        >>> line_id = ec.create_line_vectors(line_length, line_start_pt, line_direction)

    Returns:
        The ID of the created line.
    """

def create_node(node_position: point_3d) -> ElementId:
    """Creates a node.

    Parameters:
        node_position: The position of the node.

    Examples:
        >>> node_position = cadwork.point_3d(250., 250., 100.)
        >>> node_id = ec.create_node(node_position)

    Returns:
        The ID of the created node.
    """

def solder_elements(element_id_list: List[ElementId]) -> List[ElementId]:
    """Solders elements together.

    Parameters:
        element_id_list: The element id list.

    Returns:
        The list of soldered element IDs.
    """

def convert_beam_to_panel(element_id_list: List[ElementId]) -> None:
    """Converts beams to panels.

    Parameters:
        element_id_list: The element id list.
    """

def convert_panel_to_beam(element_id_list: List[ElementId]) -> None:
    """Converts panels to beams.

    Parameters:
        element_id_list: The element id list.
    """

def delete_all_element_end_types(element_id_list: List[ElementId]) -> None:
    """Deletes all end types of the elements.

    Parameters:
        element_id_list: The element id list.
    """

def delete_all_element_processes(element_id_list: List[ElementId]) -> None:
    """Deletes all processes of the elements.

    Parameters:
        element_id_list: The element id list.
    """

def move_element(element_id_list: List[ElementId], move_vector: point_3d) -> None:
    """Moves the provided element by a specified vector.

    Parameters:
        element_id_list: The element id list.
        move_vector: The vector by which to move the elements.
    """


def create_polygon_beam(polygon_vertices: vertex_list, thickness: float, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a polygon beam.

    Parameters:
        polygon_vertices: The vertices of the polygon.
        thickness: The thickness of the beam.
        x_local_direction: The x local direction of the beam.
        z_local_direction: The z local direction of the beam.

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
        The ID of the created polygon beam.
    """

def create_text_object(text: str, position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, size: float) -> ElementId:
    """Creates a text object.

    Parameters:
        text: The text content.
        position: The position of the text.
        x_local_direction: The x local direction of the text.
        z_local_direction: The z local direction of the text.
        size: The size of the text.

    Examples:
        >>> text_content = "Cadwork API"
        >>> text_position = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Text direction
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Text orientation
        >>> text_height = 200.
        >>> text_id = ec.create_text_object(text_content, text_position, x_direction, z_direction, text_height)

    Returns:
        The ID of the created text object.
    """

def copy_elements(element_id_list: List[ElementId], copy_vector: point_3d) -> List[int]:
    """Copy a list of elements.

    Parameters:
        element_id_list: The element id list.
        copy_vector: The vector by which to copy the elements.

    Returns:
        The IDs of the copied elements.
    """

def rotate_elements(element_id_list: List[ElementId], origin: point_3d, rotation_axis: point_3d, rotation_angle: float) -> None:
    """Rotate the provided elements around a specified axis.

    Parameters:
        element_id_list: The element id list.
        origin: The origin point of the rotation.
        rotation_axis: The axis around which to rotate the elements.
        rotation_angle: The angle by which to rotate the elements un degree.
    """

def subtract_elements(hard_elements: List[ElementId], soft_elements: List[ElementId]) -> List[ElementId]:
    """Subtracts a list of "soft" elements from a list of "hard" elements.

    Parameters:
        hard_elements: The list of "hard" elements.
        soft_elements: The list of "soft" elements.

    Returns:
        The list of resulting elements.
    """

def check_element_id(element_id: ElementId) -> bool:
    """Check if the provided element ID exists.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element ID exists, false otherwise.
    """

def start_element_module_calculation(covers: List[ElementId]) -> None:
    """Starts the calculation of the element module for a list of covers.

    Parameters:
        covers: The list of cover element IDs.
    """

def set_element_detail_path(path: str) -> None:
    """Sets the detail path for the element.

    Parameters:
        path: The detail path.
    """

def get_element_from_cadwork_guid(cadwork_guid: str) -> ElementId:
    """Gets element from cadwork guid.

    Parameters:
        cadwork_guid: The cadwork guid.

    Returns:
        The element ID.
    """

def add_elements_to_undo(element_id_list: List[ElementId], cmd: int) -> None:
    """Add elements to the undo stack.

    Parameters:
        element_id_list: The elements to add.
        cmd: The command associated with the undo.
    """

def make_undo() -> None:
    """Performs an undo operation, reverting the last change made.
    """

def make_redo() -> None:
    """Performs a redo operation, reapplying the last undone change.
    """

def split_elements(element_id_list: List[ElementId]) -> None:
    """Splits elements.

    Parameters:
        element_id_list: The elements to split.
    """

def set_line_to_marking_line(element_id_list: List[ElementId]) -> None:
    """Sets the line to the marking line.

    Parameters:
        element_id_list: The elements to modify.
    """

def set_line_to_normal_line(element_id_list: List[ElementId]) -> None:
    """Sets the line to the normal line.

    Parameters:
        element_id_list: The elements to modify.
    """

def create_auto_export_solid_from_standard(element_id_list: List[ElementId], output_name: str, standard_element_name: str) -> ElementId:
    """Creates an auto export solid from a standard element.

    Parameters:
        element_id_list: The elements to use.
        output_name: The output name.
        standard_element_name: The standard element name.

    Returns:
        The element ID of the created solid.
    """

def set_element_module_properties_for_elements(element_id_list: List[ElementId], properties: element_module_properties) -> None:
    """Sets the element module properties for elements.

    Parameters:
        element_id_list: The elements to modify.
        properties: The properties to set.
    """

def create_text_object_with_font(text: str, position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, size: float, font_name: str) -> ElementId:
    """Creates a text object with a specific font.

    Parameters:
        text: The text to be displayed in the text object.
        position: The position of the text object.
        x_local_direction: The X-axis direction of the text object.
        z_local_direction: The Z-axis direction of the text object.
        size: The size of the text object.
        font_name: The font name.

    Examples:
        >>> text_content = "Custom Text"
        >>> text_position = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Text direction
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Text orientation
        >>> text_height = 150.
        >>> font = "Arial"
        >>> text_id = ec.create_text_object_with_font(text_content, text_position, x_direction, z_direction, text_height, font)

    Returns:
        The element ID of the created text object.
    """

def apply_transformation_coordinate(element_id_list: List[ElementId], old_point: point_3d, old_x_local_direction: point_3d, old_y_local_direction: point_3d, new_point: point_3d, new_x_local_direction: point_3d, new_y_local_direction: point_3d) -> None:
    """Apply transformation coordinate to elements.

    Parameters:
        element_id_list: The elements to modify.
        old_point: The old point.
        old_x_local_direction: The old X local direction.
        old_y_local_direction: The old Y local direction.
        new_point: The new point.
        new_x_local_direction: The new X local direction.
        new_y_local_direction: The new Y local direction.
    """

def delete_elements_with_undo(element_id_list: List[ElementId]) -> None:
    """Deletes the provided elements with undo functionality.

    Parameters:
        element_id_list: The elements to delete.
    """

def add_created_elements_to_undo(element_id_list: List[ElementId]) -> None:
    """Adds created elements to the undo stack.

    Parameters:
        element_id_list: The elements to add.
    """

def add_modified_elements_to_undo(element_id_list: List[ElementId]) -> None:
    """Adds modified elements to the undo stack.

    Parameters:
        element_id_list: The elements to add.
    """

def recreate_elements(element_id_list: List[ElementId]) -> None:
    """Recreate elements based on the provided list.

    Parameters:
        element_id_list: The elements to recreate.
    """

def create_multi_wall(element_id_list: List[ElementId]) -> None:
    """Creates a multi-wall structure.

    Parameters:
        element_id_list: The elements to use in the multi-wall structure.
    """

def get_user_element_ids() -> List[ElementId]:
    """Gets a list of user element IDs.

    Returns:
        The user element IDs.
    """

def get_user_element_ids_with_existing(element_id_list: List[ElementId]) -> List[ElementId]:
    """Retrieve a list of user element IDs that exist in the provided list.

    Parameters:
        element_id_list: The elements to check for existence.

    Returns:
        The list of existing user element IDs.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

def glide_elements(element_id_list: List[ElementId], glide_origin_point: point_3d) -> None:
    """Glides elements to a specified point.

    Parameters:
        element_id_list: The elements to glide.
        glide_origin_point: The glide origin point.
    """

def cut_elements_with_miter(first_id: ElementId, second_id: ElementId) -> bool:
    """Cut two elements with a miter joint.

    Parameters:
        first_id: The ID of the first element.
        second_id: The ID of the second element.

    Returns:
        True if the cut operation was successful, false otherwise.
    """

def cut_element_with_plane(element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """Cut an element with a plane.

    Parameters:
        element_id: The element id.
        cut_plane_normal_vector: The normal vector of the cut plane.
        distance_from_global_origin: The distance from the global origin to the cut plane.

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
        True if the cut operation was successful, false otherwise.
    """

def create_circular_mep(diameter: float, points: List[point_3d]) -> ElementId:
    """Create a circular MEP (Mechanical, Electrical, and Plumbing) element.

    Parameters:
        diameter: The diameter of the circular MEP.
        points: The points defining the circular MEP.

    Returns:
        The ID of the created circular MEP element.
    """

def create_rectangular_mep(width: float, depth: float, points: List[point_3d]) -> ElementId:
    """Create a rectangular MEP (Mechanical, Electrical, and Plumbing) element.

    Parameters:
        width: The width of the rectangular MEP.
        depth: The depth of the rectangular MEP.
        points: The points defining the rectangular MEP.

    Returns:
        The ID of the created rectangular MEP element.
    """

def slice_element_with_plane(element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """Slice an element with a plane.

    Parameters:
        element_id: The element id.
        cut_plane_normal_vector: The normal vector of the cut plane.
        distance_from_global_origin: The distance from the global origin to the slicing plane.

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
        True if the slicing operation was successful, false otherwise.
    """

def create_auto_container_from_standard(element_id_list: List[ElementId], output_name: str, standard_element_name: str) -> ElementId:
    """Create an auto container from a standard element.

    Parameters:
        element_id_list: The list of elements to be used in the auto container.
        output_name: The name of the output.
        standard_element_name: The name of the standard element.

    Returns:
        The id of the created auto container element.
    """

def create_auto_export_solid_from_standard_with_reference(element_id_list: List[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId) -> ElementId:
    """Creates an auto export solid from a standard element with a reference.

    Parameters:
        element_id_list: The list of elements to be used in the export solid.
        output_name: The name of the output.
        standard_element_name: The name of the standard element.
        reference_id: The ID of the reference element.

    Returns:
        The id of the created auto export solid element.
    """

def create_auto_container_from_standard_with_reference(element_id_list: List[ElementId], output_name: str, standard_element_name: str, reference_id: ElementId) -> ElementId:
    """Creates an auto container from a standard element with a reference.

    Parameters:
        element_id_list: The list of elements to be used in the auto container.
        output_name: The name of the output.
        standard_element_name: The name of the standard element.
        reference_id: The ID of the reference element.

    Returns:
        The ID of the created auto container element.
    """


def create_surface(surface_vertices: vertex_list) -> ElementId:
    """Creates a surface from a list of vertices.

    Parameters:
        surface_vertices: The list of vertices defining the surface.

    Examples:
        >>> # Create a rectangular surface
        >>> vertices = cadwork.vertex_list()
        >>> vertices.append(cadwork.point_3d(0., 0., 0.))
        >>> vertices.append(cadwork.point_3d(1000., 0., 0.))
        >>> vertices.append(cadwork.point_3d(1000., 800., 0.))
        >>> vertices.append(cadwork.point_3d(0., 800., 0.))
        >>> surface_id = ec.create_surface(vertices)

    Returns:
        The ID of the created surface element.
    """

def stretch_start_facet(element_id_list: List[ElementId], stretch_vector: point_3d) -> None:
    """Stretch the start facet of the given elements.

    Parameters:
        element_id_list: The list of elements to be stretched.
        stretch_vector: A vector that defines the stretch direction and distance.
    """

def stretch_end_facet(element_id_list: List[ElementId], stretch_vector: point_3d) -> None:
    """Stretch the end facet of the given elements.

    Parameters:
        element_id_list: The list of elements to be stretched.
        stretch_vector: A vector that defines the stretch direction and distance.
    """

def set_export_solid_contents(export_solid_id: ElementId, element_id_list: List[ElementId]) -> None:
    """Sets the contents of an export solid.

    Parameters:
        export_solid_id: The ID of the export solid to set the contents for.
        element_id_list: The list of element IDs to set as the contents of the export solid.
    """

def set_container_contents(container_id: ElementId, element_id_list: List[ElementId]) -> None:
    """Sets the contents of a container.

    Parameters:
        container_id: The ID of the container to set the contents for.
        element_id_list: The list of element IDs to set as the contents of the container.
    """

def set_parent_opening_variants_opening_angle(element_id_list: List[ElementId], angle: float) -> None:
    """Sets the opening angle of the parent opening variants.

    Parameters:
        element_id_list: The list of element IDs to set the opening angle for.
        angle: The opening angle to set.
    """

def mirror_move_elements(element_id_list: List[ElementId], plane: point_3d, plane_distance: float) -> None:
    """Mirrors and moves elements across a plane.

    Parameters:
        element_id_list: The list of element IDs to mirror and move.
        plane: The plane to mirror across.
        plane_distance: The distance from the plane.
    """

def mirror_copy_elements(element_id_list: List[ElementId], plane: point_3d, plane_distance: float) -> List[ElementId]:
    """Copies elements by mirroring them across a plane.

    Parameters:
        element_id_list: The ID of the element to copy.
        plane: The plane to mirror across.
        plane_distance: The distance from the plane.

    Returns:
        The list of IDs of the copied elements.
    """

def reset_element_cadwork_guid(element_id: ElementId) -> None:
    """Sets the Cadwork Guid of an element to NULL.

    Parameters:
        element_id: The element id.
    """

def create_standard_beam_points(standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a standard beam using points.

    Parameters:
        standard_element_name: The name of the standard element.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The ID of the created standard beam.
    """

def create_standard_beam_vectors(standard_element_name: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a standard beam using vectors.

    Parameters:
        standard_element_name: The name of the standard element.
        length: The length of the beam.
        starting_point: The starting point of the beam.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> std_beam_name = "Standard-Timber-100x100"  # Name as found in standard elements library
        >>> beam_length = 2500.
        >>> origin_point = cadwork.point_3d(100., 100., 100.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Orientation vector
        >>> std_beam_id = ec.create_standard_beam_vectors(std_beam_name, beam_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created standard beam.
    """

def create_standard_panel_points(standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a standard panel using points.

    Parameters:
        standard_element_name: The name of the standard element.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

    Examples:
        >>> std_panel_name = "Standard-Panel-27mm"  # Name as found in standard elements library
        >>> panel_corner_pt = cadwork.point_3d(0., 0., 0.)
        >>> panel_width_pt = cadwork.point_3d(1200., 0., 0.)
        >>> # Calculate normal point for panel orientation (assuming Z is up)
        >>> panel_normal = cadwork.point_3d(0., 0., 1.)
        >>> orientation_pt = panel_corner_pt + panel_normal
        >>> std_panel_id = ec.create_standard_panel_points(std_panel_name, panel_corner_pt, panel_width_pt, orientation_pt)

    Returns:
        The id of the created standard panel.
    """

def create_standard_panel_vectors(standard_element_name: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a standard panel using vectors.

    Parameters:
        standard_element_name: The name of the standard element.
        length: The length of the panel.
        starting_point: The starting point of the panel.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> std_panel_name = "Standard-Panel-20mm"  # Name as found in standard elements library
        >>> panel_length = 2400.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(1., 0., 0.)  # Direction along length
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Panel normal direction
        >>> std_panel_id = ec.create_standard_panel_vectors(std_panel_name, panel_length, origin_point, x_direction, z_direction)

    Returns:
        The id of the created standard panel.
    """

def create_standard_steel_points(standard_element_name: str, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a standard steel element using points.

    Parameters:
        standard_element_name: The name of the standard element.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The id of the created standard steel element.
    """

def create_standard_steel_vectors(standard_element_name: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a standard steel element using vectors.

    Parameters:
        standard_element_name: The name of the standard element.
        length: The length of the element.
        starting_point: The starting point of the element.
        x_local_direction: The local X direction vector.
        z_local_direction: The local Z direction vector.

    Examples:
        >>> std_steel_name = "HEA 220"  # Name of standard steel profile from library
        >>> steel_length = 4500.
        >>> origin_point = cadwork.point_3d(200., 0., 200.)
        >>> x_direction = cadwork.point_3d(0., 1., 0.)  # Direction along Y axis
        >>> z_direction = cadwork.point_3d(0., 0., 1.)  # Up direction
        >>> steel_id = ec.create_standard_steel_vectors(std_steel_name, steel_length, origin_point, x_direction, z_direction)

    Returns:
        The id of the created standard steel element.
    """

def move_element_with_undo(element_id_list: List[ElementId], vector: point_3d) -> None:
    """Moves an element with undo functionality.

    Parameters:
        element_id_list: The element id list.
        vector: The vector to move the element.
    """

def create_normal_axis_points(first_point: point_3d, second_point: point_3d) -> ElementId:
    """Creates a normal axis using points.

    Parameters:
        first_point: The first point of the axis.
        second_point: The second point of the axis.

    Examples:
        >>> axis_start_pt = cadwork.point_3d(0., 0., 0.)
        >>> axis_end_pt = cadwork.point_3d(0., 0., 2000.)
        >>> axis_id = ec.create_normal_axis_points(axis_start_pt, axis_end_pt)

    Returns:
        The id of the created normal axis.
    """

def create_normal_axis_vectors(length: float, starting_point: point_3d, axis_direction: point_3d) -> ElementId:
    """Creates a normal axis using vectors.

    Parameters:
        length: The length of the axis.
        starting_point: The starting point of the axis.
        axis_direction: The direction vector of the axis.

    Examples:
        >>> axis_length = 1500.
        >>> axis_start_pt = cadwork.point_3d(200., 200., 0.)
        >>> axis_direction = cadwork.point_3d(1., 0., 0.)  # Direction along X axis
        >>> axis_id = ec.create_normal_axis_vectors(axis_length, axis_start_pt, axis_direction)

    Returns:
        The id of the created normal axis.
    """

def convert_bolt_to_standardconnector(element_id_list: List[ElementId], standard_element_name: str) -> None:
    """Converts bolts to standard connectors.

    Parameters:
        element_id_list: The list of bolts to convert.
        standard_element_name: The name of the standard element.
    """

def extrude_surface_to_auxiliary_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrudes a surface to create an auxiliary element.

    Parameters:
        surface: The surface to extrude.
        vector: The vector to extrude along.

    Returns:
        The id of the created auxiliary element.
    """

def extrude_surface_to_panel_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrudes a surface to create a panel element.

    Parameters:
        surface: The surface to extrude.
        vector: The vector to extrude along.

    Returns:
        The id of the created panel element.
    """

def extrude_surface_to_beam_vector(surface: ElementId, vector: point_3d) -> ElementId:
    """Extrudes a surface to create a beam element.

    Parameters:
        surface: The surface to extrude.
        vector: The vector to extrude along.

    Returns:
        The id of the created beam element.
    """

def convert_container_to_container_block(element_id_list: List[ElementId]) -> None:
    """Converts a container to a container block.

    Parameters:
        element_id_list: The list of elements to convert.
    """

def create_bounding_box_local(reference_element: ElementId, element_id_list: List[ElementId]) -> ElementId:
    """Creates a local bounding box for a list of elements relative to a reference element.

    Parameters:
        reference_element: The ID of the reference element.
        element_id_list: The list of elements for which to create the bounding box. 

    Returns:
        The ID of the created bounding box element.
    """

def create_bounding_box_global(element_id_list: List[ElementId]) -> ElementId:
    """Creates a global bounding box for a list of elements.

    Parameters:
        element_id_list: The list of elements for which to create the bounding box.

    Returns:
        The ID of the created bounding box element.
    """

def convert_auxiliary_to_panel(element_id_list: List[ElementId]) -> None:
    """Converts auxiliary elements to panel.

    Parameters:
        element_id_list: The list of elements to convert.
    """

def convert_auxiliary_to_beam(element_id_list: List[ElementId]) -> None:
    """Converts auxiliary elements to beams.

    Parameters:
        element_id_list: The list of elements to convert.
    """

def auto_set_rough_volume_situation(element_id_list: List[ElementId]) -> None:
    """Automatically sets the rough volume situation for a list of elements.

    Parameters:
        element_id_list: The list of elements to process.
    """

def rough_volume_situation_manual(cover: ElementId, add_partner: List[ElementId], remove_partner: List[ElementId]) -> None:
    """Manually sets the rough volume situation for a cover element.

    Parameters:
        cover: The cover element ID.
        add_partner: The list of partner element IDs to add.
        remove_partner: The list of partner element IDs to remove.
    """

def auto_set_parts_situation(element_id_list: List[ElementId]) -> None:
    """Automatically sets the parts situation for a list of elements.

    Parameters:
        element_id_list: The list of elements to process.
    """

def parts_situation_manual(cover: ElementId, add_childs: List[ElementId], remove_childs: List[ElementId]) -> None:
    """Manually sets the parts situation for a cover element.

    Parameters:
        cover: The cover element ID.
        add_childs: The list of child element IDs to add.
        remove_childs: The list of child element IDs to remove.
    """

def activate_rv_without_situation() -> List[ElementId]:
    """Activates the rough volume situation for elements without a situation.

    Returns:
        The list of IDs of the elements for which the rough volume situation was activated.
    """

def activate_parts_without_situation() -> List[ElementId]:
    """Activates the parts situation for elements without a situation.

    Returns:
        The list of IDs of the elements for which the parts situation was activated.
    """

def add_elements_to_detail(element_id_list: List[ElementId], detail: int) -> None:
    """Adds elements to a detail.

    Parameters:
        element_id_list: The list of elements to be added to the detail.
        detail: The ID of the detail.
    """

def subtract_elements_with_undo(hard_element_id_list: List[ElementId], soft_element_id_list: List[ElementId], with_undo: bool) -> List[ElementId]:
    """Subtracts a list of "soft" elements from a list of "hard" elements with undo functionality.

    Parameters:
        hard_element_id_list: The list of "hard" elements.
        soft_element_id_list: The list of "soft" elements.
        with_undo: Indicate whether the operation should be added to the undo stack.

    Returns:
        The list of elements resulting from the subtraction.
    """

def create_linear_optimization(element_id_list: List[ElementId], optimization_number: int, total_length: float, start_cut: float, end_cut: float, saw_kerf: float, is_production_list: bool) -> ElementId:
    """create linear optimization

    Parameters:
        element_id_list: The list of elements to be optimized.
        optimization_number: The optimization number, nested parent element id.
        total_length: The total length for the optimization.
        start_cut: The start cut for the optimization.
        end_cut: The end cut for the optimization.
        saw_kerf: The saw kerf for the optimization.
        is_production_list: A flag indicating if this is a production list.

    Returns:
        The ID of the created linear optimization element.
    """

def start_element_module_calculation_silently(covers: List[ElementId]) -> None:
    """Starts the calculation of the element module for a list of covers silently (without user interaction).

    Parameters:
        covers: The list of covers for which to start the element module calculation.
    """

def replace_physical_drillings_with_drilling_axes(element_id_list: List[ElementId], mininum_diameter: float, maximum_diameter: float) -> List[ElementId]:
    """Replaces physical drillings with drilling axes based on diameter range.

    Parameters:
        element_id_list: The list of elements to process.
        mininum_diameter: The minimum diameter of the drilling.
        maximum_diameter: The maximum diameter of the drilling.

    Returns:
        The list of IDs of the elements where the replacement was successful.
    """

def cut_element_with_processing_group(soft_element: ElementId, processing: ElementId) -> None:
    """Cuts an element with a processing group.

    Parameters:
        soft_element: The ID of the element to be cut.
        processing: The ID of the processing group.
    """

def add_element_to_detail(element_id_list: List[ElementId], detail: int) -> None:
    """Adds elements to a detail.

    Parameters:
        element_id_list: The list of elements to be added to the detail.
        detail: The ID of the detail.
    """

def convert_elements_to_auxiliary_elements(element_id_list: List[ElementId]) -> None:
    """Converts elements to auxiliary elements.

    Parameters:
        element_id_list: The list of elements to be converted.
    """

def create_circular_axis_points(diameter: float, first_point: point_3d, second_point: point_3d) -> ElementId:
    """Creates a circular axis using points.

    Parameters:
        diameter: The diameter of the circular axis.
        first_point: The first point defining the axis.
        second_point: The second point defining the axis.

    Examples:
        >>> axis_diameter = 50.
        >>> axis_start_pt = cadwork.point_3d(100., 100., 0.)
        >>> axis_end_pt = cadwork.point_3d(100., 100., 300.)
        >>> circular_axis_id = ec.create_circular_axis_points(axis_diameter, axis_start_pt, axis_end_pt)

    Returns:
        The ID of the created circular axis element.
    """

def create_circular_axis_vector(diameter: float, length: float, starting_point: point_3d, axis_direction: point_3d) -> ElementId:
    """Creates a circular axis using a vector.

    Parameters:
        diameter: The diameter of the circular axis.
        length: The length of the circular axis.
        starting_point: The starting point.
        axis_direction: The direction of the X-axis.

    Examples:
        >>> axis_diameter = 60.
        >>> axis_length = 400.
        >>> axis_start_pt = cadwork.point_3d(200., 200., 200.)
        >>> axis_direction = cadwork.point_3d(0., 1., 0.)  # Direction along Y axis
        >>> circular_axis_id = ec.create_circular_axis_vector(axis_diameter, axis_length, axis_start_pt, axis_direction)

    Returns:
        The ID of the created circular axis element.
    """


def create_polygon_panel(polygon_vertices: vertex_list, thickness: float, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a polygon panel.

    Parameters:
        polygon_vertices: The vertices of the polygon.
        thickness: The thickness of the panel.
        x_local_direction: The X-axis direction of the panel.
        z_local_direction: The Z-axis direction of the panel.

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
        The ID of the created polygon panel element.
    """

def cut_elements_with_overmeasure(hard_element_id_list: List[ElementId], soft_element_id_list: List[ElementId]) -> None:
    """Cuts elements with overmeasure.

    Parameters:
        hard_element_id_list: The list of hard elements.
        soft_element_id_list: The list of soft elements.
    """

def cut_log_corner_joint(settings_name: str, element_id_list: List[ElementId]) -> None:
    """Cuts log corner joint.

    Parameters:
        settings_name: The name of the settings to be used for the cut.
        element_id_list: The list of elements to be cut.
    """

def get_edge_selection(element_id_list: List[ElementId]) -> edge_list:
    """Retrieves the edge selection of the provided elements.

    Parameters:
        element_id_list: The list of element IDs.

    Returns:
        The list of edges selected.
    """

def get_facets_with_lasso(element_id_list: List[ElementId]) -> facet_list:
    """Retrieves the facets of elements within a lasso selection.

    Parameters:
        element_id_list: The list of elements to check for facets within the lasso selection.

    Returns:
        The list of facets selected.
    """

def create_standard_element_from_guid_points(guid: str, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a standard element from GUID points.

    Parameters:
        guid: The GUID of the standard element.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

    Returns:
        The id of the created standard element.
    """

def create_standard_element_from_guid_vectors(guid: str, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a standard element from GUID vectors.

    Parameters:
        guid: The GUID of the standard element.
        length: The length of the element.
        starting_point: The starting point of the element.
        x_local_direction: The X-axis direction vector.
        z_local_direction: The Z-axis direction vector.

    Returns:
        The ID of the created standard element.
    """

def fillet_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, radius: float) -> None:
    """Fillet an edge of an element.

    Parameters:
        element_id: The element id.
        edge_start: The start point of the edge.
        edge_end: The end point of the edge.
        radius: The radius of the fillet.
    """

def chamfer_edge(element_id: ElementId, edge_start: point_3d, edge_end: point_3d, length: float) -> None:
    """Chamfers an edge of an element.

    Parameters:
        element_id: The element id.
        edge_start: The start point of the edge.
        edge_end: The end point of the edge.
        length: The length of the chamfer.
    """

def convert_drilling_to_circular_beam(element_id_list: List[ElementId]) -> None:
    """Converts drilling to circular beam.

    Parameters:
        element_id_list: The list of element IDs to convert.
    """

def convert_lines_to_surfaces(element_id_list: List[ElementId]) -> List[ElementId]:
    """Converts lines to surfaces.

    Parameters:
        element_id_list: The list of element IDs to convert.

    Returns:
        The list of element IDs that were converted.
    """

def convert_surfaces_to_volume(element_id_list: List[ElementId]) -> ElementId:
    """Converts surfaces to volume.

    Parameters:
        element_id_list: The list of element IDs to convert.

    Returns:
        The ID of the created volume element.
    """

def cut_corner_lap(element_id_list: List[ElementId], depth: float, clearance_base: float, clearance_side: float, backcut: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a corner-lap joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        depth: The vertical depth of the lap cut applied to each element.
        clearance_base: Additional clearance applied at the bottom (base) of the lap cut for fitting tolerance.
        clearance_side: Additional clearance on the side faces of the cut to prevent tight joints or interference.
        backcut: A small offset or undercut applied to the outer face of the cut to improve fit or reduce friction.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def cut_t_lap(element_id_list: List[ElementId], depth: float, clearance_base: float, clearance_side: float, backcut: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a T-lap joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        depth: The vertical depth of the cut where the intersecting element will be placed.
        clearance_base: Additional clearance at the base (bottom) of the cut to ensure a proper fit.
        clearance_side: Additional clearance on the side faces of the cut to avoid tight fitting.
        backcut: A small offset or undercut applied inward to improve fitting during assembly.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def cut_cross_lap(element_id_list: List[ElementId], depth: float, clearance_base: float, clearance_side: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a cross-lap joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        depth: The vertical depth of the cross-lap cut, typically half the thickness of the material.
        clearance_base: Additional clearance at the bottom of the cut to ensure a proper fit between intersecting elements.
        clearance_side: Additional clearance on the side walls of the cut to prevent tight fits or friction.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def delete_processes_keep_cutting_bodies(element_id_list: List[ElementId], keep_cutting_elements_only: bool) -> List[ElementId]:
    """Gets the cutting bodies of all processes (and deletes processes), like Ctrl+D Action

    Parameters:
        element_id_list: The list of elements to be processed.
        keep_cutting_elements_only: True if the return element id contains only cutting elements, false otherwise.

    Returns:
        The id list of all removed geometry, cuttings bodies.
    """

def cut_double_tenon(element_id_list: List[ElementId], depth1: float, depth2: float, clearance: float, backcut: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cut a double tenon joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        depth1: The depth of the first tenon shoulder.
        depth2: The depth of the second tenon shoulder.
        clearance: Additional clearance applied around the tenons for fitting tolerance during assembly.
        backcut: A small undercut or inward offset to ensure the tenons fit without surface interference.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def get_coordinate_system_data_nesting_child(nesting_parent_id: ElementId, nesting_child_id: ElementId) -> coordinate_system_data:
    """Get the coordinate system of nesting child

    Parameters:
        nesting_parent_id: The nesting parent id.
        nesting_child_id: The nesting child id.

    Returns:
        A global element coordinate-system of the nested child element consisting of a Point1, a Point2 and a Point3. You can get the local placement by subtracting the parent coordinate - system with child coordinate - system.
    """

def cut_half_lap(element_id_list: List[ElementId], length: float, clearance_length: float, clearance_depth: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cut a half-lap joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        length: The length of the half-lap joint along the main axis of the elements.
        clearance_length: Additional clearance along the length of the cut to ensure proper fitting.
        clearance_depth: Additional clearance in the depth direction to avoid tight joints or surface interference.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def cut_simple_scarf(element_id_list: List[ElementId], length: float, depth: float, clearance_length: float, clearance_depth: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cut a simple scarf joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        length: The distance between the two starting points of the cut.
        depth: The vertical depth of the initial straight cut before the diagonal cut begins.
        clearance_length: The additional length clearance applied along the initial (depth) cut.
        clearance_depth: The additional depth clearance applied along the diagonal cut.
        drilling_count: The number of drill holes to be created for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size, typically for fitting the bolt head or allowing easier assembly.
    """

def cut_diagonal_cut(element_id_list: List[ElementId], length: float, clearance_length: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cut a diagonal cut joint with specific parameters.

    Parameters:
        element_id_list: The list of elements to be cut.
        length: The total length of the diagonal cut applied along the element.
        clearance_length: Additional clearance along the cut length to ensure proper fitting between elements.
        drilling_count: The number of drill holes to create for fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: The tolerance applied to the hole size for bolt head clearance or easier insertion.
    """

def get_all_identifiable_element_ids() -> List[ElementId]:
    """Retrieves a list of all identifiable elements.

    Returns:
        A list of all identifiable element IDs.
    """

def get_visible_identifiable_element_ids() -> List[ElementId]:
    """Get a list of all visible identifiable elements.

    Returns:
        A list of IDs of all visible identifiable elements.
    """

def get_invisible_identifiable_element_ids() -> List[ElementId]:
    """Get a list of all invisible identifiable elements.

    Returns:
        A list of IDs of all invisible identifiable elements.
    """

def get_active_identifiable_element_ids() -> List[ElementId]:
    """Get a list of all active identifiable elements.

    Returns:
        A list of IDs of all active identifiable elements.
    """

def get_inactive_all_identifiable_element_ids() -> List[ElementId]:
    """Get a list of all inactive identifiable elements.

    Returns:
        A list of IDs of all inactive identifiable elements.
    """

def get_inactive_visible_identifiable_element_ids() -> List[ElementId]:
    """Get a list of all inactive visible identifiable elements.

    Returns:
        A list of IDs of all inactive visible identifiable elements.
    """

def check_if_point_is_in_element(point: point_3d, element_id: ElementId) -> bool:
    """Check if a point is inside an element.

    Parameters:
        point: The point to check.
        element_id: The ID of the element to check against.

    Returns:
        True if the point is inside the element, false otherwise.
    """

def check_if_point_is_on_element(point: point_3d, element_id: ElementId) -> bool:
    """Check if a point is on the surface of an element.

    Parameters:
        point: The point to check.
        element_id: The ID of the element to check against.

    Returns:
        True if the point is on the surface of the element, false otherwise.
    """

def get_element_contact_facets(first_id: ElementId, second_id: ElementId) -> facet_list:
    """Retrieves the contact facets between two elements.

    Parameters:
        first_id: The ID of the first element.
        second_id: The ID of the second element.

    Returns:
        The list of contact facets between the two elements.
    """

def get_element_raw_interface_vertices(first_id: ElementId, second_id: ElementId) -> List[point_3d]:
    """Get the raw interface vertices between two elements.

    Parameters:
        first_id: The ID of the first element.
        second_id: The ID of the second element.

    Returns:
        The list of raw interface vertices between the two elements.
    """

def get_standard_export_solid_list() -> List[str]:
    """Retrieves a list of standard export solid names.

    Returns:
        The list of standard export solid names.
    """

def get_standard_container_list() -> List[str]:
    """Retrieves a list of standard container names.

    Returns:
        The list of standard container names.
    """

def get_standard_beam_list() -> List[str]:
    """Retrieves a list of standard beam names.

    Returns:
        The list of standard beam names.
    """

def get_standard_panel_list() -> List[str]:
    """Retrieves a list of standard panel names.

    Returns:
        The list of standard panel names.
    """

def get_variant_sibling_element_ids(element_id: ElementId) -> List[ElementId]:
    """Retrieves a list of variant sibling element IDs.

    Parameters:
        element_id: The element id.

    Returns:
        The list of variant sibling element IDs.
    """

def get_reference_element(element_id: ElementId) -> ElementId:
    """Get the reference element for a given element.

    Parameters:
        element_id: The element id.

    Returns:
        The reference element ID.
    """

def get_element_contact_vertices(first_id: ElementId, second_id: ElementId) -> List[point_3d]:
    """Get the contact vertices between two elements.

    Parameters:
        first_id: The ID of the first element.
        second_id: The ID of the second element.

    Returns:
        The list of contact vertices between the two elements.
    """

def get_nesting_parent_id(element_id: ElementId) -> ElementId:
    """Get the parent ID of a nested element.

    Parameters:
        element_id: The element id.

    Returns:
        The ID of the parent element.
    """

def check_if_elements_are_in_collision(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check if two elements are in collision.

    Parameters:
        first_element_id: The ID of the first element.
        second_element_id: The ID of the second element.

    Returns:
        True if the elements are in collision, false otherwise.
    """

def check_if_elements_are_in_contact(first_element_id: ElementId, second_element_id: ElementId) -> bool:
    """Check if two elements are in contact.

    Parameters:
        first_element_id: The ID of the first element.
        second_element_id: The ID of the second element.

    Returns:
        True if the elements are in contact, false otherwise.
    """

def get_element_module_properties_for_element(element_id: ElementId) -> element_module_properties:
    """Retrieves the module properties for a specific element.

    Parameters:
        element_id: The element id.

    Returns:
        The module properties of the element.
    """

def get_element_type_description(element_id: ElementId) -> str:
    """Retrieves the type description of a specific element.

    Parameters:
        element_id: The element id.

    Returns:
        The type description of the element.
    """

def get_opening_variant_ids(element_id_list: List[ElementId], opening_type: int) -> List[int]:
    """Get the opening variant IDs for a list of elements.

    Parameters:
        element_id_list: The list of element IDs.
        opening_type: The type of opening to check for. Unknown = 0, Window = 1, Door = 2.

    Returns:
        The list of opening variant IDs.
    """

def get_parent_container_id(element_id: ElementId) -> ElementId:
    """Get the parent container ID of a nested element.

    Parameters:
        element_id: The element id.

    Returns:
        The ID of the parent element.
    """

def get_export_solid_content_elements(element_id: ElementId) -> List[ElementId]:
    """Get the content elements of an export solid.

    Parameters:
        element_id: The element id.

    Returns:
        The list of content elements.
    """

def get_container_content_elements(element_id: ElementId) -> List[ElementId]:
    """Get the content elements of a container.

    Parameters:
        element_id: The element id.

    Returns:
        The list of content elements.
    """

def get_element_detail_path() -> str:
    """Get the detail path of the element module.

    Returns:
        The detail path of the element module.
    """

def get_element_cadwork_guid(element_id: ElementId) -> str:
    """Get the Cadwork GUID of a specific element.

    Parameters:
        element_id: The element id.

    Returns:
        The Cadwork GUID of the element.
    """

def get_bounding_box_vertices_local(reference_element: ElementId, element_id_list: List[ElementId]) -> List[point_3d]:
    """Retrieves the local bounding box vertices for a list of elements relative to a reference element.

    Parameters:
        reference_element: The ID of the reference element.
        element_id_list: The list of elements for which to retrieve the bounding box vertices.

    Returns:
        The list of vertices representing the local bounding box of the elements.
    """

def get_bounding_box_vertices_global(element_id_list: List[ElementId]) -> List[point_3d]:
    """Get the global bounding box vertices for a list of elements.

    Parameters:
        element_id_list: The list of elements for which to retrieve the bounding box vertices.

    Returns:
        The list of vertices representing the global bounding box of the elements.
    """

def get_all_nesting_raw_parts() -> List[ElementId]:
    """Get a list of all raw parts in a nesting operation.

    Returns:
        The list of IDs of all raw parts in a nesting operation.
    """

def get_joined_elements(element_id: ElementId) -> List[ElementId]:
    """Retrieves the IDs of elements that have been joined with the specified element.

    Parameters:
        element_id: The element id.

    Returns:
        The list of IDs of the joined elements.
    """

def check_element_duplicates(element_id_list: List[ElementId]) -> List[ElementId]:
    """Checks for duplicate elements in the provided list.

    Parameters:
        element_id_list: The list of element IDs to check for duplicates.

    Returns:
        The list of duplicate elements.
    """

def get_elements_in_contact(element_id: ElementId) -> List[ElementId]:
    """Retrieves a list of elements in contact with a specific element.

    Parameters:
        element_id: The ID of the element to check for contact.

    Returns:
        The list of IDs of the elements in contact with the specified element.
    """

def create_text_object_with_options(position: point_3d, x_local_direction: point_3d, z_local_direction: point_3d, text_options: text_object_options) -> ElementId:
    """Creates a text object with the specified options.

    Parameters:
        position: The position of the text object.
        x_local_direction: The X-axis direction of the text object.
        z_local_direction: The Z-axis direction of the text object.
        text_options: The options for the text object.

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
        The ID of the created text object.
    """

def convert_surfaces_to_roof_surfaces(element_id_list: List[ElementId], roof_name: str) -> None:
    """Converts surfaces to roof surfaces.

    Parameters:
        element_id_list: The list of elements to convert.
        roof_name: The name of the roof surface.
    """

def start_standard_element_dialog(standard_element_type: standard_element_type) -> str:
    """Starts the standard element dialogue based on the chosen element type.

    Parameters:
        standard_element_type: The type of the standard element to create.

    Returns:
        The GUID of the selected standard element if the item is valid, else null.
    """

def remove_standard_connector_axis(guid: str) -> None:
    """Removes a standard connector axis.

    Parameters:
        guid: The unique identifier of the standard connector axis to be removed.
    """

def remove_standard_beam(guid: str) -> None:
    """Removes a standard beam.

    Parameters:
        guid: The unique identifier of the standard connector axis to be removed.
    """

def remove_standard_panel(guid: str) -> None:
    """Removes a standard panel.

    Parameters:
        guid: The unique identifier of the standard panel to be removed.
    """

def remove_standard_container(guid: str) -> None:
    """Removes a standard container.

    Parameters:
        guid: The unique identifier of the standard container to be removed.
    """

def remove_standard_export_solid(guid: str) -> None:
    """Removes a standard export solid.

    Parameters:
        guid: The unique identifier of the standard export solid to be removed.
    """

def get_user_element_ids_with_count(count: int) -> List[ElementId]:
    """Retrieves a list of user element IDs.

    Parameters:
        count: The maximal number of elements to select.

    Returns:
        The list of user element IDs.
    """

def cut_scarf_straight(element_id_list: List[ElementId], length: float, depth: float, clearance_length: float, clearance_depth: float, clearance_hook: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a straight scarf joint (lengthwise) with specific parameters.

    Parameters:
        element_id_list: The list of elements to apply the scarf cut to.
        length: The total length of the scarf joint cut, measured along the element’s longitudinal axis.
        depth: The depth of the vertical cut where both side join.
        clearance_length: Additional clearance along the length direction to ensure proper fitting of the joint.
        clearance_depth: Additional clearance in the depth direction to avoid tight fits or interference.
        clearance_hook: Clearance added specifically at the hook or notch feature of the joint, if any.
        drilling_count: The number of holes to be drilled, typically for bolts, pegs, or dowels to reinforce the joint.
        drilling_diameter: The diameter of each drilled hole.
        drilling_tolerance: The tolerance added to the hole size for easier assembly or bolt head fitting.
    """

def cut_scarf_diagonal(element_id_list: List[ElementId], length: float, depth: float, clearance_length: float, clearance_depth: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a diagonal scarf joint (lengthwise) with specific parameters.

    Parameters:
        element_id_list: The list of elements on which the diagonal scarf cut will be applied.
        length: The total length of the scarf joint measured along the element’s axis.
        depth: The vertical depth of the initial straight section before the diagonal cut begins.
        clearance_length: Additional clearance along the length direction to facilitate proper fitting of the joint.
        clearance_depth: Additional clearance along the depth direction to avoid tight joints or misalignment.
        drilling_count: The number of drill holes for mechanical fasteners (e.g., bolts or dowels).
        drilling_diameter: The diameter of each drill hole.
        drilling_tolerance: Tolerance added to the hole diameter for ease of insertion or head fit.
    """

def cut_scarf_with_wedge(element_id_list: List[ElementId], length: float, depth: float, clearance_length: float, clearance_depth: float, wedge_width: float, drilling_count: UnsignedInt, drilling_diameter: float, drilling_tolerance: float) -> None:
    """Cuts a diagonal scarf joint with an added wedge, using specific parameters.

    Parameters:
        element_id_list: The list of elements on which to apply the scarf-with-wedge cut.
        length: The total length of the scarf joint, measured along the main axis of the element.
        depth: The vertical depth of the straight portion of the cut before the diagonal section.
        clearance_length: Additional clearance along the length direction for proper fit of the joint.
        clearance_depth: Additional clearance in the depth direction to avoid interference.
        wedge_width: The width of the wedge feature inserted or carved as part of the joint geometry.
        drilling_count: The number of drill holes used to secure the joint (e.g., for bolts, pegs, or dowels).
        drilling_diameter: The diameter of the drilled holes.
        drilling_tolerance: Tolerance applied to the hole size, often used for easier bolt fitting or head clearance.
    """

def cut_beam_end_profile(element_id_list: List[ElementId], profile_name: str, on_start_face: bool, on_end_face: bool) -> None:
    """Add end profile to beam elements.

    Parameters:
        element_id_list: The list of elements to modify.
        profile_name: The name of the profile to add.
        on_start_face: Cut on the start face?
        on_end_face: Cut on the end face?
    """

def create_truncated_cone_beam_points(start_diameter: float, end_diameter: float, first_point: point_3d, second_point: point_3d, third_point: point_3d) -> ElementId:
    """Creates a truncated cone beam using points.

    Parameters:
        start_diameter: The starting diameter of the beam.
        end_diameter: The ending diameter of the beam.
        first_point: The first point.
        second_point: The second point.
        third_point: The third point.

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
        The ID of the created beam.
    """

def create_truncated_cone_beam_vectors(start_diameter: float, end_diameter: float, length: float, starting_point: point_3d, x_local_direction: point_3d, z_local_direction: point_3d) -> ElementId:
    """Creates a truncated cone beam using vectors.

    Parameters:
        start_diameter: The starting diameter of the beam.
        end_diameter: The ending diameter of the beam.
        length: The length of the beam.
        starting_point: The starting point.
        x_local_direction: The direction of the X-axis.
        z_local_direction: The direction of the Z-axis.

    Examples:
        >>> start_dia = 120.
        >>> end_dia = 80.
        >>> cone_length = 2500.
        >>> origin_point = cadwork.point_3d(0., 0., 0.)
        >>> x_direction = cadwork.point_3d(0., 0., 1.)  # Direction along Z axis
        >>> z_direction = cadwork.point_3d(1., 0., 0.)  # Orientation vector
        >>> cone_id = ec.create_truncated_cone_beam_vectors(start_dia, end_dia, cone_length, origin_point, x_direction, z_direction)

    Returns:
        The ID of the created beam.
    """


def create_spline_line(spline_points: vertex_list) -> ElementId:
    """Creates a spline line.

    Parameters:
        spline_points: The points defining the spline.

    Examples:
        >>> # Create a spline through multiple points
        >>> points = cadwork.vertex_list()
        >>> points.append(cadwork.point_3d(0., 0., 0.))
        >>> points.append(cadwork.point_3d(500., 200., 0.))
        >>> points.append(cadwork.point_3d(1000., 0., 200.))
        >>> points.append(cadwork.point_3d(1500., -100., 100.))
        >>> spline_id = ec.create_spline_line(points)

    Returns:
        The ID of the created spline.
    """

def unjoin_elements(element_id_list: List[ElementId]) -> bool:
    """Unjoins the specified elements.

    Parameters:
        element_id_list: The element id list.

    Returns:
        True if the operation was successful, false if an error occured.
    """

def unjoin_top_level_elements(element_id_list: List[ElementId]) -> bool:
    """Unjoins the specified top-level elements.

    Parameters:
        element_id_list: The element id list.

    Returns:
        True if the operation was successful, false if an error occured.
    """

def set_element_group_single_select_mode() -> None:
    """ Switches the current element group selection mode so that single elements of a group are selectable.
    """

def set_element_group_multi_select_mode() -> None:
    """Switches the current element group selection mode so that all elements of a group are selected when selecting one of it.
    """

def convert_circular_beam_to_drilling(element_id_list: List[ElementId]) -> None:
    """Converts circular beams to drillings.

    Parameters:
        element_id_list: The list of element IDs to convert.
    """

def slice_elements_with_plane_and_get_new_elements(element_id: ElementId, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> List[ElementId]:
    """Slices an element with a plane and returns the new elements.

    Parameters:
        element_id: The ID of the element to be sliced.
        cut_plane_normal_vector: The normal vector of the cutting plane.
        distance_from_global_origin: The distance from the global origin to the cutting plane.

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
       The list of IDs of the new elements created by the slicing operation.
    """

def get_elements_in_collision(element_id: ElementId) -> List[ElementId]:
    """Retrieves a list of elements in collision with a specific element.

    Parameters:
        element_id: The ID of the element to check for collision.

    Returns:
        A list of IDs of the elements in collision with the specified element.
    """

def get_text_object_options(element_id: ElementId) ->'text_object_options':
    """Retrieves the text object options for a specific element e.g. font, text content, etc.

    Parameters:
        element_id: The ID of the element to retrieve options for.

    Returns:
        The text object options for the specified element.
    """

def get_is_element_group_single_select_mode() ->bool:
    """Gets whether the current element group selection mode is setup to select single elements.

    Returns:
        True if the current element group selection mode is set to single select, false otherwise.
    """

def get_is_element_group_multi_select_mode() ->bool:
    """Gets whether the current element group selection mode is setup to select multiple elements.

    Returns:
        True if the current element group selection mode is set to multi select, false otherwise.
    """


def set_shoulder_options(options: shoulder_options) -> None:
    """Sets the shoulder cut options.

    Parameters:
        options: The shoulder options to set.
    """


def set_heel_shoulder_options(options: heel_shoulder_options) -> None:
    """Sets the heel shoulder cut options.

    Parameters:
        options: The heel shoulder options to set.
    """


def set_double_shoulder_options(options: double_shoulder_options) -> None:
    """Sets the double shoulder cut options.

    Parameters:
        options: The double shoulder options to set.
    """

def cut_shoulder(element_id_list: List[ElementId], connecting_element_id_list:
    List[ElementId]) ->None:
    """Cuts shoulder with current 3D options.

    Parameters:
        element_id_list: The element id list.
        connecting_element_id_list: The list of elements that intersect or connect with the cut elements, used to determine the cutting geometry.
    """

def cut_heel_shoulder(element_id_list: List[ElementId],
    connecting_element_id_list: List[ElementId]) ->None:
    """Cuts heel with current 3D options

    Parameters:
        element_id_list: The element id list.
        connecting_element_id_list: The list of elements that intersect or connect with the cut elements, used to determine the cutting geometry.
    """

def cut_double_shoulder(element_id_list: List[ElementId],
    connecting_element_id_list: List[ElementId]) ->None:
    """Cuts a double shoulder joint using the current 3D cutting options.

    Parameters:
        element_id_list: The element id list.
        connecting_element_id_list: The list of elements that intersect or connect with the cut elements, used to determine the cutting geometry.
    """


def filter_elements(element_id_list: List[ElementId], element_filter: element_filter) -> List[ElementId]:
    """Filters a list of elements based on a provided filter.

    Parameters:
        element_id_list: The list of elements to filter.
        element_filter: The filter to apply to the list of elements.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_element_filter = cadwork.element_filter()
        >>> your_element_filter.set_name("beam")
        >>> filtered_elements = ec.filter_elements(ec.get_active_identifiable_element_ids(), your_element_filter)
        >>> print(filtered_elements)

    Returns:
        The filtered list of element IDs.
    """


def map_elements(element_id_list: List[ElementId], map_query: element_map_query) -> Dict[str, List[ElementId]]:
    """Maps a list of elements based on a provided map query.

    Parameters:
        element_id_list: The list of elements to map.
        map_query: The map query to apply to the list of elements.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_map_query = cadwork.element_map_query()
        >>> your_map_query.set_by_subgroup()
        >>> mapped_items = ec.map_elements(ec.get_active_identifiable_element_ids(), your_map_query)
        >>> print(mapped_items)

    Returns:
        The map of elements that pass the map query.
    """


def cast_ray_and_get_element_intersections(element_id_list: List[ElementId], ray_start_position: point_3d,
                                           ray_end_position: point_3d, radius: float) -> hit_result:
    """Casts a ray through the 3D model and calculates all intersection points between the ray and specified elements. This function performs ray casting against each specified element to find intersection points.For each element hit by the ray, it returns the element ID and all points where the ray intersects with that element. The ray is defined by a start point, end point, and radius.

    Parameters:
        element_id_list: List of element IDs to test against the ray.
        ray_start_position: 3D start point of the ray.
        ray_end_position: 3D end point of the ray.
        radius: Radius of the ray cylinder (allows testing against a volume rather than just a line).

    Examples:
        >>> import element_controller as ec
        >>> from cadwork import point_3d
        >>> ray_start = point_3d(0, 0, 0)
        >>> ray_end = point_3d(1000, 0, 0)
        >>> hit_result = ec.cast_ray_and_get_element_intersections(ec.get_active_identifiable_element_ids(), ray_start, ray_end, 40.0)
        >>> print(hits.get_hit_element_ids())
        >>> for element in hits.get_hit_element_ids():
        >>>     print(f"ElementID {element}: {hits.get_hit_vertices_by_element(element)}")
        >>>     for pos in hits.get_hit_vertices_by_element(element):
        >>>         ec.create_node(pos)

    Returns:
        Contains list of elements that were hit by the ray and list of vertices that are queried via ElementID.
    """
