from enum import IntEnum, unique


@unique
class ifc_element_combine_behaviour(IntEnum):
    """ifc element combine behaviour

    Examples:
        >>> cadwork.ifc_element_combine_behaviour.element_module
        element_module
    """
    element_module = 0
    """"""
    element_assembly = 1
    """"""

    def __int__(self) -> int:
        return self.value

