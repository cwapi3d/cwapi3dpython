from enum import IntEnum, unique


@unique
class ifc_element_combine_behaviour(IntEnum):
    """ifc export element combine behaviour.

    Examples:
        >>> ifc_options = cadwork.ifc_options()
        >>> ifc_options_combine = ifc_options.get_ifc_options_aggregation()
        >>> ifc_options_combine.set_consider_element_aggregation(True)
        >>> ifc_options_combine.set_element_combine_behaviour(cadwork.ifc_element_combine_behaviour.element_module)

    Args:
        element_module (int): 1
        element_assembly (int): 2
    """

    element_module = 1
    element_assembly = 2

    def __int__(self) -> int:
        return self.value
