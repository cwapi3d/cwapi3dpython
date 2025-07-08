class point_3d:
    def __init__(self, x: float, y: float, z: float):
        """
        Initialize an instance of a point_3d.

        Parameters:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
            z (float): The z-coordinate of the point.
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'point_3d') -> 'point_3d':
        """
        Add two points component-wise.

        Returns:
            point_3d: The sum of two points.
        """

    def __sub__(self, other: 'point_3d') -> 'point_3d':
        """
        Subtract two points component-wise.

        Returns:
            point_3d: The difference of two points.
        """

    def __mul__(self, other: float) -> 'point_3d':
        """
        Multiply point by a scalar.

        Returns:
            point_3d: The scaled point.
        """

    def __rmul__(self, other: float) -> 'point_3d':
        """
        Multiply point by a scalar (right-hand side).

        Returns:
            point_3d: The scaled point.
        """

    def __truediv__(self, other: float) -> 'point_3d':
        """
        Divide point by a scalar.

        Returns:
            point_3d: The scaled point.
        """

    def __iadd__(self, other: 'point_3d') -> 'point_3d':
        """
        In-place addition of another point.

        Returns:
            point_3d: The updated point.
        """

    def __isub__(self, other: 'point_3d') -> 'point_3d':
        """
        In-place subtraction of another point.

        Returns:
            point_3d: The updated point.
        """

    def __imul__(self, other: float) -> 'point_3d':
        """
        In-place multiplication by a scalar.

        Returns:
            point_3d: The updated point.
        """

    def __itruediv__(self, other: float) -> 'point_3d':
        """
        In-place division by a scalar.

        Returns:
            point_3d: The updated point.
        """

    def __neg__(self) -> 'point_3d':
        """
        Negate the point (component-wise).

        Returns:
            point_3d: The negated point.
        """

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
        Get coordinate by index (0: x, 1: y, 2: z).

        Returns:
            float: The coordinate value.
        Raises:
            IndexError: If index is out of range.
        """

    def __setitem__(self, index: int, value: float) -> None:
        """
        Set coordinate by index (0: x, 1: y, 2: z).

        Raises:
            IndexError: If index is out of range.
        """

    def __repr__(self) -> str:
        """
        Return the string representation of the point.

        Returns:
            str: The string representation.
        """

    def dot(self, p: 'point_3d') -> float:
        """Dot product with another point."""

    def cross(self, p: 'point_3d') -> 'point_3d':
        """Cross product with another point."""

    def magnitude(self) -> float:
        """Return the magnitude of the point vector."""

    def normalized(self) -> 'point_3d':
        """Return the normalized (unit) vector."""

    def distance(self, p: 'point_3d') -> float:
        """Euclidean distance to another point."""

    def invert(self) -> 'point_3d':
        """Return the inverted point (negated coordinates)."""
