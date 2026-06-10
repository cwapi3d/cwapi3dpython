from cadwork.point_3d import point_3d


class hit_result:

    def get_hit_element_ids(self) -> list[int]:
        """Get hit element IDs.

        Returns:
            list[int]: element IDs that were hit.
        """

    def get_hit_vertices_by_element(self, element_id: int) -> list[point_3d]:
        """Get hit vertices for a specific element.

        Parameters:
            element_id: The element ID.

        Returns:
            list[point_3d]: vertices hit on the element.
        """
