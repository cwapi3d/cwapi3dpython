from typing import List
from cadwork.api_types import *

def get_endtype_id(name: str) -> EndtypeId:
    """Gets the endtype id by endtype name.

    Parameters:
        name: The endtype name.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Tenon_100x50"
        >>> endtype_id = etc.get_endtype_id(endtype_name)
        >>> print(f"Endtype ID: {endtype_id}")

    Returns:
        The wanted endtype id.
    """

def get_endtype_id_start(element_id: ElementId) -> EndtypeId:
    """Gets the endtype id of the start face.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_endtype_id = etc.get_endtype_id_start(element)
        >>> print(f"Start endtype ID: {start_endtype_id}")

    Returns:
        The wanted endtype id.
    """

def get_endtype_id_end(element_id: ElementId) -> EndtypeId:
    """Gets the endtype id of the end face.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_endtype_id = etc.get_endtype_id_end(element)
        >>> print(f"End endtype ID: {end_endtype_id}")

    Returns:
        The wanted endtype id.
    """


def get_endtype_id_facet(element_id: ElementId, face_number: int) -> EndtypeId:
    """Gets the endtype id of a face with the face number.

    Parameters:
        element_id: The element id.
        face_number: The face number. 0 <= aFaceNumber < element face count.

    Note:
        Endtypes can only be set on faces that are placed at start or end points.
        Endtypes cannot be placed on arbitrary faces.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> face_number = 1
        >>> facet_endtype_id = etc.get_endtype_id_facet(element, face_number)
        >>> print(f"Facet endtype ID: {facet_endtype_id}")

    Returns:
        The wanted endtype id.
    """

def set_endtype_name_start(element_id: ElementId, name: str) -> None:
    """Sets the endtype to start face by endtype name.

    Parameters:
        element_id: The element id.
        name: The endtype name.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Tenon_100x50"
        >>> etc.set_endtype_name_start(element, endtype_name)
    """

def set_endtype_name_end(element_id: ElementId, name: str) -> None:
    """Sets the endtype to end face by endtype name.

    Parameters:
        element_id: The element id.
        name: The endtype name.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Mortise_100x50"
        >>> etc.set_endtype_name_end(element, endtype_name)
    """


def set_endtype_name_facet(element_id: ElementId, name: str, face_number: int) -> None:
    """Sets the endtype to a face by endtype name.

    Parameters:
        element_id: The element id.
        name: The endtype name.
        face_number: The face number. 0 <= aFaceNumber < element face count.

    Note:
        Endtypes can only be set on faces that are placed at start or end points.
        Endtypes cannot be placed on arbitrary faces.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Dovetail_60x30"
        >>> face_number = 2
        >>> etc.set_endtype_name_facet(element, endtype_name, face_number)
    """

def set_endtype_id_start(element_id: ElementId, endtype_id: EndtypeId) -> None:
    """Sets the endtype to start face by endtype id.

    Parameters:
        element_id: The element id.
        endtype_id: The endtype id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 12345
        >>> etc.set_endtype_id_start(element, endtype_id)
    """

def set_endtype_id_end(element_id: ElementId, endtype_id: EndtypeId) -> None:
    """Sets the endtype to end face by endtype id.

    Parameters:
        element_id: The element id.
        endtype_id: The endtype id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 54321
        >>> etc.set_endtype_id_end(element, endtype_id)
    """


def set_endtype_id_facet(element_id: ElementId, endtype_id: EndtypeId, face_number: int) -> None:
    """Sets the endtype to a face by endtype id.

    Parameters:
        element_id: The element id.
        endtype_id: The endtype id.
        face_number: The face number. 0 <= aFaceNumber < element face count.

    Note:
        Endtypes can only be set on faces that are placed at start or end points.
        Endtypes cannot be placed on arbitrary faces.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 67890
        >>> face_number = 3
        >>> etc.set_endtype_id_facet(element, endtype_id, face_number)
    """

def create_new_endtype(endtype_name: str, endtype_id: EndtypeId, folder_name: str) -> EndtypeId:
    """Creates a new Endtype.

    Parameters:
        endtype_name: The new endtype name.
        endtype_id: The new endtype id.
        folder_name: The new endtype folder.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Custom_Joint_80x40"
        >>> endtype_id = 99999
        >>> folder_name = "Custom_Joints"
        >>> new_id = etc.create_new_endtype(endtype_name, endtype_id, folder_name)
        >>> print(f"Created endtype with ID: {new_id}")

    Returns:
        The ID of the created endtype.
    """

def get_endtype_name(element_id: ElementId) -> str:
    """Gets the endtype name by endtype id.

    Parameters:
        element_id: The endtype id.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_id = 12345
        >>> endtype_name = etc.get_endtype_name(endtype_id)
        >>> print(f"Endtype name: {endtype_name}")

    Returns:
        The endtype name.
    """

def get_endtype_name_start(element_id: ElementId) -> str:
    """Gets the endtype name of the start face.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_name = etc.get_endtype_name_start(element)
        >>> print(f"Start endtype name: {start_name}")

    Returns:
        The endtype name of the start face.
    """

def get_endtype_name_end(element_id: ElementId) -> str:
    """Gets the endtype name of the end face.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_name = etc.get_endtype_name_end(element)
        >>> print(f"End endtype name: {end_name}")

    Returns:
        The endtype name of the end face.
    """

def get_endtype_name_facet(element_id: ElementId, face_number: int) -> str:
    """Gets the endtype name of the face with a number.

    Parameters:
        element_id: The element id.
        face_number: The face number. 0 <= aFaceNumber < element face count.

    Note:
        Endtypes can only be set on faces that are placed at start or end points.
        Endtypes cannot be placed on arbitrary faces.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> face_number = 2
        >>> facet_name = etc.get_endtype_name_facet(element, face_number)
        >>> print(f"Facet endtype name: {facet_name}")

    Returns:
        The endtype name of the face.
    """

def get_existing_tenon_ids() -> List[EndtypeId]:
    """Get the existing tenon endtype id list.

    Examples:
        >>> import endtype_controller as etc

        >>> tenon_ids = etc.get_existing_tenon_ids()
        >>> print(f"Available tenon endtype IDs: {tenon_ids}")

    Returns:
        List of existing tenon endtype id.
    """

def get_existing_lengthening_ids() -> List[EndtypeId]:
    """Get the existing lengthening endtype id list.

    Examples:
        >>> import endtype_controller as etc

        >>> lengthening_ids = etc.get_existing_lengthening_ids()
        >>> print(f"Available lengthening endtype IDs: {lengthening_ids}")

    Returns:
        List of existing lengthening endtype id.
    """

def get_existing_dovetail_ids() -> List[EndtypeId]:
    """Get the existing dovetail endtype id list.

    Examples:
        >>> import endtype_controller as etc

        >>> dovetail_ids = etc.get_existing_dovetail_ids()
        >>> print(f"Available dovetail endtype IDs: {dovetail_ids}")

    Returns:
        List of existing dovetail endtype id.
    """

def get_existing_dovetail_dado_ids() -> List[EndtypeId]:
    """Get the existing dado endtype id list.

    Examples:
        >>> import endtype_controller as etc

        >>> dado_ids = etc.get_existing_dovetail_dado_ids()
        >>> print(f"Available dado endtype IDs: {dado_ids}")

    Returns:
        List of existing dado endtype id.
    """

def get_existing_japanese_tenon_ids() -> List[EndtypeId]:
    """Get the existing japanese-tenon endtype id list.

    Examples:
        >>> import endtype_controller as etc

        >>> japanese_tenon_ids = etc.get_existing_japanese_tenon_ids()
        >>> print(f"Available japanese-tenon endtype IDs: {japanese_tenon_ids}")

    Returns:
        List of existing japanese-tenon endtype id.
    """

def start_endtype_dialog() -> int:
    """Start endtype dialog.

    Examples:
        >>> import endtype_controller as etc

        >>> selected_endtype_id = etc.start_endtype_dialog()
        >>> print(f"User selected endtype ID: {selected_endtype_id}")

    Returns:
        Selected endtype id.
    """
