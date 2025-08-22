from typing import List

from cadwork.api_types import ElementId, UnsignedInt

def export_production_list(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a production list to the given file path.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
    """

def export_part_list(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a part list to the specified file path.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
    """

def check_position_numbers_production_list() -> List[ElementId]:
    """Checks the production list numbers and returns the element IDs that have discrepancies.

    Returns:
        The element IDs with discrepancies.
    """

def check_position_numbers_part_list() -> List[ElementId]:
    """Checks the part list numbers and returns the element IDs that have discrepancies.

    Returns:
        The element IDs with discrepancies.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

def export_production_list_with_settings(element_id_list: List[ElementId], file_path: str, settings_file_path: str) -> None:
    """Exports a production list using an additional settings file.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
        settings_file_path: The path to the settings file to be used for export.
    """

def export_part_list_with_settings(element_id_list: List[ElementId], file_path: str, settings_file_path: str) -> None:
    """Exports a part list using an additional settings file.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
        settings_file_path: The path to the settings file to be used for export.
    """

def generate_new_production_list_numbers(element_id_list: List[ElementId]) -> None:
    """Generates new production list numbers for the specified elements.

    Parameters:
        element_id_list: The list of elements to generate numbers for.
    """

def generate_new_part_list_numbers(element_id_list: List[ElementId]) -> None:
    """Generates new part list numbers for the specified elements.

    Parameters:
        element_id_list: The list of elements to generate numbers for.
    """

def load_production_list_calculation_settings(settings_file_path: str) -> None:
    """Loads the production list calculation settings from a file.

    Parameters:
        settings_file_path: The path to the settings file to be loaded.
    """

def load_part_list_calculation_settings(settings_file_path: str) -> None:
    """Loads the part list calculation settings from a file.

    Parameters:
        settings_file_path: The path to the settings file to be loaded.
    """

def generate_new_production_list_silently(element_id_list: List[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool,
                                          with_containers: bool) -> None:
    """Generates new production list numbers silently starting from a given number, optionally keeping existing numbers and considering container elements.

    Parameters:
        element_id_list: The list of elements to generate numbers for.
        starting_number: The number from which to start assigning new numbers.
        keep_existing_numbers: Whether or not to retain already assigned numbers in the list.
        with_containers: Whether to include container elements in the number generation.
    """

def generate_new_part_list_silently(element_id_list: List[ElementId], starting_number: UnsignedInt, keep_existing_numbers: bool,
                                    with_containers: bool) -> None:
    """Generates new part list numbers silently starting from a given number, optionally keeping existing numbers and considering container elements.

    Parameters:
        element_id_list: The list of elements to generate numbers for.
        starting_number: The number from which to start assigning new numbers.
        keep_existing_numbers: Whether or not to retain already assigned numbers in the list.
        with_containers: Whether to include container elements in the number generation.
    """

def export_cover_list(element_id_list: List[ElementId], file_path: str) -> None:
    """Exports a Wall, Roof, or Floor list to the specified file path.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
    """

def export_cover_list_with_settings(element_id_list: List[ElementId], file_path: str, settings_file_path: str) -> None:
    """Exports a Wall, Roof, or Floor list to the specified file path using an additional settings file.

    Parameters:
        element_id_list: The list of element IDs to be exported.
        file_path: The path of the target file for the export.
        settings_file_path: The path to the settings file to be used for export.
    """
