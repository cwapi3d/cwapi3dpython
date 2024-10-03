from enum import IntEnum, unique


@unique
class bim_team_upload_result_code(IntEnum):
    """bim team upload result code

    Examples:
        >>> cadwork.bim_team_upload_result_code.ok
        ok
    """
    ok = 0
    """"""
    error_general_error = 1
    """"""
    error_too_many_models = 2
    """"""
    error_insufficient_storage = 3
    """"""
    error_invalid_project_id = 4
    """"""
    error_authentication_failed = 5
    """"""

    def __int__(self) -> int:
        return self.value
