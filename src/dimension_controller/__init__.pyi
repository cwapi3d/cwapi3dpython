from typing import List
from cadwork.point_3d import point_3d
from cadwork.dimension_base_format import dimension_base_format
from cadwork.api_types import *

def create_dimension(xl: point_3d, plane_normal: point_3d, distance: point_3d, dimension_points: List[point_3d]) -> ElementId:
    """Creates a dimension element to measure distances on 3D parts.
       The dimension is drawn on a plane 
       defined by its normal and offset distance. Points added to the dimension are projected 
       onto this plane, and dimension segments are automatically created between consecutive points.

    Parameters:
        xl: The direction vector defining the dimension line axis (the direction of the measurement arrow). Can be aligned with X, Y, Z axes or any 3D direction.
        plane_normal: The normal vector defining the orientation of the dimension plane.
        distance: The offset vector from the dimensioned geometry to where the dimension line is drawn. Can offset in any direction.
        dimension_points:  A list of dimension points to measure. At least 2 points are needed for a valid dimension measurement, but the points can be added later using addSegment(). Points are projected onto the dimension plane.
        
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
        The element id of the created dimension element.
    """

def set_orientation(element_id_list: List[ElementId], view_dir: point_3d, view_dir_up: point_3d) -> None:
    """Sets the orientation of dimension elements.

    Parameters:
        element_id_list: The element id list.
        view_dir: The view direction vector.
        view_dir_up: The view direction up vector.
    """

def add_segment(element_id: ElementId, segment: point_3d) -> None:
    """Adds a new point to a dimension's point list. A dimension segment is automatically 
       created between this point and the previous point. This method can be called multiple times 
       to progressively add more measurement points to the dimension.

    Parameters:
        element_id: The element id. 
        segment: The point to add to the dimension (despite the parameter name, this is a point, not a segment).
    """

def set_precision(element_id_list: List[ElementId], precision: UnsignedInt) -> None:
    """Sets the precision/decimal places of a dimension element.

    Parameters:
        element_id_list: The element id list.
        precision: The precision/decimal places to set.
    """

def set_text_size(element_id_list: List[ElementId], text_size: float) -> None:
    """Sets the text size of a dimension element.

    Parameters:
        element_id_list: The element id list.
        text_size: The text size to set.
    """

def set_line_thickness(element_id_list: List[ElementId], thickness: float) -> None:
    """Sets the line thickness of a dimension element.

    Parameters:
        element_id_list: The element id list.
        thickness: The line thickness to set.
    """

def set_total_dimension(element_id_list: List[ElementId], total: bool) -> None:
    """Set whether the visualisation of the overall dimension is set for a dimension element.

    Parameters:
        element_id_list: The element id list.
        total: True if the visualisation is set, false otherwise.
    """

def set_text_color(element_id_list: List[ElementId], color_id: ColorId) -> None:
    """Sets the text color of a dimension element.

    Parameters:
        element_id_list: The element id list.
        color_id: The color id to set.
    """

def set_line_color(element_id_list: List[ElementId], color_id: ColorId) -> None:
    """Sets the line color of a dimension element.

    Parameters:
        element_id_list: The element id list.
        color_id: The color id to set.
        """

def set_default_anchor_length(element_id_list: List[ElementId], length: float) -> None:
    """Sets the default anchor length of a dimension element.

    Parameters:
        element_id_list: The element id list.
        length: The default anchor length to set.
    """

def set_distance(element_id_list: List[ElementId], distance: point_3d) -> None:
    """Sets the distance vector between the points and the line.

    Parameters:
        element_id_list: The element id list.
        distance: The distance vector to set.
    """

def shift_distance_and_texts(element_id_list: List[ElementId], shifted: bool) -> None:
    """Sets if distance and texts are shifted.

    Parameters:
        element_id_list: The element id list.
        shifted: True if distance and texts are shifted, false otherwise.
    """

def get_dimension_points(element_id: ElementId) -> List[point_3d]:
    """Gets all dimension points ordered by dimension direction.

    Parameters:
        element_id: The element id.

    Returns:
        A list of dimension points.
    """

def get_default_anchor_length(element_id: ElementId) -> float:
    """Gets the default anchor length.

    Parameters:
        element_id: The element id. 

    Returns:
        The default anchor length.
    """

def get_distance(element_id: ElementId) -> point_3d:
    """Get the distance to the dimension reference point. The point is in the plane of the dimensioning.

    Parameters:
        element_id: The element id. 

    Returns:
        The distance vector.
    """

def get_plane_normal(element_id: ElementId) -> point_3d:
    """Get the plane normal.

    Parameters:
        element_id: The element id. 

    Returns:
        The plane normal vector.
    """

def get_plane_xl(element_id: ElementId) -> point_3d:
    """Get the plane x direction.

    Parameters:
        element_id: The element id. 

    Returns:
        The plane x direction vector.
    """

def get_segment_count(element_id: ElementId) -> int:
    """Get count of segments.

    Parameters:
        element_id: The element id. 

    Returns:
        The number of segments.
    """

def get_segment_distance(element_id: ElementId, segment_index: int) -> float:
    """Get the distance from the anchor point to the dimension segment.

    Parameters:
        element_id: The element id.
        segment_index: The segment index.

    Returns:
        The distance from the anchor point to the dimension segment.
    """

def get_segment_direction(element_id: ElementId, segment_index: int) -> point_3d:
    """Get the normalized direction from the anchor point to the point on the dimension.

    Parameters:
        element_id: The element id.
        segment_index: The segment index.

    Returns:
        The segment direction vector.
    """

def get_total_dimension(element_id: ElementId) -> bool:
    """Query whether the visualisation of the overall dimension is set for a dimension element.

    Parameters:
        element_id: The element id. 

    Returns:
        True if the visualisation is set, false otherwise. For elements that are not of type dimension, the return value is per default false.
    """


def get_dimension_base_format(element_id: ElementId) -> dimension_base_format:
    """Get the dimension base format.

    Parameters:
        element_id: The element id. 

    Returns:
        The format used for the dimension. Enum value `None` may indicate that something went wrong while retrieving the value due to e.g. the element not being a valid dimension.
    """
