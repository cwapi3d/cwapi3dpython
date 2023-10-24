from enum import IntEnum, unique


@unique
class btl_version(IntEnum):
    """BTL version.

    Examples:
        >>> machine_controller.export_btl(btl_version.btl_1_6, "C:\\temp\\test.btl")

    Args:
        btl_1_0 (int): 110
        btl_1_1 (int): 111
        btl_1_2 (int): 112
        btl_1_3 (int): 113
        btl_1_4 (int): 114
        btl_1_5 (int): 115
        btl_1_6 (int): 116

    """
    btl_1_0 = 110
    btl_1_1 = 111
    btl_1_2 = 112
    btl_1_3 = 113
    btl_1_4 = 114
    btl_1_5 = 115
    btl_1_6 = 116

    def __int__(self) -> int:
        return self.value
