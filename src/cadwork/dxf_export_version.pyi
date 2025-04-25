from enum import IntEnum, unique


@unique
class dxf_export_version(IntEnum):
    """ Enumeration for DXF export version.

    Examples:
        >>> cadwork.dxf_export_version.auto_cad_r27

    """
    auto_cad_r10 = 0
    """"""
    auto_cad_r27 = 1
    """"""

    def __int__(self) -> int:
        return self.value
