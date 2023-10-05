
from typing import List
from enum import IntEnum, unique
from .ifc_options import *
from .extended_settings import extended_settings
from .output_type import output_type
from .process_type import process_type
from .element_type import element_type
from .point_3d import point_3d
from .element_module_properties import element_module_properties
from .ifc_2x3_element_type import ifc_2x3_element_type
from .node_symbol import node_symbol
from .element_module_detail import element_module_detail
from .division_zone_direction import division_zone_direction
from .shortcut_key import shortcut_key, shortcut_key_modifier
from .btl_version import btl_version
from .weinmann_mfb_version import weinmann_mfb_version
from .hundegger_machine_type import hundegger_machine_type
from .rhino_options import rhino_options
from .edge_list import edge_list
from .facet_list import facet_list
from .polygon_list import polygon_list
from .vertex_list import vertex_list
from .element_grouping_type import element_grouping_type
from .element_type import element_type


class layer_settings():
    def __init__(self) -> None:
        pass


class rgb_color():
    def __init__(self, r: int, b: int, g: int) -> None:
        self.r = r
        self.b = b
        self.g = g


class visibility_state():
    def __init__(self) -> None:
        pass


class activation_state():
    def __init__(self) -> None:
        pass


def get_auto_attribute_elements() -> List[int]:
    """Get ontly the elements of the selected types in the attribute manager dialog. All other elements will 
    get an empty attribute value.

    Returns:
        List[int]: element IDs
    """


def set_auto_attribute(elements: List[int], value: str) -> None:
    """Set the auto attribute to the selected element types. 

    Args:
        elements (List[int]): element IDs 
        value (str): attribute 
    """
