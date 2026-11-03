from enum import IntEnum, unique

@unique
class render_view_type(IntEnum):
    """The render view of the 3d window. Each render view keeps its own background setting, as shown per render mode in the graphics options dialog.

    Examples:
        >>> cadwork.render_view_type.wireframe
        wireframe
    """

    wireframe = 0
    """Wireframe view."""
    shading1 = 1
    """Shaded view 1."""
    shading2 = 2
    """Shaded view 2."""
    hidden_line = 3
    """Hidden line view."""
    hidden_line_dashed = 4
    """Hidden line view with dashed hidden edges."""
    drawing2d = 5
    """2d drawing view."""

    def __int__(self) -> int:
        return self.value
