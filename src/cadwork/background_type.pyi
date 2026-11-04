from enum import IntEnum, unique

@unique
class background_type(IntEnum):
    """How the background of a render view is filled.

    Examples:
        >>> cadwork.background_type.black
        black
    """

    black = 0
    """Plain black."""
    white = 1
    """Plain white."""
    user = 2
    """Plain user-defined color."""
    image = 3
    """Background image chosen in the graphics options dialog."""

    def __int__(self) -> int:
        return self.value
