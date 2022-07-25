from typing import List
from cadwork import ifc_2x3_element_type


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
def export_ifc(elements: List[int], file: str) -> None: 
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

def get_all_storeys(building_name:str) -> List[str]:
    """Get all Storeys from a building.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        building_name (str): building name

    Returns:
        List[str]: storey names 
    """


def get_storey_height(building_name:str, storey_name:str) -> float:
    """Get the storey height. 
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        building_name (str): building name
        storey_name (str): storey name

    Returns:
        float: storey elevation height
    """


def import_ifc_return_exchange_objects(file_path:str) -> None:
    """Import ifc as exchange objects

    Args:
        file_path (str): file path
    """

def set_storey_height(building_name:str, storey_name:str, height:float) -> None:
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