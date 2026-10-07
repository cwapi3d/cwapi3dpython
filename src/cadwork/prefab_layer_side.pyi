from enum import IntEnum, unique

@unique
class prefab_layer_side(IntEnum):
    """prefab layer side

    Examples:
        >>> cadwork.prefab_layer_side.referenceElement
        referenceElement
    """

    referenceElement = 0
    """The reference element's own layer ("Riegelwerk") — the centre column of the dialog."""
    referenceSide = 1
    """A layer on the reference face of the element ("Bund Schicht")."""
    oppositeSide = 2
    """A layer on the side facing away from the reference face ("Gegen Schicht")."""

    def __int__(self) -> int:
        return self.value
