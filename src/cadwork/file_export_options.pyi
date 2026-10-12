from .element_level_of_detail_options import element_level_of_detail_options
from .file_export_format import file_export_format


class file_export_options:
    """Common base for all format-specific export options (SAT, STEP, IGES, ...).

    Passed to `file_controller.export_file_with_options()`; the concrete subclass
    determines the exported file format.
    """

    def get_file_export_format(self) -> file_export_format:
        """Gets the concrete export format this instance decorates.

        Returns:
            The file export format.
        """

    def get_level_of_detail_options(self) -> element_level_of_detail_options:
        """Gets the agnostic element level-of-detail options decorating this export.

        Returns:
            The element level-of-detail options.
        """
