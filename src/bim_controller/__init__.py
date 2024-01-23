from typing import List
from cadwork import ifc_2x3_element_type
from cadwork import ifc_options


def get_last_error(a0: int) -> str:
    """get last error
    Args:
        a0 ( int): a0

    Returns:
        str
    """


def get_ifc_guid(id: int) -> str:
    """get ifc guid
    Args:
        id ( int): id

    Returns:
        str
    """


def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """


def get_ifc2x3_element_type(element_id: int) -> ifc_2x3_element_type:
    """get ifc2x3 element type
    Args:
        element_id ( int): element_id

    Returns:
        ifc_2x3_element_type
    """


def set_ifc2x3_element_type(element_i_ds: List[int], element_type: None) -> None:
    """set ifc2x3 element type
    Args:
        element_i_ds ( List[int]): element_i_ds
        element_type ( None): element_type

    Returns:
        None
    """


def import_ifc_as_graphical_object(file_path: str) -> bool:
    """import ifc as graphical object
    Args:
        file_path ( str): file_path

    Returns:
        bool
    """


def import_bcf(file_path: str) -> bool:
    """import bcf
    Args:
        file_path ( str): file_path

    Returns:
        bool
    """


def export_bcf(file_path: str) -> bool:
    """export bcf
    Args:
        file_path ( str): file_path

    Returns:
        bool
    """


def export_ifc(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc
    Args:
        element_i_ds ( List[int]): element_i_ds
        file_path ( str): file_path

    Returns:
        bool
    """


def import_ifc_return_exchange_objects(file_path: str) -> List[int]:
    """import ifc return exchange objects
    Args:
        file_path ( str): file_path

    Returns:
        List[int]
    """


def convert_exchange_objects(exchange_objects: List[int]) -> List[int]:
    """convert exchange objects
    Args:
        exchange_objects ( List[int]): exchange_objects

    Returns:
        List[int]
    """


def set_storey_height(building: str, storey: str, height: float) -> None:
    """set storey height
    Args:
        building ( str): building
        storey ( str): storey
        height ( float): height

    Returns:
        None
    """


def set_building_and_storey(element_id_list: List[int], building: str, storey: str) -> None:
    """set building and storey
    Args:
        element_id_list ( List[int]): element_id_list
        building ( str): building
        storey ( str): storey

    Returns:
        None
    """


def get_building(element: int) -> str:
    """get building
    Args:
        element ( int): element

    Returns:
        str
    """


def get_storey(element: int) -> str:
    """get storey
    Args:
        element ( int): element

    Returns:
        str
    """


def get_storey_height(building: str, storey: str) -> float:
    """get storey height
    Args:
        building ( str): building
        storey ( str): storey

    Returns:
        float
    """


def get_ifc2x3_element_type_string(element_type: None) -> str:
    """get ifc2x3 element type string
    Args:
        element_type ( None): element_type

    Returns:
        str
    """


def get_ifc2x3_element_type_display_string(element_type: None) -> str:
    """get ifc2x3 element type display string
    Args:
        element_type ( None): element_type

    Returns:
        str
    """


def get_all_buildings() -> List[str]:
    """get all buildings
    Args:

    Returns:
        List[str]
    """


def get_all_storeys(building: str) -> List[str]:
    """get all storeys
    Args:
        building ( str): building

    Returns:
        List[str]
    """


def export_ifc2x3_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc2x3 silently
    Args:
        element_i_ds ( List[int]): element_i_ds
        file_path ( str): file_path

    Returns:
        bool
    """


def export_ifc4_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc4 silently
    Args:
        element_i_ds ( List[int]): element_i_ds
        file_path ( str): file_path

    Returns:
        bool
    """


def get_element_id_from_base64_ifc_guid(a1: str) -> int:
    """get element id from base64 ifc guid
    Args:
        a1 ( str): a1

    Returns:
        int
    """


def get_ifc_base64_guid(element_id: int) -> str:
    """get ifc base64 guid
    Args:
        element_id ( int): element_id

    Returns:
        The IFC GUID in base64 string format ("28kif20KPEuBjk2m1N3ep$"). (str)
    """


def export_ifc2x3_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc2x3 silently with options
    Args:
        element_i_ds ( List[int]): element_i_ds
        file_path ( str): file_path
        options ( ifc_options): options

    Returns:
        bool
    """


def export_ifc4_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc4 silently with options
    Args:
        element_i_ds ( List[int]): element_i_ds
        file_path ( str): file_path
        options ( ifc_options): options

    Returns:
        bool
    """
