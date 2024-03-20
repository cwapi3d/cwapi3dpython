from typing import List

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def export_btl(btl_version: int, file_path: str) -> None:
    """Exports a BTL file

    Parameters:
        btl_version: btl_version
        file_path: file_path

    Returns:
        None
    """

def export_weinmann_mfb(mfb_version: int) -> None:
    """Exports a WUP file

    Parameters:
        mfb_version: mfb_version

    Returns:
        None
    """

def export_hundegger(hundeggertype: int) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def export_hundegger_with_file_path(hundeggertype: int, file_path: str) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting(hundeggertype: int, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path
        presetting: presetting

    Returns:
        None
    """

def export_btl_with_presetting(btl_version: int, file_path: str, presetting: str) -> None:
    """Exports a BTL file with a presetting file

    Parameters:
        btl_version: btl_version
        file_path: file_path
        presetting: presetting

    Returns:
        None
    """

def calculate_btl_machine_data(elements: List[int], btl_version: int) -> None:
    """Calculates the Machine Data for BTL

    Parameters:
        elements: elements
        btl_version: btl_version

    Returns:
        None
    """

def calculate_hundegger_machine_data(elements: List[int], hunderggertype: int) -> None:
    """Calculates the Machine Data for Hundegger

    Parameters:
        elements: elements
        hunderggertype: hunderggertype

    Returns:
        None
    """

def load_hundegger_calculation_set(hundeggertype: int, file_path: str) -> None:
    """load hundegger calculation set

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_silent(hundeggertype: int, file_path: str) -> None:
    """Exports a Hundegger file silently

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting_silent(hundeggertype: int, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file silently

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path
        presetting: presetting

    Returns:
        None
    """

