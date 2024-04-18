---
hide:
  - navigation
---

# Differences from the last to the current version

- What all counts as a change:
    - New functions
    - Changed function descriptions (docstrings)
    - New classes
    - Changed classes descriptions (docstrings)
    - New enums
    - Changed enums descriptions (docstrings)


## New Items
### Functions attribute_controller
#### is_attribute_visible_in_modify_window

```python
def is_attribute_visible_in_modify_window(number: int) ->bool:
    """is attribute visible in modify window

    Parameters:
        number: number

    Returns:
        bool
    """

```

#### set_attribute_visibility_in_modify_window

```python
def set_attribute_visibility_in_modify_window(number: int, visibility: bool
    ) ->None:
    """set attribute visibility in modify window

    Parameters:
        number: number
        visibility: visibility

    Returns:
        None
    """

```

#### set_cutting_set

```python
def set_cutting_set(element_id_list: List[int], cutting_set_name: str) ->bool:
    """set cutting set

    Parameters:
        element_id_list: element_id_list
        cutting_set_name: cutting_set_name

    Returns:
        bool
    """

```

## New Items
### Functions bim_controller
#### get_ifc_predefined_type

```python
def get_ifc_predefined_type(element_id: int) ->ifc_predefined_type:
    """Get the IfcPredefinedType of an element.

    Parameters:
        element_id: element_id

    Returns:
        IfcPredefinedType Wrapper
    """

```

#### set_ifc_predefined_type

```python
def set_ifc_predefined_type(element_i_ds: List[int], predefined_type: None
    ) ->None:
    """Set a predefined type to elements. Attention, if you change the PredefinedType of the elements, you are responsible for ensuring that valid types are set

    Parameters:
        element_i_ds: element_i_ds
        predefined_type: predefined_type

    Returns:
        None
    """

```

## New Items
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

## New Items
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

#### start_standard_element_dialog

```python
def start_standard_element_dialog(standard_element_type: None) ->str:
    """Starts the standard element dialogue based on the chosen element type

    Parameters:
        standard_element_type: standard_element_type

    Returns:
        Returns guid of selected standard element if item is valid, else null
    """

```

#### remove_standard_connector_axis

```python
def remove_standard_connector_axis(a0: str) ->None:
    """remove standard connector axis

    Parameters:
        a0: a0

    Returns:
        None
    """

```

#### remove_standard_beam

```python
def remove_standard_beam(guid: str) ->None:
    """remove standard beam

    Parameters:
        guid: guid

    Returns:
        None
    """

```

#### remove_standard_panel

```python
def remove_standard_panel(guid: str) ->None:
    """remove standard panel

    Parameters:
        guid: guid

    Returns:
        None
    """

```

#### remove_standard_container

```python
def remove_standard_container(guid: str) ->None:
    """remove standard container

    Parameters:
        guid: guid

    Returns:
        None
    """

```

#### remove_standard_export_solid

```python
def remove_standard_export_solid(guid: str) ->None:
    """remove standard export solid

    Parameters:
        guid: guid

    Returns:
        None
    """

```

#### get_user_element_ids_with_count

```python
def get_user_element_ids_with_count(count: int) ->List[int]:
    """get user element ids with count

    Parameters:
        count: count

    Returns:
        List[int]
    """

```

#### cut_scarf_straight

```python
def cut_scarf_straight(elements: List[int], length: float, depth: float,
    clearance_length: float, clearance_depth: float, clearance_hook: float,
    drilling_count: int, drilling_diameter: float, drilling_tolerance: float
    ) ->None:
    """cut scarf straight

    Parameters:
        elements: elements
        length: length
        depth: depth
        clearance_length: clearance_length
        clearance_depth: clearance_depth
        clearance_hook: clearance_hook
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

```

#### cut_scarf_diagonal

```python
def cut_scarf_diagonal(elements: List[int], length: float, depth: float,
    clearance_length: float, clearance_depth: float, drilling_count: int,
    drilling_diameter: float, drilling_tolerance: float) ->None:
    """cut scarf diagonal

    Parameters:
        elements: elements
        length: length
        depth: depth
        clearance_length: clearance_length
        clearance_depth: clearance_depth
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

```

#### cut_scarf_with_wedge

```python
def cut_scarf_with_wedge(elements: List[int], length: float, depth: float,
    clearance_length: float, clearance_depth: float, wedge_width: float,
    drilling_count: int, drilling_diameter: float, drilling_tolerance: float
    ) ->None:
    """cut scarf with wedge

    Parameters:
        elements: elements
        length: length
        depth: depth
        clearance_length: clearance_length
        clearance_depth: clearance_depth
        wedge_width: wedge_width
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

```

#### cut_beam_end_profile

```python
def cut_beam_end_profile(elements: List[int], profile_name: str,
    on_start_face: bool, on_end_face: bool) ->None:
    """cut beam end profile

    Parameters:
        elements: elements
        profile_name: profile_name
        on_start_face: on_start_face
        on_end_face: on_end_face

    Returns:
        None
    """

```

## New Items
### Functions geometry_controller
#### get_round_machine_rough_part_negative_width

```python
def get_round_machine_rough_part_negative_width(element_id: int) ->bool:
    """get round machine rough part negative width

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_negative_width

```python
def set_round_machine_rough_part_negative_width(elements: List[int], value:
    bool) ->None:
    """set round machine rough part negative width

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_round_machine_rough_part_positive_width

```python
def get_round_machine_rough_part_positive_width(element_id: int) ->bool:
    """get round machine rough part positive width

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_positive_width

```python
def set_round_machine_rough_part_positive_width(elements: List[int], value:
    bool) ->None:
    """set round machine rough part positive width

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_round_machine_rough_part_negative_height

```python
def get_round_machine_rough_part_negative_height(element_id: int) ->bool:
    """get round machine rough part negative height

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_negative_height

```python
def set_round_machine_rough_part_negative_height(elements: List[int], value:
    bool) ->None:
    """set round machine rough part negative height

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_round_machine_rough_part_positive_height

```python
def get_round_machine_rough_part_positive_height(element_id: int) ->bool:
    """get round machine rough part positive height

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_positive_height

```python
def set_round_machine_rough_part_positive_height(elements: List[int], value:
    bool) ->None:
    """set round machine rough part positive height

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_round_machine_rough_part_negative_length

```python
def get_round_machine_rough_part_negative_length(element_id: int) ->bool:
    """get round machine rough part negative length

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_negative_length

```python
def set_round_machine_rough_part_negative_length(elements: List[int], value:
    bool) ->None:
    """set round machine rough part negative length

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_round_machine_rough_part_positive_length

```python
def get_round_machine_rough_part_positive_length(element_id: int) ->bool:
    """get round machine rough part positive length

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

```

#### set_round_machine_rough_part_positive_length

```python
def set_round_machine_rough_part_positive_length(elements: List[int], value:
    bool) ->None:
    """set round machine rough part positive length

    Parameters:
        elements: elements
        value: value

    Returns:
        None
    """

```

#### get_standard_element_width_from_guid

```python
def get_standard_element_width_from_guid(standard_element_guid: str) ->float:
    """get standard element width from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """

```

#### get_standard_element_height_from_guid

```python
def get_standard_element_height_from_guid(standard_element_guid: str) ->float:
    """get standard element height from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """

```

#### get_standard_element_length_from_guid

```python
def get_standard_element_length_from_guid(standard_element_guid: str) ->float:
    """get standard element length from guid

    Parameters:
        standard_element_guid: standard_element_guid

    Returns:
        float
    """

```

#### get_standard_element_width_from_name

```python
def get_standard_element_width_from_name(standard_element_name: str) ->float:
    """get standard element width from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """

```

#### get_standard_element_height_from_name

```python
def get_standard_element_height_from_name(standard_element_name: str) ->float:
    """get standard element height from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """

```

#### get_standard_element_length_from_name

```python
def get_standard_element_length_from_name(standard_element_name: str) ->float:
    """get standard element length from name

    Parameters:
        standard_element_name: standard_element_name

    Returns:
        float
    """

```

## New Items
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

## New Items
### Functions material_controller
#### get_material_color_assignment_for_nodes

```python
def get_material_color_assignment_for_nodes(a0: int) ->int:
    """get material color assignment for nodes

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_nodes

```python
def set_material_color_assignment_for_nodes(a0: int, a1: int) ->None:
    """set material color assignment for nodes

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_standard_axes

```python
def get_material_color_assignment_for_standard_axes(a0: int) ->int:
    """get material color assignment for standard axes

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_standard_axes

```python
def set_material_color_assignment_for_standard_axes(a0: int, a1: int) ->None:
    """set material color assignment for standard axes

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_drillings

```python
def get_material_color_assignment_for_drillings(a0: int) ->int:
    """get material color assignment for drillings

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_drillings

```python
def set_material_color_assignment_for_drillings(a0: int, a1: int) ->None:
    """set material color assignment for drillings

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_mep_axes

```python
def get_material_color_assignment_for_mep_axes(a0: int) ->int:
    """get material color assignment for mep axes

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_mep_axes

```python
def set_material_color_assignment_for_mep_axes(a0: int, a1: int) ->None:
    """set material color assignment for mep axes

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_beams

```python
def get_material_color_assignment_for_beams(a0: int) ->int:
    """get material color assignment for beams

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_beams

```python
def set_material_color_assignment_for_beams(a0: int, a1: int) ->None:
    """set material color assignment for beams

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_panels

```python
def get_material_color_assignment_for_panels(a0: int) ->int:
    """get material color assignment for panels

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_panels

```python
def set_material_color_assignment_for_panels(a0: int, a1: int) ->None:
    """set material color assignment for panels

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_auxiliary_elements

```python
def get_material_color_assignment_for_auxiliary_elements(a0: int) ->int:
    """get material color assignment for auxiliary elements

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_auxiliary_elements

```python
def set_material_color_assignment_for_auxiliary_elements(a0: int, a1: int
    ) ->None:
    """set material color assignment for auxiliary elements

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_material_color_assignment_for_surfaces

```python
def get_material_color_assignment_for_surfaces(a0: int) ->int:
    """get material color assignment for surfaces

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_material_color_assignment_for_surfaces

```python
def set_material_color_assignment_for_surfaces(a0: int, a1: int) ->None:
    """set material color assignment for surfaces

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_color

```python
def get_texture_color(a0: int) ->int:
    """get texture color

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_texture_color

```python
def set_texture_color(a0: int, a1: int) ->None:
    """set texture color

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_transparency

```python
def get_texture_transparency(a0: int) ->int:
    """get texture transparency

    Parameters:
        a0: a0

    Returns:
        int
    """

```

#### set_texture_transparency

```python
def set_texture_transparency(a0: int, a1: int) ->None:
    """set texture transparency

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_rotation_angle

```python
def get_texture_rotation_angle(a0: int) ->float:
    """get texture rotation angle

    Parameters:
        a0: a0

    Returns:
        float
    """

```

#### set_texture_rotation_angle

```python
def set_texture_rotation_angle(a0: int, a1: float) ->None:
    """set texture rotation angle

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_length_alignment

```python
def get_texture_length_alignment(a0: int) ->bool:
    """get texture length alignment

    Parameters:
        a0: a0

    Returns:
        bool
    """

```

#### set_texture_length_alignment

```python
def set_texture_length_alignment(a0: int, a1: bool) ->None:
    """set texture length alignment

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_zoom_x

```python
def get_texture_zoom_x(a0: int) ->float:
    """get texture zoom x

    Parameters:
        a0: a0

    Returns:
        float
    """

```

#### set_texture_zoom_x

```python
def set_texture_zoom_x(a0: int, a1: float) ->None:
    """set texture zoom x

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

#### get_texture_zoom_y

```python
def get_texture_zoom_y(a0: int) ->float:
    """get texture zoom y

    Parameters:
        a0: a0

    Returns:
        float
    """

```

#### set_texture_zoom_y

```python
def set_texture_zoom_y(a0: int, a1: float) ->None:
    """set texture zoom y

    Parameters:
        a0: a0
        a1: a1

    Returns:
        None
    """

```

## New Items
### Functions scene_controller
#### is_scene_present

```python
def is_scene_present(name: str) ->bool:
    """Queries of scene with name is present

    Parameters:
        name: name

    Returns:
        presence of scene
    """

```

#### set_group_tab_color

```python
def set_group_tab_color(scene_group_name: str, red: int, green: int, blue: int
    ) ->None:
    """set group tab color

    Parameters:
        scene_group_name: scene_group_name
        red: red
        green: green
        blue: blue

    Returns:
        None
    """

```

#### rename_scene_group

```python
def rename_scene_group(old_name: str, new_name: str) ->None:
    """rename scene group

    Parameters:
        old_name: old_name
        new_name: new_name

    Returns:
        None
    """

```

#### get_group_index_by_name

```python
def get_group_index_by_name(scene_group_name: str) ->int:
    """get group index by name

    Parameters:
        scene_group_name: scene_group_name

    Returns:
        int
    """

```

#### rename_scene_group_by_index

```python
def rename_scene_group_by_index(group_index: int, new_name: str) ->None:
    """rename scene group by index

    Parameters:
        group_index: group_index
        new_name: new_name

    Returns:
        None
    """

```

#### group_scences_with_name

```python
def group_scences_with_name(a0: List[str], a1: str) ->int:
    """group scences with name

    Parameters:
        a0: a0
        a1: a1

    Returns:
        int
    """

```

## New Items
### Functions utility_controller
#### get_3d_main_window_geometry

```python
def get_3d_main_window_geometry() ->'window_geometry':
    """get 3d main window geometry

    Returns:
        window geometry
    """

```

#### get_project_data_keys

```python
def get_project_data_keys() ->List[str]:
    """get project data keys

    Returns:
        List[str]
    """

```

## New Items
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

## New Items
### Classes cadwork
#### ifc_predefined_type

```python
class ifc_predefined_type:

    def is_none(self) ->bool:
        """is none

        Returns:
            bool
        """

    def is_ceiling(self) ->bool:
        """is ceiling

        Returns:
            bool
        """

    def is_cladding(self) ->bool:
        """is cladding

        Returns:
            bool
        """

    def is_flooring(self) ->bool:
        """is flooring

        Returns:
            bool
        """

    def is_insulation(self) ->bool:
        """is insulation

        Returns:
            bool
        """

    def is_membrane(self) ->bool:
        """is membrane

        Returns:
            bool
        """

    def is_roofing(self) ->bool:
        """is roofing

        Returns:
            bool
        """

    def is_sleeving(self) ->bool:
        """is sleeving

        Returns:
            bool
        """

    def is_wrapping(self) ->bool:
        """is wrapping

        Returns:
            bool
        """

    def is_footing_beam(self) ->bool:
        """is footing beam

        Returns:
            bool
        """

    def is_pad_footing(self) ->bool:
        """is pad footing

        Returns:
            bool
        """

    def is_pile_cap(self) ->bool:
        """is pile cap

        Returns:
            bool
        """

    def is_strip_footing(self) ->bool:
        """is strip footing

        Returns:
            bool
        """

    def is_cohesion(self) ->bool:
        """is cohesion

        Returns:
            bool
        """

    def is_friction(self) ->bool:
        """is friction

        Returns:
            bool
        """

    def is_support(self) ->bool:
        """is support

        Returns:
            bool
        """

    def is_balustrade(self) ->bool:
        """is balustrade

        Returns:
            bool
        """

    def is_guardrail(self) ->bool:
        """is guardrail

        Returns:
            bool
        """

    def is_handrail(self) ->bool:
        """is handrail

        Returns:
            bool
        """

    def is_baseslab(self) ->bool:
        """is baseslab

        Returns:
            bool
        """

    def is_floor(self) ->bool:
        """is floor

        Returns:
            bool
        """

    def is_landing(self) ->bool:
        """is landing

        Returns:
            bool
        """

    def is_roof(self) ->bool:
        """is roof

        Returns:
            bool
        """

    def is_beam(self) ->bool:
        """is beam

        Returns:
            bool
        """

    def is_spandrel(self) ->bool:
        """is spandrel

        Returns:
            bool
        """

    def is_tbeam(self) ->bool:
        """is tbeam

        Returns:
            bool
        """

    def is_complex(self) ->bool:
        """is complex

        Returns:
            bool
        """

    def is_element(self) ->bool:
        """is element

        Returns:
            bool
        """

    def is_partial(self) ->bool:
        """is partial

        Returns:
            bool
        """

    def is_provision_for_space(self) ->bool:
        """is provision for space

        Returns:
            bool
        """

    def is_provision_for_void(self) ->bool:
        """is provision for void

        Returns:
            bool
        """

    def is_column(self) ->bool:
        """is column

        Returns:
            bool
        """

    def is_pilaster(self) ->bool:
        """is pilaster

        Returns:
            bool
        """

    def is_molding(self) ->bool:
        """is molding

        Returns:
            bool
        """

    def is_skirtingboard(self) ->bool:
        """is skirtingboard

        Returns:
            bool
        """

    def is_door(self) ->bool:
        """is door

        Returns:
            bool
        """

    def is_gate(self) ->bool:
        """is gate

        Returns:
            bool
        """

    def is_trap_door(self) ->bool:
        """is trap door

        Returns:
            bool
        """

    def is_caisson_foundation(self) ->bool:
        """is caisson foundation

        Returns:
            bool
        """

    def is_brace(self) ->bool:
        """is brace

        Returns:
            bool
        """

    def is_chord(self) ->bool:
        """is chord

        Returns:
            bool
        """

    def is_collar(self) ->bool:
        """is collar

        Returns:
            bool
        """

    def is_member(self) ->bool:
        """is member

        Returns:
            bool
        """

    def is_mullion(self) ->bool:
        """is mullion

        Returns:
            bool
        """

    def is_plate(self) ->bool:
        """is plate

        Returns:
            bool
        """

    def is_post(self) ->bool:
        """is post

        Returns:
            bool
        """

    def is_purlin(self) ->bool:
        """is purlin

        Returns:
            bool
        """

    def is_rafter(self) ->bool:
        """is rafter

        Returns:
            bool
        """

    def is_stringer(self) ->bool:
        """is stringer

        Returns:
            bool
        """

    def is_strut(self) ->bool:
        """is strut

        Returns:
            bool
        """

    def is_stud(self) ->bool:
        """is stud

        Returns:
            bool
        """

    def is_bored(self) ->bool:
        """is bored

        Returns:
            bool
        """

    def is_driven(self) ->bool:
        """is driven

        Returns:
            bool
        """

    def is_jetgrouting(self) ->bool:
        """is jetgrouting

        Returns:
            bool
        """

    def is_curtain_panel(self) ->bool:
        """is curtain panel

        Returns:
            bool
        """

    def is_sheet(self) ->bool:
        """is sheet

        Returns:
            bool
        """

    def is_half_turn_ramp(self) ->bool:
        """is half turn ramp

        Returns:
            bool
        """

    def is_quarter_turn_ramp(self) ->bool:
        """is quarter turn ramp

        Returns:
            bool
        """

    def is_spiral_ramp(self) ->bool:
        """is spiral ramp

        Returns:
            bool
        """

    def is_straight_run_ramp(self) ->bool:
        """is straight run ramp

        Returns:
            bool
        """

    def is_two_quarter_turn_ramp(self) ->bool:
        """is two quarter turn ramp

        Returns:
            bool
        """

    def is_two_straight_run_ramp(self) ->bool:
        """is two straight run ramp

        Returns:
            bool
        """

    def is_barrel_roof(self) ->bool:
        """is barrel roof

        Returns:
            bool
        """

    def is_butterfly_roof(self) ->bool:
        """is butterfly roof

        Returns:
            bool
        """

    def is_dome_roof(self) ->bool:
        """is dome roof

        Returns:
            bool
        """

    def is_flat_roof(self) ->bool:
        """is flat roof

        Returns:
            bool
        """

    def is_freeform(self) ->bool:
        """is freeform

        Returns:
            bool
        """

    def is_gable_roof(self) ->bool:
        """is gable roof

        Returns:
            bool
        """

    def is_gambrel_roof(self) ->bool:
        """is gambrel roof

        Returns:
            bool
        """

    def is_hipped_gable_roof(self) ->bool:
        """is hipped gable roof

        Returns:
            bool
        """

    def is_hip_roof(self) ->bool:
        """is hip roof

        Returns:
            bool
        """

    def is_mansard_roof(self) ->bool:
        """is mansard roof

        Returns:
            bool
        """

    def is_pavilion_roof(self) ->bool:
        """is pavilion roof

        Returns:
            bool
        """

    def is_rainbow_roof(self) ->bool:
        """is rainbow roof

        Returns:
            bool
        """

    def is_shed_roof(self) ->bool:
        """is shed roof

        Returns:
            bool
        """

    def is_curved_run_stair(self) ->bool:
        """is curved run stair

        Returns:
            bool
        """

    def is_double_return_stair(self) ->bool:
        """is double return stair

        Returns:
            bool
        """

    def is_half_turn_stair(self) ->bool:
        """is half turn stair

        Returns:
            bool
        """

    def is_half_winding_stair(self) ->bool:
        """is half winding stair

        Returns:
            bool
        """

    def is_quarter_turn_stair(self) ->bool:
        """is quarter turn stair

        Returns:
            bool
        """

    def is_quarter_winding_stair(self) ->bool:
        """is quarter winding stair

        Returns:
            bool
        """

    def is_spiral_stair(self) ->bool:
        """is spiral stair

        Returns:
            bool
        """

    def is_straight_run_stair(self) ->bool:
        """is straight run stair

        Returns:
            bool
        """

    def is_three_quarter_turn_stair(self) ->bool:
        """is three quarter turn stair

        Returns:
            bool
        """

    def is_three_quarter_winding_stair(self) ->bool:
        """is three quarter winding stair

        Returns:
            bool
        """

    def is_two_curved_run_stair(self) ->bool:
        """is two curved run stair

        Returns:
            bool
        """

    def is_two_quarter_turn_stair(self) ->bool:
        """is two quarter turn stair

        Returns:
            bool
        """

    def is_two_quarter_winding_stair(self) ->bool:
        """is two quarter winding stair

        Returns:
            bool
        """

    def is_two_straight_run_stair(self) ->bool:
        """is two straight run stair

        Returns:
            bool
        """

    def is_curved(self) ->bool:
        """is curved

        Returns:
            bool
        """

    def is_spiral(self) ->bool:
        """is spiral

        Returns:
            bool
        """

    def is_straight(self) ->bool:
        """is straight

        Returns:
            bool
        """

    def is_winder(self) ->bool:
        """is winder

        Returns:
            bool
        """

    def is_elemented_wall(self) ->bool:
        """is elemented wall

        Returns:
            bool
        """

    def is_movable(self) ->bool:
        """is movable

        Returns:
            bool
        """

    def is_parapet(self) ->bool:
        """is parapet

        Returns:
            bool
        """

    def is_partitioning(self) ->bool:
        """is partitioning

        Returns:
            bool
        """

    def is_plumbing_wall(self) ->bool:
        """is plumbing wall

        Returns:
            bool
        """

    def is_polygonal(self) ->bool:
        """is polygonal

        Returns:
            bool
        """

    def is_shear(self) ->bool:
        """is shear

        Returns:
            bool
        """

    def is_solid_wall(self) ->bool:
        """is solid wall

        Returns:
            bool
        """

    def is_standard(self) ->bool:
        """is standard

        Returns:
            bool
        """

    def is_lightdome(self) ->bool:
        """is lightdome

        Returns:
            bool
        """

    def is_skylight(self) ->bool:
        """is skylight

        Returns:
            bool
        """

    def is_window(self) ->bool:
        """is window

        Returns:
            bool
        """

    def is_opening(self) ->bool:
        """is opening

        Returns:
            bool
        """

    def is_recess(self) ->bool:
        """is recess

        Returns:
            bool
        """

    def is_anchorbolt(self) ->bool:
        """is anchorbolt

        Returns:
            bool
        """

    def is_bolt(self) ->bool:
        """is bolt

        Returns:
            bool
        """

    def is_dowel(self) ->bool:
        """is dowel

        Returns:
            bool
        """

    def is_nail(self) ->bool:
        """is nail

        Returns:
            bool
        """

    def is_nail_plate(self) ->bool:
        """is nail plate

        Returns:
            bool
        """

    def is_rivet(self) ->bool:
        """is rivet

        Returns:
            bool
        """

    def is_screw(self) ->bool:
        """is screw

        Returns:
            bool
        """

    def is_shear_connector(self) ->bool:
        """is shear connector

        Returns:
            bool
        """

    def is_staple(self) ->bool:
        """is staple

        Returns:
            bool
        """

    def is_stud_shear_connector(self) ->bool:
        """is stud shear connector

        Returns:
            bool
        """

    def is_glue(self) ->bool:
        """is glue

        Returns:
            bool
        """

    def is_mortar(self) ->bool:
        """is mortar

        Returns:
            bool
        """

    def is_weld(self) ->bool:
        """is weld

        Returns:
            bool
        """

    def is_external(self) ->bool:
        """is external

        Returns:
            bool
        """

    def is_gfa(self) ->bool:
        """is gfa

        Returns:
            bool
        """

    def is_internal(self) ->bool:
        """is internal

        Returns:
            bool
        """

    def is_parking(self) ->bool:
        """is parking

        Returns:
            bool
        """

    def is_space(self) ->bool:
        """is space

        Returns:
            bool
        """

    def is_accessory_assembly(self) ->bool:
        """is accessory assembly

        Returns:
            bool
        """

    def is_arch(self) ->bool:
        """is arch

        Returns:
            bool
        """

    def is_beam_grid(self) ->bool:
        """is beam grid

        Returns:
            bool
        """

    def is_braced_frame(self) ->bool:
        """is braced frame

        Returns:
            bool
        """

    def is_girder(self) ->bool:
        """is girder

        Returns:
            bool
        """

    def is_reinforcement_unit(self) ->bool:
        """is reinforcement unit

        Returns:
            bool
        """

    def is_rigid_frame(self) ->bool:
        """is rigid frame

        Returns:
            bool
        """

    def is_slab_field(self) ->bool:
        """is slab field

        Returns:
            bool
        """

    def is_truss(self) ->bool:
        """is truss

        Returns:
            bool
        """

    def is_cable_ladder_segment(self) ->bool:
        """is cable ladder segment

        Returns:
            bool
        """

    def is_cable_tray_segment(self) ->bool:
        """is cable tray segment

        Returns:
            bool
        """

    def is_cable_trunking_segment(self) ->bool:
        """is cable trunking segment

        Returns:
            bool
        """

    def is_conduit_segment(self) ->bool:
        """is conduit segment

        Returns:
            bool
        """

    def is_busbar_segment(self) ->bool:
        """is busbar segment

        Returns:
            bool
        """

    def is_cable_segment(self) ->bool:
        """is cable segment

        Returns:
            bool
        """

    def is_conductor_segment(self) ->bool:
        """is conductor segment

        Returns:
            bool
        """

    def is_core_segment(self) ->bool:
        """is core segment

        Returns:
            bool
        """

    def is_flexible_segment(self) ->bool:
        """is flexible segment

        Returns:
            bool
        """

    def is_rigid_segment(self) ->bool:
        """is rigid segment

        Returns:
            bool
        """

    def is_culvert(self) ->bool:
        """is culvert

        Returns:
            bool
        """

    def is_gutter(self) ->bool:
        """is gutter

        Returns:
            bool
        """

    def is_spool(self) ->bool:
        """is spool

        Returns:
            bool
        """

    def is_audio_visual_outlet(self) ->bool:
        """is audio visual outlet

        Returns:
            bool
        """

    def is_communications_outlet(self) ->bool:
        """is communications outlet

        Returns:
            bool
        """

    def is_power_outlet(self) ->bool:
        """is power outlet

        Returns:
            bool
        """

    def is_data_outlet(self) ->bool:
        """is data outlet

        Returns:
            bool
        """

    def is_telephone_outlet(self) ->bool:
        """is telephone outlet

        Returns:
            bool
        """

    def is_anchoring(self) ->bool:
        """is anchoring

        Returns:
            bool
        """

    def is_edge(self) ->bool:
        """is edge

        Returns:
            bool
        """

    def is_ligature(self) ->bool:
        """is ligature

        Returns:
            bool
        """

    def is_main(self) ->bool:
        """is main

        Returns:
            bool
        """

    def is_punching(self) ->bool:
        """is punching

        Returns:
            bool
        """

    def is_ring(self) ->bool:
        """is ring

        Returns:
            bool
        """

    def set_none(self) ->None:
        """set none

        Returns:
            None
        """

    def set_ceiling(self) ->None:
        """set ceiling

        Returns:
            None
        """

    def set_cladding(self) ->None:
        """set cladding

        Returns:
            None
        """

    def set_flooring(self) ->None:
        """set flooring

        Returns:
            None
        """

    def set_insulation(self) ->None:
        """set insulation

        Returns:
            None
        """

    def set_membrane(self) ->None:
        """set membrane

        Returns:
            None
        """

    def set_roofing(self) ->None:
        """set roofing

        Returns:
            None
        """

    def set_sleeving(self) ->None:
        """set sleeving

        Returns:
            None
        """

    def set_wrapping(self) ->None:
        """set wrapping

        Returns:
            None
        """

    def set_footing_beam(self) ->None:
        """set footing beam

        Returns:
            None
        """

    def set_pad_footing(self) ->None:
        """set pad footing

        Returns:
            None
        """

    def set_pile_cap(self) ->None:
        """set pile cap

        Returns:
            None
        """

    def set_strip_footing(self) ->None:
        """set strip footing

        Returns:
            None
        """

    def set_cohesion(self) ->None:
        """set cohesion

        Returns:
            None
        """

    def set_friction(self) ->None:
        """set friction

        Returns:
            None
        """

    def set_support(self) ->None:
        """set support

        Returns:
            None
        """

    def set_balustrade(self) ->None:
        """set balustrade

        Returns:
            None
        """

    def set_guardrail(self) ->None:
        """set guardrail

        Returns:
            None
        """

    def set_handrail(self) ->None:
        """set handrail

        Returns:
            None
        """

    def set_baseslab(self) ->None:
        """set baseslab

        Returns:
            None
        """

    def set_floor(self) ->None:
        """set floor

        Returns:
            None
        """

    def set_landing(self) ->None:
        """set landing

        Returns:
            None
        """

    def set_roof(self) ->None:
        """set roof

        Returns:
            None
        """

    def set_beam(self) ->None:
        """set beam

        Returns:
            None
        """

    def set_hollowcore(self) ->None:
        """set hollowcore

        Returns:
            None
        """

    def set_joist(self) ->None:
        """set joist

        Returns:
            None
        """

    def set_lintel(self) ->None:
        """set lintel

        Returns:
            None
        """

    def set_spandrel(self) ->None:
        """set spandrel

        Returns:
            None
        """

    def set_tbeam(self) ->None:
        """set tbeam

        Returns:
            None
        """

    def set_complex(self) ->None:
        """set complex

        Returns:
            None
        """

    def set_element(self) ->None:
        """set element

        Returns:
            None
        """

    def set_partial(self) ->None:
        """set partial

        Returns:
            None
        """

    def set_provision_for_space(self) ->None:
        """set provision for space

        Returns:
            None
        """

    def set_provision_for_void(self) ->None:
        """set provision for void

        Returns:
            None
        """

    def set_column(self) ->None:
        """set column

        Returns:
            None
        """

    def set_pilaster(self) ->None:
        """set pilaster

        Returns:
            None
        """

    def set_molding(self) ->None:
        """set molding

        Returns:
            None
        """

    def set_skirtingboard(self) ->None:
        """set skirtingboard

        Returns:
            None
        """

    def set_door(self) ->None:
        """set door

        Returns:
            None
        """

    def set_gate(self) ->None:
        """set gate

        Returns:
            None
        """

    def set_trap_door(self) ->None:
        """set trap door

        Returns:
            None
        """

    def set_caisson_foundation(self) ->None:
        """set caisson foundation

        Returns:
            None
        """

    def set_brace(self) ->None:
        """set brace

        Returns:
            None
        """

    def set_chord(self) ->None:
        """set chord

        Returns:
            None
        """

    def set_collar(self) ->None:
        """set collar

        Returns:
            None
        """

    def set_member(self) ->None:
        """set member

        Returns:
            None
        """

    def set_mullion(self) ->None:
        """set mullion

        Returns:
            None
        """

    def set_plate(self) ->None:
        """set plate

        Returns:
            None
        """

    def set_post(self) ->None:
        """set post

        Returns:
            None
        """

    def set_purlin(self) ->None:
        """set purlin

        Returns:
            None
        """

    def set_rafter(self) ->None:
        """set rafter

        Returns:
            None
        """

    def set_stringer(self) ->None:
        """set stringer

        Returns:
            None
        """

    def set_strut(self) ->None:
        """set strut

        Returns:
            None
        """

    def set_stud(self) ->None:
        """set stud

        Returns:
            None
        """

    def set_bored(self) ->None:
        """set bored

        Returns:
            None
        """

    def set_driven(self) ->None:
        """set driven

        Returns:
            None
        """

    def set_jetgrouting(self) ->None:
        """set jetgrouting

        Returns:
            None
        """

    def set_curtain_panel(self) ->None:
        """set curtain panel

        Returns:
            None
        """

    def set_sheet(self) ->None:
        """set sheet

        Returns:
            None
        """

    def set_half_turn_ramp(self) ->None:
        """set half turn ramp

        Returns:
            None
        """

    def set_quarter_turn_ramp(self) ->None:
        """set quarter turn ramp

        Returns:
            None
        """

    def set_spiral_ramp(self) ->None:
        """set spiral ramp

        Returns:
            None
        """

    def set_straight_run_ramp(self) ->None:
        """set straight run ramp

        Returns:
            None
        """

    def set_two_quarter_turn_ramp(self) ->None:
        """set two quarter turn ramp

        Returns:
            None
        """

    def set_two_straight_run_ramp(self) ->None:
        """set two straight run ramp

        Returns:
            None
        """

    def set_barrel_roof(self) ->None:
        """set barrel roof

        Returns:
            None
        """

    def set_butterfly_roof(self) ->None:
        """set butterfly roof

        Returns:
            None
        """

    def set_dome_roof(self) ->None:
        """set dome roof

        Returns:
            None
        """

    def set_flat_roof(self) ->None:
        """set flat roof

        Returns:
            None
        """

    def set_freeform(self) ->None:
        """set freeform

        Returns:
            None
        """

    def set_gable_roof(self) ->None:
        """set gable roof

        Returns:
            None
        """

    def set_gambrel_roof(self) ->None:
        """set gambrel roof

        Returns:
            None
        """

    def set_hipped_gable_roof(self) ->None:
        """set hipped gable roof

        Returns:
            None
        """

    def set_hip_roof(self) ->None:
        """set hip roof

        Returns:
            None
        """

    def set_mansard_roof(self) ->None:
        """set mansard roof

        Returns:
            None
        """

    def set_pavilion_roof(self) ->None:
        """set pavilion roof

        Returns:
            None
        """

    def set_rainbow_roof(self) ->None:
        """set rainbow roof

        Returns:
            None
        """

    def set_shed_roof(self) ->None:
        """set shed roof

        Returns:
            None
        """

    def set_curved_run_stair(self) ->None:
        """set curved run stair

        Returns:
            None
        """

    def set_double_return_stair(self) ->None:
        """set double return stair

        Returns:
            None
        """

    def set_half_turn_stair(self) ->None:
        """set half turn stair

        Returns:
            None
        """

    def set_half_winding_stair(self) ->None:
        """set half winding stair

        Returns:
            None
        """

    def set_quarter_turn_stair(self) ->None:
        """set quarter turn stair

        Returns:
            None
        """

    def set_quarter_winding_stair(self) ->None:
        """set quarter winding stair

        Returns:
            None
        """

    def set_spiral_stair(self) ->None:
        """set spiral stair

        Returns:
            None
        """

    def set_straight_run_stair(self) ->None:
        """set straight run stair

        Returns:
            None
        """

    def set_three_quarter_turn_stair(self) ->None:
        """set three quarter turn stair

        Returns:
            None
        """

    def set_three_quarter_winding_stair(self) ->None:
        """set three quarter winding stair

        Returns:
            None
        """

    def set_two_curved_run_stair(self) ->None:
        """set two curved run stair

        Returns:
            None
        """

    def set_two_quarter_turn_stair(self) ->None:
        """set two quarter turn stair

        Returns:
            None
        """

    def set_two_quarter_winding_stair(self) ->None:
        """set two quarter winding stair

        Returns:
            None
        """

    def set_two_straight_run_stair(self) ->None:
        """set two straight run stair

        Returns:
            None
        """

    def set_curved(self) ->None:
        """set curved

        Returns:
            None
        """

    def set_spiral(self) ->None:
        """set spiral

        Returns:
            None
        """

    def set_straight(self) ->None:
        """set straight

        Returns:
            None
        """

    def set_winder(self) ->None:
        """set winder

        Returns:
            None
        """

    def set_elemented_wall(self) ->None:
        """set elemented wall

        Returns:
            None
        """

    def set_movable(self) ->None:
        """set movable

        Returns:
            None
        """

    def set_parapet(self) ->None:
        """set parapet

        Returns:
            None
        """

    def set_partitioning(self) ->None:
        """set partitioning

        Returns:
            None
        """

    def set_plumbing_wall(self) ->None:
        """set plumbing wall

        Returns:
            None
        """

    def set_polygonal(self) ->None:
        """set polygonal

        Returns:
            None
        """

    def set_shear(self) ->None:
        """set shear

        Returns:
            None
        """

    def set_solid_wall(self) ->None:
        """set solid wall

        Returns:
            None
        """

    def set_standard(self) ->None:
        """set standard

        Returns:
            None
        """

    def set_lightdome(self) ->None:
        """set lightdome

        Returns:
            None
        """

    def set_skylight(self) ->None:
        """set skylight

        Returns:
            None
        """

    def set_window(self) ->None:
        """set window

        Returns:
            None
        """

    def set_opening(self) ->None:
        """set opening

        Returns:
            None
        """

    def set_recess(self) ->None:
        """set recess

        Returns:
            None
        """

    def set_anchorbolt(self) ->None:
        """set anchorbolt

        Returns:
            None
        """

    def set_bolt(self) ->None:
        """set bolt

        Returns:
            None
        """

    def set_dowel(self) ->None:
        """set dowel

        Returns:
            None
        """

    def set_nail(self) ->None:
        """set nail

        Returns:
            None
        """

    def set_nailplate(self) ->None:
        """set nailplate

        Returns:
            None
        """

    def set_rivet(self) ->None:
        """set rivet

        Returns:
            None
        """

    def set_screw(self) ->None:
        """set screw

        Returns:
            None
        """

    def set_shearconnector(self) ->None:
        """set shearconnector

        Returns:
            None
        """

    def set_staple(self) ->None:
        """set staple

        Returns:
            None
        """

    def set_studshearconnector(self) ->None:
        """set studshearconnector

        Returns:
            None
        """

    def set_glue(self) ->None:
        """set glue

        Returns:
            None
        """

    def set_mortar(self) ->None:
        """set mortar

        Returns:
            None
        """

    def set_weld(self) ->None:
        """set weld

        Returns:
            None
        """

    def set_external(self) ->None:
        """set external

        Returns:
            None
        """

    def set_gfa(self) ->None:
        """set gfa

        Returns:
            None
        """

    def set_internal(self) ->None:
        """set internal

        Returns:
            None
        """

    def set_parking(self) ->None:
        """set parking

        Returns:
            None
        """

    def set_space(self) ->None:
        """set space

        Returns:
            None
        """

    def set_accessory_assembly(self) ->None:
        """set accessory assembly

        Returns:
            None
        """

    def set_arch(self) ->None:
        """set arch

        Returns:
            None
        """

    def set_beam_grid(self) ->None:
        """set beam grid

        Returns:
            None
        """

    def set_braced_frame(self) ->None:
        """set braced frame

        Returns:
            None
        """

    def set_girder(self) ->None:
        """set girder

        Returns:
            None
        """

    def set_reinforcement_unit(self) ->None:
        """set reinforcement unit

        Returns:
            None
        """

    def set_rigid_frame(self) ->None:
        """set rigid frame

        Returns:
            None
        """

    def set_slab_field(self) ->None:
        """set slab field

        Returns:
            None
        """

    def set_truss(self) ->None:
        """set truss

        Returns:
            None
        """

    def set_cable_ladder_segment(self) ->None:
        """set cable ladder segment

        Returns:
            None
        """

    def set_cable_tray_segment(self) ->None:
        """set cable tray segment

        Returns:
            None
        """

    def set_cable_trunking_segment(self) ->None:
        """set cable trunking segment

        Returns:
            None
        """

    def set_conduit_segment(self) ->None:
        """set conduit segment

        Returns:
            None
        """

    def set_busbar_segment(self) ->None:
        """set busbar segment

        Returns:
            None
        """

    def set_cable_segment(self) ->None:
        """set cable segment

        Returns:
            None
        """

    def set_conductor_segment(self) ->None:
        """set conductor segment

        Returns:
            None
        """

    def set_core_segment(self) ->None:
        """set core segment

        Returns:
            None
        """

    def set_flexible_segment(self) ->None:
        """set flexible segment

        Returns:
            None
        """

    def set_rigid_segment(self) ->None:
        """set rigid segment

        Returns:
            None
        """

    def set_culvert(self) ->None:
        """set culvert

        Returns:
            None
        """

    def set_gutter(self) ->None:
        """set gutter

        Returns:
            None
        """

    def set_spool(self) ->None:
        """set spool

        Returns:
            None
        """

    def set_audio_visual_outlet(self) ->None:
        """set audio visual outlet

        Returns:
            None
        """

    def set_communications_outlet(self) ->None:
        """set communications outlet

        Returns:
            None
        """

    def set_power_outlet(self) ->None:
        """set power outlet

        Returns:
            None
        """

    def set_data_outlet(self) ->None:
        """set data outlet

        Returns:
            None
        """

    def set_telephone_outlet(self) ->None:
        """set telephone outlet

        Returns:
            None
        """

    def set_anchoring(self) ->None:
        """set anchoring

        Returns:
            None
        """

    def set_edge(self) ->None:
        """set edge

        Returns:
            None
        """

    def set_ligature(self) ->None:
        """set ligature

        Returns:
            None
        """

    def set_main(self) ->None:
        """set main

        Returns:
            None
        """

    def set_punching(self) ->None:
        """set punching

        Returns:
            None
        """

    def set_ring(self) ->None:
        """set ring

        Returns:
            None
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
## New Items
### Classes cadwork
#### standard_element_type

```python
@unique
class standard_element_type(IntEnum):
    """standard element type

    Examples:
        >>> cadwork.standard_element_type.beam
        beam
    """
    beam = 0
    """"""
    panel = 2
    """"""
    vba = 3
    """"""
    exportSolid = 4
    """"""
    container = 5
    """"""
    metal = 6
    """"""

    def __int__(self) ->int:
        return self.value

```

## New Items
### Classes cadwork
#### window_geometry

```python
class window_geometry:


    class point:

        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self):
        self.bottom_left = self.point(0, 0)
        self.bottom_right = self.point(0, 0)
        self.top_left = self.point(0, 0)
        self.top_right = self.point(0, 0)

```




