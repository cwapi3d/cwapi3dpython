from .vertex_list import vertex_list
from .point_3d import point_3d


class facet_list:
    def __init__(self) -> None:
        pass

    def at(index: int) -> vertex_list:
        """
        Args:
            index (int): index

        Returns:
            vertex_list: vertex list
        """
        pass

    def count(self) -> int:
        """
        Returns:
            int: count
        """
        pass

    def get_distance_to_origin(self) -> float:
        """
        Returns:
            float: distance
        """
        pass

    def get_external_polygon(self) -> vertex_list:
        """
        Returns:
            vertex_list: vertex list
        """
        pass

    def get_external_polygon_for_reference_face(self) -> vertex_list:
        """
        Returns:
            vertex_list: vertex list
        """
        pass

    def get_internal_polygons(self) -> vertex_list:
        """
        Returns:
            vertex_list: vertex list
        """
        pass

    def get_internal_polygons_for_reference_face(self) -> vertex_list:
        """
        Returns:
            vertex_list: vertex list
        """
        pass

    def get_normal_vector(self) -> point_3d:
        """
        Returns:
            point_3d: normal vector
        """
        pass

    def get_vertices_for_reference_face(self) -> vertex_list:
        """
        Returns:
            vertex_list: vertex list
        """
        pass
