class rgb_color:
    """RGB color representation.

    Attributes:
        r: Red component (0-255).
        g: Green component (0-255).
        b: Blue component (0-255).
    """

    r: int
    g: int
    b: int

    def __init__(self, r: int, g: int, b: int) -> None:
        """Initialize an RGB color.

        Parameters:
            r: Red component (0-255).
            g: Green component (0-255).
            b: Blue component (0-255).
        """
