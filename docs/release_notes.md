# Newly added functions, classes, and enums in cadwork 3D API 2025.0.245

### Functions dimension_controller

#### get_dimension_base_format

```python
def get_dimension_base_format(element: int) -> dimension_base_format:
    """get dimension base format

    Parameters:
        element: element

    Returns:
        dimension_base_format
    """

```


### Functions element_controller

#### filter_elements

```python
def filter_elements(elements: List[int], element_filter: element_filter
                    ) -> List[int]:
    """filter elements

    Parameters:
        elements: elements
        element_filter: name_filter

    Example:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_element_filter = cadwork.element_filter()
        >>> your_element_filter.set_name("beam")
        >>> filtered_elements = ec.filter_elements(ec.get_active_identifiable_element_ids(), your_element_filter)
        >>> print(filtered_elements)

    Returns:
        List[int]
    """

```

#### map_elements

```python
def map_elements(elements: List[int], map_query: element_map_query) -> Dict[
    str, List[int]]:
    """map elements

    Parameters:
        elements: elements
        map_query: map_query

    Example:
        >>> import cadwork
        >>> import element_controller as ec
        >>> your_map_query = cadwork.element_map_query()
        >>> your_map_query.set_by_subgroup()
        >>> mapped_items = ec.map_elements(ec.get_active_identifiable_element_ids(), your_map_query)
        >>> print(mapped_items)

    Returns:
        Dict[str, List[int]]
    """

```

#### cast_ray_and_get_element_intersections

```python
def cast_ray_and_get_element_intersections(elements: List[int],
                                           ray_start_position: point_3d, ray_end_position: point_3d, radius: float
                                           ) -> hit_result:
    """cast ray and get element intersections
    Parameters:
        elements: elements
        ray_start_position: ray_start_position
        ray_end_position: ray_end_position
        radius: radius

    Example:
        >>> import cadwork
        >>> import element_controller as ec
        >>> ray_start = cadwork.point_3d(0, 0, 0)
        >>> ray_end = cadwork.point_3d(1000, 0, 0)
        >>> hit_result = ec.cast_ray_and_get_element_intersections(ec.get_active_identifiable_element_ids(), ray_start, ray_end, 40.0)
        >>> print(hits.get_hit_element_ids())
        >>> for element in hits.get_hit_element_ids():
        >>>     print(f"ElementID {element}: {hits.get_hit_vertices_by_element(element)}")
        >>>     for pos in hits.get_hit_vertices_by_element(element):
        >>>         ec.create_node(pos)

    Returns:
        hit_result
    """

```


### Functions file_controller

#### export_dxf_file

```python
def export_dxf_file(file_path: str, dxf_layer_format_type:
dxf_layer_format_type, dxf_export_version: dxf_export_version) -> bool:
    """export dxf file

    Parameters:
        file_path: file_path
        dxf_layer_format_type: dxf_layer_format_type
        dxf_export_version: dxf_export_version

    Returns:
        bool
    """

```

#### export_dstv_file

```python
def export_dstv_file(file_path: str) -> bool:
    """export dstv file

    Parameters:
        file_path: file_path

    Returns:
        bool
    """

```

### Functions utility_controller

#### get_3d_version_name

```python
def get_3d_version_name() -> str:
    """get 3d version name

    Returns:
        str
    """

```

#### redirect_python_output_to_logger

```python
def redirect_python_output_to_logger() -> None:
    """redirect python output to logger.
    This function is used to redirect the output of the Python interpreter to the logger.
    This is useful for debugging and logging purposes.

    Returns:
        None
    """

```

### Classes cadwork

#### bim_team_upload_result

```python
class bim_team_upload_result:
    """bim team upload result
    """

    def __init__(self):
        """
        Instance of the bim_team_upload_result class.

        Attributes:
            upload_result_code (bim_team_upload_result_code): The result code of the upload.
            share_link (str): The share link for the uploaded BIM team result.
        """
        self.upload_result_code = bim_team_upload_result_code.ok
        self.share_link = ''

```

### Classes cadwork

#### bim_team_upload_result_code

```python
@unique
class bim_team_upload_result_code(IntEnum):
    """bim team upload result code

    Examples:
        >>> cadwork.bim_team_upload_result_code.ok
        ok
    """
    ok = 0
    """"""
    error_general_error = 1
    """"""
    error_too_many_models = 2
    """"""
    error_insufficient_storage = 3
    """"""
    error_invalid_project_id = 4
    """"""
    error_authentication_failed = 5
    """"""

    def __int__(self) -> int:
        return self.value

```

### Classes cadwork

#### dimension_base_format

```python
@unique
class dimension_base_format(IntEnum):
    """ Enumeration for dimension base format.

    Examples:
        >>> cadwork.dimension_base_format.sum_only

    """
    none = 0
    """"""
    distance_only = 1
    """"""
    sum_only = 2
    """"""
    distance_and_sum = 3
    """"""
    sum_moved = 4
    """"""

    def __int__(self) -> int:
        return self.value

```

### Classes cadwork

#### dxf_export_version

```python
@unique
class dxf_export_version(IntEnum):
    """ Enumeration for DXF export version.

    Examples:
        >>> cadwork.dxf_export_version.auto_cad_r27

    """
    auto_cad_r10 = 0
    """"""
    auto_cad_r27 = 1
    """"""

    def __int__(self) -> int:
        return self.value

```

### Classes cadwork

#### dxf_layer_format_type

```python
@unique
class dxf_layer_format_type(IntEnum):
    """ Enumeration for DXF layer format type.

    Examples:
        >>> cadwork.dxf_layer_format_type.color

    """
    all_in_no_1 = 0
    """"""
    color = 1
    """"""
    material = 2
    """"""
    name = 3
    """"""
    group = 4
    """"""
    subgroup = 5
    """"""

    def __int__(self) -> int:
        return self.value

```


### Classes cadwork

#### element_filter

```python
class element_filter:

    def set_name(self, name: str) -> None:
        """set name

        Parameters:
            name: name

        Returns:
            None
        """

    def set_group(self, group: str) -> None:
        """set group

        Parameters:
            group: group

        Returns:
            None
        """

    def set_subgroup(self, subgroup: str) -> None:
        """set subgroup

        Parameters:
            subgroup: subgroup

        Returns:
            None
        """

    def set_comment(self, comment: str) -> None:
        """set comment

        Parameters:
            comment: comment

        Returns:
            None
        """

    def set_user_attribute(self, number: int, user_attribute: str) -> None:
        """set user attribute

        Parameters:
            number: number
            user_attribute: user_attribute

        Returns:
            None
        """

    def set_sku(self, sku: str) -> None:
        """set sku

        Parameters:
            sku: sku

        Returns:
            None
        """

    def set_production_number(self, production_number: int) -> None:
        """set production number

        Parameters:
            production_number: production_number

        Returns:
            None
        """

    def set_part_number(self, part_number: int) -> None:
        """set part number

        Parameters:
            part_number: part_number

        Returns:
            None
        """

```


### Classes cadwork

#### element_map_query

```python
class element_map_query:

    def set_by_name(self) -> None:
        """set by name

        Returns:
            None
        """

    def set_by_group(self) -> None:
        """set by group

        Returns:
            None
        """

    def set_by_subgroup(self) -> None:
        """set by subgroup

        Returns:
            None
        """

    def set_by_comment(self) -> None:
        """set by comment

        Returns:
            None
        """

    def set_by_user_attribute(self, number: int) -> None:
        """set by user attribute

        Parameters:
            number: number

        Returns:
            None
        """

    def set_by_sku(self) -> None:
        """set by sku

        Returns:
            None
        """

    def set_by_production_number(self) -> None:
        """set by production number

        Returns:
            None
        """

    def set_by_part_number(self) -> None:
        """set by part number

        Returns:
            None
        """

    def set_by_building(self) -> None:
        """set by building

        Returns:
            None
        """

    def set_by_storey(self) -> None:
        """set by storey

        Returns:
            None
        """

```


### Classes cadwork

#### hit_result

```python
class hit_result:

    def get_hit_element_ids(self) -> List[int]:
        """get hit element ids

        Returns:
            List[int]
        """

    def get_hit_vertices_by_element(self, element_id: int) -> List[point_3d]:
        """get hit vertices by element

        Parameters:
            element_id: element_id

        Returns:
            List[point_3d]
        """

```