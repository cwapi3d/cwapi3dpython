from typing import List


def get_last_error(error_code: int) -> str:
    """Gets the last error

    Args:
        error_code: error_code

    Returns:
        error string (str)
    """


def add_scene(name: str) -> bool:
    """Adds a new scene

    Args:
        name: name

    Returns:
        did operation succeed (bool)
    """


def rename_scene(old_name: str, new_name: str) -> bool:
    """Renames a scene

    Args:
        old_name: old_name
        new_name: new_name

    Returns:
        did operation succeed (bool)
    """


def delete_scene(name: str) -> bool:
    """Deletes a scene

    Args:
        name: name

    Returns:
        did operation succeed (bool)
    """


def add_elements_to_scene(name: str, element_i_ds: List[int]) -> bool:
    """Adds elements to a scene

    Args:
        name: name
        element_i_ds: element_i_ds

    Returns:
        did operation succeed (bool)
    """


def remove_elements_from_scene(name: str, element_i_ds: List[int]) -> bool:
    """Removes elements from a scene

    Args:
        name: name
        element_i_ds: element_i_ds

    Returns:
        did operation succeed (bool)
    """


def get_elements_from_scene(name: str) -> List[int]:
    """Gets the elements from a scene

    Args:
        name: name

    Returns:
        element ID list (List[int])
    """


def activate_scene(name: str) -> bool:
    """Activates a scene

    Args:
        name: name

    Returns:
        did operation succeed (bool)
    """


def clear_errors() -> None:
    """clear errors

    """


def get_scene_list() -> List[str]:
    """get scene list

    Returns:
        List[str]
    """


def group_scences(a0: List[str]) -> int:
    """group scences

    Args:
        a0: a0

    Returns:
        int
    """


def ungroup_scences(a0: int) -> None:
    """ungroup scences

    Args:
        a0 : a0

    """
