from typing import List
from cadwork import (layer_settings,
                     extended_settings,
                     output_type,
                     process_type,
                     element_type,
                     )


def get_name(element: int) -> str:
    """get element name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): elmement id

    Returns:
        str: element name
    """


def set_name(elements: List[int], name: str) -> None:
    """

    Args:
        elements (List[int]): element IDs
        name (str): name
    """


def get_group(element: int) -> str:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: group name
    """


def set_group(elements: List[int], group: str) -> None:
    """set group

    Args:
        elements (List[int]): element IDs
        group (str): group name
    """


def get_subgroup(element: int) -> str:
    """get subgroup

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: subgroup name
    """


def set_subgroup(elements: List[int], subgroup: str) -> None:
    """

    Args:
        elements (List[int]): element IDs
        subgroup (str): subgroup name
    """


def get_comment(element: int) -> str:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: comment
    """


def set_comment(elements: List[int], comment: str) -> None:
    """_summary_

    Args:
        elements (List[int]): element IDs
        comment (str): comment
    """


def get_user_attribute(element: int, number: int) -> str:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        number (int): number user attribute

    Returns:
        str: user attribute name (key)
    """


def set_user_attribute(elements: List[int], number: int, value: str) -> None:
    """

    Args:
        elements (List[int]): element IDs
        number (int): user attribute (key)
        value (str): user attribute name (value)
    """


def get_sku(element: int) -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: sku code
    """


def set_sku(elements: List[int], sku: str) -> None:
    """_summary_

    Args:
        elements (List[int]): element IDs
        sku (str): sku code
    """


def get_production_number(element: int) -> int:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: number
    """


def set_production_number(elements: List[int], number: int) -> None:
    """

    Args:
        elements (List[int]): element IDs
        number (int): production number
    """


def get_part_number(element: int) -> int:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: part number
    """


def set_part_number(elements: List[int], number: int) -> None:
    """

    Args:
        elements (List[int]): element IDs
        number (int): part number
    """


def get_additional_guid(element: int, data_id: str) -> str:
    """get additional guid

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        data_id (str): data

    Returns:
        str: data
    """


def set_additional_guid(elements: List[int], data_id: str, guid: str) -> None:
    """set additional guid

    Args:
        elements (List[int]): element IDs
        data_id (str): data iD
        guid (str): a guid
    """


def get_additional_data(element: int, data_id: str) -> str:
    """Gets the element additional data

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        data_id (str): data id 

    Returns:
        str: additional data
    """


def set_additional_data(elements: List[int], data_id: str, data_text: str) -> None:
    """

    Args:
        elements (List[int]): element IDs
        data_id (str): data id
        data_text (str): additional data text
    """


def delete_additional_data(elements: List[int], data_id: str) -> None:
    """Deletes the element additional data

    Args:
        elements (List[int]): element IDs
        data_id (str): data ID
    """


def get_user_attribute_name(number: int) -> str:
    """Gets the user attribute name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): Number user attribute number

    Returns:
        str: user attribute name
    """


def set_user_attribute_name(number: int, name: str) -> None:
    """Sets the user attribute name

    Args:
        number (int): Number user attribute number
        name (str): User attribute name user attribute name
    """


def get_wall_situation(element: int) -> str:
    """Gets the element wall situation

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: element wall situation
    """


def is_beam(element: int) -> bool:
    """Tests if element is beam

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element beam
    """


def is_panel(element: int) -> bool:
    """Tests if element is panel

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element panel
    """


def is_opening(element: int) -> bool:
    """Tests if element is opening

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element opening
    """


def is_wall(element: int) -> bool:
    """Tests if element is wall

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element wall
    """


def is_framed_wall(element: int) -> bool:
    """Tests if element is a framed wall

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a framed wall
    """


def is_solid_wall(element: int) -> bool:
    """Tests if element is a solid wall

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a solid wall
    """


def is_log_wall(element: int) -> bool:
    """Tests if element is a log wall

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a log wall
    """


def is_framed_floor(element: int) -> bool:
    """Tests if element is a framed floor

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a framed floor
    """


def is_solid_floor(element: int) -> bool:
    """Tests if element is a solid floor

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a solid floor
    """


def is_floor(element: int) -> bool:
    """Tests if element is floor

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element floor
    """


def is_roof(element: int) -> bool:
    """Tests if element is roof

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element roof
    """


def is_framed_roof(element: int) -> bool:
    """Tests if element is a framed roof

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a framed roof
    """


def is_solid_roof(element: int) -> bool:
    """Tests if element is a solid roof

    !!! Info
            Available in script filled attribut

    Args:
        element (int): element ID

    Returns:
        bool: is element a solid roof
    """


def is_metal(element: int) -> bool:
    """Tests if element is metal

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element metal
    """


def is_export_solid(element: int) -> bool:
    """Tests if element is export solid

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element export solid
    """


def is_container(element: int) -> bool:
    """Tests if element is container

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element container
    """


def is_connector_axis(element: int) -> bool:
    """Tests if element is connector axis

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element connector axis
    """


def is_drilling(element: int) -> bool:
    """Tests if element is drilling

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element drilling
    """


def is_node(element: int) -> bool:
    """Tests if element is node

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element node
    """


def is_auxiliary(element: int) -> bool:
    """Tests if element is auxiliary

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element auxiliary
    """


def is_line(element: int) -> bool:
    """Tests if element is line

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element line
    """


def is_surface(element: int) -> bool:
    """Tests if element is surface

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is element surface
    """


def get_element_material_name(element: int) -> str:
    """Gets the element material name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: element material name
    """


def get_prefab_layer(element: int) -> str:
    """Gets the element prefab layer

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: element prefab layer
    """


def get_machine_calculation_set(element: int) -> str:
    """Gets the element machine calculation set

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: element machine calculation set
    """


def get_cutting_set(element: int) -> str:
    """Gets the element cutting set

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: element cutting set
    """


def set_process_type_and_extended_settings_from_name(elements: List[int]) -> None:
    """ Sets the element process type and extended settings from the element name

    Args:
        elements (List[int]): ElementIDs
    """


def set_name_process_type(name: str, process_type: process_type) -> None:
    """Sets the process type for an element name

    Args:
        name (str): element name
        process_type (process_type): process type
    """


def get_name_process_type(name: int) -> process_type:
    """Gets the process type for an element name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (int): element name

    Returns:
        process_type: process type
    """


def set_name_extended_settings(name: str, extended_settings: extended_settings) -> None:
    """Sets the extended settings for an element name

    Args:
        name (str): element name
        extended_settings (extended_settings): extended settings
    """


def get_name_extended_settings(name: str) -> extended_settings:
    """Gets the extended settings for an element name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        name (str): element name

    Returns:
        extended_settings: extended settings
    """


def get_output_type(element: int) -> output_type:
    """Gets the element output type

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        output_type: output type
    """


def set_output_type(elements: List[int], output_type: output_type) -> None:
    """Sets the element output type

    Args:
        elements (List[int]):  element IDs
        output_type (output_type): element output type
    """


def get_extended_settings(element: int) -> extended_settings:
    """Gets the element extended settings

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        extended_settings: extended settings
    """


def set_extended_settings(elements: List[int], extended_settings: extended_settings) -> None:
    """Sets the element extended settings

    Args:
        elements (List[int]): element IDs
        extended_settings (extended_settings): element extended settings
    """


def get_element_type(element: int) -> element_type:
    """Gets the element type

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        element_type: type
    """


def set_wall(elements: List[int]) -> None:
    """Sets the element to wall

    Args:
        elements (List[int]): element IDs
    """


def set_log_wall(elements: List[int]) -> None:
    """Sets the element to log wall

    Args:
        elements (List[int]): element IDs
    """


def set_floor(elements: List[int]) -> None:
    """Sets the element to floor

    Args:
        elements (List[int]): element IDs
    """


def set_opening(elements: List[int]) -> None:
    """Sets the element to opening

    Args:
        elements (List[int]): element IDs
    """


def get_fastening_attribute(element: int) -> str:
    """Get the element fastening attribute

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: element fastening attribute
    """


def set_fastening_attribute(elements: List[int], value: str) -> None:
    """Sets the element fastening attribute

    Args:
        elements (List[int]): element IDs
        value (str): Value element fastening attribute
    """


def is_roof_surface(element: int) -> bool:
    """Tests if the element is caddy object

    Args:
        element (int): element ID

    Returns:
        bool: is element caddy object
    """


def is_caddy_object(element: int) -> bool:
    """Tests if the element is caddy object

    Args:
        element (int): element ID

    Returns:
        bool: is element caddy object
    """


def set_element_material(elements: List[int], material_id: int) -> None:
    """Sets the element material

    Args:
        elements (List[int]): element IDs
        material_id (int): material ID
    """


def get_assembly_number(element: int) -> str:
    """Get the elmement assembly number

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: assembly number
    """


def set_assembly_number(elements: List[int], number: str) -> None:
    """Set the elmement assembly number

    Args:
        elements (List[int]): element IDs
        number (str): assembly number
    """


def get_list_quantity(element: int) -> int:
    """Get element quantity

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): elmement ID

    Returns:
        int: elmement quantity 
    """


def set_list_quantity(elements: List[int], quantity: int) -> None:
    """Set element quantity

    Args:
        elements (List[int]): element IDs
        quantity (int): elmement quantity 
    """


def is_envelope(element: int) -> bool:
    """Tests if the element is envelope

    Args:
        element (int): element ID

    Returns:
        bool: is element envelope
    """


def set_layer_settings(elements: List[int], layer_settings: layer_settings) -> None:
    """Sets element layer settings

    Args:
        elements (List[int]): element IDs
        layer_settings (layer_settings): layer setting
    """


def set_ignore_in_vba_calculation(elements: List[int], value: bool) -> None:
    """Sets if the element should be ignored in VBA Calculation

    Args:
        elements (List[int]): element IDs
        value (bool): Ignore
    """


def get_ignore_in_vba_calculation(element: int) -> bool:
    """
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: Ignore
    """


def is_architecture_wall_2dc(element: int) -> bool:
    """Tests if the element has a 2dc reference wall

    Args:
        element (int): element ID

    Returns:
        bool: is architecturewall 2dc
    """


def is_architecture_wall_xml(element: int) -> bool:
    """Tests if the element has a xml reference wall

    Args:
        element (int): element ID

    Returns:
        bool: is architecturewall xml
    """


def set_reference_wall_2dc(elements: List[int], wall: str) -> None:
    """Applies a new 2dc reference wall to an element

    Args:
        elements (List[int]): element IDs
        wall (str): 2dc file path
    """


def set_node_symbol(elements: List[int], node_symbol: int) -> None:
    """Set a node symbol.
    ChessSquare, Circle, Cross, CrossSquare, FilledCircle, FilledSquare, HalfFilledSquare ,SmallSquare, Square

    Args:
        elements (List[int]): element IDs
        node_symbol (int): node symbol number
    """


def set_solid_floor(elements: List[int]) -> None:
    """set property for element type to solid floor 

    Args:
        elements (List[int]): element IDs
    """


def set_solid_roof(elements: List[int]) -> None:
    """set property for element type to solid roof 

    Args:
        elements (List[int]): element IDs
    """


def set_solid_wall(elements: List[int]) -> None:
    """set property for element type to solid wall 

    Args:
        elements (List[int]): element IDs
    """


def set_wall(elements: List[int]) -> None:
    """set element to type wall

    Args:
        elements (List[int]): element IDs
    """


def set_standard_part(elements: List[int]) -> None:
    """Sets covers (wall, opening or floor) to standard part

    Args:
        elements (List[int]): element IDs
    """


def update_auto_attribute() -> None:
    """Start update auto attribute
    """


def get_auto_attribute(element: int, number: int) -> str:
    """Get auto attribute

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        number (int): auto attribute number

    Returns:
        str: name (value)
    """


def get_auto_attribute_name(element: int) -> str:
    """Get auto attribute name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: auto attribute name
    """


def get_steel_shape_name(element: int) -> str:
    """Get steel profile name
    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: steel profile name
    """


def get_standard_element_name(element: int) -> str:
    """Get standard element name

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: standard element name
    """


def enable_attribute_display() -> None:
    """enable attribute display
    """


def disable_attribute_display() -> None:
    """disable attribute display
    """


def get_prefab_layer_all_assigned(element: int) -> List[int]:
    """Get all layer to which the element is assigned

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[int]: Layer
    """


def get_prefab_layer_with_dimensions(element: int) -> List[int]:
    """Check if element is exported with prefab layer with dimensions

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[int]: layer number
    """


def get_prefab_layer_without_dimensions(element: int) -> List[int]:
    """Check if element is exported with prefab layer without dimensions

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[int]: layer number
    """


def get_prefab_layer(element: int) -> str:
    """Get prefab layer. Returns layer values for "With dimensions", "Without dimensions", "Show Attributes".

    Args:
        element (int): element id

    Returns:
        str: value 
    """


def is_nesting_parent(element: int) -> bool:
    """check if element is a nesting parent.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is nesting parent
    """


def is_nesting_raw_part(element: int) -> bool:
    """check if element is a nesting raw part.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        bool: is nesting raw part
    """


def is_circular_mep(self, element_type) -> bool:
    """

    Args:
        element_type (_type_): element type 

    Returns:
        bool: condition
    """


def is_rectangular_mep(self, element_type) -> bool:
    """

    Args:
        element_type (_type_): element type 

    Returns:
        bool: condition
    """
