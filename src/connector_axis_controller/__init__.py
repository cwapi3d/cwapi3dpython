from typing import List
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        str
    """

def create_standard_connector(axis_name: str, point1: point_3d, point2: point_3d) -> int:
    """Creates a standard connector axis between two points. 
    Args:
        axis_name ( str): axis_name
        point1 ( point_3d): point1
        point2 ( point_3d): point2

    Returns:
        int
    """

def set_bolt_length(axis_id: int, length: float) -> None:
    """Sets the Bolt Length 
    Args:
        axis_id ( int): axis_id
        length ( float): length

    Returns:
        None
    """

def set_bolt_length_automatic(axis_id: int, length_automatic: bool) -> None:
    """Sets the Bolt Length Automatic 
    Args:
        axis_id ( int): axis_id
        length_automatic ( bool): length_automatic

    Returns:
        None
    """

def set_diameter(axis_id: int, diameter: float) -> None:
    """Sets the Drilling Diameter for all Sections 
    Args:
        axis_id ( int): axis_id
        diameter ( float): diameter

    Returns:
        None
    """

def set_section_diameter(axis_id: int, section_nr: int, diameter: float) -> None:
    """Sets the Drilling Diameter for a specific Sections 
    Args:
        axis_id ( int): axis_id
        section_nr ( int): section_nr
        diameter ( float): diameter

    Returns:
        None
    """

def check_axis(axis_id: int) -> bool:
    """Returns if the axis is valid. 
    Args:
        axis_id ( int): axis_id

    Returns:
        bool
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def update_axis_cutting_ability(axis_i_ds: List[int]) -> None:
    """updates the Connection Config (CuttingAbility) of Axis/VBAs 
    Args:
        axis_i_ds ( List[int]): axis_i_ds

    Returns:
        None
    """

def set_bolt_item(axis_id: int, item_guid: str) -> None:
    """Sets the Bolt Item 
    Args:
        axis_id ( int): axis_id
        item_guid ( str): item_guid

    Returns:
        None
    """

def create_blank_connector(a0: float, a1: point_3d, a2: point_3d) -> int:
    """create blank connector
    Args:
        a0 ( float): a0
        a1 ( point_3d): a1
        a2 ( point_3d): a2

    Returns:
        int
    """

def import_from_file(a0: str) -> None:
    """import from file
    Args:
        a0 ( str): a0

    Returns:
        None
    """

def start_configuration_dialog() -> None:
    """Starts the ConnectorAxis configuration dialog. 
    Args:

    Returns:
        None
    """

def get_item_guid_by_name(name: str, item_type: int) -> str:
    """get item guid by name
    Args:
        name ( str): name
        item_type ( int): item_type

    Returns:
        str
    """

def get_bolt_length(axis_id: int) -> float:
    """Gets the Bolt Length 
    Args:
        axis_id ( int): axis_id

    Returns:
        float
    """

def get_bolt_over_length(axis_id: int) -> float:
    """Gets the Bolt OverLength 
    Args:
        axis_id ( int): axis_id

    Returns:
        float
    """

def set_bolt_over_length(axis_id: int, over_length: float) -> None:
    """Sets the Bolt OverLength 
    Args:
        axis_id ( int): axis_id
        over_length ( float): over_length

    Returns:
        None
    """

def get_bolt_length_automatic(axis_id: int) -> bool:
    """Returns if Bolt Length Automatic is set 
    Args:
        axis_id ( int): axis_id

    Returns:
        bool
    """

def get_bolt_item_guid(axis_id: int) -> str:
    """Gets the Guid of the Bolt Item 
    Args:
        axis_id ( int): axis_id

    Returns:
        str
    """

def get_section_diameter(axis_id: int, section_nr: int) -> float:
    """Gets the Drilling Diameter of a specific Sections 
    Args:
        axis_id ( int): axis_id
        section_nr ( int): section_nr

    Returns:
        float
    """

def get_axis_items_guids(axis_id: int) -> List[str]:
    """Returns a list of GUIDs of all axis items. 
    Args:
        axis_id ( int): axis_id

    Returns:
        List[str]
    """

def get_axis_item_name(guid: str) -> str:
    """Returns the name of an axis item. 
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_material(guid: str) -> str:
    """Returns the material of an axis item. 
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_norm(guid: str) -> str:
    """Returns the norm of an axis item. 
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_strength_category(guid: str) -> str:
    """Returns the strength category of an axis item. 
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_user_field(guid: str, user_item_nr: int) -> str:
    """Returns an userfield value of an axis item. 
    Args:
        guid ( str): guid
        user_item_nr ( int): user_item_nr

    Returns:
        str
    """

def get_axis_item_order_number(guid: str) -> str:
    """Returns the strength category of an axis item. 
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_bolt_order_number(axis_id: int) -> str:
    """Returns the ordernumber of a bolt item. 
    Args:
        axis_id ( int): axis_id

    Returns:
        str
    """

def get_section_count(axis_id: int) -> int:
    """Returns the number of sections. 
    Args:
        axis_id ( int): axis_id

    Returns:
        int
    """

def get_section_material_name(axis_id: int, section_nr: int) -> str:
    """Returns material of a section contact element. 
    Args:
        axis_id ( int): axis_id
        section_nr ( int): section_nr

    Returns:
        str
    """

def get_section_contact_element(a0: float, a1: int) -> int:
    """get section contact element
    Args:
        a0 ( float): a0
        a1 ( int): a1

    Returns:
        int
    """

def get_bolt_diameter(a0: int) -> float:
    """get bolt diameter
    Args:
        a0 ( int): a0

    Returns:
        float
    """

def get_standard_connector_list() -> List[str]:
    """Returns a list of all standard connectors. 
    Args:

    Returns:
        List[str]
    """

