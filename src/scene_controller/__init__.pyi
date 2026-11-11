"""Scenes: named, organisable views of element subsets.

Manages the collection of saved scenes in the project — their
creation and removal, their membership of elements, their grouping
into folders/tabs, and their activation. Scenes are persistent
named selections; transient visibility belongs to
visualization_controller.
"""

from cadwork.api_types import *

def add_scene(name: str) -> bool:
    """Create a new, empty scene in the active document.

    Scenes are named element collections shown as tabs in the scene bar. The new scene is empty and,
    like every new scene, starts in its own scene group. If a scene with exactly this name already
    exists nothing is created. Fill the scene with `scene_controller.add_elements_to_scene()`.

    Parameters:
        name: Name of the new scene. The comparison with existing scene names is case-sensitive.

    Examples:
        >>> import scene_controller as sc

        >>> if sc.add_scene('Walls'):
        ...     print('scene created')
        ... else:
        ...     print('scene already exists')

    Returns:
        True if the scene was created, False if a scene with this name already exists.
    """

def rename_scene(old_name: str, new_name: str) -> bool:
    """Rename a scene.

    Every scene whose name matches `old_name` exactly (case-sensitive) gets the new name. Nothing
    changes, but True is still returned, if no scene has the old name. The new name is not checked
    for duplicates. Check for the scene first with `scene_controller.is_scene_present()`.

    Parameters:
        old_name: Current scene name, e.g. from `scene_controller.get_scene_list()`. Must not be
            empty.
        new_name: New scene name. Must not be empty.

    Examples:
        >>> import scene_controller as sc

        >>> if sc.is_scene_present('Walls'):
        ...     sc.rename_scene('Walls', 'Ground floor walls')

    Returns:
        True normally, False if either name is empty (nothing is renamed then).
    """

def delete_scene(name: str) -> bool:
    """Delete a scene from the active document.

    Only the scene is removed; the elements it contained are not deleted. The scene name is matched
    without regard to case, and only the first match is deleted. Deleting a scene that does not
    exist changes nothing but still returns True. Use `scene_controller.is_scene_present()` to check
    beforehand.

    Parameters:
        name: Name of the scene to delete, e.g. from `scene_controller.get_scene_list()`. Must not
            be empty.

    Examples:
        >>> import scene_controller as sc

        >>> if sc.is_scene_present('Temporary'):
        ...     sc.delete_scene('Temporary')

    Returns:
        True normally, False if name is empty.
    """

def add_elements_to_scene(name: str, element_id_list: list[ElementId]) -> bool:
    """Add elements to an existing scene.

    Element IDs that are invalid or not found in the document are skipped. If no scene has this
    exact name (case-sensitive), nothing is added; create it first with
    `scene_controller.add_scene()`. The call returns True in every case, so verify with
    `scene_controller.get_elements_from_scene()` if needed.

    Parameters:
        name: Name of an existing scene, e.g. from `scene_controller.get_scene_list()`.
        element_id_list: List of element IDs to add, e.g. from
            `element_controller.get_active_identifiable_element_ids()`.

    Examples:
        >>> import element_controller as ec
        >>> import scene_controller as sc

        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> if not sc.is_scene_present('Walls'):
        ...     sc.add_scene('Walls')
        >>> sc.add_elements_to_scene('Walls', element_ids)

    Returns:
        Always True, even if the scene does not exist or no element was added.
    """

def remove_elements_from_scene(name: str, element_id_list: list[ElementId]) -> bool:
    """Remove elements from a scene without deleting them.

    Only the scene membership is removed; the elements stay in the model. Invalid element IDs and
    elements not found in the document are skipped. The scene must exist: the call does not check
    for a missing scene, so verify with `scene_controller.is_scene_present()` first. Add elements
    with `scene_controller.add_elements_to_scene()`.

    Parameters:
        name: Name of an existing scene, e.g. from `scene_controller.get_scene_list()`.
        element_id_list: List of element IDs to remove, e.g. from
            `scene_controller.get_elements_from_scene()`.

    Examples:
        >>> import element_controller as ec
        >>> import scene_controller as sc

        >>> if sc.is_scene_present('Walls'):
        ...     element_ids = ec.get_active_identifiable_element_ids()
        ...     sc.remove_elements_from_scene('Walls', element_ids)

    Returns:
        True after the removal was performed.
    """

def get_elements_from_scene(name: str) -> list[ElementId]:
    """Get the IDs of all elements in a scene.

    Reads the current content of the scene; the active selection and visibility of the elements do
    not matter. The name must match a scene exactly (case-sensitive). Fill a scene with
    `scene_controller.add_elements_to_scene()`.

    Parameters:
        name: Name of the scene, e.g. from `scene_controller.get_scene_list()`.

    Examples:
        >>> import scene_controller as sc

        >>> element_ids = sc.get_elements_from_scene('Walls')
        >>> print(len(element_ids), 'elements in scene')

    Returns:
        List of element IDs in the scene. Empty list if the scene does not exist or is empty.
    """

def activate_scene(name: str) -> bool:
    """Show a scene, as if its tab had been clicked.

    Displays the scene in the 3D view. The scene name must match exactly
    (case-sensitive). Returns False without any change if no scene has this name. Scene names come
    from `scene_controller.get_scene_list()`.

    Parameters:
        name: Name of an existing scene.

    Examples:
        >>> import scene_controller as sc

        >>> if not sc.activate_scene('Walls'):
        ...     print('scene not found')

    Returns:
        True if the scene was found and activated, False if no scene has this name.
    """

def clear_errors() -> None:
    """Clear the stored scene error messages.

    Empties the error stack that belongs to `scene_controller`. Use it before a series of scene
    calls so that earlier errors are not read later.

    Examples:
        >>> import scene_controller as sc

        >>> sc.clear_errors()
    """

def get_scene_list() -> list[str]:
    """Get the names of all scenes in the active document.

    The names are ordered by the position of the scenes in the scene bar. Use the names with the
    other `scene_controller` functions, for example `scene_controller.activate_scene()`.

    Examples:
        >>> import scene_controller as sc

        >>> for scene_name in sc.get_scene_list():
        ...     print(scene_name, len(sc.get_elements_from_scene(scene_name)))

    Returns:
        List of scene names; empty list if there are none.
    """

def group_scences(scene_names: list[str]) -> UnsignedInt:
    """Move scenes into the scene group of the first scene.

    Scene groups are the folders in the scene bar that bundle several scene tabs; every new scene
    starts in its own group. The first name defines the target group and the other scenes are moved
    into it. Names that do not exist are skipped. The group keeps its current name; use
    `scene_controller.group_scences_with_name()` to name it in the same call. Undo it with
    `scene_controller.ungroup_scences()`.

    Parameters:
        scene_names: List of at least two scene names, e.g. from
            `scene_controller.get_scene_list()`. The group of the first scene is the target group.

    Examples:
        >>> import scene_controller as sc

        >>> group_index = sc.group_scences(['Walls', 'Floors', 'Roof'])
        >>> sc.rename_scene_group_by_index(group_index, 'Building')

    Returns:
        0-based index of the target group. 0 if fewer than two names are given or the first scene
        does not exist, so the value 0 alone does not prove success.
    """

def ungroup_scences(group_index: UnsignedInt) -> None:
    """Take all scenes out of a scene group.

    The scenes are kept and are no longer bundled in that group. An index that does not exist is
    ignored. Find the index with `scene_controller.get_group_index_by_name()` or from the return
    value of `scene_controller.group_scences()`.

    Parameters:
        group_index: 0-based index of the scene group.

    Examples:
        >>> import scene_controller as sc

        >>> group_index = sc.get_group_index_by_name('Building')
        >>> if group_index != 18446744073709551615:
        ...     sc.ungroup_scences(group_index)
    """

def is_scene_present(name: str) -> bool:
    """Check whether a scene with the given name exists.

    Call it before functions that need an existing scene, for example
    `scene_controller.remove_elements_from_scene()`. The name must match exactly (case-sensitive).

    Parameters:
        name: Scene name to look up.

    Examples:
        >>> import scene_controller as sc

        >>> if not sc.is_scene_present('Walls'):
        ...     sc.add_scene('Walls')

    Returns:
        True if the scene exists, False otherwise.
    """

def set_group_tab_color(scene_group_name: str, red: int, green: int, blue: int, alpha: int) -> None:
    """Set the tab color of a scene group.

    Scene groups are the folders in the scene bar that bundle scene tabs. Every group with exactly
    this name (case-sensitive) gets the color. Unnamed groups cannot be addressed, and nothing
    happens if no group has the name. Name a group with `scene_controller.rename_scene_group()` or
    `scene_controller.group_scences_with_name()`.

    Parameters:
        scene_group_name: Name of an existing, non-empty scene group.
        red: Red component, 0-255.
        green: Green component, 0-255.
        blue: Blue component, 0-255.
        alpha: Opacity, 0-255 (255 is opaque).

    Examples:
        >>> import scene_controller as sc

        >>> sc.set_group_tab_color('Building', 200, 60, 60, 255)
    """

def rename_scene_group(old_name: str, new_name: str) -> None:
    """Rename a scene group by its current name.

    Every group with exactly the old name (case-sensitive) is renamed. Nothing happens if no group
    has that name or if the old name is empty. To address a group by position use
    `scene_controller.rename_scene_group_by_index()`.

    Parameters:
        old_name: Current non-empty group name.
        new_name: New group name.

    Examples:
        >>> import scene_controller as sc

        >>> sc.rename_scene_group('Building', 'Building A')
    """

def get_group_index_by_name(scene_group_name: str) -> UnsignedInt:
    """Get the index of a scene group from its name.

    The name is compared case-sensitively. Use the index with `scene_controller.ungroup_scences()`
    or `scene_controller.rename_scene_group_by_index()`. Compare the result with the not-found value
    before using it as an index.

    Parameters:
        scene_group_name: Name of the scene group.

    Examples:
        >>> import scene_controller as sc

        >>> group_index = sc.get_group_index_by_name('Building')
        >>> if group_index == 18446744073709551615:
        ...     print('no such group')

    Returns:
        0-based group index, or the maximum unsigned 64-bit value (18446744073709551615) if no group
        has this name.
    """

def rename_scene_group_by_index(group_index: UnsignedInt, new_name: str) -> None:
    """Rename a scene group by its index.

    Does nothing if no group exists at the index. The index comes from
    `scene_controller.get_group_index_by_name()` or from `scene_controller.group_scences()`.

    Parameters:
        group_index: 0-based index of the group.
        new_name: New group name.

    Examples:
        >>> import scene_controller as sc

        >>> group_index = sc.get_group_index_by_name('Building')
        >>> sc.rename_scene_group_by_index(group_index, 'Building A')
    """

def group_scences_with_name(scene_names: list[str], group_name: str) -> UnsignedInt:
    """Move scenes into the group of the first scene and name that group.

    The first name defines the target group and the other scenes are moved into it; names that do
    not exist are skipped. The target group is renamed to `group_name`. Needs at least two names.
    For grouping without renaming use `scene_controller.group_scences()`.

    Parameters:
        scene_names: List of at least two scene names, e.g. from
            `scene_controller.get_scene_list()`. The group of the first scene is the target group.
        group_name: New name of the target group.

    Examples:
        >>> import scene_controller as sc

        >>> group_index = sc.group_scences_with_name(['Walls', 'Floors'], 'Building')
        >>> sc.set_group_tab_color('Building', 200, 60, 60, 255)

    Returns:
        0-based index of the target group. 0 if fewer than two names are given or the first scene
        does not exist.
    """
