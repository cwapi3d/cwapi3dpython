from enum import IntEnum, unique


@unique
class weinmann_mfb_version(IntEnum):
    """Weinmann MFB version.

    Examples:
        >>> machine_controller.export_weinmann_mfb(weinmann_mfb_version.wup_2_0)

    Args:
        wup_2_0 (int): 20
        wup_3_1 (int): 31
        wup_3_2 (int): 32
        wup_3_3 (int): 33
        wup_3_4 (int): 34

    """

    wup_2_0 = 20
    wup_3_1 = 31
    wup_3_2 = 32
    wup_3_3 = 33
    wup_3_4 = 34

    def __int__(self) -> int:
        return self.value
