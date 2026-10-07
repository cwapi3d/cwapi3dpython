from typing import Any
from cadwork.element_segment_type import element_segment_type
from cadwork.point_3d import point_3d


class element_segment:
    """element segment."""

    def __init__(self, arg0: element_segment_type, arg1: point_3d, arg2: point_3d) -> None:
        """Initialize a element_segment."""

    type: Any
    """read/write."""
    position: Any
    """read/write."""
    support_position: Any
    """read/write."""
