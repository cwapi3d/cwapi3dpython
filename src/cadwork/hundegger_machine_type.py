from enum import IntEnum, unique


@unique
class hundegger_machine_type(IntEnum):
    """Hundegger machine type.

    Examples:
        >>> machine_controller.export_hundegger(hundegger_machine_type.k2)

    Args:
        p8_10 (int): 1
        k1 (int): 2
        k2 (int): 3
        k2_cambium (int): 4
        k2_uf_5 (int): 5
        k2_uf_5_cambium (int): 6
        speedcut (int): 7
        pba (int): 8
        pba_bvx (int): 9
        pba_bvx_cambium (int): 10
        spm (int): 12
        spm_cambium (int): 13
        robot_drive (int): 14
        turbo_drive (int): 15

    """

    p8_10 = 1
    k1 = 2
    k2 = 3
    k2_cambium = 4
    k2_uf_5 = 5
    k2_uf_5_cambium = 6
    speedcut = 7
    pba = 8
    pba_bvx = 9
    pba_bvx_cambium = 10
    spm = 12
    spm_cambium = 13
    robot_drive = 14
    turbo_drive = 15

    def __int__(self) -> int:
        return self.value
