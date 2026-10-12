from typing import ClassVar

from .file_export_options import file_export_options


class sat_export_options(file_export_options):
    """SAT export options.

    Inherits the element level-of-detail options from `file_export_options`.
    """

    ACIS_V21_0: ClassVar[int] = 2100
    ACIS_V32_0: ClassVar[int] = 3200
    ACIS_V33_0: ClassVar[int] = 3300
    ACIS_V34_0: ClassVar[int] = 3400

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

    def get_binary(self) -> bool:
        """Gets whether to write the SAT file in binary or a human-readable format.

        Returns:
            Whether to write the SAT file in binary or a human-readable format.
        """

    def set_binary(self, value: bool) -> None:
        """Sets whether to write the SAT file in binary or a human-readable format.

        Parameters:
            value: Whether to write the SAT file in binary or a human-readable format.
        """

    def get_version(self) -> int:
        """Gets the ACIS version to use.

        Returns:
            The ACIS version (see the `ACIS_V*` constants, e.g. `ACIS_V33_0` = 3300).
        """

    def set_version(self, value: int) -> None:
        """Sets the ACIS version to use.

        Any int is accepted, so a version not named by the `ACIS_V*` constants can be passed directly.

        Parameters:
            value: The ACIS version (e.g. `sat_export_options.ACIS_V33_0`).
        """
