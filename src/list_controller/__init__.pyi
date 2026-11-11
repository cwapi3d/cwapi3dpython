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

    Does nothing without the cadwork 3D list license. Returns nothing; failures are not reported.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv' or '.xlsx', the list is built as a
            temporary list file in the temp folder and the cadwork list module is then started with
            this path; otherwise the list file is written directly to this path.
    """

def export_part_list(element_id_list: list[ElementId], file_path: str) -> None:
    """Export a part list of the given elements to a file.

    Does nothing without the cadwork 3D list license. Returns nothing; failures are not reported.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv' or '.xlsx', the list is built as a
            temporary list file in the temp folder and the cadwork list module is then started with
            this path; otherwise the list file is written directly to this path.
    """

def check_position_numbers_production_list() -> list[ElementId]:
    """Find visible elements with faulty production list numbers.

    Only visible elements that already have a production list number (non-zero) are checked. Does
    nothing without the cadwork 3D list license.

    Returns:
        List of element IDs whose production list number is flagged as faulty. Empty list if there
        are none, if the check fails, or without the list license.
    """

def check_position_numbers_part_list() -> list[ElementId]:
    """Find visible elements with faulty part list numbers.

    Only visible elements that already have a part list number (non-zero) are checked. Does nothing
    without the cadwork 3D list license.

    Returns:
        List of element IDs whose part list number is flagged as faulty. Empty list if there are
        none, if the check fails, or without the list license.
    """

def clear_errors() -> None:
    """Clear the stored API error state."""

def export_production_list_with_settings(
    element_id_list: list[ElementId], file_path: str, settings_file_path: str
) -> None:
    """Export a production list to a file using a settings file.

    Does nothing without the cadwork 3D list license. Same as export_production_list, but the
    settings file content controls the export.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv' or '.xlsx', the list is built as a
            temporary list file in the temp folder and the cadwork list module is then started with
            this path; otherwise the list file is written directly to this path.
        settings_file_path: Path to a settings file whose UTF-8 text is used for the export. If the
            file does not exist or cannot be read, the export runs with empty settings.
    """

def export_part_list_with_settings(element_id_list: list[ElementId], file_path: str, settings_file_path: str) -> None:
    """Export a part list to a file using a settings file.

    Does nothing without the cadwork 3D list license. Same as export_part_list, but the settings
    file content controls the export.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv' or '.xlsx', the list is built as a
            temporary list file in the temp folder and the cadwork list module is then started with
            this path; otherwise the list file is written directly to this path.
        settings_file_path: Path to a settings file whose UTF-8 text is used for the export. If the
            file does not exist or cannot be read, the export runs with empty settings.
    """

def generate_new_production_list_numbers(element_id_list: list[ElementId]) -> None:
    """Generate new production list numbers for the given elements.

    Does nothing without the cadwork 3D list license. Opens the list number selection dialog
    and blocks the script until it is closed. Numbers are written only if the user confirms.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
    """

def generate_new_part_list_numbers(element_id_list: list[ElementId]) -> None:
    """Generate new part list numbers for the given elements.

    Does nothing without the cadwork 3D list license. Opens the list number selection dialog
    and blocks the script until it is closed. Numbers are written only if the user confirms.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
    """

def load_production_list_calculation_settings(settings_file_path: str) -> None:
    """Load production list calculation settings from a file and save them.

    The loaded settings are saved into the current document. If the file cannot be loaded as valid
    settings, nothing is saved.

    Parameters:
        settings_file_path: Path to the settings file to load.
    """

def load_part_list_calculation_settings(settings_file_path: str) -> None:
    """Load part list calculation settings from a file and save them.

    The loaded settings are saved into the current document. If the file cannot be loaded as valid
    settings, nothing is saved.

    Parameters:
        settings_file_path: Path to the settings file to load.
    """

def generate_new_production_list_silently(
    element_id_list: list[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool, with_containers: bool
) -> None:
    """Generate production list numbers without dialogs.

    Does nothing without the cadwork 3D list license. Numbers are written to the elements. Empty
    list is a no-op. Container elements and non-container elements are numbered separately
    (container numbers only when with_containers is True).

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        starting_number: First number to assign.
        keep_existing_numbers: If True, elements that already have a number keep it.
        with_containers: If True, container elements are numbered too (with their own container list
            numbering); if False, containers are ignored.
    """

def generate_new_part_list_silently(
    element_id_list: list[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool, with_containers: bool
) -> None:
    """Generate part list numbers without dialogs.

    Does nothing without the cadwork 3D list license. Numbers are written to the elements.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        starting_number: First number to assign.
        keep_existing_numbers: If True, elements that already have a number keep it.
        with_containers: Whether container elements are considered when numbering.
    """

def export_cover_list(element_id_list: list[ElementId], file_path: str) -> None:
    """Export a wall, roof or floor list of the given elements to a file.

    Does nothing without the cadwork 3D list license. Returns nothing; failures are not reported.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv', the list is built as a temporary list
            file in the temp folder and the cadwork list module is then started with this path;
            otherwise the list file is written directly to this path.
    """

def export_cover_list_with_settings(element_id_list: list[ElementId], file_path: str, settings_file_path: str) -> None:
    """Export a wall, roof or floor list to a file using a settings file.

    Does nothing without the cadwork 3D list license. Same as export_cover_list, but the settings
    file content controls the export.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        file_path: Target file path. If it contains '.csv', the list is built as a temporary list
            file in the temp folder and the cadwork list module is then started with this path;
            otherwise the list file is written directly to this path.
        settings_file_path: Path to a settings file whose UTF-8 text is used for the export. If the
            file does not exist or cannot be read, the export runs with empty settings.
    """

def export_container_list(element_id_list: list[ElementId], export_file_path: str) -> None:
    """Export a container list of the given elements to a file.

    Does nothing without the cadwork 3D list license. The file is written directly at the given
    path, with no csv/xlsx conversion step.

    Parameters:
        element_id_list: List of element IDs to include. Invalid IDs are skipped.
        export_file_path: Target file path for the exported list.
    """
