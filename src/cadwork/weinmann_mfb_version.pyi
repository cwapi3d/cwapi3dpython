from enum import IntEnum, unique


@unique
class weinmann_mfb_version(IntEnum):
    """weinmann mfb version

    Examples:
        >>> cadwork.weinmann_mfb_version.wup_2_0
        wup_2_0
    """
    wup_2_0 = 20
    """"""
    wup_3_1 = 31
    """"""
    wup_3_2 = 32
    """"""
    wup_3_3 = 33
    """"""
    wup_3_4 = 34
    """"""

    def __int__(self) -> int:
        return self.value

