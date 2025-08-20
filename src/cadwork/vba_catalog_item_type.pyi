from enum import IntEnum, unique


@unique
class vba_catalog_item_type(IntEnum):
    """ Enumeration for vba item types.

    Examples:
        >>> cadwork.vba_catalog_item_type.nut
        nut
    """
    null = 0
    """"""
    nut = 1
    """"""
    washer = 2
    """"""
    wpecial_ring = 3
    """"""
    square_washer = 4
    """"""
    wooden_plug = 5
    """"""
    bolt_with_head = 10001
    """"""
    bolt_without_head = 10002
    """"""
    lag_bolt = 10003
    """"""
    bolt_peg = 10004
    """"""
    normal_screw = 10005
    """"""
    wooden_dowl = 10006
    """"""
    bolt_anchor = 10007
    """"""
    bolt_with_mushroom_head = 10008
    """"""
    bolt_with_conical_head = 10009
    """"""
    bolt_with_head_and_washer = 10010
    """"""
    hanger_bolt = 10011
    """"""
    connection_screw = 10012
    """"""

    def __int__(self) -> int:
        return self.value
