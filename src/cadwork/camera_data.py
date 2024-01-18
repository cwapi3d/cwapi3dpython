from .point_3d import point_3d
from .projection_type import projection_type


class camera_data:
    def get_position(self) -> point_3d:
        """get position
        Args:

        Returns:
            point_3d
        """

    def set_position(self, position: point_3d) -> None:
        """set position
        Args:
            position ( point_3d): position

        Returns:
            None
        """

    def get_target(self) -> point_3d:
        """get target
        Args:

        Returns:
            point_3d
        """

    def set_target(self, target: point_3d) -> None:
        """set target
        Args:
            target ( point_3d): target

        Returns:
            None
        """

    def get_up_vector(self) -> point_3d:
        """get up vector
        Args:

        Returns:
            point_3d
        """

    def set_up_vector(self, up_vector: point_3d) -> None:
        """set up vector
        Args:
            up_vector ( point_3d): up_vector

        Returns:
            None
        """

    def get_projection_type(self) -> projection_type:
        """get projection type
        Args:

        Returns:
            projection_type
        """

    def set_projection_type(self, projection_type: projection_type) -> None:
        """set projection type
        Args:
            projection_type ( projection_type): projection_type

        Returns:
            None
        """

    def get_field_width(self) -> float:
        """get field width
        Args:

        Returns:
            float
        """

    def set_field_width(self, field_width: float) -> None:
        """set field width
        Args:
            field_width ( float): field_width

        Returns:
            None
        """

    def get_field_height(self) -> float:
        """get field height
        Args:

        Returns:
            float
        """

    def set_field_height(self, field_height: float) -> None:
        """set field height
        Args:
            field_height ( float): field_height

        Returns:
            None
        """

    def get_field_of_view(self) -> float:
        """get field of view
        Args:

        Returns:
            float
        """

    def set_field_of_view(self, field_of_view: float) -> None:
        """set field of view
        Args:
            field_of_view ( float): field_of_view

        Returns:
            None
        """
