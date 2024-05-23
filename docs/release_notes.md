# change log build 30.498.0

## New Items

### Functions dimension_controller

#### get_segment_direction

```python
def get_segment_direction(element: int, segment_index: int) ->point_3d:
    """get segment direction

    Parameters:
        element: element
        segment_index: segment_index

    Returns:
        point_3d
    """

```

## New Items

### Functions element_controller

#### create_truncated_cone_beam_points

```python
def create_truncated_cone_beam_points(start_diameter: float, end_diameter:
    float, p1: point_3d, p2: point_3d, p3: point_3d) ->int:
    """create truncated cone beam points

    Parameters:
        start_diameter: start_diameter
        end_diameter: end_diameter
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

```

#### create_truncated_cone_beam_vectors

```python
def create_truncated_cone_beam_vectors(start_diameter: float, end_diameter:
    float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) ->int:
    """create truncated cone beam vectors

    Parameters:
        start_diameter: start_diameter
        end_diameter: end_diameter
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

```

#### create_spline_line

```python
def create_spline_line(spline_points: None) ->int:
    """create spline line

    Parameters:
        spline_points: spline_points

    Returns:
        int
    """

```

## New Items

### Functions utility_controller

#### get_user_int_with_default_value

```python
def get_user_int_with_default_value(message: str, default_value: int) ->int:
    """get user int with default value

    Parameters:
        message: message
        default_value: default_value

    Returns:
        int
    """

```

#### get_user_double_with_default_value

```python
def get_user_double_with_default_value(message: str, default_value: float
    ) ->float:
    """get user double with default value

    Parameters:
        message: message
        default_value: default_value

    Returns:
        float
    """

```

#### get_user_string_with_default_value

```python
def get_user_string_with_default_value(message: str, default_value: str) ->str:
    """get user string with default value

    Parameters:
        message: message
        default_value: default_value

    Returns:
        str
    """

```

## New Items

### Classes cadwork

#### multi_layer_type

```python
@unique
class multi_layer_type(IntEnum):
    """multi layer type

    Examples:
        >>> cadwork.multi_layer_type.undefined
        undefined
    """
    undefined = 0
    """"""
    structure = 1
    """"""
    panel = 2
    """"""
    lathing = 3
    """"""
    air = 4
    """"""
    covering = 5
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items

### Classes cadwork

#### ifc_2x3_element_type

```python
class ifc_2x3_element_type:
    def is_ifc_element_assembly(self) ->bool:
        """is ifc element assembly

        Returns:
            bool
        """

    def set_ifc_element_assembly(self) ->None:
        """set ifc element assembly

        Returns:
            None
        """

```