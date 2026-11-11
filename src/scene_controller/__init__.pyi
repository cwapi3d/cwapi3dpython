"""Scenes: named, organisable views of element subsets.

Manages the collection of saved scenes in the project — their
creation and removal, their membership of elements, their grouping
into folders/tabs, and their activation. Scenes are persistent
named selections; transient visibility belongs to
visualization_controller.
"""

from cadwork.api_types import *

def add_scene(name: str) -> bool:
    """Create a new, empty scene.

    Fails if a scene with this name already exists.

    Parameters:
        name: Name of the new scene.

    Returns:
        True if the scene was created, False if a scene with this name already exists.
    """

def rename_scene(old_name: str, new_name: str) -> bool:
    """Rename a scene.

    Renaming a scene that does not exist changes nothing but still returns True.

    Parameters:
        old_name: Current scene name. Must not be empty.
        new_name: New scene name. Must not be empty.

    Returns:
        True normally, False if either name is empty.
    """

def delete_scene(name: str) -> bool:
    """Delete a scene.

    The elements in the scene are not deleted. Deleting a scene that does not exist changes nothing
    but still returns True.

    Parameters:
        name: Name of the scene to delete. Must not be empty.

    Returns:
        True normally, False if name is empty.
    """

def add_elements_to_scene(name: str, element_id_list: list[ElementId]) -> bool:
    """Add elements to a scene.

    Invalid or deleted element IDs are skipped. An unknown scene name adds nothing.

    Parameters:
        name: Name of an existing scene.
        element_id_list: List of element IDs to add.

    Returns:
        Always True, even if the scene does not exist or no element was added.
    """

def remove_elements_from_scene(name: str, element_id_list: list[ElementId]) -> bool:
    """Remove elements from a scene.

    The scene must exist; check with is_scene_present first. Invalid or deleted element IDs are
    skipped. The elements themselves are not deleted.

    Parameters:
        name: Name of an existing scene.
        element_id_list: List of element IDs to remove.

    Returns:
        True after the elements were removed from the scene.
    """

def get_elements_from_scene(name: str) -> list[ElementId]:
    """Get the IDs of all elements in a scene.

    Parameters:
        name: Name of the scene.

    Returns:
        List of element IDs in the scene; empty list if the scene does not exist.
    """

def activate_scene(name: str) -> bool:
    """Activate a scene.

    Parameters:
        name: Name of an existing scene.

    Returns:
        True if the scene was found and activated, False if no scene has this name.
    """

def clear_errors() -> None:
    """Clear the stored scene error messages."""

def get_scene_list() -> list[str]:
    """Get the names of all scenes.

    Returns:
        List of scene names; empty list if there are none.
    """

def group_scences(scene_names: list[str]) -> UnsignedInt:
    """Move scenes into the same scene group as the first scene.

    The first name defines the target group; the other scenes are moved into it. Names that do not
    exist are skipped. Needs at least two names.

    Parameters:
        scene_names: List of scene names. The first scene's group is the target group.

    Returns:
        Index (0-based) of the target group. 0 if fewer than two names are given or the first scene
        is not found.
    """

def ungroup_scences(group_index: UnsignedInt) -> None:
    """Remove all scenes from a scene group.

    Parameters:
        group_index: 0-based index of the group, as returned by get_group_index_by_name or
            group_scences.
    """

def is_scene_present(name: str) -> bool:
    """Check whether a scene with the given name exists.

    Parameters:
        name: Scene name to look up.

    Returns:
        True if the scene exists, False otherwise.
    """

def set_group_tab_color(scene_group_name: str, red: int, green: int, blue: int, alpha: int) -> None:
    """Set the tab color of a scene group.

    Does nothing if no group has this name.

    Parameters:
        scene_group_name: Name of the scene group.
        red: Red component, 0-255.
        green: Green component, 0-255.
        blue: Blue component, 0-255.
        alpha: Opacity, 0-255 (255 is opaque).
    """

def rename_scene_group(old_name: str, new_name: str) -> None:
    """Rename a scene group.

    Does nothing if no group has the old name.

    Parameters:
        old_name: Current group name.
        new_name: New group name.
    """

def get_group_index_by_name(scene_group_name: str) -> UnsignedInt:
    """Get the index of a scene group by its name.

    The name comparison is case-sensitive.

    Parameters:
        scene_group_name: Name of the scene group.

    Returns:
        0-based group index, or the maximum unsigned 64-bit value (18446744073709551615) if no group
        has this name.
    """

def rename_scene_group_by_index(group_index: UnsignedInt, new_name: str) -> None:
    """Rename a scene group by its index.

    Does nothing if the index does not exist.

    Parameters:
        group_index: 0-based index of the group.
        new_name: New group name.
    """

def group_scences_with_name(scene_names: list[str], group_name: str) -> UnsignedInt:
    """Group scenes together and name the group.

    The first name defines the target group; the other scenes are moved into it. The group is
    renamed to group_name only if the first scene already belongs to a group. Needs at least two
    names; names that do not exist are skipped.

    Parameters:
        scene_names: List of scene names. The first scene's group is the target group.
        group_name: New name of the target group.

    Returns:
        Index (0-based) of the target group. 0 if fewer than two names are given or the first scene
        is not found.
    """
