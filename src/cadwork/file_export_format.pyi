from enum import IntEnum, unique

@unique
class file_export_format(IntEnum):
    """Identifies the concrete format of a file export options instance.

    Examples:
        >>> import cadwork
        >>> import file_controller as fc
        >>> options = fc.get_step_export_options()
        >>> options.get_file_export_format() == cadwork.file_export_format.step
        True

    """

    sat = 0
    """SAT export format."""
    step = 1
    """STEP export format."""
    iges = 2
    """IGES export format."""

    def __int__(self) -> int:
        return self.value
