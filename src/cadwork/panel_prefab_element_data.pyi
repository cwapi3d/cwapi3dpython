from cadwork.panel_prefab_element_type import panel_prefab_element_type


class panel_prefab_element_data:
    """Read-only machine panel prefabrication data of an element.

    Holds the element type, layer location and MFB prefab config (machine
    calculation set) of an element. Returned by
    machine_controller.get_panel_prefab_element_data.
    """

    def get_element_type(self) -> panel_prefab_element_type:
        """get element type

        Returns:
            panel_prefab_element_type
        """

    def has_layer(self) -> bool:
        """has layer

        Tests if a layer location is set on the element.

        Returns:
            bool
        """

    def get_layer(self) -> int:
        """get layer

        Gets the layer location. Only meaningful if has_layer() returns True.

        Returns:
            int
        """

    def get_machine_calculation_set(self) -> str:
        """get machine calculation set

        Gets the machine calculation set (MFB prefab config) name.

        Returns:
            str
        """
