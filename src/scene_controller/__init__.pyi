from typing import List

def get_last_error(error_code: int) -> str:
    """Gets the last error

    Parameters:
        error_code: error_code

    Returns:
        error string
    """

def add_scene(name: str) -> bool:
    """Adds a new scene

    Parameters:
        name: name

    Returns:
        did operation succeed
    """

def rename_scene(old_name: str, new_name: str) -> bool:
    """Renames a scene

    Parameters:
        old_name: old_name
        new_name: new_name

    Returns:
        did operation succeed
    """

def delete_scene(name: str) -> bool:
    """Deletes a scene

    Parameters:
        name: name

    Returns:
        did operation succeed
    """

def add_elements_to_scene(name: str, element_i_ds: List[int]) -> bool:
    """Adds elements to a scene

    Parameters:
        name: name
        element_i_ds: element_i_ds

    Returns:
        did operation succeed
    """

def remove_elements_from_scene(name: str, element_i_ds: List[int]) -> bool:
    """Removes elements from a scene

    Parameters:
        name: name
        element_i_ds: element_i_ds

    Returns:
        did operation succeed
    """

def get_elements_from_scene(name: str) -> List[int]:
    """Gets the elements from a scene

    Parameters:
        name: name

    Returns:
        element ID list
    """

def activate_scene(name: str) -> bool:
    """Activates a scene

    Parameters:
        name: name

    Returns:
        did operation succeed
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def get_scene_list() -> List[str]:
    """get scene list

    Returns:
        List[str]
    """

def group_scences(a0: List[str]) -> int:
    """group scences

    Parameters:
        a0: a0

    Returns:
        int
    """

def ungroup_scences(a0: int) -> None:
    """ungroup scences

    Parameters:
        a0: a0

    Returns:
        None
    """

def is_scene_present(name: str) -> bool:
    """Queries of scene with name is present

    Parameters:
        name: name

    Returns:
        presence of scene
    """

def set_group_tab_color(scene_group_name: str, red: int, green: int, blue: int) -> None:
    """set group tab color

    Parameters:
        scene_group_name: scene_group_name
        red: red
        green: green
        blue: blue

    Returns:
        None
    """

def rename_scene_group(old_name: str, new_name: str) -> None:
    """rename scene group

    Parameters:
        old_name: old_name
        new_name: new_name

    Returns:
        None
    """

def get_group_index_by_name(scene_group_name: str) -> int:
    """get group index by name

    Parameters:
        scene_group_name: scene_group_name

    Returns:
        int
    """

def rename_scene_group_by_index(group_index: int, new_name: str) -> None:
    """rename scene group by index

    Parameters:
        group_index: group_index
        new_name: new_name

    Returns:
        None
    """

def group_scences_with_name(a0: List[str], a1: str) -> int:
    """group scences with name

    Parameters:
        a0: a0
        a1: a1

    Returns:
        int
    """
