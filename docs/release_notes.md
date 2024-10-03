## New Items
### Functions element_controller
#### unjoin_elements

```python
def unjoin_elements(element_id_list: List[int]) ->bool:
    """unjoin elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        bool
    """

```

#### unjoin_top_level_elements

```python
def unjoin_top_level_elements(element_id_list: List[int]) ->bool:
    """unjoin top level elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        bool
    """

```

#### set_element_group_single_select_mode

```python
def set_element_group_single_select_mode() ->None:
    """set element group single select mode

    Returns:
        None
    """

```

#### set_element_group_multi_select_mode

```python
def set_element_group_multi_select_mode() ->None:
    """set element group multi select mode

    Returns:
        None
    """

```

#### get_elements_in_collision

```python
def get_elements_in_collision(element: int) ->List[int]:
    """get elements in collision

    Parameters:
        element: element

    Returns:
        List[int]
    """

```

## New Items
### Functions file_controller
#### export_step_file_cut_drillings

```python
def export_step_file_cut_drillings(elements: List[int], file_path: str, scale_factor: float, version: int,
                                   text_mode: bool, imperial_units: bool) -> None:
    """Exports a STEP file with extruded drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        version: version
        text_mode: text_mode
        imperial_units: imperial_units

    Returns:
        None
    """

```

#### export_sat_file_cut_drillings

```python
def export_sat_file_cut_drillings(elements: List[int], file_path: str,
    scale_factor: float, binary: bool, version: int) ->None:
    """export sat file cut drillings

    Parameters:
        elements: elements
        file_path: file_path
        scale_factor: scale_factor
        binary: binary
        version: version

    Returns:
        None
    """

```

#### upload_to_bim_team_and_create_share_link

```python
def upload_to_bim_team_and_create_share_link(elements: None
    ) ->bim_team_upload_result:
    """upload to bim team and create share link

    Parameters:
        elements: elements

    Returns:
        bim_team_upload_result
    """

```

## New Items
### Functions visualization_controller
#### enter_working_plane

```python
def enter_working_plane(plane_normal: point_3d, plane_origin: point_3d) ->None:
    """enter working plane

    Parameters:
        plane_normal: plane_normal
        plane_origin: plane_origin

    Returns:
        None
    """

```

