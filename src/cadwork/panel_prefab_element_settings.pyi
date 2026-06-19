from cadwork.panel_prefab_element_type import panel_prefab_element_type


class panel_prefab_element_settings:
    """Machine panel prefabrication settings passed to the setter.

    Only the fields that are explicitly set are applied to the elements; unset
    fields are left untouched, mirroring the interactive "only change what
    differs" behaviour. Passed to machine_controller.set_panel_prefab_element_data.
    """

    def __init__(self) -> None:
        """Creates an empty panel prefab element settings object."""

    def set_element_type(self, type: panel_prefab_element_type) -> None:
        """set element type

        Sets the panel prefab element type to apply.

        Parameters:
            type: The element type.

        Returns:
            None
        """

    def set_layer(self, layer: int) -> None:
        """set layer

        Sets the layer location to apply.

        Parameters:
            layer: The layer location.

        Returns:
            None
        """

    def reset_layer(self) -> None:
        """reset layer

        Resets (clears) the layer location.

        Returns:
            None
        """

    def set_machine_calculation_set(self, machine_calculation_set: str) -> None:
        """set machine calculation set

        Sets the machine calculation set (MFB prefab config) name to apply.

        Parameters:
            machine_calculation_set: The MFB prefab config name.

        Returns:
            None
        """
