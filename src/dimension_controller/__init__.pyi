from typing import List
from cadwork import point_3d

def create_dimension(xl: point_3d, plane_normal: point_3d, distance: point_3d, dimension_points: List[point_3d]) -> int:
    """creates a dimension element

    Parameters:
        xl: xl
        plane_normal: plane_normal
        distance: distance
        dimension_points: dimension_points

    Returns:
        elementID of created dimension element
    """

def set_orientation(elements: List[int], view_dir: point_3d, view_dir_up: point_3d) -> None:
    """sets the orientation of a dimension element

    Parameters:
        elements: elements
        view_dir: view_dir
        view_dir_up: view_dir_up

    Returns:
        None
    """

def add_segment(element: int, segment: point_3d) -> None:
    """adds a segment to a dimension element

    Parameters:
        element: element
        segment: segment

    Returns:
        None
    """

def set_precision(elements: List[int], precision: int) -> None:
    """sets the precision/decimal places of a dimension element

    Parameters:
        elements: elements
        precision: precision

    Returns:
        None
    """

def set_text_size(elements: List[int], text_size: float) -> None:
    """sets the text size a dimension element

    Parameters:
        elements: elements
        text_size: text_size

    Returns:
        None
    """

def set_line_thickness(elements: List[int], thickness: float) -> None:
    """sets the line thickness a dimension element

    Parameters:
        elements: elements
        thickness: thickness

    Returns:
        None
    """

def set_total_dimension(elements: List[int], total: bool) -> None:
    """sets if the total dimension is shown in a dimension element

    Parameters:
        elements: elements
        total: total

    Returns:
        None
    """

def set_text_color(elements: List[int], color_id: int) -> None:
    """sets the text color a dimension element

    Parameters:
        elements: elements
        color_id: color_id

    Returns:
        None
    """

def set_line_color(elements: List[int], color_id: int) -> None:
    """sets the line color a dimension element

    Parameters:
        elements: elements
        color_id: color_id

    Returns:
        None
    """

def set_default_anchor_length(elements: List[int], length: float) -> None:
    """sets the default anchor length a dimension element

    Parameters:
        elements: elements
        length: length

    Returns:
        None
    """

def set_distance(elements: List[int], distance: point_3d) -> None:
    """sets the distance vector between the points and the line

    Parameters:
        elements: elements
        distance: distance

    Returns:
        None
    """

def shift_distance_and_texts(elements: List[int], shifted: bool) -> None:
    """sets if distance and texts are shifted

    Parameters:
        elements: elements
        shifted: shifted

    Returns:
        None
    """

def get_dimension_points(element: int) -> List[point_3d]:
    """gets all dimension points ordered by dimension direction

    Parameters:
        element: element

    Returns:
        ICwAPI3DVertexList
    """

def get_default_anchor_length(element: int) -> float:
    """gets the default anchor length

    Parameters:
        element: element

    Returns:
        double
    """

def get_distance(element: int) -> point_3d:
    """Get the distance to the dimension reference point. The point is in the plane of the dimensioning.

    Parameters:
        element: element

    Returns:
        point_3d
    """

def get_plane_normal(element: int) -> point_3d:
    """Get the plane normal

    Parameters:
        element: element

    Returns:
        normal
    """

def get_plane_xl(element: int) -> point_3d:
    """Get the plane x direction

    Parameters:
        element: element

    Returns:
        x direction
    """

def get_segment_count(element: int) -> int:
    """Get count of segments

    Parameters:
        element: element

    Returns:
        segment count
    """

def get_segment_distance(element: int, segment_index: int) -> float:
    """Get the distance from the anchor point to the dimension segment

    Parameters:
        element: element
        segment_index: segment_index

    Returns:
        distance
    """

def get_segment_direction(element: int, segment_index: int) -> point_3d:
    """get segment direction

    Parameters:
        element: element
        segment_index: segment_index

    Returns:
        point_3d
    """

