from cadwork import point_3d
from cadwork import projection_type


class camera_data:
    def get_position(self) -> point_3d:
        pass

    def set_position(self, position: point_3d) -> None:
        pass

    def get_target(self) -> point_3d:
        pass

    def set_target(self, target: point_3d) -> None:
        pass

    def get_up_vector(self) -> point_3d:
        pass

    def set_up_vector(self, up_vector: point_3d) -> None:
        pass

    def get_projection_type(self) -> projection_type:
        pass

    def set_projection_type(self, projection_type: projection_type) -> None:
        pass

    def get_field_width(self) -> float:
        pass

    def set_field_width(self, field_width: float) -> None:
        pass

    def get_field_height(self) -> float:
        pass

    def set_field_height(self, field_height: float) -> None:
        pass

    def get_field_of_view(self) -> float:
        pass

    def set_field_of_view(self, field_of_view: float) -> None:
        pass
