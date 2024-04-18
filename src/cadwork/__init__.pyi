from .attribute_display_settings import attribute_display_settings
from .btl_version import btl_version
from .camera_data import camera_data
from .coordinate_system_data import coordinate_system_data
from .division_zone_direction import division_zone_direction
from .edge_list import edge_list
from .element_grouping_type import element_grouping_type
from .element_module_detail import element_module_detail
from .element_module_properties import element_module_properties
from .element_type import element_type
from .extended_settings import extended_settings
from .facet_list import facet_list
from .hundegger_machine_type import hundegger_machine_type
from .ifc_2x3_element_type import ifc_2x3_element_type
from .ifc_element_combine_behaviour import ifc_element_combine_behaviour
from .ifc_options import ifc_options
from .ifc_options_aggregation import ifc_options_aggregation
from .ifc_options_level_of_detail import ifc_options_level_of_detail
from .ifc_options_project_data import ifc_options_project_data
from .ifc_options_properties import ifc_options_properties
from .ifc_predefined_type import ifc_predefined_type
from .import_3dc_options import import_3dc_options
from .layer_settings import layer_settings
from .node_symbol import node_symbol
from .point_3d import point_3d
from .polygon_list import polygon_list
from .process_type import process_type
from .projection_type import projection_type
from .rhino_options import rhino_options
from .shortcut_key import shortcut_key
from .shortcut_key_modifier import shortcut_key_modifier
from .standard_element_type import standard_element_type
from .text_element_type import text_element_type
from .text_object_options import text_object_options
from .vertex_list import vertex_list
from .weinmann_mfb_version import weinmann_mfb_version
from .window_geometry import window_geometry
from typing import List


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
