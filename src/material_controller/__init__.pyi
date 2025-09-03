from typing import List
from cadwork.api_types import MaterialId, UnsignedInt

def create_material(name: str) -> MaterialId:
    """Creates new material.

    Parameters:
        name: The material name.

    Returns:
        The material id.
    """

def set_name(material_id: MaterialId, name: str) -> None:
    """Sets the material name.

    Parameters:
        material_id: The material id.
        name: The material name.
    """

def set_group(material_id: MaterialId, group: str) -> None:
    """Sets the material group.

    Parameters:
        material_id: The material id.
        group: The material group.
    """

def set_code(material_id: MaterialId, code: str) -> None:
    """Sets the material code.

    Parameters:
        material_id: The material id.
        code: The material code.
    """

def set_modulus_elasticity_1(material_id: MaterialId, modulus_elasticity1: float) -> None:
    """Sets the material modulus of elasticity 1.

    Parameters:
        material_id: The material id.
        modulus_elasticity1: The material modulus of elasticity 1.
    """

def set_modulus_elasticity_2(material_id: MaterialId, modulus_elasticity2: float) -> None:
    """Sets the material modulus of elasticity 2.

    Parameters:
        material_id: The material id.
        modulus_elasticity2: The material modulus of elasticity 2.
    """

def set_modulus_elasticity_3(material_id: MaterialId, modulus_elasticity3: float) -> None:
    """Sets the material modulus of elasticity 3.

    Parameters:
        material_id: The material id.
        modulus_elasticity3: The material modulus of elasticity 3.
    """

def set_shear_modulus_1(material_id: MaterialId, shear_modulus1: float) -> None:
    """Sets the material shear modulus 1.

    Parameters:
        material_id: The material id.
        shear_modulus1: The material shear modulus 1.
    """

def set_shear_modulus_2(material_id: MaterialId, shear_modulus2: float) -> None:
    """Sets the material shear modulus 2.

    Parameters:
        material_id: The material id.
        shear_modulus2: The material shear modulus 2.
    """

def set_price(material_id: MaterialId, price: float) -> None:
    """Sets the material price.

    Parameters:
        material_id: The material id.
        price: The material price.
    """

def set_price_type(material_id: MaterialId, price_type: str) -> None:
    """Sets the material price type.

    Parameters:
        material_id: The material id.
        price_type: The material price type.
    """

def set_thermal_conductivity(material_id: MaterialId, thermal_conductivity: float) -> None:
    """Sets the material thermal conductivity.

    Parameters:
        material_id: The material id.
        thermal_conductivity: The material thermal conductivity.
    """

def set_heat_capacity(material_id: MaterialId, heat_capacity: float) -> None:
    """Sets the material heat capacity.

    Parameters:
        material_id: The material id.
        heat_capacity: The material heat capacity.
    """

def set_u_min(material_id: MaterialId, u_min: float) -> None:
    """Sets the material U min.

    Parameters:
        material_id: The material id.
        u_min: The material U min.
    """

def set_u_max(material_id: MaterialId, u_max: float) -> None:
    """Sets the material U max.

    Parameters:
        material_id: The material id.
        u_max: The material U max.
    """

def set_fire_resistance_class(material_id: MaterialId, fire_resistance_class: str) -> None:
    """Sets the material fire resistance class.

    Parameters:
        material_id: The material id.
        fire_resistance_class: The material fire resistance class.
    """

def set_smoke_class(material_id: MaterialId, smoke_class: str) -> None:
    """Sets the material smoke class.

    Parameters:
        material_id: The material id.
        smoke_class: The material smoke class.
    """

def set_drop_forming_class(material_id: MaterialId, drop_forming_class: str) -> None:
    """Sets the material drop forming class.

    Parameters:
        material_id: The material id.
        drop_forming_class: The material drop forming class.
    """

def set_burn_off_rate(material_id: MaterialId, burn_off_rate: float) -> None:
    """Sets the material burn-off rate.

    Parameters:
        material_id: The material id.
        burn_off_rate: The material burn off rate.
    """

def set_weight(material_id: MaterialId, weight: float) -> None:
    """Sets the material weight.

    Parameters:
        material_id: The material id.
        weight: The material weight.
    """

def set_weight_type(material_id: MaterialId, weight_type: str) -> None:
    """Sets the material weight type.

    Parameters:
        material_id: The material id.
        weight_type: The material weight type.
    """

def clear_errors() -> None:
    """Clears all errors.
    """


def set_grade(material_id: MaterialId, grade: str) -> None:
    """Sets the grade of a material.

    Parameters:
        material_id: The material id.
        grade: The grade to set.
    """


def set_quality(material_id: MaterialId, quality: str) -> None:
    """Sets the quality of a material.

    Parameters:
        material_id: The material id.
        quality: The quality to set.
    """


def set_composition(material_id: MaterialId, composition: str) -> None:
    """Sets the composition of a material.

    Parameters:
        material_id: The material id.
        composition: The composition to set.
    """

def get_material_id(material_name: str) -> MaterialId:
    """Gets the material with a given name.

    Parameters:
        material_name: The material name.

    Returns:
        The material id.
    """

def get_name(material_id: MaterialId) -> str:
    """Gets the material name.

    Parameters:
        material_id: The material id.

    Returns:
        The material name.
    """

def get_group(material_id: MaterialId) -> str:
    """Gets the material group.

    Parameters:
        material_id: The material id.

    Returns:
        The material group.
    """

def get_code(material_id: MaterialId) -> str:
    """Gets the material code.

    Parameters:
        material_id: The material id.

    Returns:
        The material code.
    """

def get_modulus_elasticity_1(material_id: MaterialId) -> float:
    """Gets the material modulus of elasticity 1.

    Parameters:
        material_id: The material id.

    Returns:
        The material modulus of elasticity 1.
    """

def get_modulus_elasticity_2(material_id: MaterialId) -> float:
    """Gets the material modulus of elasticity 2.

    Parameters:
        material_id: The material id.

    Returns:
        The material modulus of elasticity 2.
    """

def get_modulus_elasticity_3(material_id: MaterialId) -> float:
    """Gets the material modulus of elasticity 3.

    Parameters:
        material_id: The material id.

    Returns:
        The material modulus of elasticity 3.
    """

def get_shear_modulus_1(material_id: MaterialId) -> float:
    """Gets the material shear modulus 1.

    Parameters:
        material_id: The material id.

    Returns:
        The material shear modulus 1.
    """

def get_shear_modulus_2(material_id: MaterialId) -> float:
    """Gets the material shear modulus 2.

    Parameters:
        material_id: The material id.

    Returns:
        The material shear modulus 2.
    """

def get_price(material_id: MaterialId) -> float:
    """Gets the material price.

    Parameters:
        material_id: The material id.

    Returns:
        The material price.
    """

def get_price_type(material_id: MaterialId) -> str:
    """Gets the material price type.

    Parameters:
        material_id: The material id.

    Returns:
        The material price type.
    """

def get_thermal_conductivity(material_id: MaterialId) -> float:
    """Gets the material thermal conductivity.

    Parameters:
        material_id: The material id.

    Returns:
        The material thermal conductivity.
    """

def get_heat_capacity(material_id: MaterialId) -> float:
    """Gets the material heat capacity.

    Parameters:
        material_id: The material id.

    Returns:
        The material heat capacity.
    """

def get_u_min(material_id: MaterialId) -> float:
    """Gets the material U min.

    Parameters:
        material_id: The material id.

    Returns:
        The material U min.
    """

def get_u_max(material_id: MaterialId) -> float:
    """Gets the material U max.

    Parameters:
        material_id: The material id.

    Returns:
        The material U max.
    """

def get_fire_resistance_class(material_id: MaterialId) -> str:
    """Gets the material fire resistance class.

    Parameters:
        material_id: The material id.

    Returns:
        The material fire resistance class.
    """

def get_smoke_class(material_id: MaterialId) -> str:
    """Gets the material smoke class.

    Parameters:
        material_id: The material id.

    Returns:
        The material smoke class.
    """

def get_drop_forming_class(material_id: MaterialId) -> str:
    """Gets the material drop forming class.

    Parameters:
        material_id: The material id.

    Returns:
        The material drop forming class.
    """

def get_burn_off_rate(material_id: MaterialId) -> float:
    """Gets the material burn-off rate.

    Parameters:
        material_id: The material id.

    Returns:
        The material burn off rate.
    """

def get_weight(material_id: MaterialId) -> float:
    """Gets the material weight.

    Parameters:
        material_id: The material id.

    Returns:
        The material weight.
    """

def get_weight_type(material_id: MaterialId) -> str:
    """Gets the material weight type.

    Parameters:
        material_id: The material id.

    Returns:
        The material weight type.
    """

def get_all_materials() -> List[MaterialId]:
    """Retrieves a list of all materials.

    Returns:
        A list of all material id.
    """


def get_grade(material_id: MaterialId) -> str:
    """Gets the grade of a material.

    Parameters:
        material_id: The material id.

    Returns:
        The grade of the material.
    """


def get_quality(material_id: MaterialId) -> str:
    """Gets the quality of a material.

    Parameters:
        material_id: The material id.

    Returns:
        The quality of the material.
    """


def get_composition(material_id: MaterialId) -> str:
    """Gets the composition of a material.

    Parameters:
        material_id: The material id.

    Returns:
        The composition of the material.
    """


def get_short_name(material_id: MaterialId) -> str:
    """Gets the short name of a material.

    Parameters:
        material_id: The material id.

    Returns:
        The short name of the material.
    """

def get_all_material_groups() -> List[MaterialId]:
    """Retrieves a list of all material groups.

    Returns:
        A list of all material group names.
    """

def get_parent_group(group: str) -> str:
    """Gets the parent group of a given group.

    Parameters:
        group: The name of the group.

    Returns:
        The name of the parent group.
    """


def get_material_color_assignment_for_nodes(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for nodes.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for nodes.
    """


def set_material_color_assignment_for_nodes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for nodes.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for nodes.
    """


def get_material_color_assignment_for_standard_axes(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for standard axes.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for standard axes.
    """


def set_material_color_assignment_for_standard_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for standard axes.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for standard axes.
    """


def get_material_color_assignment_for_drillings(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for drillings.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for drillings.
    """


def set_material_color_assignment_for_drillings(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for drillings.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for drillings.
    """


def get_material_color_assignment_for_mep_axes(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for MEP axes.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for MEP axes.
    """


def set_material_color_assignment_for_mep_axes(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for MEP axes.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for MEP axes.
    """


def get_material_color_assignment_for_beams(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for beams.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for beams.
    """


def set_material_color_assignment_for_beams(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for beams.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for beams.
    """


def get_material_color_assignment_for_panels(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for panels.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for panels.
    """


def set_material_color_assignment_for_panels(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for panels.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for panels.
    """


def get_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for auxiliary elements.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for auxiliary elements.
    """


def set_material_color_assignment_for_auxiliary_elements(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for auxiliary elements.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for auxiliary elements.
    """


def get_material_color_assignment_for_surfaces(color_nb: UnsignedInt) -> MaterialId:
    """Gets the material color assignment for surfaces.

    Parameters:
        color_nb: The color number. [1-255]

    Returns:
        The material id assigned to the color number for surfaces.
    """


def set_material_color_assignment_for_surfaces(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the material color assignment for surfaces.

    Parameters:
        color_nb: The color number. [1-255]
        material_id: The material ID to assign to the color number for surfaces.
    """


def get_texture_color(material_id: MaterialId) -> int:
    """Gets the texture color for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        The color of the texture. [1-255]
    """


def set_texture_color(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the texture color for a given material ID.

    Parameters:
        color_nb: The color to set for the texture. [1-255]
        material_id: The material id.
    """


def get_texture_transparency(material_id: MaterialId) -> int:
    """Gets the texture transparency for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        The transparency of the texture.
    """


def set_texture_transparency(color_nb: UnsignedInt, material_id: MaterialId) -> None:
    """Sets the texture transparency for a given material ID.

    Parameters:
        color_nb: The transparency to set for the texture.
        material_id: The material id.
    """


def get_texture_rotation_angle(material_id: MaterialId) -> float:
    """Gets the texture rotation angle for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        The rotation angle of the texture.
    """


def set_texture_rotation_angle(material_id: MaterialId, angle: float) -> None:
    """Sets the texture rotation angle for a given material ID.

    Parameters:
        material_id: The material id.
        angle: The rotation angle to set for the texture.
    """


def get_texture_length_alignment(material_id: MaterialId) -> bool:
    """Gets the texture length alignment for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        True if Texture Random Placement is enabled, false otherwise.
    """


def set_texture_length_alignment(material_id: MaterialId, flag: bool) -> None:
    """Sets the texture length alignment for a given material ID.

    Parameters:
        material_id: The material id.
        flag: True if Texture Random Placement is enabled, false otherwise.
    """


def get_texture_zoom_x(material_id: MaterialId) -> float:
    """Gets the texture zoom factor in the X direction for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        The zoom factor of the texture in the X direction.
    """


def set_texture_zoom_x(material_id: MaterialId, value: float) -> None:
    """Sets the texture zoom factor in the X direction for a given material ID.

    Parameters:
        material_id: The material id.
        value: The zoom factor to set in the X direction.
    """


def get_texture_zoom_y(material_id: MaterialId) -> float:
    """Gets the texture zoom factor in the Y direction for a given material ID.

    Parameters:
        material_id: The material id.

    Returns:
        The zoom factor of the texture in the Y direction.
    """


def set_texture_zoom_y(material_id: MaterialId, value: float) -> None:
    """Sets the texture zoom factor in the Y direction for a given material ID.

    Parameters:
        material_id: The material id.
        value: The zoom factor to set.
    """