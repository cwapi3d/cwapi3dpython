from enum import IntEnum, unique


@unique
class btl_version(IntEnum):
    """btl version

    Examples:
        >>> cadwork.btl_version.btlx_1_0
        btlx_1_0
    """
    btlx_1_0 = 110
    """"""
    btlx_1_1 = 111
    """"""
    btl_1_2 = 112
    """"""
    btl_1_3 = 113
    """"""
    btl_1_4 = 114
    """"""
    btl_1_5 = 115
    """"""
    btl_1_6 = 116
    """"""
    btl_10_0 = 100
    """"""
    btl_10_1 = 101
    """"""
    btl_10_2 = 102
    """"""
    btl_10_3 = 103
    """"""
    btl_10_4 = 104
    """"""
    btl_10_5 = 105
    """"""
    btl_10_6 = 106
    """"""
    btlx_2_0 = 120
    """"""
    btlx_2_1 = 121
    """"""
    btlx_2_2 = 122
    """"""

    def __int__(self) -> int:
        return self.value

