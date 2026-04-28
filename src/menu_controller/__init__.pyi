"""Custom in-application menus driven by scripts.

Provides the means to surface script-driven choices to the user
through cadwork's native menu UI and to capture the user's
selection. The complement to utility_controller's prompts and
dialogs when a list-of-options interaction fits better than a
modal form.
"""


def display_simple_menu(menu_items: list[str]) -> str:
    """Displays a simple menu.

    Parameters:
        menu_items: The menu items.

    Returns:
        The selected menu item.
    """

