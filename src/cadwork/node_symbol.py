from enum import IntEnum, unique


@unique
class node_symbol(IntEnum):
    """Change node symbol. 

    Examples:
        >>> point = cadwork.point_3d(0, 0, 0)
        >>> node = element_controller.create_node(point)
        >>> node.set_node_symbol(node, node_symbol.circle)

    Args:
        SmallCircle (int): 1
        Square (int): 2
        Cross (int): 3
        Circle (int): 4
        FilledCircle (int): 5
        ChessSquare (int): 6
        HalfFilledSquare (int): 7
        CrossSquare (int): 8
        FilledSquare (int): 9  
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
