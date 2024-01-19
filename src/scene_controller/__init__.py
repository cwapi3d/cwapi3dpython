from typing import List

def get_last_error(error_code: int) -> str:
    """get last error
    Args:
        error_code ( int): error_code

    Returns:
        strerror string
    """

def add_scene(name: str) -> bool:
    """add scene
    Args:
        name ( str): name

    Returns:
        booldid operation succeed
    """

def rename_scene(old_name: str, new_name: str) -> bool:
    """rename scene
    Args:
        old_name ( str): old_name
        new_name ( str): new_name

    Returns:
        booldid operation succeed
    """

def delete_scene(name: str) -> bool:
    """delete scene
    Args:
        name ( str): name

    Returns:
        booldid operation succeed
    """

def add_elements_to_scene(name: str, element_i_ds: List[int]) -> bool:
    """add elements to scene
    Args:
        name ( str): name
        element_i_ds ( List[int]): element_i_ds

    Returns:
        booldid operation succeed
    """

def remove_elements_from_scene(name: str, element_i_ds: List[int]) -> bool:
    """remove elements from scene
    Args:
        name ( str): name
        element_i_ds ( List[int]): element_i_ds

    Returns:
        booldid operation succeed
    """

def get_elements_from_scene(name: str) -> List[int]:
    """get elements from scene
    Args:
        name ( str): name

    Returns:
        List[int]element ID list
    """

def activate_scene(name: str) -> bool:
    """activate scene
    Args:
        name ( str): name

    Returns:
        booldid operation succeed
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def get_scene_list() -> List[str]:
    """get scene list
    Args:

    Returns:
        List[str]
    """

