from typing import List

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def export_btl(btl_version: int, file_path: str) -> None:
    """export btl
    Args:
        btl_version ( int): btl_version
        file_path ( str): file_path

    Returns:
        None
    """

def export_weinmann_mfb(mfb_version: int) -> None:
    """export weinmann mfb
    Args:
        mfb_version ( int): mfb_version

    Returns:
        None
    """

def export_hundegger(hundeggertype: int) -> None:
    """export hundegger
    Args:
        hundeggertype ( int): hundeggertype

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def export_hundegger_with_file_path(hundeggertype: int, file_path: str) -> None:
    """export hundegger with file path
    Args:
        hundeggertype ( int): hundeggertype
        file_path ( str): file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting(hundeggertype: int, file_path: str, presetting: str) -> None:
    """export hundegger with file path and presetting
    Args:
        hundeggertype ( int): hundeggertype
        file_path ( str): file_path
        presetting ( str): presetting

    Returns:
        None
    """

def export_btl_with_presetting(btl_version: int, file_path: str, presetting: str) -> None:
    """export btl with presetting
    Args:
        btl_version ( int): btl_version
        file_path ( str): file_path
        presetting ( str): presetting

    Returns:
        None
    """

def calculate_btl_machine_data(elements: List[int], btl_version: int) -> None:
    """calculate btl machine data
    Args:
        elements ( List[int]): elements
        btl_version ( int): btl_version

    Returns:
        None
    """

def calculate_hundegger_machine_data(elements: List[int], hunderggertype: int) -> None:
    """calculate hundegger machine data
    Args:
        elements ( List[int]): elements
        hunderggertype ( int): hunderggertype

    Returns:
        None
    """

def load_hundegger_calculation_set(hundeggertype: int, file_path: str) -> None:
    """load hundegger calculation set
    Args:
        hundeggertype ( int): hundeggertype
        file_path ( str): file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_silent(hundeggertype: int, file_path: str) -> None:
    """export hundegger with file path silent
    Args:
        hundeggertype ( int): hundeggertype
        file_path ( str): file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting_silent(hundeggertype: int, file_path: str, presetting: str) -> None:
    """export hundegger with file path and presetting silent
    Args:
        hundeggertype ( int): hundeggertype
        file_path ( str): file_path
        presetting ( str): presetting

    Returns:
        None
    """

