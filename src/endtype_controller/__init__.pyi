from typing import List

def get_last_error(error_code: int) -> str:
    """get last error

    Parameters:
        error_code: error_code

    Returns:
        str
    """

def get_endtype_id(name: str) -> int:
    """Gets the endtypeID by endtypename

    Parameters:
        name: name

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Tenon_100x50"
        >>> endtype_id = etc.get_endtype_id(endtype_name)
        >>> print(f"Endtype ID: {endtype_id}")

    Returns:
        int
    """

def get_endtype_id_start(element_id: int) -> int:
    """Gets the endtypeID of the start face

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_endtype_id = etc.get_endtype_id_start(element)
        >>> print(f"Start endtype ID: {start_endtype_id}")

    Returns:
        int
    """

def get_endtype_id_end(element_id: int) -> int:
    """Gets the endtypeID of the end face

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_endtype_id = etc.get_endtype_id_end(element)
        >>> print(f"End endtype ID: {end_endtype_id}")

    Returns:
        int
    """


def get_endtype_id_facet(element_id: int, face_number: int) -> int:
    """get endtype id facet

    Parameters:
        element_id: element_id
        face_number: face_number

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
        int
    """

def set_endtype_name_start(element_id: int, name: str) -> None:
    """Sets the endtype to start face by endtypename

    Parameters:
        element_id: element_id
        name: name

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Tenon_100x50"
        >>> etc.set_endtype_name_start(element, endtype_name)

    Returns:
        None
    """

def set_endtype_name_end(element_id: int, name: str) -> None:
    """Sets the endtype to end face by endtypename

    Parameters:
        element_id: element_id
        name: name

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Mortise_100x50"
        >>> etc.set_endtype_name_end(element, endtype_name)

    Returns:
        None
    """


def set_endtype_name_facet(element_id: int, name: str, face_number: int) -> None:
    """set endtype name facet

    Parameters:
        element_id: element_id
        name: name
        face_number: face_number

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

    Returns:
        None
    """

def set_endtype_id_start(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to start face by endtypeID

    Parameters:
        element_id: element_id
        endtype_id: endtype_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 12345
        >>> etc.set_endtype_id_start(element, endtype_id)

    Returns:
        None
    """

def set_endtype_id_end(element_id: int, endtype_id: int) -> None:
    """Sets the endtype to end face by endtypeID

    Parameters:
        element_id: element_id
        endtype_id: endtype_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 54321
        >>> etc.set_endtype_id_end(element, endtype_id)

    Returns:
        None
    """


def set_endtype_id_facet(element_id: int, endtype_id: int, face_number: int) -> None:
    """set endtype id facet

    Parameters:
        element_id: element_id
        endtype_id: endtype_id
        face_number: face_number

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

    Returns:
        None
    """

def create_new_endtype(endtype_name: str, endtype_id: int, folder_name: str) -> int:
    """Creates a new Endtype

    Parameters:
        endtype_name: endtype_name
        endtype_id: endtype_id
        folder_name: folder_name

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Custom_Joint_80x40"
        >>> endtype_id = 99999
        >>> folder_name = "Custom_Joints"
        >>> new_id = etc.create_new_endtype(endtype_name, endtype_id, folder_name)
        >>> print(f"Created endtype with ID: {new_id}")

    Returns:
        int
    """

def get_endtype_name(element_id: int) -> str:
    """Gets the endtypename by endtypeID

    Parameters:
        element_id: element_id

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_id = 12345
        >>> endtype_name = etc.get_endtype_name(endtype_id)
        >>> print(f"Endtype name: {endtype_name}")

    Returns:
        str
    """

def get_endtype_name_start(element_id: int) -> str:
    """Gets the endtypename of the start face

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_name = etc.get_endtype_name_start(element)
        >>> print(f"Start endtype name: {start_name}")

    Returns:
        str
    """

def get_endtype_name_end(element_id: int) -> str:
    """Gets the endtypename of the end face

    Parameters:
        element_id: element_id

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_name = etc.get_endtype_name_end(element)
        >>> print(f"End endtype name: {end_name}")

    Returns:
        str
    """

def get_endtype_name_facet(element_id: int, face_number: int) -> str:
    """get endtype name facet

    Parameters:
        element_id: element_id
        face_number: face_number

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
        str
    """

def get_existing_tenon_ids() -> List[int]:
    """Get the existing tenon endtypeIDs

    Examples:
        >>> import endtype_controller as etc

        >>> tenon_ids = etc.get_existing_tenon_ids()
        >>> print(f"Available tenon endtype IDs: {tenon_ids}")

    Returns:
        list of existing tenon endtypeIDs
    """

def get_existing_lengthening_ids() -> List[int]:
    """Get the existing lengthening endtypeIDs

    Examples:
        >>> import endtype_controller as etc

        >>> lengthening_ids = etc.get_existing_lengthening_ids()
        >>> print(f"Available lengthening endtype IDs: {lengthening_ids}")

    Returns:
        list of existing lengthening endtypeIDs
    """

def get_existing_dovetail_ids() -> List[int]:
    """Get the existing dovetail endtypeIDs

    Examples:
        >>> import endtype_controller as etc

        >>> dovetail_ids = etc.get_existing_dovetail_ids()
        >>> print(f"Available dovetail endtype IDs: {dovetail_ids}")

    Returns:
        list of existing dovetail endtypeIDs
    """

def get_existing_dovetail_dado_ids() -> List[int]:
    """Get the existing dado endtypeIDs

    Examples:
        >>> import endtype_controller as etc

        >>> dado_ids = etc.get_existing_dovetail_dado_ids()
        >>> print(f"Available dado endtype IDs: {dado_ids}")

    Returns:
        list of existing dado endtypeIDs
    """

def get_existing_japanese_tenon_ids() -> List[int]:
    """Get the existing japanese-tenon endtypeIDs

    Examples:
        >>> import endtype_controller as etc

        >>> japanese_tenon_ids = etc.get_existing_japanese_tenon_ids()
        >>> print(f"Available japanese-tenon endtype IDs: {japanese_tenon_ids}")

    Returns:
        list of existing japanese-tenon endtypeIDs
    """

def start_endtype_dialog() -> int:
    """Start endtype dialog

    Examples:
        >>> import endtype_controller as etc

        >>> selected_endtype_id = etc.start_endtype_dialog()
        >>> print(f"User selected endtype ID: {selected_endtype_id}")

    Returns:
        Selected endtypeID
    """
