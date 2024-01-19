from typing import List

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        strerror string
    """

def create_material(name: str) -> int:
    """create material
    Args:
        name ( str): name

    Returns:
        intmaterial ID
    """

def set_name(material_id: int, name: str) -> None:
    """set name
    Args:
        material_id ( int): material_id
        name ( str): name

    Returns:
        None
    """

def set_group(material_id: int, group: str) -> None:
    """set group
    Args:
        material_id ( int): material_id
        group ( str): group

    Returns:
        None
    """

def set_code(material_id: int, code: str) -> None:
    """set code
    Args:
        material_id ( int): material_id
        code ( str): code

    Returns:
        None
    """

def set_modulus_elasticity_1(material_id: int, modulus_elasticity1: float) -> None:
    """set modulus elasticity 1
    Args:
        material_id ( int): material_id
        modulus_elasticity1 ( float): modulus_elasticity1

    Returns:
        None
    """

def set_modulus_elasticity_2(material_id: int, modulus_elasticity2: float) -> None:
    """set modulus elasticity 2
    Args:
        material_id ( int): material_id
        modulus_elasticity2 ( float): modulus_elasticity2

    Returns:
        None
    """

def set_modulus_elasticity_3(material_id: int, modulus_elasticity3: float) -> None:
    """set modulus elasticity 3
    Args:
        material_id ( int): material_id
        modulus_elasticity3 ( float): modulus_elasticity3

    Returns:
        None
    """

def set_shear_modulus_1(material_id: int, shear_modulus1: float) -> None:
    """set shear modulus 1
    Args:
        material_id ( int): material_id
        shear_modulus1 ( float): shear_modulus1

    Returns:
        None
    """

def set_shear_modulus_2(material_id: int, shear_modulus2: float) -> None:
    """set shear modulus 2
    Args:
        material_id ( int): material_id
        shear_modulus2 ( float): shear_modulus2

    Returns:
        None
    """

def set_price(material_id: int, price: float) -> None:
    """set price
    Args:
        material_id ( int): material_id
        price ( float): price

    Returns:
        None
    """

def set_price_type(material_id: int, price_type: str) -> None:
    """set price type
    Args:
        material_id ( int): material_id
        price_type ( str): price_type

    Returns:
        None
    """

def set_thermal_conductivity(material_id: int, thermal_conductivity: float) -> None:
    """set thermal conductivity
    Args:
        material_id ( int): material_id
        thermal_conductivity ( float): thermal_conductivity

    Returns:
        None
    """

def set_heat_capacity(material_id: int, heat_capacity: float) -> None:
    """set heat capacity
    Args:
        material_id ( int): material_id
        heat_capacity ( float): heat_capacity

    Returns:
        None
    """

def set_u_min(material_id: int, u_min: float) -> None:
    """set u min
    Args:
        material_id ( int): material_id
        u_min ( float): u_min

    Returns:
        None
    """

def set_u_max(material_id: int, u_max: float) -> None:
    """set u max
    Args:
        material_id ( int): material_id
        u_max ( float): u_max

    Returns:
        None
    """

def set_fire_resistance_class(material_id: int, fire_resistance_class: str) -> None:
    """set fire resistance class
    Args:
        material_id ( int): material_id
        fire_resistance_class ( str): fire_resistance_class

    Returns:
        None
    """

def set_smoke_class(material_id: int, smoke_class: str) -> None:
    """set smoke class
    Args:
        material_id ( int): material_id
        smoke_class ( str): smoke_class

    Returns:
        None
    """

def set_drop_forming_class(material_id: int, drop_forming_class: str) -> None:
    """set drop forming class
    Args:
        material_id ( int): material_id
        drop_forming_class ( str): drop_forming_class

    Returns:
        None
    """

def set_burn_off_rate(material_id: int, burn_off_rate: float) -> None:
    """set burn off rate
    Args:
        material_id ( int): material_id
        burn_off_rate ( float): burn_off_rate

    Returns:
        None
    """

def set_weight(material_id: int, weight: float) -> None:
    """set weight
    Args:
        material_id ( int): material_id
        weight ( float): weight

    Returns:
        None
    """

def set_weight_type(material_id: int, weight_type: str) -> None:
    """set weight type
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
    """get material id
    Args:
        material_name ( str): material_name

    Returns:
        intmaterial ID
    """

def get_name(material_id: int) -> str:
    """get name
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial name
    """

def get_group(material_id: int) -> str:
    """get group
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial group
    """

def get_code(material_id: int) -> str:
    """get code
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial code
    """

def get_modulus_elasticity_1(material_id: int) -> float:
    """get modulus elasticity 1
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial modulus of elasticity 1
    """

def get_modulus_elasticity_2(material_id: int) -> float:
    """get modulus elasticity 2
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial modulus of elasticity 2
    """

def get_modulus_elasticity_3(material_id: int) -> float:
    """get modulus elasticity 3
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial modulus of elasticity 3
    """

def get_shear_modulus_1(material_id: int) -> float:
    """get shear modulus 1
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial shear modulus 1
    """

def get_shear_modulus_2(material_id: int) -> float:
    """get shear modulus 2
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial shear modulus 2
    """

def get_price(material_id: int) -> float:
    """get price
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial price
    """

def get_price_type(material_id: int) -> str:
    """get price type
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial price type
    """

def get_thermal_conductivity(material_id: int) -> float:
    """get thermal conductivity
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial thermal conductivity
    """

def get_heat_capacity(material_id: int) -> float:
    """get heat capacity
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial heat capacity
    """

def get_u_min(material_id: int) -> float:
    """get u min
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial U min
    """

def get_u_max(material_id: int) -> float:
    """get u max
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial U max
    """

def get_fire_resistance_class(material_id: int) -> str:
    """get fire resistance class
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial fire resistance class
    """

def get_smoke_class(material_id: int) -> str:
    """get smoke class
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial smoke class
    """

def get_drop_forming_class(material_id: int) -> str:
    """get drop forming class
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial drop forming class
    """

def get_burn_off_rate(material_id: int) -> float:
    """get burn off rate
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial burn off rate
    """

def get_weight(material_id: int) -> float:
    """get weight
    Args:
        material_id ( int): material_id

    Returns:
        floatmaterial weight
    """

def get_weight_type(material_id: int) -> str:
    """get weight type
    Args:
        material_id ( int): material_id

    Returns:
        strmaterial weight type
    """

def get_all_materials() -> List[int]:
    """get all materials
    Args:

    Returns:
        List[int]material ID list
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

