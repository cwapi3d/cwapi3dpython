from typing import List

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def create_material(name: str) -> int:
    """Creates new material

    Parameters:
        name: name

    Returns:
        material ID
    """

def set_name(material_id: int, name: str) -> None:
    """Sets the material name

    Parameters:
        material_id: material_id
        name: name

    Returns:
        None
    """

def set_group(material_id: int, group: str) -> None:
    """Sets the material group

    Parameters:
        material_id: material_id
        group: group

    Returns:
        None
    """

def set_code(material_id: int, code: str) -> None:
    """Sets the material code

    Parameters:
        material_id: material_id
        code: code

    Returns:
        None
    """

def set_modulus_elasticity_1(material_id: int, modulus_elasticity1: float) -> None:
    """Sets the material modulus of elasticity 1

    Parameters:
        material_id: material_id
        modulus_elasticity1: modulus_elasticity1

    Returns:
        None
    """

def set_modulus_elasticity_2(material_id: int, modulus_elasticity2: float) -> None:
    """Sets the material modulus of elasticity 2

    Parameters:
        material_id: material_id
        modulus_elasticity2: modulus_elasticity2

    Returns:
        None
    """

def set_modulus_elasticity_3(material_id: int, modulus_elasticity3: float) -> None:
    """Sets the material modulus of elasticity 3

    Parameters:
        material_id: material_id
        modulus_elasticity3: modulus_elasticity3

    Returns:
        None
    """

def set_shear_modulus_1(material_id: int, shear_modulus1: float) -> None:
    """Sets the material shear modulus 1

    Parameters:
        material_id: material_id
        shear_modulus1: shear_modulus1

    Returns:
        None
    """

def set_shear_modulus_2(material_id: int, shear_modulus2: float) -> None:
    """Sets the material shear modulus 2

    Parameters:
        material_id: material_id
        shear_modulus2: shear_modulus2

    Returns:
        None
    """

def set_price(material_id: int, price: float) -> None:
    """Sets the material price

    Parameters:
        material_id: material_id
        price: price

    Returns:
        None
    """

def set_price_type(material_id: int, price_type: str) -> None:
    """Sets the material price type

    Parameters:
        material_id: material_id
        price_type: price_type

    Returns:
        None
    """

def set_thermal_conductivity(material_id: int, thermal_conductivity: float) -> None:
    """Sets the material thermal conductivity

    Parameters:
        material_id: material_id
        thermal_conductivity: thermal_conductivity

    Returns:
        None
    """

def set_heat_capacity(material_id: int, heat_capacity: float) -> None:
    """Sets the material heat capacity

    Parameters:
        material_id: material_id
        heat_capacity: heat_capacity

    Returns:
        None
    """

def set_u_min(material_id: int, u_min: float) -> None:
    """Sets the material U min

    Parameters:
        material_id: material_id
        u_min: u_min

    Returns:
        None
    """

def set_u_max(material_id: int, u_max: float) -> None:
    """Sets the material U max

    Parameters:
        material_id: material_id
        u_max: u_max

    Returns:
        None
    """

def set_fire_resistance_class(material_id: int, fire_resistance_class: str) -> None:
    """Sets the material fire resistance class

    Parameters:
        material_id: material_id
        fire_resistance_class: fire_resistance_class

    Returns:
        None
    """

def set_smoke_class(material_id: int, smoke_class: str) -> None:
    """Sets the material smoke class

    Parameters:
        material_id: material_id
        smoke_class: smoke_class

    Returns:
        None
    """

def set_drop_forming_class(material_id: int, drop_forming_class: str) -> None:
    """Sets the material drop forming class

    Parameters:
        material_id: material_id
        drop_forming_class: drop_forming_class

    Returns:
        None
    """

def set_burn_off_rate(material_id: int, burn_off_rate: float) -> None:
    """Sets the material burn-off rate

    Parameters:
        material_id: material_id
        burn_off_rate: burn_off_rate

    Returns:
        None
    """

def set_weight(material_id: int, weight: float) -> None:
    """Sets the material weight

    Parameters:
        material_id: material_id
        weight: weight

    Returns:
        None
    """

def set_weight_type(material_id: int, weight_type: str) -> None:
    """Sets the material weight type

    Parameters:
        material_id: material_id
        weight_type: weight_type

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def set_grade(a0: int, a1: str) -> None:
    """set grade

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def set_quality(a0: int, a1: str) -> None:
    """set quality

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def set_composition(a0: int, a1: str) -> None:
    """set composition

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def get_material_id(material_name: str) -> int:
    """Gets the material with a given name

    Parameters:
        material_name: material_name

    Returns:
        material ID
    """

def get_name(material_id: int) -> str:
    """Gets the material name

    Parameters:
        material_id: material_id

    Returns:
        material name
    """

def get_group(material_id: int) -> str:
    """Gets the material group

    Parameters:
        material_id: material_id

    Returns:
        material group
    """

def get_code(material_id: int) -> str:
    """Gets the material code

    Parameters:
        material_id: material_id

    Returns:
        material code
    """

def get_modulus_elasticity_1(material_id: int) -> float:
    """Gets the material modulus of elasticity 1

    Parameters:
        material_id: material_id

    Returns:
        material modulus of elasticity 1
    """

def get_modulus_elasticity_2(material_id: int) -> float:
    """Gets the material modulus of elasticity 2

    Parameters:
        material_id: material_id

    Returns:
        material modulus of elasticity 2
    """

def get_modulus_elasticity_3(material_id: int) -> float:
    """Gets the material modulus of elasticity 3

    Parameters:
        material_id: material_id

    Returns:
        material modulus of elasticity 3
    """

def get_shear_modulus_1(material_id: int) -> float:
    """Gets the material shear modulus 1

    Parameters:
        material_id: material_id

    Returns:
        material shear modulus 1
    """

def get_shear_modulus_2(material_id: int) -> float:
    """Gets the material shear modulus 2

    Parameters:
        material_id: material_id

    Returns:
        material shear modulus 2
    """

def get_price(material_id: int) -> float:
    """Gets the material price

    Parameters:
        material_id: material_id

    Returns:
        material price
    """

def get_price_type(material_id: int) -> str:
    """Sets the material price type

    Parameters:
        material_id: material_id

    Returns:
        material price type
    """

def get_thermal_conductivity(material_id: int) -> float:
    """Gets the material thermal conductivity

    Parameters:
        material_id: material_id

    Returns:
        material thermal conductivity
    """

def get_heat_capacity(material_id: int) -> float:
    """Gets the material heat capacity

    Parameters:
        material_id: material_id

    Returns:
        material heat capacity
    """

def get_u_min(material_id: int) -> float:
    """Gets the material U min

    Parameters:
        material_id: material_id

    Returns:
        material U min
    """

def get_u_max(material_id: int) -> float:
    """Gets the material U max

    Parameters:
        material_id: material_id

    Returns:
        material U max
    """

def get_fire_resistance_class(material_id: int) -> str:
    """Gets the material fire resistance class

    Parameters:
        material_id: material_id

    Returns:
        material fire resistance class
    """

def get_smoke_class(material_id: int) -> str:
    """Gets the material smoke class

    Parameters:
        material_id: material_id

    Returns:
        material smoke class
    """

def get_drop_forming_class(material_id: int) -> str:
    """Gets the material drop forming class

    Parameters:
        material_id: material_id

    Returns:
        material drop forming class
    """

def get_burn_off_rate(material_id: int) -> float:
    """Gets the material burn-off rate

    Parameters:
        material_id: material_id

    Returns:
        material burn off rate
    """

def get_weight(material_id: int) -> float:
    """Gets the material weight

    Parameters:
        material_id: material_id

    Returns:
        material weight
    """

def get_weight_type(material_id: int) -> str:
    """Gets the material weight type

    Parameters:
        material_id: material_id

    Returns:
        material weight type
    """

def get_all_materials() -> List[int]:
    """Gets all the materials

    Returns:
        material ID list
    """

def get_grade(a0: int) -> str:
    """get grade

    Parameters:
        a0: a0

    Returns:
        str
    """

def get_quality(a0: int) -> str:
    """get quality

    Parameters:
        a0: a0

    Returns:
        str
    """

def get_composition(a0: int) -> str:
    """get composition

    Parameters:
        a0: a0

    Returns:
        str
    """

def get_short_name(a0: int) -> str:
    """get short name

    Parameters:
        a0: a0

    Returns:
        str
    """

def get_all_material_groups() -> List[str]:
    """Gets all the material groups

    Returns:
        group names
    """

def get_parent_group(group: str) -> str:
    """Gets the parent group of a material group

    Parameters:
        group: group

    Returns:
        parent group name
    """

