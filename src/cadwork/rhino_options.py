
class rhino_options:
    """
    Rhino options

    Examples:
        >>> rhino_options = rhino_options()
        >>> rhino_options.set_cut_drillings(True)
        >>> rhino_options.set_cut_end_types_counterparts(True)
        >>> file_controller.export_rhino_file_with_options(elements, "yourFile.3dm", 7, user_default_assignment=True, write_standard_attributes=True, rhino_options)

    """

    def __init__(self) -> None:
        pass

    def get_cut_drillings(self) -> bool:
        """Get cut drillings option.

        Returns:
            bool: True if cut drillings are exported
        """
        pass

    def get_cut_end_types_counterparts(self) -> bool:
        """Get cut end types counterparts option.

        Returns:
            bool: True if cut end types counterparts are exported
        """
        pass

    def get_cut_mep(self) -> bool:
        """Get cut mep option.

        Returns:
            bool: True if cut mep is exported
        """
        pass

    def get_cut_openings(self) -> bool:
        """Get cut openings option.

        Returns:
            bool: True if cut openings are exported
        """
        pass

    def get_materialize_end_types(self) -> bool:
        """Get materialize end types option.

        Returns:
            bool: True if materialize end types are exported
        """
        pass

    def set_cut_drillings(self, value: bool) -> None:
        """Set cut drillings option.

        Args:
            value (bool): True if cut drillings are exported
        """
        pass

    def set_cut_end_types_counterparts(self, value: bool) -> None:
        """Set cut end types counterparts option.

        Args:
            value (bool): True if cut end types counterparts are exported
        """
        pass

    def set_cut_mep(self, value: bool) -> None:
        """Set cut mep option.

        Args:
            value (bool): True if cut mep is exported
        """
        pass

    def set_cut_openings(self, value: bool) -> None:
        """Set cut openings option.

        Args:
            value (bool): True if cut openings are exported
        """
        pass

    def set_materialize_end_types(self, value: bool) -> None:
        """Set materialize end types option.

        Args:
            value (bool): True if materialize end types are exported
        """
        pass
