"""Application environment and user interaction.

The bridge between scripts and the surrounding cadwork application:
filesystem and version information, language and locale, user-facing
dialogs and prompts, status messages and progress indicators, GUID
generation, project metadata, and access to the host window itself.
General-purpose helpers that don't belong to any specific modelling
domain.
"""

from cadwork.api_types import ElementId
from cadwork.point_3d import point_3d
from cadwork.window_geometry import window_geometry
from cadwork.shortcut_key import shortcut_key
from cadwork.shortcut_key_modifier import shortcut_key_modifier
from cadwork.language import language
from cadwork.navigation_widget_subwindow_position import navigation_widget_subwindow_position

def get_3d_version() -> int:
    """Return the major version number of the running cadwork 3D.

    Returns:
        Major version number, for example 33.
    """

def get_3d_build() -> int:
    """Return the build number of the running cadwork 3D.

    Returns:
        Build number.
    """

def get_3d_file_path() -> str:
    """Return the full path of the currently open 3D file.

    Returns:
        File path as a string.
    """

def set_project_data(project_data_id: str, data: str) -> None:
    """Store a text value under an ID in the project data of the open document.

    The data is saved with the document. Use delete_project_data to remove an entry.

    Parameters:
        project_data_id: Key under which the data is stored.
        data: Text value to store.
    """

def print_error(message: str) -> None:
    """Show an error message in the command bar at the bottom of the 3D window.

    The command bar is cleared first and the message is shown as an error.

    Parameters:
        message: Error text to display.
    """

def get_language() -> str:
    """Return the language of cadwork 3D as a two-letter code.

    Returns:
        Code such as 'de', 'en', 'fr', 'it', 'es', 'cs', 'fi', 'ru', 'pl', 'ro', 'no', 'zh', 'pt',
        'et', 'ja', 'nl', 'sv'; empty string if undefined.
    """

def set_language(lang: language) -> None:
    """Set the user interface language of cadwork 3D and refresh the UI.

    Parameters:
        lang: Language to switch to, a member of cadwork.language.

    Examples:
        >>> import utility_controller as uc
        >>> import cadwork
        >>> uc.set_language(cadwork.language.german)
    """

def get_language_enum() -> language:
    """Return the language of cadwork 3D as a cadwork.language member.

    Returns:
        Active language; english if the language is undefined.
    """

def print_message(message: str, row: int, column: int) -> None:
    """Show a message in a cell of the command bar at the bottom of the 3D window.

    The addressed cell is cleared and replaced. The command bar has two rows and two columns; other
    row or column values address cell 1/1.

    Parameters:
        message: Text to display.
        row: Row of the cell, 1 or 2.
        column: Column of the cell, 1 or 2.

    Examples:
        >>> import utility_controller as uc
        >>> uc.print_message("Hello World!", 1, 1)
    """

def get_user_int(message: str) -> int:
    """Ask the user for an integer in the command bar and wait for the input.

    The script is blocked until the user answers. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    prompt is shown and 0 is returned.

    Parameters:
        message: Prompt text shown to the user.

    Returns:
        The entered integer; 0 if the input was cancelled or invalid.
    """

def get_user_double(message: str) -> float:
    """Ask the user for a decimal number in the command bar and wait for the input.

    The script is blocked until the user answers. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    prompt is shown and 0.0 is returned.

    Parameters:
        message: Prompt text shown to the user.

    Returns:
        The entered number; 0.0 if the input was cancelled or invalid.
    """

def get_user_bool(message: str, default_yes: bool) -> bool:
    """Ask the user a yes/no question in the command bar and wait for the answer.

    The script is blocked until the user answers. Cancelling returns False. In unattended runs
    (/PLUGIN or /RUNPROGRAM) no prompt is shown and False is returned.

    Parameters:
        message: Question text shown to the user.
        default_yes: If True the preselected answer is yes, otherwise no.

    Returns:
        True if the user answered yes, otherwise False.
    """

def get_user_string(message: str) -> str:
    """Ask the user for a text in the command bar and wait for the input.

    The script is blocked until the user answers. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    prompt is shown and an empty string is returned.

    Parameters:
        message: Prompt text shown to the user.

    Returns:
        The entered text; empty string if the input was cancelled.
    """

def set_project_name(project_name: str) -> None:
    """Set the project name in the project data of the open document.

    Parameters:
        project_name: The project name.
    """

def set_project_number(project_number: str) -> None:
    """Set the project number in the project data of the open document.

    Parameters:
        project_number: The project number.
    """

def set_project_part(project_part: str) -> None:
    """Set the project part in the project data of the open document.

    Parameters:
        project_part: The project part.
    """

def set_project_architect(project_architect: str) -> None:
    """Set the architect in the project data of the open document.

    Parameters:
        project_architect: The architect.
    """

def set_project_customer(project_customer: str) -> None:
    """Set the customer in the project data of the open document.

    Parameters:
        project_customer: The customer.
    """

def set_project_designer(project_designer: str) -> None:
    """Set the designer in the project data of the open document.

    Parameters:
        project_designer: The designer.
    """

def set_project_deadline(project_deadline: str) -> None:
    """Set the project deadline in the project data of the open document.

    The deadline is stored as free text.

    Parameters:
        project_deadline: The deadline as text.
    """

def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """Set the value of a project user attribute in the project data.

    Parameters:
        number: Index of the project user attribute.
        user_attribute: The value to store.
    """

def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Set the title of a project user attribute in the project data.

    Parameters:
        number: Index of the project user attribute.
        user_attribute_name: The title to store.
    """

def set_project_latitude(latitude: float) -> None:
    """Set the geographic latitude of the project.

    Parameters:
        latitude: Latitude of the project location.
    """

def set_project_longitude(longitude: float) -> None:
    """Set the geographic longitude of the project.

    Parameters:
        longitude: Longitude of the project location.
    """

def set_project_address(address: str) -> None:
    """Set the project address in the project data of the open document.

    Parameters:
        address: The project address.
    """

def set_project_postal_code(postal_code: str) -> None:
    """Set the project postal code in the project data of the open document.

    Parameters:
        postal_code: The project postal code.
    """

def set_project_city(city: str) -> None:
    """Set the project city in the project data of the open document.

    Parameters:
        city: The project city.
    """

def set_project_country(country: str) -> None:
    """Set the project country in the project data of the open document.

    Parameters:
        country: The project country.
    """

def get_user_file_from_dialog(name_filter: str) -> str:
    """Show an open-file dialog and return the selected existing file.

    The script is blocked until the dialog is closed. The dialog starts in the folder of the current
    3D file.

    Parameters:
        name_filter: File filter in Qt syntax, for example 'Text files (*.txt)'.

    Returns:
        Full path of the selected file; empty string if the dialog was cancelled.
    """

def get_client_number() -> str:
    """Return the cadwork client number of the licence.

    Returns:
        Client number as a string.
    """

def get_user_point() -> point_3d:
    """Let the user pick a point in the 3D view and return it.

    The script is blocked until the user picks a point; midpoints can be snapped. In unattended runs
    (/PLUGIN or /RUNPROGRAM) no prompt is shown.

    Returns:
        The picked point in model units (mm); point (0, 0, 0) if the pick was cancelled or the run
        is unattended.
    """

def disable_auto_display_refresh() -> None:
    """Stop the 3D view from refreshing automatically after each operation.

    Speeds up scripts that make many changes. Always pair with enable_auto_display_refresh.
    """

def enable_auto_display_refresh() -> None:
    """Resume automatic refresh of the 3D view after disable_auto_display_refresh.

    Elements created while refresh was disabled must be recreated (for example with
    element_controller.recreate_elements) to be displayed correctly.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc
        >>> import element_controller as ec
        >>> uc.disable_auto_display_refresh()
        >>> # Perform operations that require disabled display refresh
        >>> your_list_of_elements: list[int] = []
        >>> uc.enable_auto_display_refresh()
        >>> ec.recreate_elements(your_list_of_elements)
    """

def create_new_guid() -> str:
    """Create a new random GUID.

    Returns:
        GUID string in registry format including braces, for example
        '{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}'.
    """

def print_to_console(message: str) -> None:
    """Write a message to the cadwork debug console log.

    The message is logged at info level.

    Parameters:
        message: Text to log.
    """

def export_screen_to_image(file_path: str, factor: int) -> None:
    """Save the current 3D view as an image file.

    The image has the size of the 3D view, enlarged by factor, with the current background colour.
    The format is derived from the file extension.

    Parameters:
        file_path: Target file path including extension.
        factor: Enlargement factor applied to the view size, 1 for original size.
    """

def get_new_user_file_from_dialog(name_filter: str) -> str:
    """Show a save-file dialog and return the chosen path.

    The script is blocked until the dialog is closed. The file is not created. The dialog starts in
    the user home folder.

    Parameters:
        name_filter: File filter in Qt syntax, for example 'Text files (*.txt)'.

    Returns:
        Full path chosen by the user; empty string if the dialog was cancelled.
    """

def api_autostart(api_name: str, option: int) -> int:
    """Enable or disable autostart of a Python API module for the current user.

    Reads and writes the user-profile alias and module configuration files, creating them if
    missing. Takes effect at the next start of cadwork 3D. Prefer enable_autostart,
    disable_autostart and check_autostart.

    Parameters:
        api_name: Name of the API to manage; an empty name is an error.
        option: 1 enables autostart, 0 disables it. The value is unsigned, so negative values
            are rejected with a TypeError; use check_autostart to query.

    Examples:
        >>> api_autostart("my_api", 1)  # Enable autostart
        >>> api_autostart("my_api", 0)  # Disable autostart
        >>> api_autostart("my_api", -1)  # Check current autostart state

    Returns:
        The option value on success; 4294967295 on error.
    """

def enable_autostart(api_name: str) -> None:
    """Enable autostart of a Python API module for the current user.

    Writes the user-profile configuration files; takes effect at the next start of cadwork 3D.
    Errors are not reported.

    Parameters:
        api_name: Name of the API to enable.
    """

def disable_autostart(api_name: str) -> None:
    """Disable autostart of a Python API module for the current user.

    Writes the user-profile configuration files; takes effect at the next start of cadwork 3D.
    Errors are not reported.

    Parameters:
        api_name: Name of the API to disable.
    """

def check_autostart(api_name: str) -> bool:
    """Check whether autostart is enabled for a Python API module.

    An error, for example an empty name, is also reported as True.

    Parameters:
        api_name: Name of the API to check.

    Returns:
        True if autostart is enabled or an error occurred, False otherwise.
    """

def delete_project_data(element_id: str) -> None:
    """Delete an entry from the project data of the open document.

    Parameters:
        element_id: ID of the project data entry, as used with set_project_data.
    """

def run_external_program(name: str) -> bool:
    """Run an external program from the cadwork API folder.

    The name is appended to the API folder path of cadwork 3D.

    Parameters:
        name: File name of the program, relative to the API folder.

    Returns:
        True if the program was started, False otherwise.
    """

def save_3d_file_silently() -> None:
    """Save the open 3D file without showing a dialog.

    Waits until saving has finished before returning.
    """

def get_licence_first_part() -> str:
    """Return the first part of the licence (dongle) ID.

    Returns:
        First part of the licence ID as a string.
    """

def get_licence_second_part() -> str:
    """Return the second part of the licence (dongle) ID.

    Returns:
        Second part of the licence ID as a string.
    """

def show_progress_bar() -> None:
    """Show the progress bar in the command bar, reset to its minimum.

    Update it with update_progress_bar and remove it with hide_progress_bar.
    """

def update_progress_bar(value: int) -> None:
    """Set the value of the progress bar in the command bar.

    Show the bar first with show_progress_bar.

    Parameters:
        value: Progress value, 0 to 100.
    """

def hide_progress_bar() -> None:
    """Hide the progress bar in the command bar."""

def get_user_color(initial_color: int) -> int:
    """Let the user choose a colour from the colour palette dialog.

    The script is blocked until the dialog is closed. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    dialog is shown and initial_color is returned.

    Parameters:
        initial_color: Colour number preselected in the dialog.

    Returns:
        The chosen colour number.
    """

def get_3d_linear_units() -> str:
    """Get the abbreviation of the document's linear unit.

    Returns:
        One of mm, cm, m, in or ft; empty string if the unit is none of these.
    """

def get_3d_linear_display_units() -> str:
    """Get the abbreviation of the linear unit used for display.

    This is the display unit setting, which can differ from the document unit.

    Returns:
        One of mm, cm, m, in or ft; empty string if the unit is none of these.
    """

def get_3d_angular_units() -> str:
    """Get the abbreviation of the document's angular unit.

    Returns:
        One of deg, gon, rad or pct; empty string if the unit is none of these.
    """

def get_3d_angular_display_units() -> str:
    """Get the abbreviation of the angular unit used for display.

    This is the display unit setting, which can differ from the document unit.

    Returns:
        One of deg, gon, rad or pct; empty string if the unit is none of these.
    """

def get_3d_build_date() -> str:
    """Get the build date of the running cadwork 3D version.

    Returns:
        The build date as a string.
    """

def set_project_elevation(elevation: float) -> None:
    """Set the project elevation in the project data.

    Updates the project data of the open document; the value is stored as the project height.

    Parameters:
        elevation: New project elevation.
    """

def clear_errors() -> None:
    """Clear the list of errors collected by the API."""

def push_check_and_query_data() -> None:
    """Save the current confirmation-dialog settings on a stack.

    Use together with pop_check_and_query_data to restore the settings after temporarily suppressing
    dialogs.
    """

def pop_check_and_query_data() -> None:
    """Restore the confirmation-dialog settings saved by the last push.

    Does nothing if nothing was pushed.
    """

def change_check_and_query_data_to_no_queries() -> None:
    """Suppress confirmation dialogs by answering them automatically.

    Dialogs set to ask with default Yes are switched to always yes, those with default No to never.
    Changes the document settings until reverted, for example with pop_check_and_query_data.
    """

def change_check_and_query_data_to_queries() -> None:
    """Re-enable confirmation dialogs that were set to answer automatically.

    Dialogs set to always yes are switched back to ask with default Yes, those set to never back to
    ask with default No.
    """

def is_direct_info_enabled() -> bool:
    """Check whether the Direct Info tooltip is enabled.

    Returns:
        True if Direct Info (element tooltip on hover) is enabled, False otherwise.
    """

def enable_direct_info() -> None:
    """Enable the Direct Info tooltip for elements."""

def disable_direct_info() -> None:
    """Disable the Direct Info tooltip for elements."""

def load_attribute_display_settings(file_path: str) -> None:
    """Load attribute display settings from a settings file and apply them.

    Overwrites the current attribute display settings of all supported display types and formats
    with those found in the file.

    Parameters:
        file_path: Path to the settings file.
    """

def set_project_description(description: str) -> None:
    """Set the project description in the project data.

    Parameters:
        description: New project description.
    """

def start_project_data_dialog() -> None:
    """Open the project data dialog.

    Shows the dialog to the user.
    """

def init_LxSDK() -> None:
    """Initialize the LxSDK of the open document."""

def load_element_attribute_display_settings(file_path: str, elements: list[ElementId]) -> None:
    """Load attribute display settings from a file for the given elements.

    Same as load_attribute_display_settings but scoped to the given elements; IDs that do not exist
    are skipped. Also applies the file's use-global flag to each loaded setting.

    Parameters:
        file_path: Path to the settings file.
        elements: List of element IDs the settings apply to.
    """

def get_global_x_offset() -> float:
    """Get the X coordinate of the document's global origin.

    Returns:
        Global X offset in model units (mm).
    """

def set_global_x_offset(offset: float) -> None:
    """Set the X coordinate of the document's global origin.

    The other two coordinates are unchanged.

    Parameters:
        offset: New global X offset in model units (mm).
    """

def get_global_y_offset() -> float:
    """Get the Y coordinate of the document's global origin.

    Returns:
        Global Y offset in model units (mm).
    """

def set_global_y_offset(offset: float) -> None:
    """Set the Y coordinate of the document's global origin.

    The other two coordinates are unchanged.

    Parameters:
        offset: New global Y offset in model units (mm).
    """

def get_global_z_offset() -> float:
    """Get the Z coordinate of the document's global origin.

    Returns:
        Global Z offset in model units (mm).
    """

def set_global_z_offset(offset: float) -> None:
    """Set the Z coordinate of the document's global origin.

    The other two coordinates are unchanged.

    Parameters:
        offset: New global Z offset in model units (mm).
    """

def show_north_arrow() -> None:
    """Show the north arrow (deprecated, does nothing).

    Deprecated: logs a warning and has no effect. Use the navigation widget functions instead.
    """

def hide_north_arrow() -> None:
    """Hide the north arrow (deprecated, does nothing).

    Deprecated: logs a warning and has no effect. Use the navigation widget functions instead.
    """

def is_north_arrow_visible() -> bool:
    """Check whether the north arrow is visible (deprecated).

    Deprecated: logs a warning and always returns False. Use the navigation widget functions
    instead.

    Returns:
        Always False.
    """

def get_north_angle() -> float:
    """Get the north direction angle stored in the program options.

    Returns:
        North angle in degrees.
    """

def set_north_angle(north_angle: float) -> None:
    """Set the north direction angle in the program options.

    Parameters:
        north_angle: North angle in degrees.
    """

def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Show an open-file dialog starting in a folder and return the chosen file.

    Blocks the script until the user closes the dialog.

    Parameters:
        name_filter: File filter in Qt dialog format, for example Text files (*.txt).
        path: Folder in which the dialog starts.

    Returns:
        Full path of the selected existing file; empty string if the dialog is cancelled.
    """

def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Show a save-file dialog starting in a folder and return the chosen file name.

    Blocks the script until the user closes the dialog. The file does not need to exist and is not
    created.

    Parameters:
        name_filter: File filter in Qt dialog format, for example Text files (*.txt).
        path: Folder in which the dialog starts.

    Returns:
        Full path of the chosen file; empty string if the dialog is cancelled.
    """

def enable_update_variant() -> None:
    """Enable automatic updating of variants.

    Reverses disable_update_variant.
    """

def disable_update_variant() -> None:
    """Disable automatic updating of variants.

    Call enable_update_variant to turn it on again.
    """

def get_user_points() -> list[point_3d]:
    """Let the user pick any number of points in the 3D view.

    Blocks the script while the user picks points. In unattended plugin runs (/PLUGIN or /RUNPROGRAM
    mode) no interaction takes place and an empty list is returned.

    Returns:
        List of picked points in picking order; empty list if nothing was picked or the interaction
        is skipped.
    """

def get_user_points_with_count(count: int) -> list[point_3d]:
    """Let the user pick a given number of points in the 3D view.

    Blocks the script while the user picks points. Returns an empty list for count 0 and in
    unattended plugin runs (/PLUGIN or /RUNPROGRAM mode).

    Parameters:
        count: Maximum number of points to pick; 1 asks for a single point.

    Returns:
        List of picked points in picking order; empty list if count is 0, nothing was picked or the
        interaction is skipped.
    """

def get_user_path_from_dialog() -> str:
    """Show a folder-selection dialog and return the chosen folder.

    Blocks the script until the user closes the dialog. In unattended plugin runs (/PLUGIN or
    /RUNPROGRAM mode) no dialog is shown.

    Returns:
        Full path of the selected folder; empty string if cancelled or skipped.
    """

def get_user_path_from_dialog_in_path(path: str) -> str:
    """Show a folder-selection dialog starting in a folder and return the chosen folder.

    Blocks the script until the user closes the dialog. In unattended plugin runs (/PLUGIN or
    /RUNPROGRAM mode) no dialog is shown.

    Parameters:
        path: Folder in which the dialog starts.

    Returns:
        Full path of the selected folder; empty string if cancelled or skipped.
    """

def execute_shortcut(shortcut_key_modifier: shortcut_key_modifier, shortcut_key: shortcut_key) -> None:
    """Trigger the main window action bound to a keyboard shortcut.

    Only function keys F1 to F12 are supported, optionally combined with one modifier. Every action
    with a matching shortcut is triggered; nothing happens if none match.

    Parameters:
        shortcut_key_modifier: Modifier key: none, Shift, Control or Alt.
        shortcut_key: Function key F1 to F12.
    """

def run_external_program_from_custom_directory(file_path: str) -> bool:
    """Run a 3D external program from a file path.

    The program is launched through the external program manager of the open document.

    Parameters:
        file_path: Path of the external program file.

    Returns:
        True if the program was started, False on error.
    """

def get_3d_file_name() -> str:
    """Get the file name of the open 3D document.

    Returns:
        File name without folder, including extension.
    """

def get_project_data(element_id: str) -> str:
    """Get a project data value by its ID.

    Parameters:
        element_id: ID (name) of the project data entry. Not an element ID.

    Returns:
        The stored value; empty string if the ID does not exist.
    """

def get_project_name() -> str:
    """Get the project name from the project data.

    Returns:
        The project name as text; empty string if not set.
    """

def get_project_part() -> str:
    """Get the project part from the project data.

    Returns:
        The project part as text; empty string if not set.
    """

def get_project_architect() -> str:
    """Get the project architect from the project data.

    Returns:
        The project architect as text; empty string if not set.
    """

def get_project_number() -> str:
    """Get the project number from the project data.

    Returns:
        The project number as text; empty string if not set.
    """

def get_project_customer() -> str:
    """Get the project customer from the project data.

    Returns:
        The project customer as text; empty string if not set.
    """

def get_project_designer() -> str:
    """Get the project designer from the project data.

    Returns:
        The project designer as text; empty string if not set.
    """

def get_project_deadline() -> str:
    """Get the project deadline from the project data.

    Returns:
        The project deadline as text; empty string if not set.
    """

def get_project_user_attribute(number: int) -> str:
    """Get a project user attribute value by its number.

    Parameters:
        number: Number of the project user attribute.

    Returns:
        The value of the attribute; empty string if not set.
    """

def get_project_user_attribute_name(number: int) -> str:
    """Return the name of a project user attribute slot.

    The name is the title defined in the project data settings, not an attribute value.

    Parameters:
        number: Number of the project user attribute slot.

    Returns:
        The slot name, or an empty string if none is set.
    """

def get_project_latitude() -> float:
    """Return the project latitude from the project data.

    Returns:
        The latitude as a float.
    """

def get_project_longitude() -> float:
    """Return the project longitude from the project data.

    Returns:
        The longitude as a float.
    """

def get_project_postal_code() -> str:
    """Return the project postal code from the project data.

    Returns:
        The postal code, or an empty string if not set.
    """

def get_project_address() -> str:
    """Return the project address from the project data.

    Returns:
        The address, or an empty string if not set.
    """

def get_project_city() -> str:
    """Return the project city from the project data.

    Returns:
        The city, or an empty string if not set.
    """

def get_project_country() -> str:
    """Return the project country from the project data.

    Returns:
        The country, or an empty string if not set.
    """

def get_project_elevation() -> float:
    """Return the project elevation (height) from the project data.

    Returns:
        The elevation as a float.
    """

def get_project_description() -> str:
    """Return the project description from the project data.

    Returns:
        The description, or an empty string if not set.
    """

def get_project_guid() -> str:
    """Return the GUID of the current project.

    Returns:
        The project GUID as a string.
    """

def get_3d_userprofil_path() -> str:
    """Return the path of the cadwork user profile directory.

    Returns:
        The directory path as a string.
    """

def get_plugin_path() -> str:
    """Return the path of the cadwork plugin directory.

    Returns:
        The directory path as a string.
    """

def get_millimetre_from_imperial_string(value: str) -> float:
    """Convert an imperial length string to millimetres.

    Parsing is done by the cadwork unit converter.

    Parameters:
        value: Imperial length as text, for example a feet-and-inches or inches string.

    Returns:
        The length in millimetres as a float.
    """

def get_imperial_string_from_millimetre(value: float) -> str:
    """Convert a length in millimetres to an imperial length string.

    Parameters:
        value: Length in millimetres.

    Returns:
        The length as an imperial text string.
    """

def get_user_catalog_path() -> str:
    """Return the path of the cadwork user catalog directory.

    Returns:
        The directory path as a string.
    """

def get_3d_hwnd() -> int:
    """Return the native window handle of the cadwork 3D main window.

    Returns:
        The Windows window handle as an integer, or 0 if there is no main window.
    """

def close_cadwork_document_saved() -> None:
    """Save the document silently, then close cadwork.

    Terminates the cadwork application, so the script ends with it. Ignored (with a log warning)
    when cadwork runs unattended via a plugin or program start parameter, because cadwork closes
    itself after the script.
    """

def close_cadwork_document_unsaved() -> None:
    """Close cadwork without saving the document.

    Unsaved changes are lost and the script ends with the application. Ignored (with a log warning)
    when cadwork runs unattended via a plugin or program start parameter, because cadwork closes
    itself after the script.
    """

def get_use_of_global_coordinates() -> bool:
    """Return whether global coordinates are used.

    This is a cadwork application option.

    Returns:
        True if global coordinates are enabled, False otherwise.
    """

def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """Enable or disable the use of global coordinates.

    This is a cadwork application option; it does not change the global origin.

    Parameters:
        use_of_global_coordinates: True to use global coordinates, False to use local ones.
    """

def get_global_origin() -> point_3d:
    """Return the global origin of the document.

    Returns:
        The global origin as a point_3d in model units (mm).
    """

def set_global_origin(global_origin: point_3d) -> None:
    """Set the global origin of the document.

    Parameters:
        global_origin: New global origin as a point_3d in model units (mm).
    """

def create_snapshot() -> str:
    """Capture the 3D view as a Base64-encoded image string.

    Captures the current 3D view with a white background and returns the PNG data encoded as Base64
    text. Decode it with base64 to get the image bytes.

    Returns:
        The Base64-encoded PNG image.
    """

def get_3d_gui_upper_left_screen_coordinates() -> tuple[int, int]:
    """Return the screen position of the upper left corner of the 3D main window.

    Returns:
        A tuple (x, y) in screen pixels.
    """

def get_3d_main_window_geometry() -> 'window_geometry':
    """Return the screen geometry of the cadwork 3D main window.

    Returns:
        A window_geometry with the four corner points bottom_left, bottom_right, top_left and
        top_right, each with x and y in screen pixels.
    """

def get_project_data_keys() -> list[str]:
    """Return the keys of the project data entries stored in the document.

    Keys reserved for internal use by cadwork are left out.

    Returns:
        List of project data keys, empty if there are none.
    """

def get_user_int_with_default_value(message: str, default_value: int) -> int:
    """Ask the user to enter an integer in the command bar, with a default.

    Blocks the script until the user answers. Returns the default value without asking when cadwork
    runs unattended via a plugin or program start parameter.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Value pre-filled in the input field, also returned in unattended runs.

    Returns:
        The value entered by the user. 0 (and an error message in cadwork) if the user cancels the
        input.
    """

def get_user_double_with_default_value(message: str, default_value: float) -> float:
    """Ask the user to enter a number in the command bar, with a default.

    Blocks the script until the user answers. Returns the default value without asking when cadwork
    runs unattended via a plugin or program start parameter.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Value pre-filled in the input field, also returned in unattended runs.

    Returns:
        The value entered by the user. 0.0 (and an error message in cadwork) if the user cancels the
        input.
    """

def get_user_string_with_default_value(message: str, default_value: str) -> str:
    """Ask the user to enter text in the command bar, with a default.

    Blocks the script until the user answers. Returns the default value without asking when cadwork
    runs unattended via a plugin or program start parameter.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Text pre-filled in the input field, also returned in unattended runs.

    Returns:
        The text entered by the user. Empty string (and an error message in cadwork) if the user
        cancels the input.
    """

def get_3d_version_name() -> str:
    """Return the cadwork 3D version name.

    Returns:
        The version name as a string.
    """

def redirect_python_output_to_logger() -> None:
    """Send Python print output and errors to the cadwork logger.

    Replaces sys.stdout and sys.stderr with logger objects and sets the cadwork API log level to
    Info. Safe to call more than once.
    """

def set_navigation_widget_enabled(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the navigation widget in one corner of the 3D view.

    The widget is recreated and the view updated.

    Parameters:
        position: Navigation widget corner. None is rejected: nothing changes and an error is
            logged.
        enabled: True to show the widget, False to hide it.
    """

def set_navigation_widget_size(position: navigation_widget_subwindow_position, size: int) -> None:
    """Set the size of the navigation widget in one corner of the 3D view.

    The widget is recreated and the view updated.

    Parameters:
        position: Navigation widget corner. None is rejected: nothing changes and an error is
            logged.
        size: Widget size. The UI allows 80 to 200 inclusive; the code does not clamp other values.
    """

def set_navigation_widget_north_arrow(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the north arrow of a navigation widget.

    The widget is recreated and the view updated.

    Parameters:
        position: Navigation widget corner. None is rejected: nothing changes and an error is
            logged.
        enabled: True to show the north arrow, False to hide it.
    """

def set_navigation_widget_axis(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the axis triad of a navigation widget.

    The widget is recreated and the view updated.

    Parameters:
        position: Navigation widget corner. None is rejected: nothing changes and an error is
            logged.
        enabled: True to show the axis triad, False to hide it.
    """

def set_navigation_widget_cube(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the view cube of a navigation widget.

    The widget is recreated and the view updated.

    Parameters:
        position: Navigation widget corner. None is rejected: nothing changes and an error is
            logged.
        enabled: True to show the view cube, False to hide it.
    """

def get_user_edge() -> list[point_3d]:
    """Ask the user to pick an edge or two points in the 3D view.

    Blocks until the user picks or aborts. Returns an empty list without asking in unattended
    runs (/PLUGIN or /RUNPROGRAM).

    Returns:
        List of two point_3d, the start and end of the picked edge. Empty list if the user
        aborted or no valid edge was picked.
    """
