from typing import List
from cadwork.ifc_2x3_element_type import ifc_2x3_element_type
from cadwork.ifc_options import ifc_options
from cadwork.ifc_predefined_type import ifc_predefined_type


def get_last_error(a0: int) -> str:
    """get last error

    Parameters:
        a0: a0

    Returns:
        str
    """

def get_ifc_guid(element_id: int) -> str:
    """get ifc guid

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_guid = bc.get_ifc_guid(element)
        >>> print(f"IFC GUID: {ifc_guid}")

    Returns:
        str
    """

def get_ifc2x3_element_type(element_id: int) -> ifc_2x3_element_type:
    """get ifc2x3 element type

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork # needed for ifc_2x3_element_type

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element)

    Returns:
        ifc_2x3_element_type
    """


def set_ifc2x3_element_type(element_i_ds: List[int], ifc_type: ifc_2x3_element_type) -> None:
    """set ifc2x3 element type

    Parameters:
        element_i_ds: element_i_ds
        ifc_type: element_type

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_entity_type = cadwork.ifc_2x3_element_type()
        >>> ifc_entity_type.set_ifc_member()
        >>> bc.set_ifc2x3_element_type(selected_elements, ifc_entity_type)

    Returns:
        None
    """

def import_ifc_as_graphical_object(file_path: str) -> bool:
    """import ifc as graphical object

    Parameters:
        file_path: file_path

    Examples:
        >>> import bim_controller as bc

        >>> ifc_file_path = r"C:/imports/building_model.ifc"
        >>> success = bc.import_ifc_as_graphical_object(ifc_file_path)
        >>> if success:
        >>>     print("IFC imported as graphical object successfully")

    Returns:
        bool
    """

def import_bcf(file_path: str) -> bool:
    """import bcf

    Parameters:
        file_path: file_path

    Examples:
        >>> import bim_controller as bc

        >>> bcf_file_path = r"C:/imports/issues.bcf"
        >>> success = bc.import_bcf(bcf_file_path)
        >>> if success:
        >>>     print("BCF file imported successfully")

    Returns:
        bool
    """

def export_bcf(file_path: str) -> bool:
    """export bcf

    Parameters:
        file_path: file_path

    Examples:
        >>> import bim_controller as bc

        >>> bcf_output_path = r"C:/exports/project_issues.bcf"
        >>> success = bc.export_bcf(bcf_output_path)
        >>> if success:
        >>>     print("BCF file exported successfully")

    Returns:
        bool
    """

def export_ifc(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_output_path = r"C:/exports/building_model.ifc"
        >>> success = bc.export_ifc(selected_elements, ifc_output_path)
        >>> if success:
        >>>     print("IFC file exported successfully")

    Returns:
        bool
    """

def import_ifc_return_exchange_objects(file_path: str) -> List[int]:
    """imports an IFC File and returns the ids of the Exchange Objects

    Parameters:
        file_path: file_path

    Returns:
        List[int]
    """

def set_storey_height(building: str, storey: str, height: float) -> None:
    """set storey height

    Parameters:
        building: building
        storey: storey
        height: height

    Examples:
        >>> import bim_controller as bc

        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> height_millimeters = 3_500
        >>> bc.set_storey_height(building_name, storey_name, height_millimeters)

    Returns:
        None
    """

def convert_exchange_objects(exchange_objects: List[int]) -> List[int]:
    """converts a list of Exchange Objects to Cadwork Elements

    Parameters:
        exchange_objects: exchange_objects

    Returns:
        List[int]
    """

def export_ifc2x3_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc2x3 silently

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Returns:
        bool
    """

def export_ifc4_silently(element_i_ds: List[int], file_path: str) -> bool:
    """export ifc4 silently

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path

    Returns:
        bool
    """

def export_ifc2x3_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc2x3 silently with options

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path
        options: options

    Returns:
        bool
    """

def export_ifc4_silently_with_options(element_i_ds: List[int], file_path: str, options: ifc_options) -> bool:
    """export ifc4 silently with options

    Parameters:
        element_i_ds: element_i_ds
        file_path: file_path
        options: options

    Returns:
        bool
    """

def update_bmt_structure_created_elements(element_i_ds: List[int]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the active building and storey.

    Parameters:
        element_i_ds: element_i_ds

    Returns:
        None
    """

def update_bmt_structure_building_storey(element_i_ds: List[int]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the assigned Building and Storey.

    Parameters:
        element_i_ds: element_i_ds

    Returns:
        None
    """

def get_ifc_options() -> ifc_options:
    """Get the IfcOptions with the settings used in the document

    Returns:
        ifc_options
    """

def set_building_and_storey(element_id_list: List[int], building: str, storey: str) -> None:
    """set building and storey

    Parameters:
        element_id_list: element_id_list
        building: building
        storey: storey

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> bc.set_building_and_storey(selected_elements, building_name, storey_name)

    Returns:
        None
    """

def get_building(element: int) -> str:
    """get building

    Parameters:
        element: element

    Returns:
        str
    """

def get_storey(element: int) -> str:
    """get storey

    Parameters:
        element: element

    Returns:
        str
    """

def get_storey_height(building: str, storey: str) -> float:
    """get storey height

    Parameters:
        building: building
        storey: storey

    Returns:
        float
    """


def get_ifc2x3_element_type_string(entity_type: ifc_2x3_element_type) -> str:
    """get ifc2x3 element type string

    Parameters:
        entity_type: entity_type

    Returns:
        str
    """


def get_ifc2x3_element_type_display_string(entity_type: ifc_2x3_element_type) -> str:
    """get ifc2x3 element type display string

    Parameters:
        entity_type: entity_type

    Returns:
        str
    """

def get_all_buildings() -> List[str]:
    """get all buildings

    Returns:
        List[str]
    """

def get_all_storeys(building: str) -> List[str]:
    """get all storeys

    Parameters:
        building: building

    Returns:
        List[str]
    """


def get_element_id_from_base64_ifc_guid(base_64_ifc_guid: str) -> int:
    """get element id from base64 ifc guid

    Parameters:
        base_64_ifc_guid: base_64_ifc_guid

    Returns:
        int
    """

def get_ifc_base64_guid(element_id: int) -> str:
    """Get IFC base64 Guid from element ID

    Parameters:
        element_id: element_id

    Returns:
        The IFC GUID in base64 string format ("28kif20KPEuBjk2m1N3ep$").
    """

def get_ifc_predefined_type(element_id: int) -> 'ifc_predefined_type':
    """Get the IfcPredefinedType of an element.

    Parameters:
        element_id: element_id

    Returns:
        IfcPredefinedType Wrapper
    """


def set_ifc_predefined_type(element_i_ds: List[int], predefined_type: ifc_predefined_type) -> None:
    """Set a predefined type to elements. Attention, if you change the PredefinedType of the elements, you are responsible for ensuring that valid types are set

    Parameters:
        element_i_ds: element_i_ds
        predefined_type: predefined_type

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> predefined_type = cadwork.ifc_predefined_type()
        >>> predefined_type.set_member()
        >>> bc.set_ifc_predefined_type(selected_elements, predefined_type)

    Returns:
        None
    """
