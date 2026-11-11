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

    Materials are the entries of the material catalog that elements get assigned to. If a material
    with this name already exists, its ID is returned and nothing is created, so the call is safe to
    repeat. Names longer than 30 characters are cut to their first 29 characters before the lookup
    and before storing. The new material starts with only its name; fill in the other properties
    with the `set_*` functions of this module.

    Parameters:
        name: Name of the material, at most 30 characters (longer names are cut to 29). Matched
            against existing material names, so reuse the exact name to get the existing ID.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.create_material('Spruce C24')
        >>> if material_id:
        ...     mtc.set_grade(material_id, 'C24')
        ...     mtc.set_price_type(material_id, 'm3')
        ...     mtc.set_price(material_id, 450.0)

    Returns:
        ID of the new or already existing material.
    """

def set_name(material_id: MaterialId, name: str) -> None:
    """Set the base name of a material.

    Replaces the base name of the material. The full name returned by
    `material_controller.get_name()` is this base name followed by grade, composition and quality
    when those are set. The name is stored as given: unlike `material_controller.create_material()`
    it is not shortened. An unknown material ID is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        name: New base name, without grade, composition or quality.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> if material_id:
        ...     mtc.set_name(material_id, 'Spruce')
        ...     print(mtc.get_name(material_id))
    """

def set_group(material_id: MaterialId, group: str) -> None:
    """Assign a material to a material group.

    Material groups (e.g. timber, insulation) organise the catalog. The group is looked up by name
    and created if it does not exist; trailing blanks in the name are removed and an empty string
    assigns the empty group. Only a material that has no group yet is changed: if the material
    already belongs to a group the call does nothing, so an existing group cannot be replaced with
    this function. Read the result back with `material_controller.get_group()`; list known groups
    with `material_controller.get_all_material_groups()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        group: Group name, e.g. one of `material_controller.get_all_material_groups()`. A name that
            does not exist yet creates a new group.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.create_material('Mineral wool 035')
        >>> mtc.set_group(material_id, 'Insulation')
        >>> print(mtc.get_group(material_id))
    """

def set_code(material_id: MaterialId, code: str) -> None:
    """Set the code of a material.

    The code is a free text identifier stored with the material, for example an article number. It
    is stored as given and does not affect the material name. Read it back with
    `material_controller.get_code()`. An unknown material ID is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        code: Code text, stored unchanged.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_code(material_id, 'KVH-001')
        >>> print(mtc.get_code(material_id))
    """

def set_modulus_elasticity_1(material_id: MaterialId, modulus_elasticity1: float) -> None:
    """Set the modulus of elasticity 1 of a material.

    Stores the modulus of elasticity 1 in the material catalog. The API does not convert the value:
    pass it in the unit your cadwork material table uses. The value is stored in single precision,
    so it is read back rounded to about 7 significant digits. Read it back with
    `material_controller.get_modulus_elasticity_1()`. An unknown material ID is not checked and
    nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        modulus_elasticity1: The modulus of elasticity 1, in the unit of the material table.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_modulus_elasticity_1(material_id, 11000.0)
        >>> print(mtc.get_modulus_elasticity_1(material_id))
    """

def set_modulus_elasticity_2(material_id: MaterialId, modulus_elasticity2: float) -> None:
    """Set the modulus of elasticity 2 of a material.

    Stores the modulus of elasticity 2 in the material catalog. The API does not convert the value:
    pass it in the unit your cadwork material table uses. The value is stored in single precision,
    so it is read back rounded to about 7 significant digits. Read it back with
    `material_controller.get_modulus_elasticity_2()`. An unknown material ID is not checked and
    nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        modulus_elasticity2: The modulus of elasticity 2, in the unit of the material table.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_modulus_elasticity_2(material_id, 11000.0)
        >>> print(mtc.get_modulus_elasticity_2(material_id))
    """

def set_modulus_elasticity_3(material_id: MaterialId, modulus_elasticity3: float) -> None:
    """Set the modulus of elasticity 3 of a material.

    Stores the modulus of elasticity 3 in the material catalog. The API does not convert the value:
    pass it in the unit your cadwork material table uses. The value is stored in single precision,
    so it is read back rounded to about 7 significant digits. Read it back with
    `material_controller.get_modulus_elasticity_3()`. An unknown material ID is not checked and
    nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        modulus_elasticity3: The modulus of elasticity 3, in the unit of the material table.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_modulus_elasticity_3(material_id, 11000.0)
        >>> print(mtc.get_modulus_elasticity_3(material_id))
    """

def set_shear_modulus_1(material_id: MaterialId, shear_modulus1: float) -> None:
    """Set the shear modulus 1 of a material.

    Stores the shear modulus 1 in the material catalog. The API does not convert the value: pass it
    in the unit your cadwork material table uses. The value is stored in single precision, so it is
    read back rounded to about 7 significant digits. Read it back with
    `material_controller.get_shear_modulus_1()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        shear_modulus1: The shear modulus 1, in the unit of the material table.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_shear_modulus_1(material_id, 11000.0)
        >>> print(mtc.get_shear_modulus_1(material_id))
    """

def set_shear_modulus_2(material_id: MaterialId, shear_modulus2: float) -> None:
    """Set the shear modulus 2 of a material.

    Stores the shear modulus 2 in the material catalog. The API does not convert the value: pass it
    in the unit your cadwork material table uses. The value is stored in single precision, so it is
    read back rounded to about 7 significant digits. Read it back with
    `material_controller.get_shear_modulus_2()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        shear_modulus2: The shear modulus 2, in the unit of the material table.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_shear_modulus_2(material_id, 11000.0)
        >>> print(mtc.get_shear_modulus_2(material_id))
    """

def set_price(material_id: MaterialId, price: float) -> None:
    """Set the price of a material.

    The price refers to the unit set with `material_controller.set_price_type()`, for example price
    per m3 or per kg. No currency is stored with it. Set the price type as well, otherwise the price
    has no defined unit. Read it back with `material_controller.get_price()`. An unknown material ID
    is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        price: Price per price unit, as a plain number.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_price_type(material_id, 'm3')
        >>> mtc.set_price(material_id, 450.0)
    """

def set_price_type(material_id: MaterialId, price_type: str) -> None:
    """Set the unit that the price of a material refers to.

    Selects the price unit, for example m3 for a price per cubic metre. The comparison is
    case-insensitive. A value that is not in the list is silently ignored and the previous price
    type is kept. Set it together with `material_controller.set_price()`; read it back with
    `material_controller.get_price_type()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        price_type: One of m3, m2, m, Piece, kg, bdft, ft2, ft, ft3 or lb (case-insensitive).
            'Piece' means price per piece.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_price_type(material_id, 'm3')
        >>> print(mtc.get_price_type(material_id))
    """

def set_thermal_conductivity(material_id: MaterialId, thermal_conductivity: float) -> None:
    """Set the thermal conductivity of a material.

    Stores the thermal conductivity of the material. Read it back with
    `material_controller.get_thermal_conductivity()`. An unknown material ID is not checked and
    nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        thermal_conductivity: The thermal conductivity, as a plain number; not converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_thermal_conductivity(material_id, 0.13)
        >>> print(mtc.get_thermal_conductivity(material_id))
    """

def set_heat_capacity(material_id: MaterialId, heat_capacity: float) -> None:
    """Set the heat capacity of a material.

    Stores the heat capacity of the material. Read it back with
    `material_controller.get_heat_capacity()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        heat_capacity: The heat capacity, as a plain number; not converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_heat_capacity(material_id, 1600.0)
        >>> print(mtc.get_heat_capacity(material_id))
    """

def set_u_min(material_id: MaterialId, u_min: float) -> None:
    """Set the minimum U value of a material.

    Stores the lower U value (thermal transmittance) of the material. Read it back with
    `material_controller.get_u_min()`. An unknown material ID is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        u_min: The minimum U value, as a plain number; not converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_u_min(material_id, 0.15)
        >>> print(mtc.get_u_min(material_id))
    """

def set_u_max(material_id: MaterialId, u_max: float) -> None:
    """Set the maximum U value of a material.

    Stores the upper U value (thermal transmittance) of the material. Read it back with
    `material_controller.get_u_max()`. An unknown material ID is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        u_max: The maximum U value, as a plain number; not converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_u_max(material_id, 0.35)
        >>> print(mtc.get_u_max(material_id))
    """

def set_fire_resistance_class(material_id: MaterialId, fire_resistance_class: str) -> None:
    """Set the fire resistance class of a material.

    Stores the fire resistance class as free text, exactly as given; the text is not validated. Read
    it back with `material_controller.get_fire_resistance_class()`. An unknown material ID is not
    checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        fire_resistance_class: Fire resistance class text, e.g. 'D-s2,d0'.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_fire_resistance_class(material_id, 'D-s2,d0')
        >>> print(mtc.get_fire_resistance_class(material_id))
    """

def set_smoke_class(material_id: MaterialId, smoke_class: str) -> None:
    """Set the smoke class of a material.

    Stores the smoke class as free text, exactly as given; the text is not validated. Read it back
    with `material_controller.get_smoke_class()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        smoke_class: Smoke class text, e.g. 's2'.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_smoke_class(material_id, 's2')
        >>> print(mtc.get_smoke_class(material_id))
    """

def set_drop_forming_class(material_id: MaterialId, drop_forming_class: str) -> None:
    """Set the drop forming class of a material.

    Stores the drop forming class as free text, exactly as given; the text is not validated. Read it
    back with `material_controller.get_drop_forming_class()`. An unknown material ID is not checked
    and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        drop_forming_class: Drop forming class text, e.g. 'd0'.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_drop_forming_class(material_id, 'd0')
        >>> print(mtc.get_drop_forming_class(material_id))
    """

def set_burn_off_rate(material_id: MaterialId, burn_off_rate: float) -> None:
    """Set the burn-off rate of a material.

    Stores the burn-off rate (rate at which the material burns away in a fire) of the material. Read
    it back with `material_controller.get_burn_off_rate()`. An unknown material ID is not checked
    and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        burn_off_rate: The burn-off rate, as a plain number; not converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_burn_off_rate(material_id, 0.7)
        >>> print(mtc.get_burn_off_rate(material_id))
    """

def set_weight(material_id: MaterialId, weight: float) -> None:
    """Set the weight value of a material.

    The value is interpreted according to the weight type set with
    `material_controller.set_weight_type()`, for example per volume, per area or per piece. Set both
    together. The value is stored in single precision, so it is read back rounded to about 7
    significant digits. Read it back with `material_controller.get_weight()`. An unknown material ID
    is not checked and nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        weight: Weight value in the unit of the weight type (kN per m3, m2, m or piece); not
            converted by the API.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_weight_type(material_id, 'kNperM3')
        >>> mtc.set_weight(material_id, 4.2)
        >>> print(mtc.get_weight(material_id))
    """

def set_weight_type(material_id: MaterialId, weight_type: str) -> None:
    """Set the unit that the weight value of a material refers to.

    Selects whether the weight is given per volume, per area, per length or per piece. The
    comparison is case-insensitive. A value that is not in the list is silently ignored and the
    previous weight type is kept. Set it together with `material_controller.set_weight()`; read it
    back with `material_controller.get_weight_type()`. An unknown material ID is not checked and
    nothing happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        weight_type: One of None, kNperM3, kNperM2, kNperM or kNperPiece (case-insensitive): no
            weight, kN per m3, per m2, per m or per piece.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> mtc.set_weight_type(material_id, 'kNperM3')
        >>> print(mtc.get_weight_type(material_id))
    """

def clear_errors() -> None:
    """Clear the stored error messages of the material API.

    Empties the list of pending error messages collected by the material API. It does not change any
    material, and no other function in this module reads that list, so a script normally has no need
    to call it.

    Examples:
        >>> import material_controller as mtc

        >>> mtc.clear_errors()
    """

def set_grade(material_id: MaterialId, grade: str) -> None:
    """Set the grade (strength) of a material.

    Stores the grade (strength) as free text. It is appended to the base name, so it changes the
    full name returned by `material_controller.get_name()` and the name that
    `material_controller.get_material_id()` matches. The full name is the base name followed by
    grade, composition and quality, separated by spaces, with empty parts left out. Read it back
    with `material_controller.get_grade()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        grade: Grade text, e.g. a strength class such as 'C24' or 'GL24h'.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.create_material('Spruce')
        >>> mtc.set_grade(material_id, 'C24')
        >>> print(mtc.get_name(material_id))
    """

def set_quality(material_id: MaterialId, quality: str) -> None:
    """Set the quality of a material.

    Stores the quality as free text. It is appended to the base name, so it changes the full name
    returned by `material_controller.get_name()` and the name that
    `material_controller.get_material_id()` matches. The full name is the base name followed by
    grade, composition and quality, separated by spaces, with empty parts left out. Read it back
    with `material_controller.get_quality()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        quality: Quality text, e.g. a sorting or surface quality.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.create_material('Spruce')
        >>> mtc.set_quality(material_id, 'IV')
        >>> print(mtc.get_name(material_id))
    """

def set_composition(material_id: MaterialId, composition: str) -> None:
    """Set the composition of a material.

    Stores the composition as free text. It is appended to the base name, so it changes the full
    name returned by `material_controller.get_name()` and the name that
    `material_controller.get_material_id()` matches. The full name is the base name followed by
    grade, composition and quality, separated by spaces, with empty parts left out. Read it back
    with `material_controller.get_composition()`. An unknown material ID is not checked and nothing
    happens.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.
        composition: Composition text, e.g. a build-up or construction description.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.create_material('Spruce')
        >>> mtc.set_composition(material_id, 'BSH')
        >>> print(mtc.get_name(material_id))
    """

def get_material_id(material_name: str) -> MaterialId:
    """Find the ID of a material by its name.

    Looks the material up by name and creates nothing, so it is the check to run before
    `material_controller.create_material()` if you only want existing materials. The name is matched
    against the full name (base name plus grade, composition and quality, see
    `material_controller.get_name()`) and against the base name. Names longer than 30 characters are
    cut to their first 29 characters for the database lookup. Use the ID with the other functions of
    this module or with `attribute_controller.set_element_material()`.

    Parameters:
        material_name: Name of the material, e.g. 'Spruce C24'.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> if material_id == 0:
        ...     material_id = mtc.create_material('Spruce C24')

    Returns:
        Material ID, or 0 if no material with this name exists.
    """

def get_name(material_id: MaterialId) -> str:
    """Get the full name of a material.

    The full name is the base name followed by grade, composition and quality, separated by spaces;
    parts that are not set are left out. This is the name `material_controller.get_material_id()`
    matches. Use `material_controller.get_short_name()` for the base name alone. Set the parts with
    `material_controller.set_name()`, `material_controller.set_grade()`,
    `material_controller.set_composition()` and `material_controller.set_quality()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> for material_id in mtc.get_all_materials():
        ...     print(material_id, mtc.get_name(material_id))

    Returns:
        Full name of the material, or an empty string if the material ID does not exist.
    """

def get_group(material_id: MaterialId) -> str:
    """Get the name of the group a material belongs to.

    Material groups organise the material catalog, for example by material family. Assign a group
    with `material_controller.set_group()`; list all groups with
    `material_controller.get_all_material_groups()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> print(mtc.get_group(material_id))

    Returns:
        Group name with surrounding whitespace removed, or an empty string if the material has no
        group or the material ID does not exist.
    """

def get_code(material_id: MaterialId) -> str:
    """Get the code of a material.

    The code is the free text identifier stored with the material. Set it with
    `material_controller.set_code()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> print(mtc.get_code(material_id))

    Returns:
        Code text, or an empty string if no code is set or the material ID does not exist.
    """

def get_modulus_elasticity_1(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 1 of a material.

    Returns the modulus of elasticity 1 as stored in the material catalog, without unit conversion.
    The value is held in single precision, so it can differ slightly from the number passed to the
    setter. Set it with `material_controller.set_modulus_elasticity_1()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_modulus_elasticity_1(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The modulus of elasticity 1, in the unit of the material table. -1.0 if the material ID does
        not exist.
    """

def get_modulus_elasticity_2(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 2 of a material.

    Returns the modulus of elasticity 2 as stored in the material catalog, without unit conversion.
    The value is held in single precision, so it can differ slightly from the number passed to the
    setter. Set it with `material_controller.set_modulus_elasticity_2()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_modulus_elasticity_2(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The modulus of elasticity 2, in the unit of the material table. -1.0 if the material ID does
        not exist.
    """

def get_modulus_elasticity_3(material_id: MaterialId) -> float:
    """Get the modulus of elasticity 3 of a material.

    Returns the modulus of elasticity 3 as stored in the material catalog, without unit conversion.
    The value is held in single precision, so it can differ slightly from the number passed to the
    setter. Set it with `material_controller.set_modulus_elasticity_3()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_modulus_elasticity_3(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The modulus of elasticity 3, in the unit of the material table. -1.0 if the material ID does
        not exist.
    """

def get_shear_modulus_1(material_id: MaterialId) -> float:
    """Get the shear modulus 1 of a material.

    Returns the shear modulus 1 as stored in the material catalog, without unit conversion. The
    value is held in single precision, so it can differ slightly from the number passed to the
    setter. Set it with `material_controller.set_shear_modulus_1()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_shear_modulus_1(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The shear modulus 1, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_shear_modulus_2(material_id: MaterialId) -> float:
    """Get the shear modulus 2 of a material.

    Returns the shear modulus 2 as stored in the material catalog, without unit conversion. The
    value is held in single precision, so it can differ slightly from the number passed to the
    setter. Set it with `material_controller.set_shear_modulus_2()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_shear_modulus_2(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The shear modulus 2, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_price(material_id: MaterialId) -> float:
    """Get the price of a material.

    The price refers to the unit returned by `material_controller.get_price_type()`. Set it with
    `material_controller.set_price()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> price = mtc.get_price(material_id)
        >>> print(price, 'per', mtc.get_price_type(material_id))

    Returns:
        Price per price unit. -1.0 if the material ID does not exist.
    """

def get_price_type(material_id: MaterialId) -> str:
    """Get the unit that the price of a material refers to.

    Tells you how to read the value from `material_controller.get_price()`, for example m3 for a
    price per cubic metre. Set it with `material_controller.set_price_type()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> if mtc.get_price_type(material_id) == 'None':
        ...     print('no price unit set')

    Returns:
        One of m3, m2, m, Piece, kg, bdft, ft2, ft, ft3 or lb. 'None' (the text) if no price type is
        set or the material ID does not exist.
    """

def get_thermal_conductivity(material_id: MaterialId) -> float:
    """Get the thermal conductivity of a material.

    Returns the thermal conductivity as stored in the material catalog, without unit conversion. Set
    it with `material_controller.set_thermal_conductivity()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_thermal_conductivity(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The thermal conductivity, in the unit of the material table. -1.0 if the material ID does
        not exist.
    """

def get_heat_capacity(material_id: MaterialId) -> float:
    """Get the heat capacity of a material.

    Returns the heat capacity as stored in the material catalog, without unit conversion. Set it
    with `material_controller.set_heat_capacity()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_heat_capacity(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The heat capacity, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_u_min(material_id: MaterialId) -> float:
    """Get the minimum U value of a material.

    Returns the minimum U value as stored in the material catalog, without unit conversion. Set it
    with `material_controller.set_u_min()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_u_min(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The minimum U value, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_u_max(material_id: MaterialId) -> float:
    """Get the maximum U value of a material.

    Returns the maximum U value as stored in the material catalog, without unit conversion. Set it
    with `material_controller.set_u_max()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_u_max(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The maximum U value, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_fire_resistance_class(material_id: MaterialId) -> str:
    """Get the fire resistance class of a material.

    Returns the fire resistance class text stored with the material. Set it with
    `material_controller.set_fire_resistance_class()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_fire_resistance_class(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The fire resistance class text, or an empty string if none is set or the material ID does
        not exist.
    """

def get_smoke_class(material_id: MaterialId) -> str:
    """Get the smoke class of a material.

    Returns the smoke class text stored with the material. Set it with
    `material_controller.set_smoke_class()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_smoke_class(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The smoke class text, or an empty string if none is set or the material ID does not exist.
    """

def get_drop_forming_class(material_id: MaterialId) -> str:
    """Get the drop forming class of a material.

    Returns the drop forming class text stored with the material. Set it with
    `material_controller.set_drop_forming_class()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_drop_forming_class(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The drop forming class text, or an empty string if none is set or the material ID does not
        exist.
    """

def get_burn_off_rate(material_id: MaterialId) -> float:
    """Get the burn-off rate of a material.

    Returns the burn-off rate as stored in the material catalog, without unit conversion. Set it
    with `material_controller.set_burn_off_rate()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_burn_off_rate(material_id)
        >>> if value >= 0:
        ...     print(value)

    Returns:
        The burn-off rate, in the unit of the material table. -1.0 if the material ID does not
        exist.
    """

def get_weight(material_id: MaterialId) -> float:
    """Get the weight value of a material.

    The unit depends on the weight type returned by `material_controller.get_weight_type()`, for
    example kN per m3. The value is held in single precision, so it can differ slightly from the
    number passed to the setter. Set it with `material_controller.set_weight()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> weight = mtc.get_weight(material_id)
        >>> print(weight, mtc.get_weight_type(material_id))

    Returns:
        Weight value in the unit of the weight type. -1.0 if the material ID does not exist.
    """

def get_weight_type(material_id: MaterialId) -> str:
    """Get the unit that the weight value of a material refers to.

    Tells you how to read the value from `material_controller.get_weight()`: per volume, area,
    length or piece. Set it with `material_controller.set_weight_type()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> print(mtc.get_weight_type(material_id))

    Returns:
        One of None, kNperM3, kNperM2, kNperM or kNperPiece. 'None' (the text) if no weight type is
        set or the material ID does not exist.
    """

def get_all_materials() -> list[MaterialId]:
    """Get the IDs of all materials in the catalog.

    Includes every material, not only those used by elements. The list is sorted by name in natural
    order (ascending), where the name is the full name from `material_controller.get_name()`. Use
    the IDs with the other functions of this module.

    Examples:
        >>> import material_controller as mtc

        >>> for material_id in mtc.get_all_materials():
        ...     print(material_id, mtc.get_name(material_id), mtc.get_group(material_id))

    Returns:
        List of material IDs sorted by full name; empty list if there are none.
    """

def get_grade(material_id: MaterialId) -> str:
    """Get the grade (strength) of a material.

    Returns the grade (strength) text stored with the material. It is also part of the full name
    returned by `material_controller.get_name()`. Set it with `material_controller.set_grade()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_grade(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The grade (strength) text, or an empty string if none is set or the material ID does not
        exist.
    """

def get_quality(material_id: MaterialId) -> str:
    """Get the quality of a material.

    Returns the quality text stored with the material. It is also part of the full name returned by
    `material_controller.get_name()`. Set it with `material_controller.set_quality()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_quality(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The quality text, or an empty string if none is set or the material ID does not exist.
    """

def get_composition(material_id: MaterialId) -> str:
    """Get the composition of a material.

    Returns the composition text stored with the material. It is also part of the full name returned
    by `material_controller.get_name()`. Set it with `material_controller.set_composition()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()`,
            `material_controller.create_material()` or `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce C24')
        >>> value = mtc.get_composition(material_id)
        >>> if value:
        ...     print(value)

    Returns:
        The composition text, or an empty string if none is set or the material ID does not exist.
    """

def get_short_name(material_id: MaterialId) -> str:
    """Get the short (internal) name of a material.

    Returns the short internal name stored for the material, as opposed to its display name from
    `material_controller.get_name()`. An unknown material ID gives an empty string.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> print(mtc.get_short_name(material_id))

    Returns:
        Short name of the material, or an empty string if it has none or the ID is unknown.
    """

def get_all_material_groups() -> list[str]:
    """Get the names of all material groups.

    Material groups organize the materials of the database, e.g. the group read with
    `material_controller.get_group()`. Names are returned in the cadwork program language currently
    in use, so they differ between language settings. Use a name with
    `material_controller.get_parent_group()`.

    Examples:
        >>> import material_controller as mtc

        >>> for group in mtc.get_all_material_groups():
        ...     print(group)

    Returns:
        List of material group names.
    """

def get_parent_group(group: str) -> str:
    """Get the name of the parent of a material group.

    Material groups form a hierarchy. The group name is matched in the current cadwork program
    language and the parent name is returned in the same language. Valid names come from
    `material_controller.get_all_material_groups()`.

    Parameters:
        group: Name of a material group in the current cadwork language, e.g. from
            `material_controller.get_all_material_groups()`.

    Examples:
        >>> import material_controller as mtc

        >>> for group in mtc.get_all_material_groups():
        ...     parent = mtc.get_parent_group(group)
        ...     print(group, '->', parent or '(top level)')

    Returns:
        Name of the parent group, or an empty string if the group is not found or has no parent.
    """

def get_material_color_assignment_for_nodes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for nodes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category nodes (points). Nothing is
    modified. Change the assignment with
    `material_controller.set_material_color_assignment_for_nodes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_nodes(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_nodes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for nodes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category nodes (points); all other
    assignments stay unchanged. The IDs are not validated and no undo step is created. Read the
    value back with `material_controller.get_material_color_assignment_for_nodes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_nodes(3, material_id)
    """

def get_material_color_assignment_for_standard_axes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for standard axes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category standard axes. Nothing is
    modified. Change the assignment with
    `material_controller.set_material_color_assignment_for_standard_axes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_standard_axes(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_standard_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for standard axes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category standard axes; all other
    assignments stay unchanged. The IDs are not validated and no undo step is created. Read the
    value back with `material_controller.get_material_color_assignment_for_standard_axes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_standard_axes(3, material_id)
    """

def get_material_color_assignment_for_drillings(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for drillings.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category drilling (bolt) axes. Nothing
    is modified. Change the assignment with
    `material_controller.set_material_color_assignment_for_drillings()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_drillings(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_drillings(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for drillings.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category drilling (bolt) axes; all
    other assignments stay unchanged. The IDs are not validated and no undo step is created. Read
    the value back with `material_controller.get_material_color_assignment_for_drillings()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_drillings(3, material_id)
    """

def get_material_color_assignment_for_mep_axes(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for MEP axes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category MEP axes. Nothing is modified.
    Change the assignment with `material_controller.set_material_color_assignment_for_mep_axes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_mep_axes(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_mep_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for MEP axes.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category MEP axes; all other
    assignments stay unchanged. The IDs are not validated and no undo step is created. Read the
    value back with `material_controller.get_material_color_assignment_for_mep_axes()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_mep_axes(3, material_id)
    """

def get_material_color_assignment_for_beams(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for beams.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category beams. Nothing is modified.
    Change the assignment with `material_controller.set_material_color_assignment_for_beams()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_beams(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_beams(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for beams.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category beams; all other assignments
    stay unchanged. The IDs are not validated and no undo step is created. Read the value back with
    `material_controller.get_material_color_assignment_for_beams()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_beams(3, material_id)
    """

def get_material_color_assignment_for_panels(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for panels.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category panels. Nothing is modified.
    Change the assignment with `material_controller.set_material_color_assignment_for_panels()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_panels(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_panels(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for panels.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category panels; all other assignments
    stay unchanged. The IDs are not validated and no undo step is created. Read the value back with
    `material_controller.get_material_color_assignment_for_panels()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_panels(3, material_id)
    """

def get_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for auxiliary elements.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category auxiliary elements. Nothing is
    modified. Change the assignment with
    `material_controller.set_material_color_assignment_for_auxiliary_elements()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_auxiliary_elements(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for auxiliary elements.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category auxiliary elements; all other
    assignments stay unchanged. The IDs are not validated and no undo step is created. Read the
    value back with `material_controller.get_material_color_assignment_for_auxiliary_elements()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_auxiliary_elements(3, material_id)
    """

def get_material_color_assignment_for_surfaces(color_nb: UnsignedInt) -> MaterialId:
    """Get the material assigned to a color number for surfaces.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This reads the entry for the category surfaces. Nothing is modified.
    Change the assignment with `material_controller.set_material_color_assignment_for_surfaces()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_color_assignment_for_surfaces(3)
        >>> if material_id:
        ...     print(mtc.get_name(material_id))
        ... else:
        ...     print('No material assigned to color 3')

    Returns:
        Material ID assigned to the color number, or 0 if no material is assigned.
    """

def set_material_color_assignment_for_surfaces(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Assign a material to a color number for surfaces.

    The document keeps a color-to-material table per element category, which links each cadwork
    color number to a material. This writes the entry for the category surfaces; all other
    assignments stay unchanged. The IDs are not validated and no undo step is created. Read the
    value back with `material_controller.get_material_color_assignment_for_surfaces()`.

    Parameters:
        color_nb: cadwork color number (palette index, 1-255). Not range-checked.
        material_id: Material ID to assign, e.g. from `material_controller.get_material_id()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if material_id:
        ...     mtc.set_material_color_assignment_for_surfaces(3, material_id)
    """

def get_texture_color(material_id: MaterialId) -> int:
    """Get the texture color of a material.

    The texture color is a property of the material's texture. It is a property of the material in
    the document, not of single elements. Change it with `material_controller.set_texture_color()`.
    An unknown material ID is not reported as an error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> value = mtc.get_texture_color(material_id)
        >>> print(value)

    Returns:
        Color as a packed RGB integer (not a cadwork palette number).
    """

def set_texture_color(material_id: MaterialId, color: int) -> None:
    """Set the texture color of a material.

    The texture color is a property of the material's texture. It is stored on the material in the
    document, so it applies to every element that uses the material. The value is stored unchanged.
    Read it back with `material_controller.get_texture_color()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        color: Color as a packed RGB integer (red, green and blue combined into one int, not a
            palette number). Use the format returned by `material_controller.get_texture_color()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_color(material_id, 0xB5651D)
        >>> print(mtc.get_texture_color(material_id))
    """

def get_texture_transparency(material_id: MaterialId) -> int:
    """Get the texture transparency of a material.

    The texture transparency controls how see-through the material's texture is. It is a property of
    the material in the document, not of single elements. Change it with
    `material_controller.set_texture_transparency()`. An unknown material ID is not reported as an
    error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> value = mtc.get_texture_transparency(material_id)
        >>> print(value)

    Returns:
        Transparency in percent, 0 means opaque.
    """

def set_texture_transparency(material_id: MaterialId, texture_transparency: UnsignedInt) -> None:
    """Set the texture transparency of a material.

    The texture transparency controls how see-through the material's texture is. It is stored on the
    material in the document, so it applies to every element that uses the material. The value is
    stored unchanged. Read it back with `material_controller.get_texture_transparency()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        texture_transparency: Transparency in percent, 0 means opaque (0-100). Values outside this
            range are not clamped.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_transparency(material_id, 30)
        >>> print(mtc.get_texture_transparency(material_id))
    """

def get_texture_rotation_angle(material_id: MaterialId) -> float:
    """Get the texture rotation angle of a material.

    The rotation angle turns the texture image of the material. It is a property of the material in
    the document, not of single elements. Change it with
    `material_controller.set_texture_rotation_angle()`. An unknown material ID is not reported as an
    error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> value = mtc.get_texture_rotation_angle(material_id)
        >>> print(value)

    Returns:
        Rotation angle of the texture, exactly as stored in the material.
    """

def set_texture_rotation_angle(material_id: MaterialId, angle: float) -> None:
    """Set the texture rotation angle of a material.

    The rotation angle turns the texture image of the material. It is stored on the material in the
    document, so it applies to every element that uses the material. The value is stored unchanged.
    Read it back with `material_controller.get_texture_rotation_angle()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        angle: Rotation angle of the texture. Stored without any conversion.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_rotation_angle(material_id, 90.0)
        >>> print(mtc.get_texture_rotation_angle(material_id))
    """

def get_texture_length_alignment(material_id: MaterialId) -> bool:
    """Check whether random texture placement is enabled for a material.

    This flag is the random placement option of the material's texture. It is a property of the
    material in the document, not of single elements. Change it with
    `material_controller.set_texture_length_alignment()`. An unknown material ID is not reported as
    an error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> if mtc.get_texture_length_alignment(material_id):
        ...     print('Random texture placement is on')

    Returns:
        True if random placement of the texture is enabled, False otherwise.
    """

def set_texture_length_alignment(material_id: MaterialId, flag: bool) -> None:
    """Enable or disable random texture placement for a material.

    This flag is the random placement option of the material's texture. It is stored on the material
    in the document, so it applies to every element that uses the material. The value is stored
    unchanged. Read it back with `material_controller.get_texture_length_alignment()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        flag: True to enable random placement of the texture, False to disable it.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_length_alignment(material_id, True)
        >>> print(mtc.get_texture_length_alignment(material_id))
    """

def get_texture_zoom_x(material_id: MaterialId) -> float:
    """Get the texture zoom factor in X of a material.

    The zoom factor scales the texture image of the material in its X direction. It is a property of
    the material in the document, not of single elements. Change it with
    `material_controller.set_texture_zoom_x()`. An unknown material ID is not reported as an error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> value = mtc.get_texture_zoom_x(material_id)
        >>> print(value)

    Returns:
        Zoom factor of the texture in the X direction.
    """

def set_texture_zoom_x(material_id: MaterialId, value: float) -> None:
    """Set the texture zoom factor in X of a material.

    The zoom factor scales the texture image of the material in its X direction. It is stored on the
    material in the document, so it applies to every element that uses the material. The value is
    stored unchanged. Read it back with `material_controller.get_texture_zoom_x()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        value: Zoom factor in the X direction.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_zoom_x(material_id, 1.5)
        >>> print(mtc.get_texture_zoom_x(material_id))
    """

def get_texture_zoom_y(material_id: MaterialId) -> float:
    """Get the texture zoom factor in Y of a material.

    The zoom factor scales the texture image of the material in its Y direction. It is a property of
    the material in the document, not of single elements. Change it with
    `material_controller.set_texture_zoom_y()`. An unknown material ID is not reported as an error.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> value = mtc.get_texture_zoom_y(material_id)
        >>> print(value)

    Returns:
        Zoom factor of the texture in the Y direction.
    """

def set_texture_zoom_y(material_id: MaterialId, value: float) -> None:
    """Set the texture zoom factor in Y of a material.

    The zoom factor scales the texture image of the material in its Y direction. It is stored on the
    material in the document, so it applies to every element that uses the material. The value is
    stored unchanged. Read it back with `material_controller.get_texture_zoom_y()`.

    Parameters:
        material_id: Material ID, e.g. from `material_controller.get_material_id()` or
            `material_controller.get_all_materials()`.
        value: Zoom factor in the Y direction.

    Examples:
        >>> import material_controller as mtc

        >>> material_id = mtc.get_material_id('Spruce')
        >>> mtc.set_texture_zoom_y(material_id, 1.5)
        >>> print(mtc.get_texture_zoom_y(material_id))
    """
