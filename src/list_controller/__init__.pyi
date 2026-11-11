"""Tabular list exports for production and quantity takeoff.

Generates the structured lists used in fabrication and project
management: production lists, part lists, and cover (wall / roof /
floor) lists, with optional external settings files to control
formatting and content. Concerned with *aggregated tabular data*
about the model, not with geometric or drawing exports.
"""

from cadwork.api_types import ElementId, UnsignedInt

def export_production_list(element_id_list: list[ElementId], file_path: str) -> None:
    """Export a production list of the given elements to a file.

    A production list is the table of elements grouped by production list number, produced by the
    cadwork list module. Does nothing without the cadwork 3D list license. Nothing is returned and
    failures are not reported, so check that the file exists afterwards. Use
    `list_controller.export_production_list_with_settings()` to control the export with a settings
    file, and `list_controller.export_part_list()` for the part list.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/list.csv'. If the path contains
            '.csv' or '.xlsx', the list is first built as a temporary list file (same base name,
            extension '.cwlm') in the temp folder and the cadwork list module is then started with
            this path to produce the final file; otherwise the list file is written directly to this
            path.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_production_list(element_ids, 'C:/Temp/cadwork_export/production.csv')
    """

def export_part_list(element_id_list: list[ElementId], file_path: str) -> None:
    """Export a part list of the given elements to a file.

    A part list is the table of elements grouped by part list number, produced by the cadwork list
    module. Does nothing without the cadwork 3D list license. Nothing is returned and failures are
    not reported, so check that the file exists afterwards. Use
    `list_controller.export_part_list_with_settings()` to control the export with a settings file,
    and `list_controller.export_production_list()` for the production list.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/list.csv'. If the path contains
            '.csv' or '.xlsx', the list is first built as a temporary list file (same base name,
            extension '.cwlm') in the temp folder and the cadwork list module is then started with
            this path to produce the final file; otherwise the list file is written directly to this
            path.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_part_list(element_ids, 'C:/Temp/cadwork_export/parts.xlsx')
    """

def check_position_numbers_production_list() -> list[ElementId]:
    """Find visible elements with faulty production list numbers.

    Runs the cadwork production list number check on all currently visible elements and returns the
    elements whose number it flags. Elements without a production list number (0) are left out of
    the check. Does nothing without the cadwork 3D list license. Renumber the reported elements with
    `list_controller.generate_new_production_list_silently()` or set a number with
    `attribute_controller.set_production_number()`.

    Examples:
        >>> import list_controller as lc

        >>> faulty_ids = lc.check_position_numbers_production_list()
        >>> if faulty_ids:
        ...     print('Faulty production list numbers on', len(faulty_ids), 'elements')
        ... else:
        ...     print('Production list numbers are consistent')

    Returns:
        List of element IDs whose production list number is flagged as faulty. Empty list if there
        are none, if the check fails, or without the list license.
    """

def check_position_numbers_part_list() -> list[ElementId]:
    """Find visible elements with faulty part list numbers.

    Runs the cadwork part list number check on all currently visible elements and returns the
    elements whose number it flags. Elements without a part list number (0) are left out of the
    check. Does nothing without the cadwork 3D list license. Renumber the reported elements with
    `list_controller.generate_new_part_list_silently()` or set a number with
    `attribute_controller.set_part_number()`.

    Examples:
        >>> import list_controller as lc

        >>> faulty_ids = lc.check_position_numbers_part_list()
        >>> if faulty_ids:
        ...     print('Faulty part list numbers on', len(faulty_ids), 'elements')
        ... else:
        ...     print('Part list numbers are consistent')

    Returns:
        List of element IDs whose part list number is flagged as faulty. Empty list if there are
        none, if the check fails, or without the list license.
    """

def clear_errors() -> None:
    """Clear the stored list controller error state.

    Empties the error stack kept by the list controller. The list functions in this module do not
    report errors to the caller, so this does not change their results.

    Examples:
        >>> import list_controller as lc

        >>> lc.clear_errors()
    """

def export_production_list_with_settings(
    element_id_list: list[ElementId], file_path: str, settings_file_path: str
) -> None:
    """Export a production list to a file using a settings file.

    Same as `list_controller.export_production_list()`, but the content of the settings file is
    passed to the list export. Does nothing without the cadwork 3D list license. Nothing is returned
    and failures are not reported, so check that the file exists afterwards.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/list.csv'. If the path contains
            '.csv' or '.xlsx', the list is first built as a temporary list file (same base name,
            extension '.cwlm') in the temp folder and the cadwork list module is then started with
            this path to produce the final file; otherwise the list file is written directly to this
            path.
        settings_file_path: Path to a settings file, e.g. 'C:/Temp/cadwork_export/settings.txt'. Its
            UTF-8 text is passed to the export and controls it. If the file does not exist or cannot
            be opened, the export runs with empty settings instead of failing.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_production_list_with_settings(
        ...         element_ids,
        ...         'C:/Temp/cadwork_export/production.csv',
        ...         'C:/Temp/cadwork_export/settings.txt'
        ...     )
    """

def export_part_list_with_settings(element_id_list: list[ElementId], file_path: str, settings_file_path: str) -> None:
    """Export a part list to a file using a settings file.

    Same as `list_controller.export_part_list()`, but the content of the settings file is passed to
    the list export. Does nothing without the cadwork 3D list license. Nothing is returned and
    failures are not reported, so check that the file exists afterwards.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/list.csv'. If the path contains
            '.csv' or '.xlsx', the list is first built as a temporary list file (same base name,
            extension '.cwlm') in the temp folder and the cadwork list module is then started with
            this path to produce the final file; otherwise the list file is written directly to this
            path.
        settings_file_path: Path to a settings file, e.g. 'C:/Temp/cadwork_export/settings.txt'. Its
            UTF-8 text is passed to the export and controls it. If the file does not exist or cannot
            be opened, the export runs with empty settings instead of failing.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_part_list_with_settings(
        ...         element_ids,
        ...         'C:/Temp/cadwork_export/parts.csv',
        ...         'C:/Temp/cadwork_export/settings.txt'
        ...     )
    """

def generate_new_production_list_numbers(element_id_list: list[ElementId]) -> None:
    """Generate production list numbers for the given elements through a dialog.

    Opens the list number dialog of cadwork 3D and blocks the script until the user closes it. Does
    nothing without the cadwork 3D list license. Which numbers are written is decided in the dialog.
    Use `list_controller.generate_new_production_list_silently()` for unattended scripts and check
    the result with `list_controller.check_position_numbers_production_list()`.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.generate_new_production_list_numbers(element_ids)
    """

def generate_new_part_list_numbers(element_id_list: list[ElementId]) -> None:
    """Generate part list numbers for the given elements through a dialog.

    Opens the list number dialog of cadwork 3D and blocks the script until the user closes it. Does
    nothing without the cadwork 3D list license. Which numbers are written is decided in the dialog.
    Use `list_controller.generate_new_part_list_silently()` for unattended scripts and check the
    result with `list_controller.check_position_numbers_part_list()`.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.generate_new_part_list_numbers(element_ids)
    """

def load_production_list_calculation_settings(settings_file_path: str) -> None:
    """Load production list calculation settings from a file into the document.

    The calculation settings define the comparison criteria used when production list numbers are
    calculated. The loaded settings are saved in the current document; if the file cannot be loaded
    as valid settings, nothing is saved and no error is reported. Use
    `list_controller.load_part_list_calculation_settings()` for the part list.

    Parameters:
        settings_file_path: Path to a saved list calculation settings file, e.g.
            'C:/Temp/cadwork_export/production_calc.xml'. If it cannot be loaded as valid settings,
            nothing is saved.

    Examples:
        >>> import list_controller as lc

        >>> settings_path = 'C:/Temp/cadwork_export/production_calc.xml'
        >>> lc.load_production_list_calculation_settings(settings_path)
    """

def load_part_list_calculation_settings(settings_file_path: str) -> None:
    """Load part list calculation settings from a file into the document.

    The calculation settings define the comparison criteria used when part list numbers are
    calculated. The loaded settings are saved in the current document; if the file cannot be loaded
    as valid settings, nothing is saved and no error is reported. Use
    `list_controller.load_production_list_calculation_settings()` for the production list.

    Parameters:
        settings_file_path: Path to a saved list calculation settings file, e.g.
            'C:/Temp/cadwork_export/part_calc.xml'. If it cannot be loaded as valid settings,
            nothing is saved.

    Examples:
        >>> import list_controller as lc

        >>> lc.load_part_list_calculation_settings('C:/Temp/cadwork_export/part_calc.xml')
    """

def generate_new_production_list_silently(
    element_id_list: list[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool, with_containers: bool
) -> None:
    """Generate production list numbers for the given elements without dialogs.

    Numbers are calculated and written directly to the elements, without the dialog of
    `list_controller.generate_new_production_list_numbers()`. Container elements and all other
    elements are numbered as two separate groups; the container group is processed only when
    with_containers is True. Does nothing without the cadwork 3D list license. An empty list or a
    list without valid elements is a no-op. Read the numbers back with
    `attribute_controller.get_production_number()`.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        starting_number: First number to assign.
        keep_existing_numbers: If True, elements that already have a number keep it.
        with_containers: If True, container elements are numbered too, as their own group. If False,
            containers are ignored.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.generate_new_production_list_silently(element_ids, 1, False, True)
        ...     print(lc.check_position_numbers_production_list())
    """

def generate_new_part_list_silently(
    element_id_list: list[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool, with_containers: bool
) -> None:
    """Generate part list numbers for the given elements without dialogs.

    Numbers are calculated and written directly to the elements, without the dialog of
    `list_controller.generate_new_part_list_numbers()`. Does nothing without the cadwork 3D list
    license. All given elements are numbered together as one part list group; unlike the production
    list variant there is no separate container group. Read the numbers back with
    `attribute_controller.get_part_number()`.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        starting_number: First number to assign.
        keep_existing_numbers: If True, elements that already have a number keep it.
        with_containers: Option forwarded to the numbering to include container elements; use True
            to include them.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.generate_new_part_list_silently(element_ids, 1, True, False)
        ...     print(lc.check_position_numbers_part_list())
    """

def export_cover_list(element_id_list: list[ElementId], file_path: str) -> None:
    """Export a wall, roof or floor list of the given elements to a file.

    The cover list is the cadwork list of wall, roof and floor elements, produced by the cadwork
    list module. Does nothing without the cadwork 3D list license. Nothing is returned and failures
    are not reported, so check that the file exists afterwards. Use
    `list_controller.export_cover_list_with_settings()` to control the export with a settings file.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/cover.csv'. If the path contains
            '.csv', the list is first built as a temporary list file (same base name, extension
            '.cwlm') in the temp folder and the cadwork list module is then started with this path
            to produce the final file; otherwise (including '.xlsx') the list file is written
            directly to this path.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_cover_list(element_ids, 'C:/Temp/cadwork_export/cover.csv')
    """

def export_cover_list_with_settings(element_id_list: list[ElementId], file_path: str, settings_file_path: str) -> None:
    """Export a wall, roof or floor list to a file using a settings file.

    Same as `list_controller.export_cover_list()`, but the content of the settings file is passed to
    the list export. Does nothing without the cadwork 3D list license. Nothing is returned and
    failures are not reported, so check that the file exists afterwards.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        file_path: Target file path, e.g. 'C:/Temp/cadwork_export/cover.csv'. If the path contains
            '.csv', the list is first built as a temporary list file (same base name, extension
            '.cwlm') in the temp folder and the cadwork list module is then started with this path
            to produce the final file; otherwise (including '.xlsx') the list file is written
            directly to this path.
        settings_file_path: Path to a settings file, e.g. 'C:/Temp/cadwork_export/settings.txt'. Its
            UTF-8 text is passed to the export and controls it. If the file does not exist or cannot
            be opened, the export runs with empty settings instead of failing.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_cover_list_with_settings(
        ...         element_ids,
        ...         'C:/Temp/cadwork_export/cover.csv',
        ...         'C:/Temp/cadwork_export/settings.txt'
        ...     )
    """

def export_container_list(element_id_list: list[ElementId], export_file_path: str) -> None:
    """Export a container list of the given elements to a file.

    A container list tabulates container elements, as produced by the cadwork list module. Does
    nothing without the cadwork 3D list license. The list file is written directly to the given
    path; unlike the other exports there is no temporary file and no csv/xlsx conversion step.
    Nothing is returned and failures are not reported.

    Parameters:
        element_id_list: List of element IDs to include, e.g. from
            `element_controller.get_active_identifiable_element_ids()`. IDs that do not exist are
            skipped.
        export_file_path: Target file path, e.g. 'C:/Temp/cadwork_export/containers.cwlm'. Used as
            is.

    Examples:
        >>> import element_controller as ec
        >>> import list_controller as lc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if element_ids:
        ...     lc.export_container_list(element_ids, 'C:/Temp/cadwork_export/containers.cwlm')
    """
