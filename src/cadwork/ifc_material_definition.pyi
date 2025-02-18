from enum import IntEnum, unique


@unique
class ifc_material_definition(IntEnum):
    """ifc material definition

    Examples:
        >>> cadwork.ifc_material_definition.ignore
        ignore
    """
    ignore = 1
    """"""
    material_layer_set = 2
    """"""
    material_constituent_set = 3
    """"""

    def __int__(self) -> int:
        return self.value

