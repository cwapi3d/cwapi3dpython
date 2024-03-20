from cadwork import point_3d
from cadwork import projection_type

class camera_data:
    
    def get_position(self) -> point_3d:
        """get position

        Returns:
            point_3d
        """

    def set_position(self, position: point_3d) -> None:
        """set position

        Parameters:
            position: position

        Returns:
            None
        """

    def get_target(self) -> point_3d:
        """get target

        Returns:
            point_3d
        """

    def set_target(self, target: point_3d) -> None:
        """set target

        Parameters:
            target: target

        Returns:
            None
        """

    def get_up_vector(self) -> point_3d:
        """get up vector

        Returns:
            point_3d
        """

    def set_up_vector(self, up_vector: point_3d) -> None:
        """set up vector

        Parameters:
            up_vector: up_vector

        Returns:
            None
        """

    def get_projection_type(self) -> projection_type:
        """get projection type

        Returns:
            projection_type
        """

    def set_projection_type(self, projection_type: projection_type) -> None:
        """set projection type

        Parameters:
            projection_type: projection_type

        Returns:
            None
        """

    def get_field_width(self) -> float:
        """get field width

        Returns:
            float
        """

    def set_field_width(self, field_width: float) -> None:
        """set field width

        Parameters:
            field_width: field_width

        Returns:
            None
        """

    def get_field_height(self) -> float:
        """get field height

        Returns:
            float
        """

    def set_field_height(self, field_height: float) -> None:
        """set field height

        Parameters:
            field_height: field_height

        Returns:
            None
        """

    def get_field_of_view(self) -> float:
        """get field of view

        Returns:
            float
        """

    def set_field_of_view(self, field_of_view: float) -> None:
        """set field of view

        Parameters:
            field_of_view: field_of_view

        Returns:
            None
        """

