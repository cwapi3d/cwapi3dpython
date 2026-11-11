"""Materials and the color-to-material mapping system.

Covers the catalog of materials available in the project — creation,
naming, grouping, and physical/structural properties — and the
mapping table that ties cadwork's color numbers to materials per
element category (beams, panels, drillings, surfaces, nodes,
standard and MEP axes, auxiliaries). Element-level material
*assignment* by name lives in attribute_controller.
"""

from cadwork.api_types import MaterialId, UnsignedInt

def create_material(name: str) -> MaterialId:
    """Create a material with the given name, or return the existing one.

    If a material with this name already exists, its ID is returned and nothing is created. Names
    longer than 30 characters are cut to their first 29 characters.

    Parameters:
        name: Material name.

    Returns:
        ID of the new or already existing material, or 0 if creation failed.
    """

def set_name(material_id: MaterialId, name: str) -> None:
    """Set the name of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        name: New name for the material.
    """

def set_group(material_id: MaterialId, group: str) -> None:
    """Set the group of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        group: Group name.
    """

def set_code(material_id: MaterialId, code: str) -> None:
    """Set the code of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        code: Material code.
    """

def set_modulus_elasticity_1(material_id: MaterialId, modulus_elasticity1: float) -> None:
    """Set the modulus of elasticity 1 of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        modulus_elasticity1: Modulus of elasticity 1. Unit is that of the material table (not
            converted).
    """

def set_modulus_elasticity_2(material_id: MaterialId, modulus_elasticity2: float) -> None:
    """Set the modulus of elasticity 2 of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        modulus_elasticity2: Modulus of elasticity 2. Unit is that of the material table (not
            converted).
    """

def set_modulus_elasticity_3(material_id: MaterialId, modulus_elasticity3: float) -> None:
    """Set the modulus of elasticity 3 of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        modulus_elasticity3: Modulus of elasticity 3. Unit is that of the material table (not
            converted).
    """

def set_shear_modulus_1(material_id: MaterialId, shear_modulus1: float) -> None:
    """Set the shear modulus 1 of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        shear_modulus1: Shear modulus 1. Unit is that of the material table (not converted).
    """

def set_shear_modulus_2(material_id: MaterialId, shear_modulus2: float) -> None:
    """Set the shear modulus 2 of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        shear_modulus2: Shear modulus 2. Unit is that of the material table (not converted).
    """

def set_price(material_id: MaterialId, price: float) -> None:
    """Set the price of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        price: Price per price unit; see set_price_type.
    """

def set_price_type(material_id: MaterialId, price_type: str) -> None:
    """Set the price type of a material.

    Unrecognized values are silently ignored and leave the price type unchanged. Unknown IDs are not
    checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        price_type: Price unit, case-insensitive: m3, m2, m, Piece, kg, bdft, ft2, ft, ft3 or lb.
    """

def set_thermal_conductivity(material_id: MaterialId, thermal_conductivity: float) -> None:
    """Set the thermal conductivity of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        thermal_conductivity: Thermal conductivity value.
    """

def set_heat_capacity(material_id: MaterialId, heat_capacity: float) -> None:
    """Set the heat capacity of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        heat_capacity: Heat capacity value.
    """

def set_u_min(material_id: MaterialId, u_min: float) -> None:
    """Set the minimum U value of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        u_min: Minimum U value.
    """

def set_u_max(material_id: MaterialId, u_max: float) -> None:
    """Set the maximum U value of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        u_max: Maximum U value.
    """

def set_fire_resistance_class(material_id: MaterialId, fire_resistance_class: str) -> None:
    """Set the fire resistance class of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        fire_resistance_class: Fire resistance class text.
    """

def set_smoke_class(material_id: MaterialId, smoke_class: str) -> None:
    """Set the smoke class of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        smoke_class: Smoke class text.
    """

def set_drop_forming_class(material_id: MaterialId, drop_forming_class: str) -> None:
    """Set the drop forming class of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        drop_forming_class: Drop forming class text.
    """

def set_burn_off_rate(material_id: MaterialId, burn_off_rate: float) -> None:
    """Set the burn-off rate of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        burn_off_rate: Burn-off rate value.
    """

def set_weight(material_id: MaterialId, weight: float) -> None:
    """Set the weight of a material.

    Unknown IDs are not checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        weight: Weight value; its unit depends on the weight type, see set_weight_type.
    """

def set_weight_type(material_id: MaterialId, weight_type: str) -> None:
    """Set the weight type of a material.

    Other values are silently ignored and leave the weight type unchanged. Unknown IDs are not
    checked; no error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        weight_type: Weight unit, case-insensitive: None, kNperM3, kNperM2, kNperM or kNperPiece.
    """

def clear_errors() -> None:
    """Clear the stored material API error stack."""

def set_grade(material_id: MaterialId, grade: str) -> None:
    """Set the grade (strength) of a material.

    The grade is part of the full name returned by get_name. Unknown IDs are not checked; no error
    is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        grade: Grade text, e.g. a strength class.
    """

def set_quality(material_id: MaterialId, quality: str) -> None:
    """Set the quality of a material.

    The quality is part of the full name returned by get_name. Unknown IDs are not checked; no error
    is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        quality: Quality text.
    """

def set_composition(material_id: MaterialId, composition: str) -> None:
    """Set the composition of a material.

    The composition is part of the full name returned by get_name. Unknown IDs are not checked; no
    error is raised.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.
        composition: Composition text.
    """

def get_material_id(material_name: str) -> MaterialId:
    """Find a material ID by name.

    No material is created if none matches.

    Parameters:
        material_name: Material name to look up (longer than 30 characters is truncated for the
            lookup).

    Returns:
        Material ID, or 0 if no material with this name exists.
    """

def get_name(material_id: MaterialId) -> str:
    """Get the full name of a material.

    The name is composed of the base name followed by grade, composition and quality when these are
    set, separated by spaces.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Empty string if the material ID does not exist.
    """

def get_group(material_id: MaterialId) -> str:
    """Get the group of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Group name, with surrounding whitespace removed. Empty string if the material ID does not
        exist.
    """

def get_code(material_id: MaterialId) -> str:
    """Get the code of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Material code. Empty string if the material ID does not exist.
    """

def get_modulus_elasticity_1(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 1 of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Value as stored in the material table. -1.0 if the material ID does not exist.
    """

def get_modulus_elasticity_2(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 2 of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Value as stored in the material table. -1.0 if the material ID does not exist.
    """

def get_modulus_elasticity_3(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 3 of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Value as stored in the material table. -1.0 if the material ID does not exist.
    """

def get_shear_modulus_1(material_id: MaterialId) -> float:
    """Get the shear modulus 1 of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Value as stored in the material table. -1.0 if the material ID does not exist.
    """

def get_shear_modulus_2(material_id: MaterialId) -> float:
    """Get the shear modulus 2 of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Value as stored in the material table. -1.0 if the material ID does not exist.
    """

def get_price(material_id: MaterialId) -> float:
    """Get the price of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Price per price unit; see get_price_type. -1.0 if the material ID does not exist.
    """

def get_price_type(material_id: MaterialId) -> str:
    """Get the price type of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        One of m3, m2, m, Piece, kg, bdft, ft2, ft, ft3 or lb. 'None' if no price type is set or the
        material ID does not exist.
    """

def get_thermal_conductivity(material_id: MaterialId) -> float:
    """Get the thermal conductivity of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Thermal conductivity value. -1.0 if the material ID does not exist.
    """

def get_heat_capacity(material_id: MaterialId) -> float:
    """Get the heat capacity of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Heat capacity value. -1.0 if the material ID does not exist.
    """

def get_u_min(material_id: MaterialId) -> float:
    """Get the minimum U value of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Minimum U value. -1.0 if the material ID does not exist.
    """

def get_u_max(material_id: MaterialId) -> float:
    """Get the maximum U value of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Maximum U value. -1.0 if the material ID does not exist.
    """

def get_fire_resistance_class(material_id: MaterialId) -> str:
    """Get the fire resistance class of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Fire resistance class text. Empty string if the material ID does not exist.
    """

def get_smoke_class(material_id: MaterialId) -> str:
    """Get the smoke class of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Smoke class text. Empty string if the material ID does not exist.
    """

def get_drop_forming_class(material_id: MaterialId) -> str:
    """Get the drop forming class of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Drop forming class text. Empty string if the material ID does not exist.
    """

def get_burn_off_rate(material_id: MaterialId) -> float:
    """Get the burn-off rate of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Burn-off rate value. -1.0 if the material ID does not exist.
    """

def get_weight(material_id: MaterialId) -> float:
    """Get the weight of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Weight value; its unit depends on the weight type, see get_weight_type. -1.0 if the material
        ID does not exist.
    """

def get_weight_type(material_id: MaterialId) -> str:
    """Get the weight type of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        One of None, kNperM3, kNperM2, kNperM or kNperPiece. 'None' if no weight type is set or the
        material ID does not exist.
    """

def get_all_materials() -> list[MaterialId]:
    """Get the IDs of all materials in the document.

    Returns:
        List of material IDs; empty list if there are none.
    """

def get_grade(material_id: MaterialId) -> str:
    """Get the grade (strength) of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Grade text. Empty string if the material ID does not exist.
    """

def get_quality(material_id: MaterialId) -> str:
    """Get the quality of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Quality text. Empty string if the material ID does not exist.
    """

def get_composition(material_id: MaterialId) -> str:
    """Get the composition of a material.

    Parameters:
        material_id: Material ID, as returned by create_material, get_material_id or
            get_all_materials.

    Returns:
        Composition text. Empty string if the material ID does not exist.
    """

def get_short_name(material_id: MaterialId) -> str:
    """Get the short (internal) name of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Short name of the material, or an empty string if it has none or the ID is unknown.
    """

def get_all_material_groups() -> list[str]:
    """Get the names of all material groups.

    Names are returned in the current cadwork program language.

    Returns:
        List of material group names.
    """

def get_parent_group(group: str) -> str:
    """Get the name of the parent of a material group.

    Group names are matched in the current cadwork program language.

    Parameters:
        group: Name of the material group.

    Returns:
        Name of the parent group, or an empty string if the group is not found or has no parent.
    """

def get_material_color_assignment_for_nodes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for nodes.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_nodes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for nodes.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_standard_axes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for standard axes.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_standard_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for standard axes.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_drillings(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for drillings.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_drillings(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for drillings.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_mep_axes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for MEP axes.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_mep_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for MEP axes.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_beams(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for beams.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_beams(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for beams.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_panels(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for panels.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_panels(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for panels.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for auxiliary elements.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for auxiliary elements.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_material_color_assignment_for_surfaces(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for surfaces.

    Reads the color-to-material table of the document.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.

    Returns:
        Material ID assigned to the color number, or 0 if none is assigned.
    """

def set_material_color_assignment_for_surfaces(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for surfaces.

    Writes the color-to-material table of the document; other assignments are unchanged. No undo
    step is created and no validation of the IDs is done.

    Parameters:
        color_nb: Color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign.
    """

def get_texture_color(material_id: MaterialId) -> int:
    """Get the texture color of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Color as a packed RGB integer, not a palette number.
    """

def set_texture_color(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Set the texture color of a material.

    At runtime the arguments are positional only and read as (material ID, color), the reverse
    of the order shown in the signature: call `set_texture_color(material_id, color)`.

    Parameters:
        color_nb: Color as a packed RGB integer, not a palette number.
        material_id: Material ID.
    """

def get_texture_transparency(material_id: MaterialId) -> int:
    """Get the texture transparency of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Transparency in percent, 0 means opaque.
    """

def set_texture_transparency(material_id: MaterialId, texture_transparency: UnsignedInt) -> None:
    """Set the texture transparency of a material.

    The value is passed on without clamping.

    Parameters:
        material_id: Material ID.
        texture_transparency: Transparency in percent, 0 means opaque (0-100).
    """

def get_texture_rotation_angle(material_id: MaterialId) -> float:
    """Get the texture rotation angle of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Rotation angle of the texture, as stored in the material.
    """

def set_texture_rotation_angle(material_id: MaterialId, angle: float) -> None:
    """Set the texture rotation angle of a material.

    Parameters:
        material_id: Material ID.
        angle: Rotation angle of the texture, stored unchanged.
    """

def get_texture_length_alignment(material_id: MaterialId) -> bool:
    """Check whether random texture placement is enabled for a material.

    Parameters:
        material_id: Material ID.

    Returns:
        True if random placement of the texture is enabled, False otherwise.
    """

def set_texture_length_alignment(material_id: MaterialId, flag: bool) -> None:
    """Enable or disable random texture placement for a material.

    Parameters:
        material_id: Material ID.
        flag: True to enable random placement of the texture, False to disable it.
    """

def get_texture_zoom_x(material_id: MaterialId) -> float:
    """Get the texture zoom factor in the X direction of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Zoom factor of the texture in the X direction.
    """

def set_texture_zoom_x(material_id: MaterialId, value: float) -> None:
    """Set the texture zoom factor in the X direction of a material.

    Parameters:
        material_id: Material ID.
        value: Zoom factor in the X direction.
    """

def get_texture_zoom_y(material_id: MaterialId) -> float:
    """Get the texture zoom factor in the Y direction of a material.

    Parameters:
        material_id: Material ID.

    Returns:
        Zoom factor of the texture in the Y direction.
    """

def set_texture_zoom_y(material_id: MaterialId, value: float) -> None:
    """Set the texture zoom factor in the Y direction of a material.

    Parameters:
        material_id: Material ID.
        value: Zoom factor in the Y direction.
    """
