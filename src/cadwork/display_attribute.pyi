class display_attribute:
    """
    A wrapper class for managing element display states for WebGL hierarchy display settings (not in Cadwork 3d).
    These methods update the internal state of the attribute object without requiring external parameters.

    Used exclusively with `set_webgl_hierarchy` to define visibility and display
    properties for elements in the WebGL.

    .. deprecated::
        This class supports legacy local WebGL workflows.
        It will be deprecated.
    """

    def __init__(self) -> None:
        """Initializes a new display_attribute instance."""

    def set_none(self) -> None:
        """Resets or clears the current display attribute state.

        Returns:
            None
        """

    def set_name(self) -> None:
        """Triggers the assignment of the name attribute.

        Returns:
            None
        """

    def set_group(self) -> None:
        """Triggers the assignment of the group attribute.

        Returns:
            None
        """

    def set_subgroup(self) -> None:
        """Triggers the assignment of the subgroup attribute.

        Returns:
            None
        """

    def set_comment(self) -> None:
        """Triggers the assignment of the comment attribute.

        Returns:
            None
        """

    def set_edv_code(self) -> None:
        """Triggers the assignment of the EDV/ERP code.

        Returns:
            None
        """

    def set_material(self) -> None:
        """Triggers the assignment of the material attribute.

        Returns:
            None
        """

    def set_material_group(self) -> None:
        """Triggers the assignment of the material group attribute.

        Returns:
            None
        """

    def set_user1(self) -> None:
        """Triggers the assignment of custom user field 1."""

    def set_user2(self) -> None:
        """Triggers the assignment of custom user field 2."""

    def set_user3(self) -> None:
        """Triggers the assignment of custom user field 3."""

    def set_user4(self) -> None:
        """Triggers the assignment of custom user field 4."""

    def set_user5(self) -> None:
        """Triggers the assignment of custom user field 5."""

    def set_user6(self) -> None:
        """Triggers the assignment of custom user field 6."""

    def set_user7(self) -> None:
        """Triggers the assignment of custom user field 7."""

    def set_user8(self) -> None:
        """Triggers the assignment of custom user field 8."""

    def set_user9(self) -> None:
        """Triggers the assignment of custom user field 9."""

    def set_user10(self) -> None:
        """Triggers the assignment of custom user field 10."""

    def set_production_number(self) -> None:
        """Triggers the assignment of the production/fabrication number.

        Returns:
            None
        """

    def set_timber_number(self) -> None:
        """Triggers the assignment of the timber-specific member number.

        Returns:
            None
        """

    def set_assembly_number(self) -> None:
        """Triggers the assignment of the assembly/unit number.

        Returns:
            None
        """

    def set_ifc_building(self) -> None:
        """Triggers the assignment of the IFC building attribute.

        Returns:
            None
        """

    def set_ifc_storey(self) -> None:
        """Triggers the assignment of the IFC storey/level attribute.

        Returns:
            None
        """
