class point_3d():

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, another_point_3d):
        """adds two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __sub__(self, another_point_3d):
        """subtracts two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __mul__(self, another_point_3d):
        """multiplies two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __div__(self, another_point_3d):
        """divides two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __eq__(self, another_point_3d):
        """checks if two points are equal

        Args:
            point_3d (point_3d): a second point

        Returns:
            bool: condition
        """

    def __ne__(self, another_point_3d):
        """checks if two points are not equal

        Args:
            point_3d (point_3d): a second point
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

    def cross(self, another_point_3d):
        """cross product takes two vectors and produces a third vector that is orthogonal to both

        Args:
            point_3d (point_3d): a second vector

        Returns:
            point_3d: a third vector orthogonal to both
        """

    def distance(self, another_point_3d) -> float:
        """distance between to points

        Args:
            point_3d (point_3d): a second point

        Returns:
            float: distance
        """

    def dot(self, another_point_3d) -> float:
        """When calculating the dot product of two unit vectors, the result is always between -1 and +1.
        The scalar product of two vectors of given length is thus zero if they are perpendicular to each other, and maximum if they have the same direction.
        A negative dot product between two vectors means that the two vectors go in the opposite general direction.

        Args:
            point_3d (point_3d): a second vector

        Returns:
            float: value betweend 0.0 and 1.0
        """

    def magnitude(self) -> float:
        """magnitude of a vector is the length of the vector.

        Returns:
            float: vector length
        """

    def normalized(self):
        """A normalized vector is a vector with a length equal to one unit.

        Returns:
            point_3d: normalized vector
        """

    def invert(self):
        """Invert point_3d

        Returns:
            point_3d: inverted point_3d
        """
