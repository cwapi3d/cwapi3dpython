from typing import List


def get_last_error(error_code: int) -> str:
    """Gets the last error.

    Args:
        error_code: error code

    Returns:
        error string
    """


def export_production_list(element_id_list: List[int], file_path: str) -> None:
    """Exports a production list.

    Args:
        element_id_list: element id list
        file_path: file path

    """


def export_part_list(element_id_list: List[int], file_path: str) -> None:
    """Exports a part list.

    Args:
        element_id_list: element id list
        file_path: file path

    """


def check_position_numbers_production_list() -> List[int]:
    """Checks the production list numbers and returns the element ids with discrepancies.

    Args:

    Returns:
        element ids with discrepancies
    """


def check_position_numbers_part_list() -> List[int]:
    """Checks the part list numbers and returns the element ids with discrepancies.

    Args:

    Returns:
        element ids with discrepancies
    """


def clear_errors() -> None:
    """Clear errors.

    """


def export_production_list_with_settings(element_id_list: List[int], file_path: str, settings_file_path: str) -> None:
    """export production list with settings.

    Args:
        element_id_list: element id list
        file_path: file path
        settings_file_path: settings file path

    """


def export_part_list_with_settings(element_id_list: List[int], file_path: str, settings_file_path: str) -> None:
    """Exports part list with settings.

    Args:
        element_id_list: element id list
        file_path: file path
        settings_file_path: settings file path

    """


def generate_new_production_list_numbers(element_id_list: List[int]) -> None:
    """Generates new production list numbers.

    Args:
        element_id_list: element id list

    """


def generate_new_part_list_numbers(element_id_list: List[int]) -> None:
    """generate new part list numbers.

    Args:
        element_id_list: element id list

    """


def load_production_list_calculation_settings(settings_file_path: str) -> None:
    """Loads production list calculation settings.

    Args:
        settings_file_path: settings file path

    """


def load_part_list_calculation_settings(settings_file_path: str) -> None:
    """Loads part list calculation settings.

    Args:
        settings_file_path: settings file path

    """


def generate_new_production_list_silently(element_id_list: List[int], a1: int, a2: bool, a3: bool) -> None:
    """generate new production list silently

    Args:
        element_id_list: element id list
        a1: a1
        a2: a2
        a3: a3

    """


def generate_new_part_list_silently(element_id_list: List[int], a1: int, a2: bool, a3: bool) -> None:
    """generate new part list silently

    Args:
        element_id_list: element id list
        a1: a1
        a2: a2
        a3: a3

    """
