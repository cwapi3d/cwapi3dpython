from typing import List
from cadwork import (ifc_2x3_element_type, ifc_options)


def get_ifc_guid(element: int) -> str:
    """Get readable ifc guid. Convert readable guid to IfcGuid, see -> https://github.com/IfcOpenShell/IfcOpenShell/blob/master/src/ifcopenshell-python/ifcopenshell/guid.py

    Args:
        element (int): element ID

    Returns:
        str: readable guid
    """


def set_building_and_storey(elements: List[int], building: str, storey: str) -> None:
    """Set bulding and storey 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]): element IDs
        building (str): building name
        storey (str): storey name
    """


def get_building(element: int) -> str:
    """Get building name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: building name
    """


def get_storey(element: int) -> str:
    """Get Storey

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: storey name
    """


def get_ifc2x3_element_type(element: int) -> ifc_2x3_element_type:
    """Get IFC element type. 

    Args:
        element (int): element ID

    Returns:
        ifc_2x3_element_type: ifc type 
    """


def set_ifc2x3_element_type(elements: List[int], ifc_2x3_element_type: ifc_2x3_element_type) -> None:
    """Set IFC element type.

    Args:
        elements (List[int]): element IDs
        ifc_2x3_element_type (ifc_2x3_element_type): cadwork ifc element type
    """


def import_ifc_as_graphical_object(file: str) -> None:
    """Import ifc as graphical object

    Args:
        file (str): path to ifc file
    """


def import_bcf(file: str) -> None:
    """Import bcf file.

    Args:
        file (str): path to bcf file
    """


def export_bcf(file: str) -> None:
    """Export bcf file. 

    Args:
        file (str): Destination path 
    """


def export_ifc(elements: List[int], file: str) -> bool:
    """Export an ifc file.

    Args:
        elements (List[int]): element IDs
        file (str): Destination path 
    """


def convert_exchange_objects(elements: List[int]) -> List[int]:
    """Convert exchange objects to cadwork elements 

    Args:
        elements (List[int]): element IDs

    Returns:
        List[int]: converted elements 
    """


def get_all_buildings() -> List[str]:
    """Get all, in 3D, existing buildings 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[str]: building names 
    """


def get_all_storeys(building_name: str) -> List[str]:
    """Get all Storeys from a building.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        building_name (str): building name

    Returns:
        List[str]: storey names 
    """


def get_storey_height(building_name: str, storey_name: str) -> float:
    """Get the storey height. 

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        building_name (str): building name
        storey_name (str): storey name

    Returns:
        float: storey elevation height
    """


def import_ifc_return_exchange_objects(file_path: str) -> None:
    """Import ifc as exchange objects

    Args:
        file_path (str): file path
    """


def set_storey_height(building_name: str, storey_name: str, height: float) -> None:
    """Set the storey elevation. 

    Args:
        building_name (str): building name
        storey_name (str): storey name
        height (float): storey elevation 
    """


def get_ifc2x3_element_type_string(ifc_2x3_element_type: ifc_2x3_element_type) -> str:
    """Get ifc tpye as a string

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        ifc_2x3_element_type (ifc_2x3_element_type): cadwork ifc element type

    Returns:
        str: entity name
    """


def get_ifc2x3_element_type_display_string(ifc_2x3_element_type: ifc_2x3_element_type) -> str:
    """Get ifc tpye display string

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        ifc_2x3_element_type (ifc_2x3_element_type): cadwork ifc element type

    Returns:
        str: entity name
    """


def export_ifc2x3_silently(elements: List[int], file: str) -> bool:
    """Export an ifc file. Elements without an IfcType get a matching IfcType assigned.
    Elements without a building or storey get the default building and storey assigned. 

    Args:
        elements (List[int]): element IDs
        file (str): Destination path 

    Returns:
        bool: True if export was successful
    """


def export_ifc4_silently(elements: List[int], file: str) -> bool:
    """Export an ifc file. Elements without an IfcType get a matching IfcType assigned.
    Elements without a building or storey get the default building and storey assigned. 

    Args:
        elements (List[int]): element IDs
        file (str): Destination path 

    Returns:
        bool: True if export was successful
    """


def get_element_id_from_base64_ifc_guid(base64_ifc_guid: str) -> int:
    """Get element id from base64 ifc guid
    IFC-GUID must be a fixed 22 character length string

    Examples:
     >>> get_element_id_from_base64_ifc_guid("28kif20KPEuBjk2m1N3ep$")
        546169

    Args:
        base64_ifc_guid (str): base64 ifc guid

    Returns:
        int: element id
    """


def get_ifc_base64_guid(element: int) -> str:
    """Get ifc base64 guid from element id

    Examples:
     >>> get_ifc_base64_guid(546169)
        "28kif20KPEuBjk2m1N3ep$"

    Args:
        element (int): element id

    Returns:
        str: base64 ifc guid
    """


def export_ifc2x3_silently_with_options(elements: List[int], file: str, options: ifc_options) -> bool:
    """Export an ifc file. Elements without an IfcType get a matching IfcType assigned.
    Elements without a building or storey get the default building and storey assigned. 
    Create an ifc_options object and set the desired options.

    Examples:
        >>> import cadwork
        >>> import bim_controller
        >>> import element_controller
        >>> ifc_options = cadwork.ifc_options()
        >>> ifc_options_level_of_detail = ifc_options.get_ifc_options_level_of_detail()
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_cut_drillings(True)
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_export_vba_drillings(True)
        >>> ifc_options_level_of_detail.set_export_vba_components(True)
        >>> element_ids = element_controller.get_active_identifiable_element_ids()
        >>> bim_controller.export_ifc2x3_silently_with_options(element_ids, "C:\\some_path\\test.ifc", ifc_options)

    Args:
        elements (List[int]): element IDs
        file (str): Destination path 
        options (ifc_options): ifc options


    Returns:
        bool: True if export was successful
    """


def export_ifc4_silently_with_options(elements: List[int], file: str, options: ifc_options) -> bool:
    """Export an ifc file. Elements without an IfcType get a matching IfcType assigned.
    Elements without a building or storey get the default building and storey assigned. 
    Create an ifc_options object and set the desired options.

    Examples:
        >>> import cadwork
        >>> import bim_controller
        >>> import element_controller
        >>> ifc_options = cadwork.ifc_options()
        >>> ifc_options_level_of_detail = ifc_options.get_ifc_options_level_of_detail()
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_cut_drillings(True)
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_export_vba_drillings(True)
        >>> ifc_options_level_of_detail.set_export_vba_components(True)
        >>> element_ids = element_controller.get_active_identifiable_element_ids()
        >>> bim_controller.export_ifc4_silently_with_options(element_ids, "C:\\some_path\\test.ifc", ifc_options)

    Args:
        elements (List[int]): element IDs
        file (str): Destination path 
        options (ifc_options): ifc options


    Returns:
        bool: True if export was successful
    """
