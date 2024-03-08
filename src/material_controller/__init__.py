from typing import List

def get_last_error(error_code: int) -> str:
    """Gets the last error 
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def create_material(name: str) -> int:
    """Creates new material 
    Args:
        name ( str): name

    Returns:
        material ID (int)
    """

def set_name(material_id: int, name: str) -> None:
    """Sets the material name 
    Args:
        material_id ( int): material_id
        name ( str): name

    Returns:
        None
    """

def set_group(material_id: int, group: str) -> None:
    """Sets the material group 
    Args:
        material_id ( int): material_id
        group ( str): group

    Returns:
        None
    """

def set_code(material_id: int, code: str) -> None:
    """Sets the material code 
    Args:
        material_id ( int): material_id
        code ( str): code

    Returns:
        None
    """

def set_modulus_elasticity_1(material_id: int, modulus_elasticity1: float) -> None:
    """Sets the material modulus of elasticity 1 
    Args:
        material_id ( int): material_id
        modulus_elasticity1 ( float): modulus_elasticity1

    Returns:
        None
    """

def set_modulus_elasticity_2(material_id: int, modulus_elasticity2: float) -> None:
    """Sets the material modulus of elasticity 2 
    Args:
        material_id ( int): material_id
        modulus_elasticity2 ( float): modulus_elasticity2

    Returns:
        None
    """

def set_modulus_elasticity_3(material_id: int, modulus_elasticity3: float) -> None:
    """Sets the material modulus of elasticity 3 
    Args:
        material_id ( int): material_id
        modulus_elasticity3 ( float): modulus_elasticity3

    Returns:
        None
    """

def set_shear_modulus_1(material_id: int, shear_modulus1: float) -> None:
    """Sets the material shear modulus 1 
    Args:
        material_id ( int): material_id
        shear_modulus1 ( float): shear_modulus1

    Returns:
        None
    """

def set_shear_modulus_2(material_id: int, shear_modulus2: float) -> None:
    """Sets the material shear modulus 2 
    Args:
        material_id ( int): material_id
        shear_modulus2 ( float): shear_modulus2

    Returns:
        None
    """

def set_price(material_id: int, price: float) -> None:
    """Sets the material price 
    Args:
        material_id ( int): material_id
        price ( float): price

    Returns:
        None
    """

def set_price_type(material_id: int, price_type: str) -> None:
    """Sets the material price type 
    Args:
        material_id ( int): material_id
        price_type ( str): price_type

    Returns:
        None
    """

def set_thermal_conductivity(material_id: int, thermal_conductivity: float) -> None:
    """Sets the material thermal conductivity 
    Args:
        material_id ( int): material_id
        thermal_conductivity ( float): thermal_conductivity

    Returns:
        None
    """

def set_heat_capacity(material_id: int, heat_capacity: float) -> None:
    """Sets the material heat capacity 
    Args:
        material_id ( int): material_id
        heat_capacity ( float): heat_capacity

    Returns:
        None
    """

def set_u_min(material_id: int, u_min: float) -> None:
    """Sets the material U min 
    Args:
        material_id ( int): material_id
        u_min ( float): u_min

    Returns:
        None
    """

def set_u_max(material_id: int, u_max: float) -> None:
    """Sets the material U max 
    Args:
        material_id ( int): material_id
        u_max ( float): u_max

    Returns:
        None
    """

def set_fire_resistance_class(material_id: int, fire_resistance_class: str) -> None:
    """Sets the material fire resistance class 
    Args:
        material_id ( int): material_id
        fire_resistance_class ( str): fire_resistance_class

    Returns:
        None
    """

def set_smoke_class(material_id: int, smoke_class: str) -> None:
    """Sets the material smoke class 
    Args:
        material_id ( int): material_id
        smoke_class ( str): smoke_class

    Returns:
        None
    """

def set_drop_forming_class(material_id: int, drop_forming_class: str) -> None:
    """Sets the material drop forming class 
    Args:
        material_id ( int): material_id
        drop_forming_class ( str): drop_forming_class

    Returns:
        None
    """

def set_burn_off_rate(material_id: int, burn_off_rate: float) -> None:
    """Sets the material burn-off rate 
    Args:
        material_id ( int): material_id
        burn_off_rate ( float): burn_off_rate

    Returns:
        None
    """

def set_weight(material_id: int, weight: float) -> None:
    """Sets the material weight 
    Args:
        material_id ( int): material_id
        weight ( float): weight

    Returns:
        None
    """

def set_weight_type(material_id: int, weight_type: str) -> None:
    """Sets the material weight type 
    Args:
        material_id ( int): material_id
        weight_type ( str): weight_type

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def set_grade(a0: int, a1: str) -> None:
    """set grade
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        None
    """

def set_quality(a0: int, a1: str) -> None:
    """set quality
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        None
    """

def set_composition(a0: int, a1: str) -> None:
    """set composition
    Args:
        a0 ( int): a0
        a1 ( str): a1

    Returns:
        None
    """

def get_material_id(material_name: str) -> int:
    """Gets the material with a given name 
    Args:
        material_name ( str): material_name

    Returns:
        material ID (int)
    """

def get_name(material_id: int) -> str:
    """Gets the material name 
    Args:
        material_id ( int): material_id

    Returns:
        material name (str)
    """

def get_group(material_id: int) -> str:
    """Gets the material group 
    Args:
        material_id ( int): material_id

    Returns:
        material group (str)
    """

def get_code(material_id: int) -> str:
    """Gets the material code 
    Args:
        material_id ( int): material_id

    Returns:
        material code (str)
    """

def get_modulus_elasticity_1(material_id: int) -> float:
    """Gets the material modulus of elasticity 1 
    Args:
        material_id ( int): material_id

    Returns:
        material modulus of elasticity 1 (float)
    """

def get_modulus_elasticity_2(material_id: int) -> float:
    """Gets the material modulus of elasticity 2 
    Args:
        material_id ( int): material_id

    Returns:
        material modulus of elasticity 2 (float)
    """

def get_modulus_elasticity_3(material_id: int) -> float:
    """Gets the material modulus of elasticity 3 
    Args:
        material_id ( int): material_id

    Returns:
        material modulus of elasticity 3 (float)
    """

def get_shear_modulus_1(material_id: int) -> float:
    """Gets the material shear modulus 1 
    Args:
        material_id ( int): material_id

    Returns:
        material shear modulus 1 (float)
    """

def get_shear_modulus_2(material_id: int) -> float:
    """Gets the material shear modulus 2 
    Args:
        material_id ( int): material_id

    Returns:
        material shear modulus 2 (float)
    """

def get_price(material_id: int) -> float:
    """Gets the material price 
    Args:
        material_id ( int): material_id

    Returns:
        material price (float)
    """

def get_price_type(material_id: int) -> str:
    """Sets the material price type 
    Args:
        material_id ( int): material_id

    Returns:
        material price type (str)
    """

def get_thermal_conductivity(material_id: int) -> float:
    """Gets the material thermal conductivity 
    Args:
        material_id ( int): material_id

    Returns:
        material thermal conductivity (float)
    """

def get_heat_capacity(material_id: int) -> float:
    """Gets the material heat capacity 
    Args:
        material_id ( int): material_id

    Returns:
        material heat capacity (float)
    """

def get_u_min(material_id: int) -> float:
    """Gets the material U min 
    Args:
        material_id ( int): material_id

    Returns:
        material U min (float)
    """

def get_u_max(material_id: int) -> float:
    """Gets the material U max 
    Args:
        material_id ( int): material_id

    Returns:
        material U max (float)
    """

def get_fire_resistance_class(material_id: int) -> str:
    """Gets the material fire resistance class 
    Args:
        material_id ( int): material_id

    Returns:
        material fire resistance class (str)
    """

def get_smoke_class(material_id: int) -> str:
    """Gets the material smoke class 
    Args:
        material_id ( int): material_id

    Returns:
        material smoke class (str)
    """

def get_drop_forming_class(material_id: int) -> str:
    """Gets the material drop forming class 
    Args:
        material_id ( int): material_id

    Returns:
        material drop forming class (str)
    """

def get_burn_off_rate(material_id: int) -> float:
    """Gets the material burn-off rate 
    Args:
        material_id ( int): material_id

    Returns:
        material burn off rate (float)
    """

def get_weight(material_id: int) -> float:
    """Gets the material weight 
    Args:
        material_id ( int): material_id

    Returns:
        material weight (float)
    """

def get_weight_type(material_id: int) -> str:
    """Gets the material weight type 
    Args:
        material_id ( int): material_id

    Returns:
        material weight type (str)
    """

def get_all_materials() -> List[int]:
    """Gets all the materials 
    Args:

    Returns:
        material ID list (List[int])
    """

def get_grade(a0: int) -> str:
    """get grade
    Args:
        a0 ( int): a0

    Returns:
        str
    """

def get_quality(a0: int) -> str:
    """get quality
    Args:
        a0 ( int): a0

    Returns:
        str
    """

def get_composition(a0: int) -> str:
    """get composition
    Args:
        a0 ( int): a0

    Returns:
        str
    """

def get_short_name(a0: int) -> str:
    """get short name
    Args:
        a0 ( int): a0

    Returns:
        str
    """

def get_all_material_groups() -> List[str]:
    """Gets all the material groups
    Args:

    Returns:
        group names (List[str])
    """

def get_parent_group(group: str) -> str:
    """Gets the parent group of a material group
    Args:
        group ( str): group

    Returns:
        parent group name (str)
    """

