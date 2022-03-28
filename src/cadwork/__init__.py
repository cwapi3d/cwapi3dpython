
class layer_settings():
    def __init__(self) -> None:
        pass

class extended_settings():
    def __init__(self) -> None:
        pass
    
class output_type():
    def __init__(self) -> None:
        pass
    
class process_type():
    def __init__(self) -> None:
        pass

class element_type():
    def __init__(self) -> None:
        pass

class element_module_properties():
    def __init__(self) -> None:
        pass


class point_3d:
    def __init__(self, x, y, z)->None:
        self.x = x
        self.y = y
        self.z = z

def cross(self, point_3d) -> point_3d:
    """_summary_

    Args:
        point_3d (_type_): _description_

    Returns:
        point_3d: _description_
    """

def distance(self, point_3d) -> float:
    """_summary_

    Args:
        point_3d (_type_): _description_

    Returns:
        float: _description_
    """

def dot(self, point_3d) -> point_3d:
    """_summary_

    Args:
        point_3d (_type_): _description_

    Returns:
        point_3d: _description_
    """
    
def magnitude(self) -> point_3d:
    """_summary_

    Returns:
        point_3d: _description_
    """

def normalized(self) -> point_3d:
    """_summary_

    Returns:
        point_3d: _description_
    """
