from typing import List
from cadwork.api_types import *

def add_scene(name: str) -> bool:
    """Adds a new scene.

    Parameters:
        name: The scene name.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def rename_scene(old_name: str, new_name: str) -> bool:
    """Renames a scene.

    Parameters:
        old_name: The old scene name.
        new_name: The new scene name.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def delete_scene(name: str) -> bool:
    """Deletes a scene.

    Parameters:
        name: The scene name.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def add_elements_to_scene(name: str, element_id_list: List[ElementId]) -> bool:
    """Adds elements to a scene.

    Parameters:
        name: The scene name.
        element_id_list:: The element id list.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def remove_elements_from_scene(name: str, element_id_list: List[ElementId]) -> bool:
    """Removes elements from a scene.

    Parameters:
        name: The scene name.
        element_id_list:: The element id list.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def get_elements_from_scene(name: str) -> List[ElementId]:
    """Gets the elements from a scene.

    Parameters:
        name: The scene name.

    Returns:
        The element id list.
    """

def activate_scene(name: str) -> bool:
    """Activates a scene.

    Parameters:
        name: The scene name.

    Returns:
        True if the operation succeeded, false otherwise.
    """

def clear_errors() -> None:
    """Clears all errors.
    """

def get_scene_list() -> List[str]:
    """Gets the list of scenes.

    Returns:
        The list of scene names.
    """

def group_scences(scene_names: List[str]) -> UnsignedInt:
    """Groups the scenes to a scene group.

    Parameters:
        scene_names: The scene names.

    Returns:
        The index of the new group.
    """

def ungroup_scences(group_index: UnsignedInt) -> None:
    """Deletes the group of scenes.

    Parameters:
        group_index: The index of the group.
    """

def is_scene_present(name: str) -> bool:
    """Checks if a scene is present.

    Parameters:
        name: The name of the scene to check.

    Returns:
        True if the scene is present, false otherwise.
    """

def set_group_tab_color(scene_group_name: str, red: int, green: int, blue: int, alpha: int) -> None:
    """Sets the group tab color.

    Parameters:
        scene_group_name: The name of the scene group.
        red: Red component.
        green: Green component.
        blue: Blue component.
    """

def rename_scene_group(old_name: str, new_name: str) -> None:
    """Renames a scene group.

    Parameters:
        old_name: The old scene group name.
        new_name: The new scene group name.
    """

def get_group_index_by_name(scene_group_name: str) -> UnsignedInt:
    """Gets the index of a scene group by its name.

    Parameters:
        scene_group_name: The group name.

    Returns:
        The index of the group, or a maximum uint64_t if not found.
    """

def rename_scene_group_by_index(group_index: UnsignedInt, new_name: str) -> None:
    """Renames a scene group by its index.

    Parameters:
        group_index: The index of the group.
        new_name: The new scene group name.
    """

def group_scences_with_name(scene_names: List[str], group_name: str) -> UnsignedInt:
    """Groups the scenes to a scene group and sets the name of the new group.

    Parameters:
        scene_names: The scene names to group.
        group_name: The name of the new group.

    Returns:
        The index of the new group.
    """
