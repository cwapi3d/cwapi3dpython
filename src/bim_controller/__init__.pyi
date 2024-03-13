from typing import List
from cadwork import ifc_2x3_element_type
from cadwork import ifc_options


def get_last_error(error_code: int) -> str:
    """Gets the last error.

    Args:
        error_code: error code

    Returns:
        error string
    """


def get_ifc_guid(element_id: int) -> str:
    """Gets IFC guid.

    Args:
        element_id: element id

    Returns:
        ifc guid
    """


def clear_errors() -> None:
    """Clears errors.

    """


def get_ifc2x3_element_type(element_id: int) -> ifc_2x3_element_type:
    """Gets the IFC2x3 element type.

    Args:
        element_id: element id

    Returns:
        ifc2x3 element type
    """


def set_ifc2x3_element_type(element_id_list: List[int], element_type: None) -> None:
    """Sets the IFC2x3 element type.

    Args:
        element_id_list: element id list
        element_type: element type

    """


def import_ifc_as_graphical_object(file_path: str) -> bool:
    """Imports IFC file as graphical object.

    Args:
        file_path: file path

    Returns:
        import status
    """


def import_bcf(file_path: str) -> bool:
    """Imports BCF file.

    Args:
        file_path: file path

    Returns:
        import status
    """


def export_bcf(file_path: str) -> bool:
    """Exports BCF file.

    Args:
        file_path: file path

    Returns:
        export status
    """


def export_ifc(element_id_list: List[int], file_path: str) -> bool:
    """Exports IFC file.

    Args:
        element_id_list: element id list
        file_path: file path

    Returns:
        export status
    """


def import_ifc_return_exchange_objects(file_path: str) -> List[int]:
    """Imports IFC file and returns exchange objects.

    Args:
        file_path: file path

    Returns:
        exchange objects ids
    """


def set_storey_height(building: str, storey: str, height: float) -> None:
    """Sets the storey height.

    Args:
        building: building
        storey: storey
        height: height

    """


def convert_exchange_objects(exchange_objects: List[int]) -> List[int]:
    """Converts exchange objects to Cadwork elements.

    Args:
        exchange_objects: exchange objects

    Returns:
        element id list
    """


def set_building_and_storey(element_id_list: List[int], building: str, storey: str) -> None:
    """Sets the building and storey.

    Args:
        element_id_list: element id list
        building: building
        storey: storey

    """


def get_building(element: int) -> str:
    """Gets the building.

    Args:
        element: element

    Returns:
        building
    """


def get_storey(element: int) -> str:
    """Gets the storey.

    Args:
        element: element

    Returns:
        storey
    """


def get_storey_height(building: str, storey: str) -> float:
    """Gets the storey height.

    Args:
        building: building
        storey: storey

    Returns:
        storey height
    """


def get_ifc2x3_element_type_string(element_type: None) -> str:
    """Gets the IFC2x3 element type string.

    Args:
        element_type: element_type

    Returns:
        ifc2x3 element type string
    """


def get_ifc2x3_element_type_display_string(element_type: None) -> str:
    """Gets the IFC2x3 element type display string.

    Args:
        element_type: element_type

    Returns:
        ifc2x3 element type display string
    """


def get_all_buildings() -> List[str]:
    """Gets all the buildings.

    Returns:
        building list
    """


def get_all_storeys(building: str) -> List[str]:
    """Gets all the storeys.

    Args:
        building: building

    Returns:
        storey list
    """


def export_ifc2x3_silently(element_id_list: List[int], file_path: str) -> bool:
    """Exports IFC2x3 file silently.

    Args:
        element_id_list: element id list
        file_path: file path

    Returns:
        export status
    """


def export_ifc4_silently(element_id_list: List[int], file_path: str) -> bool:
    """Exports IFC4 file silently.

    Args:
        element_id_list: element id list
        file_path: file path

    Returns:
        export status
    """


def get_element_id_from_base64_ifc_guid(ifc_guid: str) -> int:
    """Gets the element ID from base64 IFC guid.

    Args:
        ifc_guid: ifc guid

    Returns:
        element id
    """


def get_ifc_base64_guid(element_id: int) -> str:
    """Gets the IFC base64 guid from element ID.

    Examples:
        >>> bim_controller.get_ifc_base64_guid(element)
        "28kif20KPEuBjk2m1N3ep$"

    Args:
        element_id: element id

    Returns:
        ifc guid
    """


def export_ifc2x3_silently_with_options(element_id_list: List[int], file_path: str, options: ifc_options) -> bool:
    """Exports IFC2x3 file silently with options.

    Args:
        element_id_list: element id list
        file_path: file path
        options: options

    Returns:
        export status
    """


def export_ifc4_silently_with_options(element_id_list: List[int], file_path: str, options: ifc_options) -> bool:
    """Exports IFC4 file silently with options.

    Args:
        element_id_list: element id list
        file_path: file path
        options: options

    Returns:
        export status
    """


def update_bmt_structure(element_id_list: List[int]) -> None:
    """Updates the BIM Manager tree structure for specified elements.

    Args:
        element_id_list: element id list

    """


def update_bmt_structure_created_elements(element_id_list: List[int]) -> None:
    """Inserts elements into the BIM Manager adds them to the active building and storey.

    Args:
        element_id_list: element id list

    """


def update_bmt_structure_building_storey(element_id_list: List[int]) -> None:
    """Inserts elements into the BIM Manager adds them to the active building and storey.

    Args:
        element_id_list: element id list

    """


def get_ifc_options() -> ifc_options:
    """Gets the IFC options with the settings used in the document.

    Returns:
        ifc options
    """
