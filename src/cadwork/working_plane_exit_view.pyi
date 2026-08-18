from enum import IntEnum, unique

@unique
class working_plane_exit_view(IntEnum):
    """working plane exit view

    Examples:
        >>> cadwork.working_plane_exit_view.previous_view
        previous_view
    """

    previous_view = 0
    """Restores the view and controller active before entering."""
    standard_axonometry = 1
    """Standard axonometry."""
    view_positive_x = 2
    """Same view as showViewPositiveX(). GUI label "X"."""
    view_positive_y = 3
    """Same view as showViewPositiveY(). GUI label "-Y"."""
    view_positive_z = 4
    """Same view as showViewPositiveZ(). GUI label "Z"."""
    keep_current_camera = 5
    """Keeps the current camera, in 3d. GUI label "Axo same view"."""

    def __int__(self) -> int:
        return self.value
