---
hide:
  - navigation
---

# Differences from the last to the current version

## Missing Items
### Functions dimension_controller
#### get_distance

```python
def get_distance(element: int) ->point_3d:
    """Get the distance to the dimension reference point. The point is in the plane of the dimensioning.

    Parameters:
        element: element

    Returns:
        point_3d
    """

```

#### get_plane_normal

```python
def get_plane_normal(element: int) ->point_3d:
    """Get the plane normal

    Parameters:
        element: element

    Returns:
        normal
    """

```

#### get_plane_xl

```python
def get_plane_xl(element: int) ->point_3d:
    """Get the plane x direction

    Parameters:
        element: element

    Returns:
        x direction
    """

```

#### get_segment_count

```python
def get_segment_count(element: int) ->int:
    """Get count of segments

    Parameters:
        element: element

    Returns:
        segment count
    """

```

#### get_segment_distance

```python
def get_segment_distance(element: int, segment_index: int) ->float:
    """Get the distance from the anchor point to the dimension segment

    Parameters:
        element: element
        segment_index: segment_index

    Returns:
        distance
    """

```

## Missing Items
### Functions element_controller
#### convert_surfaces_to_roof_surfaces

```python
def convert_surfaces_to_roof_surfaces(elements: List[int], roof_name: str
    ) ->None:
    """converts surfaces to roof surfaces

    Parameters:
        elements: elements
        roof_name: roof_name

    Returns:
        None
    """

```

## Missing Items
### Functions list_controller
#### export_cover_list

```python
def export_cover_list(element_id_list: List[int], file_path: str) ->None:
    """Exports a Wall/Roof/Floor list

    Parameters:
        element_id_list: element_id_list
        file_path: file_path

    Returns:
        None
    """

```

#### export_cover_list_with_settings

```python
def export_cover_list_with_settings(element_id_list: List[int], file_path:
    str, settings_file_path: str) ->None:
    """Exports a Wall/Roof/Floor list with settings file

    Parameters:
        element_id_list: element_id_list
        file_path: file_path
        settings_file_path: settings_file_path

    Returns:
        None
    """

```

## Missing Items
### Classes cadwork
#### attribute_display_settings

```python
class attribute_display_settings:

    def get_text_position_percentage(self) ->int:
        """get text position percentage

        Returns:
            int
        """

    def set_text_position_percentage(self, percentage: int) ->None:
        """set text position percentage

        Parameters:
            percentage: percentage

        Returns:
            None
        """

    def get_text_position_absolute(self) ->int:
        """get text position absolute

        Returns:
            int
        """

    def set_text_position_absolute(self, absolute: int) ->None:
        """set text position absolute

        Parameters:
            absolute: absolute

        Returns:
            None
        """

    def is_text_position_type_percentage(self) ->bool:
        """is text position type percentage

        Returns:
            bool
        """

    def set_text_position_type_percentage(self, percentage_type: bool) ->None:
        """set text position type percentage

        Parameters:
            percentage_type: percentage_type

        Returns:
            None
        """

    def is_text_position_type_absolute(self) ->bool:
        """is text position type absolute

        Returns:
            bool
        """

    def set_text_position_type_absolute(self, absolute_type: bool) ->None:
        """set text position type absolute

        Parameters:
            absolute_type: absolute_type

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### btl_version

```python
@unique
class btl_version(IntEnum):
    """btl version

    Examples:
        >>> cadwork.btl_version.btlx_1_0
        btlx_1_0
    """
    btlx_1_0 = 110
    """"""
    btlx_1_1 = 111
    """"""
    btl_1_2 = 112
    """"""
    btl_1_3 = 113
    """"""
    btl_1_4 = 114
    """"""
    btl_1_5 = 115
    """"""
    btl_1_6 = 116
    """"""
    btl_10_0 = 100
    """"""
    btl_10_1 = 101
    """"""
    btl_10_2 = 102
    """"""
    btl_10_3 = 103
    """"""
    btl_10_4 = 104
    """"""
    btl_10_5 = 105
    """"""
    btl_10_6 = 106
    """"""
    btlx_2_0 = 120
    """"""
    btlx_2_1 = 121
    """"""
    btlx_2_2 = 122
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### camera_data

```python
class camera_data:

    def get_position(self) ->point_3d:
        """get position

        Returns:
            point_3d
        """

    def set_position(self, position: point_3d) ->None:
        """set position

        Parameters:
            position: position

        Returns:
            None
        """

    def get_target(self) ->point_3d:
        """get target

        Returns:
            point_3d
        """

    def set_target(self, target: point_3d) ->None:
        """set target

        Parameters:
            target: target

        Returns:
            None
        """

    def get_up_vector(self) ->point_3d:
        """get up vector

        Returns:
            point_3d
        """

    def set_up_vector(self, up_vector: point_3d) ->None:
        """set up vector

        Parameters:
            up_vector: up_vector

        Returns:
            None
        """

    def get_projection_type(self) ->projection_type:
        """get projection type

        Returns:
            projection_type
        """

    def set_projection_type(self, projection_type: projection_type) ->None:
        """set projection type

        Parameters:
            projection_type: projection_type

        Returns:
            None
        """

    def get_field_width(self) ->float:
        """get field width

        Returns:
            float
        """

    def set_field_width(self, field_width: float) ->None:
        """set field width

        Parameters:
            field_width: field_width

        Returns:
            None
        """

    def get_field_height(self) ->float:
        """get field height

        Returns:
            float
        """

    def set_field_height(self, field_height: float) ->None:
        """set field height

        Parameters:
            field_height: field_height

        Returns:
            None
        """

    def get_field_of_view(self) ->float:
        """get field of view

        Returns:
            float
        """

    def set_field_of_view(self, field_of_view: float) ->None:
        """set field of view

        Parameters:
            field_of_view: field_of_view

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### coordinate_system_data

```python
class coordinate_system_data:

    def get_p1(self) ->point_3d:
        """get p1

        Returns:
            point_3d
        """

    def get_p2(self) ->point_3d:
        """get p2

        Returns:
            point_3d
        """

    def get_p3(self) ->point_3d:
        """get p3

        Returns:
            point_3d
        """

```

## Missing Items
### Classes cadwork
#### division_zone_direction

```python
@unique
class division_zone_direction(IntEnum):
    """division zone direction

    Examples:
        >>> cadwork.division_zone_direction.positive
        positive
    """
    positive = 1
    """"""
    negative = 2
    """"""
    no_direction = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### edge_list

```python
class edge_list:

    def count(self) ->int:
        """count

        Returns:
            int
        """

    def at(self, index: int) ->point_3d:
        """at

        Parameters:
            index: index

        Returns:
            point_3d
        """

```

## Missing Items
### Classes cadwork
#### element_grouping_type

```python
@unique
class element_grouping_type(IntEnum):
    """element grouping type

    Examples:
        >>> cadwork.element_grouping_type.group
        group
    """
    group = 1
    """"""
    subgroup = 2
    """"""
    _none = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### element_module_detail

```python
@unique
class element_module_detail(IntEnum):
    """element module detail

    Examples:
        >>> cadwork.element_module_detail.no_detail
        no_detail
    """
    no_detail = 1
    """"""
    angle_detail = 2
    """"""
    area_detail = 3
    """"""
    cross_detail = 4
    """"""
    edge_detail = 5
    """"""
    end_detail = 6
    """"""
    line_detail = 7
    """"""
    open_detail = 8
    """"""
    t_detail = 9
    """"""
    floor_area_detail = 10
    """"""
    floor_end_detail = 11
    """"""
    floor_line_detail = 12
    """"""
    floor_open_detail = 13
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### element_module_properties

```python
class element_module_properties:

    def is_stretch_with_top_of_wall(self) ->bool:
        """is stretch with top of wall

        Returns:
            bool
        """

    def is_move_with_top_of_wall(self) ->bool:
        """is move with top of wall

        Returns:
            bool
        """

    def is_distribute_in_axis_direction(self) ->bool:
        """is distribute in axis direction

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction(self) ->bool:
        """is distribute perpendicular to axis direction

        Returns:
            bool
        """

    def is_stop_in_axis_direction(self) ->bool:
        """is stop in axis direction

        Returns:
            bool
        """

    def is_stop_perpendicular_to_axis_direction(self) ->bool:
        """is stop perpendicular to axis direction

        Returns:
            bool
        """

    def is_bottom_plate(self) ->bool:
        """is bottom plate

        Returns:
            bool
        """

    def is_top_plate(self) ->bool:
        """is top plate

        Returns:
            bool
        """

    def is_opening_sill(self) ->bool:
        """is opening sill

        Returns:
            bool
        """

    def is_opening_lintel(self) ->bool:
        """is opening lintel

        Returns:
            bool
        """

    def is_cutting_element(self) ->bool:
        """is cutting element

        Returns:
            bool
        """

    def is_not_cut_with_cutting_element(self) ->bool:
        """is not cut with cutting element

        Returns:
            bool
        """

    def is_auxiliary(self) ->bool:
        """is auxiliary

        Returns:
            bool
        """

    def is_not_placed_at_end_of_wall(self) ->bool:
        """is not placed at end of wall

        Returns:
            bool
        """

    def is_not_placed_at_start_of_wall(self) ->bool:
        """is not placed at start of wall

        Returns:
            bool
        """

    def is_stretch_with_opening_lintel(self) ->bool:
        """is stretch with opening lintel

        Returns:
            bool
        """

    def is_stretch_with_opening_sill(self) ->bool:
        """is stretch with opening sill

        Returns:
            bool
        """

    def is_solder_in_axis_direction(self) ->bool:
        """is solder in axis direction

        Returns:
            bool
        """

    def is_no_collision_control(self) ->bool:
        """is no collision control

        Returns:
            bool
        """

    def is_no_inside_cover_control(self) ->bool:
        """is no inside cover control

        Returns:
            bool
        """

    def is_use_for_detail_coordinate_system(self) ->bool:
        """is use for detail coordinate system

        Returns:
            bool
        """

    def set_stretch_with_top_of_wall(self, active: bool) ->None:
        """set stretch with top of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_with_top_of_wall(self, active: bool) ->None:
        """set move with top of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_in_axis_direction(self, active: bool, distance: float
        ) ->None:
        """set distribute in axis direction

        Parameters:
            active: active
            distance: distance

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction(self, active: bool,
        distance: float) ->None:
        """set distribute perpendicular to axis direction

        Parameters:
            active: active
            distance: distance

        Returns:
            None
        """

    def set_stop_in_axis_direction(self, active: bool) ->None:
        """set stop in axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stop_perpendicular_to_axis_direction(self, active: bool) ->None:
        """set stop perpendicular to axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_bottom_plate(self, active: bool) ->None:
        """set bottom plate

        Parameters:
            active: active

        Returns:
            None
        """

    def set_top_plate(self, active: bool) ->None:
        """set top plate

        Parameters:
            active: active

        Returns:
            None
        """

    def set_opening_sill(self, active: bool) ->None:
        """set opening sill

        Parameters:
            active: active

        Returns:
            None
        """

    def set_opening_lintel(self, active: bool) ->None:
        """set opening lintel

        Parameters:
            active: active

        Returns:
            None
        """

    def set_cutting_element(self, active: bool, priority: int) ->None:
        """set cutting element

        Parameters:
            active: active
            priority: priority

        Returns:
            None
        """

    def set_not_cut_with_cutting_element(self, active: bool) ->None:
        """set not cut with cutting element

        Parameters:
            active: active

        Returns:
            None
        """

    def set_auxiliary(self) ->None:
        """set auxiliary

        Returns:
            None
        """

    def set_not_placed_at_end_of_wall(self, active: bool) ->None:
        """set not placed at end of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_not_placed_at_start_of_wall(self, active: bool) ->None:
        """set not placed at start of wall

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stretch_with_opening_lintel(self, active: bool) ->None:
        """set stretch with opening lintel

        Parameters:
            active: active

        Returns:
            None
        """

    def set_stretch_with_opening_sill(self, active: bool) ->None:
        """set stretch with opening sill

        Parameters:
            active: active

        Returns:
            None
        """

    def set_solder_in_axis_direction(self, active: bool) ->None:
        """set solder in axis direction

        Parameters:
            active: active

        Returns:
            None
        """

    def set_no_collision_control(self, active: bool) ->None:
        """set no collision control

        Parameters:
            active: active

        Returns:
            None
        """

    def set_no_inside_cover_control(self, active: bool) ->None:
        """set no inside cover control

        Parameters:
            active: active

        Returns:
            None
        """

    def set_use_for_detail_coordinate_system(self, active: bool) ->None:
        """set use for detail coordinate system

        Parameters:
            active: active

        Returns:
            None
        """

    def get_distribute_in_axis_direction_distance(self) ->float:
        """get distribute in axis direction distance

        Returns:
            float
        """

    def get_distribute_perpendicular_to_axis_direction_distance(self) ->float:
        """get distribute perpendicular to axis direction distance

        Returns:
            float
        """

    def get_cutting_element_priority(self) ->int:
        """get cutting element priority

        Returns:
            int
        """

    def is_distribute_in_axis_direction_use_max_distance(self) ->bool:
        """is distribute in axis direction use max distance

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self
        ) ->bool:
        """is distribute perpendicular to axis direction use max distance

        Returns:
            bool
        """

    def is_distribute_in_axis_direction_use_number(self) ->bool:
        """is distribute in axis direction use number

        Returns:
            bool
        """

    def is_distribute_perpendicular_to_axis_direction_use_number(self) ->bool:
        """is distribute perpendicular to axis direction use number

        Returns:
            bool
        """

    def set_distribute_in_axis_direction_use_max_distance(self, active: bool
        ) ->None:
        """set distribute in axis direction use max distance

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self,
        active: bool) ->None:
        """set distribute perpendicular to axis direction use max distance

        Parameters:
            active: active

        Returns:
            None
        """

    def set_distribute_in_axis_direction_use_number(self, active: bool,
        number: int) ->None:
        """set distribute in axis direction use number

        Parameters:
            active: active
            number: number

        Returns:
            None
        """

    def set_distribute_perpendicular_to_axis_direction_use_number(self,
        active: bool, number: int) ->None:
        """set distribute perpendicular to axis direction use number

        Parameters:
            active: active
            number: number

        Returns:
            None
        """

    def get_distribute_in_axis_direction_number(self) ->int:
        """get distribute in axis direction number

        Returns:
            int
        """

    def get_distribute_perpendicular_to_axis_direction_number(self) ->int:
        """get distribute perpendicular to axis direction number

        Returns:
            int
        """

    def is_main_element(self) ->bool:
        """is main element

        Returns:
            bool
        """

    def is_strecht_according_thickness_axis(self) ->bool:
        """is strecht according thickness axis

        Returns:
            bool
        """

    def is_strecht_according_length_axis(self) ->bool:
        """is strecht according length axis

        Returns:
            bool
        """

    def is_move_according_thickness_axis(self) ->bool:
        """is move according thickness axis

        Returns:
            bool
        """

    def is_move_according_length_axis(self) ->bool:
        """is move according length axis

        Returns:
            bool
        """

    def is_unique_layername(self) ->bool:
        """is unique layername

        Returns:
            bool
        """

    def is_keep_in_center_of_layer_current_wall(self) ->bool:
        """is keep in center of layer current wall

        Returns:
            bool
        """

    def is_keep_in_center_of_layer_neighbour_wall(self) ->bool:
        """is keep in center of layer neighbour wall

        Returns:
            bool
        """

    def is_keep_in_center_of_rough_volume(self) ->bool:
        """is keep in center of rough volume

        Returns:
            bool
        """

    def is_element_from_detail(self) ->bool:
        """is element from detail

        Returns:
            bool
        """

    def set_main_element(self, active: bool) ->None:
        """set main element

        Parameters:
            active: active

        Returns:
            None
        """

    def set_strecht_according_thickness_axis(self, active: bool) ->None:
        """set strecht according thickness axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_strecht_according_length_axis(self, active: bool) ->None:
        """set strecht according length axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_according_thickness_axis(self, active: bool) ->None:
        """set move according thickness axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_move_according_length_axis(self, active: bool) ->None:
        """set move according length axis

        Parameters:
            active: active

        Returns:
            None
        """

    def set_unique_layername(self, active: bool, layername: str) ->None:
        """set unique layername

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_layer_current_wall(self, active: bool,
        layername: str) ->None:
        """set keep in center of layer current wall

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_layer_neighbour_wall(self, active: bool,
        layername: str) ->None:
        """set keep in center of layer neighbour wall

        Parameters:
            active: active
            layername: layername

        Returns:
            None
        """

    def set_keep_in_center_of_rough_volume(self, active: bool) ->None:
        """set keep in center of rough volume

        Parameters:
            active: active

        Returns:
            None
        """

    def set_element_from_detail(self, active: bool) ->None:
        """set element from detail

        Parameters:
            active: active

        Returns:
            None
        """

    def get_unique_layername(self) ->str:
        """get unique layername

        Returns:
            str
        """

    def get_keep_in_center_of_layer_current_wall(self) ->str:
        """get keep in center of layer current wall

        Returns:
            str
        """

    def get_keep_in_center_of_layer_neighbour_wall(self) ->str:
        """get keep in center of layer neighbour wall

        Returns:
            str
        """

    def is_stretch_in_opening_width(self) ->bool:
        """is stretch in opening width

        Returns:
            bool
        """

    def set_stretch_in_opening_width(self, active: bool) ->None:
        """set stretch in opening width

        Parameters:
            active: active

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### element_type

```python
class element_type:

    def is_none(self) ->bool:
        """is none

        Returns:
            bool
        """

    def is_normal_node(self) ->bool:
        """is normal node

        Returns:
            bool
        """

    def is_connector_node(self) ->bool:
        """is connector node

        Returns:
            bool
        """

    def is_wire_axis(self) ->bool:
        """is wire axis

        Returns:
            bool
        """

    def is_eave_axis(self) ->bool:
        """is eave axis

        Returns:
            bool
        """

    def is_rectangular_axis(self) ->bool:
        """is rectangular axis

        Returns:
            bool
        """

    def is_circular_axis(self) ->bool:
        """is circular axis

        Returns:
            bool
        """

    def is_drilling_axis(self) ->bool:
        """is drilling axis

        Returns:
            bool
        """

    def is_connector_axis(self) ->bool:
        """is connector axis

        Returns:
            bool
        """

    def is_line(self) ->bool:
        """is line

        Returns:
            bool
        """

    def is_surface(self) ->bool:
        """is surface

        Returns:
            bool
        """

    def is_cadwork(self) ->bool:
        """is cadwork

        Returns:
            bool
        """

    def is_global_cut(self) ->bool:
        """is global cut

        Returns:
            bool
        """

    def is_wall(self) ->bool:
        """is wall

        Returns:
            bool
        """

    def is_opening(self) ->bool:
        """is opening

        Returns:
            bool
        """

    def is_floor(self) ->bool:
        """is floor

        Returns:
            bool
        """

    def is_roof(self) ->bool:
        """is roof

        Returns:
            bool
        """

    def is_container(self) ->bool:
        """is container

        Returns:
            bool
        """

    def is_export_solid(self) ->bool:
        """is export solid

        Returns:
            bool
        """

    def is_auxiliary(self) ->bool:
        """is auxiliary

        Returns:
            bool
        """

    def is_nesting_parent(self) ->bool:
        """is nesting parent

        Returns:
            bool
        """

    def is_rectangular_beam(self) ->bool:
        """is rectangular beam

        Returns:
            bool
        """

    def is_circular_beam(self) ->bool:
        """is circular beam

        Returns:
            bool
        """

    def is_steel_shape(self) ->bool:
        """is steel shape

        Returns:
            bool
        """

    def is_panel(self) ->bool:
        """is panel

        Returns:
            bool
        """

    def is_rotation_element(self) ->bool:
        """is rotation element

        Returns:
            bool
        """

    def is_additional_element(self) ->bool:
        """is additional element

        Returns:
            bool
        """

    def is_room(self) ->bool:
        """is room

        Returns:
            bool
        """

    def is_graphical_object(self) ->bool:
        """is graphical object

        Returns:
            bool
        """

    def is_dimension(self) ->bool:
        """is dimension

        Returns:
            bool
        """

    def is_text_document(self) ->bool:
        """is text document

        Returns:
            bool
        """

    def is_export_solid_scene(self) ->bool:
        """is export solid scene

        Returns:
            bool
        """

    def is_section_trace(self) ->bool:
        """is section trace

        Returns:
            bool
        """

    def set_none(self) ->None:
        """set none

        Returns:
            None
        """

    def set_normal_node(self) ->None:
        """set normal node

        Returns:
            None
        """

    def set_connector_node(self) ->None:
        """set connector node

        Returns:
            None
        """

    def set_wire_axis(self) ->None:
        """set wire axis

        Returns:
            None
        """

    def set_eave_axis(self) ->None:
        """set eave axis

        Returns:
            None
        """

    def set_rectangular_axis(self) ->None:
        """set rectangular axis

        Returns:
            None
        """

    def set_circular_axis(self) ->None:
        """set circular axis

        Returns:
            None
        """

    def set_drilling_axis(self) ->None:
        """set drilling axis

        Returns:
            None
        """

    def set_connector_axis(self) ->None:
        """set connector axis

        Returns:
            None
        """

    def set_line(self) ->None:
        """set line

        Returns:
            None
        """

    def set_surface(self) ->None:
        """set surface

        Returns:
            None
        """

    def set_cadwork(self) ->None:
        """set cadwork

        Returns:
            None
        """

    def set_global_cut(self) ->None:
        """set global cut

        Returns:
            None
        """

    def set_opening(self) ->None:
        """set opening

        Returns:
            None
        """

    def set_container(self) ->None:
        """set container

        Returns:
            None
        """

    def set_export_solid(self) ->None:
        """set export solid

        Returns:
            None
        """

    def set_auxiliary(self) ->None:
        """set auxiliary

        Returns:
            None
        """

    def set_nesting_parent(self) ->None:
        """set nesting parent

        Returns:
            None
        """

    def set_rectangular_beam(self) ->None:
        """set rectangular beam

        Returns:
            None
        """

    def set_circular_beam(self) ->None:
        """set circular beam

        Returns:
            None
        """

    def set_steel_shape(self) ->None:
        """set steel shape

        Returns:
            None
        """

    def set_panel(self) ->None:
        """set panel

        Returns:
            None
        """

    def set_rotation_element(self) ->None:
        """set rotation element

        Returns:
            None
        """

    def set_additional_element(self) ->None:
        """set additional element

        Returns:
            None
        """

    def set_room(self) ->None:
        """set room

        Returns:
            None
        """

    def set_graphical_object(self) ->None:
        """set graphical object

        Returns:
            None
        """

    def set_dimension(self) ->None:
        """set dimension

        Returns:
            None
        """

    def set_text_document(self) ->None:
        """set text document

        Returns:
            None
        """

    def set_export_solid_scene(self) ->None:
        """set export solid scene

        Returns:
            None
        """

    def set_section_trace(self) ->None:
        """set section trace

        Returns:
            None
        """

```

## Missing Items
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

```

## Missing Items
### Classes cadwork
#### facet_list

```python
class facet_list:

    def count(self) ->int:
        """count

        Returns:
            int
        """

    def at(self, index: int) ->point_3d:
        """at

        Parameters:
            index: index

        Returns:
            point_3d
        """

    def get_external_polygon(self, index: int) ->vertex_list:
        """get external polygon

        Parameters:
            index: index

        Returns:
            vertex_list
        """

    def get_internal_polygons(self, index: int) ->polygon_list:
        """get internal polygons

        Parameters:
            index: index

        Returns:
            polygon_list
        """

    def get_vertices_for_reference_face(self) ->vertex_list:
        """get vertices for reference face

        Returns:
            vertex_list
        """

    def get_external_polygon_for_reference_face(self) ->vertex_list:
        """get external polygon for reference face

        Returns:
            vertex_list
        """

    def get_internal_polygons_for_reference_face(self) ->polygon_list:
        """get internal polygons for reference face

        Returns:
            polygon_list
        """

    def get_normal_vector(self, index: int) ->point_3d:
        """get normal vector

        Parameters:
            index: index

        Returns:
            point_3d
        """

    def get_distance_to_origin(self, index: int) ->float:
        """get distance to origin

        Parameters:
            index: index

        Returns:
            float
        """

```

## Missing Items
### Classes cadwork
#### hundegger_machine_type

```python
@unique
class hundegger_machine_type(IntEnum):
    """hundegger machine type

    Examples:
        >>> cadwork.hundegger_machine_type.p8_10
        p8_10
    """
    p8_10 = 1
    """"""
    k1 = 2
    """"""
    k2 = 3
    """"""
    k2_cambium = 4
    """"""
    k2_uf_5 = 5
    """"""
    k2_uf_5_cambium = 6
    """"""
    speedcut = 7
    """"""
    pba = 8
    """"""
    pba_bvx = 9
    """"""
    pba_bvx_cambium = 10
    """"""
    spm = 12
    """"""
    spm_cambium = 13
    """"""
    robot_drive = 14
    """"""
    turbo_drive = 15
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### ifc_2x3_element_type

```python
class ifc_2x3_element_type:

    def is_none(self) ->bool:
        """is none

        Returns:
            bool
        """

    def is_ifc_beam(self) ->bool:
        """is ifc beam

        Returns:
            bool
        """

    def is_ifc_column(self) ->bool:
        """is ifc column

        Returns:
            bool
        """

    def is_ifc_curtain_wall(self) ->bool:
        """is ifc curtain wall

        Returns:
            bool
        """

    def is_ifc_door(self) ->bool:
        """is ifc door

        Returns:
            bool
        """

    def is_ifc_member(self) ->bool:
        """is ifc member

        Returns:
            bool
        """

    def is_ifc_plate(self) ->bool:
        """is ifc plate

        Returns:
            bool
        """

    def is_ifc_railing(self) ->bool:
        """is ifc railing

        Returns:
            bool
        """

    def is_ifc_ramp(self) ->bool:
        """is ifc ramp

        Returns:
            bool
        """

    def is_ifc_ramp_flight(self) ->bool:
        """is ifc ramp flight

        Returns:
            bool
        """

    def is_ifc_roof(self) ->bool:
        """is ifc roof

        Returns:
            bool
        """

    def is_ifc_slab(self) ->bool:
        """is ifc slab

        Returns:
            bool
        """

    def is_ifc_stair(self) ->bool:
        """is ifc stair

        Returns:
            bool
        """

    def is_ifc_stair_flight(self) ->bool:
        """is ifc stair flight

        Returns:
            bool
        """

    def is_ifc_wall(self) ->bool:
        """is ifc wall

        Returns:
            bool
        """

    def is_ifc_wall_standard_case(self) ->bool:
        """is ifc wall standard case

        Returns:
            bool
        """

    def is_ifc_window(self) ->bool:
        """is ifc window

        Returns:
            bool
        """

    def is_ifc_building_element_proxy(self) ->bool:
        """is ifc building element proxy

        Returns:
            bool
        """

    def is_ifc_chimney(self) ->bool:
        """is ifc chimney

        Returns:
            bool
        """

    def is_ifc_covering(self) ->bool:
        """is ifc covering

        Returns:
            bool
        """

    def is_ifc_footing(self) ->bool:
        """is ifc footing

        Returns:
            bool
        """

    def is_ifc_furnishing_element(self) ->bool:
        """is ifc furnishing element

        Returns:
            bool
        """

    def is_ifc_opening_element(self) ->bool:
        """is ifc opening element

        Returns:
            bool
        """

    def is_ifc_space(self) ->bool:
        """is ifc space

        Returns:
            bool
        """

    def is_ifc_flow_segment(self) ->bool:
        """is ifc flow segment

        Returns:
            bool
        """

    def is_ifc_building_element_part(self) ->bool:
        """is ifc building element part

        Returns:
            bool
        """

    def is_ifc_discrete_accessory(self) ->bool:
        """is ifc discrete accessory

        Returns:
            bool
        """

    def is_ifc_fastener(self) ->bool:
        """is ifc fastener

        Returns:
            bool
        """

    def is_ifc_mechanical_fastener(self) ->bool:
        """is ifc mechanical fastener

        Returns:
            bool
        """

    def set_none(self) ->None:
        """set none

        Returns:
            None
        """

    def set_ifc_beam(self) ->None:
        """set ifc beam

        Returns:
            None
        """

    def set_ifc_column(self) ->None:
        """set ifc column

        Returns:
            None
        """

    def set_ifc_curtain_wall(self) ->None:
        """set ifc curtain wall

        Returns:
            None
        """

    def set_ifc_door(self) ->None:
        """set ifc door

        Returns:
            None
        """

    def set_ifc_member(self) ->None:
        """set ifc member

        Returns:
            None
        """

    def set_ifc_plate(self) ->None:
        """set ifc plate

        Returns:
            None
        """

    def set_ifc_railing(self) ->None:
        """set ifc railing

        Returns:
            None
        """

    def set_ifc_ramp(self) ->None:
        """set ifc ramp

        Returns:
            None
        """

    def set_ifc_ramp_flight(self) ->None:
        """set ifc ramp flight

        Returns:
            None
        """

    def set_ifc_roof(self) ->None:
        """set ifc roof

        Returns:
            None
        """

    def set_ifc_slab(self) ->None:
        """set ifc slab

        Returns:
            None
        """

    def set_ifc_stair(self) ->None:
        """set ifc stair

        Returns:
            None
        """

    def set_ifc_stair_flight(self) ->None:
        """set ifc stair flight

        Returns:
            None
        """

    def set_ifc_wall(self) ->None:
        """set ifc wall

        Returns:
            None
        """

    def set_ifc_wall_standard_case(self) ->None:
        """set ifc wall standard case

        Returns:
            None
        """

    def set_ifc_window(self) ->None:
        """set ifc window

        Returns:
            None
        """

    def set_ifc_building_element_proxy(self) ->None:
        """set ifc building element proxy

        Returns:
            None
        """

    def set_ifc_chimney(self) ->None:
        """set ifc chimney

        Returns:
            None
        """

    def set_ifc_covering(self) ->None:
        """set ifc covering

        Returns:
            None
        """

    def set_ifc_footing(self) ->None:
        """set ifc footing

        Returns:
            None
        """

    def set_ifc_furnishing_element(self) ->None:
        """set ifc furnishing element

        Returns:
            None
        """

    def set_ifc_opening_element(self) ->None:
        """set ifc opening element

        Returns:
            None
        """

    def set_ifc_space(self) ->None:
        """set ifc space

        Returns:
            None
        """

    def set_ifc_flow_segment(self) ->None:
        """set ifc flow segment

        Returns:
            None
        """

    def set_ifc_building_element_part(self) ->None:
        """set ifc building element part

        Returns:
            None
        """

    def set_ifc_discrete_accessory(self) ->None:
        """set ifc discrete accessory

        Returns:
            None
        """

    def set_ifc_fastener(self) ->None:
        """set ifc fastener

        Returns:
            None
        """

    def set_ifc_mechanical_fastener(self) ->None:
        """set ifc mechanical fastener

        Returns:
            None
        """

    def __repr__(self) ->str:
        """  repr  

        Returns:
            str
        """

```

## Missing Items
### Classes cadwork
#### ifc_element_combine_behaviour

```python
@unique
class ifc_element_combine_behaviour(IntEnum):
    """ifc element combine behaviour

    Examples:
        >>> cadwork.ifc_element_combine_behaviour.element_module
        element_module
    """
    element_module = 0
    """"""
    element_assembly = 1
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### ifc_options

```python
class ifc_options:

    def get_ifc_options_properties(self) ->'ifc_options_properties':
        """get ifc options properties

        Returns:
            'ifc_options_properties'
        """

    def get_ifc_options_project_data(self) ->'ifc_options_project_data':
        """get ifc options project data

        Returns:
            'ifc_options_project_data'
        """

    def get_ifc_options_aggregation(self) ->'ifc_options_aggregation':
        """get ifc options aggregation

        Returns:
            'ifc_options_aggregation'
        """

    def get_ifc_options_level_of_detail(self) ->'ifc_options_level_of_detail':
        """get ifc options level of detail

        Returns:
            'ifc_options_level_of_detail'
        """

```

## Missing Items
### Classes cadwork
#### ifc_options_aggregation

```python
class ifc_options_aggregation:

    def get_export_cover_geometry(self) ->bool:
        """get export cover geometry

        Returns:
            bool
        """

    def set_element_aggregation_attribute(self,
        element_aggregation_attribute: element_grouping_type) ->None:
        """set element aggregation attribute

        Parameters:
            element_aggregation_attribute: element_aggregation_attribute

        Returns:
            None
        """

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

    def get_consider_element_aggregation(self) ->bool:
        """get consider element aggregation

        Returns:
            bool
        """

    def get_element_combine_type(self) ->ifc_element_combine_behaviour:
        """get element combine type

        Returns:
            ifc_element_combine_behaviour
        """

    def set_export_cover_geometry(self, export_cover_geometry: bool) ->None:
        """set export cover geometry

        Parameters:
            export_cover_geometry: export_cover_geometry

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

```

## Missing Items
### Classes cadwork
#### ifc_options_level_of_detail

```python
class ifc_options_level_of_detail:

    def get_export_vba_drillings(self) ->bool:
        """get export vba drillings

        Returns:
            bool
        """

    def set_cut_endtype_counterparts(self, cut_endtype_counterparts: bool
        ) ->None:
        """set cut endtype counterparts

        Parameters:
            cut_endtype_counterparts: cut_endtype_counterparts

        Returns:
            None
        """

    def set_export_installation_rectangular_materialization(self,
        export_installation_rectangular_materialization: bool) ->None:
        """set export installation rectangular materialization

        Parameters:
            export_installation_rectangular_materialization: export_installation_rectangular_materialization

        Returns:
            None
        """

    def get_export_endtype_materialization(self) ->bool:
        """get export endtype materialization

        Returns:
            bool
        """

    def get_cut_endtype_counterparts(self) ->bool:
        """get cut endtype counterparts

        Returns:
            bool
        """

    def get_export_installation_round_materialization(self) ->bool:
        """get export installation round materialization

        Returns:
            bool
        """

    def set_export_vba_drillings(self, export_vba_drillings: bool) ->None:
        """set export vba drillings

        Parameters:
            export_vba_drillings: export_vba_drillings

        Returns:
            None
        """

    def set_cut_installation_round(self, cut_installation_round: bool) ->None:
        """set cut installation round

        Parameters:
            cut_installation_round: cut_installation_round

        Returns:
            None
        """

    def get_export_vba_components(self) ->bool:
        """get export vba components

        Returns:
            bool
        """

    def set_export_experimental_swept_solid_materialization(self,
        export_swept_solid_for_simple_geometry: bool) ->None:
        """set export experimental swept solid materialization

        Parameters:
            export_swept_solid_for_simple_geometry: export_swept_solid_for_simple_geometry

        Returns:
            None
        """

    def set_export_endtype_materialization(self, materializaiton: bool) ->None:
        """set export endtype materialization

        Parameters:
            materializaiton: materializaiton

        Returns:
            None
        """

    def set_cut_drillings(self, flag: bool) ->None:
        """set cut drillings

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_drillings(self) ->bool:
        """get cut drillings

        Returns:
            bool
        """

    def set_export_vba_components(self, export_vba_components: bool) ->None:
        """set export vba components

        Parameters:
            export_vba_components: export_vba_components

        Returns:
            None
        """

    def get_export_experimental_swept_solid_materialization(self) ->bool:
        """get export experimental swept solid materialization

        Returns:
            bool
        """

    def get_cut_installation_round(self) ->bool:
        """get cut installation round

        Returns:
            bool
        """

    def set_export_installation_round_materialization(self,
        export_installation_round_materialization: bool) ->None:
        """set export installation round materialization

        Parameters:
            export_installation_round_materialization: export_installation_round_materialization

        Returns:
            None
        """

    def get_cut_installation_rectangular(self) ->bool:
        """get cut installation rectangular

        Returns:
            bool
        """

    def get_export_installation_rectangular_materialization(self) ->bool:
        """get export installation rectangular materialization

        Returns:
            bool
        """

    def set_cut_installation_rectangular(self, cut_installation_rectangular:
        bool) ->None:
        """set cut installation rectangular

        Parameters:
            cut_installation_rectangular: cut_installation_rectangular

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### ifc_options_project_data

```python
class ifc_options_project_data:

    def get_export_coordinates_in_ifc_site(self) ->bool:
        """get export coordinates in ifc site

        Returns:
            bool
        """

    def set_export_project_name_as_ifc_project(self,
        export_project_name_as_ifc_project: bool) ->None:
        """set export project name as ifc project

        Parameters:
            export_project_name_as_ifc_project: export_project_name_as_ifc_project

        Returns:
            None
        """

    def set_export_coordinates_in_ifc_site(self,
        export_coordinates_in_ifc_site: bool) ->None:
        """set export coordinates in ifc site

        Parameters:
            export_coordinates_in_ifc_site: export_coordinates_in_ifc_site

        Returns:
            None
        """

    def set_export_true_north_in_geometric_context(self,
        export_true_north_in_geometric_context: bool) ->None:
        """set export true north in geometric context

        Parameters:
            export_true_north_in_geometric_context: export_true_north_in_geometric_context

        Returns:
            None
        """

    def get_export_project_name_as_ifc_project(self) ->bool:
        """get export project name as ifc project

        Returns:
            bool
        """

    def get_export_true_north_in_geometric_context(self) ->bool:
        """get export true north in geometric context

        Returns:
            bool
        """

    def get_export_adress_in_ifc_site(self) ->bool:
        """get export adress in ifc site

        Returns:
            bool
        """

    def set_export_adress_in_ifc_site(self, export_adress_in_ifc_site: bool
        ) ->None:
        """set export adress in ifc site

        Parameters:
            export_adress_in_ifc_site: export_adress_in_ifc_site

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### ifc_options_properties

```python
class ifc_options_properties:

    def get_attriubte_nr_ifc_tag(self) ->int:
        """get attriubte nr ifc tag

        Returns:
            int
        """

    def set_export_empty_building_and_storeys(self,
        export_empty_building_and_storeys: bool) ->None:
        """set export empty building and storeys

        Parameters:
            export_empty_building_and_storeys: export_empty_building_and_storeys

        Returns:
            None
        """

    def set_attribute_nr_ifc_tag(self, attribute_nr_ifc_tag: int) ->None:
        """set attribute nr ifc tag

        Parameters:
            attribute_nr_ifc_tag: attribute_nr_ifc_tag

        Returns:
            None
        """

    def set_export_bim_wood_property(self, export_bi_mwood_property: bool
        ) ->None:
        """set export bim wood property

        Parameters:
            export_bi_mwood_property: export_bi_mwood_property

        Returns:
            None
        """

    def get_export_empty_building_and_storeys(self) ->bool:
        """get export empty building and storeys

        Returns:
            bool
        """

    def set_ignore_user_attributes_used_in_psets(self,
        ignore_user_attributes_used_in_user_psets: bool) ->None:
        """set ignore user attributes used in psets

        Parameters:
            ignore_user_attributes_used_in_user_psets: ignore_user_attributes_used_in_user_psets

        Returns:
            None
        """

    def get_ignore_user_attributes_used_in_psets(self) ->bool:
        """get ignore user attributes used in psets

        Returns:
            bool
        """

    def get_attribute_nr_ifc_layer(self) ->int:
        """get attribute nr ifc layer

        Returns:
            int
        """

    def set_attribute_nr_ifc_layer(self, attribute_nr_ifc_layer: int) ->None:
        """set attribute nr ifc layer

        Parameters:
            attribute_nr_ifc_layer: attribute_nr_ifc_layer

        Returns:
            None
        """

    def get_export_bim_wood_property(self) ->bool:
        """get export bim wood property

        Returns:
            bool
        """

    def set_export_cadwork_3d_pset(self, export_cadwork3d_p_set: bool) ->None:
        """set export cadwork 3d pset

        Parameters:
            export_cadwork3d_p_set: export_cadwork3d_p_set

        Returns:
            None
        """

    def get_export_cadwork_3d_pset(self) ->bool:
        """get export cadwork 3d pset

        Returns:
            bool
        """

```

## Missing Items
### Classes cadwork
#### import_3dc_options

```python
class import_3dc_options:

    def set_import_saved_2d_planes(self, value: bool) ->None:
        """set import saved 2d planes

        Parameters:
            value: value

        Returns:
            None
        """

    def get_import_saved_2d_planes(self) ->bool:
        """get import saved 2d planes

        Returns:
            bool
        """

    def set_import_saved_scenes(self, value: bool) ->None:
        """set import saved scenes

        Parameters:
            value: value

        Returns:
            None
        """

    def get_import_saved_scenes(self) ->bool:
        """get import saved scenes

        Returns:
            bool
        """

    def set_import_export_solids(self, value: bool) ->None:
        """set import export solids

        Parameters:
            value: value

        Returns:
            None
        """

    def get_import_export_solids(self) ->bool:
        """get import export solids

        Returns:
            bool
        """

    def set_reset_position_numbers(self, value: bool) ->None:
        """set reset position numbers

        Parameters:
            value: value

        Returns:
            None
        """

    def get_reset_position_numbers(self) ->bool:
        """get reset position numbers

        Returns:
            bool
        """

```

## Missing Items
### Classes cadwork
#### layer_settings

```python
class layer_settings:

    def get_layer(self) ->int:
        """get layer

        Returns:
            int
        """

    def set_layer(self, layer_number: int) ->None:
        """set layer

        Parameters:
            layer_number: layer_number

        Returns:
            None
        """

    def is_without_output(self) ->bool:
        """is without output

        Returns:
            bool
        """

    def set_without_output(self) ->None:
        """set without output

        Returns:
            None
        """

    def is_with_dimensions_output(self) ->bool:
        """is with dimensions output

        Returns:
            bool
        """

    def set_with_dimensions_output(self) ->None:
        """set with dimensions output

        Returns:
            None
        """

    def is_without_dimensions_output(self) ->bool:
        """is without dimensions output

        Returns:
            bool
        """

    def set_without_dimensions_output(self) ->None:
        """set without dimensions output

        Returns:
            None
        """

    def is_with_attributes_output(self) ->bool:
        """is with attributes output

        Returns:
            bool
        """

    def set_with_attributes_output(self) ->None:
        """set with attributes output

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### node_symbol

```python
@unique
class node_symbol(IntEnum):
    """node symbol

    Examples:
        >>> cadwork.node_symbol.SmallSquare
        SmallSquare
    """
    SmallSquare = 1
    """"""
    Square = 2
    """"""
    Cross = 3
    """"""
    Circle = 4
    """"""
    FilledCircle = 5
    """"""
    ChessSquare = 6
    """"""
    HalfFilledSquare = 7
    """"""
    CrossSquare = 8
    """"""
    FilledSquare = 9
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### point_3d

```python
class point_3d:

    def dot(self, p: 'point_3d') ->float:
        """dot

        Parameters:
            p: p

        Returns:
            float
        """

    def cross(self, p: 'point_3d') ->'point_3d':
        """cross

        Parameters:
            p: p

        Returns:
            'point_3d'
        """

    def magnitude(self) ->float:
        """magnitude

        Returns:
            float
        """

    def normalized(self) ->'point_3d':
        """normalized

        Returns:
            'point_3d'
        """

    def distance(self, p: 'point_3d') ->float:
        """distance

        Parameters:
            p: p

        Returns:
            float
        """

    def invert(self) ->'point_3d':
        """invert

        Returns:
            'point_3d'
        """

```

## Missing Items
### Classes cadwork
#### polygon_list

```python
class polygon_list:

    def count(self) ->int:
        """count

        Returns:
            int
        """

    def at(self, index: int) ->point_3d:
        """at

        Parameters:
            index: index

        Returns:
            point_3d
        """

```

## Missing Items
### Classes cadwork
#### process_type

```python
class process_type:

    def set_none(self) ->None:
        """set none

        Returns:
            None
        """

    def is_none(self) ->bool:
        """is none

        Returns:
            bool
        """

    def set_purlin(self) ->None:
        """set purlin

        Returns:
            None
        """

    def is_purlin(self) ->bool:
        """is purlin

        Returns:
            bool
        """

    def set_stud(self) ->None:
        """set stud

        Returns:
            None
        """

    def is_stud(self) ->bool:
        """is stud

        Returns:
            bool
        """

    def set_rafter(self) ->None:
        """set rafter

        Returns:
            None
        """

    def is_rafter(self) ->bool:
        """is rafter

        Returns:
            bool
        """

    def set_jack_rafter(self) ->None:
        """set jack rafter

        Returns:
            None
        """

    def is_jack_rafter(self) ->bool:
        """is jack rafter

        Returns:
            bool
        """

    def set_hip_valley(self) ->None:
        """set hip valley

        Returns:
            None
        """

    def is_hip_valley(self) ->bool:
        """is hip valley

        Returns:
            bool
        """

    def set_log(self) ->None:
        """set log

        Returns:
            None
        """

    def is_log(self) ->bool:
        """is log

        Returns:
            bool
        """

    def set_truss(self) ->None:
        """set truss

        Returns:
            None
        """

    def is_truss(self) ->bool:
        """is truss

        Returns:
            bool
        """

    def set_tread(self) ->None:
        """set tread

        Returns:
            None
        """

    def is_tread(self) ->bool:
        """is tread

        Returns:
            bool
        """

    def set_user_1(self) ->None:
        """set user 1

        Returns:
            None
        """

    def is_user_1(self) ->bool:
        """is user 1

        Returns:
            bool
        """

    def set_user_2(self) ->None:
        """set user 2

        Returns:
            None
        """

    def is_user_2(self) ->bool:
        """is user 2

        Returns:
            bool
        """

    def set_user_3(self) ->None:
        """set user 3

        Returns:
            None
        """

    def is_user_3(self) ->bool:
        """is user 3

        Returns:
            bool
        """

    def set_user_4(self) ->None:
        """set user 4

        Returns:
            None
        """

    def is_user_4(self) ->bool:
        """is user 4

        Returns:
            bool
        """

    def set_user_5(self) ->None:
        """set user 5

        Returns:
            None
        """

    def is_user_5(self) ->bool:
        """is user 5

        Returns:
            bool
        """

    def set_panel_1(self) ->None:
        """set panel 1

        Returns:
            None
        """

    def is_panel_1(self) ->bool:
        """is panel 1

        Returns:
            bool
        """

    def set_panel_2(self) ->None:
        """set panel 2

        Returns:
            None
        """

    def is_panel_2(self) ->bool:
        """is panel 2

        Returns:
            bool
        """

    def set_panel_3(self) ->None:
        """set panel 3

        Returns:
            None
        """

    def is_panel_3(self) ->bool:
        """is panel 3

        Returns:
            bool
        """

    def set_panel_4(self) ->None:
        """set panel 4

        Returns:
            None
        """

    def is_panel_4(self) ->bool:
        """is panel 4

        Returns:
            bool
        """

    def set_panel_5(self) ->None:
        """set panel 5

        Returns:
            None
        """

    def is_panel_5(self) ->bool:
        """is panel 5

        Returns:
            bool
        """

    def set_rough_volume_framed_wall(self) ->None:
        """set rough volume framed wall

        Returns:
            None
        """

    def is_rough_volume_framed_wall(self) ->bool:
        """is rough volume framed wall

        Returns:
            bool
        """

    def set_rough_volume_solid_wood_wall(self) ->None:
        """set rough volume solid wood wall

        Returns:
            None
        """

    def is_rough_volume_solid_wood_wall(self) ->bool:
        """is rough volume solid wood wall

        Returns:
            bool
        """

    def set_rough_volume_log_home(self) ->None:
        """set rough volume log home

        Returns:
            None
        """

    def is_rough_volume_log_home(self) ->bool:
        """is rough volume log home

        Returns:
            bool
        """

```

## Missing Items
### Classes cadwork
#### projection_type

```python
@unique
class projection_type(IntEnum):
    """projection type

    Examples:
        >>> cadwork.projection_type.Perspective
        Perspective
    """
    Perspective = 1
    """"""
    Orthographic = 2
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### rhino_options

```python
class rhino_options:

    def get_materialize_end_types(self) ->bool:
        """get materialize end types

        Returns:
            bool
        """

    def set_materialize_end_types(self, flag: bool) ->None:
        """set materialize end types

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_end_types_counterparts(self) ->bool:
        """get cut end types counterparts

        Returns:
            bool
        """

    def set_cut_end_types_counterparts(self, flag: bool) ->None:
        """set cut end types counterparts

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_drillings(self) ->bool:
        """get cut drillings

        Returns:
            bool
        """

    def set_cut_drillings(self, flag: bool) ->None:
        """set cut drillings

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_mep(self) ->bool:
        """get cut mep

        Returns:
            bool
        """

    def set_cut_mep(self, flag: bool) ->None:
        """set cut mep

        Parameters:
            flag: flag

        Returns:
            None
        """

    def get_cut_openings(self) ->bool:
        """get cut openings

        Returns:
            bool
        """

    def set_cut_openings(self, flag: bool) ->None:
        """set cut openings

        Parameters:
            flag: flag

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### shortcut_key

```python
@unique
class shortcut_key(IntEnum):
    """shortcut key

    Examples:
        >>> cadwork.shortcut_key.F1
        F1
    """
    F1 = 1
    """"""
    F2 = 2
    """"""
    F3 = 3
    """"""
    F4 = 4
    """"""
    F5 = 5
    """"""
    F6 = 6
    """"""
    F7 = 7
    """"""
    F8 = 8
    """"""
    F9 = 9
    """"""
    F10 = 10
    """"""
    F11 = 11
    """"""
    F12 = 12
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### shortcut_key_modifier

```python
@unique
class shortcut_key_modifier(IntEnum):
    """shortcut key modifier

    Examples:
        >>> cadwork.shortcut_key_modifier.shift
        shift
    """
    shift = 1
    """"""
    ctrl = 2
    """"""
    alt = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### text_element_type

```python
@unique
class text_element_type(IntEnum):
    """text element type

    Examples:
        >>> cadwork.text_element_type.line
        line
    """
    line = 0
    """"""
    surface = 1
    """"""
    volume = 2
    """"""
    raster = 3
    """"""

    def __int__(self) ->int:
        return self.value

```

## Missing Items
### Classes cadwork
#### text_object_options

```python
class text_object_options:

    def set_font_name(self, font_name: str) ->None:
        """set font name

        Parameters:
            font_name: font_name

        Returns:
            None
        """

    def get_font_name(self) ->str:
        """get font name

        Returns:
            str
        """

    def set_text(self, text: str) ->None:
        """set text

        Parameters:
            text: text

        Returns:
            None
        """

    def get_text(self) ->str:
        """get text

        Returns:
            str
        """

    def set_bold(self, value: bool) ->None:
        """set bold

        Parameters:
            value: value

        Returns:
            None
        """

    def get_bold(self) ->bool:
        """get bold

        Returns:
            bool
        """

    def set_italic(self, value: bool) ->None:
        """set italic

        Parameters:
            value: value

        Returns:
            None
        """

    def get_italic(self) ->bool:
        """get italic

        Returns:
            bool
        """

    def set_height(self, height: float) ->None:
        """set height

        Parameters:
            height: height

        Returns:
            None
        """

    def get_height(self) ->float:
        """get height

        Returns:
            float
        """

    def set_element_type(self, element_type: text_element_type) ->None:
        """set element type

        Parameters:
            element_type: element_type

        Returns:
            None
        """

    def get_element_type(self) ->text_element_type:
        """get element type

        Returns:
            text_element_type
        """

    def set_thickness(self, thickness: float) ->None:
        """set thickness

        Parameters:
            thickness: thickness

        Returns:
            None
        """

    def get_thickness(self) ->float:
        """get thickness

        Returns:
            float
        """

    def set_color(self, color: int) ->None:
        """set color

        Parameters:
            color: color

        Returns:
            None
        """

    def get_color(self) ->int:
        """get color

        Returns:
            int
        """

    def set_height_relative(self, value: bool) ->None:
        """set height relative

        Parameters:
            value: value

        Returns:
            None
        """

    def get_height_relative(self) ->bool:
        """get height relative

        Returns:
            bool
        """

```

## Missing Items
### Classes cadwork
#### vertex_list

```python
class vertex_list:

    def count(self) ->int:
        """count

        Returns:
            int
        """

    def at(self, index: int) ->point_3d:
        """at

        Parameters:
            index: index

        Returns:
            point_3d
        """

    def append(self, vertex: point_3d) ->None:
        """append

        Parameters:
            vertex: vertex

        Returns:
            None
        """

```

## Missing Items
### Classes cadwork
#### weinmann_mfb_version

```python
@unique
class weinmann_mfb_version(IntEnum):
    """weinmann mfb version

    Examples:
        >>> cadwork.weinmann_mfb_version.wup_2_0
        wup_2_0
    """
    wup_2_0 = 20
    """"""
    wup_3_1 = 31
    """"""
    wup_3_2 = 32
    """"""
    wup_3_3 = 33
    """"""
    wup_3_4 = 34
    """"""

    def __int__(self) ->int:
        return self.value

```

