from typing import Any
from cadwork.element_segment_type import element_segment_type
from cadwork.point_3d import point_3d

class element_segment:
    """element segment."""

    def __init__(self, type: element_segment_type, position: point_3d, support_position: point_3d) -> None:
        """Initialize a element_segment.

        Parameters:
            type: The segment type.
            position: The end point of the segment.
            support_position: The through-point of an arc segment.
        """

    type: Any
    """read/write."""
    position: Any
    """read/write."""
    support_position: Any
    """read/write."""
