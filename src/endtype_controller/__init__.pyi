def get_last_error(error_code: int) -> str:
    """Gets the last error.

    Args:
        error_code: error code

    Returns:
        error string
    """

def get_endtype_id(name: str) -> int:
    """Gets the endtypeID by endtypename

    Args:
        name: name

    Returns:
        end-type id
    """

def get_endtype_id_start(element_id: int) -> int:
    """Gets the endtypeID of the start face

    Args:
        element_id: element_id

    Returns:
        int
    """

def get_endtype_id_end(element_id: int) -> int:
    """Gets the endtypeID of the end face

    Args:
        element_id: element_id

    Returns:
        int
    """

def get_endtype_id_facet(a0: int, a1: int) -> int:
    """get endtype id facet

    Args:
        a0: a0
        a1: a1

    Returns:
        int
    """

def set_endtype_name_start(element_id: int, name: str) -> None:
    """Sets the endtype to start face by endtypename

    Args:
        element_id: element_id
        name: name

    """

def set_endtype_name_end(element_id: int, name: str) -> None:
    """Sets the endtype to end face by endtypename

    Args:
        element_id: element_id
        name: name

    """

def set_endtype_name_facet(a0: int, a1: str, a2: int) -> None:
    """set endtype name facet

    Args:
        a0: a0
        a1: a1
        a2: a2

    """

def set_endtype_id_start(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to start face by endtypeID

    Args:
        element_id: element_id
        endtype_id: endtype_id

    """

def set_endtype_id_end(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to end face by endtypeID

    Args:
        element_id: element_id
        endtype_id: endtype_id

    """

def set_endtype_id_facet(a0: int, a1: int, a2: int) -> None:
    """set endtype id facet

    Args:
        a0: a0
        a1: a1
        a2: a2

    """

def clear_errors() -> None:
    """clear errors

    """

def create_new_endtype(endtype_name: str, endtype_id: int, folder_name: str) -> int:
    """Creates a new Endtype

    Args:
        endtype_name: endtype_name
        endtype_id: endtype_id
        folder_name: folder_name

    Returns:
        int
    """

def get_endtype_name(element_id: int) -> str:
    """Gets the endtypename by endtypeID

    Args:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_start(element_id: int) -> str:
    """Gets the endtypename of the start face

    Args:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_end(element_id: int) -> str:
    """Gets the endtypename of the end face

    Args:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_facet(a0: int, a1: int) -> str:
    """get endtype name facet

    Args:
        a0: a0
        a1: a1

    Returns:
        str
    """

from typing import List

def get_existing_tenon_ids() -> List[int]:
    """Get the existing tenon endtypeIDs

    Returns:
        list of existing tenon endtypeIDs (List[int])
    """

def get_existing_lengthening_ids() -> List[int]:
    """Get the existing lengthening endtypeIDs

    Returns:
        list of existing lengthening endtypeIDs (List[int])
    """

def get_existing_dovetail_ids() -> List[int]:
    """Get the existing dovetail endtypeIDs

    Returns:
        list of existing dovetail endtypeIDs (List[int])
    """

def get_existing_dovetail_dado_ids() -> List[int]:
    """Get the existing dado endtypeIDs

    Returns:
        list of existing dado endtypeIDs (List[int])
    """

def get_existing_japanese_tenon_ids() -> List[int]:
    """Get the existing japanese-tenon endtypeIDs

    Returns:
        list of existing japanese-tenon endtypeIDs (List[int])
    """

def start_endtype_dialog() -> int:
    """Start endtype dialog

    Returns:
        Selected endtypeID (int)
    """

