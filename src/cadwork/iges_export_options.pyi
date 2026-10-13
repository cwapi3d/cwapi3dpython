from .file_export_options import file_export_options

class iges_export_options(file_export_options):
    """IGES export options.

    Inherits the element level-of-detail options from `file_export_options`.
    """

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
