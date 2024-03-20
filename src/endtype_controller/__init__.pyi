from typing import List

def get_last_error(error_code: int) -> str:
    """get last error

    Parameters:
        error_code: error_code

    Returns:
        str
    """

def get_endtype_id(name: str) -> int:
    """Gets the endtypeID by endtypename

    Parameters:
        name: name

    Returns:
        int
    """

def get_endtype_id_start(element_id: int) -> int:
    """Gets the endtypeID of the start face

    Parameters:
        element_id: element_id

    Returns:
        int
    """

def get_endtype_id_end(element_id: int) -> int:
    """Gets the endtypeID of the end face

    Parameters:
        element_id: element_id

    Returns:
        int
    """

def get_endtype_id_facet(a0: int, a1: int) -> int:
    """get endtype id facet

    Parameters:
        a0: a0
        a1: a1

    Returns:
        int
    """

def set_endtype_name_start(element_id: int, name: str) -> None:
    """Sets the endtype to start face by endtypename

    Parameters:
        element_id: element_id
        name: name

    Returns:
        None
    """

def set_endtype_name_end(element_id: int, name: str) -> None:
    """Sets the endtype to end face by endtypename

    Parameters:
        element_id: element_id
        name: name

    Returns:
        None
    """

def set_endtype_name_facet(a0: int, a1: str, a2: int) -> None:
    """set endtype name facet

    Parameters:
        a0: a0
        a1: a1
        a2: a2

    Returns:
        None
    """

def set_endtype_id_start(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to start face by endtypeID

    Parameters:
        element_id: element_id
        endtype_id: endtype_id

    Returns:
        None
    """

def set_endtype_id_end(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to end face by endtypeID

    Parameters:
        element_id: element_id
        endtype_id: endtype_id

    Returns:
        None
    """

def set_endtype_id_facet(a0: int, a1: int, a2: int) -> None:
    """set endtype id facet

    Parameters:
        a0: a0
        a1: a1
        a2: a2

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def create_new_endtype(endtype_name: str, endtype_id: int, folder_name: str) -> int:
    """Creates a new Endtype

    Parameters:
        endtype_name: endtype_name
        endtype_id: endtype_id
        folder_name: folder_name

    Returns:
        int
    """

def get_endtype_name(element_id: int) -> str:
    """Gets the endtypename by endtypeID

    Parameters:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_start(element_id: int) -> str:
    """Gets the endtypename of the start face

    Parameters:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_end(element_id: int) -> str:
    """Gets the endtypename of the end face

    Parameters:
        element_id: element_id

    Returns:
        str
    """

def get_endtype_name_facet(a0: int, a1: int) -> str:
    """get endtype name facet

    Parameters:
        a0: a0
        a1: a1

    Returns:
        str
    """

def get_existing_tenon_ids() -> List[int]:
    """Get the existing tenon endtypeIDs

    Returns:
        list of existing tenon endtypeIDs
    """

def get_existing_lengthening_ids() -> List[int]:
    """Get the existing lengthening endtypeIDs

    Returns:
        list of existing lengthening endtypeIDs
    """

def get_existing_dovetail_ids() -> List[int]:
    """Get the existing dovetail endtypeIDs

    Returns:
        list of existing dovetail endtypeIDs
    """

def get_existing_dovetail_dado_ids() -> List[int]:
    """Get the existing dado endtypeIDs

    Returns:
        list of existing dado endtypeIDs
    """

def get_existing_japanese_tenon_ids() -> List[int]:
    """Get the existing japanese-tenon endtypeIDs

    Returns:
        list of existing japanese-tenon endtypeIDs
    """

def start_endtype_dialog() -> int:
    """Start endtype dialog

    Returns:
        Selected endtypeID
    """

