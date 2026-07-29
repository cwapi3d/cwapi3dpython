class point_2d:
    """A two-dimensional point or vector with the coordinates u and v.

    Wherever a point_2d is expected, a plain ``(u, v)`` tuple of length 2 may be
    passed instead: it is implicitly converted to a point_2d.
    """

    def __init__(self, u: float = 0., v: float = 0.):
        """
        Initialize an instance of a point_2d.

        Parameters:
            u (float): The u-coordinate of the point.
            v (float): The v-coordinate of the point.
        """
        self.u = u
        self.v = v

    def __eq__(self, other: object) -> bool:
        """
        Check if two points are equal.

        Returns:
            bool: True if equal, False otherwise.
        """

    def __ne__(self, other: object) -> bool:
        """
        Check if two points are not equal.

        Returns:
            bool: True if not equal, False otherwise.
        """

    def __getitem__(self, index: int) -> float:
        """
        Get coordinate by index (0: u, 1: v).

        Returns:
            float: The coordinate value.
        Raises:
            IndexError: If index is out of range.
        """

    def __setitem__(self, index: int, value: float) -> None:
        """
        Set coordinate by index (0: u, 1: v).

        Raises:
            IndexError: If index is out of range.
        """

    def __repr__(self) -> str:
        """
        Return the string representation of the point.

        Returns:
            str: The string representation.
        """
