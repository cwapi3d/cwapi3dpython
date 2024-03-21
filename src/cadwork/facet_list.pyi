from cadwork import point_3d
from cadwork import polygon_list
from cadwork import vertex_list

class facet_list:
    
    def count(self) -> int:
        """count

        Returns:
            int
        """

    def at(self, index: int) -> point_3d:
        """at

        Parameters:
            index: index

        Returns:
            point_3d
        """

    def get_external_polygon(self, index: int) -> vertex_list:
        """get external polygon

        Parameters:
            index: index

        Returns:
            vertex_list
        """

    def get_internal_polygons(self, index: int) -> polygon_list:
        """get internal polygons

        Parameters:
            index: index

        Returns:
            polygon_list
        """

    def get_vertices_for_reference_face(self) -> vertex_list:
        """get vertices for reference face

        Returns:
            vertex_list
        """

    def get_external_polygon_for_reference_face(self) -> vertex_list:
        """get external polygon for reference face

        Returns:
            vertex_list
        """

    def get_internal_polygons_for_reference_face(self) -> polygon_list:
        """get internal polygons for reference face

        Returns:
            polygon_list
        """

    def get_normal_vector(self, index: int) -> point_3d:
        """get normal vector

        Parameters:
            index: index

        Returns:
            point_3d
        """

    def get_distance_to_origin(self, index: int) -> float:
        """get distance to origin

        Parameters:
            index: index

        Returns:
            float
        """

