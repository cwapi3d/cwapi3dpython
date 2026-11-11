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

def set_element_multi_layer_set(element_id: ElementId, set_id: MultiLayerSetId) -> None:
    """Assign a multi layer set to a cover element.

    The cover element then uses the layer build-up of that set. The element is marked as modified
    and the display is refreshed if automatic display refresh is on. Nothing happens if the element
    ID or the set ID is invalid. Remove the assignment with
    `multi_layer_cover_controller.unset_element_multi_layer_set()`, read it with
    `multi_layer_cover_controller.get_element_multi_layer_set()`.

    Parameters:
        element_id: Element ID of a cover (wall, floor or roof), e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> cover_id = element.create_cover(points, normal_vector)
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Wall Type A")
        >>> mlc.set_element_multi_layer_set(cover_id, multi_layer_set_id)
    """

def set_multi_layer_set_name(set_id: MultiLayerSetId, set_name: str) -> None:
    """Rename a multi layer set.

    The name is made unique: if any set already has the requested name, ' (1)', ' (2)' and so on is
    appended. This also applies to the set's own current name, so setting the same name again adds a
    suffix. Nothing happens for an unknown set ID. The change is saved to the document. Read the
    name with `multi_layer_cover_controller.get_multi_layer_set_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        set_name: Desired name of the set.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_multi_layer_set_name(multi_layer_set_id, "Exterior Wall Type B")
    """

def set_cover_name(set_id: MultiLayerSetId, cover_name: str) -> None:
    """Set the cover name of a multi layer set.

    The cover name is a separate text property of the set, distinct from the set name that
    identifies it in lists. Nothing happens for an unknown set ID. The change is saved to the
    document. Read it with `multi_layer_cover_controller.get_cover_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        cover_name: Cover name to store; not required to be unique.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> mlc.set_cover_name(multi_layer_set_id, "Exterior Facade")
    """

def set_cover_material(set_id: MultiLayerSetId, cover_material: MaterialId) -> None:
    """Set the cover material of a multi layer set.

    The cover material is the material of the cover as a whole, separate from the materials of the
    individual layers. Nothing happens for an unknown set ID. The change is saved to the document.
    Read it with `multi_layer_cover_controller.get_cover_material()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        cover_material: Material ID, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> material_id = mc.get_material_id("Cement Board")
        >>> mlc.set_cover_material(multi_layer_set_id, material_id)
    """

def set_cover_thickness(set_id: MultiLayerSetId, cover_thickness: float) -> None:
    """Set the cover thickness of a simple wall set.

    Only sets flagged as simple walls (a cover without layers) accept a thickness; for every other
    set, including all sets made by the create functions, nothing happens. Sets with layers get
    their thickness from the layers instead. Nothing happens for an unknown set ID. Read the value
    with `multi_layer_cover_controller.get_cover_thickness()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        cover_thickness: Cover thickness in mm.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Simple Wall")
        >>> mlc.set_cover_thickness(multi_layer_set_id, 150.0)
    """

def create_multi_layer_wall(set_name: str) -> MultiLayerSetId:
    """Create a new framed wall multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type framed wall and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Identical to
    `multi_layer_cover_controller.create_multi_layer_framed_wall()`. Fill the set with
    `multi_layer_cover_controller.add_layer()` and assign it to covers with
    `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> wall_set_id = mlc.create_multi_layer_wall("Exterior Insulated Wall")
        >>> print(f"Created new multi-layer wall with ID: {wall_set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def add_layer(set_id: MultiLayerSetId, layer_type: int, name: str, material_id: MaterialId, thickness: float) -> None:
    """Append a layer to the end of a multi layer set.

    The cover thickness of the set becomes the sum of all layer thicknesses. A simple wall set
    (cover without layers) is converted to a layered set. The change is saved to the document;
    covers already using the set are not queued for recreation by this call. Nothing happens for an
    unknown set ID or a thickness of 0 or less. Use `multi_layer_cover_controller.insert_layer()` to
    place a layer at a given position.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_type: Layer type as integer: 1 structure, 2 panel, 3 lathing, 4 air, 5 covering
            (`cadwork.multi_layer_type` members, use `.value`). The value is not validated.
        name: Name of the layer.
        material_id: Material ID, e.g. from `material_controller.get_material_id()`. The ID is not
            validated.
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

    Nothing happens for an unknown set ID or an out-of-range layer index. The change is saved to the
    document. Read it with `multi_layer_cover_controller.get_layer_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        name: New layer name.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_name(multi_layer_set_id, 0, "Exterior Cladding")
        >>> mlc.set_layer_name(multi_layer_set_id, 1, "Insulation Layer")
    """

def set_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt, material_id: MaterialId) -> None:
    """Set the material of a layer in a multi layer set.

    Nothing happens for an unknown set ID or an out-of-range layer index. The change is saved to the
    document. Read it with `multi_layer_cover_controller.get_layer_material()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        material_id: Material ID, e.g. from `material_controller.get_material_id()`. The ID is not
            validated.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> insulation_material_id = mc.get_material_id("Mineral Wool")
        >>> mlc.set_layer_material(multi_layer_set_id, 1, insulation_material_id)
    """

def set_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt, thickness: float) -> None:
    """Set the thickness of a layer in a multi layer set.

    The cover thickness of the set is recalculated as the sum of all layer thicknesses. The change
    is saved to the document; covers already using the set are not queued for recreation by this
    call. Nothing happens for an unknown set ID, an out-of-range layer index or a thickness of 0 or
    less. Read it with `multi_layer_cover_controller.get_layer_thickness()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        thickness: Layer thickness in mm; must be greater than 0.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> mlc.set_layer_thickness(multi_layer_set_id, 0, 25.0)  # Set first layer to 25mm
        >>> mlc.set_layer_thickness(multi_layer_set_id, 1, 120.0)  # Set second layer to 120mm
    """

def set_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt, layer_type: int) -> None:
    """Set the type of a layer in a multi layer set.

    The layer type says what the layer is (structure, panel, lathing, air or covering). Nothing
    happens for an unknown set ID or an out-of-range layer index. The change is saved to the
    document. Read it with `multi_layer_cover_controller.get_layer_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        layer_type: Layer type as integer: 1 structure, 2 panel, 3 lathing, 4 air, 5 covering
            (`cadwork.multi_layer_type` members, use `.value`). The value is not validated.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> layer_mid_point_idx = layer_count // 2
        >>> mlc.set_layer_type(multi_layer_set_id, layer_mid_point_idx, cadwork.multi_layer_type.structure.value)
    """

def set_cover_color(set_id: MultiLayerSetId, cover_color: ColorId) -> None:
    """Set the cover color of a multi layer set.

    The color is used for covers that use this set. Nothing happens for an unknown set ID. The
    change is saved to the document. Read it with `multi_layer_cover_controller.get_cover_color()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        cover_color: cadwork color ID, e.g. read from an element with
            `visualization_controller.get_color()`.

    Examples:
        >>> multi_layer_set_id = mlc.create_multi_layer_wall("Default Wall")
        >>> blue_color_id = vc.get_color_id("blue")
        >>> mlc.set_cover_color(multi_layer_set_id, blue_color_id)
    """

def get_multi_layer_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of wall type.

    Returns the framed, solid and log wall sets of the current document, in the order they are
    stored. Floors and roofs are not included; get every type with
    `multi_layer_cover_controller.get_multi_layer_sets()` or filter by one type with the specific
    getters.

    Examples:
        >>> wall_ids = mlc.get_multi_layer_walls()
        >>> print(f"Found {len(wall_ids)} multi-layer wall definitions")
        >>> for wall_id in wall_ids:
        ...     name = mlc.get_multi_layer_set_name(wall_id)
        ...     print(f"Wall ID: {wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if the document has none.
    """

def get_multi_layer_set_name(set_id: MultiLayerSetId) -> str:
    """Get the name of a multi layer set.

    The set name identifies the set in lists and is unique among sets. Change it with
    `multi_layer_cover_controller.set_multi_layer_set_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        >>> print(f"Element uses multi-layer definition: {set_name}")

    Returns:
        Name of the set; empty string if the set ID is unknown.
    """

def get_element_multi_layer_set(element_id: ElementId) -> MultiLayerSetId:
    """Get the multi layer set ID assigned to a cover element.

    Use the ID with the other getters to read the build-up (layers, thickness, material) of the
    cover. Assign a set with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        element_id: Element ID of a cover (wall, floor or roof), e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> cover_ids = element.get_covers()
        >>> for cover_id in cover_ids:
        ...     multi_layer_set_id = mlc.get_element_multi_layer_set(cover_id)
        ...     set_name = mlc.get_multi_layer_set_name(multi_layer_set_id)
        ...     print(f"Cover {cover_id} uses wall type: {set_name}")

    Returns:
        ID of the multi layer set; 0 if the element ID is invalid or the element cannot hold a set.
    """

def get_cover_name(set_id: MultiLayerSetId) -> str:
    """Get the cover name of a multi layer set.

    The cover name is a text property of the set, separate from the set name. Change it with
    `multi_layer_cover_controller.set_cover_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> cover_name = mlc.get_cover_name(multi_layer_set_id)
        >>> print(f"Cover name: {cover_name}")

    Returns:
        Cover name; empty string if the set ID is unknown.
    """

def get_cover_material(set_id: MultiLayerSetId) -> MaterialId:
    """Get the cover material of a multi layer set.

    This is the material of the cover as a whole, not of a single layer; read layer materials with
    `multi_layer_cover_controller.get_layer_material()`. New sets start with the default material of
    the document. Resolve the name with `material_controller.get_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> material_id = mlc.get_cover_material(multi_layer_set_id)
        >>> material_name = mc.get_material_name(material_id)
        >>> print(f"Cover uses material: {material_name}")

    Returns:
        Material ID; 0 if the set ID is unknown.
    """

def get_cover_thickness(set_id: MultiLayerSetId) -> float:
    """Get the cover thickness of a multi layer set.

    For sets with layers the thickness is the sum of the layer thicknesses, kept in sync when layers
    are added, changed or removed through this module. Removing all layers keeps the previous
    thickness. Set it directly with `multi_layer_cover_controller.set_cover_thickness()` (simple
    wall sets only).

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> thickness = mlc.get_cover_thickness(multi_layer_set_id)
        >>> print(f"Cover thickness: {thickness}mm")

    Returns:
        Thickness in mm; 0 if the set ID is unknown.
    """

def get_layer_count(set_id: MultiLayerSetId) -> UnsignedInt:
    """Get the number of layers in a multi layer set.

    Use the count as the upper bound for the layer index of the other layer functions. Simple wall
    sets (a cover without layers) report 0 layers.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> count = mlc.get_layer_count(multi_layer_set_id)
        >>> print(f"Wall has {count} layers")

    Returns:
        Number of layers; 0 if the set ID is unknown, the set is a simple wall or it has no layers.
    """

def get_layer_name(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the name of a layer in a multi layer set.

    Layers are indexed from 0 in stored order. Change the name with
    `multi_layer_cover_controller.set_layer_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     print(f"Layer {i}: {layer_name}")

    Returns:
        Layer name; empty string if the set ID is unknown or the layer index is out of range.
    """

def get_layer_thickness(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> float:
    """Get the thickness of a layer in a multi layer set.

    Layers are indexed from 0 in stored order. Change the thickness with
    `multi_layer_cover_controller.set_layer_thickness()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

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
        Layer thickness in mm; 0 if the set ID is unknown or the layer index is out of range.
    """

def get_layer_material(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> MaterialId:
    """Get the material of a layer in a multi layer set.

    Layers are indexed from 0 in stored order. Layers created with
    `multi_layer_cover_controller.add_layer_by_standard_elements()` have no material. Resolve the
    name with `material_controller.get_name()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(layer_count):
        ...     material_id = mlc.get_layer_material(multi_layer_set_id, i)
        ...     material_name = mc.get_material_name(material_id)
        ...     print(f"Layer {i} material: {material_name}")

    Returns:
        Material ID; 0 if the set ID is unknown or the layer index is out of range.
    """

def get_layer_type(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> int:
    """Get the type of a layer in a multi layer set.

    The type says what the layer is: structure, panel, lathing, air or covering. Compare against
    `cadwork.multi_layer_type` members using `.value`. Change it with
    `multi_layer_cover_controller.set_layer_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> layer_count = mlc.get_layer_count(multi_layer_set_id)
        >>> for i in range(1, layer_count + 1):
        ...     layer_type = mlc.get_layer_type(multi_layer_set_id, i)
        ...     layer_name = mlc.get_layer_name(multi_layer_set_id, i)
        ...     type_str = "Structure" if layer_type == cadwork.multi_layer_type.structure.value else "your logic..."
        ...     print(f"Layer {i} ({layer_name}): Type = {type_str}")

    Returns:
        Layer type as integer (1 structure, 2 panel, 3 lathing, 4 air, 5 covering); 0 (undefined) if
        the set ID is unknown or the layer index is out of range.
    """

def get_cover_color(set_id: MultiLayerSetId) -> ColorId:
    """Get the cover color of a multi layer set.

    The color is used for covers that use this set; new sets start with color 90. Change it with
    `multi_layer_cover_controller.set_cover_color()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> multi_layer_set_id = mlc.get_element_multi_layer_set(element_id)
        >>> color_id = mlc.get_cover_color(multi_layer_set_id)
        >>> color_name = vc.get_color_name(color_id)
        >>> print(f"Cover uses color: {color_name}")

    Returns:
        cadwork color ID; 0 if the set ID is unknown.
    """

def get_multi_layer_framed_floors() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type framed floor.

    Only sets created with cover type framed floor are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_framed_floor()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_framed_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_framed_floor(set_name: str) -> MultiLayerSetId:
    """Create a new framed floor multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type framed floor and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it
    to covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_floor("Standard Floor")
        >>> print(f"Created new multi-layer floor with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_framed_roofs() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type framed roof.

    Only sets created with cover type framed roof are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_framed_roof()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> roof_ids = mlc.get_multi_layer_framed_roofs()
        >>> print(f"Found {len(roof_ids)} multi-layer roof definitions")
        >>> for roof_id in roof_ids:
        ...     name = mlc.get_multi_layer_set_name(roof_id)
        ...     print(f"Roof ID: {roof_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def get_multi_layer_solid_floors() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid floor.

    Only sets created with cover type solid floor are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_solid_floor()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> floor_ids = mlc.get_multi_layer_solid_floors()
        >>> print(f"Found {len(floor_ids)} multi-layer floor definitions")
        >>> for floor_id in floor_ids:
        ...     name = mlc.get_multi_layer_set_name(floor_id)
        ...     print(f"Floor ID: {floor_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_solid_floor(set_name: str) -> MultiLayerSetId:
    """Create a new solid floor multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type solid floor and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it
    to covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_floor("Standard Solid Floor")
        >>> print(f"Created new multi-layer solid floor with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def create_multi_layer_framed_roof(set_name: str) -> MultiLayerSetId:
    """Create a new framed roof multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type framed roof and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it
    to covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_roof("Pitched Roof")
        >>> print(f"Created new multi-layer roof with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def create_multi_layer_framed_wall(set_name: str) -> MultiLayerSetId:
    """Create a new framed wall multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type framed wall and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Identical to `multi_layer_cover_controller.create_multi_layer_wall()`. Fill
    the set with `multi_layer_cover_controller.add_layer()` and assign it to covers with
    `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_framed_wall("Standard Wall")
        >>> print(f"Created new multi-layer wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_sets() -> list[MultiLayerSetId]:
    """Get all multi layer sets of every cover type.

    Returns walls, floors and roofs of all kinds (framed, solid, log) defined in the current
    document. Use the type specific getters or
    `multi_layer_cover_controller.get_multi_layer_sets_for_cover_type()` to filter.

    Examples:
        >>> all_ids = mlc.get_multi_layer_sets()
        >>> print(f"Found {len(all_ids)} multi-layer definitions in total")
        >>> for set_id in all_ids:
        ...     name = mlc.get_multi_layer_set_name(set_id)
        ...     print(f"Set ID: {set_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_by_cover_type(set_name: str, cover_type: multi_layer_cover_type) -> MultiLayerSetId:
    """Create a new multi layer set of the given cover type.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. Use this when the cover type is chosen at run time;
    otherwise the specific create functions are shorter. The set is saved to the document. The new
    set has no layers, a cover thickness of 100 mm, the default material and cover color 90. Fill
    the set with `multi_layer_cover_controller.add_layer()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.
        cover_type: Cover type of the new set: framed, solid or log wall, framed or solid floor,
            framed or solid roof (`cadwork.multi_layer_cover_type`).

    Examples:
        >>> set_id = mlc.create_multi_layer_by_cover_type("Custom Solid Wall", cadwork.multi_layer_cover_type.solidWall)
        >>> print(f"Created new multi-layer set with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty or the cover type is not one of the
        supported ones.
    """

def get_multi_layer_sets_for_cover_type(cover_type: multi_layer_cover_type) -> list[MultiLayerSetId]:
    """Get all multi layer sets of the given cover type.

    Exact match on the cover type: framed and solid variants of walls, floors and roofs are separate
    types. Use `multi_layer_cover_controller.get_multi_layer_sets()` for all sets regardless of
    type.

    Parameters:
        cover_type: Cover type to filter by (`cadwork.multi_layer_cover_type`).

    Examples:
        >>> set_ids = mlc.get_multi_layer_sets_for_cover_type(cadwork.multi_layer_cover_type.solidWall)

    Returns:
        List of multi layer set IDs; empty if there are none or the cover type is not supported.
    """

def get_multi_layer_log_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type log wall.

    Only sets created with cover type log wall are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_log_wall()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> log_wall_ids = mlc.get_multi_layer_log_walls()
        >>> print(f"Found {len(log_wall_ids)} multi-layer log wall definitions")
        >>> for log_wall_id in log_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(log_wall_id)
        ...     print(f"Log Wall ID: {log_wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_log_wall(set_name: str) -> MultiLayerSetId:
    """Create a new log wall multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type log wall and saved to
    the document. The new set has no layers, a cover thickness of 100 mm, the default material and
    cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it to
    covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_log_wall("Standard Log Wall")
        >>> print(f"Created new multi-layer log wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_solid_roofs() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid roof.

    Only sets created with cover type solid roof are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_solid_roof()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> solid_roof_ids = mlc.get_multi_layer_solid_roofs()
        >>> print(f"Found {len(solid_roof_ids)} multi-layer solid roof definitions")
        >>> for solid_roof_id in solid_roof_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_roof_id)
        ...     print(f"Solid Roof ID: {solid_roof_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_solid_roof(set_name: str) -> MultiLayerSetId:
    """Create a new solid roof multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type solid roof and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it
    to covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_roof("Standard Solid Roof")
        >>> print(f"Created new multi-layer solid roof with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_solid_walls() -> list[MultiLayerSetId]:
    """Get all multi layer sets of type solid wall.

    Only sets created with cover type solid wall are returned. Create one with
    `multi_layer_cover_controller.create_multi_layer_solid_wall()`; get every type at once with
    `multi_layer_cover_controller.get_multi_layer_sets()`.

    Examples:
        >>> solid_wall_ids = mlc.get_multi_layer_solid_walls()
        >>> print(f"Found {len(solid_wall_ids)} multi-layer solid wall definitions")
        >>> for solid_wall_id in solid_wall_ids:
        ...     name = mlc.get_multi_layer_set_name(solid_wall_id)
        ...     print(f"Solid Wall ID: {solid_wall_id}, Name: {name}")

    Returns:
        List of multi layer set IDs; empty if there are none.
    """

def create_multi_layer_solid_wall(set_name: str) -> MultiLayerSetId:
    """Create a new solid wall multi layer set.

    A multi layer set is a named build-up that cover elements (walls, floors, roofs) reference by
    ID; the set is stored in the document. The set is created with cover type solid wall and saved
    to the document. The new set has no layers, a cover thickness of 100 mm, the default material
    and cover color 90. Fill the set with `multi_layer_cover_controller.add_layer()` and assign it
    to covers with `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        set_name: Name of the new set; must not be empty. If another set already has this name, '
            (1)', ' (2)' and so on is appended.

    Examples:
        >>> set_id = mlc.create_multi_layer_solid_wall("Standard Solid Wall")
        >>> print(f"Created new multi-layer solid wall with ID: {set_id}")

    Returns:
        ID of the new multi layer set, or 0 if the name is empty.
    """

def get_multi_layer_set_component_type(set_id: MultiLayerSetId) -> int:
    """Get the component type of a multi layer set.

    The component type tells whether the layers of the set are defined by materials or by standard
    elements (see `multi_layer_cover_controller.add_layer_by_standard_elements()`). New sets are
    created with component type material. Change it with
    `multi_layer_cover_controller.set_multi_layer_set_component_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> for set_id in mlc.get_multi_layer_sets():
        ...     name = mlc.get_multi_layer_set_name(set_id)
        ...     component_type = mlc.get_multi_layer_set_component_type(set_id)
        ...     print(name, 'standard elements' if component_type == 2 else 'materials')

    Returns:
        Component type as integer: 1 material, 2 standard element; 0 if the set ID is unknown.
    """

def set_multi_layer_set_component_type(set_id: MultiLayerSetId, type: int) -> None:
    """Set the component type of a multi layer set.

    Switches the set between layers defined by materials and layers defined by standard elements.
    Existing layers are not changed. Nothing happens for an unknown set ID. The change is saved to
    the document. Read it with `multi_layer_cover_controller.get_multi_layer_set_component_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        type: Component type as integer: 1 material, 2 standard element. The value is not validated.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Standard element wall')
        >>> mlc.set_multi_layer_set_component_type(set_id, 2)  # 2 = standard element
        >>> print(mlc.get_multi_layer_set_component_type(set_id))
    """

def get_layer_sub_type(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> int:
    """Get the sub type of a layer in a multi layer set.

    The sub type refines the layer type, for example whether a structure layer is a load-bearing
    frame or a solid structure. Layers are indexed from 0 in stored order. Change it with
    `multi_layer_cover_controller.set_layer_sub_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Sub type demo')
        >>> material_id = mlc.get_cover_material(set_id)
        >>> mlc.add_layer(set_id, 1, 'Frame', material_id, 160.0)
        >>> print(mlc.get_layer_sub_type(set_id, 0))

    Returns:
        Layer sub type as integer (1 load-bearing frame structure, 2 solid structure, 3 straight
        edge, 4 bias edge, 5 vertical, 6 horizontal, 7 air, 8 non-load-bearing frame structure); 0
        if the set ID is unknown, the layer index is out of range or no sub type is set.
    """

def set_layer_sub_type(set_id: MultiLayerSetId, layer_index: UnsignedInt, sub_type: int) -> None:
    """Set the sub type of a layer in a multi layer set.

    The sub type refines the layer type, for example whether a structure layer is a load-bearing
    frame or a solid structure. Nothing happens for an unknown set ID or an out-of-range layer
    index. The change is saved to the document. Read it with
    `multi_layer_cover_controller.get_layer_sub_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        sub_type: Layer sub type as integer: 1 load-bearing frame structure, 2 solid structure, 3
            straight edge, 4 bias edge, 5 vertical, 6 horizontal, 7 air, 8 non-load-bearing frame
            structure. The value is not validated.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Frame wall')
        >>> material_id = mlc.get_cover_material(set_id)
        >>> mlc.add_layer(set_id, 1, 'Frame', material_id, 160.0)
        >>> mlc.set_layer_sub_type(set_id, 0, 1)  # 1 = load-bearing frame structure
        >>> print(mlc.get_layer_sub_type(set_id, 0))
    """

def get_layer_standard_panel_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the GUID of the standard panel used by a layer.

    Layers of a set whose component type is standard element refer to a standard panel from the
    standard element library. Resolve the GUID to a name with
    `element_controller.get_standard_element_name_from_guid()`. Change it with
    `multi_layer_cover_controller.set_layer_standard_panel_guid()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> for set_id in mlc.get_multi_layer_sets():
        ...     for index in range(mlc.get_layer_count(set_id)):
        ...         guid = mlc.get_layer_standard_panel_guid(set_id, index)
        ...         if guid:
        ...             print(index, ec.get_standard_element_name_from_guid(guid))

    Returns:
        GUID as string; empty string if the set ID is unknown or the layer index is out of range. A
        layer without a standard panel returns an empty or null GUID text.
    """

def set_layer_standard_panel_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt, guid: str) -> None:
    """Set the standard panel GUID of a layer.

    Links the layer to a standard panel from the standard element library. The GUID is converted but
    not checked against existing standard elements. Nothing happens for an unknown set ID or an
    out-of-range layer index. The change is saved to the document. Read it with
    `multi_layer_cover_controller.get_layer_standard_panel_guid()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        guid: GUID string of a standard panel, e.g. from
            `element_controller.get_standard_panel_guid_list()`.

    Examples:
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Standard panel wall')
        >>> mlc.add_layer(set_id, 2, 'Sheathing', mlc.get_cover_material(set_id), 18.0)
        >>> panel_guids = ec.get_standard_panel_guid_list()
        >>> if panel_guids:
        ...     mlc.set_layer_standard_panel_guid(set_id, 0, panel_guids[0])
    """

def get_layer_standard_beam_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> str:
    """Get the GUID of the standard beam used by a layer.

    Layers of a set whose component type is standard element refer to a standard beam from the
    standard element library. Resolve the GUID to a name with
    `element_controller.get_standard_element_name_from_guid()`. Change it with
    `multi_layer_cover_controller.set_layer_standard_beam_guid()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> for set_id in mlc.get_multi_layer_sets():
        ...     for index in range(mlc.get_layer_count(set_id)):
        ...         guid = mlc.get_layer_standard_beam_guid(set_id, index)
        ...         if guid:
        ...             print(index, ec.get_standard_element_name_from_guid(guid))

    Returns:
        GUID as string; empty string if the set ID is unknown or the layer index is out of range. A
        layer without a standard beam returns an empty or null GUID text.
    """

def set_layer_standard_beam_guid(set_id: MultiLayerSetId, layer_index: UnsignedInt, guid: str) -> None:
    """Set the standard beam GUID of a layer.

    Links the layer to a standard beam from the standard element library. The GUID is converted but
    not checked against existing standard elements. Nothing happens for an unknown set ID or an
    out-of-range layer index. The change is saved to the document. Read it with
    `multi_layer_cover_controller.get_layer_standard_beam_guid()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer, counted from the first layer; must be smaller
            than `multi_layer_cover_controller.get_layer_count()`.
        guid: GUID string of a standard beam, e.g. from
            `element_controller.get_standard_beam_guid_list()`.

    Examples:
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Standard beam wall')
        >>> mlc.add_layer(set_id, 1, 'Studs', mlc.get_cover_material(set_id), 160.0)
        >>> beam_guids = ec.get_standard_beam_guid_list()
        >>> if beam_guids:
        ...     mlc.set_layer_standard_beam_guid(set_id, 0, beam_guids[0])
    """

def add_layer_by_standard_elements(
    set_id: MultiLayerSetId, type: int, name: str, panel_guid: str, beam_guid: str, thickness: float
) -> None:
    """Append a layer defined by a standard panel and a standard beam.

    The layer is added at the end and the cover thickness of the set becomes the sum of all layer
    thicknesses. A simple wall set is converted to a layered set. The layer has no material; the
    standard elements describe it. The change is saved to the document; covers already using the set
    are not queued for recreation. Nothing happens for an unknown set ID or a thickness of 0 or
    less. Switch the set to standard element layers with
    `multi_layer_cover_controller.set_multi_layer_set_component_type()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        type: Layer type as integer: 1 structure, 2 panel, 3 lathing, 4 air, 5 covering
            (`cadwork.multi_layer_type` members, use `.value`). The value is not validated.
        name: Name of the layer.
        panel_guid: GUID string of a standard panel, e.g. from
            `element_controller.get_standard_panel_guid_list()`.
        beam_guid: GUID string of a standard beam, e.g. from
            `element_controller.get_standard_beam_guid_list()`.
        thickness: Layer thickness in mm; must be greater than 0.

    Examples:
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Standard element wall')
        >>> panel_guids = ec.get_standard_panel_guid_list()
        >>> beam_guids = ec.get_standard_beam_guid_list()
        >>> if panel_guids and beam_guids:
        ...     mlc.add_layer_by_standard_elements(
        ...         set_id, 1, 'Frame', panel_guids[0], beam_guids[0], 160.0
        ...     )
    """

def remove_layer(set_id: MultiLayerSetId, layer_index: UnsignedInt) -> None:
    """Remove one layer from a multi layer set.

    The cover thickness becomes the sum of the remaining layer thicknesses; it stays unchanged if no
    layer remains. The set is saved and covers using it are queued for recreation, which only
    happens while automatic display refresh is on. Nothing happens for an unknown set ID or an
    out-of-range layer index. Remove every layer with
    `multi_layer_cover_controller.remove_all_layers()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        layer_index: Zero-based index of the layer to remove; must be smaller than
            `multi_layer_cover_controller.get_layer_count()`.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Two layer wall')
        >>> material_id = mlc.get_cover_material(set_id)
        >>> mlc.add_layer(set_id, 1, 'Frame', material_id, 160.0)
        >>> mlc.add_layer(set_id, 2, 'Sheathing', material_id, 18.0)
        >>> mlc.remove_layer(set_id, 0)
        >>> print(mlc.get_layer_count(set_id), mlc.get_cover_thickness(set_id))  # 1 18.0
    """

def remove_all_layers(set_id: MultiLayerSetId) -> None:
    """Remove all layers from a multi layer set.

    The set is saved and covers using it are queued for recreation, which only happens while
    automatic display refresh is on. The cover thickness is not reset and keeps its previous value.
    Nothing happens for an unknown set ID or a set that has no layers. The set itself remains; add
    new layers with `multi_layer_cover_controller.add_layer()`.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Temporary wall')
        >>> material_id = mlc.get_cover_material(set_id)
        >>> mlc.add_layer(set_id, 1, 'Frame', material_id, 160.0)
        >>> mlc.remove_all_layers(set_id)
        >>> print(mlc.get_layer_count(set_id))  # 0
    """

def insert_layer(
    set_id: MultiLayerSetId,
    position: UnsignedInt,
    type: int,
    name: str,
    material_id: MaterialId,
    thickness: float,
) -> None:
    """Insert a new layer into a multi layer set at the given position.

    Layers at or behind the position move up by one. The cover thickness becomes the sum of all
    layer thicknesses and a simple wall set is converted to a layered set. The set is saved and
    covers using it are queued for recreation, which only happens while automatic display refresh is
    on. Nothing happens for an unknown set ID or a thickness of 0 or less. Use
    `multi_layer_cover_controller.add_layer()` to append.

    Parameters:
        set_id: ID of a multi layer set, e.g. from
            `multi_layer_cover_controller.get_multi_layer_sets()` or a create function.
        position: Zero-based position the new layer receives; a value at or beyond the layer count
            appends the layer.
        type: Layer type as integer: 1 structure, 2 panel, 3 lathing, 4 air, 5 covering
            (`cadwork.multi_layer_type` members, use `.value`). The value is not validated.
        name: Name of the layer.
        material_id: Material ID, e.g. from `material_controller.get_material_id()`. The ID is not
            validated.
        thickness: Layer thickness in mm; must be greater than 0.

    Examples:
        >>> import multi_layer_cover_controller as mlc

        >>> set_id = mlc.create_multi_layer_wall('Insert demo')
        >>> material_id = mlc.get_cover_material(set_id)
        >>> mlc.add_layer(set_id, 1, 'Frame', material_id, 160.0)
        >>> mlc.insert_layer(set_id, 0, 5, 'Cladding', material_id, 20.0)  # 5 = covering
        >>> print(mlc.get_layer_name(set_id, 0))  # Cladding
    """

def unset_element_multi_layer_set(element_id: ElementId) -> None:
    """Remove the multi layer set assignment from a cover element.

    The element is marked as modified and the display is refreshed if automatic display refresh is
    on. Nothing happens for an invalid element ID or an element that has no set assigned. The set
    itself is not deleted and other covers keep using it. Assign a set again with
    `multi_layer_cover_controller.set_element_multi_layer_set()`.

    Parameters:
        element_id: Element ID of a cover (wall, floor or roof), e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec
        >>> import multi_layer_cover_controller as mlc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> for element_id in element_ids:
        ...     if ac.is_wall(element_id):
        ...         mlc.unset_element_multi_layer_set(element_id)
    """
