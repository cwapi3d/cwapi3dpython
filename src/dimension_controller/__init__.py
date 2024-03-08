from typing import List
from cadwork import point_3d

def create_dimension(xl: point_3d, plane_normal: point_3d, distance: point_3d, dimension_points: List[point_3d]) -> int:
    """create dimension
    Args:
        xl ( point_3d): xl
        plane_normal ( point_3d): plane_normal
        distance ( point_3d): distance
        dimension_points ( List[point_3d]): dimension_points

    Returns:
        int
    """

def set_orientation(elements: List[int], view_dir: point_3d, view_dir_up: point_3d) -> None:
    """set orientation
    Args:
        elements ( List[int]): elements
        view_dir ( point_3d): view_dir
        view_dir_up ( point_3d): view_dir_up

    Returns:
        None
    """

def add_segment(element: int, segment: point_3d) -> None:
    """add segment
    Args:
        element ( int): element
        segment ( point_3d): segment

    Returns:
        None
    """

def set_precision(elements: List[int], precision: int) -> None:
    """set precision
    Args:
        elements ( List[int]): elements
        precision ( int): precision

    Returns:
        None
    """

def set_text_size(elements: List[int], text_size: float) -> None:
    """set text size
    Args:
        elements ( List[int]): elements
        text_size ( float): text_size

    Returns:
        None
    """

def set_line_thickness(elements: List[int], thickness: float) -> None:
    """set line thickness
    Args:
        elements ( List[int]): elements
        thickness ( float): thickness

    Returns:
        None
    """

def set_total_dimension(elements: List[int], total: bool) -> None:
    """set total dimension
    Args:
        elements ( List[int]): elements
        total ( bool): total

    Returns:
        None
    """

def set_text_color(elements: List[int], color_id: int) -> None:
    """set text color
    Args:
        elements ( List[int]): elements
        color_id ( int): color_id

    Returns:
        None
    """

def set_line_color(elements: List[int], color_id: int) -> None:
    """set line color
    Args:
        elements ( List[int]): elements
        color_id ( int): color_id

    Returns:
        None
    """

def set_default_anchor_length(elements: List[int], length: float) -> None:
    """set default anchor length
    Args:
        elements ( List[int]): elements
        length ( float): length

    Returns:
        None
    """


def set_distance(elements: List[int], distance: point_3d) -> None:
    """sets the distance vector between the points and the line
    Args:
        elements ( List[int]): elements
        distance ( point_3d): distance

    Returns:
        None
    """

def shift_distance_and_texts(elements: List[int], shifted: bool) -> None:
    """sets if distance and texts are shifted
    Args:
        elements ( List[int]): elements
        shifted ( bool): shifted

    Returns:
        None
    """

def get_dimension_points(element: int) -> List[point_3d]:
    """gets all dimension points ordered by dimension direction
    Args:
        element ( int): element

    Returns:
        ICwAPI3DVertexList (List[point_3d])
    """

def get_default_anchor_length(element: int) -> float:
    """gets the default anchor length
    Args:
        element ( int): element

    Returns:
        double (float)
    """

