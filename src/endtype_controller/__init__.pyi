"""End-type joinery: profiled cuts at element faces.

Domain of named joinery profiles (tenons, mortises, dovetails,
custom shapes, ...) applied to the start, end or arbitrary faces
of an element. Covers the catalog (creation, lookup by name and
id), assignment to specific element faces, retrieval of currently
applied end-types, and the interactive selection dialog.
"""

from cadwork.api_types import *

def get_endtype_id(name: str) -> EndtypeId:
    """Return the endtype ID for an endtype name.

    Searches all endtypes in the library for an exact name match.

    Parameters:
        name: Endtype name as shown in the endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Tenon_100x50"
        >>> endtype_id = etc.get_endtype_id(endtype_name)
        >>> print(f"Endtype ID: {endtype_id}")

    Returns:
        Endtype ID of the first endtype with that name, or 0 if the name is empty or not found.
    """

def get_endtype_id_start(element_id: ElementId) -> EndtypeId:
    """Return the endtype ID assigned to the start face of an element.

    Parameters:
        element_id: Element ID.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_endtype_id = etc.get_endtype_id_start(element)
        >>> print(f"Start endtype ID: {start_endtype_id}")

    Returns:
        Endtype ID, or 0 if the element ID is invalid or no endtype is set.
    """

def get_endtype_id_end(element_id: ElementId) -> EndtypeId:
    """Return the endtype ID assigned to the end face of an element.

    Parameters:
        element_id: Element ID.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_endtype_id = etc.get_endtype_id_end(element)
        >>> print(f"End endtype ID: {end_endtype_id}")

    Returns:
        Endtype ID, or 0 if the element ID is invalid or no endtype is set.
    """

def get_endtype_id_facet(element_id: ElementId, face_number: int) -> EndtypeId:
    """Return the endtype ID assigned to a face of an element.

    Endtypes exist only on faces at the start or end of the element.

    Parameters:
        element_id: Element ID.
        face_number: Zero-based index of the face; must be less than the element's face count.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> face_number = 1
        >>> facet_endtype_id = etc.get_endtype_id_facet(element, face_number)
        >>> print(f"Facet endtype ID: {facet_endtype_id}")

    Returns:
        Endtype ID, or 0 if the element ID is invalid, the face number is out of range or the face
        has no endtype.
    """

def set_endtype_name_start(element_id: ElementId, name: str) -> None:
    """Assign an endtype to the start face of an element by endtype name.

    Does nothing if the name is empty or unknown. Otherwise behaves like the ID variant: the element
    is rebuilt, the display refreshed if auto-refresh is on, and the document marked as modified.
    Not undoable.

    Parameters:
        element_id: Element ID.
        name: Endtype name as shown in the endtype library.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Tenon_100x50"
        >>> etc.set_endtype_name_start(element, endtype_name)
    """

def set_endtype_name_end(element_id: ElementId, name: str) -> None:
    """Assign an endtype to the end face of an element by endtype name.

    Does nothing if the name is empty or unknown. Otherwise behaves like the ID variant: the element
    is rebuilt, the display refreshed if auto-refresh is on, and the document marked as modified.
    Not undoable.

    Parameters:
        element_id: Element ID.
        name: Endtype name as shown in the endtype library.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Mortise_100x50"
        >>> etc.set_endtype_name_end(element, endtype_name)
    """

def set_endtype_name_facet(element_id: ElementId, name: str, face_number: int) -> None:
    """Assign an endtype to a face of an element by endtype name.

    Does nothing if the name is empty or unknown, if the face number is out of range or if the
    element is invalid. Otherwise the element is rebuilt, the display refreshed if auto-refresh is
    on, and the document marked as modified. Not undoable.

    Parameters:
        element_id: Element ID.
        name: Endtype name as shown in the endtype library.
        face_number: Zero-based index of the face; must be less than the element's face count.

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
    """Assign an endtype to the start face of an element by endtype ID.

    The element is rebuilt, the display refreshed if auto-refresh is on, and the document marked as
    modified. Not undoable. The endtype ID is not validated here.

    Parameters:
        element_id: Element ID.
        endtype_id: Endtype ID, for example from get_endtype_id or start_endtype_dialog.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 12345
        >>> etc.set_endtype_id_start(element, endtype_id)
    """

def set_endtype_id_end(element_id: ElementId, endtype_id: EndtypeId) -> None:
    """Assign an endtype to the end face of an element by endtype ID.

    The element is rebuilt, the display refreshed if auto-refresh is on, and the document marked as
    modified. Not undoable. The endtype ID is not validated here.

    Parameters:
        element_id: Element ID.
        endtype_id: Endtype ID, for example from get_endtype_id or start_endtype_dialog.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 54321
        >>> etc.set_endtype_id_end(element, endtype_id)
    """

def set_endtype_id_facet(element_id: ElementId, endtype_id: EndtypeId, face_number: int) -> None:
    """Assign an endtype to a face of an element by endtype ID.

    Does nothing if the face number is out of range or the element is invalid. Otherwise the element
    is rebuilt, the display refreshed if auto-refresh is on, and the document marked as modified.
    Not undoable.

    Parameters:
        element_id: Element ID.
        endtype_id: Endtype ID, for example from get_endtype_id or start_endtype_dialog.
        face_number: Zero-based index of the face; must be less than the element's face count.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 67890
        >>> face_number = 3
        >>> etc.set_endtype_id_facet(element, endtype_id, face_number)
    """

def create_new_endtype(endtype_name: str, end_type_id: int, folder_name: str) -> EndtypeId:
    """Create a new endtype with default settings in an endtype folder.

    The folder is created if it does not exist. The endtype library is saved to the database
    immediately. Existing names are not checked for duplicates.

    Parameters:
        endtype_name: Name of the new endtype.
        end_type_id: Kind of endtype, a cadwork.end_type value: Tenon (1), Lengthening (2),
            DovetailTenon (3), GMIWithCounterpart (4), DovetailMortise (5). Other values create
            nothing.
        folder_name: Name of the endtype folder to put it in.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Custom_Joint_80x40"
        >>> end_type_id = cadwork.end_type.Tenon
        >>> folder_name = "Custom_Joints"
        >>> new_id = etc.create_new_endtype(endtype_name, end_type_id, folder_name)
        >>> print(f"Created endtype with ID: {new_id}")

    Returns:
        ID of the new endtype, or 0 if end_type_id is not supported.
    """

def get_endtype_name(endtype_id: EndtypeId) -> str:
    """Return the name of an endtype.

    Parameters:
        endtype_id: ID of the endtype to look up.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_id = 12345
        >>> endtype_name = etc.get_endtype_name(endtype_id)
        >>> print(f"Endtype name: {endtype_name}")

    Returns:
        Endtype name, or an empty string if the ID is unknown.
    """

def get_endtype_name_start(element_id: ElementId) -> str:
    """Return the name of the endtype on the start face of an element.

    Parameters:
        element_id: Element ID.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_name = etc.get_endtype_name_start(element)
        >>> print(f"Start endtype name: {start_name}")

    Returns:
        Endtype name.
    """

def get_endtype_name_end(element_id: ElementId) -> str:
    """Return the name of the endtype on the end face of an element.

    Parameters:
        element_id: Element ID.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_name = etc.get_endtype_name_end(element)
        >>> print(f"End endtype name: {end_name}")

    Returns:
        Endtype name.
    """

def get_endtype_name_facet(element_id: ElementId, face_number: int) -> str:
    """Return the name of the endtype on a face of an element.

    Parameters:
        element_id: Element ID.
        face_number: Zero-based index of the face; must be less than the element's face count.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> face_number = 2
        >>> facet_name = etc.get_endtype_name_facet(element, face_number)
        >>> print(f"Facet endtype name: {facet_name}")

    Returns:
        Endtype name, or an empty string if the element ID is invalid, the face number is out of
        range or the face has no endtype.
    """

def get_existing_tenon_ids() -> list[EndtypeId]:
    """Return the IDs of all existing tenon endtypes.

    Scans the whole endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> tenon_ids = etc.get_existing_tenon_ids()
        >>> print(f"Available tenon endtype IDs: {tenon_ids}")

    Returns:
        List of endtype IDs of kind tenon; empty if none exist.
    """

def get_existing_lengthening_ids() -> list[EndtypeId]:
    """Return the IDs of all existing lengthening endtypes.

    Scans the whole endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> lengthening_ids = etc.get_existing_lengthening_ids()
        >>> print(f"Available lengthening endtype IDs: {lengthening_ids}")

    Returns:
        List of endtype IDs of kind lengthening; empty if none exist.
    """

def get_existing_dovetail_ids() -> list[EndtypeId]:
    """Return the IDs of all existing dovetail endtypes.

    Scans the whole endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> dovetail_ids = etc.get_existing_dovetail_ids()
        >>> print(f"Available dovetail endtype IDs: {dovetail_ids}")

    Returns:
        List of endtype IDs of kind dovetail tenon; empty if none exist.
    """

def get_existing_dovetail_dado_ids() -> list[EndtypeId]:
    """Return the IDs of all existing dovetail dado endtypes.

    Scans the whole endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> dado_ids = etc.get_existing_dovetail_dado_ids()
        >>> print(f"Available dado endtype IDs: {dado_ids}")

    Returns:
        List of endtype IDs of kind dovetail mortise (dado); empty if none exist.
    """

def get_existing_japanese_tenon_ids() -> list[EndtypeId]:
    """Return the IDs of all existing Japanese tenon endtypes.

    Scans the whole endtype library.

    Examples:
        >>> import endtype_controller as etc

        >>> japanese_tenon_ids = etc.get_existing_japanese_tenon_ids()
        >>> print(f"Available japanese-tenon endtype IDs: {japanese_tenon_ids}")

    Returns:
        List of endtype IDs of kind Japanese tenon; empty if none exist.
    """

def start_endtype_dialog() -> int:
    """Open the endtype selection dialog and return the chosen endtype.

    Blocks the script until the user closes the dialog.

    Examples:
        >>> import endtype_controller as etc

        >>> selected_endtype_id = etc.start_endtype_dialog()
        >>> print(f"User selected endtype ID: {selected_endtype_id}")

    Returns:
        ID of the selected endtype, or 0 if the dialog was cancelled.
    """
