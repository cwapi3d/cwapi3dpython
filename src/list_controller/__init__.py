from typing import List


def export_production_list(elements: List[int], file: str) -> None: 
    """Exports a production list

    Examples:
        >>> list_controller.export_production_list(elements, "C:\\Users\\John\\my_list.csv")
        >>> list_controller.export_production_list(elements, "C:\\Users\\John\\my_list.cwle")

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def export_part_list(elements: List[int], file: str) -> None: 
    """Exports a part list
    
    Examples:
        >>> list_controller.export_part_list(elements, "C:\\Users\\John\\my_list.csv")
        >>> list_controller.export_part_list(elements, "C:\\Users\\John\\my_list.cwle")

    Args:
        elements (List[int]): element IDs
        file (str): file path
    """
def check_position_numbers_production_list() -> List[int]: 
    """Checks the production list numbers and returns the element ids with discrepancies

    Returns:
        List[int]: element IDs
    """
def check_position_numbers_part_list() -> List[int]: 
    """Checks the part list numbers and returns the element ids with discrepancies

    Returns:
        List[int]: element IDs with discrepancies
    """
def export_production_list_with_settings(elements: List[int], file: str, settings: str) -> None: 
    """export production list with settings. Available file formats are .cwle and .csv
    
    Examples:
        >>> list_controller.export_production_list_with_settings(elements, "C:\\Users\\John\\my_list.csv", settings_file_path)
        >>> list_controller.export_production_list_with_settings(elements, "C:\\Users\\John\\my_list.cwle", settings_file_path)

    Args:
        elements (List[int]): element IDs
        file (str): file path
        settings (str): settings file path
    """
def export_part_list_with_settings(elements: List[int], file: str, settings: str) -> None: 
    """export part list with settings. Available file formats are .cwle and .csv
    
    Examples:
        >>> list_controller.export_part_list_with_settings(elements, "C:\\Users\\John\\my_list.csv", settings_file_path)
        >>> list_controller.export_part_list_with_settings(elements, "C:\\Users\\John\\my_list.cwle", settings_file_path)
   
    Args:
        elements (List[int]): element IDs
        file (str): file path
        settings (str): settings file path
    """
def generate_new_production_list_numbers(elements: List[int]) -> None: 
    """generates new positions numbers for production list

    Args:
        elements (List[int]): element IDs
    """
def generate_new_part_list_numbers(elements: List[int]) -> None: 
    """generates new positions numbers for part list

    Args:
        elements (List[int]): element IDs
    """
def load_production_list_calculation_settings(file: str) -> None: 
    """loads a settings file for production list calculation

    Args:
        file (str): file path
    """
def load_part_list_calculation_settings(file: str) -> None: 
    """_summary_

    Args:
        file (str): file path
    """

def generate_new_production_list_silently(elements: List[int], start_number: int, keep_existing_numbers: bool, with_containers: bool) -> None:
    """

    Args:
        elements (List[int]): element IDs
        start_number (int): a start number
        keep_existing_numbers (bool): keep existing numbers
        with_containers (bool): with containers

    """

def generate_new_part_list_silently(elements: List[int], start_number: int, keep_existing_numbers: bool, with_containers: bool) -> None:
    """_summary_

    Args:
        elements (List[int]): element IDs
        start_number (int): a start number
        keep_existing_numbers (bool): keep existing numbers
        with_containers (bool): with containers

    """