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

    def dot(self, p: 'point_3d') -> float:
        """dot

        Parameters:
            p: p

        Returns:
            float
        """

    def cross(self, p: 'point_3d') -> 'point_3d':
        """cross

        Parameters:
            p: p

        Returns:
            'point_3d'
        """

    def magnitude(self) -> float:
        """magnitude

        Returns:
            float
        """

    def normalized(self) -> 'point_3d':
        """normalized

        Returns:
            'point_3d'
        """

    def distance(self, p: 'point_3d') -> float:
        """distance

        Parameters:
            p: p

        Returns:
            float
        """

    def invert(self) -> 'point_3d':
        """invert

        Returns:
            'point_3d'
        """

    def __sub__(self, other: 'point_3d') -> 'point_3d':
        """sub

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __truediv__(self, other: float) -> 'point_3d':
        """truediv

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __iadd__(self, other: 'point_3d') -> 'point_3d':
        """iadd

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __isub__(self, other: 'point_3d') -> 'point_3d':
        """isub

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __imul__(self, other: float) -> 'point_3d':
        """imul

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __itruediv__(self, other: float) -> 'point_3d':
        """itruediv

        Parameters:
            other: other

        Returns:
            'point_3d'
        """

    def __neg__(self) -> 'point_3d':
        """neg

        Returns:
            'point_3d'
        """

    def __eq__(self, other: object) -> bool:
        """eq

        Parameters:
            other: other

        Returns:
            bool
        """

    def __ne__(self, other: object) -> bool:
        """neg

        Parameters:
            other: other

        Returns:
            bool
        """

    def __add__(self, other: 'point_3d') -> 'point_3d':
        """add

        Parameters:
            other: other

        Returns:
            'point_3d'
        """
