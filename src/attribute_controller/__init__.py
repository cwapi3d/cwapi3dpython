from typing import List
from cadwork import attribute_display_settings
from cadwork import element_grouping_type
from cadwork import element_type
from cadwork import extended_settings
from cadwork import process_type


def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        strerror string
    """


def set_name(element_id_list: List[int], name: str) -> None:
    """set name
    Args:
        element_id_list ( List[int]): element_id_list
        name ( str): name

    Returns:
        None
    """


def set_group(element_id_list: List[int], group: str) -> None:
    """set group
    Args:
        element_id_list ( List[int]): element_id_list
        group ( str): group

    Returns:
        None
    """


def set_subgroup(element_id_list: List[int], subgroup: str) -> None:
    """set subgroup
    Args:
        element_id_list ( List[int]): element_id_list
        subgroup ( str): subgroup

    Returns:
        None
    """


def set_comment(element_id_list: List[int], comment: str) -> None:
    """set comment
    Args:
        element_id_list ( List[int]): element_id_list
        comment ( str): comment

    Returns:
        None
    """


def set_user_attribute(element_id_list: List[int], number: int, user_attribute: str) -> None:
    """set user attribute
    Args:
        element_id_list ( List[int]): element_id_list
        number ( int): number
        user_attribute ( str): user_attribute

    Returns:
        None
    """


def set_sku(element_id_list: List[int], sku: str) -> None:
    """set sku
    Args:
        element_id_list ( List[int]): element_id_list
        sku ( str): sku

    Returns:
        None
    """


def set_production_number(element_id_list: List[int], production_number: int) -> None:
    """set production number
    Args:
        element_id_list ( List[int]): element_id_list
        production_number ( int): production_number

    Returns:
        None
    """


def set_part_number(element_id_list: List[int], part_number: int) -> None:
    """set part number
    Args:
        element_id_list ( List[int]): element_id_list
        part_number ( int): part_number

    Returns:
        None
    """


def set_additional_data(element_id_list: List[int], data_id: str, data_text: str) -> None:
    """set additional data
    Args:
        element_id_list ( List[int]): element_id_list
        data_id ( str): data_id
        data_text ( str): data_text

    Returns:
        None
    """


def delete_additional_data(element_id_list: List[int], data_id: str) -> None:
    """delete additional data
    Args:
        element_id_list ( List[int]): element_id_list
        data_id ( str): data_id

    Returns:
        None
    """


def set_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """set user attribute name
    Args:
        number ( int): number
        user_attribute_name ( str): user_attribute_name

    Returns:
        None
    """


def set_process_type_and_extended_settings_from_name(element_id_list: List[int]) -> None:
    """set process type and extended settings from name
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_name_process_type(name: str, process_type: None) -> None:
    """set name process type
    Args:
        name ( str): name
        process_type ( None): process_type

    Returns:
        None
    """


def set_name_extended_settings(name: str, extended_settings: None) -> None:
    """set name extended settings
    Args:
        name ( str): name
        extended_settings ( None): extended_settings

    Returns:
        None
    """


def set_output_type(element_id_list: List[int], process_type: None) -> None:
    """set output type
    Args:
        element_id_list ( List[int]): element_id_list
        process_type ( None): process_type

    Returns:
        None
    """


def set_extended_settings(element_id_list: List[int], extended_settings: None) -> None:
    """set extended settings
    Args:
        element_id_list ( List[int]): element_id_list
        extended_settings ( None): extended_settings

    Returns:
        None
    """


def set_wall(element_id_list: List[int]) -> None:
    """set wall
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_floor(element_id_list: List[int]) -> None:
    """set floor
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_opening(element_id_list: List[int]) -> None:
    """set opening
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """


def set_fastening_attribute(element_id_list: List[int], value: str) -> None:
    """set fastening attribute
    Args:
        element_id_list ( List[int]): element_id_list
        value ( str): value

    Returns:
        None
    """


def set_element_material(element_id_list: List[int], material: int) -> None:
    """set element material
    Args:
        element_id_list ( List[int]): element_id_list
        material ( int): material

    Returns:
        None
    """


def set_assembly_number(element_id_list: List[int], assembly_number: str) -> None:
    """set assembly number
    Args:
        element_id_list ( List[int]): element_id_list
        assembly_number ( str): assembly_number

    Returns:
        None
    """


def set_list_quantity(element_id_list: List[int], list_quantity: int) -> None:
    """set list quantity
    Args:
        element_id_list ( List[int]): element_id_list
        list_quantity ( int): list_quantity

    Returns:
        None
    """


def set_layer_settings(element_id_list: List[int], layer_settings: None) -> None:
    """set layer settings
    Args:
        element_id_list ( List[int]): element_id_list
        layer_settings ( None): layer_settings

    Returns:
        None
    """


def set_ignore_in_vba_calculation(elements: List[int], ignore: bool) -> None:
    """set ignore in vba calculation
    Args:
        elements ( List[int]): elements
        ignore ( bool): ignore

    Returns:
        None
    """


def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """


def set_reference_wall_2dc(elements: List[int], a2dc_file_path: str) -> None:
    """set reference wall 2dc
    Args:
        elements ( List[int]): elements
        2dc_file_path ( str): 2dc_file_path

    Returns:
        None
    """


def get_user_attribute_count() -> int:
    """get user attribute count
    Args:

    Returns:
        int
    """


def set_standard_part(elements: List[int]) -> None:
    """set standard part
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def set_solid_wall(elements: List[int]) -> None:
    """set solid wall
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def set_log_wall(elements: List[int]) -> None:
    """set log wall
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def set_solid_floor(elements: List[int]) -> None:
    """set solid floor
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def set_roof(elements: List[int]) -> None:
    """set roof
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def set_solid_roof(elements: List[int]) -> None:
    """set solid roof
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """


def get_node_symbol(element: None) -> int:
    """get node symbol
    Args:
        element ( None): element

    Returns:
        int
    """


def set_node_symbol(elements: List[int], symbol: int) -> None:
    """set node symbol
    Args:
        elements ( List[int]): elements
        symbol ( int): symbol

    Returns:
        None
    """


def enable_attribute_display() -> None:
    """enable attribute display
    Args:

    Returns:
        None
    """


def disable_attribute_display() -> None:
    """disable attribute display
    Args:

    Returns:
        None
    """


def is_attribute_display_enabled() -> bool:
    """is attribute display enabled
    Args:

    Returns:
        bool
    """


def update_auto_attribute() -> None:
    """update auto attribute
    Args:

    Returns:
        None
    """


def set_additional_guid(a0: List[int], a1: str, a2: str) -> None:
    """set additional guid
    Args:
        a0 ( List[int]): a0
        a1 ( str): a1
        a2 ( str): a2

    Returns:
        None
    """


def add_item_to_group_list(a0: str) -> None:
    """add item to group list
    Args:
        a0 ( str): a0

    Returns:
        None
    """


def add_item_to_subgroup_list(a0: str) -> None:
    """add item to subgroup list
    Args:
        a0 ( str): a0

    Returns:
        None
    """


def add_item_to_comment_list(a0: str) -> None:
    """add item to comment list
    Args:
        a0 ( str): a0

    Returns:
        None
    """


def add_item_to_sku_list(a0: str) -> None:
    """add item to sku list
    Args:
        a0 ( str): a0

    Returns:
        None
    """


def add_item_to_user_attribute_list(a0: int, a1: str) -> None:
    """add item to user attribute list
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        None
    """


def set_container_number(a0: List[int], a1: int) -> None:
    """set container number
    Args:
        a0 ( List[int]): a0
        a1 ( int): a1

    Returns:
        None
    """


def get_name_list_items() -> List[str]:
    """get name list items
    Args:

    Returns:
        List[str]
    """


def add_item_to_name_list(a0: str) -> None:
    """add item to name list
    Args:
        a0 ( str): a0

    Returns:
        None
    """


def delete_item_from_comment_list(a0: str) -> bool:
    """delete item from comment list
    Args:
        a0 ( str): a0

    Returns:
        bool
    """


def delete_item_from_group_list(a0: str) -> bool:
    """delete item from group list
    Args:
        a0 ( str): a0

    Returns:
        bool
    """


def delete_item_from_sku_list(a0: str) -> bool:
    """delete item from sku list
    Args:
        a0 ( str): a0

    Returns:
        bool
    """


def delete_item_from_subgroup_list(a0: str) -> bool:
    """delete item from subgroup list
    Args:
        a0 ( str): a0

    Returns:
        bool
    """


def delete_item_from_user_attribute_list(a0: int, a1: str) -> bool:
    """delete item from user attribute list
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        bool
    """


def set_attribute_display_settings_for_2d(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_2d_with_layout(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d with layout
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_2d_without_layout(a0: attribute_display_settings) -> None:
    """set attribute display settings for 2d without layout
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_3d(a0: attribute_display_settings) -> None:
    """set attribute display settings for 3d
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_container(a0: attribute_display_settings) -> None:
    """set attribute display settings for container
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_export_solid(a0: attribute_display_settings) -> None:
    """set attribute display settings for export solid
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall axis
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall beam
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall opening
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_framed_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for framed wall panel
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall axis
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall beam
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall opening
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_log_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for log wall panel
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_machine(a0: attribute_display_settings) -> None:
    """set attribute display settings for machine
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_nesting_element(a0: attribute_display_settings) -> None:
    """set attribute display settings for nesting element
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_nesting_volume(a0: attribute_display_settings) -> None:
    """set attribute display settings for nesting volume
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_axis(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall axis
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_beam(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall beam
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_opening(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall opening
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def set_attribute_display_settings_for_solid_wall_panel(a0: attribute_display_settings) -> None:
    """set attribute display settings for solid wall panel
    Args:
        a0 ( attribute_display_settings): a0

    Returns:
        None
    """


def get_name(id: int) -> str:
    """get name
    Args:
        id ( int): id

    Returns:
        strelement name
    """


def get_group(id: int) -> str:
    """get group
    Args:
        id ( int): id

    Returns:
        strelement group
    """


def get_subgroup(id: int) -> str:
    """get subgroup
    Args:
        id ( int): id

    Returns:
        strelement subgroup
    """


def get_subgroup(id: int) -> str:
    """get subgroup
    Args:
        id ( int): id

    Returns:
        strelement subgroup
    """


def get_comment(id: int) -> str:
    """get comment
    Args:
        id ( int): id

    Returns:
        strelement comment
    """


def get_user_attribute(id: int, number: int) -> str:
    """get user attribute
    Args:
        id ( int): id
        number ( int): number

    Returns:
        strelement user attribute
    """


def get_sku(id: int) -> str:
    """get sku
    Args:
        id ( int): id

    Returns:
        strelement SKU
    """


def get_production_number(id: int) -> int:
    """get production number
    Args:
        id ( int): id

    Returns:
        intelement production number
    """


def get_part_number(id: int) -> int:
    """get part number
    Args:
        id ( int): id

    Returns:
        intelement part number
    """


def get_additional_data(id: int, data_id: str) -> str:
    """get additional data
    Args:
        id ( int): id
        data_id ( str): data_id

    Returns:
        strelement additional data
    """


def get_user_attribute_name(number: int) -> str:
    """get user attribute name
    Args:
        number ( int): number

    Returns:
        struser attribute name
    """


def get_wall_situation(id: int) -> str:
    """get wall situation
    Args:
        id ( int): id

    Returns:
        strelement wall situation
    """


def get_element_material_name(id: int) -> str:
    """get element material name
    Args:
        id ( int): id

    Returns:
        strelement material name
    """


def get_prefab_layer(id: int) -> str:
    """get prefab layer
    Args:
        id ( int): id

    Returns:
        strelement prefab layer
    """


def get_machine_calculation_set(id: int) -> str:
    """get machine calculation set
    Args:
        id ( int): id

    Returns:
        strelement machine calculation set
    """


def get_cutting_set(id: int) -> str:
    """get cutting set
    Args:
        id ( int): id

    Returns:
        strelement cutting set
    """


def get_name_process_type(name: str) -> process_type:
    """get name process type
    Args:
        name ( str): name

    Returns:
        process_typeprocess type
    """


def get_name_extended_settings(name: str) -> extended_settings:
    """get name extended settings
    Args:
        name ( str): name

    Returns:
        extended_settingsextended settings
    """


def get_output_type(id: int) -> process_type:
    """get output type
    Args:
        id ( int): id

    Returns:
        process_typeelement output type
    """


def get_extended_settings(id: int) -> extended_settings:
    """get extended settings
    Args:
        id ( int): id

    Returns:
        extended_settingselement extended settings
    """


def get_element_type(id: int) -> element_type:
    """get element type
    Args:
        id ( int): id

    Returns:
        element_typeelement type
    """


def get_fastening_attribute(id: int) -> str:
    """get fastening attribute
    Args:
        id ( int): id

    Returns:
        strelement fastening attribute
    """


def get_assembly_number(id: int) -> str:
    """get assembly number
    Args:
        id ( int): id

    Returns:
        str
    """


def get_list_quantity(id: int) -> int:
    """get list quantity
    Args:
        id ( int): id

    Returns:
        int
    """


def get_ignore_in_vba_calculation(element: int) -> bool:
    """get ignore in vba calculation
    Args:
        element ( int): element

    Returns:
        bool
    """


def get_standard_element_name(id: None) -> str:
    """get standard element name
    Args:
        id ( None): id

    Returns:
        str
    """


def get_steel_shape_name(id: None) -> str:
    """get steel shape name
    Args:
        id ( None): id

    Returns:
        str
    """


def is_beam(id: int) -> bool:
    """is beam
    Args:
        id ( int): id

    Returns:
        boolis element beam
    """


def is_panel(id: int) -> bool:
    """is panel
    Args:
        id ( int): id

    Returns:
        boolis element panel
    """


def is_opening(id: int) -> bool:
    """is opening
    Args:
        id ( int): id

    Returns:
        boolis element opening
    """


def is_wall(id: int) -> bool:
    """is wall
    Args:
        id ( int): id

    Returns:
        boolis element wall
    """


def is_floor(id: int) -> bool:
    """is floor
    Args:
        id ( int): id

    Returns:
        boolis element floor
    """


def is_roof(id: int) -> bool:
    """is roof
    Args:
        id ( int): id

    Returns:
        boolis element roof
    """


def is_metal(id: int) -> bool:
    """is metal
    Args:
        id ( int): id

    Returns:
        boolis element metal
    """


def is_export_solid(id: int) -> bool:
    """is export solid
    Args:
        id ( int): id

    Returns:
        boolis element export solid
    """


def is_container(id: int) -> bool:
    """is container
    Args:
        id ( int): id

    Returns:
        boolis element container
    """


def is_connector_axis(id: int) -> bool:
    """is connector axis
    Args:
        id ( int): id

    Returns:
        boolis element connector axis
    """


def is_drilling(id: int) -> bool:
    """is drilling
    Args:
        id ( int): id

    Returns:
        boolis element drilling
    """


def is_node(id: int) -> bool:
    """is node
    Args:
        id ( int): id

    Returns:
        boolis element node
    """


def is_auxiliary(id: int) -> bool:
    """is auxiliary
    Args:
        id ( int): id

    Returns:
        boolis element auxiliary
    """


def is_roof_surface(id: int) -> bool:
    """is roof surface
    Args:
        id ( int): id

    Returns:
        boolis element roof surface
    """


def is_caddy_object(id: int) -> bool:
    """is caddy object
    Args:
        id ( int): id

    Returns:
        boolis element caddy object
    """


def is_envelope(id: int) -> bool:
    """is envelope
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_architecture_wall_2dc(element: None) -> bool:
    """is architecture wall 2dc
    Args:
        element ( None): element

    Returns:
        boolis architecturewall 2dc
    """


def is_architecture_wall_xml(element: None) -> bool:
    """is architecture wall xml
    Args:
        element ( None): element

    Returns:
        boolis architecturewall xml
    """


def is_surface(id: None) -> bool:
    """is surface
    Args:
        id ( None): id

    Returns:
        boolis Surface
    """


def is_line(id: None) -> bool:
    """is line
    Args:
        id ( None): id

    Returns:
        boolis Line
    """


def get_auto_attribute(id: int, number: int) -> str:
    """get auto attribute
    Args:
        id ( int): id
        number ( int): number

    Returns:
        str
    """


def get_auto_attribute_name(number: int) -> str:
    """get auto attribute name
    Args:
        number ( int): number

    Returns:
        str
    """


def is_framed_wall(id: int) -> bool:
    """is framed wall
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_solid_wall(id: int) -> bool:
    """is solid wall
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_log_wall(id: int) -> bool:
    """is log wall
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_framed_floor(id: int) -> bool:
    """is framed floor
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_solid_floor(id: int) -> bool:
    """is solid floor
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_framed_roof(id: int) -> bool:
    """is framed roof
    Args:
        id ( int): id

    Returns:
        bool
    """


def is_solid_roof(id: int) -> bool:
    """is solid roof
    Args:
        id ( int): id

    Returns:
        bool
    """


def get_additional_guid(a0: int, a1: str) -> str:
    """get additional guid
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        str
    """


def get_prefab_layer_all_assigned(a0: int) -> List[int]:
    """get prefab layer all assigned
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """


def get_prefab_layer_with_dimensions(a0: int) -> List[int]:
    """get prefab layer with dimensions
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """


def get_prefab_layer_without_dimensions(a0: int) -> List[int]:
    """get prefab layer without dimensions
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """


def is_nesting_parent(a0: int) -> bool:
    """is nesting parent
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def is_nesting_raw_part(a0: int) -> bool:
    """is nesting raw part
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def get_container_number(a0: int) -> int:
    """get container number
    Args:
        a0 ( int): a0

    Returns:
        int
    """


def get_container_number_with_prefix(a0: int) -> str:
    """get container number with prefix
    Args:
        a0 ( int): a0

    Returns:
        str
    """


def get_group_list_items() -> List[str]:
    """get group list items
    Args:

    Returns:
        List[str]
    """


def get_subgroup_list_items() -> List[str]:
    """get subgroup list items
    Args:

    Returns:
        List[str]
    """


def get_comment_list_items() -> List[str]:
    """get comment list items
    Args:

    Returns:
        List[str]
    """


def get_sku_list_items() -> List[str]:
    """get sku list items
    Args:

    Returns:
        List[str]
    """


def get_user_attribute_list_items(a0: int) -> List[str]:
    """get user attribute list items
    Args:
        a0 ( int): a0

    Returns:
        List[str]
    """


def is_circular_mep(a0: int) -> bool:
    """is circular mep
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def is_rectangular_mep(a0: int) -> bool:
    """is rectangular mep
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def get_machine_calculation_state(a0: int) -> str:
    """get machine calculation state
    Args:
        a0 ( int): a0

    Returns:
        str
    """


def get_machine_calculation_set_machine_type(a0: int) -> str:
    """get machine calculation set machine type
    Args:
        a0 ( int): a0

    Returns:
        str
    """


def is_btl_processing_group(a0: int) -> bool:
    """is btl processing group
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def is_hundegger_processing_group(a0: int) -> bool:
    """is hundegger processing group
    Args:
        a0 ( int): a0

    Returns:
        bool
    """


def get_element_grouping_type() -> element_grouping_type:
    """get element grouping type
    Args:

    Returns:
        element_grouping_type
    """


def set_element_grouping_type(a0: element_grouping_type) -> None:
    """set element grouping type
    Args:
        a0 ( element_grouping_type): a0

    Returns:
        None
    """


def get_associated_nesting_name(id: None) -> str:
    """get associated nesting name
    Args:
        id ( None): id

    Returns:
        str
    """


def get_associated_nesting_number(id: None) -> str:
    """get associated nesting number
    Args:
        id ( None): id

    Returns:
        str
    """


def get_attribute_display_settings_for_2d() -> attribute_display_settings:
    """get attribute display settings for 2d
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_2d_with_layout() -> attribute_display_settings:
    """get attribute display settings for 2d with layout
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_2d_without_layout() -> attribute_display_settings:
    """get attribute display settings for 2d without layout
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_3d() -> attribute_display_settings:
    """get attribute display settings for 3d
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_container() -> attribute_display_settings:
    """get attribute display settings for container
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_export_solid() -> attribute_display_settings:
    """get attribute display settings for export solid
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_axis() -> attribute_display_settings:
    """get attribute display settings for framed wall axis
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_beam() -> attribute_display_settings:
    """get attribute display settings for framed wall beam
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_opening() -> attribute_display_settings:
    """get attribute display settings for framed wall opening
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_framed_wall_panel() -> attribute_display_settings:
    """get attribute display settings for framed wall panel
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_axis() -> attribute_display_settings:
    """get attribute display settings for log wall axis
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_beam() -> attribute_display_settings:
    """get attribute display settings for log wall beam
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_opening() -> attribute_display_settings:
    """get attribute display settings for log wall opening
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_log_wall_panel() -> attribute_display_settings:
    """get attribute display settings for log wall panel
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_machine() -> attribute_display_settings:
    """get attribute display settings for machine
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_nesting_element() -> attribute_display_settings:
    """get attribute display settings for nesting element
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_nesting_volume() -> attribute_display_settings:
    """get attribute display settings for nesting volume
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_axis() -> attribute_display_settings:
    """get attribute display settings for solid wall axis
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_beam() -> attribute_display_settings:
    """get attribute display settings for solid wall beam
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_opening() -> attribute_display_settings:
    """get attribute display settings for solid wall opening
    Args:

    Returns:
        attribute_display_settings
    """


def get_attribute_display_settings_for_solid_wall_panel() -> attribute_display_settings:
    """get attribute display settings for solid wall panel
    Args:

    Returns:
        attribute_display_settings
    """


def is_processing(id: None) -> bool:
    """is processing
    Args:
        id ( None): id

    Returns:
        bool
    """
