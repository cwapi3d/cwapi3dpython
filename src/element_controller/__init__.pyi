from typing import List
from cadwork import edge_list
from cadwork import element_module_properties
from cadwork import facet_list
from cadwork import point_3d
from cadwork import text_object_options
from cadwork.coordinate_system_data import coordinate_system_data

def delete_elements(element_id_list: List[int]) -> None:
    """delete elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def join_elements(element_id_list: List[int]) -> None:
    """join elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def join_top_level_elements(element_id_list: List[int]) -> None:
    """join top level elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def create_rectangular_beam_points(width: float, height: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular beam points

    Parameters:
        width: width
        height: height
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_circular_beam_points(diameter: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create circular beam points

    Parameters:
        diameter: diameter
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_square_beam_points(width: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create square beam points

    Parameters:
        width: width
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_rectangular_beam_vectors(width: float, height: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create rectangular beam vectors

    Parameters:
        width: width
        height: height
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_circular_beam_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create circular beam vectors

    Parameters:
        diameter: diameter
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_square_beam_vectors(width: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create square beam vectors

    Parameters:
        width: width
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_rectangular_panel_points(width: float, thickness: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular panel points

    Parameters:
        width: width
        thickness: thickness
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_rectangular_panel_vectors(width: float, thickness: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create rectangular panel vectors

    Parameters:
        width: width
        thickness: thickness
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_drilling_points(diameter: float, p1: point_3d, p2: point_3d) -> int:
    """create drilling points

    Parameters:
        diameter: diameter
        p1: p1
        p2: p2

    Returns:
        int
    """

def create_drilling_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d) -> int:
    """create drilling vectors

    Parameters:
        diameter: diameter
        length: length
        p1: p1
        xl: xl

    Returns:
        int
    """

def create_line_points(p1: point_3d, p2: point_3d) -> int:
    """create line points

    Parameters:
        p1: p1
        p2: p2

    Returns:
        int
    """

def create_line_vectors(length: float, p1: point_3d, xl: point_3d) -> int:
    """create line vectors

    Parameters:
        length: length
        p1: p1
        xl: xl

    Returns:
        int
    """

def create_node(p1: point_3d) -> int:
    """create node

    Parameters:
        p1: p1

    Returns:
        int
    """

def solder_elements(element_id_list: List[int]) -> List[int]:
    """solder elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        List[int]
    """

def convert_beam_to_panel(element_id_list: List[int]) -> None:
    """convert beam to panel

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def convert_panel_to_beam(element_id_list: List[int]) -> None:
    """convert panel to beam

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def delete_all_element_end_types(element_id_list: List[int]) -> None:
    """delete all element end types

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def delete_all_element_processes(element_id_list: List[int]) -> None:
    """delete all element processes

    Parameters:
        element_id_list: element_id_list

    Returns:
        None
    """

def move_element(element_id_list: List[int], vector: point_3d) -> None:
    """move element

    Parameters:
        element_id_list: element_id_list
        vector: vector

    Returns:
        None
    """

def create_polygon_beam(polygon_vertices: List[point_3d], thickness: float, xl: point_3d, zl: point_3d) -> int:
    """create polygon beam

    Parameters:
        polygon_vertices: polygon_vertices
        thickness: thickness
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_text_object(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float) -> int:
    """create text object

    Parameters:
        text: text
        position: position
        xl: xl
        zl: zl
        size: size

    Returns:
        int
    """

def copy_elements(element_id_list: List[int], copy_vector: point_3d) -> List[int]:
    """copy elements

    Parameters:
        element_id_list: element_id_list
        copy_vector: copy_vector

    Returns:
        List[int]
    """

def rotate_elements(element_id_list: List[int], origin: point_3d, rotation_axis: point_3d, rotation_angle: float) -> None:
    """rotate elements

    Parameters:
        element_id_list: element_id_list
        origin: origin
        rotation_axis: rotation_axis
        rotation_angle: rotation_angle

    Returns:
        None
    """

def subtract_elements(hard_elements: List[int], soft_elements: List[int]) -> List[int]:
    """subtract elements

    Parameters:
        hard_elements: hard_elements
        soft_elements: soft_elements

    Returns:
        List[int]
    """

def check_element_id(element_id: int) -> bool:
    """check element id

    Parameters:
        element_id: element_id

    Returns:
        bool
    """

def start_element_module_calculation(covers: List[int]) -> None:
    """start element module calculation

    Parameters:
        covers: covers

    Returns:
        None
    """

def set_element_detail_path(path: str) -> None:
    """set element detail path

    Parameters:
        path: path

    Returns:
        None
    """

def get_element_from_cadwork_guid(cadwork_guid: str) -> int:
    """get element from cadwork guid

    Parameters:
        cadwork_guid: cadwork_guid

    Returns:
        int
    """

def add_elements_to_undo(elements: List[int], cmd: int) -> None:
    """add elements to undo

    Parameters:
        elements: elements
        cmd: cmd

    Returns:
        None
    """

def make_undo() -> None:
    """make undo

    Returns:
        None
    """

def make_redo() -> None:
    """make redo

    Returns:
        None
    """

def split_elements(elements: List[int]) -> None:
    """split elements

    Parameters:
        elements: elements

    Returns:
        None
    """

def set_line_to_marking_line(elements: List[int]) -> None:
    """set line to marking line

    Parameters:
        elements: elements

    Returns:
        None
    """

def set_line_to_normal_line(elements: List[int]) -> None:
    """set line to normal line

    Parameters:
        elements: elements

    Returns:
        None
    """

def create_auto_export_solid_from_standard(elements: List[int], output_name: str, standard_element_name: str) -> int:
    """create auto export solid from standard

    Parameters:
        elements: elements
        output_name: output_name
        standard_element_name: standard_element_name

    Returns:
        int
    """

def set_element_module_properties_for_elements(elements: List[int], properties: None) -> None:
    """set element module properties for elements

    Parameters:
        elements: elements
        properties: properties

    Returns:
        None
    """

def create_text_object_with_font(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float, font_name: str) -> int:
    """create text object with font

    Parameters:
        text: text
        position: position
        xl: xl
        zl: zl
        size: size
        font_name: font_name

    Returns:
        int
    """

def apply_transformation_coordinate(elements: List[int], old_point: point_3d, old_xl: point_3d, old_yl: point_3d, new_point: point_3d, new_xl: point_3d, new_yl: point_3d) -> None:
    """apply transformation coordinate

    Parameters:
        elements: elements
        old_point: old_point
        old_xl: old_xl
        old_yl: old_yl
        new_point: new_point
        new_xl: new_xl
        new_yl: new_yl

    Returns:
        None
    """

def delete_elements_with_undo(elements: List[int]) -> None:
    """delete elements with undo

    Parameters:
        elements: elements

    Returns:
        None
    """

def add_created_elements_to_undo(elements: List[int]) -> None:
    """add created elements to undo

    Parameters:
        elements: elements

    Returns:
        None
    """

def add_modified_elements_to_undo(elements: List[int]) -> None:
    """add modified elements to undo

    Parameters:
        elements: elements

    Returns:
        None
    """

def recreate_elements(elements: List[int]) -> None:
    """recreate elements

    Parameters:
        elements: elements

    Returns:
        None
    """

def create_multi_wall(elements: List[int]) -> None:
    """create multi wall

    Parameters:
        elements: elements

    Returns:
        None
    """

def get_user_element_ids() -> List[int]:
    """get user element ids

    Returns:
        List[int]
    """

def get_user_element_ids_with_existing(elements: List[int]) -> List[int]:
    """get user element ids with existing

    Parameters:
        elements: elements

    Returns:
        List[int]
    """

def clear_errors() -> None:
    """clear errors

    Returns:
        None
    """

def glide_elements(element_i_ds: List[int], glide_point: point_3d) -> None:
    """glide elements

    Parameters:
        element_i_ds: element_i_ds
        glide_point: glide_point

    Returns:
        None
    """

def cut_elements_with_miter(first_id: int, second_id: int) -> bool:
    """cut elements with miter

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        bool
    """

def cut_element_with_plane(element_id: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """cut element with plane

    Parameters:
        element_id: element_id
        cut_plane_normal_vector: cut_plane_normal_vector
        distance_from_global_origin: distance_from_global_origin

    Returns:
        bool
    """

def create_circular_mep(diameter: float, points: List[point_3d]) -> int:
    """create circular mep

    Parameters:
        diameter: diameter
        points: points

    Returns:
        int
    """

def create_rectangular_mep(width: float, depth: float, points: List[point_3d]) -> int:
    """create rectangular mep

    Parameters:
        width: width
        depth: depth
        points: points

    Returns:
        int
    """

def slice_element_with_plane(element_id: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """slice element with plane

    Parameters:
        element_id: element_id
        cut_plane_normal_vector: cut_plane_normal_vector
        distance_from_global_origin: distance_from_global_origin

    Returns:
        bool
    """

def create_auto_container_from_standard(elements: List[int], output_name: str, standard_element_name: str) -> int:
    """create auto container from standard

    Parameters:
        elements: elements
        output_name: output_name
        standard_element_name: standard_element_name

    Returns:
        int
    """

def create_auto_export_solid_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto export solid from standard with reference

    Parameters:
        elements: elements
        output_name: output_name
        standard_element_name: standard_element_name
        reference_id: reference_id

    Returns:
        int
    """

def create_auto_container_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto container from standard with reference

    Parameters:
        elements: elements
        output_name: output_name
        standard_element_name: standard_element_name
        reference_id: reference_id

    Returns:
        int
    """

def create_surface(surface_vertices: List[point_3d]) -> int:
    """create surface

    Parameters:
        surface_vertices: surface_vertices

    Returns:
        int
    """

def stretch_start_facet(elements: List[int], stretch_vector: point_3d) -> None:
    """stretch start facet

    Parameters:
        elements: elements
        stretch_vector: a vector that defines the stretch direction and distance

    Returns:
        None
    """

def stretch_end_facet(elements: List[int], stretch_vector: point_3d) -> None:
    """stretch end facet

    Parameters:
         elements: elements
        stretch_vector: a vector that defines the stretch direction and distance

    Returns:
        None
    """

def set_export_solid_contents(export_solid_id: int, element_i_ds: List[int]) -> None:
    """set export solid contents

    Parameters:
        export_solid_id: export_solid_id
        element_i_ds: element_i_ds

    Returns:
        None
    """

def set_container_contents(container_id: int, element_i_ds: List[int]) -> None:
    """set container contents

    Parameters:
        container_id: container_id
        element_i_ds: element_i_ds

    Returns:
        None
    """

def set_parent_opening_variants_opening_angle(element_i_ds: List[int], angle: float) -> None:
    """set parent opening variants opening angle

    Parameters:
        element_i_ds: element_i_ds
        angle: angle

    Returns:
        None
    """

def mirror_move_elements(elements: List[int], plane: point_3d, plane_distance: float) -> None:
    """mirror move elements

    Parameters:
        elements: elements
        plane: plane
        plane_distance: plane_distance

    Returns:
        None
    """

def mirror_copy_elements(elements: List[int], plane: point_3d, plane_distance: float) -> List[int]:
    """mirror copy elements

    Parameters:
        elements: elements
        plane: plane
        plane_distance: plane_distance

    Returns:
        List[int]
    """

def reset_element_cadwork_guid(element_id: int) -> None:
    """reset element cadwork guid

    Parameters:
        element_id: element_id

    Returns:
        None
    """

def create_standard_beam_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard beam points

    Parameters:
        standard_element_name: standard_element_name
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_standard_beam_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard beam vectors

    Parameters:
        standard_element_name: standard_element_name
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_standard_panel_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard panel points

    Parameters:
        standard_element_name: standard_element_name
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_standard_panel_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard panel vectors

    Parameters:
        standard_element_name: standard_element_name
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def create_standard_steel_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard steel points

    Parameters:
        standard_element_name: standard_element_name
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_standard_steel_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard steel vectors

    Parameters:
        standard_element_name: standard_element_name
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def move_element_with_undo(element_id_list: List[int], vector: point_3d) -> None:
    """move element with undo

    Parameters:
        element_id_list: element_id_list
        vector: vector

    Returns:
        None
    """

def create_normal_axis_points(p1: point_3d, p2: point_3d) -> int:
    """create normal axis points

    Parameters:
        p1: p1
        p2: p2

    Returns:
        int
    """

def create_normal_axis_vectors(length: float, p1: point_3d, xl: point_3d) -> int:
    """create normal axis vectors

    Parameters:
        length: length
        p1: p1
        xl: xl

    Returns:
        int
    """

def convert_bolt_to_standardconnector(elements: List[int], standard_element_name: str) -> None:
    """convert bolt to standardconnector

    Parameters:
        elements: elements
        standard_element_name: standard_element_name

    Returns:
        None
    """

def extrude_surface_to_auxiliary_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to auxiliary vector

    Parameters:
        surface: surface
        vector: vector

    Returns:
        int
    """

def extrude_surface_to_panel_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to panel vector

    Parameters:
        surface: surface
        vector: vector

    Returns:
        int
    """

def extrude_surface_to_beam_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to beam vector

    Parameters:
        surface: surface
        vector: vector

    Returns:
        int
    """

def convert_container_to_container_block(elements: List[int]) -> None:
    """convert container to container block

    Parameters:
        elements: elements

    Returns:
        None
    """

def create_bounding_box_local(reference_element: int, elements: List[int]) -> int:
    """create bounding box local

    Parameters:
        reference_element: reference_element
        elements: elements

    Returns:
        int
    """

def create_bounding_box_global(elements: List[int]) -> int:
    """create bounding box global

    Parameters:
        elements: elements

    Returns:
        int
    """

def convert_auxiliary_to_panel(elements: List[int]) -> None:
    """convert auxiliary to panel

    Parameters:
        elements: elements

    Returns:
        None
    """

def convert_auxiliary_to_beam(elements: List[int]) -> None:
    """convert auxiliary to beam

    Parameters:
        elements: elements

    Returns:
        None
    """

def auto_set_rough_volume_situation(elements: List[int]) -> None:
    """auto set rough volume situation

    Parameters:
        elements: elements

    Returns:
        None
    """

def rough_volume_situation_manual(cover: int, add_partner: List[int], remove_partner: List[int]) -> None:
    """rough volume situation manual

    Parameters:
        cover: cover
        add_partner: add_partner
        remove_partner: remove_partner

    Returns:
        None
    """

def auto_set_parts_situation(elements: List[int]) -> None:
    """auto set parts situation

    Parameters:
        elements: elements

    Returns:
        None
    """

def parts_situation_manual(cover: int, add_childs: List[int], remove_childs: List[int]) -> None:
    """parts situation manual

    Parameters:
        cover: cover
        add_childs: add_childs
        remove_childs: remove_childs

    Returns:
        None
    """

def activate_rv_without_situation() -> List[int]:
    """activate rv without situation

    Returns:
        List[int]
    """

def activate_parts_without_situation() -> List[int]:
    """activate parts without situation

    Returns:
        List[int]
    """

def add_elements_to_detail(elements: List[int], detail: int) -> None:
    """add elements to detail

    Parameters:
        elements: The list of elements to be added to the detail
        detail: The ID of the detail

    Returns:
        None
    """

def subtract_elements_with_undo(hard_elements: List[int], soft_elements: List[int], with_undo: bool) -> List[int]:
    """subtract elements with undo

    Parameters:
        hard_elements: hard_elements
        soft_elements: soft_elements
        with_undo: with_undo

    Returns:
        List[int]
    """

def create_linear_optimization(elements: List[int], optimization_number: int, total_length: float, start_cut: float, end_cut: float, saw_kerf: float, is_production_list: bool) -> int:
    """create linear optimization

    Parameters:
        elements: elements
        optimization_number: optimization_number
        total_length: total_length
        start_cut: start_cut
        end_cut: end_cut
        saw_kerf: saw_kerf
        is_production_list: is_production_list

    Returns:
        int
    """

def start_element_module_calculation_silently(covers: List[int]) -> None:
    """start element module calculation silently

    Parameters:
        covers: covers

    Returns:
        None
    """

def replace_physical_drillings_with_drilling_axes(elements: List[int], mininum_diameter: float, maximum_diameter: float) -> List[int]:
    """replace physical drillings with drilling axes

    Parameters:
        elements: elements
        mininum_diameter: mininum_diameter
        maximum_diameter: maximum_diameter

    Returns:
        List[int]
    """

def cut_element_with_processing_group(soft_element: int, processing: int) -> None:
    """cut element with processing group

    Parameters:
        soft_element: soft_element
        processing: processing

    Returns:
        None
    """

def add_element_to_detail(elements: List[int], detail: int) -> None:
    """add element to detail

    Parameters:
        elements: elements
        detail: detail

    Returns:
        None
    """

def convert_elements_to_auxiliary_elements(elements: List[int]) -> None:
    """convert elements to auxiliary elements

    Parameters:
        elements: elements

    Returns:
        None
    """

def create_circular_axis_points(diameter: float, p1: point_3d, p2: point_3d) -> int:
    """create circular axis points

    Parameters:
        diameter: diameter
        p1: p1
        p2: p2

    Returns:
        int
    """

def create_circular_axis_vector(diameter: float, length: float, p1: point_3d, xl: point_3d) -> int:
    """create circular axis vector

    Parameters:
        diameter: diameter
        length: length
        p1: p1
        xl: xl

    Returns:
        int
    """

def create_polygon_panel(polygon_vertices: List[point_3d], thickness: float, xl: point_3d, zl: point_3d) -> int:
    """create polygon panel

    Parameters:
        polygon_vertices: polygon_vertices
        thickness: thickness
        xl: xl
        zl: zl

    Returns:
        int
    """

def cut_elements_with_overmeasure(hard_elements: List[int], soft_elements: List[int]) -> None:
    """cut elements with overmeasure

    Parameters:
        hard_elements: hard_elements
        soft_elements: soft_elements

    Returns:
        None
    """

def cut_log_corner_joint(settings_name: str, elements: List[int]) -> None:
    """cut log corner joint

    Parameters:
        settings_name: settings_name
        elements: elements

    Returns:
        None
    """

def get_edge_selection(elements: List[int]) -> edge_list:
    """get edge selection

    Parameters:
        elements: elements

    Returns:
        edge_list
    """

def get_facets_with_lasso(elements: List[int]) -> facet_list:
    """get facets with lasso

    Parameters:
        elements: elements

    Returns:
        facet_list
    """

def create_standard_element_from_guid_points(guid: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard element from guid points

    Parameters:
        guid: guid
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

def create_standard_element_from_guid_vectors(guid: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard element from guid vectors

    Parameters:
        guid: guid
        length: length
        p1: p1
        xl: xl
        zl: zl

    Returns:
        int
    """

def fillet_edge(element_id: int, edge_start: point_3d, edge_end: point_3d, radius: float) -> None:
    """fillet edge

    Parameters:
        element_id: element_id
        edge_start: edge_start
        edge_end: edge_end
        radius: radius

    Returns:
        None
    """

def chamfer_edge(element_id: int, edge_start: point_3d, edge_end: point_3d, length: float) -> None:
    """chamfer edge

    Parameters:
        element_id: element_id
        edge_start: edge_start
        edge_end: edge_end
        length: length

    Returns:
        None
    """

def convert_drilling_to_circular_beam(elements: List[int]) -> None:
    """convert drilling to circular beam

    Parameters:
        elements: elements

    Returns:
        None
    """

def convert_lines_to_surfaces(elements: List[int]) -> List[int]:
    """convert lines to surfaces

    Parameters:
        elements: elements

    Returns:
        List[int]
    """

def convert_surfaces_to_volume(elements: List[int]) -> int:
    """convert surfaces to volume

    Parameters:
        elements: elements

    Returns:
        int
    """

def cut_corner_lap(elements: List[int], depth: float, clearance_base: float, clearance_side: float, backcut: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut corner lap

    Parameters:
        elements: elements
        depth: depth
        clearance_base: clearance_base
        clearance_side: clearance_side
        backcut: backcut
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def cut_t_lap(elements: List[int], depth: float, clearance_base: float, clearance_side: float, backcut: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut t lap

    Parameters:
        elements: elements
        depth: depth
        clearance_base: clearance_base
        clearance_side: clearance_side
        backcut: backcut
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def cut_cross_lap(elements: List[int], depth: float, clearance_base: float, clearance_side: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut cross lap

    Parameters:
        elements: elements
        depth: depth
        clearance_base: clearance_base
        clearance_side: clearance_side
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def delete_processes_keep_cutting_bodies(elements: List[int], keep_cutting_elements_only: bool) -> List[int]:
    """delete processes keep cutting bodies

    Parameters:
        elements: elements
        keep_cutting_elements_only: keep_cutting_elements_only

    Returns:
        List[int]
    """

def cut_double_tenon(elements: List[int], depth1: float, depth2: float, clearance: float, backcut: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut double tenon

    Parameters:
        elements: elements
        depth1: depth1
        depth2: depth2
        clearance: clearance
        backcut: backcut
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def get_coordinate_system_data_nesting_child(nesting_parent_id: int, nesting_child_id: int) -> 'coordinate_system_data':
    """get coordinate system data nesting child

    Parameters:
        nesting_parent_id: nesting_parent_id
        nesting_child_id: nesting_child_id

    Returns:
        coordinate_system_data
    """

def cut_half_lap(elements: List[int], length: float, clearance_length: float, clearance_depth: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut half lap

    Parameters:
        elements: elements
        length: length
        clearance_length: clearance_length
        clearance_depth: clearance_depth
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def cut_simple_scarf(elements: List[int], length: float, depth: float, clearance_length: float, clearance_depth: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut simple scarf

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

def cut_diagonal_cut(elements: List[int], length: float, clearance_length: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
    """cut diagonal cut

    Parameters:
        elements: elements
        length: length
        clearance_length: clearance_length
        drilling_count: drilling_count
        drilling_diameter: drilling_diameter
        drilling_tolerance: drilling_tolerance

    Returns:
        None
    """

def get_all_identifiable_element_ids() -> List[int]:
    """get all identifiable element ids

    Returns:
        List[int]
    """

def get_visible_identifiable_element_ids() -> List[int]:
    """get visible identifiable element ids

    Returns:
        List[int]
    """

def get_invisible_identifiable_element_ids() -> List[int]:
    """get invisible identifiable element ids

    Returns:
        List[int]
    """

def get_active_identifiable_element_ids() -> List[int]:
    """get active identifiable element ids

    Returns:
        List[int]
    """

def get_inactive_all_identifiable_element_ids() -> List[int]:
    """get inactive all identifiable element ids

    Returns:
        List[int]
    """

def get_inactive_visible_identifiable_element_ids() -> List[int]:
    """get inactive visible identifiable element ids

    Returns:
        List[int]
    """

def check_if_point_is_in_element(point: point_3d, element_id: int) -> bool:
    """check if point is in element

    Parameters:
        point: point
        element_id: element_id

    Returns:
        bool
    """

def check_if_point_is_on_element(point: point_3d, element_id: int) -> bool:
    """check if point is on element

    Parameters:
        point: point
        element_id: element_id

    Returns:
        bool
    """

def get_element_contact_facets(first_id: int, second_id: int) -> facet_list:
    """get element contact facets

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        facet_list
    """

def get_element_raw_interface_vertices(first_id: int, second_id: int) -> List[point_3d]:
    """get element raw interface vertices

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        List[point_3d]
    """

def get_standard_export_solid_list() -> List[str]:
    """get standard export solid list

    Returns:
        List[str]
    """

def get_standard_container_list() -> List[str]:
    """get standard container list

    Returns:
        List[str]
    """

def get_standard_beam_list() -> List[str]:
    """get standard beam list

    Returns:
        List[str]
    """

def get_standard_panel_list() -> List[str]:
    """get standard panel list

    Returns:
        List[str]
    """

def get_variant_sibling_element_ids(element_id: int) -> List[int]:
    """get variant sibling element ids

    Parameters:
        element_id: element_id

    Returns:
        List[int]
    """

def get_reference_element(element: int) -> int:
    """get reference element

    Parameters:
        element: element

    Returns:
        int
    """

def get_element_contact_vertices(first_id: int, second_id: int) -> List[point_3d]:
    """get element contact vertices

    Parameters:
        first_id: first_id
        second_id: second_id

    Returns:
        List[point_3d]
    """

def get_nesting_parent_id(element_id: int) -> int:
    """get nesting parent id

    Parameters:
        element_id: element_id

    Returns:
        int
    """

def check_if_elements_are_in_collision(first_element_id: int, second_element_id: int) -> bool:
    """check if elements are in collision

    Parameters:
        first_element_id: first_element_id
        second_element_id: second_element_id

    Returns:
        bool
    """

def check_if_elements_are_in_contact(first_element_id: int, second_element_id: int) -> bool:
    """check if elements are in contact

    Parameters:
        first_element_id: first_element_id
        second_element_id: second_element_id

    Returns:
        bool
    """

def get_element_module_properties_for_element(element_id: int) -> element_module_properties:
    """get element module properties for element

    Parameters:
        element_id: element_id

    Returns:
        element_module_properties
    """

def get_element_type_description(element_id: int) -> str:
    """get element type description

    Parameters:
        element_id: element_id

    Returns:
        str
    """

def get_opening_variant_ids(elements: List[int], opening_type: int) -> List[int]:
    """get opening variant ids

    Parameters:
        elements: elements
        opening_type: opening_type

    Returns:
        List[int]
    """

def get_parent_container_id(element_id: int) -> int:
    """get parent container id

    Parameters:
        element_id: element_id

    Returns:
        int
    """

def get_export_solid_content_elements(element_id: int) -> List[int]:
    """get export solid content elements

    Parameters:
        element_id: element_id

    Returns:
        List[int]
    """

def get_container_content_elements(element_id: int) -> List[int]:
    """get container content elements

    Parameters:
        element_id: element_id

    Returns:
        List[int]
    """

def get_element_detail_path() -> str:
    """get element detail path

    Returns:
        str
    """

def get_element_cadwork_guid(element_id: int) -> str:
    """get element cadwork guid

    Parameters:
        element_id: element_id

    Returns:
        str
    """

def get_bounding_box_vertices_local(reference_element: int, elements: List[int]) -> List[point_3d]:
    """get bounding box vertices local

    Parameters:
        reference_element: reference_element
        elements: elements

    Returns:
        List[point_3d]
    """

def get_bounding_box_vertices_global(elements: List[int]) -> List[point_3d]:
    """get bounding box vertices global

    Parameters:
        elements: elements

    Returns:
        List[point_3d]
    """

def get_all_nesting_raw_parts() -> List[int]:
    """get all nesting raw parts

    Returns:
        List[int]
    """

def get_joined_elements(element_id: int) -> List[int]:
    """get joined elements

    Parameters:
        element_id: element_id

    Returns:
        List[int]
    """

def check_element_duplicates(elements: List[int]) -> List[int]:
    """check element duplicates

    Parameters:
        elements: elements

    Returns:
        List[int]
    """

def get_elements_in_contact(element: int) -> List[int]:
    """get elements in contact

    Parameters:
        element: element

    Returns:
        List[int]
    """

def create_text_object_with_options(position: point_3d, xl: point_3d, zl: point_3d, text_options: text_object_options) -> int:
    """create text object with options

    Parameters:
        position: position
        xl: xl
        zl: zl
        text_options: text_options

    Returns:
        int
    """

def convert_surfaces_to_roof_surfaces(elements: List[int], roof_name: str) -> None:
    """convert surfaces to roof surfaces

    Parameters:
        elements: elements
        roof_name: roof_name

    Returns:
        None
    """

def start_standard_element_dialog(standard_element_type: None) -> str:
    """start standard element dialog

    Parameters:
        standard_element_type: standard_element_type

    Returns:
        str
    """

def remove_standard_connector_axis(guid: str) -> None:
    """remove standard connector axis

    Parameters:
        guid: guid

    Returns:
        None
    """

def remove_standard_beam(guid: str) -> None:
    """remove standard beam

    Parameters:
        guid: guid

    Returns:
        None
    """

def remove_standard_panel(guid: str) -> None:
    """remove standard panel

    Parameters:
        guid: guid

    Returns:
        None
    """

def remove_standard_container(guid: str) -> None:
    """remove standard container

    Parameters:
        guid: guid

    Returns:
        None
    """

def remove_standard_export_solid(guid: str) -> None:
    """remove standard export solid

    Parameters:
        guid: guid

    Returns:
        None
    """

def get_user_element_ids_with_count(count: int) -> List[int]:
    """get user element ids with count

    Parameters:
        count: count

    Returns:
        List[int]
    """

def cut_scarf_straight(elements: List[int], length: float, depth: float, clearance_length: float, clearance_depth: float, clearance_hook: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
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

def cut_scarf_diagonal(elements: List[int], length: float, depth: float, clearance_length: float, clearance_depth: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
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

def cut_scarf_with_wedge(elements: List[int], length: float, depth: float, clearance_length: float, clearance_depth: float, wedge_width: float, drilling_count: int, drilling_diameter: float, drilling_tolerance: float) -> None:
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

def cut_beam_end_profile(elements: List[int], profile_name: str, on_start_face: bool, on_end_face: bool) -> None:
    """cut beam end profile

    Parameters:
        elements: elements
        profile_name: profile_name
        on_start_face: on_start_face
        on_end_face: on_end_face

    Returns:
        None
    """

def create_truncated_cone_beam_points(start_diameter: float, end_diameter: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
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

def create_truncated_cone_beam_vectors(start_diameter: float, end_diameter: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
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

def create_spline_line(spline_points: None) -> int:
    """create spline line

    Parameters:
        spline_points: spline_points

    Returns:
        int
    """

def unjoin_elements(element_id_list: List[int]) -> bool:
    """unjoin elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        bool
    """

def unjoin_top_level_elements(element_id_list: List[int]) -> bool:
    """unjoin top level elements

    Parameters:
        element_id_list: element_id_list

    Returns:
        bool
    """

def set_element_group_single_select_mode() -> None:
    """set element group single select mode

    Returns:
        None
    """

def set_element_group_multi_select_mode() -> None:
    """set element group multi select mode

    Returns:
        None
    """

def convert_circular_beam_to_drilling(elements: List[int]) -> None:
    """convert circular beam to drilling

    Parameters:
        elements: elements

    Returns:
        None
    """

def slice_elements_with_plane_and_get_new_elements(element: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> List[int]:
    """slice elements with plane and get new elements

    Parameters:
        element: The ID of the element to be sliced
        cut_plane_normal_vector: The normal vector of the cutting plane
        distance_from_global_origin: list of IDs of the new elements created by the slicing operation

    Returns:
        List[int]
    """

