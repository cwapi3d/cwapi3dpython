from typing import List
from cadwork.attribute_display_settings import attribute_display_settings
from cadwork.element_grouping_type import element_grouping_type
from cadwork.element_type import element_type
from cadwork.extended_settings import extended_settings
from cadwork.layer_settings import layer_settings
from cadwork.node_symbol import node_symbol
from cadwork.process_type import process_type
from cadwork.api_types import *

def set_name(element_id_list: List[ElementId], name: str) -> None:
    """Sets the element name.

    Parameters:
        element_id_list: The element id list.
        name: The element name.
    """

def set_group(element_id_list: List[ElementId], group: str) -> None:
    """Sets the element group.

    Parameters:
        element_id_list: The element id list.
        group: The element group.
    """

def set_subgroup(element_id_list: List[ElementId], subgroup: str) -> None:
    """Sets the element subgroup.

    Parameters:
        element_id_list: The element id list.
        subgroup: The element subgroup.
    """

def set_comment(element_id_list: List[ElementId], comment: str) -> None:
    """Sets the element comment.

    Parameters:
        element_id_list: The element id list.
        comment: The element comment.
    """

def set_user_attribute(element_id_list: List[ElementId], number: UserAttributeId, user_attribute: str) -> None:
    """Sets the element user attribute.

    Parameters:
        element_id_list: The element id list.
        number: The user attribute id.
        user_attribute: The user attribute.
    """

def set_sku(element_id_list: List[ElementId], sku: str) -> None:
    """Sets the element SKU.

    Parameters:
        element_id_list: The element id list.
        sku: The element SKU.
    """

def set_production_number(element_id_list: List[ElementId], production_number: UnsignedInt) -> None:
    """Sets the element production number.

    Parameters:
        element_id_list: The element id list.
        production_number: The element production number.
    """

def set_part_number(element_id_list: List[ElementId], part_number: UnsignedInt) -> None:
    """Sets the element part number.

    Parameters:
        element_id_list: The element id list.
        part_number: The element part number.
    """

def set_additional_data(element_id_list: List[ElementId], data_id: str, data_text: str) -> None:
    """Sets the element additional data.

    Parameters:
        element_id_list: The element id list.
        data_id: The data id.
        data_text: The element additional data.
    """

def delete_additional_data(element_id_list: List[ElementId], data_id: str) -> None:
    """Deletes the element additional data.

    Parameters:
        element_id_list: The element id list.
        data_id: The data id.
    """

def set_user_attribute_name(number: UserAttributeId, user_attribute_name: str) -> None:
    """Sets the user attribute name.

    Parameters:
        number: The user attribute id.
        user_attribute_name: The user attribute name.
    """

def set_process_type_and_extended_settings_from_name(element_id_list: List[ElementId]) -> None:
    """Sets the element process type and extended settings from the element name.

    Parameters:
        element_id_list: The element id list.
    """

def set_name_process_type(name: str, process_type: process_type) -> None:
    """Sets the process type for an element name.

    Parameters:
        name: The element name.
        process_type: The process type.
    """

def set_name_extended_settings(name: str, extended_settings: extended_settings) -> None:
    """Sets the extended settings for an element name.

    Parameters:
        name: The element name.
        extended_settings: The extended settings.
    """

def set_output_type(element_id_list: List[ElementId], process_type: process_type) -> None:
    """Sets the element output type.

    Parameters:
        element_id_list: The element id list.
        process_type: The process type.
    """

def set_extended_settings(element_id_list: List[ElementId], extended_settings: extended_settings) -> None:
    """Sets the element extended settings.

    Parameters:
        element_id_list: The element id list.
        extended_settings: The extended settings.
    """

def set_wall(element_id_list: List[ElementId]) -> None:
    """Sets the element to wall.

    Deprecated : 
        Use [set_framed_wall][attribute_controller.set_framed_wall] instead.

    Parameters:
        element_id_list: The element id list.
    """


def set_floor(element_id_list: List[ElementId]) -> None:
    """Set floor.

    Deprecated : 
        Use [set_framed_floor][attribute_controller.set_framed_floor] instead.
    
    Parameters:
        element_id_list: The element id list.
    """

def set_opening(element_id_list: List[ElementId]) -> None:
    """Sets the element to opening.

    Parameters:
        element_id_list: The element id list.
    """

def set_fastening_attribute(element_id_list: List[ElementId], value: str) -> None:
    """Sets the element fastening attribute.

    Parameters:
        element_id_list: The element id list.
        value: The fastening attribute value.
    """

def set_element_material(element_id_list: List[ElementId], material: MaterialId) -> None:
    """Sets the element material.

    Parameters:
        element_id_list: The element id list.
        material: The element material id.
    """

def set_assembly_number(element_id_list: List[ElementId], assembly_number: str) -> None:
    """set assembly number.

    Parameters:
        element_id_list: The element id list.
        assembly_number: The assembly number.
    """

def set_list_quantity(element_id_list: List[ElementId], list_quantity: UnsignedInt) -> None:
    """Set list quantity.

    Parameters:
        element_id_list: The element id list.
        list_quantity: The list quantity.
    """

def set_layer_settings(element_id_list: List[ElementId], layer_settings: layer_settings) -> None:
    """Set layer settings.

    Parameters:
        element_id_list: The element id list.
        layer_settings: The layer settings.
    """

def set_ignore_in_vba_calculation(element_id_list: List[ElementId], ignore: bool) -> None:
    """Sets if the element should be ignored in VBA Calculation.

    Parameters:
        element_id_list: The element id list.
        ignore: True if the element should be ignored in VBA calculation, false otherwise.
    """

def clear_errors() -> None:
    """clear all errors.
    """

def set_reference_wall_2dc(element_id_list: List[ElementId], _2dc_file_path: str) -> None:
    """Applies a new 2dc reference wall to an element.

    Parameters:
        element_id_list: The element id list.
        _2dc_file_path: The 2dc file path.
    """

def get_user_attribute_count() -> UnsignedInt:
    """Get user attribute count.
    
    Returns:
        The count of user attributes.
    """

def set_standard_part(element_id_list: List[ElementId]) -> None:
    """Sets covers (wall,opening or floor) to standard part.

    Parameters:
        element_id_list: The element id list.
    """

def set_solid_wall(element_id_list: List[ElementId]) -> None:
    """Sets elements to solid wall.

    Parameters:
        element_id_list: The element id list.
    """

def set_log_wall(element_id_list: List[ElementId]) -> None:
    """Sets elements to log wall.

    Parameters:
        element_id_list: The element id list.
    """

def set_solid_floor(element_id_list: List[ElementId]) -> None:
    """Sets elements to solid floor.

    Parameters:
        element_id_list: The element id list.
    """


def set_roof(element_id_list: List[ElementId]) -> None:
    """Set roof.

    Deprecated : 
        Use [set_framed_roof][attribute_controller.set_framed_roof] instead.

    Parameters:
        element_id_list: The element id list.
    """

def set_solid_roof(element_id_list: List[ElementId]) -> None:
    """Sets elements to solid roof cover.

    Parameters:
        element_id_list: The element id list.
    """

def get_node_symbol(element_id: ElementId) -> node_symbol:
    """Get node symbol.

    Parameters:
        element_id: The element id.

    Returns:
        The node symbol of the element.
    """

def set_node_symbol(element_id_list: List[ElementId], symbol: node_symbol) -> None:
    """Set node symbol.

    Parameters:
        element_id_list: The element id list.
        symbol: The node symbol.
    """

def enable_attribute_display() -> None:
    """Enable attribute display.
    """

def disable_attribute_display() -> None:
    """Disable attribute display.
    """

def is_attribute_display_enabled() -> bool:
    """Is attribute display enabled.

    Returns:
        True if attribute display is enabled, false otherwise.
    """

def update_auto_attribute() -> None:
    """Update the auto attribute.
    """


def set_additional_guid(element_id_list: List[ElementId], data_id: str, guid: str) -> None:
    """Set additional guid.

    Parameters:
        element_id_list: The element id list.
        data_id: The data id.
        guid: The guid to set.
    """

def add_item_to_group_list(item: str) -> None:
    """Add item to group list.

    Parameters:
        item: The item to add in the group list.
    """


def add_item_to_subgroup_list(item: str) -> None:
    """Add item to subgroup list.

    Parameters:
        item: The item to add in the subgroup list.
    """

def add_item_to_comment_list(item: str) -> None:
    """Add item to comment list.

    Args:
        item: The item to add in the comment list.
    """


def add_item_to_sku_list(item: str) -> None:
    """Add item to sku list.

    Parameters:
        item: The item to add in the sku list.
    """


def add_item_to_user_attribute_list(attribute_number: UserAttributeId, item: str) -> None:
    """Add item to user attribute list.

    Parameters:
        attribute_number: The attribute number.
        item: The item to add in the user attribute list.
    """


def set_container_number(element_id_list: List[ElementId], number: UnsignedInt) -> None:
    """Set container number.

    Parameters:
        element_id_list: The element id list.
        number: The container number.
    """

def get_name_list_items() -> List[str]:
    """Retrieve a list of name for all items

    Returns:
        A list of names for all items.
    """


def add_item_to_name_list(item: str) -> None:
    """Add item to name list.

    Parameters:
        item: The item to add in the name list.
    """


def delete_item_from_comment_list(item: str) -> bool:
    """Delete item from comment list.

    Parameters:
        item: The item to delete from the comment list.

    Returns:
        True if the item was successfully deleted, false otherwise.
    """


def delete_item_from_group_list(item: str) -> bool:
    """Delete item from group list.

    Parameters:
        item: The item to delete from the group list.

    Returns:
        True if the item was successfully deleted, false otherwise.
    """


def delete_item_from_sku_list(item: str) -> bool:
    """Delete item from sku list.

    Parameters:
        item: The item to delete from the sku list.

    Returns:
        True if the item was successfully deleted, false otherwise.
    """


def delete_item_from_subgroup_list(item: str) -> bool:
    """Delete item from subgroup list.

    Parameters:
        item: The item to delete from the subgroup list.

    Returns:
        True if the item was successfully deleted, false otherwise.
    """


def delete_item_from_user_attribute_list(attribute_number: UserAttributeId, item: str) -> bool:
    """Delete item from user attribute list.

    Parameters:
        attribute_number: The attribute number.
        item: The item to delete from the user attribute list.

    Returns:
        True if the item was successfully deleted, false otherwise.
    """


def set_attribute_display_settings_for_2d(settings: attribute_display_settings) -> None:
    """Set attribute display settings for 2d.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_2d_with_layout(settings: attribute_display_settings) -> None:
    """Set attribute display settings for 2d with layout.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_2d_without_layout(settings: attribute_display_settings) -> None:
    """Set attribute display settings for 2d without layout.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_3d(settings: attribute_display_settings) -> None:
    """Set attribute display settings for 3d.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_3d(settings: attribute_display_settings) -> None:
    """Set attribute display settings for 3d.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_container(settings: attribute_display_settings) -> None:
    """Set attribute display settings for container.

    Parameters:
        settings: The display settings to apply.
    """

def set_attribute_display_settings_for_export_solid(settings: attribute_display_settings) -> None:
    """Set attribute display settings for export solid.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_framed_wall_axis(settings: attribute_display_settings) -> None:
    """Set attribute display settings for framed wall axis.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_framed_wall_beam(settings: attribute_display_settings) -> None:
    """Set attribute display settings for framed wall beam.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_framed_wall_beam(settings: attribute_display_settings) -> None:
    """Set attribute display settings for framed wall beam.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_framed_wall_opening(settings: attribute_display_settings) -> None:
    """Set attribute display settings for framed wall opening.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_framed_wall_panel(settings: attribute_display_settings) -> None:
    """Set attribute display settings for framed wall panel.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_log_wall_axis(settings: attribute_display_settings) -> None:
    """Set attribute display settings for log wall axis.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_log_wall_beam(settings: attribute_display_settings) -> None:
    """Set attribute display settings for log wall beam.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_log_wall_opening(settings: attribute_display_settings) -> None:
    """Set attribute display settings for log wall opening.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_log_wall_panel(settings: attribute_display_settings) -> None:
    """Set attribute display settings for log wall panel.

    Parameters:
        settings: The display settings to apply.
    """

def set_attribute_display_settings_for_machine(settings: attribute_display_settings) -> None:
    """Set attribute display settings for machine.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_nesting_element(settings: attribute_display_settings) -> None:
    """Set attribute display settings for nesting element.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_nesting_volume(settings: attribute_display_settings) -> None:
    """Set attribute display settings for nesting volume.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_solid_wall_axis(settings: attribute_display_settings) -> None:
    """Set attribute display settings for solid wall axis.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_solid_wall_beam(settings: attribute_display_settings) -> None:
    """Set attribute display settings for solid wall beam.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_solid_wall_opening(settings: attribute_display_settings) -> None:
    """Set attribute display settings for solid wall opening.

    Parameters:
        settings: The display settings to apply.
    """


def set_attribute_display_settings_for_solid_wall_panel(settings: attribute_display_settings) -> None:
    """Set attribute display settings for solid wall panel.

    Parameters:
        settings: The display settings to apply.
    """

def set_framed_floor(element_id_list: List[ElementId]) -> None:
    """Sets the elements to framed floor.

    Parameters:
        element_id_list: The element id list.
    """

def set_framed_roof(element_id_list: List[ElementId]) -> None:
    """Sets the elements to framed roof.

    Parameters:
        element_id_list: The element id list.
    """

def set_framed_wall(element_id_list: List[ElementId]) -> None:
    """Sets the element to framed wall.

    Parameters:
        element_id_list: The element id list.
    """


def get_name_list_items_by_element_type(element_type: element_type) -> List[str]:
    """Get name list items by element type.

    Parameters:
        element_type: The element type to filter by.

    Returns:
        The list of names for the specified element type.
    """

def get_name(element_id: ElementId) -> str:
    """Gets the element name.

    Parameters:
        element_id: The element id.

    Returns:
        The element name.
    """

def get_group(element_id: ElementId) -> str:
    """Gets the element group.

    Parameters:
        element_id: The element id.

    Returns:
        The element group.
    """

def get_subgroup(element_id: ElementId) -> str:
    """Gets the element subgroup.

    Parameters:
        element_id: The element id.

    Returns:
        The element subgroup.
    """

def get_comment(element_id: ElementId) -> str:
    """Gets the element comment.

    Parameters:
        element_id: The element id.

    Returns:
        The element comment.
    """

def get_user_attribute(element_id: ElementId, number: UserAttributeId) -> str:
    """Gets the element user attribute.

    Parameters:
        element_id: The element id.
        number: The user attribute number.

    Returns:
        The element user attribute.
    """

def get_sku(element_id: ElementId) -> str:
    """Gets the element SKU.

    Parameters:
        element_id: The element id.

    Returns:
        The element SKU.
    """

def get_production_number(element_id: ElementId) -> UnsignedInt:
    """Gets the element production number.

    Parameters:
        element_id: The element id.

    Returns:
        The element production number.
    """

def get_part_number(element_id: ElementId) -> UnsignedInt:
    """Gets the element part number.

    Parameters:
        element_id: The element id.

    Returns:
        The element part number.
    """

def get_additional_data(element_id: ElementId, data_id: str) -> str:
    """Gets the element additional data.

    Parameters:
        element_id: The element id.
        data_id: The data id.

    Returns:
        The element additional data.
    """

def get_user_attribute_name(number: UserAttributeId) -> str:
    """Gets the user attribute name.

    Parameters:
        number: The user attribute number.

    Returns:
        The user attribute name.
    """

def get_wall_situation(element_id: ElementId) -> str:
    """Gets the element wall situation.

    Parameters:
        element_id: The element id.

    Returns:
        The element wall situation.
    """

def get_element_material_name(element_id: ElementId) -> str:
    """Gets the element material name.

    Parameters:
        element_id: The element id.

    Returns:
        The element material name.
    """

def get_prefab_layer(element_id: ElementId) -> str:
    """Gets the element prefab layer.

    Parameters:
        element_id: The element id.

    Returns:
        The element prefab layer.
    """

def get_machine_calculation_set(element_id: ElementId) -> str:
    """Gets the element machine calculation set.

    Parameters:
        element_id: The element id.

    Returns:
        The element machine calculation set.
    """

def get_cutting_set(element_id: ElementId) -> str:
    """Gets the element cutting set.

    Parameters:
        element_id: The element id.

    Returns:
        The element cutting set.
    """

def get_name_process_type(name: str) -> process_type:
    """Gets the process type for an element name.

    Parameters:
        name: The element name.

    Returns:
        The process type.
    """

def get_name_extended_settings(name: str) -> extended_settings:
    """Gets the extended settings for an element name.

    Parameters:
        name: The element name.

    Returns:
        The extended settings.
    """

def get_output_type(element_id: ElementId) -> process_type:
    """Gets the element output type.

    Parameters:
        element_id: The element id.

    Returns:
        The element output type.
    """

def get_extended_settings(element_id: ElementId) -> extended_settings:
    """Gets the element extended settings.

    Parameters:
        element_id: The element id.

    Returns:
        The element extended settings.
    """

def get_element_type(element_id: ElementId) -> element_type:
    """Gets the element type.

    Parameters:
        element_id: The element id.

    Returns:
        The element type.
    """

def get_fastening_attribute(element_id: ElementId) -> str:
    """Get the element fastening attribute.

    Parameters:
        element_id: The element id.

    Returns:
        The element fastening attribute.
    """

def get_assembly_number(element_id: ElementId) -> str:
    """Get assembly number.

    Parameters:
        element_id: The element id.

    Returns:
        The assembly number.
    """

def get_list_quantity(element_id: ElementId) -> UnsignedInt:
    """Get list quantity.

    Parameters:
        element_id: The element id.

    Returns:
        The list quantity.
    """

def get_ignore_in_vba_calculation(element_id: ElementId) -> bool:
    """Get ignore in vba calculation.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is ignored in VBA calculation, false otherwise.
    """

def get_standard_element_name(element_id: ElementId) -> str:
    """Get standard element name.

    Parameters:
        element_id: The element id.

    Returns:
        The standard element name.
    """

def get_steel_shape_name(element_id: ElementId) -> str:
    """Get steel shape name.

    Parameters:
        element_id: The element id.

    Returns:
        The steel shape name.
    """

def is_beam(element_id: ElementId) -> bool:
    """Tests if element is beam.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a beam, false otherwise.
    """

def is_panel(element_id: ElementId) -> bool:
    """Tests if element is panel.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a panel, false otherwise.
    """

def is_opening(element_id: ElementId) -> bool:
    """Tests if element is opening.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is an opening, false otherwise.
    """

def is_wall(element_id: ElementId) -> bool:
    """Tests if element is wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a wall, false otherwise.
    """

def is_floor(element_id: ElementId) -> bool:
    """Tests if element is floor.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a floor, false otherwise.
    """

def is_roof(element_id: ElementId) -> bool:
    """Tests if element is roof.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a roof, false otherwise.
    """

def is_metal(element_id: ElementId) -> bool:
    """Tests if element is metal.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is metal, false otherwise.
    """

def is_export_solid(element_id: ElementId) -> bool:
    """Tests if element is export solid.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is an export solid, false otherwise.
    """

def is_container(element_id: ElementId) -> bool:
    """Tests if element is container.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a container, false otherwise.
    """

def is_connector_axis(element_id: ElementId) -> bool:
    """Tests if element is connector axis.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a connector axis, false otherwise.
    """

def is_drilling(element_id: ElementId) -> bool:
    """Tests if element is drilling.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is drilling, false otherwise.
    """

def is_node(element_id: ElementId) -> bool:
    """Tests if element is node.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a node, false otherwise.
    """

def is_auxiliary(element_id: ElementId) -> bool:
    """Tests if element is auxiliary.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is auxiliary, false otherwise.
    """

def is_roof_surface(element_id: ElementId) -> bool:
    """Tests if the element is roof surface.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a roof surface, false otherwise.
    """

def is_caddy_object(element_id: ElementId) -> bool:
    """Tests if the element is caddy object.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a caddy object, false otherwise.
    """

def is_envelope(element_id: ElementId) -> bool:
    """Tests if the element is an envelope.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is an envelope, false otherwise.
    """

def is_architecture_wall_2dc(element_id: ElementId) -> bool:
    """Tests if the element is a 2dc reference wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a 2dc reference wall, false otherwise.
    """

def is_architecture_wall_xml(element_id: ElementId) -> bool:
    """Tests if the element is a xml reference wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a xml reference wall, false otherwise.
    """

def is_surface(element_id: ElementId) -> bool:
    """Tests if the element is a Surface.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a Surface, false otherwise.
    """

def is_line(element_id: ElementId) -> bool:
    """Tests if the element is a Line.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a Line, false otherwise.
    """

def get_auto_attribute(element_id: ElementId, number: UnsignedInt) -> str:
    """Get auto attribute.

    Parameters:
        element_id: The element id.
        number: The auto attribute number.

    Returns:
        The auto attribute value.
    """

def get_auto_attribute_name(number: UnsignedInt) -> str:
    """Get auto attribute name.

    Parameters:
        number: The auto attribute number.

    Returns:
        The auto attribute name.
    """

def is_framed_wall(element_id: ElementId) -> bool:
    """Tests if the element is a framed wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a framed wall, false otherwise.
    """

def is_solid_wall(element_id: ElementId) -> bool:
    """Tests if the element is a solid wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a solid wall, false otherwise.
    """

def is_log_wall(element_id: ElementId) -> bool:
    """Tests if the element is a log wall.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a log wall, false otherwise.
    """

def is_framed_floor(element_id: ElementId) -> bool:
    """Tests if the element is a framed floor.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a framed floor, false otherwise.
    """

def is_solid_floor(element_id: ElementId) -> bool:
    """Tests if the element is a solid floor.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a solid floor, false otherwise.
    """

def is_framed_roof(element_id: ElementId) -> bool:
    """Tests if the element is a framed roof.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a framed roof, false otherwise.
    """

def is_solid_roof(element_id: ElementId) -> bool:
    """Tests if the element is a solid roof.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a solid roof, false otherwise.
    """


def get_additional_guid(element_id: ElementId, data_id: str) -> str:
    """Get additional guid.

    Parameters:
        element_id: The element id.
        data_id: The data id.

    Returns:
        The additional guid associated with the element and data id.
    """


def get_prefab_layer_all_assigned(element_id: ElementId) -> List[int]:
    """Get all assigned prefab layers.

    Parameters:
        element_id: The element id.

    Returns:
        The list of all assigned prefab layers for the element.
    """


def get_prefab_layer_with_dimensions(element_id: ElementId) -> List[int]:
    """Get prefab layer with dimensions.

    Parameters:
        element_id: The element id.

    Returns:
        The list of prefab layers with dimensions for the element.
    """


def get_prefab_layer_without_dimensions(element_id: ElementId) -> List[int]:
    """Get prefab layer without dimensions.

    Parameters:
        element_id: The element id.

    Returns:
        The list of prefab layers without dimensions for the element.
    """


def is_nesting_parent(element_id: ElementId) -> bool:
    """Tests if the element is a nesting parent.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a nesting parent, false otherwise.
    """


def is_nesting_raw_part(element_id: ElementId) -> bool:
    """Tests if the element is a nesting raw part.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a nesting raw part, false otherwise.
    """


def get_container_number(element_id: ElementId) -> UnsignedInt:
    """Get container number.

    Parameters:
        element_id: The element id.

    Returns:
        The container number associated with the element.
    """


def get_container_number_with_prefix(element_id: ElementId) -> str:
    """Get container number with prefix.

    Parameters:
        element_id: The element id.

    Returns:
        The container number with prefix associated with the element.
    """

def get_group_list_items() -> List[str]:
    """Get group list items.

    Returns:
        The list of group list items.
    """

def get_subgroup_list_items() -> List[str]:
    """Get subgroup list items.

    Returns:
        The list of subgroup list items.
    """

def get_comment_list_items() -> List[str]:
    """Get comment list items.

    Returns:
        The list of comment list items.
    """

def get_sku_list_items() -> List[str]:
    """Get sku list items.

    Returns:
        The list of sku list items.
    """


def get_user_attribute_list_items(element_id: ElementId) -> List[str]:
    """Get user attribute list items.

    Parameters:
        element_id: The element id.

    Returns:
        The list of user attribute list items.
    """


def is_circular_mep(element_id: ElementId) -> bool:
    """Test if element is circular mep.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a circular mep, false otherwise.
    """


def is_rectangular_mep(element_id: ElementId) -> bool:
    """Test if element is rectangular mep.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a rectangular mep, false otherwise.
    """

def get_machine_calculation_state(element_id: ElementId) -> str:
    """Get machine calculation state.

    Parameters:
        element_id: The element id.

    Returns:
        The machine calculation state of the element.
    """


def get_machine_calculation_set_machine_type(element_id: ElementId) -> str:
    """Get machine calculation set machine type.

    Parameters:
        element_id: The element id.

    Returns:
        The machine calculation set machine type of the element.
    """

def is_btl_processing_group(element_id: ElementId) -> bool:
    """Test if element is btl processing group.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a btl processing group, false otherwise.
    """

def is_hundegger_processing_group(element_id: ElementId) -> bool:
    """Test if element is hundegger processing group.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is a hundegger processing group, false otherwise.
    """

def get_element_grouping_type() -> element_grouping_type:
    """Get the element grouping type (group, subgroup).

    Returns:
        The element grouping type.
    """

def set_element_grouping_type(element_grouping_type: element_grouping_type) -> None:
    """Set the element grouping type (group, subgroup).

    Parameters:
        element_grouping_type: The element grouping type to set.
    """

def get_associated_nesting_name(element_id: ElementId) -> str:
    """Get associated nesting name

    Parameters:
        element_id: The element id.

    Returns:
        The associated nesting name.
    """

def get_associated_nesting_number(element_id: ElementId) -> str:
    """Get associated nesting number.

    Parameters:
        element_id: The element id.

    Returns:
        The associated nesting number.
    """

def get_attribute_display_settings_for_2d() -> attribute_display_settings:
    """Get attribute display settings for 2d.

    Returns:
        The attribute display settings for 2d.
    """

def get_attribute_display_settings_for_2d_with_layout() -> attribute_display_settings:
    """Get attribute display settings for 2d with layout.

    Returns:
        The attribute display settings for 2d with layout.
    """

def get_attribute_display_settings_for_2d_without_layout() -> attribute_display_settings:
    """Get attribute display settings for 2d without layout.

    Returns:
        The attribute display settings for 2d without layout.
    """

def get_attribute_display_settings_for_3d() -> attribute_display_settings:
    """Get attribute display settings for 3d.

    Returns:
        The attribute display settings for 3d.
    """

def get_attribute_display_settings_for_container() -> attribute_display_settings:
    """Get attribute display settings for container.

    Returns:
        The attribute display settings for container.
    """

def get_attribute_display_settings_for_export_solid() -> attribute_display_settings:
    """Get attribute display settings for export solid.

    Returns:
        The attribute display settings for export solid.
    """

def get_attribute_display_settings_for_framed_wall_axis() -> attribute_display_settings:
    """Get attribute display settings for framed wall axis.

    Returns:
        The attribute display settings for framed wall axis.
    """

def get_attribute_display_settings_for_framed_wall_beam() -> attribute_display_settings:
    """Get attribute display settings for framed wall beam.

    Returns:
        The attribute display settings for framed wall beam.
    """

def get_attribute_display_settings_for_framed_wall_opening() -> attribute_display_settings:
    """Get attribute display settings for framed wall opening.

    Returns:
        The attribute display settings for framed wall opening.
    """

def get_attribute_display_settings_for_framed_wall_panel() -> attribute_display_settings:
    """Get attribute display settings for framed wall panel.

    Returns:
        The attribute display settings for framed wall panel.
    """

def get_attribute_display_settings_for_log_wall_axis() -> attribute_display_settings:
    """Get attribute display settings for log wall axis.

    Returns:
        The attribute display settings for log wall axis.
    """

def get_attribute_display_settings_for_log_wall_beam() -> attribute_display_settings:
    """Get attribute display settings for log wall beam.

    Returns:
        The attribute display settings for log wall beam.
    """

def get_attribute_display_settings_for_log_wall_opening() -> attribute_display_settings:
    """Get attribute display settings for log wall opening.

    Returns:
        The attribute display settings for log wall opening.
    """

def get_attribute_display_settings_for_log_wall_panel() -> attribute_display_settings:
    """Get attribute display settings for log wall panel.

    Returns:
        The attribute display settings for log wall panel.
    """

def get_attribute_display_settings_for_machine() -> attribute_display_settings:
    """Get attribute display settings for machine.

    Returns:
        The attribute display settings for machine.
    """

def get_attribute_display_settings_for_nesting_element() -> attribute_display_settings:
    """Get attribute display settings for nesting element.

    Returns:
        The attribute display settings for nesting element.
    """

def get_attribute_display_settings_for_nesting_volume() -> attribute_display_settings:
    """Get attribute display settings for nesting volume.

    Returns:
        The attribute display settings for nesting volume.
    """

def get_attribute_display_settings_for_solid_wall_axis() -> attribute_display_settings:
    """Get attribute display settings for solid wall axis.

    Returns:
        The attribute display settings for solid wall axis.
    """

def get_attribute_display_settings_for_solid_wall_beam() -> attribute_display_settings:
    """Get attribute display settings for solid wall beam.

    Returns:
        The attribute display settings for solid wall beam.
    """

def get_attribute_display_settings_for_solid_wall_opening() -> attribute_display_settings:
    """Get attribute display settings for solid wall opening.

    Returns:
        The attribute display settings for solid wall opening.
    """

def get_attribute_display_settings_for_solid_wall_panel() -> attribute_display_settings:
    """Get attribute display settings for solid wall panel.

    Returns:
        The attribute display settings for solid wall panel.
    """

def is_processing(element_id: ElementId) -> bool:
    """Tests if element is processing.

    Parameters:
        element_id: The element id.

    Returns:
        True if the element is processing, false otherwise.
    """

def delete_user_attribute(number: UserAttributeId) -> bool:
    """Delete user attribute from attribute list. The attribute is only deleted when the attribute is not used.

    Parameters:
        number: The attribute number.

    Returns:
        True if the attribute was successfully deleted, false otherwise.
    """

def is_attribute_visible_in_modify_window(number: UnsignedInt) -> bool:
    """Test if attribute is visible in modify window.

    Parameters:
        number: The attribute number.

    Returns:
        True if the attribute is visible in the modify window, false otherwise.
    """

def set_attribute_visibility_in_modify_window(number: UnsignedInt, visibility: bool) -> None:
    """Set attribute visibility in modify window.

    Parameters:
        number: The attribute number.
        visibility: The visibility state.
    """

def set_cutting_set(element_id_list: List[ElementId], cutting_set_name: str) -> bool:
    """Set cutting set.

    Parameters:
        element_id_list: The list of element ids.
        cutting_set_name: The name of the cutting set.

    Returns:
        True if the cutting set was successfully set, false otherwise.
    """

def get_standard_element_material_id(element_id: ElementId) -> int:
    """Get standard element material id.

    Parameters:
        element_id: The element id.

    Returns:
        The standard element material id.
    """