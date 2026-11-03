class extended_settings:
    """Extended settings of an element: a set of on/off flags that decide in which
    exports and machine outputs an element takes part.

    In cadwork 3D these flags are spread over two menus, and the API names do not
    match the labels you see there. Use the tables below to find the right method.

    **Modify > Extended settings**

    | Checkbox in cadwork 3D     | API methods                                          |
    |----------------------------|------------------------------------------------------|
    | Piece by piece export      | `get/set_piece_by_piece_export_with_dimensions`      |
    | Wall shop drawing          | `get/set_wall_export`                                |
    | Chief element              | `get/set_chief_element`                              |
    | Panel prefab export        | `get/set_mfb_export`                                 |
    | Single part machine export | `get/set_btl_wall_export`                            |

    **Modify > Processing in machine**

    | Checkbox in cadwork 3D     | API methods                                          |
    |----------------------------|------------------------------------------------------|
    | Single piece               | `get/set_single_piece`                               |
    | Composite                  | `get/set_composite`                                  |
    | Drilling creates notches   | `get/set_drilling_create_notches` (connector axes)   |
    | Generate processing        | `get/set_ignore_processing` (**inverted**)           |

    **Other flags** (shown in the standard element dialog, no extended-settings menu
    entry): `get/set_log_macro_export`, `get/set_outline`,
    `get/set_ignore_for_connector_axis`.

    **Flags without effect**: `piece_by_piece_export_without_dimensions`,
    `group_export` and `log_home_export` are legacy flags. cadwork 3D no longer
    evaluates them; `set_log_home_export` is not even stored.

    !!! warning "Common pitfall"
        "Single part machine export" (`set_btl_wall_export`) and "Single piece"
        (`set_single_piece`) are two **different** flags in two different menus.
        Setting one does not change the other.

    !!! note "How writing works"
        `attribute_controller.set_extended_settings(element_ids, settings)` writes
        **all** flags of `settings` to every element in `element_ids`; flags you did
        not touch are overwritten too. Always start from the element's current
        settings with `attribute_controller.get_extended_settings(element_id)`, change
        what you need, then write them back.

        The change is not added to the undo history, and a cadwork menu or dialog that
        is already open may keep showing the old state until it is reopened.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import attribute_controller as ac
        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     settings = ac.get_extended_settings(element_id)
        ...     settings.set_mfb_export(True)        # "Panel prefab export"
        ...     settings.set_btl_wall_export(True)   # "Single part machine export"
        ...     ac.set_extended_settings([element_id], settings)
    """

    def get_btl_wall_export(self) -> bool:
        """Returns whether the element is exported to single part machines
        (checkbox **Single part machine export** in *Modify > Extended settings*).

        Not to be confused with `get_single_piece`, which belongs to
        *Processing in machine*.

        Returns:
            True if the element is included in the single part machine export.
        """

    def get_chief_element(self) -> bool:
        """Returns whether the element is marked as chief element
        (checkbox **Chief element** in *Modify > Extended settings*).

        Returns:
            True if the element is a chief element.
        """

    def get_group_export(self) -> bool:
        """Returns the legacy group export flag.

        This flag has no effect in cadwork 3D; it is kept for compatibility with
        older scripts.

        Returns:
            The stored value of the legacy flag.
        """

    def get_ignore_for_connector_axis(self) -> bool:
        """Returns whether connector axes ignore this element when they are
        calculated (option **Ignore for connector axis**).

        Returns:
            True if connector axis calculations skip this element.
        """

    def get_log_home_export(self) -> bool:
        """Returns the legacy log home export flag.

        This flag has no effect in cadwork 3D and is never stored, so it always
        returns False.

        Returns:
            Always False.
        """

    def get_log_macro_export(self) -> bool:
        """Returns whether the element's cross-section is exported as a round log
        (log macro) in the machine output (option **Log macro output**).

        Returns:
            True if the element is exported as a round log.
        """

    def get_mfb_export(self) -> bool:
        """Returns whether the element is exported to panel prefabrication
        (checkbox **Panel prefab export** in *Modify > Extended settings*).

        "MFB" is the internal name of the panel prefabrication (multifunction
        bridge) export.

        Returns:
            True if the element is included in the panel prefab export.
        """

    def get_outline(self) -> bool:
        """Returns the **Outline** output flag of the element.

        Returns:
            True if the outline output is enabled for the element.
        """

    def get_piece_by_piece_export_with_dimensions(self) -> bool:
        """Returns whether the element gets a piece-by-piece shop drawing
        (checkbox **Piece by piece export** in *Modify > Extended settings*).

        Returns:
            True if the element is included in the piece-by-piece export.
        """

    def get_piece_by_piece_export_without_dimensions(self) -> bool:
        """Returns the legacy "piece by piece export without dimensions" flag.

        This flag has no effect in cadwork 3D; use
        `get_piece_by_piece_export_with_dimensions` for the **Piece by piece export**
        checkbox.

        Returns:
            The stored value of the legacy flag.
        """

    def get_wall_export(self) -> bool:
        """Returns whether the element is included in wall shop drawings
        (checkbox **Wall shop drawing** in *Modify > Extended settings*).

        Returns:
            True if the element is included in wall shop drawings.
        """

    def set_btl_wall_export(self, value: bool) -> None:
        """Includes or excludes the element from the export to single part machines
        (checkbox **Single part machine export** in *Modify > Extended settings*).

        Not to be confused with `set_single_piece`, which belongs to
        *Processing in machine*. Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to include the element, False to exclude it.

        Returns:
            None
        """

    def set_chief_element(self, value: bool) -> None:
        """Marks or unmarks the element as chief element
        (checkbox **Chief element** in *Modify > Extended settings*).

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to mark the element as chief element, False to unmark it.

        Returns:
            None
        """

    def set_group_export(self, value: bool) -> None:
        """Sets the legacy group export flag.

        This flag has no effect in cadwork 3D; it is kept for compatibility with
        older scripts.

        Parameters:
            value: The value to store.

        Returns:
            None
        """

    def set_ignore_for_connector_axis(self, value: bool) -> None:
        """Sets whether connector axes ignore this element when they are calculated
        (option **Ignore for connector axis**).

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to let connector axis calculations skip the element,
                False to include it.

        Returns:
            None
        """

    def set_log_home_export(self, value: bool) -> None:
        """Legacy log home export flag; has no effect.

        cadwork 3D does not store this flag: the value is dropped when the settings
        are written back, and `get_log_home_export` keeps returning False.

        Parameters:
            value: Ignored.

        Returns:
            None
        """

    def set_mfb_export(self, value: bool) -> None:
        """Includes or excludes the element from the panel prefabrication export
        (checkbox **Panel prefab export** in *Modify > Extended settings*).

        "MFB" is the internal name of the panel prefabrication (multifunction
        bridge) export. Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to include the element, False to exclude it.

        Returns:
            None
        """

    def set_outline(self, value: bool) -> None:
        """Enables or disables the **Outline** output flag of the element.

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to enable the outline output, False to disable it.

        Returns:
            None
        """

    def set_piece_by_piece_export_with_dimensions(self, value: bool) -> None:
        """Includes or excludes the element from piece-by-piece shop drawings
        (checkbox **Piece by piece export** in *Modify > Extended settings*).

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to include the element, False to exclude it.

        Returns:
            None
        """

    def set_piece_by_piece_export_without_dimensions(self, value: bool) -> None:
        """Sets the legacy "piece by piece export without dimensions" flag.

        This flag has no effect in cadwork 3D; use
        `set_piece_by_piece_export_with_dimensions` for the **Piece by piece export**
        checkbox.

        Parameters:
            value: The value to store.

        Returns:
            None
        """

    def set_wall_export(self, value: bool) -> None:
        """Includes or excludes the element from wall shop drawings
        (checkbox **Wall shop drawing** in *Modify > Extended settings*).

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to include the element, False to exclude it.

        Returns:
            None
        """

    def get_ignore_processing(self) -> bool:
        """Returns whether cadwork skips generating machine processings for the
        element.

        This is the **inverse** of the **Generate processing** setting in
        *Modify > Processing in machine*: True means no processings are generated.

        Returns:
            True if no processings are generated for the element.
        """

    def set_ignore_processing(self, value: bool) -> None:
        """Turns off or on the generation of machine processings for the element.

        This is the **inverse** of the **Generate processing** setting in
        *Modify > Processing in machine*: pass True to stop generating processings.
        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to stop generating processings, False to generate them.

        Returns:
            None
        """

    def get_single_piece(self) -> bool:
        """Returns whether the element's processings are generated for single-piece
        machines (checkbox **Single piece** in *Modify > Processing in machine*).

        Not to be confused with `get_btl_wall_export` (**Single part machine
        export** in *Modify > Extended settings*).

        Returns:
            True if processings are generated for single-piece machines.
        """

    def set_single_piece(self, value: bool) -> None:
        """Sets whether the element's processings are generated for single-piece
        machines (checkbox **Single piece** in *Modify > Processing in machine*).

        Not to be confused with `set_btl_wall_export` (**Single part machine
        export** in *Modify > Extended settings*). Takes effect only once written
        back with `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to generate processings for single-piece machines,
                False to stop.

        Returns:
            None
        """

    def get_composite(self) -> bool:
        """Returns whether the element's processings are generated for composite
        (wall prefabrication) machines (checkbox **Composite** in
        *Modify > Processing in machine*).

        Returns:
            True if processings are generated for composite machines.
        """

    def set_composite(self, value: bool) -> None:
        """Sets whether the element's processings are generated for composite
        (wall prefabrication) machines (checkbox **Composite** in
        *Modify > Processing in machine*).

        Takes effect only once written back with
        `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to generate processings for composite machines,
                False to stop.

        Returns:
            None
        """

    def get_drilling_create_notches(self) -> bool:
        """Returns whether drillings of a connector axis also create notches in the
        machine processing (checkbox **Drilling creates notches** in
        *Modify > Processing in machine*).

        Only relevant for connector axis elements.

        Returns:
            True if the drillings create notches.
        """

    def set_drilling_create_notches(self, value: bool) -> None:
        """Sets whether drillings of a connector axis also create notches in the
        machine processing (checkbox **Drilling creates notches** in
        *Modify > Processing in machine*).

        Only relevant for connector axis elements. Takes effect only once written
        back with `attribute_controller.set_extended_settings`.

        Parameters:
            value: True to let the drillings create notches, False otherwise.

        Returns:
            None
        """
