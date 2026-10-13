class element_level_of_detail_options:
    """Format-agnostic element level-of-detail options.

    Decorates every format-specific export options instance (SAT, STEP, IGES, ...).
    Obtained through `file_export_options.get_level_of_detail_options()`.
    """

    def get_materialize_end_types(self) -> bool:
        """Gets whether endtypes are materialized as real geometry.

        Returns:
            Whether endtypes are materialized as real geometry.
        """

    def set_materialize_end_types(self, value: bool) -> None:
        """Sets whether endtypes are materialized as real geometry.

        Parameters:
            value: Whether endtypes are materialized as real geometry.
        """

    def get_cut_end_type_counterparts(self) -> bool:
        """Gets whether endtype counterparts are cut from the materialized endtype.

        Returns:
            Whether endtype counterparts are cut from the materialized endtype.
        """

    def set_cut_end_type_counterparts(self, value: bool) -> None:
        """Sets whether endtype counterparts are cut from the materialized endtype.

        Parameters:
            value: Whether endtype counterparts are cut from the materialized endtype.
        """

    def get_cut_openings(self) -> bool:
        """Gets whether openings are cut from the exported solids.

        Returns:
            Whether openings are cut from the exported solids.
        """

    def set_cut_openings(self, value: bool) -> None:
        """Sets whether openings are cut from the exported solids.

        Parameters:
            value: Whether openings are cut from the exported solids.
        """

    def get_cut_drillings(self) -> bool:
        """Gets whether drillings are cut from the exported solids.

        Returns:
            Whether drillings are cut from the exported solids.
        """

    def set_cut_drillings(self, value: bool) -> None:
        """Sets whether drillings are cut from the exported solids.

        Parameters:
            value: Whether drillings are cut from the exported solids.
        """

    def get_materialize_mep_elements(self) -> bool:
        """Gets whether MEP elements are materialized as real geometry.

        Returns:
            Whether MEP elements are materialized as real geometry.
        """

    def set_materialize_mep_elements(self, value: bool) -> None:
        """Sets whether MEP elements are materialized as real geometry.

        Parameters:
            value: Whether MEP elements are materialized as real geometry.
        """

    def get_cut_mep_elements(self) -> bool:
        """Gets whether materialized MEP elements are cut from intersecting solids.

        Returns:
            Whether materialized MEP elements are cut from intersecting solids.
        """

    def set_cut_mep_elements(self, value: bool) -> None:
        """Sets whether materialized MEP elements are cut from intersecting solids.

        Parameters:
            value: Whether materialized MEP elements are cut from intersecting solids.
        """
