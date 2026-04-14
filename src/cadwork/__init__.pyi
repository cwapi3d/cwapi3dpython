"""cadwork Python API type definitions.

This module re-exports all cadwork data types, enumerations, and utility classes.

Usage::

    from cadwork import point_3d, element_type, rgb_color

    # or
    import cadwork
    p = cadwork.point_3d(0.0, 0.0, 0.0)
"""

# --- Type aliases ---
from .api_types import AxisId as AxisId
from .api_types import ColorId as ColorId
from .api_types import ElementId as ElementId
from .api_types import EndtypeId as EndtypeId
from .api_types import MaterialId as MaterialId
from .api_types import MenuIndex as MenuIndex
from .api_types import MultiLayerSetId as MultiLayerSetId
from .api_types import ReferenceSide as ReferenceSide
from .api_types import UnsignedInt as UnsignedInt
from .api_types import UserAttributeId as UserAttributeId

# --- Data classes ---
from .active_point_result import active_point_result as active_point_result
from .attribute_display_settings import attribute_display_settings as attribute_display_settings
from .bim_team_upload_result import bim_team_upload_result as bim_team_upload_result
from .camera_data import camera_data as camera_data
from .coordinate_system_data import coordinate_system_data as coordinate_system_data
from .double_shoulder_options import double_shoulder_options as double_shoulder_options
from .edge_list import edge_list as edge_list
from .element_filter import element_filter as element_filter
from .element_map_query import element_map_query as element_map_query
from .element_module_detail import element_module_detail as element_module_detail
from .element_module_properties import element_module_properties as element_module_properties
from .extended_settings import extended_settings as extended_settings
from .facet_list import facet_list as facet_list
from .heel_shoulder_beam_geometry import heel_shoulder_beam_geometry as heel_shoulder_beam_geometry
from .heel_shoulder_options import heel_shoulder_options as heel_shoulder_options
from .hit_result import hit_result as hit_result
from .ifc_material_definition import ifc_material_definition as ifc_material_definition
from .ifc_options import ifc_options as ifc_options
from .ifc_options_aggregation import ifc_options_aggregation as ifc_options_aggregation
from .ifc_options_level_of_detail import ifc_options_level_of_detail as ifc_options_level_of_detail
from .ifc_options_project_data import ifc_options_project_data as ifc_options_project_data
from .ifc_options_properties import ifc_options_properties as ifc_options_properties
from .import_3dc_options import import_3dc_options as import_3dc_options
from .layer_settings import layer_settings as layer_settings
from .point import point as point
from .point_3d import point_3d as point_3d
from .polygon_list import polygon_list as polygon_list
from .rhino_options import rhino_options as rhino_options
from .rgb_color import rgb_color as rgb_color
from .shoulder_beam_geometry import shoulder_beam_geometry as shoulder_beam_geometry
from .shoulder_options import shoulder_options as shoulder_options
from .text_object_options import text_object_options as text_object_options
from .vertex_list import vertex_list as vertex_list
from .window_geometry import window_geometry as window_geometry

# --- Enumerations ---
from .bim_team_upload_result_code import bim_team_upload_result_code as bim_team_upload_result_code
from .btl_version import btl_version as btl_version
from .dimension_base_format import dimension_base_format as dimension_base_format
from .display_attribute import display_attribute as display_attribute
from .division_zone_direction import division_zone_direction as division_zone_direction
from .dxf_export_version import dxf_export_version as dxf_export_version
from .dxf_layer_format_type import dxf_layer_format_type as dxf_layer_format_type
from .element_grouping_type import element_grouping_type as element_grouping_type
from .element_type import element_type as element_type
from .hundegger_machine_type import hundegger_machine_type as hundegger_machine_type
from .ifc_2x3_element_type import ifc_2x3_element_type as ifc_2x3_element_type
from .ifc_element_combine_behaviour import ifc_element_combine_behaviour as ifc_element_combine_behaviour
from .ifc_predefined_type import ifc_predefined_type as ifc_predefined_type
from .multi_layer_cover_type import multi_layer_cover_type as multi_layer_cover_type
from .multi_layer_subtype import multi_layer_subtype as multi_layer_subtype
from .multi_layer_type import multi_layer_type as multi_layer_type
from .node_symbol import node_symbol as node_symbol
from .process_type import process_type as process_type
from .projection_type import projection_type as projection_type
from .shortcut_key import shortcut_key as shortcut_key
from .shortcut_key_modifier import shortcut_key_modifier as shortcut_key_modifier
from .shoulder_drilling_orientation import shoulder_drilling_orientation as shoulder_drilling_orientation
from .standard_element_type import standard_element_type as standard_element_type
from .text_element_type import text_element_type as text_element_type
from .vba_catalog_item_type import vba_catalog_item_type as vba_catalog_item_type
from .weinmann_mfb_version import weinmann_mfb_version as weinmann_mfb_version

__all__ = [
    # Type aliases
    "AxisId",
    "ColorId",
    "ElementId",
    "EndtypeId",
    "MaterialId",
    "MenuIndex",
    "MultiLayerSetId",
    "ReferenceSide",
    "UnsignedInt",
    "UserAttributeId",
    # Data classes
    "active_point_result",
    "attribute_display_settings",
    "bim_team_upload_result",
    "camera_data",
    "coordinate_system_data",
    "double_shoulder_options",
    "edge_list",
    "element_filter",
    "element_map_query",
    "element_module_detail",
    "element_module_properties",
    "extended_settings",
    "facet_list",
    "heel_shoulder_beam_geometry",
    "heel_shoulder_options",
    "hit_result",
    "ifc_material_definition",
    "ifc_options",
    "ifc_options_aggregation",
    "ifc_options_level_of_detail",
    "ifc_options_project_data",
    "ifc_options_properties",
    "import_3dc_options",
    "layer_settings",
    "point",
    "point_3d",
    "polygon_list",
    "rhino_options",
    "rgb_color",
    "shoulder_beam_geometry",
    "shoulder_options",
    "text_object_options",
    "vertex_list",
    "window_geometry",
    # Enumerations
    "bim_team_upload_result_code",
    "btl_version",
    "dimension_base_format",
    "display_attribute",
    "division_zone_direction",
    "dxf_export_version",
    "dxf_layer_format_type",
    "element_grouping_type",
    "element_type",
    "hundegger_machine_type",
    "ifc_2x3_element_type",
    "ifc_element_combine_behaviour",
    "ifc_predefined_type",
    "multi_layer_cover_type",
    "multi_layer_subtype",
    "multi_layer_type",
    "node_symbol",
    "process_type",
    "projection_type",
    "shortcut_key",
    "shortcut_key_modifier",
    "shoulder_drilling_orientation",
    "standard_element_type",
    "text_element_type",
    "vba_catalog_item_type",
    "weinmann_mfb_version",
    # Module-level functions
    "get_auto_attribute_elements",
    "set_auto_attribute",
]


def get_auto_attribute_elements() -> list[int]:
    """Get only the elements of the selected types in the attribute manager dialog.

    All other elements will get an empty attribute value.

    Returns:
        list[int]: element IDs
    """


def set_auto_attribute(elements: list[int], value: str) -> None:
    """Set the auto attribute to the selected element types.

    Parameters:
        elements: element IDs
        value: attribute value
    """
