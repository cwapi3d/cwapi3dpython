from typing import List
from typing import Tuple
from cadwork.api_types import ElementId
from cadwork.point_3d import point_3d
from cadwork.window_geometry import window_geometry
from cadwork.shortcut_key import shortcut_key
from cadwork.shortcut_key_modifier import shortcut_key_modifier


def get_3d_version() -> int:
    """Gets the 3D version.

    Returns:
        The 3D version.
    """

def get_3d_build() -> int:
    """Gets the 3D build.

    Returns:
        The 3D build.
    """

def get_3d_file_path() -> str:
    """Gets the 3D file path.

    Returns:
        The 3D file path.
    """

def set_project_data(project_data_id: str, data: str) -> None:
    """Sets the project data.

    Parameters:
        project_data_id: The project data id.
        data: The data to set.
    """


def print_error(message: str) -> None:
    """Prints an error.

    Parameters:
        message: The error message.
    """


def get_language() -> str:
    """Gets the 3D language.

    Returns:
        The language.
    """


def print_message(message: str, row: int, column: int) -> None:
    """Prints a message.

    Parameters:
        message: The message to print.
        row: The row to print the message in.
        column: The column to print the message in.
    """


def get_user_int(message: str) -> int:
    """Prompts the user for an integer.

    Parameters:
        message: The message to display.

    Returns:
        The user input integer.
    """


def get_user_double(message: str) -> float:
    """Prompts the user for a double.

    Parameters:
        message: The message to display.

    Returns:
        The user input double.
    """


def get_user_bool(message: str, default_yes: bool) -> bool:
    """Prompts the user for a boolean.

    Parameters:
        message: The message to display.
        default_yes: The default value, True by default.

    Returns:
        The user input boolean.
    """


def get_user_string(message: str) -> str:
    """Prompts the user for a string.

    Parameters:
        message: The message to display.

    Returns:
        The user input string.
    """


def set_project_name(project_name: str) -> None:
    """Sets the project name.

    Parameters:
        project_name: The project name.
    """


def set_project_number(project_number: str) -> None:
    """Sets the project number.

    Parameters:
        project_number: The project number.
    """


def set_project_part(project_part: str) -> None:
    """Sets the project part.

    Parameters:
        project_part: The project part.
    """


def set_project_architect(project_architect: str) -> None:
    """Sets the project architect.

    Parameters:
        project_architect: The project architect.
    """


def set_project_customer(project_customer: str) -> None:
    """Sets the project customer.

    Parameters:
        project_customer: The project customer.
    """


def set_project_designer(project_designer: str) -> None:
    """Sets the project designer.

    Parameters:
        project_designer: The project designer.
    """


def set_project_deadline(project_deadline: str) -> None:
    """Sets the project deadline.

    Parameters:
        project_deadline: The project deadline.
    """


def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """Sets the project user attribute.

    Parameters:
        number: The project user attribute number.
        user_attribute: The project user attribute.
    """


def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Sets the project user attribute name.

    Parameters:
        number: The project user attribute number.
        user_attribute_name: The project user attribute name.
    """


def set_project_latitude(latitude: float) -> None:
    """Sets the project latitude.

    Parameters:
        latitude: The project latitude.
    """


def set_project_longitude(longitude: float) -> None:
    """Sets the project longitude.

    Parameters:
        longitude: The project longitude.
    """


def set_project_address(address: str) -> None:
    """Sets the project address.

    Parameters:
        address: The project address.
    """


def set_project_postal_code(postal_code: str) -> None:
    """Sets the project postal code.

    Parameters:
        postal_code: The project postal code.
    """


def set_project_city(city: str) -> None:
    """Sets the project city.

    Parameters:
        city: The project city.
    """


def set_project_country(country: str) -> None:
    """Sets the project country.

    Parameters:
        country: The project country.
    """


def get_user_file_from_dialog(name_filter: str) -> str:
    """Gets a file with a dialog.

    Parameters:
        name_filter: The dialog file filter.

    Returns:
        The file path.
    """


def get_client_number() -> str:
    """Gets the client number.

    Returns:
        The client number.
    """


def get_user_point() -> point_3d:
    """Gets a point from the user.

    Returns:
        The user point.
    """


def disable_auto_display_refresh() -> None:
    """Disables automatic display refresh.
       This function prevents the display from updating automatically,
       which can significantly improve performance during operations that involve multiple changes or computations.
       The display will remain static until explicitly refreshed by the user.
    """


def enable_auto_display_refresh() -> None:
    """Enables automatic display refresh.
       This function restores the default behavior where the display updates automatically after each operation. 
       Use this function to resume normal display updates after previously disabling them with disable_auto_display_refresh().
       It's recommended to call this function after completing operations that required disabled display refreshing.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc
        >>> import element_controller as ec
        >>> uc.disable_auto_display_refresh()
        >>> # Perform operations that require disabled display refresh
        >>> your_list_of_elements: List[int] = []
        >>> uc.enable_auto_display_refresh()
        >>> ec.recreate_elements(your_list_of_elements)

    Note:
        If elements were created while display refresh was disabled, it's important
        to recreate these elements after enabling the display refresh to ensure they
        are properly visualized in cadwork.
    """


def create_new_guid() -> str:
    """Creates a new GUID.

    Returns:
        The new GUID.
    """


def print_to_console(message: str) -> None:
    """Prints a message to the console.

    Parameters:
        message: The message.
    """


def export_screen_to_image(file_path: str, factor: int) -> None:
    """Exports the screen to an image.

    Parameters:
        file_path: The file path.
        factor: The image factor.
    """


def get_new_user_file_from_dialog(name_filter: str) -> str:
    """Gets a new file with a dialog.

    Parameters:
        name_filter: The dialog file filter.

    Returns:
        The file path.
    """

 
def api_autostart(api_name: str, option: int) -> int:
    """Sets an API autostart option.

    Parameters:
        api_name: The name of the API be managed.
        option: The autostart option to use.


            - -1: Checks if API is configured for autostart without making changes. Returns 1 if API is found, 0 if not, or -1 in case of errors.
            - 1: Enables autostart for the specified API.
            - 0: Disables autostart for the specified API.

    Note:
    This function reads and updates alias and module configuration files
    to manage the autostart state of the API.

    Examples:
        >>> api_autostart("my_api", 1)  # Enable autostart
        >>> api_autostart("my_api", 0)  # Disable autostart
        >>> api_autostart("my_api", -1)  # Check current autostart state

    Returns:
        The value of option if the operation is successful, or -1 in case of errors.
    """


def enable_autostart(api_name: str) -> None:
    """Enables autostart for a given API.

    Parameters:
        api_name: The name of the API for which to enable autostart.
    """


def disable_autostart(api_name: str) -> None:
    """Disables autostart for a given API.

    Parameters:
        api_name: The name of the API for which to disable autostart.
    """


def check_autostart(api_name: str) -> bool:
    """Checks if autostart is enabled for a given API.

    Parameters:
        api_name: The name of the API to check.

    Returns:
        True if autostart is enabled, false otherwise.
    """


def delete_project_data(element_id: str) -> None:
    """Deletes the project data.

    Parameters:
        element_id: The project data id.
    """


def run_external_program(name: str) -> bool:
    """Runs a 3D external program.

    Parameters:
        name: The external program name.

    Returns:
        False if the program could not be run, true otherwise.
    """


def save_3d_file_silently() -> None:
    """Saves the 3D file silently.
    """


def get_licence_first_part() -> str:
    """Gets the first part of the licence.

    Returns:
        The first part of the licence.
    """


def get_licence_second_part() -> str:
    """Gets the second part of the licence.

    Returns:
        The second part of the licence.
    """


def show_progress_bar() -> None:
    """Shows a ProgressBar in the CommandBar.
    """


def update_progress_bar(value: int) -> None:
    """Updates the ProgressBar with a value.

    Parameters:
        value: A value between 0 and 100.
    """


def hide_progress_bar() -> None:
    """Hides the ProgressBar.
    """


def get_user_color(initial_color: int) -> int:
    """Gets a color choosen by the user.

    Parameters:
        initial_color: The initial color.

    Returns:
        The color number.
    """


def get_3d_linear_units() -> str:
    """Gets the current linear units.

    Returns:
        The current linear units.
    """


def get_3d_linear_display_units() -> str:
    """Gets the current display units.

    Returns:
        The current display units.
    """


def get_3d_angular_units() -> str:
    """Gets the current angular units.

    Returns:
        The current angular units.
    """


def get_3d_angular_display_units() -> str:
    """Gets the current angular display units.

    Returns:
        The current angular display units.
    """


def get_3d_build_date() -> str:
    """Gets the current build date.

    Returns:
        The current build date.
    """


def set_project_elevation(elevation: float) -> None:
    """Sets the project elevation.

    Parameters:
        elevation: The project elevation.
    """


def clear_errors() -> None:
    """Clears all errors.
    """


def push_check_and_query_data() -> None:
    """Pushes the current state of check and query data onto a stack.
    """


def pop_check_and_query_data() -> None:
    """Pops the most recent state of check and query data from the stack.
    """


def change_check_and_query_data_to_no_queries() -> None:
    """Changes the current state of check and query data to no queries.
    """


def change_check_and_query_data_to_queries() -> None:
    """Changes the current state of check and query data to allow queries.
    """


def is_direct_info_enabled() -> bool:
    """Checks if Direct Info is enabled.

    Returns:
        True if Direct Info is enabled, false otherwise.
    """


def enable_direct_info() -> None:
    """Enables Direct Info.
    """


def disable_direct_info() -> None:
    """Disables Direct Info.
    """


def load_attribute_display_settings(file_path: str) -> None:
    """Loads attribute display settings from a file.

    Parameters:
        file_path: The path to the file containing the settings.
    """


def set_project_description(description: str) -> None:
    """Sets the project description.

    Parameters:
        description: The new description for the project.
    """


def start_project_data_dialog() -> None:
    """Starts the project data dialog.
    """


def init_LxSDK() -> None:
    """Initializes the LxSDK.
    """


def load_element_attribute_display_settings(file_path: str, elements: List[ElementId]) -> None:
    """Loads element attribute display settings from a file.

    Parameters:
        file_path: The path to the file containing the settings.
        elements: The element list for which to load the settings.
    """


def get_global_x_offset() -> float:
    """Gets the global X offset.

    Returns:
        The global X offset.
    """


def set_global_x_offset(offset: float) -> None:
    """Sets the global X offset.

    Parameters:
        offset: The new global X offset.
    """


def get_global_y_offset() -> float:
    """Gets the global Y offset.

    Returns:
        The global Y offset.
    """


def set_global_y_offset(offset: float) -> None:
    """Sets the global Y offset.

    Parameters:
        offset: The new global Y offset.
    """


def get_global_z_offset() -> float:
    """Gets the global Z offset.

    Returns:
        The global Z offset.
    """


def set_global_z_offset(offset: float) -> None:
    """Sets the global Z offset.

    Parameters:
        offset: The new global Z offset.
    """


def show_north_arrow() -> None:
    """Shows the north arrow on the 3D view.
    """


def hide_north_arrow() -> None:
    """Hides the north arrow on the 3D view.
    """


def is_north_arrow_visible() -> bool:
    """Checks if the north arrow is visible on the 3D view.

    Returns:
        True if the north arrow is visible, false otherwise.
    """


def get_north_angle() -> float:
    """Gets the angle of the north direction.

    Returns:
        The angle of the north direction in degrees.
    """


def set_north_angle(north_angle: float) -> None:
    """Sets the angle of the north direction.

    Parameters:
        north_angle: The angle of the north direction in degrees.
    """


def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Gets a user file from a dialog in a specified path.

    Parameters:
        name_filter: The filter for the dialog.
        path: The path in which to get the user file.

    Returns:
        A string containing the user file.
    """


def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Gets a new user file from a dialog in a specified path.

    Parameters:
        name_filter: The filter for the dialog.
        path: The path in which to get the new user file.

    Returns:
        A string containing the new user file.
    """


def enable_update_variant() -> None:
    """Enables the update variant.
    """


def disable_update_variant() -> None:
    """Disables the update variant.
    """


def get_user_points() -> List[point_3d]:
    """Gets user points.

    Returns:
        A list of user points.
    """


def get_user_points_with_count(count: int) -> List[point_3d]:
    """Gets user points with a specified count.

    Parameters:
        count: The number of user points to get.

    Returns:
        A list of user points.
    """


def get_user_path_from_dialog() -> str:
    """Gets the user path from a dialog.

    Returns:
        A string containing the user path.
    """


def get_user_path_from_dialog_in_path(path: str) -> str:
    """Gets the user path from a dialog in a specified path.

    Parameters:
        path: The path in which to get the user path.

    Returns:
        A string containing the user path.
    """


def execute_shortcut(shortcut_key_modifier: shortcut_key_modifier, shortcut_key: shortcut_key) -> None:
    """Executes a shortcut.

    Parameters:
        shortcut_key_modifier: The modifier key for the shortcut.
        shortcut_key: The key for the shortcut.
    """


def run_external_program_from_custom_directory(file_path: str) -> bool:
    """Runs a 3D external program from a custom directory.

    Parameters:
        file_path: The external program file path.

    Returns:
        False if error, true otherwise.
    """


def get_3d_file_name() -> str:
    """Gets the 3D file name.

    Returns:
        The 3D file name.
    """


def get_project_data(element_id: str) -> str:
    """Gets the project data.

    Parameters:
        element_id: The project data id.

    Returns:
        The project data.
    """


def get_project_name() -> str:
    """Gets the project name.

    Returns:
        The project name.
    """


def get_project_part() -> str:
    """Gets the project part.

    Returns:
        The project part.
    """


def get_project_architect() -> str:
    """Gets the project architect.

    Returns:
        The project architect.
    """


def get_project_number() -> str:
    """Gets the project number.

    Returns:
        The project number.
    """


def get_project_customer() -> str:
    """Gets the project customer.

    Returns:
        The project customer.
    """


def get_project_designer() -> str:
    """Gets the project designer.

    Returns:
        The project designer.
    """


def get_project_deadline() -> str:
    """Gets the project deadline.

    Returns:
        The project deadline.
    """


def get_project_user_attribute(number: int) -> str:
    """Gets the project user attribute.

    Parameters:
        number: The project user attribute number.

    Returns:
        The project user attribute.
    """


def get_project_user_attribute_name(number: int) -> str:
    """Gets the project user attribute name.

    Parameters:
        number: The project user attribute number.

    Returns:
        The project user attribute name.
    """


def get_project_latitude() -> float:
    """Gets the project latitude.

    Returns:
        The project latitude.
    """


def get_project_longitude() -> float:
    """Gets the project longitude.

    Returns:
        The project longitude.
    """


def get_project_postal_code() -> str:
    """Gets the project postal code.

    Returns:
        The project postal code.
    """


def get_project_address() -> str:
    """Gets the project address.

    Returns:
        The project address.
    """


def get_project_city() -> str:
    """Gets the project city.

    Returns:
        The project city.
    """


def get_project_country() -> str:
    """Gets the project country.

    Returns:
        The project country.
    """


def get_project_elevation() -> float:
    """Gets the project elevation.

    Returns:
        The project elevation.
    """


def get_project_description() -> str:
    """Gets the project description.

    Returns:
        A string containing the project description.
    """


def get_project_guid() -> str:
    """Gets the project GUID.

    Returns:
        The project GUID.
    """


def get_3d_userprofil_path() -> str:
    """Gets the 3D userprofil path.

    Returns:
        The 3D userprofil path.
    """


def get_plugin_path() -> str:
    """Gets the plugin path.

    Returns:
        A string containing the plugin path.
    """


def get_millimetre_from_imperial_string(value: str) -> float:
    """Converts an imperial string to millimetres.

    Parameters:
        value: The imperial string to convert.

    Returns:
        The value in millimetres.
    """


def get_imperial_string_from_millimetre(value: float) -> str:
    """Converts a value in millimetres to an imperial string.

    Parameters:
        value: The value in millimetres to convert.

    Returns:
        The value as an imperial string.
    """


def get_user_catalog_path() -> str:
    """Gets the user catalog path.

    Returns:
        A string containing the user catalog path.
    """


def get_3d_hwnd() -> int:
    """Gets the 3D HWND.

    Returns:
        The 3D HWND.
    """


def close_cadwork_document_saved() -> None:
    """close cadwork saved.
    """


def close_cadwork_document_unsaved() -> None:
    """close cadwork unsaved.
    """


def get_use_of_global_coordinates() -> bool:
    """Gets the use of global coordinates.

    Returns:
        True if global coordinates are used, false otherwise.
    """


def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """Sets the use of global coordinates.

    Parameters:
        use_of_global_coordinates: True to use global coordinates, false otherwise.
    """


def get_global_origin() -> point_3d:
    """Gets the global origin.

    Returns:
        The global origin.
    """


def set_global_origin(global_origin: point_3d) -> None:
    """Sets the global origin.

    Parameters:
        global_origin: The global origin.
    """


def create_snapshot() -> str:
    """Get snapshot from screen.

    Returns:
        The snapshot as a string.
    """


def get_3d_gui_upper_left_screen_coordinates() -> Tuple[int, int]:
    """Get the coordinates of the upper left corner of the 3D GUI.

    Returns:
        The coordinates of the upper left corner of the 3D GUI.
    """


def get_3d_main_window_geometry() -> 'window_geometry':
    """Get the geometry of 3d main window.

    Returns:
        The geometry of the 3D main window.
    """


def get_project_data_keys() -> List[str]:
    """Gets all keys for project data.

    Returns:
        The list of project data keys.
    """


def get_user_int_with_default_value(message: str, default_value: int) -> int:
    """Prompts the user for an integer with a default value.

    Parameters:
        message: The message to display.
        default_value: The default value.

    Returns:
        The user integer.
    """


def get_user_double_with_default_value(message: str, default_value: float) -> float:
    """Prompts the user for a double with a default value.

    Parameters:
        message: The message to display.
        default_value: The default value.

    Returns:
        The user double.
    """


def get_user_string_with_default_value(message: str, default_value: str) -> str:
    """Prompts the user for a string with a default value.

    Parameters:
        message: The message to display.
        default_value: The default value.

    Returns:
        The user string.
    """


def get_3d_version_name() -> str:
    """Gets the 3D version name.

    Returns:
        The 3D version name.
    """


def redirect_python_output_to_logger() -> None:
    """Redirects output from Python's print function to the cadwork logger.
       This function is used to redirect the output of the Python interpreter to the logger. 
       This is useful for debugging and logging purposes.
    """
