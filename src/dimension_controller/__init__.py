from typing import List
from cadwork import point_3d


def create_dimension(direction: point_3d, plane_normal: point_3d, distance_from_origin: point_3d, dimension_points: List[point_3d]) -> int:
    """ Creates a 3d dimension


    Examples:
        >>> dimension = create_dimension(point_3d(0,0,1), point_3d(1,0,0), point_3d(0,0,0), [point_3d(0,0,0), point_3d(0,0,1000)])

    Args:
        direction (point_3d): a dimension direction
        plane_normal (point_3d): plane normal
        distance_from_origin (point_3d): distance from origin (0,0,0)
        dimension_points (List[point_3d]): dimension points

    Returns:
        int: element ID
    """


def set_orientation(element_ids: List[int], view_direction: point_3d, view_up_direction: point_3d) -> None:
    """ Sets the orientation of a dimension

    Examples:
        >>> dimension = create_dimension(point_3d(0,0,1), point_3d(1,0,0), point_3d(0,0,0), point_3d(0,0,0), [point_3d(0,0,0), point_3d(0,0,1000)])
        >>> set_orientation([dimension], point_3d(1,0,0).invert(), point_3d(0,0,1))

    Args:
        element_ids (List[int]): dimension element IDs
        view_direction (point_3d): view direction
        view_up_direction (point_3d): view up direction
    """


def add_segment(element: int, point: point_3d) -> None:
    """ Adds a segment to a dimension

    Args:
        element (int): element ID
        point (point_3d): point
    """


def set_precision(element_ids: List[int], precision: int) -> None:
    """ Sets the precision of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        precision (int): precision
    """


def set_text_size(element_ids: List[int], size: float) -> None:
    """ Sets the text size of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        size (float): text size
    """


def set_line_thickness(element_ids: List[int], thickness: float) -> None:
    """ Sets the line thickness of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        thickness (float): line thickness
    """


def set_total_dimension(element_ids: List[int], total_dimension: bool) -> None:
    """ Sets the total dimension of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        total_dimension (bool): total dimension
    """


def set_text_color(element_ids: List[int], color: int) -> None:
    """ Sets the text color of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        color (int): color number
    """


def set_line_color(element_ids: List[int], color: int) -> None:
    """ Sets the line color of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        color (int): color number
    """


def set_default_anchor_length(element_ids: List[int], length: float) -> None:
    """ Sets the default anchor length of a dimension

    Args:
        element_ids (List[int]): dimension element IDs
        length (float): anchor length
    """
