from enum import IntEnum, unique


@unique
class event_type(IntEnum):
    """event type

    Examples:
        >>> cadwork.event_type.on_activate
        on_activate
    """
    on_activate = 0
    """"""
    on_hide = 1
    """"""
    on_show = 2
    """elements became visible; aElementIDs holds the affected elements"""
    on_close = 3
    """"""
    on_geometry = 4
    """an element's geometry changed; aElementIDs holds the affected element"""
    on_attribute = 5
    """an element's attribute changed; aElementIDs holds the affected element"""

    def __int__(self) -> int:
        return self.value
