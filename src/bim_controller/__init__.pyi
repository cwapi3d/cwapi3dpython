from typing import List
from cadwork.ifc_2x3_element_type import ifc_2x3_element_type
from cadwork.ifc_options import ifc_options
from cadwork.ifc_predefined_type import ifc_predefined_type
from cadwork.api_types import *

def get_ifc_guid(element_id: ElementId) -> str:
    """Get the IFC GUID of an element.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_guid = bc.get_ifc_guid(element)
        >>> print(f"IFC GUID: {ifc_guid}")

    Returns:
        A string representing the IFC GUID.
    """

def get_ifc2x3_element_type(element_id: ElementId) -> ifc_2x3_element_type:
    """Get ifc2x3 element type.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork # needed for ifc_2x3_element_type

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> ifc_type = bc.get_ifc2x3_element_type(element)

    Returns:
        The ifc_2x3_element_type of the element.
    """


def set_ifc2x3_element_type(element_id_list: List[ElementId], ifc_type: ifc_2x3_element_type) -> None:
    """Set ifc2x3 element type.

    Parameters:
        element_id_list: The list of element ids.
        ifc_type: The ifc_2x3_element_type to set.
        
    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_entity_type = cadwork.ifc_2x3_element_type()
        >>> ifc_entity_type.set_ifc_member()
        >>> bc.set_ifc2x3_element_type(selected_elements, ifc_entity_type)
    """

def import_ifc_as_graphical_object(file_path: str) -> bool:
    """Imports ifc as graphical object.

    Parameters:
        file_path: The path to the IFC file.

    Examples:
        >>> import bim_controller as bc

        >>> ifc_file_path = r"C:/imports/building_model.ifc"
        >>> success = bc.import_ifc_as_graphical_object(ifc_file_path)
        >>> if success:
        >>>     print("IFC imported as graphical object successfully")

    Returns:
        True if the import was successful, false otherwise.
    """

def import_bcf(file_path: str) -> bool:
    """Imports a BCF file.

    Parameters:
        file_path: The path to the BCF file.

    Examples:
        >>> import bim_controller as bc

        >>> bcf_file_path = r"C:/imports/issues.bcf"
        >>> success = bc.import_bcf(bcf_file_path)
        >>> if success:
        >>>     print("BCF file imported successfully")

    Returns:
        True if the import was successful, false otherwise.
    """

def export_bcf(file_path: str) -> bool:
    """Exports a BCF file.

    Parameters:
        file_path: The path where the BCF file will be exported.

    Examples:
        >>> import bim_controller as bc

        >>> bcf_output_path = r"C:/exports/project_issues.bcf"
        >>> success = bc.export_bcf(bcf_output_path)
        >>> if success:
        >>>     print("BCF file exported successfully")

    Returns:
        True if the export was successful, false otherwise.
    """

def export_ifc(element_id_list: List[ElementId], file_path: str) -> bool:
    """Export IFC file.

    Parameters:
        element_id_list: The list of element ids.
        file_path: The path where the IFC file will be exported.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> ifc_output_path = r"C:/exports/building_model.ifc"
        >>> success = bc.export_ifc(selected_elements, ifc_output_path)
        >>> if success:
        >>>     print("IFC file exported successfully")

    Returns:
        True if the export was successful, false otherwise.
    """

def import_ifc_return_exchange_objects(file_path: str) -> List[ElementId]:
    """Imports an IFC File and returns the ids of the Exchange Objects.

    Parameters:
        file_path: The path to the IFC file.

    Returns:
        The ids of the exchange objects.
    """

def set_storey_height(building: str, storey: str, height: float) -> None:
    """Set storey height.

    Parameters:
        building: The name of the building.
        storey: The name of the storey.
        height: The height of the storey.

    Examples:
        >>> import bim_controller as bc

        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> height_millimeters = 3_500
        >>> bc.set_storey_height(building_name, storey_name, height_millimeters)
    """

def convert_exchange_objects(exchange_objects: List[ElementId]) -> List[ElementId]:
    """Converts a list of Exchange Objects to Cadwork Elements.

    Parameters:
        exchange_objects: A list of Exchange Object id to convert.

    Returns:
        The list of Cadwork Element ids.
    """

def export_ifc2x3_silently(element_id_list: List[ElementId], file_path: str) -> bool:
    """Export IFC2x3 silently.

    Parameters:
        element_id_list: The list of element ids.
        file_path: The path where the IFC file will be exported.

    Returns:
        True if the export was successful, false otherwise.
    """

def export_ifc4_silently(element_id_list: List[ElementId], file_path: str) -> bool:
    """Exports IFC4 silently.

    Parameters:
        element_id_list: The list of element ids.
        file_path: The path where the IFC file will be exported.

    Returns:
        True if the export was successful, false otherwise.
    """

def export_ifc2x3_silently_with_options(element_id_list: List[ElementId], file_path: str, options: ifc_options) -> bool:
    """Exports IFC2x3 silently with options.

    Parameters:
        element_id_list: The list of element ids.
        file_path: The path where the IFC file will be exported.
        options: The export options.

    Returns:
        True if the export was successful, false otherwise.
    """

def export_ifc4_silently_with_options(element_id_list: List[ElementId], file_path: str, options: ifc_options) -> bool:
    """Exports IFC4 silently with options.

    Parameters:
        element_id_list: The list of element ids.
        file_path: The path where the IFC file will be exported.
        options: The export options.

    Returns:
        True if the export was successful, false otherwise.
    """

def update_bmt_structure_created_elements(element_id_list: List[ElementId]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the active building and storey.

    Parameters:
        element_id_list: The list of element ids to be updated in the BMT structure.
    """

def update_bmt_structure_building_storey(element_id_list: List[ElementId]) -> None:
    """This function takes the specified elements and inserts them into the BMT structure and adds them to the assigned Building and Storey.

    Parameters:
        element_id_list: The list of element ids to be updated in the BMT structure.
    """

def get_ifc_options() -> ifc_options:
    """Get the IfcOptions with the settings used in the document.

    Returns:
        The IfcOptions object containing the current settings.
    """

def set_building_and_storey(element_id_list: List[ElementId], building: str, storey: str) -> None:
    """Set building and storey.

    Parameters:
        element_id_list: The list of element ids.
        building: The building name.
        storey: The storey name.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> building_name = "Building A"
        >>> storey_name = "Ground Floor"
        >>> bc.set_building_and_storey(selected_elements, building_name, storey_name)
    """

def get_building(element_id: ElementId) -> str:
    """Get building name for a given element.

    Parameters:
        element_id: The element id.

    Returns:
        The name of the building.
    """

def get_storey(element_id: ElementId) -> str:
    """Get storey name for a given element.

    Parameters:
        element_id: The element id.

    Returns:
        The name of the storey.
    """

def get_storey_height(building: str, storey: str) -> float:
    """Get storey height for a given building and storey.

    Parameters:
        building: The building name.
        storey: The storey name.

    Returns:
        The height of the storey.
    """


def get_ifc2x3_element_type_string(entity_type: ifc_2x3_element_type) -> str:
    """Get IFC2x3 element type string.

    Parameters:
        entity_type: The entity type.

    Returns:
        The string representation of the IFC2x3 element type.
    """


def get_ifc2x3_element_type_display_string(entity_type: ifc_2x3_element_type) -> str:
    """Get IFC2x3 element type display string.

    Parameters:
        entity_type: The entity type.

    Returns:
        The display string representation of the IFC2x3 element type.
    """

def get_all_buildings() -> List[str]:
    """Get all buildings.

    Returns:
        A list of all building.
    """

def get_all_storeys(building: str) -> List[str]:
    """Get all storeys.

    Parameters:
        building: The building name.

    Returns:
        A list of all storeys in the building.
    """


def get_element_id_from_base64_ifc_guid(base_64_ifc_guid: str) -> ElementId:
    """Get element id from base64 ifc guid.

    Parameters:
        base_64_ifc_guid: The base64 IFC GUID.

    Returns:
        The element id corresponding to the base64 IFC GUID.
    """

def get_ifc_base64_guid(element_id: ElementId) -> str:
    """Get IFC base64 Guid from element id.

    Parameters:
        element_id: The element id.

    Returns:
        The IFC GUID in base64 string format ("28kif20KPEuBjk2m1N3ep$").
    """

def get_ifc_predefined_type(element_id: ElementId) -> 'ifc_predefined_type':
    """Get the IfcPredefinedType of an element.

    Parameters:
        element_id: The element id.

    Returns:
        The IfcPredefinedType of the element.
    """


def set_ifc_predefined_type(element_id_list: List[ElementId], predefined_type: ifc_predefined_type) -> None:
    """Set a predefined type to elements. Attention, if you change the PredefinedType of the elements, you are responsible for ensuring that valid types are set.

    Parameters:
        element_id_list: The list of element ids.
        predefined_type: The predefined type to set.

    Examples:
        >>> import element_controller as ec
        >>> import bim_controller as bc
        >>> import cadwork

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> predefined_type = cadwork.ifc_predefined_type()
        >>> predefined_type.set_member()
        >>> bc.set_ifc_predefined_type(selected_elements, predefined_type)
    """
