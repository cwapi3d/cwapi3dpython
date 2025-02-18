## New Items
### Functions attribute_controller
#### get_standard_element_material_id

```python
def get_standard_element_material_id(element_id: int) ->int:
    """get standard element material id

    Parameters:
        element_id: element_id

    Returns:
        int
    """

```

## New Items
### Functions dimension_controller
#### get_total_dimension

```python
def get_total_dimension(element: int) ->bool:
    """get total dimension

    Parameters:
        element: element

    Returns:
        bool
    """

```

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

#### get_text_object_options

```python
def get_text_object_options(element: int) ->text_object_options:
    """get text object options

    Parameters:
        element: element

    Returns:
        text_object_options
    """

```

#### get_is_element_group_single_select_mode

```python
def get_is_element_group_single_select_mode() ->bool:
    """get is element group single select mode

    Returns:
        bool
    """

```

#### get_is_element_group_multi_select_mode

```python
def get_is_element_group_multi_select_mode() ->bool:
    """get is element group multi select mode

    Returns:
        bool
    """

```

#### apply_image_to_surface

```python
def apply_image_to_surface(element: int, image_file_path: str, p1: point_3d,
    p2: point_3d) ->bool:
    """apply image to surface

    Parameters:
        element: element
        image_file_path: image_file_path
        p1: p1
        p2: p2

    Returns:
        bool
    """

```

#### set_shoulder_options

```python
def set_shoulder_options(options: None) ->None:
    """set shoulder options

    Parameters:
        options: options

    Returns:
        None
    """

```

#### set_heel_shoulder_options

```python
def set_heel_shoulder_options(options: None) ->None:
    """set heel shoulder options

    Parameters:
        options: options

    Returns:
        None
    """

```

#### set_double_shoulder_options

```python
def set_double_shoulder_options(options: None) ->None:
    """set double shoulder options

    Parameters:
        options: options

    Returns:
        None
    """

```

#### cut_shoulder

```python
def cut_shoulder(element_id_list: List[int], connecting_element_id_list:
    List[int]) ->None:
    """cut shoulder

    Parameters:
        element_id_list: element_id_list
        connecting_element_id_list: connecting_element_id_list

    Returns:
        None
    """

```

#### cut_heel_shoulder

```python
def cut_heel_shoulder(element_id_list: List[int],
    connecting_element_id_list: List[int]) ->None:
    """cut heel shoulder

    Parameters:
        element_id_list: element_id_list
        connecting_element_id_list: connecting_element_id_list

    Returns:
        None
    """

```

#### cut_double_shoulder

```python
def cut_double_shoulder(element_id_list: List[int],
    connecting_element_id_list: List[int]) ->None:
    """cut double shoulder

    Parameters:
        element_id_list: element_id_list
        connecting_element_id_list: connecting_element_id_list

    Returns:
        None
    """

```

## New Items
### Functions file_controller
#### export_step_file_cut_drillings

```python
def export_step_file_cut_drillings(a0: List[int], a1: str, a2: float, a3:
    int, a4: bool, a5: bool) ->None:
    """export step file cut drillings

    Parameters:
        a0: a0
        a1: a1
        a2: a2
        a3: a3
        a4: a4
        a5: a5

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

#### get_element_transparency

```python
def get_element_transparency(element_id: int) ->int:
    """get element transparency

    Parameters:
        element_id: element_id

    Returns:
        int
    """

```

#### set_element_transparency

```python
def set_element_transparency(element_id_list: List[int], value: int) ->None:
    """set element transparency

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

```

#### get_use_material_texture

```python
def get_use_material_texture(element_id: int) ->bool:
    """get use material texture

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_use_material_texture

```python
def set_use_material_texture(element_id_list: List[int], value: bool) ->None:
    """set use material texture

    Parameters:
        element_id_list: element_id_list
        value: value

    Returns:
        None
    """

```

#### display_bitmaps_as_texture_representation_in_shaded1

```python
def display_bitmaps_as_texture_representation_in_shaded1(a0: bool) ->None:
    """display bitmaps as texture representation in shaded1

    Parameters:
        a0: a0

    Returns:
        None
    """

```

#### display_bitmaps_as_texture_representation_in_shaded2

```python
def display_bitmaps_as_texture_representation_in_shaded2(a0: bool) ->None:
    """display bitmaps as texture representation in shaded2

    Parameters:
        a0: a0

    Returns:
        None
    """

```

## New Items
### Classes cadwork
#### double_shoulder_options

```python
class double_shoulder_options:

    def get_add_drilling_axis(self) ->bool:
        """get add drilling axis

        Returns:
            bool
        """

    def set_add_drilling_axis(self, value: bool) ->None:
        """set add drilling axis

        Parameters:
            value: value

        Returns:
            None
        """

    def get_add_drilling_axis_query_user_flag(self) ->bool:
        """get add drilling axis query user flag

        Returns:
            bool
        """

    def set_add_drilling_axis_query_user_flag(self, flag: bool) ->None:
        """set add drilling axis query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_diameter(self) ->float:
        """get drilling diameter

        Returns:
            float
        """

    def set_drilling_diameter(self, value: float) ->None:
        """set drilling diameter

        Parameters:
            value: value

        Returns:
            None
        """

    def get_drilling_diameter_query_user_flag(self) ->bool:
        """get drilling diameter query user flag

        Returns:
            bool
        """

    def set_drilling_diameter_query_user_flag(self, flag: bool) ->None:
        """set drilling diameter query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_tolerance(self) ->float:
        """get drilling tolerance

        Returns:
            float
        """

    def set_drilling_tolerance(self, value: float) ->None:
        """set drilling tolerance

        Parameters:
            value: value

        Returns:
            None
        """

    def get_drilling_tolerance_query_user_flag(self) ->bool:
        """get drilling tolerance query user flag

        Returns:
            bool
        """

    def set_drilling_tolerance_query_user_flag(self, flag: bool) ->None:
        """set drilling tolerance query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_orientation_query_user_flag(self) ->bool:
        """get drilling orientation query user flag

        Returns:
            bool
        """

    def set_drilling_orientation_query_user_flag(self, flag: bool) ->None:
        """set drilling orientation query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_beam_geometry(self) ->shoulder_beam_geometry:
        """get beam geometry

        Returns:
            shoulder_beam_geometry
        """

    def set_beam_geometry(self, value: shoulder_beam_geometry) ->None:
        """set beam geometry

        Parameters:
            value: value

        Returns:
            None
        """

    def get_beam_geometry_query_user_flag(self) ->bool:
        """get beam geometry query user flag

        Returns:
            bool
        """

    def set_beam_geometry_query_user_flag(self, flag: bool) ->None:
        """set beam geometry query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_double_shoulder_depth(self) ->float:
        """get double shoulder depth

        Returns:
            float
        """

    def set_double_shoulder_depth(self, value: float) ->None:
        """set double shoulder depth

        Parameters:
            value: value

        Returns:
            None
        """

    def get_double_shoulder_depth_query_user_flag(self) ->bool:
        """get double shoulder depth query user flag

        Returns:
            bool
        """

    def set_double_shoulder_depth_query_user_flag(self, flag: bool) ->None:
        """set double shoulder depth query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_heel_shoulder_depth(self) ->float:
        """get heel shoulder depth

        Returns:
            float
        """

    def set_heel_shoulder_depth(self, value: float) ->None:
        """set heel shoulder depth

        Parameters:
            value: value

        Returns:
            None
        """

    def get_heel_shoulder_depth_query_user_flag(self) ->bool:
        """get heel shoulder depth query user flag

        Returns:
            bool
        """

    def set_heel_shoulder_depth_query_user_flag(self, flag: bool) ->None:
        """set heel shoulder depth query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width(self) ->bool:
        """get cut counter part through whole width

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width(self, value: bool) ->None:
        """set cut counter part through whole width

        Parameters:
            value: value

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width_query_user_flag(self) ->bool:
        """get cut counter part through whole width query user flag

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width_query_user_flag(self, flag:
        bool) ->None:
        """set cut counter part through whole width query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_orientation(self) ->shoulder_drilling_orientation:
        """get drilling orientation

        Returns:
            shoulder_drilling_orientation
        """

    def set_drilling_orientation(self, value: shoulder_drilling_orientation
        ) ->None:
        """set drilling orientation

        Parameters:
            value: value

        Returns:
            None
        """

```

## New Items
### Classes cadwork
#### extended_settings

```python
class extended_settings:

    def get_btl_wall_export(self) ->bool:
        """get btl wall export

        Returns:
            bool
        """

    def get_chief_element(self) ->bool:
        """get chief element

        Returns:
            bool
        """

    def get_group_export(self) ->bool:
        """get group export

        Returns:
            bool
        """

    def get_ignore_for_connector_axis(self) ->bool:
        """get ignore for connector axis

        Returns:
            bool
        """

    def get_log_home_export(self) ->bool:
        """get log home export

        Returns:
            bool
        """

    def get_log_macro_export(self) ->bool:
        """get log macro export

        Returns:
            bool
        """

    def get_mfb_export(self) ->bool:
        """get mfb export

        Returns:
            bool
        """

    def get_outline(self) ->bool:
        """get outline

        Returns:
            bool
        """

    def get_piece_by_piece_export_with_dimensions(self) ->bool:
        """get piece by piece export with dimensions

        Returns:
            bool
        """

    def get_piece_by_piece_export_without_dimensions(self) ->bool:
        """get piece by piece export without dimensions

        Returns:
            bool
        """

    def get_wall_export(self) ->bool:
        """get wall export

        Returns:
            bool
        """

    def set_btl_wall_export(self, value: bool) ->None:
        """set btl wall export

        Parameters:
            value: value

        Returns:
            None
        """

    def set_chief_element(self, value: bool) ->None:
        """set chief element

        Parameters:
            value: value

        Returns:
            None
        """

    def set_group_export(self, value: bool) ->None:
        """set group export

        Parameters:
            value: value

        Returns:
            None
        """

    def set_ignore_for_connector_axis(self, value: bool) ->None:
        """set ignore for connector axis

        Parameters:
            value: value

        Returns:
            None
        """

    def set_log_home_export(self, value: bool) ->None:
        """set log home export

        Parameters:
            value: value

        Returns:
            None
        """

    def set_mfb_export(self, value: bool) ->None:
        """set mfb export

        Parameters:
            value: value

        Returns:
            None
        """

    def set_outline(self, value: bool) ->None:
        """set outline

        Parameters:
            value: value

        Returns:
            None
        """

    def set_piece_by_piece_export_with_dimensions(self, value: bool) ->None:
        """set piece by piece export with dimensions

        Parameters:
            value: value

        Returns:
            None
        """

    def set_piece_by_piece_export_without_dimensions(self, value: bool) ->None:
        """set piece by piece export without dimensions

        Parameters:
            value: value

        Returns:
            None
        """

    def set_wall_export(self, value: bool) ->None:
        """set wall export

        Parameters:
            value: value

        Returns:
            None
        """

    def get_ignore_processing(self) ->bool:
        """get ignore processing

        Returns:
            bool
        """

    def set_ignore_processing(self, value: bool) ->None:
        """set ignore processing

        Parameters:
            value: value

        Returns:
            None
        """

    def get_single_piece(self) ->bool:
        """get single piece

        Returns:
            bool
        """

    def set_single_piece(self, value: bool) ->None:
        """set single piece

        Parameters:
            value: value

        Returns:
            None
        """

    def get_composite(self) ->bool:
        """get composite

        Returns:
            bool
        """

    def set_composite(self, value: bool) ->None:
        """set composite

        Parameters:
            value: value

        Returns:
            None
        """

    def get_drilling_create_notches(self) ->bool:
        """get drilling create notches

        Returns:
            bool
        """

    def set_drilling_create_notches(self, value: bool) ->None:
        """set drilling create notches

        Parameters:
            value: value

        Returns:
            None
        """

```

## New Items
### Classes cadwork
#### heel_shoulder_beam_geometry

```python
@unique
class heel_shoulder_beam_geometry(IntEnum):
    """heel shoulder beam geometry

    Examples:
        >>> cadwork.heel_shoulder_beam_geometry.normal
        normal
    """
    normal = 0
    """"""
    straight = 1
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items
### Classes cadwork
#### heel_shoulder_options

```python
class heel_shoulder_options:

    def get_beam_geometry(self) ->shoulder_beam_geometry:
        """get beam geometry

        Returns:
            shoulder_beam_geometry
        """

    def set_beam_geometry(self, value: shoulder_beam_geometry) ->None:
        """set beam geometry

        Parameters:
            value: value

        Returns:
            None
        """

    def get_beam_geometry_query_user_flag(self) ->bool:
        """get beam geometry query user flag

        Returns:
            bool
        """

    def set_beam_geometry_query_user_flag(self, flag: bool) ->None:
        """set beam geometry query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_shoulder_depth(self) ->float:
        """get shoulder depth

        Returns:
            float
        """

    def set_shoulder_depth(self, value: float) ->None:
        """set shoulder depth

        Parameters:
            value: value

        Returns:
            None
        """

    def get_shoulder_depth_query_user_flag(self) ->bool:
        """get shoulder depth query user flag

        Returns:
            bool
        """

    def set_shoulder_depth_query_user_flag(self, flag: bool) ->None:
        """set shoulder depth query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_gap(self) ->float:
        """get gap

        Returns:
            float
        """

    def set_gap(self, value: float) ->None:
        """set gap

        Parameters:
            value: value

        Returns:
            None
        """

    def get_gap_query_user_flag(self) ->bool:
        """get gap query user flag

        Returns:
            bool
        """

    def set_gap_query_user_flag(self, flag: bool) ->None:
        """set gap query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width(self) ->bool:
        """get cut counter part through whole width

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width(self, value: bool) ->None:
        """set cut counter part through whole width

        Parameters:
            value: value

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width_query_user_flag(self) ->bool:
        """get cut counter part through whole width query user flag

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width_query_user_flag(self, flag:
        bool) ->None:
        """set cut counter part through whole width query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_add_end_type(self) ->bool:
        """get add end type

        Returns:
            bool
        """

    def set_add_end_type(self, value: bool) ->None:
        """set add end type

        Parameters:
            value: value

        Returns:
            None
        """

    def get_add_end_type_query_user_flag(self) ->bool:
        """get add end type query user flag

        Returns:
            bool
        """

    def set_add_end_type_query_user_flag(self, flag: bool) ->None:
        """set add end type query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_end_type_name(self) ->str:
        """get end type name

        Returns:
            str
        """

    def set_end_type_name(self, value: str) ->None:
        """set end type name

        Parameters:
            value: value

        Returns:
            None
        """

    def get_end_type_name_query_user_flag(self) ->bool:
        """get end type name query user flag

        Returns:
            bool
        """

    def set_end_type_name_query_user_flag(self, flag: bool) ->None:
        """set end type name query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

```

## New Items
### Classes cadwork
#### ifc_material_definition

```python
@unique
class ifc_material_definition(IntEnum):
    """ifc material definition

    Examples:
        >>> cadwork.ifc_material_definition.ignore
        ignore
    """
    ignore = 1
    """"""
    material_layer_set = 2
    """"""
    material_constituent_set = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items
### Classes cadwork
#### ifc_options_aggregation

```python
class ifc_options_aggregation:

    def set_consider_element_aggregation(self, consider_element_aggregation:
        bool) ->None:
        """set consider element aggregation

        Parameters:
            consider_element_aggregation: consider_element_aggregation

        Returns:
            None
        """

    def get_element_aggregation_attribute(self) ->int:
        """get element aggregation attribute

        Returns:
            int
        """

    def set_export_cover_geometry(self, export_cover_geometry: bool) ->None:
        """set export cover geometry

        Parameters:
            export_cover_geometry: export_cover_geometry

        Returns:
            None
        """

    def set_element_aggregation_attribute(self,
        element_aggregation_attribute: element_grouping_type) ->None:
        """set element aggregation attribute

        Parameters:
            element_aggregation_attribute: element_aggregation_attribute

        Returns:
            None
        """

    def set_element_combine_type(self, element_combine_type:
        ifc_element_combine_behaviour) ->None:
        """set element combine type

        Parameters:
            element_combine_type: element_combine_type

        Returns:
            None
        """

    def get_consider_element_aggregation(self) ->bool:
        """get consider element aggregation

        Returns:
            bool
        """

    def get_export_cover_geometry(self) ->bool:
        """get export cover geometry

        Returns:
            bool
        """

    def get_element_combine_type(self) ->ifc_element_combine_behaviour:
        """get element combine type

        Returns:
            ifc_element_combine_behaviour
        """

    def set_multi_layer_material_definition_type(self,
        ifc_material_definition: ifc_material_definition) ->None:
        """set multi layer material definition type

        Parameters:
            ifc_material_definition: ifc_material_definition

        Returns:
            None
        """

    def get_multi_layer_material_definition_type(self
        ) ->ifc_material_definition:
        """get multi layer material definition type

        Returns:
            ifc_material_definition
        """

```

## New Items
### Classes cadwork
#### shoulder_beam_geometry

```python
@unique
class shoulder_beam_geometry(IntEnum):
    """shoulder beam geometry

    Examples:
        >>> cadwork.shoulder_beam_geometry.bisector
        bisector
    """
    bisector = 0
    """"""
    perpendicular_to_strut = 1
    """"""
    perpendicular_to_counter_part = 2
    """"""
    birdsmouth = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items
### Classes cadwork
#### shoulder_drilling_orientation

```python
@unique
class shoulder_drilling_orientation(IntEnum):
    """shoulder drilling orientation

    Examples:
        >>> cadwork.shoulder_drilling_orientation.perpendicular_to_bisector
        perpendicular_to_bisector
    """
    perpendicular_to_bisector = 1
    """"""
    perpendicular_to_counter_part = 2
    """"""
    perpendicular_to_strut = 3
    """"""
    perpendicular_to_contact_surface = 4
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items
### Classes cadwork
#### shoulder_options

```python
class shoulder_options:

    def get_add_drilling_axis(self) ->bool:
        """get add drilling axis

        Returns:
            bool
        """

    def set_add_drilling_axis(self, value: bool) ->None:
        """set add drilling axis

        Parameters:
            value: value

        Returns:
            None
        """

    def get_add_drilling_axis_query_user_flag(self) ->bool:
        """get add drilling axis query user flag

        Returns:
            bool
        """

    def set_add_drilling_axis_query_user_flag(self, flag: bool) ->None:
        """set add drilling axis query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_diameter(self) ->float:
        """get drilling diameter

        Returns:
            float
        """

    def set_drilling_diameter(self, value: float) ->None:
        """set drilling diameter

        Parameters:
            value: value

        Returns:
            None
        """

    def get_drilling_diameter_query_user_flag(self) ->bool:
        """get drilling diameter query user flag

        Returns:
            bool
        """

    def set_drilling_diameter_query_user_flag(self, flag: bool) ->None:
        """set drilling diameter query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_tolerance(self) ->float:
        """get drilling tolerance

        Returns:
            float
        """

    def set_drilling_tolerance(self, value: float) ->None:
        """set drilling tolerance

        Parameters:
            value: value

        Returns:
            None
        """

    def get_drilling_tolerance_query_user_flag(self) ->bool:
        """get drilling tolerance query user flag

        Returns:
            bool
        """

    def set_drilling_tolerance_query_user_flag(self, flag: bool) ->None:
        """set drilling tolerance query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_orientation_query_user_flag(self) ->bool:
        """get drilling orientation query user flag

        Returns:
            bool
        """

    def set_drilling_orientation_query_user_flag(self, flag: bool) ->None:
        """set drilling orientation query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_beam_geometry(self) ->shoulder_beam_geometry:
        """get beam geometry

        Returns:
            shoulder_beam_geometry
        """

    def set_beam_geometry(self, value: shoulder_beam_geometry) ->None:
        """set beam geometry

        Parameters:
            value: value

        Returns:
            None
        """

    def get_beam_geometry_query_user_flag(self) ->bool:
        """get beam geometry query user flag

        Returns:
            bool
        """

    def set_beam_geometry_query_user_flag(self, flag: bool) ->None:
        """set beam geometry query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_shoulder_depth(self) ->float:
        """get shoulder depth

        Returns:
            float
        """

    def set_shoulder_depth(self, value: float) ->None:
        """set shoulder depth

        Parameters:
            value: value

        Returns:
            None
        """

    def get_shoulder_depth_query_user_flag(self) ->bool:
        """get shoulder depth query user flag

        Returns:
            bool
        """

    def set_shoulder_depth_query_user_flag(self, flag: bool) ->None:
        """set shoulder depth query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_toe_offset(self) ->float:
        """get toe offset

        Returns:
            float
        """

    def set_toe_offset(self, value: float) ->None:
        """set toe offset

        Parameters:
            value: value

        Returns:
            None
        """

    def get_toe_offset_query_user_flag(self) ->bool:
        """get toe offset query user flag

        Returns:
            bool
        """

    def set_toe_offset_query_user_flag(self, flag: bool) ->None:
        """set toe offset query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width(self) ->bool:
        """get cut counter part through whole width

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width(self, value: bool) ->None:
        """set cut counter part through whole width

        Parameters:
            value: value

        Returns:
            None
        """

    def get_cut_counter_part_through_whole_width_query_user_flag(self) ->bool:
        """get cut counter part through whole width query user flag

        Returns:
            bool
        """

    def set_cut_counter_part_through_whole_width_query_user_flag(self, flag:
        bool) ->None:
        """set cut counter part through whole width query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_add_end_type(self) ->bool:
        """get add end type

        Returns:
            bool
        """

    def set_add_end_type(self, value: bool) ->None:
        """set add end type

        Parameters:
            value: value

        Returns:
            None
        """

    def get_add_end_type_query_user_flag(self) ->bool:
        """get add end type query user flag

        Returns:
            bool
        """

    def set_add_end_type_query_user_flag(self, flag: bool) ->None:
        """set add end type query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_end_type_name(self) ->str:
        """get end type name

        Returns:
            str
        """

    def set_end_type_name(self, value: str) ->None:
        """set end type name

        Parameters:
            value: value

        Returns:
            None
        """

    def get_end_type_name_query_user_flag(self) ->bool:
        """get end type name query user flag

        Returns:
            bool
        """

    def set_end_type_name_query_user_flag(self, flag: bool) ->None:
        """set end type name query user flag

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_drilling_orientation(self) ->shoulder_drilling_orientation:
        """get drilling orientation

        Returns:
            shoulder_drilling_orientation
        """

    def set_drilling_orientation(self, value: shoulder_drilling_orientation
        ) ->None:
        """set drilling orientation

        Parameters:
            value: value

        Returns:
            None
        """

```

