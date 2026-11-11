"""End-type joinery: profiled cuts at element faces.

Domain of named joinery profiles (tenons, mortises, dovetails,
custom shapes, ...) applied to the start, end or arbitrary faces
of an element. Covers the catalog (creation, lookup by name and
id), assignment to specific element faces, retrieval of currently
applied end-types, and the interactive selection dialog.
"""

from cadwork.api_types import *

def get_endtype_id(name: str) -> EndtypeId:
    """Look up an endtype ID by its name.

    End-types are named joinery profiles (tenons, lengthenings, dovetails and so on) kept in the
    endtype library of the document, organised in folders. The name is compared with every endtype
    in the library and the ID of the first one with an equal name is returned. Use the result with
    `endtype_controller.set_endtype_id_start()`, `endtype_controller.set_endtype_id_end()` or
    `endtype_controller.set_endtype_id_facet()`. The reverse lookup is
    `endtype_controller.get_endtype_name()`.

    Parameters:
        name: Endtype name as shown in the endtype library. An empty string finds nothing.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Tenon_100x50"
        >>> endtype_id = etc.get_endtype_id(endtype_name)
        >>> print(f"Endtype ID: {endtype_id}")

    Returns:
        ID of the first endtype with that name, or 0 if the name is empty or no endtype has it.
    """

def get_endtype_id_start(element_id: ElementId) -> EndtypeId:
    """Return the endtype ID assigned to the start of an element.

    Reads the end-type that is currently applied at the start of the element. Get the name with
    `endtype_controller.get_endtype_name_start()` and change it with
    `endtype_controller.set_endtype_id_start()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_endtype_id = etc.get_endtype_id_start(element)
        >>> print(f"Start endtype ID: {start_endtype_id}")

    Returns:
        Endtype ID, or 0 if the element ID is invalid, the element cannot carry end-types or none is
        set.
    """

def get_endtype_id_end(element_id: ElementId) -> EndtypeId:
    """Return the endtype ID assigned to the end of an element.

    Reads the end-type that is currently applied at the end of the element. Get the name with
    `endtype_controller.get_endtype_name_end()` and change it with
    `endtype_controller.set_endtype_id_end()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_endtype_id = etc.get_endtype_id_end(element)
        >>> print(f"End endtype ID: {end_endtype_id}")

    Returns:
        Endtype ID, or 0 if the element ID is invalid, the element cannot carry end-types or none is
        set.
    """

def get_endtype_id_facet(element_id: ElementId, face_number: int) -> EndtypeId:
    """Return the endtype ID assigned to a face of an element.

    Reads the end-type applied to one face of the element, addressed by its position in the
    element's face list. A face without an end-type, an out-of-range face number and an invalid
    element all give 0. Use `endtype_controller.get_endtype_id_start()` and
    `endtype_controller.get_endtype_id_end()` for the two ends of an element, and
    `endtype_controller.set_endtype_id_facet()` to change it.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        face_number: Zero-based index into the element's list of faces. Values at or beyond the face
            count are out of range. Must not be negative.

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
    """Assign an endtype to the start of an element by endtype name.

    Looks the name up in the endtype library and then assigns the endtype like
    `endtype_controller.set_endtype_id_start()`. Nothing happens if the name is empty or no endtype
    has it. The element is rebuilt with the end-type shown, the display is refreshed if automatic
    refresh is on, and the document is marked as modified. The change is not recorded for undo.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        name: Endtype name exactly as shown in the endtype library.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_name = "Tenon_100x50"
        >>> etc.set_endtype_name_start(element, endtype_name)
    """

def set_endtype_name_end(element_id: ElementId, name: str) -> None:
    """Assign an endtype to the end of an element by endtype name.

    Looks the name up in the endtype library and then assigns the endtype like
    `endtype_controller.set_endtype_id_end()`. Nothing happens if the name is empty or no endtype
    has it. The element is rebuilt with the end-type shown, the display is refreshed if automatic
    refresh is on, and the document is marked as modified. The change is not recorded for undo.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        name: Endtype name exactly as shown in the endtype library.

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

    Looks the name up in the endtype library and then assigns the endtype like
    `endtype_controller.set_endtype_id_facet()`. Nothing happens if the name is empty or unknown,
    the face number is out of range, or the element is invalid or cannot carry end-types. The
    element is rebuilt with the end-type shown, the display is refreshed if automatic refresh is on,
    and the document is marked as modified. The change is not recorded for undo.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        name: Endtype name exactly as shown in the endtype library.
        face_number: Zero-based index into the element's list of faces. Values at or beyond the face
            count are out of range. Must not be negative.

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
    """Assign an endtype to the start of an element by endtype ID.

    Sets the end-type applied at the start of the element, replacing the previous one. The endtype
    ID is not checked against the library, so take it from `endtype_controller.get_endtype_id()`,
    one of the `endtype_controller.get_existing_*_ids()` functions,
    `endtype_controller.create_new_endtype()` or `endtype_controller.start_endtype_dialog()`. The
    element is rebuilt with the end-type shown, the display is refreshed if automatic refresh is on,
    and the document is marked as modified. The change is not recorded for undo. Use
    `endtype_controller.set_endtype_name_start()` to assign by name.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        endtype_id: Endtype ID, e.g. from `endtype_controller.get_endtype_id()` or
            `endtype_controller.start_endtype_dialog()`.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> endtype_id = 12345
        >>> etc.set_endtype_id_start(element, endtype_id)
    """

def set_endtype_id_end(element_id: ElementId, endtype_id: EndtypeId) -> None:
    """Assign an endtype to the end of an element by endtype ID.

    Sets the end-type applied at the end of the element, replacing the previous one. The endtype ID
    is not checked against the library, so take it from `endtype_controller.get_endtype_id()`, one
    of the `endtype_controller.get_existing_*_ids()` functions,
    `endtype_controller.create_new_endtype()` or `endtype_controller.start_endtype_dialog()`. The
    element is rebuilt with the end-type shown, the display is refreshed if automatic refresh is on,
    and the document is marked as modified. The change is not recorded for undo. Use
    `endtype_controller.set_endtype_name_end()` to assign by name.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        endtype_id: Endtype ID, e.g. from `endtype_controller.get_endtype_id()` or
            `endtype_controller.start_endtype_dialog()`.

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

    Sets the end-type of one face of the element, addressed by its position in the element's face
    list. Nothing happens if the face number is out of range or the element is invalid or cannot
    carry end-types. The endtype ID is not checked against the library. The element is rebuilt with
    the end-type shown, the display is refreshed if automatic refresh is on, and the document is
    marked as modified. The change is not recorded for undo. Use
    `endtype_controller.set_endtype_name_facet()` to assign by name.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        endtype_id: Endtype ID, e.g. from `endtype_controller.get_endtype_id()` or
            `endtype_controller.start_endtype_dialog()`.
        face_number: Zero-based index into the element's list of faces. Values at or beyond the face
            count are out of range. Must not be negative.

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

    Adds a new endtype of the requested kind to the endtype library, with the default parameters of
    that kind, and saves the library to the database immediately. The folder is created at the top
    level of the library when no folder of that name exists. Names are not checked for duplicates,
    so `endtype_controller.get_endtype_id()` returns the first one when several share a name. Use
    the returned ID with `endtype_controller.set_endtype_id_start()` and the related functions.

    Parameters:
        endtype_name: Name of the new endtype as it appears in the library.
        end_type_id: Kind of endtype to create: 1 tenon, 2 lengthening, 3 dovetail tenon, 4 generic
            endtype (GMI with counterpart), 5 dovetail mortise (dado), 6 Japanese tenon. Any other
            value, including 7, creates nothing. The numbers do not match every `cadwork.end_type`
            member: `cadwork.end_type.FrontSlot` is 6 and creates a Japanese tenon, and
            `cadwork.end_type.JapaneseTenon` is 7 and creates nothing.
        folder_name: Name of the endtype folder to put it in. Created if missing.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_name = "Custom_Joint_80x40"
        >>> end_type_id = cadwork.end_type.Tenon
        >>> folder_name = "Custom_Joints"
        >>> new_id = etc.create_new_endtype(endtype_name, end_type_id, folder_name)
        >>> print(f"Created endtype with ID: {new_id}")

    Returns:
        ID of the new endtype, or 0 if end_type_id is not supported (in which case nothing is
        created).
    """

def get_endtype_name(endtype_id: EndtypeId) -> str:
    """Return the name of an endtype from its ID.

    Looks the ID up in the endtype library of the document. The reverse lookup is
    `endtype_controller.get_endtype_id()`. To read the name of the end-type applied to an element
    use `endtype_controller.get_endtype_name_start()`, `endtype_controller.get_endtype_name_end()`
    or `endtype_controller.get_endtype_name_facet()`.

    Parameters:
        endtype_id: ID of an endtype, e.g. from `endtype_controller.get_endtype_id()` or
            `endtype_controller.get_existing_tenon_ids()`.

    Examples:
        >>> import endtype_controller as etc

        >>> endtype_id = 12345
        >>> endtype_name = etc.get_endtype_name(endtype_id)
        >>> print(f"Endtype name: {endtype_name}")

    Returns:
        Endtype name, or an empty string if no endtype has that ID.
    """

def get_endtype_name_start(element_id: ElementId) -> str:
    """Return the name of the endtype on the start of an element.

    Reads the name of the end-type currently applied at the start of the element. The ID variant is
    `endtype_controller.get_endtype_id_start()`; assign with
    `endtype_controller.set_endtype_name_start()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> start_name = etc.get_endtype_name_start(element)
        >>> print(f"Start endtype name: {start_name}")

    Returns:
        Endtype name as shown in the endtype library.
    """

def get_endtype_name_end(element_id: ElementId) -> str:
    """Return the name of the endtype on the end of an element.

    Reads the name of the end-type currently applied at the end of the element. The ID variant is
    `endtype_controller.get_endtype_id_end()`; assign with
    `endtype_controller.set_endtype_name_end()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import endtype_controller as etc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> element = selected_elements[0]
        >>> end_name = etc.get_endtype_name_end(element)
        >>> print(f"End endtype name: {end_name}")

    Returns:
        Endtype name as shown in the endtype library.
    """

def get_endtype_name_facet(element_id: ElementId, face_number: int) -> str:
    """Return the name of the endtype on a face of an element.

    Reads the name of the end-type applied to one face of the element, addressed by its position in
    the element's face list. The ID variant is `endtype_controller.get_endtype_id_facet()`; assign
    with `endtype_controller.set_endtype_name_facet()`.

    Parameters:
        element_id: Element ID, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.
        face_number: Zero-based index into the element's list of faces. Values at or beyond the face
            count are out of range. Must not be negative.

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
    """Return the IDs of all tenon endtypes in the library.

    Scans the whole endtype library of the document, including all folders, and collects the
    endtypes whose kind is tenon. Use the IDs with `endtype_controller.get_endtype_name()` to list
    them by name or with `endtype_controller.set_endtype_id_start()` and related functions to assign
    one. Create a new one with `endtype_controller.create_new_endtype()`.

    Examples:
        >>> import endtype_controller as etc

        >>> tenon_ids = etc.get_existing_tenon_ids()
        >>> print(f"Available tenon endtype IDs: {tenon_ids}")

    Returns:
        List of endtype IDs of kind tenon; empty if there are none.
    """

def get_existing_lengthening_ids() -> list[EndtypeId]:
    """Return endtype IDs from the library; currently the same list as the tenon query.

    In the current implementation this function returns the same IDs as
    `endtype_controller.get_existing_tenon_ids()`, i.e. the tenon endtypes, not the lengthening
    endtypes. Check the kind of each returned endtype by name with
    `endtype_controller.get_endtype_name()` before relying on it.

    Examples:
        >>> import endtype_controller as etc

        >>> lengthening_ids = etc.get_existing_lengthening_ids()
        >>> print(f"Available lengthening endtype IDs: {lengthening_ids}")

    Returns:
        List of endtype IDs, currently those of kind tenon; empty if there are none.
    """

def get_existing_dovetail_ids() -> list[EndtypeId]:
    """Return the IDs of all dovetail tenon endtypes in the library.

    Scans the whole endtype library of the document, including all folders, and collects the
    endtypes whose kind is dovetail tenon. Use the IDs with `endtype_controller.get_endtype_name()`
    to list them by name or with `endtype_controller.set_endtype_id_start()` and related functions
    to assign one. Create a new one with `endtype_controller.create_new_endtype()`.

    Examples:
        >>> import endtype_controller as etc

        >>> dovetail_ids = etc.get_existing_dovetail_ids()
        >>> print(f"Available dovetail endtype IDs: {dovetail_ids}")

    Returns:
        List of endtype IDs of kind dovetail tenon; empty if there are none.
    """

def get_existing_dovetail_dado_ids() -> list[EndtypeId]:
    """Return the IDs of all dovetail mortise (dado) endtypes in the library.

    Scans the whole endtype library of the document, including all folders, and collects the
    endtypes whose kind is dovetail mortise (dado). Use the IDs with
    `endtype_controller.get_endtype_name()` to list them by name or with
    `endtype_controller.set_endtype_id_start()` and related functions to assign one. Create a new
    one with `endtype_controller.create_new_endtype()`.

    Examples:
        >>> import endtype_controller as etc

        >>> dado_ids = etc.get_existing_dovetail_dado_ids()
        >>> print(f"Available dado endtype IDs: {dado_ids}")

    Returns:
        List of endtype IDs of kind dovetail mortise (dado); empty if there are none.
    """

def get_existing_japanese_tenon_ids() -> list[EndtypeId]:
    """Return the IDs of all Japanese tenon endtypes in the library.

    Scans the whole endtype library of the document, including all folders, and collects the
    endtypes whose kind is Japanese tenon. Use the IDs with `endtype_controller.get_endtype_name()`
    to list them by name or with `endtype_controller.set_endtype_id_start()` and related functions
    to assign one. Create a new one with `endtype_controller.create_new_endtype()`.

    Examples:
        >>> import endtype_controller as etc

        >>> japanese_tenon_ids = etc.get_existing_japanese_tenon_ids()
        >>> print(f"Available japanese-tenon endtype IDs: {japanese_tenon_ids}")

    Returns:
        List of endtype IDs of kind Japanese tenon; empty if there are none.
    """

def start_endtype_dialog() -> int:
    """Open the endtype selection dialog and return the chosen endtype ID.

    Shows cadwork's endtype library dialog and blocks the script until the user closes it. Pass the
    returned ID to `endtype_controller.set_endtype_id_start()`,
    `endtype_controller.set_endtype_id_end()` or `endtype_controller.set_endtype_id_facet()`, or
    read its name with `endtype_controller.get_endtype_name()`. Avoid it in unattended scripts since
    it needs user input.

    Examples:
        >>> import endtype_controller as etc

        >>> selected_endtype_id = etc.start_endtype_dialog()
        >>> print(f"User selected endtype ID: {selected_endtype_id}")

    Returns:
        ID of the selected endtype. If the user cancels, an invalid ID (expected to be 0) is
        returned, so check it before use.
    """
