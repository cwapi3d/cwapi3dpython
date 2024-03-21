from cadwork import element_grouping_type
from cadwork import ifc_element_combine_behaviour

class ifc_options_aggregation:
    
    def get_export_cover_geometry(self) -> bool:
        """get export cover geometry

        Returns:
            bool
        """

    def set_element_aggregation_attribute(self, element_aggregation_attribute: element_grouping_type) -> None:
        """set element aggregation attribute

        Parameters:
            element_aggregation_attribute: element_aggregation_attribute

        Returns:
            None
        """

    def set_consider_element_aggregation(self, consider_element_aggregation: bool) -> None:
        """set consider element aggregation

        Parameters:
            consider_element_aggregation: consider_element_aggregation

        Returns:
            None
        """

    def get_element_aggregation_attribute(self) -> int:
        """get element aggregation attribute

        Returns:
            int
        """

    def get_consider_element_aggregation(self) -> bool:
        """get consider element aggregation

        Returns:
            bool
        """

    def get_element_combine_type(self) -> ifc_element_combine_behaviour:
        """get element combine type

        Returns:
            ifc_element_combine_behaviour
        """

    def set_export_cover_geometry(self, export_cover_geometry: bool) -> None:
        """set export cover geometry

        Parameters:
            export_cover_geometry: export_cover_geometry

        Returns:
            None
        """

    def set_element_combine_type(self, element_combine_type: ifc_element_combine_behaviour) -> None:
        """set element combine type

        Parameters:
            element_combine_type: element_combine_type

        Returns:
            None
        """

