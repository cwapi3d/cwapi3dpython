from typing import List
from cadwork import point_3d


class hit_result:

    def get_hit_element_ids(self) -> List[int]:
        """get hit element ids

        Returns:
            List[int]
        """

    def get_hit_vertices_by_element(self, element_id: int) -> List[point_3d]:
        """get hit vertices by element

        Parameters:
            element_id: element_id

        Returns:
            List[point_3d]
        """
