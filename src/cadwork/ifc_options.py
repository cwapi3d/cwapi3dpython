from .ifc_element_combine_behaviour import ifc_element_combine_behaviour
from .element_grouping_type import element_grouping_type


class ifc_options:
    """
    ifc_options class

    Examples:
        >>> import cadwork
        >>> import bim_controller
        >>> import element_controller
        >>> ifc_options = cadwork.ifc_options()
        >>> ifc_options_level_of_detail = ifc_options.get_ifc_options_level_of_detail()
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_cut_drillings(True)
        >>> ifc_options_level_of_detail.get_cut_drillings()
        >>> ifc_options_level_of_detail.set_export_vba_drillings(True)
        >>> ifc_options_level_of_detail.set_export_vba_components(True)
        >>> element_ids = element_controller.get_active_identifiable_element_ids()
        >>> bim_controller.export_ifc4_silently_with_options(element_ids, "C:\\some_path\\test.ifc", ifc_options)
    """

    def __init__(self) -> None:
        pass

    def get_ifc_options_project_data(self):
        """
        Examples:
            >>> ifc_options = ifc_options()
            >>> ifc_options_project_data = ifc_options.get_ifc_options_project_data()
        """
        pass

    def get_ifc_options_properties(self):
        """
        Examples:
            >>> ifc_options = ifc_options()
            >>> ifc_options_properties = ifc_options.get_ifc_options_properties()
        """
        pass

    def get_ifc_options_level_of_detail(self):
        """
        Examples:
            >>> ifc_options = ifc_options()
            >>> ifc_options_level_of_detail = ifc_options.get_ifc_options_level_of_detail()
        """
        pass

    def get_ifc_options_aggregation(self):
        """
        Examples:
            >>> ifc_options = ifc_options()
            >>> ifc_options_aggregation = ifc_options.get_ifc_options_aggregation()
        """
        pass

    class ifc_options_project_data():
        """
        settings for project data
        """

        def __init__(self) -> None:
            pass

        def get_export_project_name_as_ifc_project(self) -> bool:
            pass

        def set_export_project_name_as_ifc_project(self, value: bool) -> None:
            pass

        def get_export_adress_in_ifc_site(self) -> bool:
            pass

        def set_export_adress_in_ifc_site(self, value: bool) -> None:
            pass

        def get_export_coordinates_in_ifc_site(self) -> bool:
            pass

        def set_export_coordinates_in_ifc_site(self, value: bool) -> None:
            pass

        def get_export_project_name_as_ifc_building(self) -> bool:
            pass

        def set_export_project_name_as_ifc_building(self, value: bool) -> None:
            pass

    class ifc_options_properties():
        """
        settings for properties
        """

        def __init__(self) -> None:
            pass

        def get_attribute_nr_ifc_layer(self) -> int:
            pass

        def set_attribute_nr_ifc_layer(self, value: bool) -> None:
            pass

        def get_attriubte_nr_ifc_tag(self) -> int:
            pass

        def set_attribute_nr_ifc_tag(self, value: bool) -> None:
            pass

        def get_export_empty_building_and_storeys(self) -> bool:
            pass

        def set_export_empty_building_and_storeys(self, value: bool) -> None:
            pass

        def get_export_cadwork_3d_pset(self) -> bool:
            pass

        def set_export_cadwork_3d_pset(self, value: bool) -> None:
            pass

        def get_ignore_user_attributes_used_in_psets(self) -> bool:
            pass

        def set_ignore_user_attributes_used_in_psets(self, value: bool) -> None:
            pass

        def get_export_bim_wood_property(self) -> bool:
            pass

        def set_export_bim_wood_property(self, value: bool) -> None:
            pass

    class ifc_options_level_of_detail():
        """
        settings for level of detail
        """

        def __init__(self) -> None:
            pass

        def get_export_endtype_materialization(self) -> bool:
            pass

        def set_export_endtype_materialization(self, value: bool) -> None:
            pass

        def get_cut_endtype_counterparts(self) -> bool:
            pass

        def set_cut_endtype_counterparts(self, value: bool) -> None:
            pass

        def get_export_vba_drillings(self) -> bool:
            pass

        def set_export_vba_drillings(self, value: bool) -> None:
            pass

        def get_export_vba_components(self) -> bool:
            pass

        def set_export_vba_components(self, value: bool) -> None:
            pass

        def get_cut_drillings(self) -> bool:
            pass

        def set_cut_drillings(self, value: bool) -> None:
            pass

        def get_export_installation_round_materialization(self) -> bool:
            pass

        def set_export_installation_round_materialization(self, value: bool) -> None:
            pass

        def get_export_installation_rectangular_materialization(self) -> bool:
            pass

        def set_export_installation_rectangular_materialization(self, value: bool) -> None:
            pass

        def get_cut_installation_round(self) -> bool:
            pass

        def set_cut_installation_round(self, value: bool) -> None:
            pass

        def get_cut_installation_rectangular(self) -> bool:
            pass

        def set_cut_installation_rectangular(self, value: bool) -> None:
            pass

        def get_export_experimental_swept_solid_materialization(self) -> bool:
            pass

        def set_export_experimental_swept_solid_materialization(self, value: bool) -> None:
            pass

    class ifc_options_aggregation():
        """
        settings for aggregation
        """

        def __init__(self) -> None:
            pass

        def get_consider_element_aggregation(self) -> bool:
            pass

        def set_consider_element_aggregation(self, value: bool) -> None:
            pass

        def get_element_aggregation_attribute(self) -> element_grouping_type:
            pass

        def set_element_aggregation_attribute(self, value: element_grouping_type) -> None:
            pass

        def get_element_combine_type(self) -> ifc_element_combine_behaviour:
            pass

        def set_element_combine_type(self, value: ifc_element_combine_behaviour) -> None:
            pass

        def get_export_cover_geometry(self) -> bool:
            pass

        def set_export_cover_geometry(self, value: bool) -> None:
            pass
