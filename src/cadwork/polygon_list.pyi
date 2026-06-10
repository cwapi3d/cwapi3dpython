from typing import Iterator

from cadwork import vertex_list


class polygon_list:

    def count(self) -> int:
        """Returns the number of polygons in the list.

        Returns: int
        """

    def at(self, index: int) -> vertex_list:
        """Returns the polygon vertices at the given index.

        Parameters:
            index: The zero-based polygon index.

        Returns:
            vertex_list: The ordered vertices defining the polygon.
        """

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[vertex_list]: ...

    def __getitem__(self, index: int) -> vertex_list: ...
