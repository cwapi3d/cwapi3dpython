from typing import List
from cadwork import point_3d


def get_3d_version() -> int:
    """

    Returns:
        int: version
    """


def get_3d_build() -> int:
    """

    Returns:
        int: 3D build
    """


def get_3d_file_name() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: file name
    """


def get_3d_file_path() -> str:
    """

    Returns:
        str: 3D file path
    """


def set_project_data(data_id: str, value: str) -> None:
    """

    Args:
        data_id (str): project data ID
        value (str): project data
    """


def get_project_data(data_id: str) -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        data_id (str): project data ID

    Returns:
        str: project data
    """


def get_language() -> str:
    """

    Returns:
        str: language
    """


def print_message(text: str, row: int, column: int) -> None:
    """Prints a message

    Args:
        text (str): message/text
        row (int): a row
        column (int): a column
    """


def print_error(text: str) -> None:
    """prints a message. 'locks' 3d GUI until user confirms with a right-click.

    Args:
        text (str): message/text
    """


def get_user_int(text: str) -> int:
    """Prompts the user for an integer

    Args:
        text (str): message

    Returns:
        int: user integer
    """


def get_user_double(text: str) -> float:
    """Prompts the user for a double

    Args:
        text (str): message

    Returns:
        float: user double
    """


def get_user_bool(text: str, default: bool = True) -> bool:
    """Prompts the user for a boolean

    Args:
        text (str): message
        default (bool): Yes default value

    Returns:
        bool: user boolean
    """


def get_user_string(text: str) -> str:
    """Prompts the user for a string

    Args:
        text (str): message

    Returns:
        str: user string
    """


def get_project_name() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: project name
    """


def set_project_name(value: str) -> None:
    """

    Args:
        value (str): project name
    """


def get_project_number() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: project number
    """


def set_project_number(value: str) -> None:
    """

    Args:
        value (str): project number
    """


def get_project_part() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: project part
    """


def set_project_part(value: str) -> None:
    """

    Args:
        value (str): project part
    """


def get_project_architect() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: project architect
    """


def set_project_architect(value: str) -> None:
    """

    Args:
        value (str): project architect
    """


def get_project_customer() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_customer(value: str) -> None:
    """

    Args:
        value (str): value
    """


def get_project_designer() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_designer(value: str) -> None:
    """

    Args:
        value (str): value
    """


def get_project_deadline() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_deadline(value: str) -> None:
    """

    Args:
        value (str): value
    """


def get_project_user_attribute(number: int) -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): user attribute number

    Returns:
        str: value
    """


def set_project_user_attribute(number: int, value: str) -> None:
    """

    Args:
        number (int): user attribute number
        value (str): value
    """


def get_project_user_attribute_name(number: int) -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        number (int): user attribute number

    Returns:
        str: value
    """


def set_project_user_attribute_name(number: int, value: str) -> None:
    """

    Args:
        number (int): user attribute number
        value (str): value
    """


def get_project_latitude() -> float:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        float: latitude
    """


def get_project_longitude(value: float) -> None:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        value (float): longitude
    """


def set_project_latitude() -> float:
    """

    Returns:
        float: latitude value
    """


def set_project_longitude(value: float) -> None:
    """

    Args:
        value (float): longitude value
    """


def get_project_address() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_address(value: float) -> None:
    """

    Args:
        value (float): adress
    """


def get_project_postal_code() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_postal_code(value: float) -> None:
    """

    Args:
        value (float): postal code
    """


def get_project_city() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_city(value: float) -> None:
    """

    Args:
        value (float): value
    """


def get_project_country() -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: value
    """


def set_project_country(value: float) -> None:
    """

    Args:
        value (float): value
    """


def get_3d_userprofil_path() -> str:
    """Get 3D userprofile path

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: path
    """


def get_plugin_path() -> str:
    """Get 3D plugin path

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: path
    """


def get_user_file_from_dialog(type_filter: str) -> str:
    """ets a file with a dialog

    Args:
        type_filter (str): dialog file filter

    Returns:
        str: file path
    """


def get_client_number() -> str:
    """

    Returns:
        str: client number
    """


def get_user_point() -> point_3d:
    """Gets a point from the user

    Returns:
        point_3d: user point
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
        str: GUID
    """


def print_to_console(text: str) -> None:
    """Prints a message to the console

    Args:
        text (str): message
    """


def export_screen_to_image(file: str, factor: int) -> None:
    """Exports the screen to an image

    Args:
        file (str): file path
        factor (int): image factor
    """


def get_new_user_file_from_dialog(type_filter: str) -> str:
    """Gets a new file with a dialog

    Args:
        type_filter (str): dialog file filter

    Returns:
        str: file path
    """


def api_autostart(name: str, option: int) -> None:
    """

    Args:
        name (str): api name
        option (int): option
    """


def enable_autostart(name: str) -> None:
    """

    Args:
        name (str): api name
    """


def disable_autostart(name: str) -> None:
    """

    Args:
        name (str): api name
    """


def check_autostart(name: str) -> bool:
    """

    Args:
        name (str): api name

    Returns:
        bool: result
    """


def delete_project_data(data_id: str) -> None:
    """

    Args:
        data_id (str): data id
    """


def run_external_program(name: str) -> None:
    """

    Args:
        name (str): external program name
    """


def save_3d_file_silently() -> None:
    """Saves the 3D file silently
    """


def get_project_guid() -> str:
    """

    Returns:
        str: GUID
    """


def get_licence_first_part() -> str:
    """Gets the first part of the licence

    Returns:
        str: first part of license
    """


def get_licence_second_part() -> str:
    """Gets the second part of the licence

    Returns:
        str: second part of licence
    """


def show_progress_bar() -> None:
    """Shows a ProgressBar in the CommandBar
    """


def update_progress_bar(status: int) -> None:
    """Updates the ProgressBar with a value

    Args:
        status (int): Value between 0 and 100
    """


def hide_progress_bar() -> None:
    """Hides the ProgressBar
    """


def get_user_color(color: int) -> int:
    """Gets a color choosen by the user

    Args:
        color (int): initial color

    Returns:
        int: color number
    """


def get_3d_linear_units() -> str:
    """Gets the current linear units

    Returns:
        str: value
    """


def get_3d_linear_display_units() -> str:
    """Gets the current display units

    Returns:
        str: value
    """


def get_3d_angular_units() -> str:
    """_summary_

    Returns:
        str: value
    """


def get_3d_angular_display_units() -> str:
    """Gets the current angular display units

    Returns:
        str: value
    """


def get_3d_build_date() -> str:
    """Gets the current build date

    Returns:
        str: value
    """


def get_project_elevation() -> float:
    """Gets the project elevation

    Returns:
        float: elevation
    """


def set_project_elevation(value: float) -> None:
    """Sets the project elevation

    Args:
        value (float): value
    """


def push_check_and_query_data() -> None:
    """disable check and query prompts
    utility_controller.push_check_and_query_data()
    utility_controller.change_check_and_query_data_to_no_queries()
    """


def pop_check_and_query_data() -> None:
    """restores check and query prompts
    utility_controller.pop_check_and_query_data()
    """


def change_check_and_query_data_to_no_queries() -> None:
    """
    """


def change_check_and_query_data_to_queries() -> None:
    """
    """


def load_attribute_display_settings(file_path: str) -> None:
    """

    Args:
        file_path (str): a file path
    """


def load_element_attribute_display_settings(file_path: str, elements: List[int]) -> None:
    """

    Args:
        file_path (str): a file path
        elements (List[int]): element IDs
    """


def get_global_x_offset() -> float:
    """

    Returns:
        float: global x offset
    """


def set_global_x_offset(offset: float) -> None:
    """

    Args:
        offset (float): a offset value
    """


def get_global_y_offset() -> float:
    """

    Returns:
        float: global y offset
    """


def set_global_y_offset(offset: float) -> None:
    """

    Args:
        offset (float): a offset value
    """


def get_global_z_offset() -> float:
    """

    Returns:
        float: global z offset
    """


def set_global_z_offset(offset: float) -> None:
    """

    Args:
        offset (float): a offset value
    """


def show_north_arrow() -> None:
    """
    """


def hide_north_arrow() -> None:
    """
    """


def is_north_arrow_visible() -> bool:
    """checks if north arrow is visible

    Returns:
        bool: is visible
    """


def get_north_angle() -> float:
    """

    Returns:
        float: angle
    """


def set_north_angle(north_angle: float) -> None:
    """

    Args:
        north_angle (float): a angle value
    """


def get_millimetre_from_imperial_string(value: str) -> float:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        value (str): imperial string

    Returns:
        float: millimetre value
    """


def get_imperial_string_from_millimetre(value: float) -> str:
    """

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        value (float): millimetre value

    Returns:
        str: imperial string
    """


def get_user_points() -> List[point_3d]:
    """Prompt user to select points. A rubberband is shown during the point selection. 

    Examples:
        >>> utility_controller.get_user_points()
            [[-13717.500000, -23.500000, 6227.000000], [-18757.500000, 8177.500000, 6254.000000], 
            [-16257.500000, 8177.500000, 6254.000000], [-13757.500000, 8177.500000, 6254.000000]]

    Returns:
        List[point_3d]: point list
    """


def get_user_points_with_count(count: int) -> List[point_3d]:
    """Prompt user to select n points. A rubberband is shown during the point selection. 

    Examples:
        >>> utility_controller.get_user_points_with_count(3)
            [[-7271.500000, -23.500000, 6227.000000], [-8757.500000, 8177.500000, 6254.000000], 
            [-11157.500000, 8112.500000, 6254.000000]]
    Args:
        count (int): count points to select

    Returns:
        List[point_3d]: selected points
    """
