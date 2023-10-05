from .point_3d import point_3d


class vertex_list:
    def __init__(self) -> None:
        pass

    def at(self, index: int) -> point_3d:
        """
        Args:
            index (int): index

        Returns:
            point_3d: point
        """
        pass

    def append(self, point: point_3d) -> None:
        """
        Args:
            point (point_3d): point
        """
        pass

    def count(self) -> int:
        """
        Returns:
            int: count
        """
        pass
