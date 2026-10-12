from typing import ClassVar

from .file_export_options import file_export_options


class step_export_options(file_export_options):
    """STEP export options.

    Inherits the element level-of-detail options from `file_export_options`.
    """

    AP203: ClassVar[int] = 203
    AP214: ClassVar[int] = 214

    def __init__(self) -> None: ...

    def get_scale_factor(self) -> float:
        """Gets the file scale factor.

        Returns:
            The file scale factor.
        """

    def set_scale_factor(self, value: float) -> None:
        """Sets the file scale factor.

        Parameters:
            value: The file scale factor.
        """

    def get_version(self) -> int:
        """Gets the STEP AP version to use.

        Returns:
            The STEP AP version (see the `AP203` / `AP214` constants).
        """

    def set_version(self, value: int) -> None:
        """Sets the STEP AP version to use.

        Any int is accepted, so a version not named by the constants can be passed directly.

        Parameters:
            value: The STEP AP version (e.g. `step_export_options.AP214`).
        """

    def get_imperial_units(self) -> bool:
        """Gets whether imperial units are used.

        Returns:
            Whether imperial units are used.
        """

    def set_imperial_units(self, value: bool) -> None:
        """Sets whether imperial units are used.

        Parameters:
            value: Whether imperial units are used.
        """
