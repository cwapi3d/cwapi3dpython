class point_3d:
    def __init__(self, x: float, y: float, z: float) -> None:
        pass

    def dot(self, p: 'point_3d') -> float:
        """dot
        Args:
            p ( point_3d): p

        Returns:
            float
        """

    def cross(self, p: 'point_3d') -> 'point_3d':
        """cross
        Args:
            p ( point_3d): p

        Returns:
            point_3d
        """

    def magnitude(self) -> float:
        """magnitude
        Args:

        Returns:
            float
        """

    def normalized(self) -> 'point_3d':
        """normalized
        Args:

        Returns:
            point_3d
        """

    def distance(self, p: 'point_3d') -> float:
        """distance
        Args:
            p ( point_3d): p

        Returns:
            float
        """

    def invert(self) -> 'point_3d':
        """invert
        Args:

        Returns:
            point_3d
        """

