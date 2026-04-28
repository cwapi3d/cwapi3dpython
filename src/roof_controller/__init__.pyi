"""Roof-surface specific queries and operations.

Concerned with information that only makes sense for roof
surfaces: roof-specific edge classifications (ridge, eave, hip,
valley, ...), profile and edge measurements, and other
analyses that depend on a surface having been designated as a
roof. Conversion of generic surfaces into roof surfaces lives in
element_controller.
"""

from cadwork.api_types import ElementId

def get_profile_length(element_id: ElementId) -> float:
    """Gets the profile length.

    Parameters:
        element_id: The element id.

    Returns:
        The profile length.
    """

def get_edge_length(element_id: ElementId, edge_type: str) -> float:
    """Gets the edge length.

    Parameters:
        element_id: The element id.
        edge_type: The edge type : 

        
            - "none"

            - "ridge"

            - "eave"

            - "vergeright"
            - "vergeleft"
            - "vergeoblique"

            - "hip"

            - "valley"

            - "userdefined1"
            - "userdefined2"

            - "userdefinedmitrejoint1"
            - "userdefinedmitrejoint2"

            - "wallconnection"
            - "wallconnectionright"
            - "wallconnectionleft"
            - "wallconnectiontop"
            - "wallconnectionbottom"

            - "roofcutout"
            - "roofcutoutright"
            - "roofcutoutleft"
            - "roofcutouttop"
            - "roofcutoutbottom"

            - "roofedgeontoproofsurface"
            - "roofedgeonbottomroofsurface"

    Returns:
        The edge length.
    """

def get_all_caddy_element_ids() -> list[ElementId]:
    """Gets all caddy elements

    Returns:
        The list of all caddy element id.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

