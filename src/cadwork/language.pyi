from enum import IntEnum, unique

@unique
class language(IntEnum):
    """Available cadwork UI languages for set_language().

    The numeric values are cadwork language IDs; each member is documented with the ISO code returned by get_language().

    Examples:
        >>> cadwork.language.german
        german
    """

    english = 0
    """en"""
    german = 1
    """de"""
    french = 2
    """fr"""
    italian = 3
    """it"""
    spanish = 4
    """es"""
    czech = 5
    """cs"""
    finnish = 6
    """fi"""
    russian = 7
    """ru"""
    polish = 8
    """pl"""
    romanian = 9
    """ro"""
    norwegian = 10
    """no"""
    chinese = 11
    """zh"""
    portuguese = 12
    """pt"""
    estonian = 13
    """et"""
    japanese = 14
    """ja"""
    dutch = 15
    """nl"""
    swedish = 16
    """sv"""

    def __int__(self) -> int:
        return self.value
