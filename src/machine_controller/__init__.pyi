from typing import List
from cadwork import vertex_list
from cadwork.api_types import ElementId
from cadwork.btl_version import btl_version
from cadwork.hundegger_machine_type import hundegger_machine_type
from cadwork.weinmann_mfb_version import weinmann_mfb_version


def export_btl(btl_version: btl_version, file_path: str) -> None:
    """Exports a BTL file.

    Parameters:
        btl_version: The BTL version.
        file_path: The export file path.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = "C:/exports/timber_project.btlx"
        >>> mc.export_btl(btl_version, output_path)
    """

def export_weinmann_mfb(mfb_version: weinmann_mfb_version) -> None:
    """Exports a Weinmann MFB file.

    Parameters:
        mfb_version: The Weinmann MFB version.

    Examples:
        >>> import machine_controller as mc

        >>> mfb_version = cadwork.weinmann_mfb_version.wup_3_4.value
        >>> mc.export_weinmann_mfb(mfb_version)
    """

def export_hundegger(hundeggertype: hundegger_machine_type) -> None:
    """Exports a Hundegger file.

    Parameters:
        hundeggertype: The Hundegger machine type.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.export_hundegger(hundegger_type)
    """

def export_hundegger_with_file_path(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Exports a Hundegger file.

    Parameters:
        hundeggertype: The Hundegger machine type.
        file_path: The export file path.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = "C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path(hundegger_type, output_path)
    """

def export_hundegger_with_file_path_and_presetting(hundeggertype: hundegger_machine_type, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file.

    Parameters:
        hundeggertype: The Hundegger machine type.
        file_path: The export file path.
        presetting: The presetting file path (.xml).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting(hundegger_type, output_path, presetting_file)
    """

def export_btl_with_presetting(btl_version: btl_version, file_path: str, presetting: str) -> None:
    """Exports a BTL file with a presetting file.

    Parameters:
        btl_version: The BTL version.
        file_path: The export file path.
        presetting: The presetting file path (.xml).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> output_path = r"C:/exports/timber_project.btlx"
        >>> presetting_file = r"...3d/Machine/BTL/btl_settings.xml"
        >>> mc.export_btl_with_presetting(btl_version, output_path, presetting_file)
    """

def calculate_btl_machine_data(element_id_list: List[ElementId], btl_version: btl_version) -> None:
    """Calculates the Machine Data for BTL.

    Parameters:
        element_id_list: The list of element Id.
        btl_version: The BTL version.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> btl_version = cadwork.btl_version.btlx_2_1.value
        >>> mc.calculate_btl_machine_data(beam_elements, btl_version)
    """

def calculate_hundegger_machine_data(element_id_list: List[ElementId], hundeggertype: hundegger_machine_type) -> None:
    """Calculates the Machine Data for Hundegger.

    Parameters:
        element_id_list: The list of element Id.
        hundeggertype: The Hundegger machine type.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> beam_elements = ec.get_all_identifiable_element_ids()
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> mc.calculate_hundegger_machine_data(beam_elements, hundegger_type)
    """

def load_hundegger_calculation_set(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Loads the Hundegger calculation set.

    Parameters:
        hundeggertype: The Hundegger machine type.
        file_path: The file path of the calculation set.
    """

def export_hundegger_with_file_path_silent(hundeggertype: hundegger_machine_type, file_path: str) -> None:
    """Exports a Hundegger file silently.

    Parameters:
        hundeggertype: The Hundegger machine type.
        file_path: The export file path.

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> mc.export_hundegger_with_file_path_silent(hundegger_type, output_path)
    """

def export_hundegger_with_file_path_and_presetting_silent(hundeggertype: hundegger_machine_type, file_path: str, presetting: str) -> None:
    """Exports a Hundegger file silently.

    Parameters:
        hundeggertype: The Hundegger machine type.
        file_path: The export file path.
        presetting: The presetting file path (.xml).

    Examples:
        >>> import cadwork
        >>> import machine_controller as mc

        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> output_path = r"C:/exports/hundegger_project.k2"
        >>> presetting_file = r"...3d/Machine/Hundegger/K2/hundegger_settings.xml"
        >>> mc.export_hundegger_with_file_path_and_presetting_silent(hundegger_type, output_path, presetting_file)
    """


def get_element_hundegger_processings(element_id: ElementId, hundeggertype: hundegger_machine_type) -> List[ElementId]:
    """Gets the list of Hundegger processings for a specific element.

    Parameters:
        element_id: The element id.
        hundeggertype: The Hundegger machine type.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> hundegger_type = cadwork.hundegger_machine_type.k2.value
        >>> processings = mc.get_element_hundegger_processings(element, hundegger_type)
        >>> print(f"Found {len(processings)} Hundegger processings")

    Returns:
        A list of element IDs representing the processings.
    """


def get_element_btl_processings(element_id: ElementId, btl_version: btl_version) -> List[ElementId]:
    """Gets the list of BTL processings for a specific element.

    Parameters:
        element_id: The element id.
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
        A list of element IDs representing the processings.
    """


def get_processing_name(reference_element_id: ElementId, processing_id: ElementId) -> str:
    """Gets the name of a specific processing.

    Parameters:
        reference_element_id: The reference element id.
        processing_id: The processing id.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     name = mc.get_processing_name(element, processing)

    Returns:
        The name of the processing.
    """


def get_processing_code(reference_element_id: ElementId, processing_id: ElementId) -> str:
    """Gets the code of a specific processing.

    Parameters:
        reference_element_id: The reference element id.
        processing_id: The processing id.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     code = mc.get_processing_code(element, processing)

    Returns:
        The code of the processing.
    """


def get_processing_points(reference_element_id: ElementId, processing_id: ElementId) -> vertex_list:
    """Gets the points of a specific processing.

    Parameters:
        reference_element_id: The reference element id.
        processing_id: The processing id.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     points = mc.get_processing_points(element, processing)

    Returns:
        A list of vertices representing the points of the processing.
    """


def get_processing_btl_parameter_set(reference_element_id: ElementId, processing_id: ElementId) -> List[str]:
    """Gets the BTL parameter set of a specific processing.

    Parameters:
        reference_element_id: The reference element id.
        processing_id: The processing id.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     parameters = mc.get_processing_btl_parameter_set(element, processing)

    Returns:
        A list of strings representing the BTL parameter set of the processing.
    """