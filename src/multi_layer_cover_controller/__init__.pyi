"""Multi-layer build-ups for walls, roofs and floors.

Covers the definition and management of layered cover assemblies
(walls — solid, framed, log; floors — solid, framed; roofs and
generic cover types): creating sets, naming them, and composing
them from ordered layers with type, material and thickness. The
template/library side of multi-layer construction; instantiation
of these covers as elements is done elsewhere in the API.
"""

from cadwork import multi_layer_cover_type
from cadwork.api_types import *
from cadwork.multi_layer_type import multi_layer_type

def set_element_multi_layer_set(element_id: ElementId, set_id: MultiLayerSetId) -> None:
    """Assign a multi layer set to a cover element.

    Does nothing if the element ID or the set ID is invalid. Marks the element as modified and
    refreshes the display if auto refresh is on.

    Parameters:
        element_id: Element ID of the cover.
        set_id: ID of an existing multi layer set.

    Examples:
        >>> cover_id = element.create_cover(points, normal_vector)
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Wall Type A")
        >>> mlc.set_element_multi_layer_set(cover_id, multi_layer_set_id)
    """

def set_multi_layer_set_name(set_id: MultiLayerSetId, set_name: str) -> None:
    """Rename a multi layer set.

    The name is made unique: if another set already has it, a suffix like ' (1)' is appended. Does
    nothing for an unknown set ID. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        set_name: Desired name of the set.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_multi_layer_set_name(multi_layer_set_id, "Exterior Wall Type B")
    """

def set_cover_name(set_id: MultiLayerSetId, cover_name: str) -> None:
    """Set the cover name of a multi layer set.

    Does nothing for an unknown set ID. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        cover_name: Cover name.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_cover_name(multi_layer_set_id, "Exterior Facade")
    """

def set_cover_material(set_id: MultiLayerSetId, cover_material: MaterialId) -> None:
    """Set the cover material of a multi layer set.

    Does nothing for an unknown set ID. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        cover_material: Material ID.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> material_id = mc.get_material_id("Cement Board")
        >>> mlc.set_cover_material(multi_layer_set_id, material_id)
    """

def set_cover_thickness(set_id: MultiLayerSetId, cover_thickness: float) -> None:
    """Set the cover thickness of a simple wall set.

    Only applies to sets flagged as simple walls (cover without layers); for all other sets,
    including sets created by the create functions, nothing happens. Does nothing for an unknown set
    ID.

    Parameters:
        set_id: ID of the multi layer set.
        cover_thickness: Cover thickness in mm.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Simple Wall")
        >>> mlc.set_cover_thickness(multi_layer_set_id, 150.0)
    """

def create_multi_layer_wall(set_name: str) -> MultiLayerSetId:
    """Create a new framed wall multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document. Same
    as create_multi_layer_framed_wall.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> wall_set_id = mlc.create_multi_layer_wall("Exterior Insulated Wall")
        >>> print(f"Created new multi-layer wall with ID: {wall_set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def add_layer(
    set_id: MultiLayerSetId, layer_type: multi_layer_type, name: str, material_id: MaterialId, thickness: float
) -> None:
    """Append a layer to a multi layer set.

    The layer is added at the end and the cover thickness becomes the sum of all layer thicknesses.
    A simple wall set is converted to a layered set. Does nothing for an unknown set ID or a
    thickness of 0 or less. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_type: Layer type as integer value (1 structure, 2 panel, 3 lathing, 4 air, 5
            covering).
        name: Layer name.
        material_id: Material ID of the layer.
        thickness: Layer thickness in mm; must be greater than 0.

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
    """Set the name of a layer in a multi layer set.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        name: New layer name.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_name(multi_layer_set_id, 0, "Exterior Cladding")
        >>> mlc.set_layer_name(multi_layer_set_id, 1, "Insulation Layer")
    """

def set_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt, material_id: MaterialId) -> None:
    """Set the material of a layer in a multi layer set.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        material_id: Material ID.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> insulation_material_id = mc.get_material_id("Mineral Wool")
        >>> mlc.set_layer_material(multi_layer_set_id, 1, insulation_material_id)
    """

def set_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt, thickness: float) -> None:
    """Set the thickness of a layer in a multi layer set.

    The cover thickness is recalculated as the sum of all layer thicknesses. Does nothing for an
    unknown set ID, an out-of-range layer index or a thickness of 0 or less. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        thickness: Layer thickness in mm; must be greater than 0.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_thickness(multi_layer_set_id, 0, 25.0)  # Set first layer to 25mm
        >>> mlc.set_layer_thickness(multi_layer_set_id, 1, 120.0)  # Set second layer to 120mm
    """

def set_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt, layer_type: multi_layer_type) -> None:
    """Set the type of a layer in a multi layer set.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        layer_type: Layer type as integer value (1 structure, 2 panel, 3 lathing, 4 air, 5
            covering).

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> layer_mid_point_idx = layer_count // 2
        >>> mlc.set_layer_type(multi_layer_set_id, layer_mid_point_idx, cadwork.multi_layer_type.structure.value)
    """

def set_cover_color(set_id: MultiLayerSetId, cover_color: ColorId) -> None:
    """Set the cover color of a multi layer set.

    Does nothing for an unknown set ID. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        cover_color: Color ID.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> blue_color_id = vc.get_color_id("blue")
        >>> mlc.set_cover_color(multi_layer_set_id, blue_color_id)
    """

def get_multi_layer_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of wall type.

    Returns an empty list if there are none.

    Examples:
        >>> wall_ids = mlc.get_multi_layer_walls()
        >>> print(f"Found {len(wall_ids)} multi-layer wall definitions")
        >>> for wall_id in wall_ids:
        ...     name = mlc.get_multi_layer_set_name(wall_id)
        ...     print(f"Wall ID: {wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; includes framed, solid and log walls.
    """

def get_multi_layer_set_name(set_id: MultiLayerSetId) -> str:
    """Get the name of a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        >>> print(f"Element uses multi-layer definition: {set_name}")

    Returns:
        Name of the set, or an empty string if the set ID is unknown.
    """

def get_element_multi_layer_set(element_id: ElementId) -> MultiLayerSetId:
    """Get the multi layer set ID assigned to a cover element.

    Parameters:
        element_id: Element ID of the cover.

    Examples:
        >>> cover_ids = element.get_covers()
        >>> for cover_id in cover_ids:
        ...     multi_layer_set_id = mlc.get_element_multi_layer_set(cover_id)
        ...     set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        ...     print(f"Cover {cover_id} uses wall type: {set_name}")

    Returns:
        ID of the multi layer set, or 0 if the element ID is invalid.
    """

def get_cover_name(set_id: MultiLayerSetId) -> str:
    """Get the cover name of a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> cover_name = mlc.get_cover_name(multi_layer_set_id)
        >>> print(f"Cover name: {cover_name}")

    Returns:
        Cover name, or an empty string if the set ID is unknown.
    """

def get_cover_material(set_id: MultiLayerSetId) -> MaterialId:
    """Get the cover material of a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> material_id = mlc.get_cover_material(multi_layer_set_id)
        >>> material_name = mc.get_material_name(material_id)
        >>> print(f"Cover uses material: {material_name}")

    Returns:
        Material ID, or 0 if the set ID is unknown.
    """

def get_cover_thickness(set_id: MultiLayerSetId) -> float:
    """Get the cover thickness of a multi layer set.

    For sets with layers this is the sum of the layer thicknesses.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> thickness = mlc.get_cover_thickness(multi_layer_set_id)
        >>> print(f"Cover thickness: {thickness}mm")

    Returns:
        Thickness in mm, or 0 if the set ID is unknown.
    """

def get_layer_count(set_id: MultiLayerSetId) -> UnsignedInt:
    """Get the number of layers in a multi layer set.

    Simple walls (cover without layers) have no layers.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> count = mlc.get_layer_count(multi_layer_set_id)
        >>> print(f"Wall has {count} layers")

    Returns:
        Number of layers; 0 if the set ID is unknown or the set is a simple wall.
    """

def get_layer_name(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the name of a layer in a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     print(f"Layer {i}: {layer_name}")

    Returns:
        Layer name. Empty string if the set ID is unknown or the layer index is out of range.
    """

def get_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> float:
    """Get the thickness of a layer in a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

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
        Layer thickness in mm, or 0 if the set ID is unknown or the layer index is out of range.
    """

def get_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> MaterialId:
    """Get the material of a layer in a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     material_id = mlc.get_layer_material(multi_layer_set_id, i)
        ...     material_name = mc.get_material_name(material_id)
        ...     print(f"Layer {i} material: {material_name}")

    Returns:
        Material ID, or 0 if the set ID is unknown or the layer index is out of range.
    """

def get_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> multi_layer_type:
    """Get the type of a layer in a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(1, layer_count + 1):
        ...     layer_type = mlc.get_layer_type(multi_layer_set_id, i)
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     type_str = "Structure" if layer_type == cadwork.multi_layer_type.structure.value else "your logic..."
        ...     print(f"Layer {i} ({layer_name}): Type = {type_str}")

    Returns:
        Layer type as integer (1 structure, 2 panel, 3 lathing, 4 air, 5 covering); 0 if the set ID
        is unknown or the layer index is out of range.
    """

def get_cover_color(set_id: MultiLayerSetId) -> ColorId:
    """Get the cover color of a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> color_id = mlc.get_cover_color(multi_layer_set_id)
        >>> color_name = vc.get_color_name(color_id)
        >>> print(f"Cover uses color: {color_name}")

    Returns:
        Color ID, or 0 if the set ID is unknown.
    """

def get_multi_layer_framed_floors() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type framed floor.

    Returns an empty list if there are none.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_framed_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_framed_floor(set_name: str) -> MultiLayerSetId:
    """Create a new framed floor multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_floor("Standard Floor")
        >>> print(f"Created new multi-layer floor with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_framed_roofs() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type framed roof.

    Returns an empty list if there are none.

    Examples:
        >>> roof_ids = mlc.get_multi_layer_framed_roofs()
        >>> print(f"Found {len(roof_ids)} multi-layer roof definitions")
        >>> for roof_id in roof_ids:
        ...     name = mlc.get_multi_layer_set_name(roof_id)
        ...     print(f"Roof ID: {roof_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def get_multi_layer_solid_floors() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid floor.

    Returns an empty list if there are none.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_solid_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_solid_floor(set_name: str) -> MultiLayerSetId:
    """Create a new solid floor multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_floor("Standard Solid Floor")
        >>> print(f"Created new multi-layer solid floor with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def create_multi_layer_framed_roof(set_name: str) -> MultiLayerSetId:
    """Create a new framed roof multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_roof("Pitched Roof")
        >>> print(f"Created new multi-layer roof with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def create_multi_layer_framed_wall(set_name: str) -> MultiLayerSetId:
    """Create a new framed wall multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document. Same
    as create_multi_layer_wall.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_wall("Standard Wall")
        >>> print(f"Created new multi-layer wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_sets() -> list[MultiLayerSetId]:
    """Get all multi layer sets of every cover type.

    Returns an empty list if there are none.

    Examples:
        >>> all_ids = mlc.get_multi_layer_sets()
        >>> print(f"Found {len(all_ids)} multi-layer definitions in total")
        >>> for set_id in all_ids:
        ...     name = mlc.get_multi_layer_set_name(set_id)
        ...     print(f"Set ID: {set_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_by_cover_type(set_name: str, cover_type: multi_layer_cover_type) -> MultiLayerSetId:
    """Create a new multi layer set of the given cover type.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.
        cover_type: Cover type of the new set.

    Examples:
        >>> set_id = mlc.create_multi_layer_by_cover_type("Custom Solid Wall", cadwork.multi_layer_cover_type.solidWall)
        >>> print(f"Created new multi-layer set with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty or the cover type is not supported.
    """

def get_multi_layer_sets_for_cover_type(cover_type: multi_layer_cover_type) -> list[MultiLayerSetId]:
    """Get all multi layer sets of the given cover type.

    Returns an empty list if there are none or the cover type is not supported.

    Parameters:
        cover_type: Cover type to filter by.

    Examples:
        >>> set_ids = mlc.get_multi_layer_sets_for_cover_type(cadwork.multi_layer_cover_type.solidWall)

    Returns:
        List of multi layer set IDs.
    """

def get_multi_layer_log_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type log wall.

    Returns an empty list if there are none.

    Examples:
        >>> log_wall_ids = mlc.get_multi_layer_log_walls()
        >>> print(f"Found {len(log_wall_ids)} multi-layer log wall definitions")
        >>> for log_wall_id in log_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(log_wall_id)
        ...     print(f"Log Wall ID: {log_wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_log_wall(set_name: str) -> MultiLayerSetId:
    """Create a new log wall multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_log_wall("Standard Log Wall")
        >>> print(f"Created new multi-layer log wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_solid_roofs() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid roof.

    Returns an empty list if there are none.

    Examples:
        >>> solid_roof_ids = mlc.get_multi_layer_solid_roofs()
        >>> print(f"Found {len(solid_roof_ids)} multi-layer solid roof definitions")
        >>> for solid_roof_id in solid_roof_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_roof_id)
        ...     print(f"Solid Roof ID: {solid_roof_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_solid_roof(set_name: str) -> MultiLayerSetId:
    """Create a new solid roof multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_roof("Standard Solid Roof")
        >>> print(f"Created new multi-layer solid roof with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_solid_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid wall.

    Returns an empty list if there are none.

    Examples:
        >>> solid_wall_ids = mlc.get_multi_layer_solid_walls()
        >>> print(f"Found {len(solid_wall_ids)} multi-layer solid wall definitions")
        >>> for solid_wall_id in solid_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_wall_id)
        ...     print(f"Solid Wall ID: {solid_wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs.
    """

def create_multi_layer_solid_wall(set_name: str) -> MultiLayerSetId:
    """Create a new solid wall multi layer set.

    The name is made unique by appending ' (1)', ' (2)' etc. if needed. The new set gets default
    values (100 mm cover thickness, default material, no layers) and is saved to the document.

    Parameters:
        set_name: Name of the new set; must not be empty.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_wall("Standard Solid Wall")
        >>> print(f"Created new multi-layer solid wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_set_component_type(set_id: MultiLayerSetId) -> int:
    """Get the component type of a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.

    Returns:
        Component type as integer: 1 material, 2 standard element; 0 if the set ID is unknown.
    """

def set_multi_layer_set_component_type(set_id: MultiLayerSetId, type: int) -> None:
    """Set the component type of a multi layer set.

    Does nothing for an unknown set ID. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        type: Component type as integer: 1 material, 2 standard element.
    """

def get_layer_sub_type(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> int:
    """Get the sub type of a layer in a multi layer set.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Returns:
        Layer sub type as integer (1 load-bearing frame structure, 2 solid structure, 3 straight
        edge, 4 bias edge, 5 vertical, 6 horizontal, 7 air, 8 non-load-bearing frame structure); 0
        if the set ID is unknown or the layer index is out of range.
    """

def set_layer_sub_type(set_id: MultiLayerSetId, layer_index: UnsignedInt, sub_type: int) -> None:
    """Set the sub type of a layer in a multi layer set.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        sub_type: Layer sub type as integer (1 load-bearing frame structure, 2 solid structure, 3
            straight edge, 4 bias edge, 5 vertical, 6 horizontal, 7 air, 8 non-load-bearing frame
            structure).
    """

def get_layer_standard_panel_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the GUID of the standard panel used by a layer.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Returns:
        GUID as string. Empty string if the set ID is unknown or the layer index is out of range.
    """

def set_layer_standard_panel_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt, guid: str) -> None:
    """Set the standard panel GUID of a layer.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        guid: GUID string of the standard panel.
    """

def get_layer_standard_beam_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the GUID of the standard beam used by a layer.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.

    Returns:
        GUID as string. Empty string if the set ID is unknown or the layer index is out of range.
    """

def set_layer_standard_beam_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt, guid: str) -> None:
    """Set the standard beam GUID of a layer.

    Does nothing for an unknown set ID or an out-of-range layer index. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based layer index.
        guid: GUID string of the standard beam.
    """

def add_layer_by_standard_elements(
    set_id: MultiLayerSetId, type: multi_layer_type, name: str, panel_guid: str, beam_guid: str, thickness: float
) -> None:
    """Append a layer defined by standard panel and beam elements.

    The layer is added at the end and the cover thickness becomes the sum of all layer thicknesses.
    A simple wall set is converted to a layered set. No material is set on the layer. Does nothing
    for an unknown set ID or a thickness of 0 or less. Saved to the document.

    Parameters:
        set_id: ID of the multi layer set.
        type: Layer type as integer value (1 structure, 2 panel, 3 lathing, 4 air, 5 covering).
        name: Layer name.
        panel_guid: GUID string of the standard panel.
        beam_guid: GUID string of the standard beam.
        thickness: Layer thickness in mm; must be greater than 0.
    """

def remove_layer(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> None:
    """Remove one layer from a multi layer set.

    The cover thickness is updated to the sum of the remaining layer thicknesses (kept unchanged if
    no layer remains). Covers using the set are queued for recreation, which only happens while auto
    display refresh is on. Does nothing for an unknown set ID or an out-of-range index.

    Parameters:
        set_id: ID of the multi layer set.
        layer_index: Zero-based index of the layer to remove; must be smaller than the layer count.
    """

def remove_all_layers(set_id: MultiLayerSetId) -> None:
    """Remove all layers from a multi layer set.

    Covers that use the set are queued for recreation, which only happens while automatic display
    refresh is on. Does nothing for an unknown set ID or a set without layers.

    Parameters:
        set_id: ID of the multi layer set.
    """

def insert_layer(
    set_id: MultiLayerSetId,
    position: UnsignedInt,
    type: multi_layer_type,
    name: str,
    material_id: MaterialId,
    thickness: float,
) -> None:
    """Insert a new layer into a multi layer set at the given position.

    The set's cover thickness becomes the sum of all layer thicknesses, and a simple-wall set
    becomes a regular layered set. Covers using the set are queued for recreation, which only
    happens while automatic display refresh is on. Does nothing for an unknown set ID or a thickness
    that is zero or negative.

    Parameters:
        set_id: ID of the multi layer set.
        position: Zero-based position of the new layer; values at or beyond the layer count append
            it.
        type: Type of the layer.
        name: Name of the layer.
        material_id: Material ID of the layer.
        thickness: Layer thickness in mm; must be greater than zero.
    """

def unset_element_multi_layer_set(element_id: ElementId) -> None:
    """Remove the multi layer set assignment from a cover element.

    The element is marked as modified and the display is refreshed if automatic refresh is on. Does
    nothing for an invalid element ID or an element without an assigned set. The set itself is not
    deleted.

    Parameters:
        element_id: Element ID of the cover.
    """
