from typing import List
from cadwork import ifc_2x3_element_type
from cadwork import ifc_options


def get_last_error(a0: int) -> str:
    """get last error

    Parameters:
        a0: a0

    Returns:
        str
    """


def get_ifc_guid(element_id: int) -> str:
    """get ifc guid

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """


def get_ifc2x3_element_type(element_id: int) -> ifc_2x3_element_type:
    """get ifc2x3 element type

    Parameters:
        element_id: element_id

    Returns:
        ifc_2x3_element_type
    """


def set_ifc2x3_element_type(element_i_ds: List[int], element_type: None) -> None:
    """set ifc2x3 element type

    Parameters:
        element_i_ds: element_i_ds
        element_type: element_type

    Returns:
        None
    """


def import_ifc_as_graphical_object(file_path: str) -> bool:
    """import ifc as graphical object

    Parameters:
        file_path: file_path

    Returns:
        bool
    """


def import_bcf(file_path: str) -> bool:
    """import bcf

    Parameters:
        file_path: file_path

    Returns:
        bool
    """


def export_bcf(file_path: str) -> bool:
    """export bcf

    Parameters:
        file_path: file_path

    Returns:
        bool
    """


def export_ifc(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Returns:
        bool
    """


def import_ifc_return_exchange_objects(file_path: str) -> List[int]:
    """imports an IFC File and returns the ids of the Exchange Objects

    Parameters:
        file_path: file_path

    Returns:
        List[int]
    """


def set_storey_height(building: str, storey: str, height: float) -> None:
    """set storey height

    Parameters:
        building: building
        storey: storey
        height: height

    Returns:
        None
    """


def convert_exchange_objects(exchange_objects: List[int]) -> List[int]:
    """converts a list of Exchange Objects to Cadwork Elements

    Parameters:
        exchange_objects: exchange_objects

    Returns:
        List[int]
    """


def export_ifc2x3_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc2x3 silently

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Returns:
        bool
    """


def export_ifc4_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc4 silently

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Returns:
        bool
    """


def export_ifc2x3_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc2x3 silently with options

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path
        options: options

    Returns:
        bool
    """


def export_ifc4_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc4 silently with options

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path
        options: options

    Returns:
        bool
    """


def update_bmt_structure_created_elements(element_i_ds: List[int]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the active building and storey.

    Parameters:
        element_i_ds: element_i_ds

    Returns:
        None
    """


def update_bmt_structure_building_storey(element_i_ds: List[int]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the assigned Building and Storey.

    Parameters:
        element_i_ds: element_i_ds

    Returns:
        None
    """


def get_ifc_options() -> ifc_options:
    """Get the IfcOptions with the settings used in the document // *

    Returns:
        IfcOptions //
    """


def set_building_and_storey(element_id_list: List[int], building: str, storey: str) -> None:
    """set building and storey

    Parameters:
        element_id_list: element_id_list
        building: building
        storey: storey

    Returns:
        None
    """


def get_building(element: int) -> str:
    """get building

    Parameters:
        element: element

    Returns:
        str
    """


def get_storey(element: int) -> str:
    """get storey

    Parameters:
        element: element

    Returns:
        str
    """


def get_storey_height(building: str, storey: str) -> float:
    """get storey height

    Parameters:
        building: building
        storey: storey

    Returns:
        float
    """


def get_ifc2x3_element_type_string(element_type: None) -> str:
    """get ifc2x3 element type string

    Parameters:
        element_type: element_type

    Returns:
        str
    """


def get_ifc2x3_element_type_display_string(element_type: None) -> str:
    """get ifc2x3 element type display string

    Parameters:
        element_type: element_type

    Returns:
        str
    """


def get_all_buildings() -> List[str]:
    """get all buildings

    Returns:
        List[str]
    """


def get_all_storeys(building: str) -> List[str]:
    """get all storeys

    Parameters:
        building: building

    Returns:
        List[str]
    """


def get_element_id_from_base64_ifc_guid(a1: str) -> int:
    """get element id from base64 ifc guid

    Parameters:
        a1: a1

    Returns:
        int
    """


def get_ifc_base64_guid(element_id: int) -> str:
    """Get IFC base64 Guid from element ID

    Parameters:
        element_id: element_id

    Returns:
        The IFC GUID in base64 string format ("28kif20KPEuBjk2m1N3ep$").
    """
