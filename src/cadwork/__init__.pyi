from cadwork.rgb_color import rgb_color
from .attribute_display_settings import attribute_display_settings
from .bim_team_upload_result import bim_team_upload_result
from .bim_team_upload_result_code import bim_team_upload_result_code
from .btl_version import btl_version
from .camera_data import camera_data
from .coordinate_system_data import coordinate_system_data
from .division_zone_direction import division_zone_direction
from .double_shoulder_options import double_shoulder_options
from .edge_list import edge_list
from .element_grouping_type import element_grouping_type
from .element_module_detail import element_module_detail
from .element_module_properties import element_module_properties
from .element_type import element_type
from .extended_settings import extended_settings
from .facet_list import facet_list
from .heel_shoulder_beam_geometry import heel_shoulder_beam_geometry
from .heel_shoulder_options import heel_shoulder_options
from .hundegger_machine_type import hundegger_machine_type
from .ifc_2x3_element_type import ifc_2x3_element_type
from .ifc_element_combine_behaviour import ifc_element_combine_behaviour
from .ifc_material_definition import ifc_material_definition
from .ifc_options import ifc_options
from .ifc_options_aggregation import ifc_options_aggregation
from .ifc_options_level_of_detail import ifc_options_level_of_detail
from .ifc_options_project_data import ifc_options_project_data
from .ifc_options_properties import ifc_options_properties
from .ifc_predefined_type import ifc_predefined_type
from .import_3dc_options import import_3dc_options
from .layer_settings import layer_settings
from .multi_layer_type import multi_layer_type
from .node_symbol import node_symbol
from .point_3d import point_3d
from .polygon_list import polygon_list
from .process_type import process_type
from .projection_type import projection_type
from .rhino_options import rhino_options
from .shortcut_key import shortcut_key
from .shortcut_key_modifier import shortcut_key_modifier
from .shoulder_beam_geometry import shoulder_beam_geometry
from .shoulder_drilling_orientation import shoulder_drilling_orientation
from .shoulder_options import shoulder_options
from .standard_element_type import standard_element_type
from .text_element_type import text_element_type
from .text_object_options import text_object_options
from .vertex_list import vertex_list
from .weinmann_mfb_version import weinmann_mfb_version
from .window_geometry import window_geometry
from .element_map_query import element_map_query
from .element_filter import element_filter
from .hit_result import hit_result
from .dimension_base_format import dimension_base_format
from .dxf_layer_format_type import dxf_layer_format_type
from .dxf_export_version import dxf_export_version
from typing import List

# These assignments make each type accessible through both import styles:
# 1. Direct import: from cadwork import point_3d
# 2. Module access: import cadwork; cadwork.point_3d(...)
# Without these assignments, the classes would be imported but not exposed as callable attributes
# of the cadwork module, resulting in "not callable" errors/warnings when using the module access style.

attribute_display_settings = attribute_display_settings
bim_team_upload_result = bim_team_upload_result
bim_team_upload_result_code = bim_team_upload_result_code
btl_version = btl_version
camera_data = camera_data
coordinate_system_data = coordinate_system_data
division_zone_direction = division_zone_direction
double_shoulder_options = double_shoulder_options
edge_list = edge_list
element_grouping_type = element_grouping_type
element_module_detail = element_module_detail
element_module_properties = element_module_properties
element_type = element_type
extended_settings = extended_settings
facet_list = facet_list
heel_shoulder_beam_geometry = heel_shoulder_beam_geometry
heel_shoulder_options = heel_shoulder_options
hundegger_machine_type = hundegger_machine_type
ifc_2x3_element_type = ifc_2x3_element_type
ifc_element_combine_behaviour = ifc_element_combine_behaviour
ifc_material_definition = ifc_material_definition
ifc_options = ifc_options
ifc_options_aggregation = ifc_options_aggregation
ifc_options_level_of_detail = ifc_options_level_of_detail
ifc_options_project_data = ifc_options_project_data
ifc_options_properties = ifc_options_properties
ifc_predefined_type = ifc_predefined_type
import_3dc_options = import_3dc_options
layer_settings = layer_settings
multi_layer_type = multi_layer_type
node_symbol = node_symbol
point_3d = point_3d
polygon_list = polygon_list
process_type = process_type
projection_type = projection_type
rhino_options = rhino_options
shortcut_key = shortcut_key
shortcut_key_modifier = shortcut_key_modifier
shoulder_beam_geometry = shoulder_beam_geometry
shoulder_drilling_orientation = shoulder_drilling_orientation
shoulder_options = shoulder_options
standard_element_type = standard_element_type
text_element_type = text_element_type
text_object_options = text_object_options
vertex_list = vertex_list
weinmann_mfb_version = weinmann_mfb_version
window_geometry = window_geometry
element_map_query = element_map_query
element_filter = element_filter
hit_result = hit_result
dimension_base_format = dimension_base_format
dxf_layer_format_type = dxf_layer_format_type
dxf_export_version = dxf_export_version
rgb_color = rgb_color


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
