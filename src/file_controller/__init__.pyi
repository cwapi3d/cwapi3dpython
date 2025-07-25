from typing import List
from cadwork import point_3d
from cadwork.bim_team_upload_result import bim_team_upload_result
from cadwork.dxf_layer_format_type import dxf_layer_format_type
from cadwork.dxf_export_version import dxf_export_version


def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """


def export_stl_file(element_id_list: List[int], file_path: str) -> None:
    """Exports an STL file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.stl"
        >>> fc.export_stl_file(selected_elements, output_path)

    Returns:
        None
    """


def import_step_file(file_path: str, scale_factor: float) -> List[int]:
    """Imports a STEP file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor

    Returns:
        imported element ID list
    """


def import_step_file_with_message_option(file_path: str, scale_factor: float, hide_message: bool) -> List[int]:
    """Imports a STEP file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        hide_message: hide_message

    Returns:
        imported element ID list
    """


def export_webgl(element_id_list: List[int], file_path: str) -> bool:
    """Exports a WebGL file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.html"
        >>> success = fc.export_webgl(selected_elements, output_path)
        >>> if success:
        >>>     print("WebGL export completed successfully")

    Returns:
        did operation succeed
    """


def export_3d_file(element_id_list: List[int], file_path: str) -> bool:
    """Exports a 3D file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3d"
        >>> success = fc.export_3d_file(selected_elements, output_path)
        >>> if success:
        >>>     print("3D file export completed successfully")

    Returns:
        did operation succeed
    """


def import_sat_file(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports an SAT file

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        binary: binary

    Returns:
        imported element ID list
    """


def import_3dc_file(file_path: str) -> List[int]:
    """Imports a 3DC file

    Parameters:
        file_path: file_path

    Returns:
        imported element ID list
    """


def import_rhino_file(file_path: str, without_dialog: bool) -> List[int]:
    """Imports a Rhino file

    Parameters:
        file_path: file_path
        without_dialog: without_dialog

    Returns:
        imported element ID list
    """


def export_step_file(element_list: List[int], file_path: str, scale_factor: float, version: int,
                     text_mode: bool) -> None:
    """Exports a STEP file

    Parameters:
        element_list: element_list
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.stp"
        >>> scale_factor = 1_000.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> fc.export_step_file(selected_elements, output_path, scale_factor, version, text_mode)

    Returns:
        None
    """


def import_3dz_file(file_path: str) -> None:
    """Imports a 3DZ file

    Parameters:
        file_path: file_path

    Returns:
        None
    """


def export_obj_file(elements: List[int], file_path: str) -> None:
    """Exports a OBJ file

    Parameters:
        elements: elements
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.obj"
        >>> fc.export_obj_file(selected_elements, output_path)

    Returns:
        None
    """


def import_sat_file_silently(file_path: str, scale_factor: float, binary: bool) -> List[int]:
    """Imports a SAT File without messages

    Parameters:
        file_path: file_path
        scale_factor: scale_factor
        binary: binary

    Returns:
        List[int]
    """


def export_fbx_file(elements: List[int], file_path: str, fbx_format: int) -> None:
    """Exports a FBX file

    Parameters:
        elements: elements
        file_path: file_path
        fbx_format: fbx_format
            Available formats:
            - 0 or default: FBX binary(*.fbx)
            - 1: FBX binary(*.fbx)
            - 2: FBX ascii(*.fbx)
            - 3: FBX encrypted(*.fbx)
            - 4: FBX 6.0 binary(*.fbx)
            - 5: FBX 6.0 ascii(*.fbx)
            - 6: FBX 6.0 encrypted(*.fbx)

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.fbx"
        >>> fbx_format = 1  # FBX binary format
        >>> fc.export_fbx_file(selected_elements, output_path, fbx_format)

        >>> # Export as ASCII format
        >>> fbx_format = 2  # FBX ascii format
        >>> fc.export_fbx_file(selected_elements, output_path, fbx_format)

    Returns:
        None
    """


def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """


def import_3dc_file_with_glide(file_path: str) -> List[int]:
    """Imports a 3DC file with glide

    Parameters:
        file_path: file_path

    Returns:
        imported element ID list
    """


def import_btl_file(file_path: str) -> None:
    """Imports a BTL file

    Parameters:
        file_path: file_path

    Returns:
        None
    """


def export_3dc_file(element_id_list: List[int], file_path: str) -> None:
    """Exports a 3D file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dc"
        >>> fc.export_3dc_file(selected_elements, output_path)

    Returns:
        None
    """


def import_btl_file_for_nesting(file_path: str) -> None:
    """Imports a BTL file for nesting

    Parameters:
        file_path: file_path

    Returns:
        None
    """


def export_btl_file_for_nesting(file_path: str) -> None:
    """Exports a BTL file for nesting

    Parameters:
        file_path: file_path

    Examples:
        >>> import file_controller as fc

        >>> output_path = r"C:/exports/nesting_project.btl"
        >>> fc.export_btl_file_for_nesting(output_path)

    Returns:
        None
    """


def export_rhino_file(element_id_list: List[int], file_path: str, version: int, use_default_assignment: bool,
                      write_standard_attributes: bool) -> None:
    """Exports a 3dm rhino file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        version: version
        use_default_assignment: use_default_assignment
        write_standard_attributes: write_standard_attributes

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dm"
        >>> version = 8  # Rhino version
        >>> use_default_assignment = True
        >>> write_standard_attributes = False
        >>> fc.export_rhino_file(selected_elements, output_path, version, use_default_assignment, write_standard_attributes)

    Returns:
        None
    """


def import_bxf_file(file_path: str, insert_position: point_3d) -> List[int]:
    """import bxf file

    Parameters:
        file_path: file_path
        insert_position: insert_position

    Returns:
        List[int]
    """


def get_blum_export_path() -> str:
    """get blum export path

    Returns:
        str
    """


def set_blum_export_path(path: str) -> None:
    """set blum export path

    Parameters:
        path: path

    Returns:
        None
    """


def export_sat_file(elements: List[int], file_path: str, scale_factor: float, binary: bool, version: int) -> None:
    """exports a SAT File

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        binary: binary
        version: version

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.sat"
        >>> scale_factor = 1.0
        >>> binary_format = True
        >>> version = 25000  # SAT version
        >>> fc.export_sat_file(selected_elements, output_path, scale_factor, binary_format, version)

    Returns:
        None
    """


def export_glb_file(elements: List[int], file_path: str) -> None:
    """exports a GLB File

    Parameters:
        elements: elements
        file_path: file_path

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.glb"
        >>> fc.export_glb_file(selected_elements, output_path)

    Returns:
        None
    """


def import_variant_file(file_path: str, insert_position: point_3d) -> List[int]:
    """imports a variant by .val-File

    Parameters:
        file_path: file_path
        insert_position: insert_position

    Returns:
        imported element ID list
    """


def import_element_light(file_path: str, insert_position: point_3d) -> int:
    """import element light

    Parameters:
        file_path: file_path
        insert_position: insert_position

    Returns:
        int
    """


def export_rhino_file_with_options(element_id_list: List[int], file_path: str, version: int,
                                   use_default_assignment: bool, write_standard_attributes: bool,
                                   rhino_options: None) -> None:
    """exports elements to a rhino 3dm file based on the export options

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        version: version
        use_default_assignment: use_default_assignment
        write_standard_attributes: write_standard_attributes
        rhino_options: rhino_options

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model.3dm"
        >>> version = 8  # Rhino version
        >>> use_default_assignment = True
        >>> write_standard_attributes = False
        >>> rhino_options = None  # Use default options
        >>> fc.export_rhino_file_with_options(selected_elements, output_path, version, use_default_assignment, write_standard_attributes, rhino_options)

    Returns:
        None
    """


def import_3dc_file_with_options(file_path: str, import3dc_options: None) -> List[int]:
    """imports a 3d or a 3dc file depending on the import options

    Parameters:
        file_path: file_path
        import3dc_options: import3dc_options

    Returns:
        imported element ID list
    """


def get_import_3dc_options() -> 'import_3dc_options':
    """get import 3dc options

    Returns:
        import_3dc_options
    """


def load_webgl_preset_file(file_path: str) -> None:
    """loads a preset file for the WebGl export

    Parameters:
        file_path: file_path

    Returns:
        None
    """


def export_step_file_extrude_drillings(elements: List[int], file_path: str, scale_factor: float, version: int,
                                       text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode
        imperial_units: imperial_units

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model_with_drillings.step"
        >>> scale_factor = 1.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> imperial_units = False
        >>> fc.export_step_file_extrude_drillings(selected_elements, output_path, scale_factor, version, text_mode, imperial_units)

    Returns:
        None
    """


def export_step_file_cut_drillings(elements: List[int], file_path: str, scale_factor: float, version: int,
                                   text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode
        imperial_units: imperial_units

    Examples:
        >>> import element_controller as ec
        >>> import file_controller as fc

        >>> selected_elements = ec.get_all_identifiable_element_ids()
        >>> output_path = r"C:/exports/model_cut_drillings.step"
        >>> scale_factor = 1.0
        >>> version = 214  # STEP version
        >>> text_mode = False
        >>> imperial_units = False
        >>> fc.export_step_file_cut_drillings(selected_elements, output_path, scale_factor, version, text_mode, imperial_units)

    Returns:
        None
    """


def export_sat_file_cut_drillings(elements: List[int], file_path: str,
                                  scale_factor: float, binary: bool, version: int) -> None:
    """export sat file cut drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        binary: binary
        version: version

    Returns:
        None
    """


def upload_to_bim_team_and_create_share_link(elements: None
                                             ) -> bim_team_upload_result:
    """upload to bim team and create share link

    Parameters:
        elements: elements

    Returns:
        bim_team_upload_result
    """


def export_dxf_file(file_path: str, dxf_layer_format_type: dxf_layer_format_type,
                    dxf_export_version: dxf_export_version) -> bool:
    """export dxf file

    Parameters:
        file_path: file_path
        dxf_layer_format_type: dxf_layer_format_type
        dxf_export_version: dxf_export_version

    Returns:
        bool
    """


def export_dstv_file(file_path: str) -> bool:
    """export dstv file

    Parameters:
        file_path: file_path

    Returns:
        bool
    """
