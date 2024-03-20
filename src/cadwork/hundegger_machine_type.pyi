from enum import IntEnum, unique


@unique
class hundegger_machine_type(IntEnum):
    """hundegger machine type

    Examples:
        >>> cadwork.hundegger_machine_type.p8_10
        p8_10
    """
    p8_10 = 1
    """"""
    k1 = 2
    """"""
    k2 = 3
    """"""
    k2_cambium = 4
    """"""
    k2_uf_5 = 5
    """"""
    k2_uf_5_cambium = 6
    """"""
    speedcut = 7
    """"""
    pba = 8
    """"""
    pba_bvx = 9
    """"""
    pba_bvx_cambium = 10
    """"""
    spm = 12
    """"""
    spm_cambium = 13
    """"""
    robot_drive = 14
    """"""
    turbo_drive = 15
    """"""

    def __int__(self) -> int:
        return self.value

