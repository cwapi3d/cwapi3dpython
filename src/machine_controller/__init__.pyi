from typing import List
from cadwork import vertex_list


def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def export_btl(btl_version: int, file_path: str) -> None:
    """Exports a BTL file

    Parameters:
        btl_version: btl_version
        file_path: file_path

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = "C:/exports/timber_project.btlx"
        >>> mc.export_btl(btl_version, output_path)

    Returns:
        None
    """

def export_weinmann_mfb(mfb_version: int) -> None:
    """Exports a WUP file

    Parameters:
        mfb_version: mfb_version

    Examples:
        >>> import machine_controller as mc

        >>> mfb_version = cadwork.weinmann_mfb_version.wup_3_4.value
        >>> mc.export_weinmann_mfb(mfb_version)

    Returns:
        None
    """

def export_hundegger(hundeggertype: int) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.export_hundegger(hundegger_type)

    Returns:
        None
    """

def export_hundegger_with_file_path(hundeggertype: int, file_path: str) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = "C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path(hundegger_type, output_path)

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting(hundeggertype: int, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path
        presetting: presetting

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting(hundegger_type, output_path, presetting_file)

    Returns:
        None
    """

def export_btl_with_presetting(btl_version: int, file_path: str, presetting: str) -> None:
    """Exports a BTL file with a presetting file

    Parameters:
        btl_version: btl_version
        file_path: file_path
        presetting: presetting

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = r"C:/exports/timber_project.btlx"
        >>> presetting_file = r"...3d/Machine/BTL/btl_settings.xml"
        >>> mc.export_btl_with_presetting(btl_version, output_path, presetting_file)

    Returns:
        None
    """

def calculate_btl_machine_data(elements: List[int], btl_version: int) -> None:
    """Calculates the Machine Data for BTL

    Parameters:
        elements: elements
        btl_version: btl_version

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> mc.calculate_btl_machine_data(beam_elements, btl_version)

    Returns:
        None
    """

def calculate_hundegger_machine_data(elements: List[int], hunderggertype: int) -> None:
    """Calculates the Machine Data for Hundegger

    Parameters:
        elements: elements
        hunderggertype: hunderggertype

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.calculate_hundegger_machine_data(beam_elements, hundegger_type)

    Returns:
        None
    """

def load_hundegger_calculation_set(hundeggertype: int, file_path: str) -> None:
    """load hundegger calculation set

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Returns:
        None
    """

def export_hundegger_with_file_path_silent(hundeggertype: int, file_path: str) -> None:
    """Exports a Hundegger file silently

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path_silent(hundegger_type, output_path)

    Returns:
        None
    """

def export_hundegger_with_file_path_and_presetting_silent(hundeggertype: int, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file silently

    Parameters:
        hundeggertype: hundeggertype
        file_path: file_path
        presetting: presetting

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting_silent(hundegger_type, output_path, presetting_file)

    Returns:
        None
    """


def get_element_hundegger_processings(element_id: int, hundeggertype: int) -> List[int]:
    """Get Hundegger processing IDs for an element.

    Parameters:
        element_id: The element ID.
        hundeggertype: The Hundegger type.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> processings = mc.get_element_hundegger_processings(element, hundegger_type)
        >>> print(f"Found {len(processings)} Hundegger processings")

    Returns:
        List of processing IDs.
    """


def get_element_btl_processings(element_id: int, btl_version: int) -> List[int]:
    """Get BTL processing IDs for an element.

    Parameters:
        element_id: The element ID.
        btl_version: The BTL version.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> processings = mc.get_element_btl_processings(element, btl_version)
        >>> print(f"Found {len(processings)} BTL processings")

    Returns:
        List of processing IDs.
    """


def get_processing_name(reference_element_id: int, processing_id: int) -> str:
    """Get the name of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     name = mc.get_processing_name(element, processing)

    Returns:
        The processing name.
    """


def get_processing_code(reference_element_id: int, processing_id: int) -> str:
    """Get the code of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     code = mc.get_processing_code(element, processing)

    Returns:
        The processing code.
    """


def get_processing_points(reference_element_id: int, processing_id: int) -> vertex_list:
    """Get the points of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     points = mc.get_processing_points(element, processing)

    Returns:
        A vertex_list of points.
    """


def get_processing_btl_parameter_set(reference_element_id: int, processing_id: int) -> List[str]:
    """Get the BTL parameter set for a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     parameters = mc.get_processing_btl_parameter_set(element, processing)

    Returns:
        List of BTL parameter strings.
    """
