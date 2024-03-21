from typing import List

def set_element_multi_layer_set(element_id: int, set_id: None) -> None:
    """Sets the multi layer set id of a cover

    Parameters:
        element_id: element_id
        set_id: set_id

    Returns:
        None
    """

def set_multi_layer_set_name(set_id: None, set_name: str) -> None:
    """Sets the name for a multi layer set

    Parameters:
        set_id: set_id
        set_name: set_name

    Returns:
        None
    """

def set_cover_name(set_id: None, cover_name: str) -> None:
    """Sets the cover name of the multi layer set

    Parameters:
        set_id: set_id
        cover_name: cover_name

    Returns:
        None
    """

def set_cover_material(set_id: None, cover_material: int) -> None:
    """Sets the cover material of the multi layer set

    Parameters:
        set_id: set_id
        cover_material: cover_material

    Returns:
        None
    """

def set_cover_thickness(set_id: None, cover_thickness: float) -> None:
    """Sets the cover thickness of the multi layer set. Only allowed for simple walls (cover without layer)

    Parameters:
        set_id: set_id
        cover_thickness: cover_thickness

    Returns:
        None
    """

def create_multi_layer_wall(set_name: str) -> int:
    """Creates a new multi layer wall with given name and default values

    Parameters:
        set_name: set_name

    Returns:
        multiLayerSetID
    """

def add_layer(set_id: None, element_grouping_type: None, name: str, material_id: int, thickness: float) -> None:
    """Adds a new layer to the multi layer set

    Parameters:
        set_id: set_id
        element_grouping_type: element_grouping_type
        name: name
        material_id: material_id
        thickness: thickness

    Returns:
        None
    """

def set_layer_name(set_id: None, layer_index: int, name: str) -> None:
    """Sets the name of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index
        name: name

    Returns:
        None
    """

def set_layer_material(set_id: None, layer_index: int, material_id: int) -> None:
    """Sets the material of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index
        material_id: material_id

    Returns:
        None
    """

def set_layer_thickness(set_id: None, layer_index: int, thickness: float) -> None:
    """Sets the thickness of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index
        thickness: thickness

    Returns:
        None
    """

def set_layer_type(set_id: None, layer_index: int, element_grouping_type: None) -> None:
    """Sets the type of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index
        element_grouping_type: element_grouping_type

    Returns:
        None
    """

def set_cover_color(set_id: None, cover_color: None) -> None:
    """Sets the cover color of the multi layer set

    Parameters:
        set_id: set_id
        cover_color: cover_color

    Returns:
        None
    """

def get_multi_layer_walls() -> List[int]:
    """Gets all multi layer wall ids

    Returns:
        List[int]
    """

def get_multi_layer_set_name(set_id: None) -> str:
    """Gets the name for a multi layer set

    Parameters:
        set_id: set_id

    Returns:
        string
    """

def get_element_multi_layer_set(element_id: int) -> int:
    """Gets the multi layer set id of a cover

    Parameters:
        element_id: element_id

    Returns:
        multiLayerSetID
    """

def get_cover_name(set_id: None) -> str:
    """Gets the cover name defined in the multi layer set

    Parameters:
        set_id: set_id

    Returns:
        string
    """

def get_cover_material(set_id: None) -> int:
    """Gets the cover material defined in the multi layer set

    Parameters:
        set_id: set_id

    Returns:
        materialID
    """

def get_cover_thickness(set_id: None) -> float:
    """Gets the cover thickness of the multi layer set

    Parameters:
        set_id: set_id

    Returns:
        double
    """

def get_layer_count(set_id: None) -> int:
    """Gets the Number of Layers of the multi layer set

    Parameters:
        set_id: set_id

    Returns:
        uint64_t
    """

def get_layer_name(set_id: None, layer_index: int) -> str:
    """Gets the name of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index

    Returns:
        string
    """

def get_layer_thickness(set_id: None, layer_index: int) -> float:
    """Gets the thickness of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index

    Returns:
        double
    """

def get_layer_material(set_id: None, layer_index: int) -> int:
    """Gets the material of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index

    Returns:
        string
    """

def get_layer_type(set_id: None, layer_index: int) -> int:
    """Gets the type of a layer of the multi layer set

    Parameters:
        set_id: set_id
        layer_index: layer_index

    Returns:
        multiLayerType
    """

def get_cover_color(set_id: None) -> int:
    """Gets the cover color defined in the multi layer set

    Parameters:
        set_id: set_id

    Returns:
        colorID
    """

