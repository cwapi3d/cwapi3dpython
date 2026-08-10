from enum import IntEnum, unique


@unique
class end_type(IntEnum):
    """end type

    End type of an element.

    Examples:
        >>> cadwork.end_type.Tenon
        Tenon
    """

    Unknown = 0
    """"""
    Tenon = 1
    """"""
    Lengthening = 2
    """"""
    DovetailTenon = 3
    """"""
    GMIWithCounterpart = 4
    """"""
    DovetailMortise = 5
    """"""
    FrontSlot = 6
    """"""
    JapaneseTenon = 7
    """"""

    def __int__(self) -> int:
        return self.value
