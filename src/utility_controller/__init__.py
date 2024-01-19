from typing import List
from cadwork import point_3d


def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        strerror string
    """


def get_3d_version() -> int:
    """get 3d version
    Args:

    Returns:
        int3D version
    """


def get_3d_build() -> int:
    """get 3d build
    Args:

    Returns:
        int3D build
    """


def get_3d_file_path() -> str:
    """get 3d file path
    Args:

    Returns:
        str3D file path
    """


def set_project_data(element_id: str, data: str) -> None:
    """set project data
    Args:
        element_id ( str): element_id
        data ( str): data

    Returns:
        None
    """


def print_error(message: str) -> None:
    """print error
    Args:
        message ( str): message

    Returns:
        None
    """


def get_language() -> str:
    """get language
    Args:

    Returns:
        str3D language
    """


def print_message(message: str) -> None:
    """print message
    Args:
        message ( str): message

    Returns:
        None
    """


def get_user_int(message: str) -> int:
    """get user int
    Args:
        message ( str): message

    Returns:
        intuser integer
    """


def get_user_double(message: str) -> float:
    """get user double
    Args:
        message ( str): message

    Returns:
        floatuser double
    """


def get_user_bool(message: str) -> bool:
    """get user bool
    Args:
        message ( str): message

    Returns:
        booluser boolean
    """


def get_user_string(message: str) -> str:
    """get user string
    Args:
        message ( str): message

    Returns:
        struser string
    """


def set_project_name(project_name: str) -> None:
    """set project name
    Args:
        project_name ( str): project_name

    Returns:
        None
    """


def set_project_number(project_number: str) -> None:
    """set project number
    Args:
        project_number ( str): project_number

    Returns:
        None
    """


def set_project_part(project_part: str) -> None:
    """set project part
    Args:
        project_part ( str): project_part

    Returns:
        None
    """


def set_project_architect(project_architect: str) -> None:
    """set project architect
    Args:
        project_architect ( str): project_architect

    Returns:
        None
    """


def set_project_customer(project_customer: str) -> None:
    """set project customer
    Args:
        project_customer ( str): project_customer

    Returns:
        None
    """


def set_project_designer(project_designer: str) -> None:
    """set project designer
    Args:
        project_designer ( str): project_designer

    Returns:
        None
    """


def set_project_deadline(project_deadline: str) -> None:
    """set project deadline
    Args:
        project_deadline ( str): project_deadline

    Returns:
        None
    """


def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """set project user attribute
    Args:
        number ( int): number
        user_attribute ( str): user_attribute

    Returns:
        None
    """


def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """set project user attribute name
    Args:
        number ( int): number
        user_attribute_name ( str): user_attribute_name

    Returns:
        None
    """


def set_project_latitude(latitude: float) -> None:
    """set project latitude
    Args:
        latitude ( float): latitude

    Returns:
        None
    """


def set_project_longitude(longitude: float) -> None:
    """set project longitude
    Args:
        longitude ( float): longitude

    Returns:
        None
    """


def set_project_address(address: str) -> None:
    """set project address
    Args:
        address ( str): address

    Returns:
        None
    """


def set_project_postal_code(postal_code: str) -> None:
    """set project postal code
    Args:
        postal_code ( str): postal_code

    Returns:
        None
    """


def set_project_city(city: str) -> None:
    """set project city
    Args:
        city ( str): city

    Returns:
        None
    """


def set_project_country(country: str) -> None:
    """set project country
    Args:
        country ( str): country

    Returns:
        None
    """


def get_user_file_from_dialog(name_filter: str) -> str:
    """get user file from dialog
    Args:
        name_filter ( str): name_filter

    Returns:
        strfile path
    """


def get_client_number() -> str:
    """get client number
    Args:

    Returns:
        strclient number
    """


def get_user_point() -> point_3d:
    """get user point
    Args:

    Returns:
        point_3duser point
    """


def disable_auto_display_refresh() -> None:
    """disable auto display refresh
    Args:

    Returns:
        None
    """


def enable_auto_display_refresh() -> None:
    """enable auto display refresh
    Args:

    Returns:
        None
    """


def create_new_guid() -> str:
    """create new guid
    Args:

    Returns:
        strGUID
    """


def print_to_console(message: str) -> None:
    """print to console
    Args:
        message ( str): message

    Returns:
        None
    """


def export_screen_to_image(file_path: str) -> None:
    """export screen to image
    Args:
        file_path ( str): file_path

    Returns:
        None
    """


def get_new_user_file_from_dialog(name_filter: str) -> str:
    """get new user file from dialog
    Args:
        name_filter ( str): name_filter

    Returns:
        strfile path
    """


def api_autostart(api_name: str, option: int) -> int:
    """api autostart
    Args:
        api_name ( str): api_name
        option ( int): option

    Returns:
        int
    """


def enable_autostart(api_name: str) -> None:
    """enable autostart
    Args:
        api_name ( str): api_name

    Returns:
        None
    """


def disable_autostart(api_name: str) -> None:
    """disable autostart
    Args:
        api_name ( str): api_name

    Returns:
        None
    """


def check_autostart(api_name: str) -> bool:
    """check autostart
    Args:
        api_name ( str): api_name

    Returns:
        bool
    """


def delete_project_data(element_id: str) -> None:
    """delete project data
    Args:
        element_id ( str): element_id

    Returns:
        None
    """


def run_external_program(name: str) -> bool:
    """run external program
    Args:
        name ( str): name

    Returns:
        boolexternal program return
    """


def save_3d_file_silently() -> None:
    """save 3d file silently
    Args:

    Returns:
        None
    """


def get_licence_first_part() -> str:
    """get licence first part
    Args:

    Returns:
        strfirst part of licence
    """


def get_licence_second_part() -> str:
    """get licence second part
    Args:

    Returns:
        strsecond part of licence
    """


def show_progress_bar() -> None:
    """show progress bar
    Args:

    Returns:
        None
    """


def update_progress_bar(value: int) -> None:
    """update progress bar
    Args:
        value ( int): value

    Returns:
        None
    """


def hide_progress_bar() -> None:
    """hide progress bar
    Args:

    Returns:
        None
    """


def get_user_color(initial_color: int) -> int:
    """get user color
    Args:
        initial_color ( int): initial_color

    Returns:
        intthe colornumber
    """


def get_3d_linear_units() -> str:
    """get 3d linear units
    Args:

    Returns:
        str
    """


def get_3d_linear_display_units() -> str:
    """get 3d linear display units
    Args:

    Returns:
        str
    """


def get_3d_angular_units() -> str:
    """get 3d angular units
    Args:

    Returns:
        str
    """


def get_3d_angular_display_units() -> str:
    """get 3d angular display units
    Args:

    Returns:
        str
    """


def get_3d_build_date() -> str:
    """get 3d build date
    Args:

    Returns:
        str
    """


def set_project_elevation(elevation: float) -> None:
    """set project elevation
    Args:
        elevation ( float): elevation

    Returns:
        None
    """


def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """


def push_check_and_query_data() -> None:
    """push check and query data
    Args:

    Returns:
        None
    """


def pop_check_and_query_data() -> None:
    """pop check and query data
    Args:

    Returns:
        None
    """


def change_check_and_query_data_to_no_queries() -> None:
    """change check and query data to no queries
    Args:

    Returns:
        None
    """


def change_check_and_query_data_to_queries() -> None:
    """change check and query data to queries
    Args:

    Returns:
        None
    """


def is_direct_info_enabled() -> bool:
    """is direct info enabled
    Args:

    Returns:
        bool
    """


def enable_direct_info() -> None:
    """enable direct info
    Args:

    Returns:
        None
    """


def disable_direct_info() -> None:
    """disable direct info
    Args:

    Returns:
        None
    """


def load_attribute_display_settings(file_path: str) -> None:
    """load attribute display settings
    Args:
        file_path ( str): file_path

    Returns:
        None
    """


def set_project_description(description: str) -> None:
    """set project description
    Args:
        description ( str): description

    Returns:
        None
    """


def start_project_data_dialog() -> None:
    """start project data dialog
    Args:

    Returns:
        None
    """


def init_LxSDK() -> None:
    """init LxSDK
    Args:

    Returns:
        None
    """


def load_element_attribute_display_settings(file_path: str, elements: List[int]) -> None:
    """load element attribute display settings
    Args:
        file_path ( str): file_path
        elements ( List[int]): elements

    Returns:
        None
    """


def get_global_x_offset() -> float:
    """get global x offset
    Args:

    Returns:
        float
    """


def set_global_x_offset(offset: float) -> None:
    """set global x offset
    Args:
        offset ( float): offset

    Returns:
        None
    """


def get_global_y_offset() -> float:
    """get global y offset
    Args:

    Returns:
        float
    """


def set_global_y_offset(offset: float) -> None:
    """set global y offset
    Args:
        offset ( float): offset

    Returns:
        None
    """


def get_global_z_offset() -> float:
    """get global z offset
    Args:

    Returns:
        float
    """


def set_global_z_offset(offset: float) -> None:
    """set global z offset
    Args:
        offset ( float): offset

    Returns:
        None
    """


def show_north_arrow() -> None:
    """show north arrow
    Args:

    Returns:
        None
    """


def hide_north_arrow() -> None:
    """hide north arrow
    Args:

    Returns:
        None
    """


def is_north_arrow_visible() -> bool:
    """is north arrow visible
    Args:

    Returns:
        bool
    """


def get_north_angle() -> float:
    """get north angle
    Args:

    Returns:
        float
    """


def set_north_angle(north_angle: float) -> None:
    """set north angle
    Args:
        north_angle ( float): north_angle

    Returns:
        None
    """


def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get user file from dialog in path
    Args:
        name_filter ( str): name_filter
        path ( str): path

    Returns:
        str
    """


def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get new user file from dialog in path
    Args:
        name_filter ( str): name_filter
        path ( str): path

    Returns:
        str
    """


def enable_update_variant() -> None:
    """enable update variant
    Args:

    Returns:
        None
    """


def disable_update_variant() -> None:
    """disable update variant
    Args:

    Returns:
        None
    """


def get_user_points() -> List[point_3d]:
    """get user points
    Args:

    Returns:
        List[point_3d]
    """


def get_user_points_with_count(a0: int) -> List[point_3d]:
    """get user points with count
    Args:
        a0 ( int): a0

    Returns:
        List[point_3d]
    """


def get_user_path_from_dialog() -> str:
    """get user path from dialog
    Args:

    Returns:
        str
    """


def get_user_path_from_dialog_in_path(a0: str) -> str:
    """get user path from dialog in path
    Args:
        a0 ( str): a0

    Returns:
        str
    """


def execute_shortcut(a0: int, a1: int) -> None:
    """execute shortcut
    Args:
        a0 ( int): a0
        a1 ( int): a1

    Returns:
        None
    """


def get_3d_file_name() -> str:
    """get 3d file name
    Args:

    Returns:
        str3D file name
    """


def get_project_data(element_id: str) -> str:
    """get project data
    Args:
        element_id ( str): element_id

    Returns:
        strproject data
    """


def get_project_name() -> str:
    """get project name
    Args:

    Returns:
        strproject name
    """


def get_project_part() -> str:
    """get project part
    Args:

    Returns:
        strproject part
    """


def get_project_architect() -> str:
    """get project architect
    Args:

    Returns:
        strproject architect
    """


def get_project_number() -> str:
    """get project number
    Args:

    Returns:
        strproject number
    """


def get_project_customer() -> str:
    """get project customer
    Args:

    Returns:
        strproject customer
    """


def get_project_designer() -> str:
    """get project designer
    Args:

    Returns:
        strproject designer
    """


def get_project_deadline() -> str:
    """get project deadline
    Args:

    Returns:
        strproject deadline
    """


def get_project_user_attribute(number: int) -> str:
    """get project user attribute
    Args:
        number ( int): number

    Returns:
        strproject user attribute
    """


def get_project_user_attribute_name(number: int) -> str:
    """get project user attribute name
    Args:
        number ( int): number

    Returns:
        strproject user attribute name
    """


def get_project_latitude() -> float:
    """get project latitude
    Args:

    Returns:
        floatproject latitude
    """


def get_project_longitude() -> float:
    """get project longitude
    Args:

    Returns:
        floatproject longitude
    """


def get_project_postal_code() -> str:
    """get project postal code
    Args:

    Returns:
        strproject postal code
    """


def get_project_address() -> str:
    """get project address
    Args:

    Returns:
        strproject address
    """


def get_project_city() -> str:
    """get project city
    Args:

    Returns:
        strproject city
    """


def get_project_country() -> str:
    """get project country
    Args:

    Returns:
        strproject country
    """


def get_project_elevation() -> float:
    """get project elevation
    Args:

    Returns:
        floatproject elevation
    """


def get_project_description() -> str:
    """get project description
    Args:

    Returns:
        str
    """


def get_project_guid() -> str:
    """get project guid
    Args:

    Returns:
        strproject GUID
    """


def get_3d_userprofil_path() -> str:
    """get 3d userprofil path
    Args:

    Returns:
        strthe 3D userprofil path
    """


def get_plugin_path() -> str:
    """get plugin path
    Args:

    Returns:
        str
    """


def get_millimetre_from_imperial_string(value: str) -> float:
    """get millimetre from imperial string
    Args:
        value ( str): value

    Returns:
        float
    """


def get_imperial_string_from_millimetre(value: float) -> str:
    """get imperial string from millimetre
    Args:
        value ( float): value

    Returns:
        str
    """


def get_user_catalog_path() -> str:
    """get user catalog path
    Args:

    Returns:
        str
    """


def get_3d_hwnd() -> int:
    """get 3d hwnd
    Args:

    Returns:
        int3D HWND
    """


def close_cadwork_document_saved() -> None:
    """close cadwork document saved
    Args:

    Returns:
        None
    """


def close_cadwork_document_unsaved() -> None:
    """close cadwork document unsaved
    Args:

    Returns:
        None
    """


def get_use_of_global_coordinates() -> bool:
    """get use of global coordinates
    Args:

    Returns:
        bool
    """


def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """set use of global coordinates
    Args:
        use_of_global_coordinates ( bool): use_of_global_coordinates

    Returns:
        None
    """


def get_global_origin() -> point_3d:
    """get global origin
    Args:

    Returns:
        point_3dglobal origin
    """


def set_global_origin(global_origin: point_3d) -> None:
    """set global origin
    Args:
        global_origin ( point_3d): global_origin

    Returns:
        None
    """


def create_snapshot() -> str:
    """create snapshot
    Args:

    Returns:
        strsnapshot
    """
