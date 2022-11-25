from typing import List

from cadwork import (point_3d)

def create_standard_connector(name: str, start: point_3d, end: point_3d) -> int: 
    """Creates a standard connector axis between two points.

    Args:
        name (str): Name of the standard axis
        start (point_3d): Point 1
        end (point_3d): Point 2

    Returns:
        int: element ID
    """
def get_item_guid_by_name(name: str, number: int) -> str: 
    """Get CA guid item by element name
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): CA name
        number (int): item type

    Returns:
        str: guid
    """
def get_bolt_length(number: int) -> float: 
    """Gets the Bolt Length
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID

    Returns:
        float: bolt length
    """
def set_bolt_length(number: int, value: float) -> None: 
    """Sets the Bolt Length
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID
        value (float): length
    """
def get_bolt_over_length(number: int) -> float: 
    """Gets the Bolt OverLength
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID

    Returns:
        float: bolt length
    """
def set_bolt_over_length(number: int, value: float) -> None: 
    """Set bolt OverLength

    Args:
        number (int): element ID
        value (float): length
    """
def get_bolt_length_automatic(number: int) -> bool: 
    """Returns if Bolt Length Automatic is set
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID

    Returns:
        bool: check if automatic is set
    """
def set_bolt_length_automatic(number: int, value: bool) -> None: 
    """Set bolt length automatic

    Args:
        number (int): element ID
        value (bool): length automatic
    """
def get_bolt_item_guid(number: int) -> str: 
    """Gets the Guid of the Bolt Item
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): _description_

    Returns:
        str: _description_
    """
def set_bolt_item(number: int, item: str) -> None: 
    """Sets the Bolt Item

    Args:
        number (int): element ID
        item (str): Item Guid
    """
def set_diameter(number: int, value: float) -> None: 
    """Sets the Drilling Diameter

    Args:
        number (int): element ID
        value (float): diameter
    """
def set_section_diameter(number: int, section_nr: int, value: float) -> None: 
    """Sets the Drilling Diameter for a specific Sections

    Args:
        number (int): element ID
        section_nr (int): Section number
        value (float): diameter
    """
def get_section_diameter(number: int, section_nr: int) -> float: 
    """Gets the Drilling Diameter of a specific Sections
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID
        other_number (int): Section number

    Returns:
        float: diameter
    """

def get_section_count(element: int) -> int:
    """Return the number of section
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): axis ID

    Returns:
        int: number of section
    """

def get_section_material_name(element: int, section_nr:int) -> str:
    """Returns material of a section contact element
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): axis ID
        section_nr (int): section nr

    Returns:
        str: material name
    """

def get_axis_items_guids(number: int) -> List[str]: 
    """Returns a list of GUIDs of all axis items.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID

    Returns:
        List[str]: elemnt IDs
    """
def get_axis_item_name(guid: str) -> str: 
    """Returns the name of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid

    Returns:
        str: element name
    """
def get_axis_item_material(name: str) -> str: 
    """Returns the material of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid

    Returns:
        str: element name
    """
def get_axis_item_norm(name: str) -> str: 
    """Returns the norm of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid

    Returns:
        str: norm
    """
def get_axis_item_strength_category(name: str) -> str: 
    """Returns the strength category of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid

    Returns:
        str: strength category 
    """
def get_axis_item_user_field(name: str, number: int) -> str: 
    """Returns an userfield value of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid
        number (int): item number

    Returns:
        str: item user field
    """
def get_axis_item_order_number(name: str) -> str: 
    """Returns the strength category of an axis item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): guid

    Returns:
        str: item order number
    """
def get_bolt_order_number(number: int) -> str: 
    """Returns the ordernumber of a bolt item.
    
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): element ID

    Returns:
        str: Order number
    """
def check_axis(number: int) -> bool: 
    """Check connector axis. 

    Args:
        number (int): element ID

    Returns:
        bool: result
    """

def update_axis_cutting_ability(elements:List[int]) -> None:
    """Update Connector axis cutting ability.

    Args:
        elements (List[int]): element IDs
    """

def get_section_contact_element(element: int, section_nr:int) -> int:
    """Get section contact element.
    
    Examples:
        >>> element_ids = [610415]
        >>> ac.get_section_contact_element(*element_ids, 0)
        >>> 545121

    Args:
        element (int): a axis ID
        section_nr (int): a section number

    Returns:
        int: element ID
    """