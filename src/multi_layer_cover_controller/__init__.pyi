from typing import List
from cadwork import multi_layer_cover_type
from cadwork.api_types import *
from cadwork.multi_layer_type import multi_layer_type

def set_element_multi_layer_set(element_id: ElementId, set_id: MultiLayerSetId) -> None:
    """Sets the multi layer set id of a cover.

    Parameters:
        element_id: The element id of the cover.
        set_id: The multi layer set id.

    Examples:
        >>> cover_id = element.create_cover(points, normal_vector)
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Wall Type A")
        >>> mlc.set_element_multi_layer_set(cover_id, multi_layer_set_id)
    """

def set_multi_layer_set_name(set_id: MultiLayerSetId, set_name: str) -> None:
    """Sets the name for a multi layer set.

    Parameters:
        set_id: The multi layer set id.
        set_name: The multi layer set name.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_multi_layer_set_name(multi_layer_set_id, "Exterior Wall Type B")
    """

def set_cover_name(set_id: MultiLayerSetId, cover_name: str) -> None:
    """Sets the cover name of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        cover_name: The cover name.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_cover_name(multi_layer_set_id, "Exterior Facade")
    """

def set_cover_material(set_id: MultiLayerSetId, cover_material: MaterialId) -> None:
    """Sets the cover material of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        cover_material: The cover material.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> material_id = mc.get_material_id("Cement Board")
        >>> mlc.set_cover_material(multi_layer_set_id, material_id)
    """

def set_cover_thickness(set_id: MultiLayerSetId, cover_thickness: float) -> None:
    """Sets the cover thickness of the multi layer set. Only allowed for simple walls (cover without layer).

    Parameters:
        set_id: The multi layer set id.
        cover_thickness: The cover thickness.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Simple Wall")
        >>> mlc.set_cover_thickness(multi_layer_set_id, 150.0)
    """

def create_multi_layer_wall(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer wall with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> wall_set_id = mlc.create_multi_layer_wall("Exterior Insulated Wall")
        >>> print(f"Created new multi-layer wall with ID: {wall_set_id}")

    Returns:
        The multi layer set id.
    """

def add_layer(set_id: MultiLayerSetId, layer_type: multi_layer_type, name: str, material_id: MaterialId, thickness: float) -> None:
    """Adds a new layer to the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_type: The type of the layer.
        name: The name of the layer.
        material_id: The material id of the layer.
        thickness: The thickness of the layer.

    Examples:
        >>> material_id_1 = mc.get_material_id("material_1")
        >>> material_id_2 = mc.get_material_id("material_2")
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("MultiLayerWall")
        >>> layer1_thickness = 200
        >>> layer2_thickness = 15
        >>> mlc.add_layer(multi_layer_set_id, cadwork.multi_layer_type.structure.value, "Layer1", material_id_1, layer1_thickness)
        >>> mlc.add_layer(multi_layer_set_id, cadwork.multi_layer_type.panel.value, "Layer2", material_id_2, layer2_thickness)
    """

def set_layer_name(set_id: MultiLayerSetId, layer_index: UnsignedInt, name: str) -> None:
    """Sets the name of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.
        name: The name of the layer.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_name(multi_layer_set_id, 0, "Exterior Cladding")
        >>> mlc.set_layer_name(multi_layer_set_id, 1, "Insulation Layer")
    """

def set_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.
        material_id: The material id of the layer.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> insulation_material_id = mc.get_material_id("Mineral Wool")
        >>> mlc.set_layer_material(multi_layer_set_id, 1, insulation_material_id)
    """

def set_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt, thickness: float) -> None:
    """Sets the thickness of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.
        thickness: The layer thickness.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_thickness(multi_layer_set_id, 0, 25.0)  # Set first layer to 25mm
        >>> mlc.set_layer_thickness(multi_layer_set_id, 1, 120.0)  # Set second layer to 120mm
    """

def set_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt, layer_type: multi_layer_type) -> None:
    """Sets the type of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.
        layer_type: The layer type.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> layer_mid_point_idx = layer_count // 2
        >>> mlc.set_layer_type(multi_layer_set_id, layer_mid_point_idx, cadwork.multi_layer_type.structure.value)
    """

def set_cover_color(set_id: MultiLayerSetId, cover_color: ColorId) -> None:
    """Sets the cover color of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        cover_color: The cover color.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> blue_color_id = vc.get_color_id("blue")
        >>> mlc.set_cover_color(multi_layer_set_id, blue_color_id)
    """

def get_multi_layer_walls() -> List[MultiLayerSetId]:
    """Gets all multi layer wall ids.

    Examples:
        >>> wall_ids = mlc.get_multi_layer_walls()
        >>> print(f"Found {len(wall_ids)} multi-layer wall definitions")
        >>> for wall_id in wall_ids:
        ...     name = mlc.get_multi_layer_set_name(wall_id)
        ...     print(f"Wall ID: {wall_id}, Name: {name}")

    Returns:
        The multi layer wall ids.
    """

def get_multi_layer_set_name(set_id: MultiLayerSetId) -> str:
    """Gets the name for a multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        >>> print(f"Element uses multi-layer definition: {set_name}")

    Returns:
        The multi layer set name.
    """

def get_element_multi_layer_set(element_id: ElementId) -> MultiLayerSetId:
    """Gets the multi layer set id of a cover.

    Parameters:
        element_id: The element id of the cover.

    Examples:
        >>> cover_ids = element.get_covers()
        >>> for cover_id in cover_ids:
        ...     multi_layer_set_id = mlc.get_element_multi_layer_set(cover_id)
        ...     set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        ...     print(f"Cover {cover_id} uses wall type: {set_name}")

    Returns:
        The multi layer set id.
    """

def get_cover_name(set_id: MultiLayerSetId) -> str:
    """Gets the cover name defined in the multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> cover_name = mlc.get_cover_name(multi_layer_set_id)
        >>> print(f"Cover name: {cover_name}")

    Returns:
        The cover name.
    """

def get_cover_material(set_id: MultiLayerSetId) -> MaterialId:
    """Gets the cover material defined in the multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> material_id = mlc.get_cover_material(multi_layer_set_id)
        >>> material_name = mc.get_material_name(material_id)
        >>> print(f"Cover uses material: {material_name}")

    Returns:
        The cover material.
    """

def get_cover_thickness(set_id: MultiLayerSetId) -> float:
    """Gets the cover thickness of the multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> thickness = mlc.get_cover_thickness(multi_layer_set_id)
        >>> print(f"Cover thickness: {thickness}mm")

    Returns:
        The cover thickness.
    """

def get_layer_count(set_id: MultiLayerSetId) -> UnsignedInt:
    """Gets the number of layers of the multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> count = mlc.get_layer_count(multi_layer_set_id)
        >>> print(f"Wall has {count} layers")

    Returns:
        The number of layers.
    """

def get_layer_name(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Gets the name of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     print(f"Layer {i}: {layer_name}")

    Returns:
        The layer name.
    """

def get_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> float:
    """Gets the thickness of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> total_thickness = 0
        >>> for i in range(layer_count):
        ...     thickness = mlc.get_layer_thickness(multi_layer_set_id, i)
        ...     total_thickness += thickness
        ...     print(f"Layer {i} thickness: {thickness}mm")
        >>> print(f"Total wall thickness: {total_thickness}mm")

    Returns:
        The layer thickness.
    """

def get_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> MaterialId:
    """Gets the material of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     material_id = mlc.get_layer_material(multi_layer_set_id, i)
        ...     material_name = mc.get_material_name(material_id)
        ...     print(f"Layer {i} material: {material_name}")

    Returns:
        The layer material.
    """

def get_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> multi_layer_type:
    """Gets the type of a layer of the multi layer set.

    Parameters:
        set_id: The multi layer set id.
        layer_index: The layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(1, layer_count + 1):
        ...     layer_type = mlc.get_layer_type(multi_layer_set_id, i)
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     type_str = "Structure" if layer_type == cadwork.multi_layer_type.structure.value else "your logic..."
        ...     print(f"Layer {i} ({layer_name}): Type = {type_str}")

    Returns:
        The layer type.
    """

def get_cover_color(set_id: MultiLayerSetId) -> ColorId:
    """Gets the cover color defined in the multi layer set.

    Parameters:
        set_id: The multi layer set id.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> color_id = mlc.get_cover_color(multi_layer_set_id)
        >>> color_name = vc.get_color_name(color_id)
        >>> print(f"Cover uses color: {color_name}")

    Returns:
        The cover color.
    """

def get_multi_layer_framed_floors() -> List[MultiLayerSetId]:
    """Gets all framed multi layer floor ids.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_framed_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        The multi layer floor ids.
    """

def create_multi_layer_framed_floor(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer floor with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_floor("Standard Floor")
        >>> print(f"Created new multi-layer floor with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def get_multi_layer_framed_roofs() -> List[MultiLayerSetId]:
    """Gets all multi layer roof ids.

    Examples:
        >>> roof_ids = mlc.get_multi_layer_framed_roofs()
        >>> print(f"Found {len(roof_ids)} multi-layer roof definitions")
        >>> for roof_id in roof_ids:
        ...     name = mlc.get_multi_layer_set_name(roof_id)
        ...     print(f"Roof ID: {roof_id}, Name: {name}")

    Returns:
        The multi layer roof ids.
    """

def get_multi_layer_solid_floors() -> List[MultiLayerSetId]:
    """Gets all solid multi layer floor ids.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_solid_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        The multi layer floor ids.
    """

def create_multi_layer_solid_floor(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer solid floor with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_floor("Standard Solid Floor")
        >>> print(f"Created new multi-layer solid floor with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def create_multi_layer_framed_roof(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer roof with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_roof("Pitched Roof")
        >>> print(f"Created new multi-layer roof with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def create_multi_layer_framed_wall(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer wall with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_wall("Standard Wall")
        >>> print(f"Created new multi-layer wall with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def get_multi_layer_sets() -> List[MultiLayerSetId]:
    """Gets all multi layer set ids of all types.

    Examples:
        >>> all_ids = mlc.get_multi_layer_sets()
        >>> print(f"Found {len(all_ids)} multi-layer definitions in total")
        >>> for set_id in all_ids:
        ...     name = mlc.get_multi_layer_set_name(set_id)
        ...     print(f"Set ID: {set_id}, Name: {name}")

    Returns:
        The multi layer set ids.
    """

def create_multi_layer_by_cover_type(set_name: str, cover_type: multi_layer_cover_type) -> MultiLayerSetId:
    """Creates a new multi layer set of specified type with given name and default values.

    Parameters:
        set_name: The multi layer set name.
        cover_type: The cover type.

    Examples:
        >>> set_id = mlc.create_multi_layer_by_cover_type("Custom Solid Wall", cadwork.multi_layer_cover_type.solidWall)
        >>> print(f"Created new multi-layer set with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def get_multi_layer_sets_for_cover_type(cover_type: multi_layer_cover_type) -> List[MultiLayerSetId]:
    """Gets all multi layer set ids of specified cover type.

    Parameters:
        cover_type: The cover type.

    Examples:
        >>> set_ids = mlc.get_multi_layer_sets_for_cover_type(cadwork.multi_layer_cover_type.solidWall)

    Returns:
        The multi layer set ids.
    """


def get_multi_layer_log_walls() -> List[MultiLayerSetId]:
    """Gets all multi layer log wall ids.

    Examples:
        >>> log_wall_ids = mlc.get_multi_layer_log_walls()
        >>> print(f"Found {len(log_wall_ids)} multi-layer log wall definitions")
        >>> for log_wall_id in log_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(log_wall_id)
        ...     print(f"Log Wall ID: {log_wall_id}, Name: {name}")

    Returns:
        The multi layer log wall ids.
    """

def create_multi_layer_log_wall(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer log wall with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_log_wall("Standard Log Wall")
        >>> print(f"Created new multi-layer log wall with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def get_multi_layer_solid_roofs() -> List[MultiLayerSetId]:
    """Gets all multi layer solid roof ids.

    Examples:
        >>> solid_roof_ids = mlc.get_multi_layer_solid_roofs()
        >>> print(f"Found {len(solid_roof_ids)} multi-layer solid roof definitions")
        >>> for solid_roof_id in solid_roof_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_roof_id)
        ...     print(f"Solid Roof ID: {solid_roof_id}, Name: {name}")

    Returns:
        The multi layer solid roof ids.
    """

def create_multi_layer_solid_roof(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer solid roof with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_roof("Standard Solid Roof")
        >>> print(f"Created new multi-layer solid roof with ID: {set_id}")

    Returns:
        The multi layer set id.
    """

def get_multi_layer_solid_walls() -> List[MultiLayerSetId]:
    """Gets all multi layer solid wall ids.

    Examples:
        >>> solid_wall_ids = mlc.get_multi_layer_solid_walls()
        >>> print(f"Found {len(solid_wall_ids)} multi-layer solid wall definitions")
        >>> for solid_wall_id in solid_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_wall_id)
        ...     print(f"Solid Wall ID: {solid_wall_id}, Name: {name}")

    Returns:
        The multi layer solid wall ids.
    """

def create_multi_layer_solid_wall(set_name: str) -> MultiLayerSetId:
    """Creates a new multi layer solid wall with given name and default values.

    Parameters:
        set_name: The multi layer set name.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_wall("Standard Solid Wall")
        >>> print(f"Created new multi-layer solid wall with ID: {set_id}")

    Returns:
        The multi layer set id.
    """