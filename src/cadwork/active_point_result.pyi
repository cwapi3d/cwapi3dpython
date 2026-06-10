from dataclasses import dataclass
from cadwork.point_3d import point_3d

@dataclass(frozen=True)
class active_point_result:
    """Result of an active point query.

    Attributes:
        has_point: Whether a valid point was found.
        point: The point coordinates, or None if no point was found.
    """

    has_point: bool
    point: point_3d | None = None

    def __bool__(self) -> bool:
        """Returns True if a valid point was found."""
