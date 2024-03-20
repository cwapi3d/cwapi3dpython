from typing import List
from cadwork import attribute_display_settings
from cadwork import element_grouping_type
from cadwork import element_type
from cadwork import extended_settings
from cadwork import process_type


def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """


def set_name(element_id_list: List[int], name: str) -> None:
    """Sets the element name

    Parameters:
        element_id_list: element_id_list
        name: name

    Returns:
        None
    """


def set_group(element_id_list: List[int], group: str) -> None:
    """Sets the element group

    Parameters:
        element_id_list: element_id_list
        group: group

    Returns:
        None
    """


def set_subgroup(element_id_list: List[int], subgroup: str) -> None:
    """Sets the element subgroup

    Parameters:
        element_id_list: element_id_list
        subgroup: subgroup

    Returns:
        None
    """


def set_comment(element_id_list: List[int], comment: str) -> None:
    """Sets the element comment

    Parameters:
        element_id_list: element_id_list
        comment: comment

    Returns:
        None
    """


def set_user_attribute(element_id_list: List[int], number: int, user_attribute: str) -> None:
    """Sets the element user attribute

    Parameters:
        element_id_list: element_id_list
        number: number
        user_attribute: user_attribute

    Returns:
        None
    """


def set_sku(element_id_list: List[int], sku: str) -> None:
    """Sets the element SKU

    Parameters:
        element_id_list: element_id_list
        sku: sku

    Returns:
        None
    """


def set_production_number(element_id_list: List[int], production_number: int) -> None:
    """Sets the element production number

    Parameters:
        element_id_list: element_id_list
        production_number: production_number

    Returns:
        None
    """


def set_part_number(element_id_list: List[int], part_number: int) -> None:
    """Sets the element part number

    Parameters:
        element_id_list: element_id_list
        part_number: part_number

    Returns:
        None
    """


def set_additional_data(element_id_list: List[int], data_id: str, data_text: str) -> None:
    """Sets the element additional data

    Parameters:
        element_id_list: element_id_list
        data_id: data_id
        data_text: data_text

    Returns:
        None
    """


def delete_additional_data(element_id_list: List[int], data_id: str) -> None:
    """Deletes the element additional data

    Parameters:
        element_id_list: element_id_list
        data_id: data_id

    Returns:
        None
    """


def set_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Sets the user attribute name

    Parameters:
        number: number
        user_attribute_name: user_attribute_name

    Returns:
        None
    """


def set_process_type_and_extended_settings_from_name(element_id_list: List[int]) -> None:
    """Sets the element process type and extended settings from the element name

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_name_process_type(name: str, process_type: None) -> None:
    """Sets the process type for an element name

    Parameters:
        name: name
        process_type: process_type

    Returns:
        None
    """


def set_name_extended_settings(name: str, extended_settings: None) -> None:
    """Sets the extended settings for an element name

    Parameters:
        name: name
        extended_settings: extended_settings

    Returns:
        None
    """


def set_output_type(element_id_list: List[int], process_type: None) -> None:
    """Sets the element output type

    Parameters:
        element_id_list: element_id_list
        process_type: process_type

    Returns:
        None
    """


def set_extended_settings(element_id_list: List[int], extended_settings: None) -> None:
    """Sets the element extended settings

    Parameters:
        element_id_list: element_id_list
        extended_settings: extended_settings

    Returns:
        None
    """


def set_wall(a0: List[int]) -> None:
    """set wall

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_floor(a0: List[int]) -> None:
    """set floor

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_opening(element_id_list: List[int]) -> None:
    """Sets the element to opening

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_fastening_attribute(element_id_list: List[int], value: str) -> None:
    """Sets the element fastening attribute

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """


def set_element_material(element_id_list: List[int], material: int) -> None:
    """Sets the element material

    Parameters:
        element_id_list: element_id_list
        material: material

    Returns:
        None
    """


def set_assembly_number(element_id_list: List[int], assembly_number: str) -> None:
    """set assembly number

    Parameters:
        element_id_list: element_id_list
        assembly_number: assembly_number

    Returns:
        None
    """


def set_list_quantity(element_id_list: List[int], list_quantity: int) -> None:
    """set list quantity

    Parameters:
        element_id_list: element_id_list
        list_quantity: list_quantity

    Returns:
        None
    """


def set_layer_settings(element_id_list: List[int], layer_settings: None) -> None:
    """set layer settings

    Parameters:
        element_id_list: element_id_list
        layer_settings: layer_settings

    Returns:
        None
    """


def set_ignore_in_vba_calculation(elements: List[int], ignore: bool) -> None:
    """Sets if the element should be ignored in VBA Calculation

    Parameters:
        elements: elements
        ignore: ignore

    Returns:
        None
    """


def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """


def set_reference_wall_2dc(elements: List[int], _2dc_file_path: str) -> None:
    """Applies a new 2dc reference wall to an element

    Parameters:
        elements: elements
        _2dc_file_path: _2dc_file_path

    Returns:
        None
    """


def get_user_attribute_count() -> int:
    """get user attribute count

    Returns:
        int
    """


def set_standard_part(elements: List[int]) -> None:
    """Sets covers (wall,opening or floor) to standard part.

    Parameters:
        elements: elements

    Returns:
        None
    """


def set_solid_wall(elements: List[int]) -> None:
    """Sets elements to solid wall.

    Parameters:
        elements: elements

    Returns:
        None
    """


def set_log_wall(elements: List[int]) -> None:
    """Sets elements to log wall.

    Parameters:
        elements: elements

    Returns:
        None
    """


def set_solid_floor(elements: List[int]) -> None:
    """Sets elements to solid floor.

    Parameters:
        elements: elements

    Returns:
        None
    """


def set_roof(a0: List[int]) -> None:
    """set roof

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_solid_roof(elements: List[int]) -> None:
    """Sets elements to solid roof cover.

    Parameters:
        elements: elements

    Returns:
        None
    """


def get_node_symbol(element: int) -> int:
    """get node symbol

    Parameters:
        element: element

    Returns:
        int
    """


def set_node_symbol(elements: List[int], symbol: int) -> None:
    """set node symbol

    Parameters:
        elements: elements
        symbol: symbol

    Returns:
        None
    """


def enable_attribute_display() -> None:
    """enable attribute display

    Returns:
        None
    """


def disable_attribute_display() -> None:
    """disable attribute display

    Returns:
        None
    """


def is_attribute_display_enabled() -> bool:
    """is attribute display enabled

    Returns:
        bool
    """


def update_auto_attribute() -> None:
    """update auto attribute

    Returns:
        None
    """


def set_additional_guid(a0: List[int], a1: str, a2: str) -> None:
    """set additional guid

    Parameters:
        a0: a0
        a1: a1
        a2: a2

    Returns:
        None
    """


def add_item_to_group_list(a0: str) -> None:
    """add item to group list

    Parameters:
        a0: a0

    Returns:
        None
    """


def add_item_to_subgroup_list(a0: str) -> None:
    """add item to subgroup list

    Parameters:
        a0: a0

    Returns:
        None
    """


def add_item_to_comment_list(a0: str) -> None:
    """add item to comment list

    Parameters:
        a0: a0

    Returns:
        None
    """


def add_item_to_sku_list(a0: str) -> None:
    """add item to sku list

    Parameters:
        a0: a0

    Returns:
        None
    """


def add_item_to_user_attribute_list(a0: int, a1: str) -> None:
    """add item to user attribute list

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """


def set_container_number(a0: List[int], a1: int) -> None:
    """set container number

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """


def get_name_list_items() -> List[str]:
    """get name list items

    Returns:
        List[str]
    """


def add_item_to_name_list(a0: str) -> None:
    """add item to name list

    Parameters:
        a0: a0

    Returns:
        None
    """


def delete_item_from_comment_list(a0: str) -> bool:
    """delete item from comment list

    Parameters:
        a0: a0

    Returns:
        bool
    """


def delete_item_from_group_list(a0: str) -> bool:
    """delete item from group list

    Parameters:
        a0: a0

    Returns:
        bool
    """


def delete_item_from_sku_list(a0: str) -> bool:
    """delete item from sku list

    Parameters:
        a0: a0

    Returns:
        bool
    """


def delete_item_from_subgroup_list(a0: str) -> bool:
    """delete item from subgroup list

    Parameters:
        a0: a0

    Returns:
        bool
    """


def delete_item_from_user_attribute_list(a0: int, a1: str) -> bool:
    """delete item from user attribute list

    Parameters:
        a0: a0
        a1: a1

    Returns:
        bool
    """


def set_attribute_display_settings_for_2d(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_2d_with_layout(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d with layout

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_2d_without_layout(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d without layout

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_3d(a0: attribute_display_settings) -> None:
    """set attribute display settings for 3d

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_container(a0: attribute_display_settings) -> None:
    """set attribute display settings for container

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_export_solid(a0: attribute_display_settings) -> None:
    """set attribute display settings for export solid

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall axis

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall beam

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall opening

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall panel

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall axis

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall beam

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall opening

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall panel

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_machine(a0: attribute_display_settings) -> None:
    """set attribute display settings for machine

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_nesting_element(a0: attribute_display_settings) -> None:
    """set attribute display settings for nesting element

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_nesting_volume(a0: attribute_display_settings) -> None:
    """set attribute display settings for nesting volume

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall axis

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall beam

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall opening

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall panel

    Parameters:
        a0: a0

    Returns:
        None
    """


def set_framed_floor(element_id_list: List[int]) -> None:
    """Sets the elements to framed floor

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_framed_roof(element_id_list: List[int]) -> None:
    """Sets the elements to framed roof

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def set_framed_wall(element_id_list: List[int]) -> None:
    """Sets the element to framed wall

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """


def get_name_list_items_by_element_type(a0: element_type) -> List[str]:
    """get name list items by element type

    Parameters:
        a0: a0

    Returns:
        List[str]
    """


def get_name(element_id: int) -> str:
    """Gets the element name

    Parameters:
        element_id: element_id

    Returns:
        element name
    """


def get_group(element_id: int) -> str:
    """Gets the element group

    Parameters:
        element_id: element_id

    Returns:
        element group
    """


def get_subgroup(element_id: int) -> str:
    """Gets the element subgroup

    Parameters:
        element_id: element_id

    Returns:
        element subgroup
    """


def get_comment(element_id: int) -> str:
    """Gets the element comment

    Parameters:
        element_id: element_id

    Returns:
        element comment
    """


def get_user_attribute(element_id: int, number: int) -> str:
    """Gets the element user attribute

    Parameters:
        element_id: element_id
        number: number

    Returns:
        element user attribute
    """


def get_sku(element_id: int) -> str:
    """Gets the element SKU

    Parameters:
        element_id: element_id

    Returns:
        element SKU
    """


def get_production_number(element_id: int) -> int:
    """Gets the element production number

    Parameters:
        element_id: element_id

    Returns:
        element production number
    """


def get_part_number(element_id: int) -> int:
    """Gets the element part number

    Parameters:
        element_id: element_id

    Returns:
        element part number
    """


def get_additional_data(element_id: int, data_id: str) -> str:
    """Gets the element additional data

    Parameters:
        element_id: element_id
        data_id: data_id

    Returns:
        element additional data
    """


def get_user_attribute_name(number: int) -> str:
    """Gets the user attribute name

    Parameters:
        number: number

    Returns:
        user attribute name
    """


def get_wall_situation(element_id: int) -> str:
    """Gets the element wall situation

    Parameters:
        element_id: element_id

    Returns:
        element wall situation
    """


def get_element_material_name(element_id: int) -> str:
    """Gets the element material name

    Parameters:
        element_id: element_id

    Returns:
        element material name
    """


def get_prefab_layer(element_id: int) -> str:
    """Gets the element prefab layer

    Parameters:
        element_id: element_id

    Returns:
        element prefab layer
    """


def get_machine_calculation_set(element_id: int) -> str:
    """Gets the element machine calculation set

    Parameters:
        element_id: element_id

    Returns:
        element machine calculation set
    """


def get_cutting_set(element_id: int) -> str:
    """Gets the element cutting set

    Parameters:
        element_id: element_id

    Returns:
        element cutting set
    """


def get_name_process_type(name: str) -> process_type:
    """Gets the process type for an element name

    Parameters:
        name: name

    Returns:
        process type
    """


def get_name_extended_settings(name: str) -> extended_settings:
    """Gets the extended settings for an element name

    Parameters:
        name: name

    Returns:
        extended settings
    """


def get_output_type(element_id: int) -> process_type:
    """Gets the element output type

    Parameters:
        element_id: element_id

    Returns:
        element output type
    """


def get_extended_settings(element_id: int) -> extended_settings:
    """Gets the element extended settings

    Parameters:
        element_id: element_id

    Returns:
        element extended settings
    """


def get_element_type(element_id: int) -> element_type:
    """Gets the element type

    Parameters:
        element_id: element_id

    Returns:
        element type
    """


def get_fastening_attribute(element_id: int) -> str:
    """Get the element fastening attribute

    Parameters:
        element_id: element_id

    Returns:
        element fastening attribute
    """


def get_assembly_number(element_id: int) -> str:
    """get assembly number

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def get_list_quantity(element_id: int) -> int:
    """get list quantity

    Parameters:
        element_id: element_id

    Returns:
        int
    """


def get_ignore_in_vba_calculation(element: int) -> bool:
    """get ignore in vba calculation

    Parameters:
        element: element

    Returns:
        bool
    """


def get_standard_element_name(element_id: int) -> str:
    """get standard element name

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def get_steel_shape_name(element_id: int) -> str:
    """get steel shape name

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def is_beam(element_id: int) -> bool:
    """Tests if element is beam

    Parameters:
        element_id: element_id

    Returns:
        is element beam
    """


def is_panel(element_id: int) -> bool:
    """Tests if element is panel

    Parameters:
        element_id: element_id

    Returns:
        is element panel
    """


def is_opening(element_id: int) -> bool:
    """Tests if element is opening

    Parameters:
        element_id: element_id

    Returns:
        is element opening
    """


def is_wall(element_id: int) -> bool:
    """Tests if element is wall

    Parameters:
        element_id: element_id

    Returns:
        is element wall
    """


def is_floor(element_id: int) -> bool:
    """Tests if element is floor

    Parameters:
        element_id: element_id

    Returns:
        is element floor
    """


def is_roof(element_id: int) -> bool:
    """Tests if element is roof

    Parameters:
        element_id: element_id

    Returns:
        is element roof
    """


def is_metal(element_id: int) -> bool:
    """Tests if element is metal

    Parameters:
        element_id: element_id

    Returns:
        is element metal
    """


def is_export_solid(element_id: int) -> bool:
    """Tests if element is export solid

    Parameters:
        element_id: element_id

    Returns:
        is element export solid
    """


def is_container(element_id: int) -> bool:
    """Tests if element is container

    Parameters:
        element_id: element_id

    Returns:
        is element container
    """


def is_connector_axis(element_id: int) -> bool:
    """Tests if element is connector axis

    Parameters:
        element_id: element_id

    Returns:
        is element connector axis
    """


def is_drilling(element_id: int) -> bool:
    """Tests if element is drilling

    Parameters:
        element_id: element_id

    Returns:
        is element drilling
    """


def is_node(element_id: int) -> bool:
    """Tests if element is node

    Parameters:
        element_id: element_id

    Returns:
        is element node
    """


def is_auxiliary(element_id: int) -> bool:
    """Tests if element is auxiliary

    Parameters:
        element_id: element_id

    Returns:
        is element auxiliary
    """


def is_roof_surface(element_id: int) -> bool:
    """Tests if the element is roof surface

    Parameters:
        element_id: element_id

    Returns:
        is element roof surface
    """


def is_caddy_object(element_id: int) -> bool:
    """Tests if the element is caddy object

    Parameters:
        element_id: element_id

    Returns:
        is element caddy object
    """


def is_envelope(element_id: int) -> bool:
    """is envelope

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_architecture_wall_2dc(element: int) -> bool:
    """Tests if the element has a 2dc reference wall

    Parameters:
        element: element

    Returns:
        is architecturewall 2dc
    """


def is_architecture_wall_xml(element: int) -> bool:
    """Tests if the element has a xml reference wall

    Parameters:
        element: element

    Returns:
        is architecturewall xml
    """


def is_surface(element_id: int) -> bool:
    """Tests if the element is a Surface

    Parameters:
        element_id: element_id

    Returns:
        is Surface
    """


def is_line(element_id: int) -> bool:
    """Tests if the element is a Line

    Parameters:
        element_id: element_id

    Returns:
        is Line
    """


def get_auto_attribute(element_id: int, number: int) -> str:
    """get auto attribute

    Parameters:
        element_id: element_id
        number: number

    Returns:
        str
    """


def get_auto_attribute_name(number: int) -> str:
    """get auto attribute name

    Parameters:
        number: number

    Returns:
        str
    """


def is_framed_wall(element_id: int) -> bool:
    """is framed wall

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_solid_wall(element_id: int) -> bool:
    """is solid wall

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_log_wall(element_id: int) -> bool:
    """is log wall

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_framed_floor(element_id: int) -> bool:
    """is framed floor

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_solid_floor(element_id: int) -> bool:
    """is solid floor

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_framed_roof(element_id: int) -> bool:
    """is framed roof

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def is_solid_roof(element_id: int) -> bool:
    """is solid roof

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def get_additional_guid(a0: int, a1: str) -> str:
    """get additional guid

    Parameters:
        a0: a0
        a1: a1

    Returns:
        str
    """


def get_prefab_layer_all_assigned(a0: int) -> List[int]:
    """get prefab layer all assigned

    Parameters:
        a0: a0

    Returns:
        List[int]
    """


def get_prefab_layer_with_dimensions(a0: int) -> List[int]:
    """get prefab layer with dimensions

    Parameters:
        a0: a0

    Returns:
        List[int]
    """


def get_prefab_layer_without_dimensions(a0: int) -> List[int]:
    """get prefab layer without dimensions

    Parameters:
        a0: a0

    Returns:
        List[int]
    """


def is_nesting_parent(a0: int) -> bool:
    """is nesting parent

    Parameters:
        a0: a0

    Returns:
        bool
    """


def is_nesting_raw_part(a0: int) -> bool:
    """is nesting raw part

    Parameters:
        a0: a0

    Returns:
        bool
    """


def get_container_number(a0: int) -> int:
    """get container number

    Parameters:
        a0: a0

    Returns:
        int
    """


def get_container_number_with_prefix(a0: int) -> str:
    """get container number with prefix

    Parameters:
        a0: a0

    Returns:
        str
    """


def get_group_list_items() -> List[str]:
    """get group list items

    Returns:
        List[str]
    """


def get_subgroup_list_items() -> List[str]:
    """get subgroup list items

    Returns:
        List[str]
    """


def get_comment_list_items() -> List[str]:
    """get comment list items

    Returns:
        List[str]
    """


def get_sku_list_items() -> List[str]:
    """get sku list items

    Returns:
        List[str]
    """


def get_user_attribute_list_items(a0: int) -> List[str]:
    """get user attribute list items

    Parameters:
        a0: a0

    Returns:
        List[str]
    """


def is_circular_mep(a0: int) -> bool:
    """is circular mep

    Parameters:
        a0: a0

    Returns:
        bool
    """


def is_rectangular_mep(a0: int) -> bool:
    """is rectangular mep

    Parameters:
        a0: a0

    Returns:
        bool
    """


def get_machine_calculation_state(a0: int) -> str:
    """get machine calculation state

    Parameters:
        a0: a0

    Returns:
        str
    """


def get_machine_calculation_set_machine_type(a0: int) -> str:
    """get machine calculation set machine type

    Parameters:
        a0: a0

    Returns:
        str
    """


def is_btl_processing_group(a0: int) -> bool:
    """is btl processing group

    Parameters:
        a0: a0

    Returns:
        bool
    """


def is_hundegger_processing_group(a0: int) -> bool:
    """is hundegger processing group

    Parameters:
        a0: a0

    Returns:
        bool
    """


def get_element_grouping_type() -> element_grouping_type:
    """Get the element grouping type (group, subgroup)

    Returns:
        element grouping type
    """


def set_element_grouping_type(element_grouping_type: element_grouping_type) -> None:
    """Set the element grouping type (group, subgroup)

    Parameters:
        element_grouping_type: element_grouping_type

    Returns:
        None
    """


def get_associated_nesting_name(element_id: int) -> str:
    """get associated nesting name

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def get_associated_nesting_number(element_id: int) -> str:
    """get associated nesting number

    Parameters:
        element_id: element_id

    Returns:
        str
    """


def get_attribute_display_settings_for_2d() -> attribute_display_settings:
    """get attribute display settings for 2d

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_2d_with_layout() -> attribute_display_settings:
    """get attribute display settings for 2d with layout

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_2d_without_layout() -> attribute_display_settings:
    """get attribute display settings for 2d without layout

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_3d() -> attribute_display_settings:
    """get attribute display settings for 3d

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_container() -> attribute_display_settings:
    """get attribute display settings for container

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_export_solid() -> attribute_display_settings:
    """get attribute display settings for export solid

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_axis() -> attribute_display_settings:
    """get attribute display settings for framed wall axis

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_beam() -> attribute_display_settings:
    """get attribute display settings for framed wall beam

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_opening() -> attribute_display_settings:
    """get attribute display settings for framed wall opening

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_panel() -> attribute_display_settings:
    """get attribute display settings for framed wall panel

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_axis() -> attribute_display_settings:
    """get attribute display settings for log wall axis

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_beam() -> attribute_display_settings:
    """get attribute display settings for log wall beam

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_opening() -> attribute_display_settings:
    """get attribute display settings for log wall opening

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_panel() -> attribute_display_settings:
    """get attribute display settings for log wall panel

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_machine() -> attribute_display_settings:
    """get attribute display settings for machine

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_nesting_element() -> attribute_display_settings:
    """get attribute display settings for nesting element

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_nesting_volume() -> attribute_display_settings:
    """get attribute display settings for nesting volume

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_axis() -> attribute_display_settings:
    """get attribute display settings for solid wall axis

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_beam() -> attribute_display_settings:
    """get attribute display settings for solid wall beam

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_opening() -> attribute_display_settings:
    """get attribute display settings for solid wall opening

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_panel() -> attribute_display_settings:
    """get attribute display settings for solid wall panel

    Returns:
        attribute_display_settings
    """


def is_processing(element_id: int) -> bool:
    """is processing

    Parameters:
        element_id: element_id

    Returns:
        bool
    """


def delete_user_attribute(number: int) -> bool:
    """Delete user attribute from attribute list. The attribute is only deleted when the attribute is not used.

    Parameters:
        number: number

    Returns:
        bool deletion successfully
    """
