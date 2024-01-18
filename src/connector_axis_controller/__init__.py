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
    """create standard connector
    Args:
        axis_name ( str): axis_name
        point1 ( point_3d): point1
        point2 ( point_3d): point2

    Returns:
        int
    """

def set_bolt_length(axis_id: int, length: float) -> None:
    """set bolt length
    Args:
        axis_id ( int): axis_id
        length ( float): length

    Returns:
        None
    """

def set_bolt_length_automatic(axis_id: int, length_automatic: bool) -> None:
    """set bolt length automatic
    Args:
        axis_id ( int): axis_id
        length_automatic ( bool): length_automatic

    Returns:
        None
    """

def set_diameter(axis_id: int, diameter: float) -> None:
    """set diameter
    Args:
        axis_id ( int): axis_id
        diameter ( float): diameter

    Returns:
        None
    """

def set_section_diameter(axis_id: int, section_nr: int, diameter: float) -> None:
    """set section diameter
    Args:
        axis_id ( int): axis_id
        section_nr ( int): section_nr
        diameter ( float): diameter

    Returns:
        None
    """

def check_axis(axis_id: int) -> bool:
    """check axis
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
    """update axis cutting ability
    Args:
        axis_i_ds ( List[int]): axis_i_ds

    Returns:
        None
    """

def set_bolt_item(axis_id: int, item_guid: str) -> None:
    """set bolt item
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
    """start configuration dialog
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
    """get bolt length
    Args:
        axis_id ( int): axis_id

    Returns:
        float
    """

def get_bolt_over_length(axis_id: int) -> float:
    """get bolt over length
    Args:
        axis_id ( int): axis_id

    Returns:
        float
    """

def set_bolt_over_length(axis_id: int, over_length: float) -> None:
    """set bolt over length
    Args:
        axis_id ( int): axis_id
        over_length ( float): over_length

    Returns:
        None
    """

def get_bolt_length_automatic(axis_id: int) -> bool:
    """get bolt length automatic
    Args:
        axis_id ( int): axis_id

    Returns:
        bool
    """

def get_bolt_item_guid(axis_id: int) -> str:
    """get bolt item guid
    Args:
        axis_id ( int): axis_id

    Returns:
        str
    """

def get_section_diameter(axis_id: int, section_nr: int) -> float:
    """get section diameter
    Args:
        axis_id ( int): axis_id
        section_nr ( int): section_nr

    Returns:
        float
    """

def get_axis_items_guids(axis_id: int) -> List[str]:
    """get axis items guids
    Args:
        axis_id ( int): axis_id

    Returns:
        List[str]
    """

def get_axis_item_name(guid: str) -> str:
    """get axis item name
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_material(guid: str) -> str:
    """get axis item material
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_norm(guid: str) -> str:
    """get axis item norm
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_strength_category(guid: str) -> str:
    """get axis item strength category
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_axis_item_user_field(guid: str, user_item_nr: int) -> str:
    """get axis item user field
    Args:
        guid ( str): guid
        user_item_nr ( int): user_item_nr

    Returns:
        str
    """

def get_axis_item_order_number(guid: str) -> str:
    """get axis item order number
    Args:
        guid ( str): guid

    Returns:
        str
    """

def get_bolt_order_number(axis_id: int) -> str:
    """get bolt order number
    Args:
        axis_id ( int): axis_id

    Returns:
        str
    """

def get_section_count(axis_id: int) -> int:
    """get section count
    Args:
        axis_id ( int): axis_id

    Returns:
        int
    """

def get_section_material_name(axis_id: int, section_nr: int) -> str:
    """get section material name
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
    """get standard connector list
    Args:

    Returns:
        List[str]
    """

