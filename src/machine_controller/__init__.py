
def export_btl(version: int, file: str) -> None: 
    """Exports a BTL file

    Args:
        version (int): BTL version
        file (str): file path
    """
def export_weinmann_mfb(version: int) -> None: 
    """ Exports a WUP file

    Args:
        version (int): WUP version
    """
def export_hundegger(version: int) -> None: 
    """Exports a Hundegger file

    Args:
        version (int): hundegger type
    """
def export_hundegger_with_file_path(version: int, file: str) -> None: 
    """Exports a Hundegger file

    Args:
        version (int): hundegger type
        file (str): file path
    """
def export_btl_with_presetting(version: int, file:str, presetting: str) -> None:
    """Exports a BTL file with a presetting file

    Args:
        version (int): BTL version
        file (str): file path
        presetting (str): export presetting file .xml
    """
def export_hundegger_with_file_path_and_presetting(type: int, file: str, presetting: str) -> None:
    """Exports a Hundegger file

    Args:
        type (int): hundegger type
        file (str): file path
        presetting (str): export presetting file .xml
    """
def load_hundegger_calculation_set(type: int, file:str) -> None:
    """

    Args:
        type (int): hundegger type
        file (str): file path
    """