class point_3d:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, p: 'point_3d'):
        """adds two points

        Args:
            p ( point_3d): p

        Returns:
            point_3d: a third point
        """

    def __sub__(self, p: 'point_3d'):
        """subtracts two points

        Args:
            p ( point_3d): p

        Returns:
            point_3d: a third point
        """

    def __mul__(self, p: 'point_3d'):
        """multiplies two points

        Args:
            p ( point_3d): p

        Returns:
            point_3d: a third point
        """

    def __div__(self, p: 'point_3d'):
        """divides two points

        Args:
            p ( point_3d): p

        Returns:
            point_3d: a third point
        """

    def __eq__(self, p: 'point_3d'):
        """checks if two points are equal

        Args:
            p ( point_3d): p

        Returns:
            bool: condition
        """

    def __ne__(self, p: 'point_3d'):
        """checks if two points are not equal

        Args:
            p ( point_3d): p
        """

    def __getitem__(self, index: int):
        """gets the value of a point at a given index

        Args:
            index (int): index

        Returns:
            float: value
        """

    def __setitem__(self, index: int, value: float):
        """sets the value of a point at a given index

        Args:
            index (int): index
            value (float): value
        """

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
