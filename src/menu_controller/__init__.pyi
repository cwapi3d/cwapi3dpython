"""Custom in-application menus driven by scripts.

Provides the means to surface script-driven choices to the user
through cadwork's native menu UI and to capture the user's
selection. The complement to utility_controller's prompts and
dialogs when a list-of-options interaction fits better than a
modal form.
"""

def display_simple_menu(menu_items: list[str]) -> str:
    """Show a menu with the given entries and wait for the user to pick one.

    The script blocks until the user selects an entry or presses Escape. At most 50 entries are
    shown; further entries are dropped. In a script started with /PLUGIN= or /RUNPROGRAM= no menu is
    shown, a warning is logged and an empty string is returned.

    Parameters:
        menu_items: Entry labels in display order. An empty string adds a blank separator line that
            cannot be selected.

    Examples:
        >>> import menu_controller as mec
        >>> choice = mec.display_simple_menu(['Beam', 'Panel', '', 'Column'])
        >>> if choice == '':
        ...     print('Menu cancelled')
        ... else:
        ...     print(f'Selected: {choice}')

    Returns:
        The label of the selected entry, or an empty string when the user presses Escape or the
        script was started with /PLUGIN= or /RUNPROGRAM=.
    """
