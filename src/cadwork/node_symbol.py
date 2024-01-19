from enum import IntEnum, unique


@unique
class node_symbol(IntEnum):
    """node symbol

    Examples:
        >>> cadwork.node_symbol.SmallSquare
        SmallSquare

    Args:
        SmallSquare = 1
        Square = 2
        Cross = 3
        Circle = 4
        FilledCircle = 5
        ChessSquare = 6
        HalfFilledSquare = 7
        CrossSquare = 8
        FilledSquare = 9

    """
    SmallSquare = 1
    Square = 2
    Cross = 3
    Circle = 4
    FilledCircle = 5
    ChessSquare = 6
    HalfFilledSquare = 7
    CrossSquare = 8
    FilledSquare = 9

    def __int__(self) -> int:
        return self.value

