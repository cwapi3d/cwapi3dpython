class point_3d:
    
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

