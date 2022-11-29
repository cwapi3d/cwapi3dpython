from typing import List


def add_scene(name: str) -> bool:
    """

    Args:
        name (str): scene name

    Returns:
        bool: result
    """


def rename_scene(old_name: str, new_name: str) -> bool:
    """

    Args:
        old_name (str): old scene name
        new_name (str): new scene name

    Returns:
        bool: result
    """


def delete_scene(name: str) -> bool:
    """

    Args:
        name (str): name

    Returns:
        bool: result
    """


def add_elements_to_scene(name: str, elements: List[int]) -> bool:
    """

    Args:
        name (str): name
        elements (List[int]): element IDs

    Returns:
        bool: result
    """


def remove_elements_from_scene(name: str, elements: List[int]) -> bool:
    """

    Args:
        name (str): name
        elements (List[int]): element IDs

    Returns:
        bool: result
    """


def get_elements_from_scene(name: str) -> List[int]:
    """

    Args:
        name (str): name

    Returns:
        List[int]: element IDs
    """


def activate_scene(name: str) -> bool:
    """

    Args:
        name (str): name

    Returns:
        bool: result
    """


def get_scene_list() -> List[str]:
    """get list of scenes in use

    Returns:
        List[str]: scenes
    """
