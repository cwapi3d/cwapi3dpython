from typing import List
from cadwork import point_3d

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def get_3d_version() -> int:
    """Gets the 3D version

    Returns:
        3D version
    """

def get_3d_build() -> int:
    """Gets the 3D build

    Returns:
        3D build
    """

def get_3d_file_path() -> str:
    """Gets the 3D file path

    Returns:
        3D file path
    """

def set_project_data(element_id: str, data: str) -> None:
    """Sets the project data

    Parameters:
        element_id: element_id
        data: data

    Returns:
        None
    """

def print_error(message: str) -> None:
    """Prints an error

    Parameters:
        message: message

    Returns:
        None
    """

def get_language() -> str:
    """Gets the 3D language

    Returns:
        3D language
    """

def print_message(message: str, column: int) -> None:
    """Prints a message

    Parameters:
        message: message
        column: column

    Returns:
        None
    """

def get_user_int(message: str) -> int:
    """Prompts the user for an integer

    Parameters:
        message: message

    Returns:
        user integer
    """

def get_user_double(message: str) -> float:
    """Prompts the user for a double

    Parameters:
        message: message

    Returns:
        user double
    """

def get_user_bool(message: str, default_yes: bool) -> bool:
    """Prompts the user for a boolean

    Parameters:
        message: message
        default_yes: default_yes

    Returns:
        user boolean
    """

def get_user_string(message: str) -> str:
    """Prompts the user for a string

    Parameters:
        message: message

    Returns:
        user string
    """

def set_project_name(project_name: str) -> None:
    """Sets the project name

    Parameters:
        project_name: project_name

    Returns:
        None
    """

def set_project_number(project_number: str) -> None:
    """Sets the project number

    Parameters:
        project_number: project_number

    Returns:
        None
    """

def set_project_part(project_part: str) -> None:
    """Sets the project part

    Parameters:
        project_part: project_part

    Returns:
        None
    """

def set_project_architect(project_architect: str) -> None:
    """Sets the project architect

    Parameters:
        project_architect: project_architect

    Returns:
        None
    """

def set_project_customer(project_customer: str) -> None:
    """Sets the project customer

    Parameters:
        project_customer: project_customer

    Returns:
        None
    """

def set_project_designer(project_designer: str) -> None:
    """Sets the project designer

    Parameters:
        project_designer: project_designer

    Returns:
        None
    """

def set_project_deadline(project_deadline: str) -> None:
    """Sets the project deadline

    Parameters:
        project_deadline: project_deadline

    Returns:
        None
    """

def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """Sets the project user attribute

    Parameters:
        number: number
        user_attribute: user_attribute

    Returns:
        None
    """

def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Sets the project user attribute name

    Parameters:
        number: number
        user_attribute_name: user_attribute_name

    Returns:
        None
    """

def set_project_latitude(latitude: float) -> None:
    """Sets the project latitude

    Parameters:
        latitude: latitude

    Returns:
        None
    """

def set_project_longitude(longitude: float) -> None:
    """Sets the project longitude

    Parameters:
        longitude: longitude

    Returns:
        None
    """

def set_project_address(address: str) -> None:
    """Sets the project address

    Parameters:
        address: address

    Returns:
        None
    """

def set_project_postal_code(postal_code: str) -> None:
    """Sets the project postal code

    Parameters:
        postal_code: postal_code

    Returns:
        None
    """

def set_project_city(city: str) -> None:
    """Sets the project city

    Parameters:
        city: city

    Returns:
        None
    """

def set_project_country(country: str) -> None:
    """Sets the project country

    Parameters:
        country: country

    Returns:
        None
    """

def get_user_file_from_dialog(name_filter: str) -> str:
    """Gets a file with a dialog

    Parameters:
        name_filter: name_filter

    Returns:
        file path
    """

def get_client_number() -> str:
    """Gets the client number

    Returns:
        client number
    """

def get_user_point() -> point_3d:
    """Gets a point from the user

    Returns:
        user point
    """

def disable_auto_display_refresh() -> None:
    """Disables automatic display refresh

    Returns:
        None
    """

def enable_auto_display_refresh() -> None:
    """Enables automatic display refresh

    Returns:
        None
    """

def create_new_guid() -> str:
    """Creates a new GUID

    Returns:
        GUID
    """

def print_to_console(message: str) -> None:
    """Prints a message to the console

    Parameters:
        message: message

    Returns:
        None
    """

def export_screen_to_image(file_path: str, factor: int) -> None:
    """Exports the screen to an image

    Parameters:
        file_path: file_path
        factor: factor

    Returns:
        None
    """

def get_new_user_file_from_dialog(name_filter: str) -> str:
    """Gets a new file with a dialog

    Parameters:
        name_filter: name_filter

    Returns:
        file path
    """

def api_autostart(api_name: str, option: int) -> int:
    """api autostart

    Parameters:
        api_name: api_name
        option: option

    Returns:
        int
    """

def enable_autostart(api_name: str) -> None:
    """enable autostart

    Parameters:
        api_name: api_name

    Returns:
        None
    """

def disable_autostart(api_name: str) -> None:
    """disable autostart

    Parameters:
        api_name: api_name

    Returns:
        None
    """

def check_autostart(api_name: str) -> bool:
    """check autostart

    Parameters:
        api_name: api_name

    Returns:
        bool
    """

def delete_project_data(element_id: str) -> None:
    """Deletes the project data

    Parameters:
        element_id: element_id

    Returns:
        None
    """

def run_external_program(name: str) -> bool:
    """Runs a 3D external program

    Parameters:
        name: name

    Returns:
        external program return
    """

def save_3d_file_silently() -> None:
    """Saves the 3D file silently

    Returns:
        None
    """

def get_licence_first_part() -> str:
    """Gets the first part of the licence

    Returns:
        first part of licence
    """

def get_licence_second_part() -> str:
    """Gets the second part of the licence

    Returns:
        second part of licence
    """

def show_progress_bar() -> None:
    """Shows a ProgressBar in the CommandBar

    Returns:
        None
    """

def update_progress_bar(value: int) -> None:
    """Updates the ProgressBar with a value

    Parameters:
        value: value

    Returns:
        None
    """

def hide_progress_bar() -> None:
    """Hides the ProgressBar

    Returns:
        None
    """

def get_user_color(initial_color: int) -> int:
    """Gets a color choosen by the user

    Parameters:
        initial_color: initial_color

    Returns:
        the colornumber
    """

def get_3d_linear_units() -> str:
    """Gets the current linear units

    Returns:
        str
    """

def get_3d_linear_display_units() -> str:
    """Gets the current display units

    Returns:
        str
    """

def get_3d_angular_units() -> str:
    """Gets the current angular units

    Returns:
        str
    """

def get_3d_angular_display_units() -> str:
    """Gets the current angular display units

    Returns:
        str
    """

def get_3d_build_date() -> str:
    """Gets the current build date

    Returns:
        str
    """

def set_project_elevation(elevation: float) -> None:
    """Sets the project elevation

    Parameters:
        elevation: elevation

    Returns:
        None
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def push_check_and_query_data() -> None:
    """push check and query data

    Returns:
        None
    """

def pop_check_and_query_data() -> None:
    """pop check and query data

    Returns:
        None
    """

def change_check_and_query_data_to_no_queries() -> None:
    """change check and query data to no queries

    Returns:
        None
    """

def change_check_and_query_data_to_queries() -> None:
    """change check and query data to queries

    Returns:
        None
    """

def is_direct_info_enabled() -> bool:
    """is direct info enabled

    Returns:
        bool
    """

def enable_direct_info() -> None:
    """enable direct info

    Returns:
        None
    """

def disable_direct_info() -> None:
    """disable direct info

    Returns:
        None
    """

def load_attribute_display_settings(file_path: str) -> None:
    """load attribute display settings

    Parameters:
        file_path: file_path

    Returns:
        None
    """

def set_project_description(description: str) -> None:
    """set project description

    Parameters:
        description: description

    Returns:
        None
    """

def start_project_data_dialog() -> None:
    """start project data dialog

    Returns:
        None
    """

def init_LxSDK() -> None:
    """init LxSDK

    Returns:
        None
    """

def load_element_attribute_display_settings(file_path: str, elements: List[int]) -> None:
    """load element attribute display settings

    Parameters:
        file_path: file_path
        elements: elements

    Returns:
        None
    """

def get_global_x_offset() -> float:
    """get global x offset

    Returns:
        float
    """

def set_global_x_offset(offset: float) -> None:
    """set global x offset

    Parameters:
        offset: offset

    Returns:
        None
    """

def get_global_y_offset() -> float:
    """get global y offset

    Returns:
        float
    """

def set_global_y_offset(offset: float) -> None:
    """set global y offset

    Parameters:
        offset: offset

    Returns:
        None
    """

def get_global_z_offset() -> float:
    """get global z offset

    Returns:
        float
    """

def set_global_z_offset(offset: float) -> None:
    """set global z offset

    Parameters:
        offset: offset

    Returns:
        None
    """

def show_north_arrow() -> None:
    """show north arrow

    Returns:
        None
    """

def hide_north_arrow() -> None:
    """hide north arrow

    Returns:
        None
    """

def is_north_arrow_visible() -> bool:
    """is north arrow visible

    Returns:
        bool
    """

def get_north_angle() -> float:
    """get north angle

    Returns:
        float
    """

def set_north_angle(north_angle: float) -> None:
    """set north angle

    Parameters:
        north_angle: north_angle

    Returns:
        None
    """

def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get user file from dialog in path

    Parameters:
        name_filter: name_filter
        path: path

    Returns:
        str
    """

def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get new user file from dialog in path

    Parameters:
        name_filter: name_filter
        path: path

    Returns:
        str
    """

def enable_update_variant() -> None:
    """enable update variant

    Returns:
        None
    """

def disable_update_variant() -> None:
    """disable update variant

    Returns:
        None
    """

def get_user_points() -> List[point_3d]:
    """get user points

    Returns:
        List[point_3d]
    """

def get_user_points_with_count(a0: int) -> List[point_3d]:
    """get user points with count

    Parameters:
        a0: a0

    Returns:
        List[point_3d]
    """

def get_user_path_from_dialog() -> str:
    """get user path from dialog

    Returns:
        str
    """

def get_user_path_from_dialog_in_path(a0: str) -> str:
    """get user path from dialog in path

    Parameters:
        a0: a0

    Returns:
        str
    """

def execute_shortcut(a0: int, a1: int) -> None:
    """execute shortcut

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

def run_external_program_from_custom_directory(file_path: str) -> bool:
    """Runs a 3D external program from a custom file path

    Parameters:
        file_path: file_path

    Returns:
        external program return
    """

def get_3d_file_name() -> str:
    """Gets the 3D file name

    Returns:
        3D file name
    """

def get_project_data(element_id: str) -> str:
    """Gets the project data

    Parameters:
        element_id: element_id

    Returns:
        project data
    """

def get_project_name() -> str:
    """Gets the project name

    Returns:
        project name
    """

def get_project_part() -> str:
    """Sets the project part

    Returns:
        project part
    """

def get_project_architect() -> str:
    """Gets the project architect

    Returns:
        project architect
    """

def get_project_number() -> str:
    """Gets the project number

    Returns:
        project number
    """

def get_project_customer() -> str:
    """Gets the project customer

    Returns:
        project customer
    """

def get_project_designer() -> str:
    """Gets the project designer

    Returns:
        project designer
    """

def get_project_deadline() -> str:
    """Gets the project deadline

    Returns:
        project deadline
    """

def get_project_user_attribute(number: int) -> str:
    """Gets the project user attribute

    Parameters:
        number: number

    Returns:
        project user attribute
    """

def get_project_user_attribute_name(number: int) -> str:
    """Gets the project user attribute name

    Parameters:
        number: number

    Returns:
        project user attribute name
    """

def get_project_latitude() -> float:
    """Gets the project latitude

    Returns:
        project latitude
    """

def get_project_longitude() -> float:
    """Gets the project longitude

    Returns:
        project longitude
    """

def get_project_postal_code() -> str:
    """Gets the project postal code

    Returns:
        project postal code
    """

def get_project_address() -> str:
    """Gets the project address

    Returns:
        project address
    """

def get_project_city() -> str:
    """Gets the project city

    Returns:
        project city
    """

def get_project_country() -> str:
    """Gets the project country

    Returns:
        project country
    """

def get_project_elevation() -> float:
    """Gets the project elevation

    Returns:
        project elevation
    """

def get_project_description() -> str:
    """get project description

    Returns:
        str
    """

def get_project_guid() -> str:
    """Gets the project GUID

    Returns:
        project GUID
    """

def get_3d_userprofil_path() -> str:
    """Gets the 3D userprofil path

    Returns:
        the 3D userprofil path
    """

def get_plugin_path() -> str:
    """get plugin path

    Returns:
        str
    """

def get_millimetre_from_imperial_string(value: str) -> float:
    """get millimetre from imperial string

    Parameters:
        value: value

    Returns:
        float
    """

def get_imperial_string_from_millimetre(value: float) -> str:
    """get imperial string from millimetre

    Parameters:
        value: value

    Returns:
        str
    """

def get_user_catalog_path() -> str:
    """get user catalog path

    Returns:
        str
    """

def get_3d_hwnd() -> int:
    """Gets the 3D HWND

    Returns:
        3D HWND
    """

def close_cadwork_document_saved() -> None:
    """close cadwork saved

    Returns:
        None
    """

def close_cadwork_document_unsaved() -> None:
    """close cadwork document unsaved

    Returns:
        None
    """

def get_use_of_global_coordinates() -> bool:
    """get use of global coordinates

    Returns:
        bool
    """

def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """Sets the use of global coordinates

    Parameters:
        use_of_global_coordinates: use_of_global_coordinates

    Returns:
        None
    """

def get_global_origin() -> point_3d:
    """Gets the global origin

    Returns:
        global origin
    """

def set_global_origin(global_origin: point_3d) -> None:
    """Sets the global origin

    Parameters:
        global_origin: global_origin

    Returns:
        None
    """

def create_snapshot() -> str:
    """get snapshot from screen

    Returns:
        snapshot
    """

def get_3d_gui_upper_left_screen_coordinates() -> Tuple[int, int]:
    """get 3d gui upper left screen coordinates

    Returns:
        Tuple[int, int]
    """

