from typing import List, Tuple
from cadwork import point_3d


def get_last_error(error_code: int) -> str:
    """Gets the last error.

    Args:
        error_code: error code

    Returns:
        error string
    """


def get_3d_version() -> int:
    """Gets the 3D version.

    Returns:
        3d version
    """


def get_3d_build() -> int:
    """Gets the 3D build.

    Returns:
        3d build
    """


def get_3d_file_path() -> str:
    """Gets the current 3D file path.

    Returns:
        3d file path
    """


def set_project_data(data_id: str, data: str) -> None:
    """Sets the project data

    Args:
        data_id: data id
        data: data

    """


def print_error(message: str) -> None:
    """Prints an error

    Args:
        message: message

    """


def get_language() -> str:
    """Gets the 3D language

    Returns:
        3d language
    """


def print_message(message: str, column: int) -> None:
    """Prints a message

    Args:
        message: message
        column: column

    """


def get_user_int(message: str) -> int:
    """Prompts the user for an integer

    Args:
        message: message

    Returns:
        query result
    """


def get_user_double(message: str) -> float:
    """Prompts the user for a double

    Args:
        message: message

    Returns:
        query result
    """


def get_user_bool(message: str, default_yes: bool) -> bool:
    """Prompts the user for a boolean

    Args:
        message: message
        default_yes: default prompt

    Returns:
        query result
    """


def get_user_string(message: str) -> str:
    """Prompts the user for a string

    Args:
        message: message

    Returns:
        query result
    """


def set_project_name(project_name: str) -> None:
    """Sets the project name

    Args:
        project_name: project name

    """


def set_project_number(project_number: str) -> None:
    """Sets the project number

    Args:
        project_number: project number

    """


def set_project_part(project_part: str) -> None:
    """Sets the project part

    Args:
        project_part: project part

    """


def set_project_architect(project_architect: str) -> None:
    """Sets the project architect

    Args:
        project_architect: project architect

    """


def set_project_customer(project_customer: str) -> None:
    """Sets the project customer

    Args:
        project_customer: project customer

    """


def set_project_designer(project_designer: str) -> None:
    """Sets the project designer

    Args:
        project_designer: project designer

    """


def set_project_deadline(project_deadline: str) -> None:
    """Sets the project deadline

    Args:
        project_deadline: project deadline

    """


def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """Sets the project user attribute

    Args:
        number: number
        user_attribute: user_attribute

    """


def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Sets the project user attribute name

    Args:
        number: number
        user_attribute_name: user_attribute_name

    """


def set_project_latitude(latitude: float) -> None:
    """Sets the project latitude

    Args:
        latitude: latitude

    """


def set_project_longitude(longitude: float) -> None:
    """Sets the project longitude

    Args:
        longitude: longitude

    """


def set_project_address(address: str) -> None:
    """Sets the project address

    Args:
        address: address

    """


def set_project_postal_code(postal_code: str) -> None:
    """Sets the project postal code

    Args:
        postal_code: postal code

    """


def set_project_city(city: str) -> None:
    """Sets the project city

    Args:
        city: city

    """


def set_project_country(country: str) -> None:
    """Sets the project country

    Args:
        country: country

    """


def get_user_file_from_dialog(name_filter: str) -> str:
    """Gets a file with a dialog

    Args:
        name_filter: name filter

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
        query result
    """


def disable_auto_display_refresh() -> None:
    """Disables automatic display refresh

    """


def enable_auto_display_refresh() -> None:
    """Enables automatic display refresh

    """


def create_new_guid() -> str:
    """Creates a new GUID

    Returns:
        guid
    """


def print_to_console(message: str) -> None:
    """Prints a message to the console

    Args:
        message: message

    """


def export_screen_to_image(file_path: str, factor: int) -> None:
    """Exports the screen to an image

    Args:
        file_path: file path
        factor: factor

    """


def get_new_user_file_from_dialog(name_filter: str) -> str:
    """Gets a new file with a dialog

    Args:
        name_filter: name filter

    Returns:
        file path
    """


def api_autostart(api_name: str, option: int) -> int:
    """api autostart

    Args:
        api_name: plugin_name
        option: option

    Returns:
        foo
    """


def enable_autostart(api_name: str) -> None:
    """enable autostart

    Args:
        api_name: plugin_name

    """


def disable_autostart(api_name: str) -> None:
    """disable autostart

    Args:
        api_name: plugin_name

    """


def check_autostart(api_name: str) -> bool:
    """check autostart

    Args:
        api_name: plugin name

    Returns:
        plugin autostart status
    """


def delete_project_data(data_id: str) -> None:
    """Deletes the project data

    Args:
        data_id: data id

    """


def run_external_program(name: str) -> bool:
    """Runs a 3D external program

    Args:
        name: plugin name

    Returns:
        plugin return code
    """


def save_3d_file_silently() -> None:
    """Saves the 3D file silently

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

    """


def update_progress_bar(value: int) -> None:
    """Updates the ProgressBar with a value

    Args:
        value: value

    """


def hide_progress_bar() -> None:
    """Hides the ProgressBar

    """


def get_user_color(initial_color: int) -> int:
    """Gets a color choosen by the user

    Args:
        initial_color: default color

    Returns:
        query result
    """


def get_3d_linear_units() -> str:
    """Gets the current linear units

    Returns:
        linear units
    """


def get_3d_linear_display_units() -> str:
    """Gets the current display units

    Returns:
        display units
    """


def get_3d_angular_units() -> str:
    """Gets the current angular units

    Returns:
        angular units
    """


def get_3d_angular_display_units() -> str:
    """Gets the current angular display units

    Returns:
        angular display units
    """


def get_3d_build_date() -> str:
    """Gets the current build date

    Returns:
        3d build date
    """


def set_project_elevation(elevation: float) -> None:
    """Sets the project elevation

    Args:
        elevation: elevation

    """


def clear_errors() -> None:
    """clear errors

    """


def push_check_and_query_data() -> None:
    """push check and query data

    """


def pop_check_and_query_data() -> None:
    """pop check and query data

    """


def change_check_and_query_data_to_no_queries() -> None:
    """change check and query data to no queries

    """


def change_check_and_query_data_to_queries() -> None:
    """change check and query data to queries

    """


def is_direct_info_enabled() -> bool:
    """is direct info enabled

    Returns:
        direct info status
    """


def enable_direct_info() -> None:
    """enable direct info

    """


def disable_direct_info() -> None:
    """disable direct info

    """


def load_attribute_display_settings(file_path: str) -> None:
    """load attribute display settings

    Args:
        file_path: file path

    """


def set_project_description(description: str) -> None:
    """set project description

    Args:
        description: description

    """


def start_project_data_dialog() -> None:
    """start project data dialog


    """


def init_LxSDK() -> None:
    """init LxSDK

    """


def load_element_attribute_display_settings(file_path: str, elements: List[int]) -> None:
    """load element attribute display settings

    Args:
        file_path: file path
        elements: elements

    """


def get_global_x_offset() -> float:
    """get global x offset

    Returns:
        global x offset
    """


def set_global_x_offset(offset: float) -> None:
    """set global x offset

    Args:
        offset: offset
    """


def get_global_y_offset() -> float:
    """get global y offset

    Returns:
        global y offset
    """


def set_global_y_offset(offset: float) -> None:
    """set global y offset

    Args:
        offset: offset

    """


def get_global_z_offset() -> float:
    """get global z offset

    Returns:
        global z offset
    """


def set_global_z_offset(offset: float) -> None:
    """set global z offset

    Args:
        offset: offset

    """


def show_north_arrow() -> None:
    """show north arrow

    """


def hide_north_arrow() -> None:
    """hide north arrow

    """


def is_north_arrow_visible() -> bool:
    """is north arrow visible

    Returns:
        north arrow status
    """


def get_north_angle() -> float:
    """get north angle

    Returns:
        north angle
    """


def set_north_angle(north_angle: float) -> None:
    """set north angle

    Args:
        north_angle: north angle

    """


def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get user file from dialog in path

    Args:
        name_filter: name filter
        path: path

    Returns:
        file path
    """


def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """get new user file from dialog in path

    Args:
        name_filter: name filter
        path: path

    Returns:
        file path
    """


def enable_update_variant() -> None:
    """enable update variant

    """


def disable_update_variant() -> None:
    """disable update variant

    """


def get_user_points() -> List[point_3d]:
    """get user points

    Returns:
        query result
    """


def get_user_points_with_count(a0: int) -> List[point_3d]:
    """get user points with count

    Args:
        a0: a0

    Returns:
        query result
    """


def get_user_path_from_dialog() -> str:
    """get user path from dialog

    Returns:
        path
    """


def get_user_path_from_dialog_in_path(a0: str) -> str:
    """get user path from dialog in path

    Args:
        a0: a0

    Returns:
        path
    """


def execute_shortcut(a0: int, a1: int) -> None:
    """execute shortcut

    Args:
        a0: a0
        a1: a1

    """


def run_external_program_from_custom_directory(file_path: str) -> bool:
    """Runs a 3D external program from a custom file path

    Args:
        file_path: file path

    Returns:
        plugin return code
    """


def get_3d_file_name() -> str:
    """Gets the 3D file name

    Returns:
        3d file name
    """


def get_project_data(data_id: str) -> str:
    """Gets the project data

    Args:
        data_id: data id

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

    Args:
        number: attribute number

    Returns:
        project user attribute
    """


def get_project_user_attribute_name(number: int) -> str:
    """Gets the project user attribute name

    Args:
        number: attribute number

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
        project description
    """


def get_project_guid() -> str:
    """Gets the project GUID

    Returns:
        project guid
    """


def get_3d_userprofil_path() -> str:
    """Gets the 3D userprofil path

    Returns:
        path
    """


def get_plugin_path() -> str:
    """get plugin path

    Returns:
        path
    """


def get_millimetre_from_imperial_string(value: str) -> float:
    """get millimetre from imperial string

    Args:
        value: value

    Returns:
        value
    """


def get_imperial_string_from_millimetre(value: float) -> str:
    """get imperial string from millimetre

    Args:
        value: value

    Returns:
        value
    """


def get_user_catalog_path() -> str:
    """get user catalog path

    Returns:
        path
    """


def get_3d_hwnd() -> int:
    """Gets the 3D HWND

    Returns:
        3d hwnd
    """


def close_cadwork_document_saved() -> None:
    """close cadwork saved

    """


def close_cadwork_document_unsaved() -> None:
    """close cadwork document unsaved

    """


def get_use_of_global_coordinates() -> bool:
    """get use of global coordinates

    Returns:
        global coordinates status
    """


def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """Sets the use of global coordinates

    Args:
        use_of_global_coordinates: global coordinates status

    """


def get_global_origin() -> point_3d:
    """Gets the global origin

    Returns:
        global origin
    """


def set_global_origin(global_origin: point_3d) -> None:
    """Sets the global origin

    Args:
        global_origin: global origin

    """


def create_snapshot() -> str:
    """get snapshot from screen

    Returns:
        snapshot
    """


def get_3d_gui_upper_left_screen_coordinates() -> Tuple[int, int]:
    """get 3d gui upper left screen coordinates

    Returns:
        screen coordinates
    """
