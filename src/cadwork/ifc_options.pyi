from cadwork.ifc_options_aggregation import ifc_options_aggregation
from cadwork.ifc_options_level_of_detail import ifc_options_level_of_detail
from cadwork.ifc_options_project_data import ifc_options_project_data
from cadwork.ifc_options_properties import ifc_options_properties


class ifc_options:

    def get_ifc_options_properties(self) -> ifc_options_properties:
        """Get IFC options properties.

        Returns:
            ifc_options_properties: The IFC properties options.
        """

    def get_ifc_options_project_data(self) -> ifc_options_project_data:
        """Get IFC options project data.

        Returns:
            ifc_options_project_data: The IFC project data options.
        """

    def get_ifc_options_aggregation(self) -> ifc_options_aggregation:
        """Get IFC options aggregation.

        Returns:
            ifc_options_aggregation: The IFC aggregation options.
        """

    def get_ifc_options_level_of_detail(self) -> ifc_options_level_of_detail:
        """Get IFC options level of detail.

        Returns:
            ifc_options_level_of_detail: The IFC level of detail options.
        """
