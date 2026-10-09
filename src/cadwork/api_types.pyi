from typing import TypeAlias

UnsignedInt: TypeAlias = int
"""Non-negative integer e.g. an index."""

MaterialId: TypeAlias = int
"""Identifier of a material, as returned by `material_controller.create_material` or `material_controller.get_material_id`."""

ColorId: TypeAlias = int
"""Identifier of a cadwork color number."""

EndtypeId: TypeAlias = int
"""Identifier of an end-type, as managed by the `endtype_controller`."""

AxisId: TypeAlias = int
"""Identifier of a connector axis."""

MenuIndex: TypeAlias = int
"""Index of an entry in a menu, as returned by the `menu_controller`."""

ReferenceSide: TypeAlias = int
"""Index of a reference side of an element."""

MultiLayerSetId: TypeAlias = int
"""Identifier of a multi-layer cover set, as managed by the `multi_layer_cover_controller`."""

UserAttributeId: TypeAlias = int
"""Number of a user attribute."""

ElementId: TypeAlias = int
"""Identifier of an element in the current 3D model."""

__all__ = [
    'UnsignedInt',
    'MaterialId',
    'ColorId',
    'EndtypeId',
    'AxisId',
    'MenuIndex',
    'ReferenceSide',
    'MultiLayerSetId',
    'UserAttributeId',
    'ElementId',
]
