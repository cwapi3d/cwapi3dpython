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

    Use it to branch on features that only exist in newer releases. Only the major number is
    returned; use `utility_controller.get_3d_build()` for the build and
    `utility_controller.get_3d_version_name()` for the readable name.

    Examples:
        >>> import utility_controller as uc

        >>> version = uc.get_3d_version()
        >>> if version < 33:
        ...     uc.print_error('This script needs cadwork 33 or newer.')

    Returns:
        Major version number, for example 33.
    """

def get_3d_build() -> int:
    """Return the build number of the running cadwork 3D.

    Identifies the exact build within a major version. Combine it with
    `utility_controller.get_3d_version()` to log or compare versions.

    Examples:
        >>> import utility_controller as uc

        >>> print(uc.get_3d_version(), uc.get_3d_build())

    Returns:
        Build number.
    """

def get_3d_file_path() -> str:
    """Return the full path of the currently open 3D file.

    Use it to place output files next to the model. For only the file name use
    `utility_controller.get_3d_file_name()`.

    Examples:
        >>> import utility_controller as uc

        >>> file_path = uc.get_3d_file_path()
        >>> print(file_path)

    Returns:
        File path as a string, including the file name.
    """

def set_project_data(project_data_id: str, data: str) -> None:
    """Store a text value under an ID in the project data of the open document.

    Project data is a free key/value store saved with the document, useful for script settings that
    must travel with the model. An existing entry with the same ID is replaced. Read it back with
    `utility_controller.get_project_data()` and remove it with
    `utility_controller.delete_project_data()`.

    Parameters:
        project_data_id: Key under which the data is stored. Choose a unique, script-specific ID.
        data: Text value to store. Convert numbers to text yourself.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_data('my_script.last_run', '2025-01-31')
        >>> print(uc.get_project_data('my_script.last_run'))
    """

def print_error(message: str) -> None:
    """Show an error message in the command bar at the bottom of the 3D window.

    The whole command bar is cleared first, so any other cell contents are lost, and the text is
    shown as an error. The script is not interrupted and no exception is raised; return or raise
    yourself if the script must stop. For neutral messages use `utility_controller.print_message()`.

    Parameters:
        message: Error text to display.

    Examples:
        >>> import utility_controller as uc

        >>> if not uc.get_user_bool('Continue?', True):
        ...     uc.print_error('Aborted by the user.')
    """

def get_language() -> str:
    """Return the language of cadwork 3D as a two-letter code.

    The result reflects the user interface language currently selected in cadwork. Use
    `utility_controller.get_language_enum()` for the same information as a `cadwork.language` member
    and `utility_controller.set_language()` to change it.

    Examples:
        >>> import utility_controller as uc

        >>> if uc.get_language() == 'de':
        ...     uc.print_message('Hallo Welt', 1, 1)
        ... else:
        ...     uc.print_message('Hello world', 1, 1)

    Returns:
        Code such as 'de', 'en', 'fr', 'it', 'es', 'cs', 'fi', 'ru', 'pl', 'ro', 'no', 'zh', 'pt',
        'et', 'ja', 'nl', 'sv'; empty string if the language is undefined.
    """

def set_language(lang: language) -> None:
    """Set the user interface language of cadwork 3D and refresh the UI.

    Changes the language of the running application, not only of the script. Read the current
    language with `utility_controller.get_language_enum()`.

    Parameters:
        lang: Language to switch to, a member of `cadwork.language`, for example
            `cadwork.language.german`.

    Examples:
        >>> import utility_controller as uc
        >>> import cadwork
        >>> uc.set_language(cadwork.language.german)
    """

def get_language_enum() -> language:
    """Return the language of cadwork 3D as a cadwork.language member.

    Typed alternative to `utility_controller.get_language()`. Pass the result back to
    `utility_controller.set_language()` to restore a language after a temporary switch.

    Examples:
        >>> import utility_controller as uc
        >>> import cadwork

        >>> previous = uc.get_language_enum()
        >>> uc.set_language(cadwork.language.german)
        >>> uc.set_language(previous)

    Returns:
        Active language as a `cadwork.language` member; `cadwork.language.english` if the language
        is undefined.
    """

def print_message(message: str, row: int, column: int) -> None:
    """Show a message in a cell of the command bar at the bottom of the 3D window.

    The command bar has two rows and two columns. Only the addressed cell is cleared and replaced.
    Row/column combinations other than 1 or 2 address cell 1/1. To show an error use
    `utility_controller.print_error()`.

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
    prompt is shown, a warning is logged and 0 is returned. Because 0 is also a valid answer, the
    failure value cannot be told apart from an entered 0.

    Parameters:
        message: Prompt text shown to the user.

    Examples:
        >>> import utility_controller as uc

        >>> count = uc.get_user_int('Number of copies')
        >>> if count > 0:
        ...     print(f'Creating {count} copies')

    Returns:
        The entered integer; 0 if the input was cancelled or the run is unattended.
    """

def get_user_double(message: str) -> float:
    """Ask the user for a decimal number in the command bar and wait for the input.

    The script is blocked until the user answers. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    prompt is shown, a warning is logged and 0.0 is returned. The returned value is not converted;
    if you treat it as a length, it is up to you to use model units (mm).

    Parameters:
        message: Prompt text shown to the user.

    Examples:
        >>> import utility_controller as uc

        >>> spacing = uc.get_user_double('Spacing in mm')
        >>> if spacing > 0:
        ...     print(f'Using spacing {spacing}')

    Returns:
        The entered number; 0.0 if the input was cancelled or the run is unattended.
    """

def get_user_bool(message: str, default_yes: bool) -> bool:
    """Ask the user a yes/no question in the command bar and wait for the answer.

    The script is blocked until the user answers. Pressing Enter accepts the preselected answer.
    Cancelling returns False. In unattended runs (/PLUGIN or /RUNPROGRAM) no prompt is shown and
    False is returned, even if default_yes is True.

    Parameters:
        message: Question text shown to the user.
        default_yes: If True the preselected answer is yes, otherwise no.

    Examples:
        >>> import utility_controller as uc

        >>> if uc.get_user_bool('Delete the old elements?', False):
        ...     print('Deleting')
        ... else:
        ...     print('Keeping')

    Returns:
        True if the user answered yes, otherwise False (including cancel).
    """

def get_user_string(message: str) -> str:
    """Ask the user for a text in the command bar and wait for the input.

    The script is blocked until the user answers. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    prompt is shown, a warning is logged and an empty string is returned. For a prompt with a preset
    answer use `utility_controller.get_user_string_with_default_value()`.

    Parameters:
        message: Prompt text shown to the user.

    Examples:
        >>> import utility_controller as uc

        >>> name = uc.get_user_string('Name of the group')
        >>> if name:
        ...     print(f'Group name: {name}')

    Returns:
        The entered text; empty string if the input was cancelled or the run is unattended.
    """

def set_project_name(project_name: str) -> None:
    """Set the project name in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_name()`.

    Parameters:
        project_name: The project name as free text.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_name('Villa Meier')
        >>> print(uc.get_project_name())
    """

def set_project_number(project_number: str) -> None:
    """Set the project number in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_number()`.

    Parameters:
        project_number: The project number as free text, for example '2025-014'.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_number('2025-014')
        >>> print(uc.get_project_number())
    """

def set_project_part(project_part: str) -> None:
    """Set the project part in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_part()`.

    Parameters:
        project_part: The project part (building section) as free text.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_part('Roof')
        >>> print(uc.get_project_part())
    """

def set_project_architect(project_architect: str) -> None:
    """Set the architect in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_architect()`.

    Parameters:
        project_architect: Name of the architect.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_architect('Muster Architekten')
        >>> print(uc.get_project_architect())
    """

def set_project_customer(project_customer: str) -> None:
    """Set the customer in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_customer()`.

    Parameters:
        project_customer: Name of the customer.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_customer('Meier AG')
        >>> print(uc.get_project_customer())
    """

def set_project_designer(project_designer: str) -> None:
    """Set the designer in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_designer()`.

    Parameters:
        project_designer: Name of the designer.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_designer('J. Smith')
        >>> print(uc.get_project_designer())
    """

def set_project_deadline(project_deadline: str) -> None:
    """Set the project deadline in the project data of the open document.

    The deadline is stored as free text; no date format is checked or converted. Read it back with
    `utility_controller.get_project_deadline()`.

    Parameters:
        project_deadline: The deadline as text, for example '2025-12-01'.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_deadline('2025-12-01')
        >>> print(uc.get_project_deadline())
    """

def set_project_user_attribute(number: int, user_attribute: str) -> None:
    """Set the value of a project user attribute in the project data.

    Project user attributes are numbered free-text fields of the project data dialog. This sets the
    value; the title shown for the field is set with
    `utility_controller.set_project_user_attribute_name()`. Read the value back with
    `utility_controller.get_project_user_attribute()`.

    Parameters:
        number: Number of the project user attribute field, as shown in the project data dialog.
        user_attribute: The value to store as text.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_user_attribute_name(1, 'Site manager')
        >>> uc.set_project_user_attribute(1, 'A. Keller')
        >>> print(uc.get_project_user_attribute(1))
    """

def set_project_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Set the title of a project user attribute in the project data.

    The title is the label of the field in the project data dialog, not its value. Set the value
    with `utility_controller.set_project_user_attribute()`. Read the title back with
    `utility_controller.get_project_user_attribute_name()`.

    Parameters:
        number: Number of the project user attribute field, as shown in the project data dialog.
        user_attribute_name: The title to store.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_user_attribute_name(1, 'Site manager')
        >>> print(uc.get_project_user_attribute_name(1))
    """

def set_project_latitude(latitude: float) -> None:
    """Set the geographic latitude of the project.

    Stored in the project data together with the longitude, which can be used to locate the project.
    Set the longitude with `utility_controller.set_project_longitude()`. Read it back with
    `utility_controller.get_project_latitude()`.

    Parameters:
        latitude: Latitude of the project location as a decimal number.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_latitude(47.3769)
        >>> uc.set_project_longitude(8.5417)
        >>> print(uc.get_project_latitude())
    """

def set_project_longitude(longitude: float) -> None:
    """Set the geographic longitude of the project.

    Stored in the project data together with the latitude. Set the latitude with
    `utility_controller.set_project_latitude()`. Read it back with
    `utility_controller.get_project_longitude()`.

    Parameters:
        longitude: Longitude of the project location as a decimal number.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_longitude(8.5417)
        >>> print(uc.get_project_longitude())
    """

def set_project_address(address: str) -> None:
    """Set the project address in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_address()`.

    Parameters:
        address: Street address as free text.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_address('Bahnhofstrasse 1')
        >>> print(uc.get_project_address())
    """

def set_project_postal_code(postal_code: str) -> None:
    """Set the project postal code in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_postal_code()`.

    Parameters:
        postal_code: Postal code as text, so leading zeros are kept.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_postal_code('8001')
        >>> print(uc.get_project_postal_code())
    """

def set_project_city(city: str) -> None:
    """Set the project city in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_city()`.

    Parameters:
        city: City name.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_city('Zurich')
        >>> print(uc.get_project_city())
    """

def set_project_country(country: str) -> None:
    """Set the project country in the project data of the open document.

    The value is stored in the project data (the project data dialog of cadwork) and saved with the
    document. An existing value is overwritten, an empty string clears it. Read it back with
    `utility_controller.get_project_country()`.

    Parameters:
        country: Country name as free text.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_country('Switzerland')
        >>> print(uc.get_project_country())
    """

def get_user_file_from_dialog(name_filter: str) -> str:
    """Show an open-file dialog and return the selected existing file.

    The script is blocked until the dialog is closed. The dialog starts in the folder of the current
    3D file and only accepts an existing file. To start in another folder use
    `utility_controller.get_user_file_from_dialog_in_path()`; to choose a new file name use
    `utility_controller.get_new_user_file_from_dialog()`.

    Parameters:
        name_filter: File filter in Qt syntax, for example 'Text files (*.txt)' or 'Images (*.png
            *.jpg)'.

    Examples:
        >>> import utility_controller as uc

        >>> path = uc.get_user_file_from_dialog('Text files (*.txt)')
        >>> if path:
        ...     with open(path) as f:
        ...         print(f.readline())

    Returns:
        Full path of the selected file; empty string if the dialog was cancelled.
    """

def get_client_number() -> str:
    """Return the cadwork client number of the licence.

    Identifies the licence holder. See also `utility_controller.get_licence_first_part()` and
    `utility_controller.get_licence_second_part()` for the dongle ID.

    Examples:
        >>> import utility_controller as uc

        >>> print(uc.get_client_number())

    Returns:
        Client number as a string.
    """

def get_user_point() -> point_3d:
    """Let the user pick a point in the 3D view and return it.

    The script is blocked until the user picks a point; midpoints of edges can be snapped,
    intersections are not offered. In unattended runs (/PLUGIN or /RUNPROGRAM) no prompt is shown.
    Cancelling cannot be told apart from picking the origin. For several points use
    `utility_controller.get_user_points()`.

    Examples:
        >>> import utility_controller as uc

        >>> point = uc.get_user_point()
        >>> print(point.x, point.y, point.z)

    Returns:
        The picked point in model units (mm); point (0, 0, 0) if the pick was cancelled or the run
        is unattended.
    """

def disable_auto_display_refresh() -> None:
    """Stop the 3D view from refreshing automatically after each operation.

    Speeds up scripts that make many changes. Always pair it with
    `utility_controller.enable_auto_display_refresh()`, also when the script fails, for example in a
    try/finally block.

    Examples:
        >>> import element_controller as ec
        >>> import utility_controller as uc

        >>> uc.disable_auto_display_refresh()
        >>> try:
        ...     element_ids = ec.get_active_identifiable_element_ids()
        ...     print(len(element_ids))
        ... finally:
        ...     uc.enable_auto_display_refresh()
    """

def enable_auto_display_refresh() -> None:
    """Resume automatic refresh of the 3D view after disable_auto_display_refresh.

    Call it after `utility_controller.disable_auto_display_refresh()`. Elements created while
    refresh was disabled must be recreated (for example with
    `element_controller.recreate_elements()`) to be displayed correctly.

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

    Every call returns a new unique value, useful as a stable ID for objects you create, for example
    as project data keys.

    Examples:
        >>> import utility_controller as uc

        >>> guid = uc.create_new_guid()
        >>> print(guid)

    Returns:
        GUID string in registry format including braces, for example
        '{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}'.
    """

def print_to_console(message: str) -> None:
    """Write a message to the cadwork debug console log.

    The message is logged at info level in the cadwork API log, not shown in the command bar. For
    user-visible messages use `utility_controller.print_message()`.

    Parameters:
        message: Text to log.

    Examples:
        >>> import utility_controller as uc

        >>> uc.print_to_console('Script started')
    """

def export_screen_to_image(file_path: str, factor: int) -> None:
    """Save the current 3D view as an image file.

    The image has the size of the 3D view, enlarged by factor, with the current background colour.
    The format is derived from the file extension. A factor outside 1 to 6 is silently ignored and
    no file is written. For an in-memory result see `utility_controller.create_snapshot()`.

    Parameters:
        file_path: Target file path including extension, for example 'C:/temp/view.png'. Use forward
            slashes.
        factor: Enlargement factor applied to the view size, 1 for original size. Valid values are 1
            to 6.

    Examples:
        >>> import utility_controller as uc

        >>> uc.export_screen_to_image('C:/temp/view.png', 2)
    """

def get_new_user_file_from_dialog(name_filter: str) -> str:
    """Show a save-file dialog and return the chosen path.

    The script is blocked until the dialog is closed. The file is not created, your script must
    write it. The dialog starts in the user home folder. To start in another folder use
    `utility_controller.get_new_user_file_from_dialog_in_path()`.

    Parameters:
        name_filter: File filter in Qt syntax, for example 'Text files (*.txt)'.

    Examples:
        >>> import utility_controller as uc

        >>> path = uc.get_new_user_file_from_dialog('Text files (*.txt)')
        >>> if path:
        ...     with open(path, 'w') as f:
        ...         f.write('done')

    Returns:
        Full path chosen by the user; empty string if the dialog was cancelled.
    """

def api_autostart(api_name: str, option: int) -> int:
    """Enable, disable or query autostart of a Python API module for the current user.

    Reads and writes the user-profile alias and module configuration files, creating them if
    missing. Takes effect at the next start of cadwork 3D. Prefer
    `utility_controller.enable_autostart()`, `utility_controller.disable_autostart()` and
    `utility_controller.check_autostart()`.

    Parameters:
        api_name: Name of the API module to manage; an empty name is an error.
        option: 1 enables autostart, 0 disables it. The value is unsigned, so negative values are
            rejected with a TypeError; use `utility_controller.check_autostart()` to query.

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
    Errors are not reported. Check the result with `utility_controller.check_autostart()`; undo with
    `utility_controller.disable_autostart()`.

    Parameters:
        api_name: Name of the API module to enable.

    Examples:
        >>> import utility_controller as uc

        >>> uc.enable_autostart('my_api')
        >>> print(uc.check_autostart('my_api'))
    """

def disable_autostart(api_name: str) -> None:
    """Disable autostart of a Python API module for the current user.

    Writes the user-profile configuration files; takes effect at the next start of cadwork 3D.
    Errors are not reported. Re-enable with `utility_controller.enable_autostart()`.

    Parameters:
        api_name: Name of the API module to disable.

    Examples:
        >>> import utility_controller as uc

        >>> uc.disable_autostart('my_api')
    """

def check_autostart(api_name: str) -> bool:
    """Check whether autostart is enabled for a Python API module.

    Reads the user-profile configuration files without changing the autostart state (the alias files
    may be created if missing). An error, for example an empty name, is also reported as True, so
    validate the name before calling.

    Parameters:
        api_name: Name of the API module to check.

    Examples:
        >>> import utility_controller as uc

        >>> if not uc.check_autostart('my_api'):
        ...     uc.enable_autostart('my_api')

    Returns:
        True if autostart is enabled or an error occurred, False otherwise.
    """

def delete_project_data(project_data_id: str) -> None:
    """Delete an entry from the project data of the open document.

    Removes a value stored with `utility_controller.set_project_data()`. Read entries with
    `utility_controller.get_project_data()`.

    Parameters:
        project_data_id: ID of the project data entry, as used with
            `utility_controller.set_project_data()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_data('my_script.tmp', '1')
        >>> uc.delete_project_data('my_script.tmp')
    """

def run_external_program(name: str) -> bool:
    """Run an external program from the cadwork API folder.

    The name is appended to the API folder path of cadwork 3D, so only programs placed there can be
    started. For programs in another folder use
    `utility_controller.run_external_program_from_custom_directory()`.

    Parameters:
        name: File name of the program, relative to the API folder.

    Examples:
        >>> import utility_controller as uc

        >>> if not uc.run_external_program('my_tool.exe'):
        ...     uc.print_error('Could not start my_tool.exe')

    Returns:
        True if the program was started, False otherwise.
    """

def save_3d_file_silently() -> None:
    """Save the open 3D file without showing a dialog.

    Waits until saving has finished before returning. Saves to the current file path, see
    `utility_controller.get_3d_file_path()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.save_3d_file_silently()
    """

def get_licence_first_part() -> str:
    """Return the first part of the licence (dongle) ID.

    The dongle ID shown by cadwork consists of two parts; this returns the part before the angle
    brackets. See `utility_controller.get_licence_second_part()` for the other part.

    Examples:
        >>> import utility_controller as uc

        >>> print(uc.get_licence_first_part(), uc.get_licence_second_part())

    Returns:
        First part of the licence ID as a string.
    """

def get_licence_second_part() -> str:
    """Return the second part of the licence (dongle) ID.

    The dongle ID shown by cadwork consists of two parts; this returns the part inside the angle
    brackets. See `utility_controller.get_licence_first_part()` for the other part.

    Examples:
        >>> import utility_controller as uc

        >>> print(uc.get_licence_second_part())

    Returns:
        Second part of the licence ID as a string.
    """

def show_progress_bar() -> None:
    """Show the progress bar in the command bar, reset to its minimum.

    Update it with `utility_controller.update_progress_bar()` and remove it with
    `utility_controller.hide_progress_bar()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.show_progress_bar()
        >>> for percent in range(0, 101, 20):
        ...     uc.update_progress_bar(percent)
        >>> uc.hide_progress_bar()
    """

def update_progress_bar(value: int) -> None:
    """Set the value of the progress bar in the command bar.

    Show the bar first with `utility_controller.show_progress_bar()`. Hide it at the end with
    `utility_controller.hide_progress_bar()`.

    Parameters:
        value: Progress value, 0 to 100.

    Examples:
        >>> import utility_controller as uc

        >>> uc.show_progress_bar()
        >>> uc.update_progress_bar(50)
        >>> uc.hide_progress_bar()
    """

def hide_progress_bar() -> None:
    """Hide the progress bar in the command bar.

    Call it when the work shown with `utility_controller.show_progress_bar()` is finished, also
    after errors.

    Examples:
        >>> import utility_controller as uc

        >>> uc.show_progress_bar()
        >>> uc.hide_progress_bar()
    """

def get_user_color(initial_color: int) -> int:
    """Let the user choose a colour from the colour palette dialog.

    The script is blocked until the dialog is closed. In unattended runs (/PLUGIN or /RUNPROGRAM) no
    dialog is shown and initial_color is returned. Cancelling is not reported separately; compare
    the result with your initial value if needed.

    Parameters:
        initial_color: cadwork colour number preselected in the dialog.

    Examples:
        >>> import utility_controller as uc

        >>> color_id = uc.get_user_color(1)
        >>> print(f'Chosen colour: {color_id}')

    Returns:
        The chosen cadwork colour number; initial_color in unattended runs.
    """

def get_3d_linear_units() -> str:
    """Get the abbreviation of the document's linear unit.

    Reports the length unit in which the open document is configured. Coordinates and dimensions
    passed to the API stay in model units (mm) regardless of this setting. Use
    `utility_controller.get_3d_linear_display_units()` for the unit shown in the user interface.

    Examples:
        >>> import utility_controller as uc

        >>> unit = uc.get_3d_linear_units()
        >>> print('Document length unit:', unit or 'unknown')

    Returns:
        One of `mm`, `cm`, `m`, `in` or `ft`; empty string if the unit is none of these.
    """

def get_3d_linear_display_units() -> str:
    """Get the abbreviation of the linear unit used for display.

    Returns the length unit the user interface displays, which can differ from the document unit
    returned by `utility_controller.get_3d_linear_units()`.

    Examples:
        >>> import utility_controller as uc

        >>> document_unit = uc.get_3d_linear_units()
        >>> display_unit = uc.get_3d_linear_display_units()
        >>> if document_unit != display_unit:
        ...     print('Display unit differs:', display_unit)

    Returns:
        One of `mm`, `cm`, `m`, `in` or `ft`; empty string if the unit is none of these.
    """

def get_3d_angular_units() -> str:
    """Get the abbreviation of the document's angular unit.

    Reports the angle unit in which the open document is configured. Use
    `utility_controller.get_3d_angular_display_units()` for the unit shown in the user interface.

    Examples:
        >>> import utility_controller as uc

        >>> unit = uc.get_3d_angular_units()
        >>> print('Document angle unit:', unit or 'unknown')

    Returns:
        One of `deg`, `gon`, `rad` or `pct`; empty string if the unit is none of these.
    """

def get_3d_angular_display_units() -> str:
    """Get the abbreviation of the angular unit used for display.

    Returns the angle unit the user interface displays, which can differ from the document unit
    returned by `utility_controller.get_3d_angular_units()`.

    Examples:
        >>> import utility_controller as uc

        >>> unit = uc.get_3d_angular_display_units()
        >>> print('Displayed angle unit:', unit or 'unknown')

    Returns:
        One of `deg`, `gon`, `rad` or `pct`; empty string if the unit is none of these.
    """

def get_3d_build_date() -> str:
    """Get the build date of the running cadwork 3D version.

    Identifies the installed cadwork 3D build, for example to log it or to branch on the program
    version in a script.

    Examples:
        >>> import utility_controller as uc

        >>> print('cadwork 3D build date:', uc.get_3d_build_date())

    Returns:
        The build date as text, in the format of the cadwork version information.
    """

def set_project_elevation(elevation: float) -> None:
    """Set the project elevation in the project data.

    Writes the value into the project data of the open document, the same value that is edited in
    the project data dialog (stored there as the project height). Other project data fields are
    kept. Open the dialog with `utility_controller.start_project_data_dialog()`.

    Parameters:
        elevation: New project elevation. It is stored as given, without unit conversion, and is
            the value `utility_controller.get_project_elevation()` returns.

    Examples:
        >>> import utility_controller as uc

        >>> elevation = uc.get_project_elevation()
        >>> uc.set_project_elevation(elevation + 10.0)
        >>> print(uc.get_project_elevation())
    """

def clear_errors() -> None:
    """Clear the list of errors collected by the API.

    The API collects errors reported by failed calls in an internal list. This empties that list so
    that later error checks only see new errors. It does not undo anything and does not affect the
    model.

    Examples:
        >>> import utility_controller as uc

        >>> uc.clear_errors()
    """

def push_check_and_query_data() -> None:
    """Save the current confirmation-dialog settings on a stack.

    Confirmation dialogs of cadwork 3D can be set to ask, always answer yes or never. This stores a
    snapshot of those document settings so they can be restored later. Call
    `utility_controller.pop_check_and_query_data()` to restore the snapshot after temporarily
    suppressing dialogs with `utility_controller.change_check_and_query_data_to_no_queries()`. Calls
    may be nested; each pop restores the most recent push.

    Examples:
        >>> import utility_controller as uc

        >>> uc.push_check_and_query_data()
        >>> uc.change_check_and_query_data_to_no_queries()
        ... # ... run operations that would normally show confirmation dialogs ...
        >>> uc.pop_check_and_query_data()
    """

def pop_check_and_query_data() -> None:
    """Restore the confirmation-dialog settings saved by the last push.

    Takes the most recent snapshot made by `utility_controller.push_check_and_query_data()` off the
    stack and applies it to the document settings. Does nothing if nothing was pushed.

    Examples:
        >>> import utility_controller as uc

        >>> uc.push_check_and_query_data()
        >>> uc.change_check_and_query_data_to_no_queries()
        ... # ... run the unattended work ...
        >>> uc.pop_check_and_query_data()
    """

def change_check_and_query_data_to_no_queries() -> None:
    """Suppress confirmation dialogs by answering them automatically.

    Every confirmation dialog set to ask with default Yes is switched to always yes, and every one
    set to ask with default No is switched to never, so scripts are not interrupted by prompts. The
    change is written to the document settings and stays until reverted. Wrap the call in
    `utility_controller.push_check_and_query_data()` and
    `utility_controller.pop_check_and_query_data()` to restore the user's settings afterwards.

    Examples:
        >>> import utility_controller as uc

        >>> uc.push_check_and_query_data()
        >>> uc.change_check_and_query_data_to_no_queries()
        ... # ... run operations without confirmation dialogs ...
        >>> uc.pop_check_and_query_data()
    """

def change_check_and_query_data_to_queries() -> None:
    """Re-enable confirmation dialogs that were set to answer automatically.

    Reverses `utility_controller.change_check_and_query_data_to_no_queries()`: dialogs set to always
    yes are switched back to ask with default Yes, and those set to never back to ask with default
    No. Dialogs already set to ask are untouched. This also converts entries the user had set to
    always or never before the script started, so prefer
    `utility_controller.pop_check_and_query_data()` to restore the exact previous state.

    Examples:
        >>> import utility_controller as uc

        >>> uc.change_check_and_query_data_to_no_queries()
        ... # ... unattended work ...
        >>> uc.change_check_and_query_data_to_queries()
    """

def is_direct_info_enabled() -> bool:
    """Check whether the Direct Info tooltip is enabled.

    Direct Info is the tooltip that shows element information when the mouse hovers over an element.
    The setting is a program option, not part of the document. Change it with
    `utility_controller.enable_direct_info()` or `utility_controller.disable_direct_info()`.

    Examples:
        >>> import utility_controller as uc

        >>> if not uc.is_direct_info_enabled():
        ...     uc.enable_direct_info()

    Returns:
        `True` if Direct Info is enabled, `False` otherwise.
    """

def enable_direct_info() -> None:
    """Enable the Direct Info tooltip for elements.

    Turns on the tooltip that shows element information on mouse hover. The setting is saved in the
    program options, so it applies to all documents. Check the state with
    `utility_controller.is_direct_info_enabled()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.enable_direct_info()
    """

def disable_direct_info() -> None:
    """Disable the Direct Info tooltip for elements.

    Turns off the tooltip that shows element information on mouse hover. The setting is saved in the
    program options, so it applies to all documents. Restore it with
    `utility_controller.enable_direct_info()`.

    Examples:
        >>> import utility_controller as uc

        >>> was_enabled = uc.is_direct_info_enabled()
        >>> uc.disable_direct_info()
        ... # ... work ...
        >>> if was_enabled:
        ...     uc.enable_direct_info()
    """

def load_attribute_display_settings(file_path: str) -> None:
    """Load attribute display settings from a settings file and apply them.

    Attribute display settings control which attributes are shown for each display type (for example
    general 3D display, export, machine or container lists) and how they are formatted. The settings
    of all supported display types and the format settings found in the file replace the current
    ones; types missing in the file keep their current setting. To apply the settings only to
    specific elements use `utility_controller.load_element_attribute_display_settings()`.

    Parameters:
        file_path: Path of an existing attribute display settings file. Use forward slashes, e.g.
            `C:/settings/attributes.ini`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.load_attribute_display_settings('C:/settings/attributes.ini')
    """

def set_project_description(description: str) -> None:
    """Set the project description in the project data.

    Writes the text into the project data of the open document, the same field that is edited in the
    project data dialog. Open the dialog with `utility_controller.start_project_data_dialog()` to
    see it.

    Parameters:
        description: New project description text. Replaces the existing description.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_project_description('Timber frame house, 2 storeys')
    """

def start_project_data_dialog() -> None:
    """Open the project data dialog.

    Shows the project data dialog (project name, number, customer and so on) to the user. Do not
    call it in unattended runs. The values can be read afterwards with functions such as
    `utility_controller.get_project_name()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.start_project_data_dialog()
        >>> print(uc.get_project_name())
    """

def init_LxSDK() -> None:
    """Initialize the LxSDK of the open document.

    Initializes the LxSDK bridge of the current document. Call it before using functionality that
    depends on the LxSDK.

    Examples:
        >>> import utility_controller as uc

        >>> uc.init_LxSDK()
    """

def load_element_attribute_display_settings(file_path: str, elements: list[ElementId]) -> None:
    """Load attribute display settings from a file for the given elements.

    Same as `utility_controller.load_attribute_display_settings()`, but the settings are applied to
    the given elements. Element IDs that do not exist are skipped. The use-global flag stored in the
    file is applied to each loaded setting. Settings and format settings found in the file replace
    the current ones.

    Parameters:
        file_path: Path of an existing attribute display settings file. Use forward slashes, e.g.
            `C:/settings/attributes.ini`.
        elements: List of element IDs, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import utility_controller as uc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> uc.load_element_attribute_display_settings('C:/settings/attributes.ini', element_ids)
    """

def get_global_x_offset() -> float:
    """Get the X coordinate of the document's global origin.

    The global origin is a coordinate offset stored in the document. Set it with
    `utility_controller.set_global_x_offset()`.

    Examples:
        >>> import utility_controller as uc

        >>> offset = uc.get_global_x_offset()
        >>> print('Global X offset (mm):', offset)

    Returns:
        Global X offset in model units (mm).
    """

def set_global_x_offset(offset: float) -> None:
    """Set the X coordinate of the document's global origin.

    Replaces only the X coordinate of the global origin stored in the document; the other two
    coordinates are unchanged. Read the current value with
    `utility_controller.get_global_x_offset()`.

    Parameters:
        offset: New global X offset in model units (mm).

    Examples:
        >>> import utility_controller as uc

        >>> old_offset = uc.get_global_x_offset()
        >>> uc.set_global_x_offset(old_offset + 1000.0)
    """

def get_global_y_offset() -> float:
    """Get the Y coordinate of the document's global origin.

    The global origin is a coordinate offset stored in the document. Set it with
    `utility_controller.set_global_y_offset()`.

    Examples:
        >>> import utility_controller as uc

        >>> offset = uc.get_global_y_offset()
        >>> print('Global Y offset (mm):', offset)

    Returns:
        Global Y offset in model units (mm).
    """

def set_global_y_offset(offset: float) -> None:
    """Set the Y coordinate of the document's global origin.

    Replaces only the Y coordinate of the global origin stored in the document; the other two
    coordinates are unchanged. Read the current value with
    `utility_controller.get_global_y_offset()`.

    Parameters:
        offset: New global Y offset in model units (mm).

    Examples:
        >>> import utility_controller as uc

        >>> old_offset = uc.get_global_y_offset()
        >>> uc.set_global_y_offset(old_offset + 1000.0)
    """

def get_global_z_offset() -> float:
    """Get the Z coordinate of the document's global origin.

    The global origin is a coordinate offset stored in the document. Set it with
    `utility_controller.set_global_z_offset()`.

    Examples:
        >>> import utility_controller as uc

        >>> offset = uc.get_global_z_offset()
        >>> print('Global Z offset (mm):', offset)

    Returns:
        Global Z offset in model units (mm).
    """

def set_global_z_offset(offset: float) -> None:
    """Set the Z coordinate of the document's global origin.

    Replaces only the Z coordinate of the global origin stored in the document; the other two
    coordinates are unchanged. Read the current value with
    `utility_controller.get_global_z_offset()`.

    Parameters:
        offset: New global Z offset in model units (mm).

    Examples:
        >>> import utility_controller as uc

        >>> old_offset = uc.get_global_z_offset()
        >>> uc.set_global_z_offset(old_offset + 1000.0)
    """

def show_north_arrow() -> None:
    """Show the north arrow (deprecated, does nothing).

    Deprecated: logs a warning and has no effect. Use the navigation widget functions such as
    `utility_controller.set_navigation_widget_north_arrow()` instead.

    Examples:
        >>> import utility_controller as uc

        ... # Deprecated: has no effect. Use the navigation widget instead.
        >>> uc.show_north_arrow()
    """

def hide_north_arrow() -> None:
    """Hide the north arrow (deprecated, does nothing).

    Deprecated: logs a warning and has no effect. Use the navigation widget functions such as
    `utility_controller.set_navigation_widget_north_arrow()` instead.

    Examples:
        >>> import utility_controller as uc

        ... # Deprecated: has no effect. Use the navigation widget instead.
        >>> uc.hide_north_arrow()
    """

def is_north_arrow_visible() -> bool:
    """Check whether the north arrow is visible (deprecated).

    Deprecated: logs a warning and always returns `False`, whatever is displayed. Use the navigation
    widget functions instead.

    Examples:
        >>> import utility_controller as uc

        ... # Deprecated: always False, do not rely on it.
        >>> visible = uc.is_north_arrow_visible()

    Returns:
        Always `False`.
    """

def get_north_angle() -> float:
    """Get the north direction angle stored in the program options.

    The north angle is a program option, not part of the document. Set it with
    `utility_controller.set_north_angle()`.

    Examples:
        >>> import utility_controller as uc

        >>> angle = uc.get_north_angle()
        >>> print('North angle (deg):', angle)

    Returns:
        North angle in degrees.
    """

def set_north_angle(north_angle: float) -> None:
    """Set the north direction angle in the program options.

    Stores the value in the program options, so it is not saved in the document. Read it back with
    `utility_controller.get_north_angle()`.

    Parameters:
        north_angle: North angle in degrees.

    Examples:
        >>> import utility_controller as uc

        >>> uc.set_north_angle(45.0)
        >>> print(uc.get_north_angle())
    """

def get_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Show an open-file dialog starting in a folder and return the chosen file.

    Opens the standard file dialog in open mode, restricted to existing files. The script is blocked
    until the user closes the dialog, so do not use it in unattended runs. Unlike the folder
    dialogs, this dialog has no plugin-run check. Use
    `utility_controller.get_user_file_from_dialog()` if no start folder is needed.

    Parameters:
        name_filter: File filter in dialog format, e.g. `Text files (*.txt)`; several patterns can
            be given in one group, e.g. `Images (*.png *.jpg)`.
        path: Folder in which the dialog starts.

    Examples:
        >>> import utility_controller as uc

        >>> file_path = uc.get_user_file_from_dialog_in_path('Text files (*.txt)', 'C:/temp')
        >>> if file_path:
        ...     print('Selected:', file_path)

    Returns:
        Full path of the selected existing file; empty string if the dialog is cancelled.
    """

def get_new_user_file_from_dialog_in_path(name_filter: str, path: str) -> str:
    """Show a save-file dialog starting in a folder and return the chosen file name.

    Opens the standard file dialog in save mode, so the user can type a new name or pick an existing
    file. The script is blocked until the user closes the dialog, so do not use it in unattended
    runs. The file is not created; the script has to write it. Use
    `utility_controller.get_new_user_file_from_dialog()` if no start folder is needed.

    Parameters:
        name_filter: File filter in dialog format, e.g. `Text files (*.txt)`.
        path: Folder in which the dialog starts.

    Examples:
        >>> import utility_controller as uc

        >>> file_path = uc.get_new_user_file_from_dialog_in_path('Text files (*.txt)', 'C:/temp')
        >>> if file_path:
        ...     with open(file_path, 'w') as f:
        ...         f.write('result')

    Returns:
        Full path of the chosen file; empty string if the dialog is cancelled.
    """

def enable_update_variant() -> None:
    """Enable automatic updating of variants.

    Turns the automatic variant update back on. It is reversed by
    `utility_controller.disable_update_variant()`.

    Examples:
        >>> import utility_controller as uc

        >>> uc.disable_update_variant()
        ... # ... modify elements without triggering variant updates ...
        >>> uc.enable_update_variant()
    """

def disable_update_variant() -> None:
    """Disable automatic updating of variants.

    Stops variants from being recalculated automatically when their elements change, for example
    while a script modifies many elements. Call `utility_controller.enable_update_variant()`
    afterwards to turn it on again.

    Examples:
        >>> import utility_controller as uc

        >>> uc.disable_update_variant()
        >>> try:
        ...     pass  # modify elements here
        ... finally:
        ...     uc.enable_update_variant()
    """

def get_user_points() -> list[point_3d]:
    """Let the user pick any number of points in the 3D view.

    Starts an interactive point-picking mode in the 3D view and blocks the script until the user has
    finished. In unattended plugin runs (`/PLUGIN` or `/RUNPROGRAM` mode) no interaction takes place
    and an empty list is returned. To pick one point use `utility_controller.get_user_point()`, for
    a fixed maximum use `utility_controller.get_user_points_with_count()`.

    Examples:
        >>> import utility_controller as uc

        >>> points = uc.get_user_points()
        >>> if points:
        ...     print('Picked', len(points), 'points')

    Returns:
        List of picked `point_3d` in model units (mm) in picking order; empty list if nothing was
        picked or the interaction is skipped.
    """

def get_user_points_with_count(count: int) -> list[point_3d]:
    """Let the user pick a given number of points in the 3D view.

    Starts an interactive point-picking mode and blocks the script until the points are picked.
    Returns an empty list for a count of 0 and in unattended plugin runs (`/PLUGIN` or `/RUNPROGRAM`
    mode). A count of 1 uses the single-point picker of `utility_controller.get_user_point()`. Check
    the length of the result before using it.

    Parameters:
        count: Maximum number of points to pick. 0 returns an empty list; 1 asks for a single point.

    Examples:
        >>> import utility_controller as uc

        >>> points = uc.get_user_points_with_count(2)
        >>> if len(points) == 2:
        ...     start, end = points
        ...     print('Picked', start.x, end.x)

    Returns:
        List of picked `point_3d` in model units (mm) in picking order; empty list if count is 0 or
        the interaction is skipped. With a count of 1 the list always holds one point, which is
        (0, 0, 0) if the pick was cancelled.
    """

def get_user_path_from_dialog() -> str:
    """Show a folder-selection dialog and return the chosen folder.

    Opens a dialog that lists folders only and blocks the script until the user closes it. In
    unattended plugin runs (`/PLUGIN` or `/RUNPROGRAM` mode) no dialog is shown and an empty string
    is returned. Use `utility_controller.get_user_path_from_dialog_in_path()` to choose the start
    folder.

    Examples:
        >>> import utility_controller as uc

        >>> folder = uc.get_user_path_from_dialog()
        >>> if folder:
        ...     print('Export to', folder)

    Returns:
        Full path of the selected folder; empty string if cancelled or skipped.
    """

def get_user_path_from_dialog_in_path(path: str) -> str:
    """Show a folder-selection dialog starting in a folder and return the chosen folder.

    Opens a dialog that lists folders only, starting in the given folder, and blocks the script
    until the user closes it. In unattended plugin runs (`/PLUGIN` or `/RUNPROGRAM` mode) no dialog
    is shown and an empty string is returned.

    Parameters:
        path: Folder in which the dialog starts.

    Examples:
        >>> import utility_controller as uc

        >>> folder = uc.get_user_path_from_dialog_in_path('C:/temp')
        >>> if folder:
        ...     print('Export to', folder)

    Returns:
        Full path of the selected folder; empty string if cancelled or skipped.
    """

def execute_shortcut(shortcut_key_modifier: shortcut_key_modifier, shortcut_key: shortcut_key) -> None:
    """Trigger the main window action bound to a keyboard shortcut.

    Looks through the actions of the cadwork 3D main window and triggers every action whose shortcut
    equals the given key combination, as if the user had pressed it. Only function keys F1 to F12
    are supported, optionally combined with one modifier. Nothing happens if no action matches. The
    triggered action may open dialogs that block the script.

    Parameters:
        shortcut_key_modifier: Modifier key: `cadwork.shortcut_key_modifier.no_modifier`, `shift`,
            `ctrl` or `alt`.
        shortcut_key: Function key `cadwork.shortcut_key.F1` to `F12`.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> uc.execute_shortcut(
        ...     cadwork.shortcut_key_modifier.no_modifier,
        ...     cadwork.shortcut_key.F5,
        ... )
    """

def run_external_program_from_custom_directory(file_path: str) -> bool:
    """Run a 3D external program from a file path.

    Starts an external program through the external program manager of the open document, given the
    full path of the program file. Use it when the program is not in the standard program folders.

    Parameters:
        file_path: Path of the external program file. Use forward slashes, e.g.
            `C:/plugins/my_tool.py`.

    Examples:
        >>> import utility_controller as uc

        >>> started = uc.run_external_program_from_custom_directory('C:/plugins/my_tool.py')
        >>> if not started:
        ...     print('Program could not be started')

    Returns:
        `True` if the program was started, `False` on error.
    """

def get_3d_file_name() -> str:
    """Get the file name of the open 3D document.

    Returns only the file name; use `utility_controller.get_3d_file_path()` for the full path.

    Examples:
        >>> import utility_controller as uc

        >>> name = uc.get_3d_file_name()
        >>> print('Open document:', name)

    Returns:
        File name without folder, including extension; may be empty if the document has no file path
        yet.
    """

def get_project_data(project_data_id: str) -> str:
    """Get a project data value by its ID.

    Project data entries are free text values stored in the document under an ID of your choice,
    written with `utility_controller.set_project_data()`. Use them to keep script settings with the
    model.

    Parameters:
        project_data_id: ID (name) of the project data entry, as used with
            `utility_controller.set_project_data()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_data('my_script_version')
        >>> if not value:
        ...     uc.set_project_data('my_script_version', '1.0')

    Returns:
        The stored value; empty string if the ID does not exist.
    """

def get_project_name() -> str:
    """Get the project name from the project data.

    Reads the project name entered in the project data of the open document. Change it with
    `utility_controller.set_project_name()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_name()
        >>> print(value or '(not set)')

    Returns:
        The project name as text; empty string if not set.
    """

def get_project_part() -> str:
    """Get the project part from the project data.

    Reads the project part entered in the project data of the open document. Change it with
    `utility_controller.set_project_part()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_part()
        >>> print(value or '(not set)')

    Returns:
        The project part as text; empty string if not set.
    """

def get_project_architect() -> str:
    """Get the project architect from the project data.

    Reads the project architect entered in the project data of the open document. Change it with
    `utility_controller.set_project_architect()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_architect()
        >>> print(value or '(not set)')

    Returns:
        The project architect as text; empty string if not set.
    """

def get_project_number() -> str:
    """Get the project number from the project data.

    Reads the project number entered in the project data of the open document. Change it with
    `utility_controller.set_project_number()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_number()
        >>> print(value or '(not set)')

    Returns:
        The project number as text; empty string if not set.
    """

def get_project_customer() -> str:
    """Get the project customer from the project data.

    Reads the project customer entered in the project data of the open document. Edit it in the
    dialog opened by `utility_controller.start_project_data_dialog()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_customer()
        >>> print(value or '(not set)')

    Returns:
        The project customer as text; empty string if not set.
    """

def get_project_designer() -> str:
    """Get the project designer from the project data.

    Reads the project designer entered in the project data of the open document. Edit it in the
    dialog opened by `utility_controller.start_project_data_dialog()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_designer()
        >>> print(value or '(not set)')

    Returns:
        The project designer as text; empty string if not set.
    """

def get_project_deadline() -> str:
    """Get the project deadline from the project data.

    Reads the project deadline entered in the project data of the open document. Edit it in the
    dialog opened by `utility_controller.start_project_data_dialog()`.

    Examples:
        >>> import utility_controller as uc

        >>> value = uc.get_project_deadline()
        >>> print(value or '(not set)')

    Returns:
        The project deadline as text; empty string if not set.
    """

def get_project_user_attribute(number: int) -> str:
    """Get a project user attribute value by its number.

    Project user attributes are numbered free-text fields in the project data. Their titles can be
    read with `utility_controller.get_project_user_attribute_name()` and the value written with
    `utility_controller.set_project_user_attribute()`.

    Parameters:
        number: Number of the project user attribute, as shown in the project data dialog.

    Examples:
        >>> import utility_controller as uc

        >>> name = uc.get_project_user_attribute_name(1)
        >>> value = uc.get_project_user_attribute(1)
        >>> print(name, '=', value)

    Returns:
        The value of the attribute; empty string if not set.
    """

def get_project_user_attribute_name(number: int) -> str:
    """Return the title of a project user attribute slot.

    Project user attributes are free text fields in the project data dialog, each with a title and a
    value. This returns the title (the label shown in the dialog), not the value. The value is read
    with `utility_controller.get_project_user_attribute()` and the title is changed with
    `utility_controller.set_project_user_attribute_name()`.

    Parameters:
        number: Number of the project user attribute slot, as numbered in the project data dialog.

    Examples:
        >>> import utility_controller as uc

        >>> name = uc.get_project_user_attribute_name(1)
        >>> value = uc.get_project_user_attribute(1)
        >>> print(name, value)

    Returns:
        The slot title as text; an empty string if no title is set.
    """

def get_project_latitude() -> float:
    """Return the project latitude from the project data.

    Reads the latitude entered in the project data dialog of the current document. It is the
    geographic location of the construction site, together with
    `utility_controller.get_project_longitude()`.

    Examples:
        >>> import utility_controller as uc

        >>> latitude = uc.get_project_latitude()
        >>> longitude = uc.get_project_longitude()
        >>> print(latitude, longitude)

    Returns:
        The latitude as a float, 0.0 if none was entered.
    """

def get_project_longitude() -> float:
    """Return the project longitude from the project data.

    Reads the longitude entered in the project data dialog of the current document. It is the
    geographic location of the construction site, together with
    `utility_controller.get_project_latitude()`.

    Examples:
        >>> import utility_controller as uc

        >>> longitude = uc.get_project_longitude()
        >>> latitude = uc.get_project_latitude()
        >>> print(longitude, latitude)

    Returns:
        The longitude as a float, 0.0 if none was entered.
    """

def get_project_postal_code() -> str:
    """Return the project postal code from the project data.

    Reads the postal code of the construction site as entered in the project data dialog of the
    current document. Related: `utility_controller.get_project_city()`,
    `utility_controller.get_project_address()` and `utility_controller.get_project_country()`.

    Examples:
        >>> import utility_controller as uc

        >>> postal_code = uc.get_project_postal_code()
        >>> city = uc.get_project_city()
        >>> print(postal_code, city)

    Returns:
        The postal code as text; an empty string if none is entered.
    """

def get_project_address() -> str:
    """Return the project address from the project data.

    Reads the street address of the construction site as entered in the project data dialog of the
    current document. Related: `utility_controller.get_project_postal_code()`,
    `utility_controller.get_project_city()` and `utility_controller.get_project_country()`.

    Examples:
        >>> import utility_controller as uc

        >>> address = uc.get_project_address()
        >>> if address:
        ...     print(address)

    Returns:
        The address as text; an empty string if none is entered.
    """

def get_project_city() -> str:
    """Return the project city from the project data.

    Reads the city of the construction site as entered in the project data dialog of the current
    document. Related: `utility_controller.get_project_postal_code()`,
    `utility_controller.get_project_address()` and `utility_controller.get_project_country()`.

    Examples:
        >>> import utility_controller as uc

        >>> city = uc.get_project_city()
        >>> if city:
        ...     print(city)

    Returns:
        The city as text; an empty string if none is entered.
    """

def get_project_country() -> str:
    """Return the project country from the project data.

    Reads the country of the construction site as entered in the project data dialog of the current
    document. Related: `utility_controller.get_project_postal_code()`,
    `utility_controller.get_project_address()` and `utility_controller.get_project_city()`.

    Examples:
        >>> import utility_controller as uc

        >>> country = uc.get_project_country()
        >>> if country:
        ...     print(country)

    Returns:
        The country as text; an empty string if none is entered.
    """

def get_project_elevation() -> float:
    """Return the project elevation (height) from the project data.

    Reads the elevation entered in the project data dialog of the current document. It is a project
    data field only; it does not move any element.

    Examples:
        >>> import utility_controller as uc

        >>> elevation = uc.get_project_elevation()
        >>> print(elevation)

    Returns:
        The elevation as a float, as stored in the project data without unit conversion; 0.0 if
        none was entered.
    """

def get_project_description() -> str:
    """Return the project description from the project data.

    Reads the free text description entered in the project data dialog of the current document.

    Examples:
        >>> import utility_controller as uc

        >>> description = uc.get_project_description()
        >>> print(description)

    Returns:
        The description as text; an empty string if none is entered.
    """

def get_project_guid() -> str:
    """Return the GUID of the current project.

    The GUID identifies the project in the cadwork project database. Use it as a stable key when you
    store or exchange data about the project outside cadwork.

    Examples:
        >>> import utility_controller as uc

        >>> project_guid = uc.get_project_guid()
        >>> print(project_guid)

    Returns:
        The project GUID as text.
    """

def get_3d_userprofil_path() -> str:
    """Return the path of the cadwork user profile directory.

    The user profile directory holds the per-user cadwork settings and data files. Use it to locate
    files that cadwork stores for the current user. Related:
    `utility_controller.get_user_catalog_path()` and `utility_controller.get_plugin_path()`.

    Examples:
        >>> import utility_controller as uc

        >>> profile_path = uc.get_3d_userprofil_path()
        >>> print(profile_path)

    Returns:
        The directory path as text.
    """

def get_plugin_path() -> str:
    """Return the path of the cadwork plugin directory.

    The plugin directory is where cadwork looks for installed plugins and Python scripts. Use it to
    locate or install files next to your plugin. Related:
    `utility_controller.get_3d_userprofil_path()`.

    Examples:
        >>> import utility_controller as uc

        >>> plugin_path = uc.get_plugin_path()
        >>> print(plugin_path)

    Returns:
        The directory path as text.
    """

def get_millimetre_from_imperial_string(value: str) -> float:
    """Convert an imperial length string to millimetres.

    Parses a length written in imperial notation, for example inches or feet and inches, and returns
    it in millimetres, the unit of the cadwork model. The reverse conversion is
    `utility_controller.get_imperial_string_from_millimetre()`. The accepted notations are defined
    by the cadwork unit converter.

    Parameters:
        value: Imperial length as text, for example a feet-and-inches or inches string, as a user
            would type it in cadwork.

    Examples:
        >>> import utility_controller as uc

        >>> text = uc.get_user_string('Length in feet and inches')
        >>> length_mm = uc.get_millimetre_from_imperial_string(text)
        >>> print(length_mm)

    Returns:
        The length in millimetres as a float.
    """

def get_imperial_string_from_millimetre(value: float) -> str:
    """Convert a length in millimetres to an imperial length string.

    Formats a model length (mm) as imperial text for display or reports. The reverse conversion is
    `utility_controller.get_millimetre_from_imperial_string()`. The text format is defined by the
    cadwork unit converter.

    Parameters:
        value: Length in millimetres, as used by the model.

    Examples:
        >>> import utility_controller as uc

        >>> text = uc.get_imperial_string_from_millimetre(1500.0)
        >>> print(text)

    Returns:
        The length as imperial text.
    """

def get_user_catalog_path() -> str:
    """Return the path of the cadwork user catalog directory.

    The user catalog directory holds the catalog files of the current user. Use it to locate or
    place catalog files. Related: `utility_controller.get_3d_userprofil_path()`.

    Examples:
        >>> import utility_controller as uc

        >>> catalog_path = uc.get_user_catalog_path()
        >>> print(catalog_path)

    Returns:
        The directory path as text.
    """

def get_3d_hwnd() -> int:
    """Return the native window handle of the cadwork 3D main window.

    The handle is the Windows HWND, useful when you embed your own windows or dialogs as children of
    cadwork, or call Windows APIs that need the owner window.

    Examples:
        >>> import utility_controller as uc

        >>> hwnd = uc.get_3d_hwnd()
        >>> if hwnd:
        ...     print(hex(hwnd))

    Returns:
        The window handle as an integer; 0 if there is no main window.
    """

def close_cadwork_document_saved() -> None:
    """Save the document silently, then close cadwork.

    Saves the current document without any prompt and then shuts the cadwork application down, so
    the script ends with it and nothing after this call runs. When cadwork was started unattended
    with a plugin or program start parameter, the closing is skipped (a warning is logged) because
    cadwork closes itself after the script. To close without saving use
    `utility_controller.close_cadwork_document_unsaved()`.

    Examples:
        >>> import utility_controller as uc

        ... # do all work first; the script ends with cadwork
        >>> uc.close_cadwork_document_saved()
    """

def close_cadwork_document_unsaved() -> None:
    """Close cadwork without saving the document.

    Shuts the cadwork application down immediately; unsaved changes are lost and the script ends
    with it, so nothing after this call runs. When cadwork was started unattended with a plugin or
    program start parameter, the call is ignored (a warning is logged) because cadwork closes itself
    after the script. To keep the changes use `utility_controller.close_cadwork_document_saved()`.

    Examples:
        >>> import utility_controller as uc

        ... # all unsaved changes are discarded
        >>> uc.close_cadwork_document_unsaved()
    """

def get_use_of_global_coordinates() -> bool:
    """Return whether global coordinates are used.

    This is a cadwork application option, not a property of the document. Change it with
    `utility_controller.set_use_of_global_coordinates()`; the origin itself is read with
    `utility_controller.get_global_origin()`.

    Examples:
        >>> import utility_controller as uc

        >>> if uc.get_use_of_global_coordinates():
        ...     print(uc.get_global_origin())

    Returns:
        True if global coordinates are enabled, False otherwise.
    """

def set_use_of_global_coordinates(use_of_global_coordinates: bool) -> None:
    """Enable or disable the use of global coordinates.

    Sets a cadwork application option; it does not change the global origin and is not stored in the
    document. Read the current state with `utility_controller.get_use_of_global_coordinates()` and
    set the origin with `utility_controller.set_global_origin()`.

    Parameters:
        use_of_global_coordinates: True to use global coordinates, False to use local ones.

    Examples:
        >>> import utility_controller as uc

        >>> previous = uc.get_use_of_global_coordinates()
        >>> uc.set_use_of_global_coordinates(True)
        ... # ... work with global coordinates ...
        >>> uc.set_use_of_global_coordinates(previous)
    """

def get_global_origin() -> point_3d:
    """Return the global origin of the document.

    The global origin is the reference point of the global coordinate system, stored in the
    document. Set it with `utility_controller.set_global_origin()`; whether it is used depends on
    `utility_controller.get_use_of_global_coordinates()`.

    Examples:
        >>> import utility_controller as uc

        >>> origin = uc.get_global_origin()
        >>> print(origin.x, origin.y, origin.z)

    Returns:
        The global origin as a point_3d in model units (mm).
    """

def set_global_origin(global_origin: point_3d) -> None:
    """Set the global origin of the document.

    Stores a new global origin in the document. It does not switch global coordinates on; use
    `utility_controller.set_use_of_global_coordinates()` for that. Read the current value with
    `utility_controller.get_global_origin()`.

    Parameters:
        global_origin: New global origin as a point_3d in model units (mm).

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> uc.set_global_origin(cadwork.point_3d(2600000.0, 1200000.0, 0.0))
        >>> print(uc.get_global_origin().x)
    """

def create_snapshot(image_format: str = 'PNG', quality: int = -1, white_background: bool = True, /) -> str:
    """Capture the 3D view as a Base64-encoded image string.

    Renders the current 3D view to an image in the requested format and returns it as Base64 text,
    so it can be stored, sent or decoded with the Python base64 module. The arguments are positional
    only. No file is written.

    Parameters:
        image_format: Image format name, e.g. "PNG" or "JPEG".
        quality: Compression quality from 0 (small, compressed) to 100 (large, uncompressed); -1
            uses the format's default.
        white_background: True for a white background, False for a transparent one (only visible in
            formats with transparency, such as PNG).

    Examples:
        >>> import utility_controller as uc

        >>> image_base64 = uc.create_snapshot('PNG', -1, True)
        >>> if image_base64:
        ...     print(len(image_base64))

    Returns:
        The Base64-encoded image; an empty string if the image could not be encoded in that format.
    """

def get_3d_gui_upper_left_screen_coordinates() -> tuple[int, int]:
    """Return the screen position of the upper left corner of the 3D main window.

    Gives the position of the cadwork main window on the desktop, for example to place your own
    window next to it. The values are the top left corner of
    `utility_controller.get_3d_main_window_geometry()`.

    Examples:
        >>> import utility_controller as uc

        >>> x, y = uc.get_3d_gui_upper_left_screen_coordinates()
        >>> print(x, y)

    Returns:
        A tuple (x, y) in screen pixels.
    """

def get_3d_main_window_geometry() -> 'window_geometry':
    """Return the screen geometry of the cadwork 3D main window.

    Gives the four corners of the main window in screen pixels, for example to place your own window
    relative to cadwork. The upper left corner is also available from
    `utility_controller.get_3d_gui_upper_left_screen_coordinates()`.

    Examples:
        >>> import utility_controller as uc

        >>> geometry = uc.get_3d_main_window_geometry()
        >>> width = geometry.top_right.x - geometry.top_left.x
        >>> print(geometry.top_left.x, geometry.top_left.y, width)

    Returns:
        A window_geometry with the four corner points bottom_left, bottom_right, top_left and
        top_right, each with x and y in screen pixels.
    """

def get_project_data_keys() -> list[str]:
    """Return the keys of the project data entries stored in the document.

    Project data entries are text values stored in the document under a key, for example by plugins.
    Keys that cadwork uses internally are left out. Read the value of a key with
    `utility_controller.get_project_data()`.

    Examples:
        >>> import utility_controller as uc

        >>> for key in uc.get_project_data_keys():
        ...     print(key, uc.get_project_data(key))

    Returns:
        List of project data keys as text; an empty list if there are none.
    """

def get_user_int_with_default_value(message: str, default_value: int) -> int:
    """Ask the user to enter an integer in the command bar, with a default.

    Shows the prompt in the cadwork command bar with the default pre-filled and blocks the script
    until the user confirms or cancels. When cadwork runs unattended via a plugin or program start
    parameter, nothing is shown and the default is returned. Use
    `utility_controller.get_user_double_with_default_value()` for decimal numbers.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Value pre-filled in the input field; also returned in unattended runs.

    Examples:
        >>> import utility_controller as uc

        >>> count = uc.get_user_int_with_default_value('Number of copies', 3)
        >>> print(count)

    Returns:
        The value entered by the user. 0 (and an error message in cadwork) if the user cancels, so a
        cancel cannot be told apart from an entered 0.
    """

def get_user_double_with_default_value(message: str, default_value: float) -> float:
    """Ask the user to enter a number in the command bar, with a default.

    Shows the prompt in the cadwork command bar with the default pre-filled and blocks the script
    until the user confirms or cancels. When cadwork runs unattended via a plugin or program start
    parameter, nothing is shown and the default is returned. Use
    `utility_controller.get_user_int_with_default_value()` for whole numbers.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Value pre-filled in the input field; also returned in unattended runs.

    Examples:
        >>> import utility_controller as uc

        >>> distance = uc.get_user_double_with_default_value('Distance in mm', 100.0)
        >>> print(distance)

    Returns:
        The value entered by the user. 0.0 (and an error message in cadwork) if the user cancels, so
        a cancel cannot be told apart from an entered 0.
    """

def get_user_string_with_default_value(message: str, default_value: str) -> str:
    """Ask the user to enter text in the command bar, with a default.

    Shows the prompt in the cadwork command bar with the default pre-filled and blocks the script
    until the user confirms or cancels. When cadwork runs unattended via a plugin or program start
    parameter, nothing is shown and the default is returned. Use
    `utility_controller.get_user_string()` when no default is needed.

    Parameters:
        message: Prompt text shown to the user.
        default_value: Text pre-filled in the input field; also returned in unattended runs.

    Examples:
        >>> import utility_controller as uc

        >>> name = uc.get_user_string_with_default_value('Group name', 'Walls')
        >>> if name:
        ...     print(name)

    Returns:
        The text entered by the user. An empty string (and an error message in cadwork) if the user
        cancels.
    """

def get_3d_version_name() -> str:
    """Return the cadwork 3D version name.

    Returns the version as shown to users, as text. For the numeric major version use
    `utility_controller.get_3d_version()`.

    Examples:
        >>> import utility_controller as uc

        >>> print(uc.get_3d_version_name(), uc.get_3d_version())

    Returns:
        The version name as text.
    """

def redirect_python_output_to_logger() -> None:
    """Send Python print output and errors to the cadwork logger.

    Replaces the Python standard output and error streams with logger objects, so print() output and
    tracebacks end up in the cadwork log, and sets the cadwork API log level to Info. Call it once
    at the start of a script. It is safe to call more than once.

    Examples:
        >>> import utility_controller as uc

        >>> uc.redirect_python_output_to_logger()
        >>> print('This line goes to the cadwork log')
    """

def set_navigation_widget_enabled(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the navigation widget in one corner of the 3D view.

    The navigation widget is the small overlay in a corner of the 3D view with view cube, axis triad
    and north arrow. The widget is recreated and the view updated immediately. Use the other
    `set_navigation_widget_*` functions to change its parts and size.

    Parameters:
        position: Corner of the 3D view, e.g.
            cadwork.navigation_widget_subwindow_position.top_right. The value none is rejected:
            nothing changes and an error is logged.
        enabled: True to show the widget, False to hide it.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> corner = cadwork.navigation_widget_subwindow_position.top_right
        >>> uc.set_navigation_widget_enabled(corner, True)
    """

def set_navigation_widget_size(position: navigation_widget_subwindow_position, size: int) -> None:
    """Set the size of the navigation widget in one corner of the 3D view.

    The widget is recreated and the view updated immediately. Show or hide the whole widget with
    `utility_controller.set_navigation_widget_enabled()`.

    Parameters:
        position: Corner of the 3D view, e.g.
            cadwork.navigation_widget_subwindow_position.top_right. The value none is rejected:
            nothing changes and an error is logged.
        size: Widget size. The cadwork settings dialog allows 80 to 200; other values are passed on
            without clamping.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> corner = cadwork.navigation_widget_subwindow_position.top_right
        >>> uc.set_navigation_widget_size(corner, 120)
    """

def set_navigation_widget_north_arrow(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the north arrow of a navigation widget.

    Changes only the north arrow of the widget in the given corner. The widget is recreated and the
    view updated immediately. See also `utility_controller.set_navigation_widget_axis()` and
    `utility_controller.set_navigation_widget_cube()`.

    Parameters:
        position: Corner of the 3D view, e.g.
            cadwork.navigation_widget_subwindow_position.top_right. The value none is rejected:
            nothing changes and an error is logged.
        enabled: True to show the north arrow, False to hide it.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> corner = cadwork.navigation_widget_subwindow_position.bottom_left
        >>> uc.set_navigation_widget_north_arrow(corner, True)
    """

def set_navigation_widget_axis(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the axis triad of a navigation widget.

    Changes only the axis triad of the widget in the given corner. The widget is recreated and the
    view updated immediately. See also `utility_controller.set_navigation_widget_north_arrow()` and
    `utility_controller.set_navigation_widget_cube()`.

    Parameters:
        position: Corner of the 3D view, e.g.
            cadwork.navigation_widget_subwindow_position.top_right. The value none is rejected:
            nothing changes and an error is logged.
        enabled: True to show the axis triad, False to hide it.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> corner = cadwork.navigation_widget_subwindow_position.bottom_right
        >>> uc.set_navigation_widget_axis(corner, False)
    """

def set_navigation_widget_cube(position: navigation_widget_subwindow_position, enabled: bool) -> None:
    """Show or hide the view cube of a navigation widget.

    Changes only the view cube of the widget in the given corner. The widget is recreated and the
    view updated immediately. See also `utility_controller.set_navigation_widget_axis()` and
    `utility_controller.set_navigation_widget_north_arrow()`.

    Parameters:
        position: Corner of the 3D view, e.g.
            cadwork.navigation_widget_subwindow_position.top_right. The value none is rejected:
            nothing changes and an error is logged.
        enabled: True to show the view cube, False to hide it.

    Examples:
        >>> import cadwork
        >>> import utility_controller as uc

        >>> corner = cadwork.navigation_widget_subwindow_position.top_left
        >>> uc.set_navigation_widget_cube(corner, True)
    """

def get_user_edge() -> list[point_3d]:
    """Ask the user to pick an edge or two points in the 3D view.

    Prompts the user in the 3D view to click an existing edge or two points, and blocks the script
    until they pick or abort. Returns an empty list without asking when cadwork runs unattended via
    a plugin or program start parameter. Use `utility_controller.get_user_point()` for a single
    point.

    Examples:
        >>> import utility_controller as uc

        >>> edge = uc.get_user_edge()
        >>> if len(edge) == 2:
        ...     start, end = edge
        ...     print(start.x, start.y, start.z, end.x, end.y, end.z)

    Returns:
        List of two point_3d, the start and end of the picked edge in model units (mm). An empty
        list if the user aborted or no valid edge was picked.
    """
