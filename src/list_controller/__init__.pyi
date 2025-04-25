from typing import List


def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """


def export_production_list(element_id_list: List[int], file_path: str) -> None:
    """Exports a production list

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """


def export_part_list(element_id_list: List[int], file_path: str) -> None:
    """Exports a part list

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """


def check_position_numbers_production_list() -> List[int]:
    """Checks the production list numbers and returns the element ids with discrepancies

    Returns:
        element ids with discrepancies
    """


def check_position_numbers_part_list() -> List[int]:
    """Checks the part list numbers and returns the element ids with discrepancies

    Returns:
        element ids with discrepancies
    """


def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """


def export_production_list_with_settings(element_id_list: List[int], file_path: str, settings_file_path: str) -> None:
    """export production list with settings

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        settings_file_path: settings_file_path

    Returns:
        None
    """


def export_part_list_with_settings(element_id_list: List[int], file_path: str, settings_file_path: str) -> None:
    """export part list with settings

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        settings_file_path: settings_file_path

    Returns:
        None
    """


def generate_new_production_list_numbers(elements: List[int]) -> None:
    """generate new production list numbers

    Parameters:
        elements: elements

    Returns:
        None
    """


def generate_new_part_list_numbers(elements: List[int]) -> None:
    """generate new part list numbers

    Parameters:
        elements: elements

    Returns:
        None
    """


def load_production_list_calculation_settings(settings_file_path: str) -> None:
    """load production list calculation settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """


def load_part_list_calculation_settings(settings_file_path: str) -> None:
    """load part list calculation settings

    Parameters:
        settings_file_path: settings_file_path

    Returns:
        None
    """


def generate_new_production_list_silently(elements: List[int], starting_number: int, keep_existing_numbers: bool,
                                          with_containers: bool) -> None:
    """generate new production list silently

    Parameters:
        elements: elements
        starting_number: starting_number
        keep_existing_numbers: keep_existing_numbers
        with_containers: with_containers

    Returns:
        None
    """


def generate_new_part_list_silently(elements: List[int], starting_number: int, keep_existing_numbers: bool,
                                    with_containers: bool) -> None:
    """generate new part list silently

    Parameters:
        elements: elements
        starting_number: starting_number
        keep_existing_numbers: keep_existing_numbers
        with_containers: with_containers

    Returns:
        None
    """


def export_cover_list(element_id_list: List[int], file_path: str) -> None:
    """Exports a Wall/Roof/Floor list

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """


def export_cover_list_with_settings(element_id_list: List[int], file_path: str, settings_file_path: str) -> None:
    """Exports a Wall/Roof/Floor list with settings file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        settings_file_path: settings_file_path

    Returns:
        None
    """
