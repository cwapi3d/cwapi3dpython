# Newly added functions in cadwork 3D API Build >= 2025.0.274

* Added examples to the docstrings for better understanding.
* Corrected several argument types in function signatures.

### Functions machine_controller

#### get_element_hundegger_processings

```python
def get_element_hundegger_processings(element_id: int, hundeggertype: int) -> List[int]:
    """Get Hundegger processing IDs for an element.

    Parameters:
        element_id: The element ID.
        hundeggertype: The Hundegger type.

    Returns:
        List of processing IDs.
    """
```

#### get_element_btl_processings

```python
def get_element_btl_processings(element_id: int, btl_version: int) -> List[int]:
    """Get BTL processing IDs for an element.

    Parameters:
        element_id: The element ID.
        btl_version: The BTL version.

    Returns:
        List of processing IDs.
    """
```

#### get_processing_name

```python
def get_processing_name(reference_element_id: int, processing_id: int) -> str:
    """Get the name of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     name = mc.get_processing_name(element, processing)

    Returns:
        The processing name.
    """
```

#### get_processing_code

```python
def get_processing_code(reference_element_id: int, processing_id: int) -> str:
    """Get the code of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     code = mc.get_processing_code(element, processing)

    Returns:
        The processing code.
    """
```

#### get_processing_points

```python
def get_processing_points(reference_element_id: int, processing_id: int) -> vertex_list:
    """Get the points of a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     points = mc.get_processing_points(element, processing)

    Returns:
        A vertex_list of points.
    """
```

#### get_processing_btl_parameter_set

```python
def get_processing_btl_parameter_set(reference_element_id: int, processing_id: int) -> List[str]:
    """Get the BTL parameter set for a processing.

    Parameters:
        reference_element_id: The reference element ID.
        processing_id: The processing ID.

    Examples:
        >>> import cadwork
        >>> import element_controller as ec
        >>> import machine_controller as mc

        >>> element: int = 123456789
        >>> processings = mc.get_element_btl_processings(element, cadwork.btl_version.btlx_2_1.value)
        >>> for processing in processings:
        >>>     parameters = mc.get_processing_btl_parameter_set(element, processing)

    Returns:
        List of BTL parameter strings.
    """
```

