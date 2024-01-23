from typing import List
from cadwork import edge_list
from cadwork import element_module_properties
from cadwork import facet_list
from cadwork import point_3d
from cadwork import text_object_options

def get_last_error(error_code: int) -> str:
    """Gets the last error 
    Args:
        error_code ( int): error_code

    Returns:
        error string (str)
    """

def delete_elements(element_id_list: List[int]) -> None:
    """delete elements
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def join_elements(element_id_list: List[int]) -> None:
    """join elements
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def join_top_level_elements(element_id_list: List[int]) -> None:
    """join top level elements
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def create_rectangular_beam_points(width: float, height: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular beam points
    Args:
        width ( float): width
        height ( float): height
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_circular_beam_points(diameter: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create circular beam points
    Args:
        diameter ( float): diameter
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_square_beam_points(width: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create square beam points
    Args:
        width ( float): width
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_rectangular_beam_vectors(width: float, height: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create rectangular beam vectors
    Args:
        width ( float): width
        height ( float): height
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_circular_beam_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create circular beam vectors
    Args:
        diameter ( float): diameter
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_square_beam_vectors(width: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create square beam vectors
    Args:
        width ( float): width
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_rectangular_panel_points(width: float, thickness: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular panel points
    Args:
        width ( float): width
        thickness ( float): thickness
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_rectangular_panel_vectors(width: float, thickness: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create rectangular panel vectors
    Args:
        width ( float): width
        thickness ( float): thickness
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_drilling_points(diameter: float, p1: point_3d, p2: point_3d) -> int:
    """create drilling points
    Args:
        diameter ( float): diameter
        p1 ( point_3d): p1
        p2 ( point_3d): p2

    Returns:
        int
    """

def create_drilling_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d) -> int:
    """create drilling vectors
    Args:
        diameter ( float): diameter
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl

    Returns:
        int
    """

def create_line_points(p1: point_3d, p2: point_3d) -> int:
    """create line points
    Args:
        p1 ( point_3d): p1
        p2 ( point_3d): p2

    Returns:
        int
    """

def create_line_vectors(length: float, p1: point_3d, xl: point_3d) -> int:
    """create line vectors
    Args:
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl

    Returns:
        int
    """

def create_node(p1: point_3d) -> int:
    """create node
    Args:
        p1 ( point_3d): p1

    Returns:
        int
    """

def solder_elements(element_id_list: List[int]) -> List[int]:
    """solder elements
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        List[int]
    """

def convert_beam_to_panel(element_id_list: List[int]) -> None:
    """convert beam to panel
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def convert_panel_to_beam(element_id_list: List[int]) -> None:
    """convert panel to beam
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def delete_all_element_end_types(element_id_list: List[int]) -> None:
    """delete all element end types
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def delete_all_element_processes(element_id_list: List[int]) -> None:
    """delete all element processes
    Args:
        element_id_list ( List[int]): element_id_list

    Returns:
        None
    """

def move_element(element_id_list: List[int], vector: point_3d) -> None:
    """move element
    Args:
        element_id_list ( List[int]): element_id_list
        vector ( point_3d): vector

    Returns:
        None
    """

def create_polygon_beam(polygon_vertices: List[point_3d], thickness: float, xl: point_3d, zl: point_3d) -> int:
    """create polygon beam
    Args:
        polygon_vertices ( List[point_3d]): polygon_vertices
        thickness ( float): thickness
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_text_object(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float) -> int:
    """create text object
    Args:
        text ( str): text
        position ( point_3d): position
        xl ( point_3d): xl
        zl ( point_3d): zl
        size ( float): size

    Returns:
        int
    """

def copy_elements(element_id_list: List[int], copy_vector: point_3d) -> List[int]:
    """copy elements
    Args:
        element_id_list ( List[int]): element_id_list
        copy_vector ( point_3d): copy_vector

    Returns:
        List[int]
    """

def rotate_elements(element_id_list: List[int], origin: point_3d, rotation_axis: point_3d, rotation_angle: float) -> None:
    """rotate elements
    Args:
        element_id_list ( List[int]): element_id_list
        origin ( point_3d): origin
        rotation_axis ( point_3d): rotation_axis
        rotation_angle ( float): rotation_angle

    Returns:
        None
    """

def subtract_elements(hard_elements: List[int], soft_elements: List[int]) -> List[int]:
    """subtract elements
    Args:
        hard_elements ( List[int]): hard_elements
        soft_elements ( List[int]): soft_elements

    Returns:
        List[int]
    """

def check_element_id(element_id: int) -> bool:
    """check element id
    Args:
        element_id ( int): element_id

    Returns:
        bool
    """

def start_element_module_calculation(covers: List[int]) -> None:
    """start element module calculation
    Args:
        covers ( List[int]): covers

    Returns:
        None
    """

def set_element_detail_path(path: str) -> None:
    """set element detail path
    Args:
        path ( str): path

    Returns:
        None
    """

def get_element_from_cadwork_guid(cadwork_guid: str) -> int:
    """get element from cadwork guid
    Args:
        cadwork_guid ( str): cadwork_guid

    Returns:
        int
    """

def add_elements_to_undo(elements: List[int], cmd: int) -> None:
    """add elements to undo
    Args:
        elements ( List[int]): elements
        cmd ( int): cmd

    Returns:
        None
    """

def make_undo() -> None:
    """make undo
    Args:

    Returns:
        None
    """

def make_redo() -> None:
    """make redo
    Args:

    Returns:
        None
    """

def split_elements(elements: List[int]) -> None:
    """split elements
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def set_line_to_marking_line(elements: List[int]) -> None:
    """set line to marking line
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def set_line_to_normal_line(elements: List[int]) -> None:
    """set line to normal line
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def create_auto_export_solid_from_standard(elements: List[int], output_name: str, standard_element_name: str) -> int:
    """create auto export solid from standard
    Args:
        elements ( List[int]): elements
        output_name ( str): output_name
        standard_element_name ( str): standard_element_name

    Returns:
        int
    """

def set_element_module_properties_for_elements(elements: List[int], properties: None) -> None:
    """set element module properties for elements
    Args:
        elements ( List[int]): elements
        properties ( None): properties

    Returns:
        None
    """

def create_text_object_with_font(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float, font_name: str) -> int:
    """create text object with font
    Args:
        text ( str): text
        position ( point_3d): position
        xl ( point_3d): xl
        zl ( point_3d): zl
        size ( float): size
        font_name ( str): font_name

    Returns:
        int
    """

def apply_transformation_coordinate(elements: List[int], old_point: point_3d, old_xl: point_3d, old_yl: point_3d, new_point: point_3d, new_xl: point_3d, new_yl: point_3d) -> None:
    """apply transformation coordinate
    Args:
        elements ( List[int]): elements
        old_point ( point_3d): old_point
        old_xl ( point_3d): old_xl
        old_yl ( point_3d): old_yl
        new_point ( point_3d): new_point
        new_xl ( point_3d): new_xl
        new_yl ( point_3d): new_yl

    Returns:
        None
    """

def delete_elements_with_undo(elements: List[int]) -> None:
    """delete elements with undo
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def add_created_elements_to_undo(elements: List[int]) -> None:
    """add created elements to undo
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def add_modified_elements_to_undo(elements: List[int]) -> None:
    """add modified elements to undo
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def recreate_elements(elements: List[int]) -> None:
    """recreate elements
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def create_multi_wall(elements: List[int]) -> None:
    """create multi wall
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def get_user_element_ids() -> List[int]:
    """get user element ids
    Args:

    Returns:
        List[int]
    """

def get_user_element_ids_with_existing(elements: List[int]) -> List[int]:
    """get user element ids with existing
    Args:
        elements ( List[int]): elements

    Returns:
        List[int]
    """

def clear_errors() -> None:
    """clear errors
    Args:

    Returns:
        None
    """

def glide_elements(element_i_ds: List[int], glide_point: point_3d) -> None:
    """Glides elements 
    Args:
        element_i_ds ( List[int]): element_i_ds
        glide_point ( point_3d): glide_point

    Returns:
        None
    """

def cut_elements_with_miter(first_id: int, second_id: int) -> bool:
    """cut elements with miter
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        bool
    """

def cut_element_with_plane(element_id: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """cut element with plane
    Args:
        element_id ( int): element_id
        cut_plane_normal_vector ( point_3d): cut_plane_normal_vector
        distance_from_global_origin ( float): distance_from_global_origin

    Returns:
        bool
    """

def create_circular_mep(diameter: float, points: List[point_3d]) -> int:
    """create circular mep
    Args:
        diameter ( float): diameter
        points ( List[point_3d]): points

    Returns:
        int
    """

def create_rectangular_mep(width: float, depth: float, points: List[point_3d]) -> int:
    """create rectangular mep
    Args:
        width ( float): width
        depth ( float): depth
        points ( List[point_3d]): points

    Returns:
        int
    """

def slice_element_with_plane(element_id: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """slice element with plane
    Args:
        element_id ( int): element_id
        cut_plane_normal_vector ( point_3d): cut_plane_normal_vector
        distance_from_global_origin ( float): distance_from_global_origin

    Returns:
        bool
    """

def create_auto_container_from_standard(elements: List[int], output_name: str, standard_element_name: str) -> int:
    """create auto container from standard
    Args:
        elements ( List[int]): elements
        output_name ( str): output_name
        standard_element_name ( str): standard_element_name

    Returns:
        int
    """

def create_auto_export_solid_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto export solid from standard with reference
    Args:
        elements ( List[int]): elements
        output_name ( str): output_name
        standard_element_name ( str): standard_element_name
        reference_id ( int): reference_id

    Returns:
        int
    """

def create_auto_container_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto container from standard with reference
    Args:
        elements ( List[int]): elements
        output_name ( str): output_name
        standard_element_name ( str): standard_element_name
        reference_id ( int): reference_id

    Returns:
        int
    """

def slice_elements_with_plane_and_get_new_elements(a0: int, a1: point_3d, a2: float) -> List[int]:
    """slice elements with plane and get new elements
    Args:
        a0 ( int): a0
        a1 ( point_3d): a1
        a2 ( float): a2

    Returns:
        List[int]
    """

def create_surface(surface_vertices: List[point_3d]) -> int:
    """create surface
    Args:
        surface_vertices ( List[point_3d]): surface_vertices

    Returns:
        int
    """

def convert_circular_beam_to_drilling(elements: List[int]) -> None:
    """converts circular/round beams into drillings 
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def stretch_start_facet(a0: List[int], a1: point_3d) -> None:
    """stretch start facet
    Args:
        a0 ( List[int]): a0
        a1 ( point_3d): a1

    Returns:
        None
    """

def stretch_end_facet(a0: List[int], a1: point_3d) -> None:
    """stretch end facet
    Args:
        a0 ( List[int]): a0
        a1 ( point_3d): a1

    Returns:
        None
    """

def set_export_solid_contents(a0: int, a1: List[int]) -> None:
    """set export solid contents
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1

    Returns:
        None
    """

def set_container_contents(a0: int, a1: List[int]) -> None:
    """set container contents
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1

    Returns:
        None
    """

def set_parent_opening_variants_opening_angle(a0: List[int], a1: float) -> None:
    """set parent opening variants opening angle
    Args:
        a0 ( List[int]): a0
        a1 ( float): a1

    Returns:
        None
    """

def mirror_move_elements(elements: List[int], plane: point_3d, plane_distance: float) -> None:
    """mirror move elements
    Args:
        elements ( List[int]): elements
        plane ( point_3d): plane
        plane_distance ( float): plane_distance

    Returns:
        None
    """

def mirror_copy_elements(elements: List[int], plane: point_3d, plane_distance: float) -> List[int]:
    """mirror copy elements
    Args:
        elements ( List[int]): elements
        plane ( point_3d): plane
        plane_distance ( float): plane_distance

    Returns:
        List[int]
    """

def reset_element_cadwork_guid(element_id: int) -> None:
    """sets the Cadwork Guid of an element to NULL 
    Args:
        element_id ( int): element_id

    Returns:
        None
    """

def create_standard_beam_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard beam points
    Args:
        standard_element_name ( str): standard_element_name
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_standard_beam_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard beam vectors
    Args:
        standard_element_name ( str): standard_element_name
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_standard_panel_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard panel points
    Args:
        standard_element_name ( str): standard_element_name
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_standard_panel_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard panel vectors
    Args:
        standard_element_name ( str): standard_element_name
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def create_standard_steel_points(standard_element_name: str, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create standard steel points
    Args:
        standard_element_name ( str): standard_element_name
        p1 ( point_3d): p1
        p2 ( point_3d): p2
        p3 ( point_3d): p3

    Returns:
        int
    """

def create_standard_steel_vectors(standard_element_name: str, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create standard steel vectors
    Args:
        standard_element_name ( str): standard_element_name
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def move_element_with_undo(element_id_list: List[int], vector: point_3d) -> None:
    """move element with undo
    Args:
        element_id_list ( List[int]): element_id_list
        vector ( point_3d): vector

    Returns:
        None
    """

def create_normal_axis_points(p1: point_3d, p2: point_3d) -> int:
    """create normal axis points
    Args:
        p1 ( point_3d): p1
        p2 ( point_3d): p2

    Returns:
        int
    """

def create_normal_axis_vectors(length: float, p1: point_3d, xl: point_3d) -> int:
    """create normal axis vectors
    Args:
        length ( float): length
        p1 ( point_3d): p1
        xl ( point_3d): xl

    Returns:
        int
    """

def convert_bolt_to_standardconnector(elements: List[int], standard_element_name: str) -> None:
    """convert bolt to standardconnector
    Args:
        elements ( List[int]): elements
        standard_element_name ( str): standard_element_name

    Returns:
        None
    """

def extrude_surface_to_auxiliary_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to auxiliary vector
    Args:
        surface ( int): surface
        vector ( point_3d): vector

    Returns:
        int
    """

def extrude_surface_to_panel_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to panel vector
    Args:
        surface ( int): surface
        vector ( point_3d): vector

    Returns:
        int
    """

def extrude_surface_to_beam_vector(surface: int, vector: point_3d) -> int:
    """extrude surface to beam vector
    Args:
        surface ( int): surface
        vector ( point_3d): vector

    Returns:
        int
    """

def convert_container_to_container_block(elements: List[int]) -> None:
    """convert container to container block
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def create_bounding_box_local(a0: int, a1: List[int]) -> int:
    """create bounding box local
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1

    Returns:
        int
    """

def create_bounding_box_global(a1: List[int]) -> int:
    """create bounding box global
    Args:
        a1 ( List[int]): a1

    Returns:
        int
    """

def convert_auxiliary_to_panel(a0: List[int]) -> None:
    """convert auxiliary to panel
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def convert_auxiliary_to_beam(a0: List[int]) -> None:
    """convert auxiliary to beam
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def auto_set_rough_volume_situation(a0: List[int]) -> None:
    """auto set rough volume situation
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def rough_volume_situation_manual(a0: int, a1: List[int], a2: List[int]) -> None:
    """rough volume situation manual
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1
        a2 ( List[int]): a2

    Returns:
        None
    """

def auto_set_parts_situation(a0: List[int]) -> None:
    """auto set parts situation
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def parts_situation_manual(a0: int, a1: List[int], a2: List[int]) -> None:
    """parts situation manual
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1
        a2 ( List[int]): a2

    Returns:
        None
    """

def activate_rv_without_situation() -> List[int]:
    """activate rv without situation
    Args:

    Returns:
        List[int]
    """

def activate_parts_without_situation() -> List[int]:
    """activate parts without situation
    Args:

    Returns:
        List[int]
    """

def add_elements_to_detail(a0: List[int], a1: int) -> None:
    """add elements to detail
    Args:
        a0 ( List[int]): a0
        a1 ( int): a1

    Returns:
        None
    """

def subtract_elements_with_undo(hard_elements: List[int], soft_elements: List[int], with_undo: bool) -> List[int]:
    """subtract elements with undo
    Args:
        hard_elements ( List[int]): hard_elements
        soft_elements ( List[int]): soft_elements
        with_undo ( bool): with_undo

    Returns:
        List[int]
    """

def create_linear_optimization(elements: List[int], optimization_number: int, total_length: float, start_cut: float, end_cut: float, saw_kerf: float, is_production_list: bool) -> int:
    """create linear optimization
    Args:
        elements ( List[int]): elements
        optimization_number ( int): optimization_number
        total_length ( float): total_length
        start_cut ( float): start_cut
        end_cut ( float): end_cut
        saw_kerf ( float): saw_kerf
        is_production_list ( bool): is_production_list

    Returns:
        int
    """

def start_element_module_calculation_silently(covers: List[int]) -> None:
    """start element module calculation silently
    Args:
        covers ( List[int]): covers

    Returns:
        None
    """

def replace_physical_drillings_with_drilling_axes(a0: List[int], a1: float, a2: float) -> List[int]:
    """replace physical drillings with drilling axes
    Args:
        a0 ( List[int]): a0
        a1 ( float): a1
        a2 ( float): a2

    Returns:
        List[int]
    """

def cut_element_with_processing_group(a0: int, a1: int) -> None:
    """cut element with processing group
    Args:
        a0 ( int): a0
        a1 ( int): a1

    Returns:
        None
    """

def add_element_to_detail(a0: List[int], a1: int) -> None:
    """add element to detail
    Args:
        a0 ( List[int]): a0
        a1 ( int): a1

    Returns:
        None
    """

def convert_elements_to_auxiliary_elements(a0: List[int]) -> None:
    """convert elements to auxiliary elements
    Args:
        a0 ( List[int]): a0

    Returns:
        None
    """

def create_circular_axis_points(a0: float, a1: point_3d, a2: point_3d) -> int:
    """create circular axis points
    Args:
        a0 ( float): a0
        a1 ( point_3d): a1
        a2 ( point_3d): a2

    Returns:
        int
    """

def create_circular_axis_vector(a0: float, a1: float, a2: point_3d, a3: point_3d) -> int:
    """create circular axis vector
    Args:
        a0 ( float): a0
        a1 ( float): a1
        a2 ( point_3d): a2
        a3 ( point_3d): a3

    Returns:
        int
    """

def create_polygon_panel(polygon_vertices: List[point_3d], thickness: float, xl: point_3d, zl: point_3d) -> int:
    """create polygon panel
    Args:
        polygon_vertices ( List[point_3d]): polygon_vertices
        thickness ( float): thickness
        xl ( point_3d): xl
        zl ( point_3d): zl

    Returns:
        int
    """

def cut_elements_with_overmeasure(a0: List[int], a1: List[int]) -> None:
    """cut elements with overmeasure
    Args:
        a0 ( List[int]): a0
        a1 ( List[int]): a1

    Returns:
        None
    """

def cut_log_corner_joint(a0: str, a1: List[int]) -> None:
    """cut log corner joint
    Args:
        a0 ( str): a0
        a1 ( List[int]): a1

    Returns:
        None
    """

def get_edge_selection(a0: List[int]) -> edge_list:
    """get edge selection
    Args:
        a0 ( List[int]): a0

    Returns:
        edge_list
    """

def get_facets_with_lasso(a0: List[int]) -> facet_list:
    """get facets with lasso
    Args:
        a0 ( List[int]): a0

    Returns:
        facet_list
    """

def create_standard_element_from_guid_points(a0: str, a1: point_3d, a2: point_3d, a3: point_3d) -> int:
    """create standard element from guid points
    Args:
        a0 ( str): a0
        a1 ( point_3d): a1
        a2 ( point_3d): a2
        a3 ( point_3d): a3

    Returns:
        int
    """

def create_standard_element_from_guid_vectors(a0: str, a1: float, a2: point_3d, a3: point_3d, a4: point_3d) -> int:
    """create standard element from guid vectors
    Args:
        a0 ( str): a0
        a1 ( float): a1
        a2 ( point_3d): a2
        a3 ( point_3d): a3
        a4 ( point_3d): a4

    Returns:
        int
    """

def fillet_edge(a0: int, a1: point_3d, a2: point_3d, a3: float) -> None:
    """fillet edge
    Args:
        a0 ( int): a0
        a1 ( point_3d): a1
        a2 ( point_3d): a2
        a3 ( float): a3

    Returns:
        None
    """

def chamfer_edge(a0: int, a1: point_3d, a2: point_3d, a3: float) -> None:
    """chamfer edge
    Args:
        a0 ( int): a0
        a1 ( point_3d): a1
        a2 ( point_3d): a2
        a3 ( float): a3

    Returns:
        None
    """

def convert_drilling_to_circular_beam(elements: List[int]) -> None:
    """convert drilling to circular beam
    Args:
        elements ( List[int]): elements

    Returns:
        None
    """

def convert_lines_to_surfaces(elements: List[int]) -> List[int]:
    """convert lines to surfaces
    Args:
        elements ( List[int]): elements

    Returns:
        List[int]
    """

def convert_surfaces_to_volume(elements: List[int]) -> int:
    """convert surfaces to volume
    Args:
        elements ( List[int]): elements

    Returns:
        int
    """

def get_all_identifiable_element_ids() -> List[int]:
    """get all identifiable element ids
    Args:

    Returns:
        List[int]
    """

def get_visible_identifiable_element_ids() -> List[int]:
    """get visible identifiable element ids
    Args:

    Returns:
        List[int]
    """

def get_invisible_identifiable_element_ids() -> List[int]:
    """get invisible identifiable element ids
    Args:

    Returns:
        List[int]
    """

def get_active_identifiable_element_ids() -> List[int]:
    """get active identifiable element ids
    Args:

    Returns:
        List[int]
    """

def get_inactive_all_identifiable_element_ids() -> List[int]:
    """get inactive all identifiable element ids
    Args:

    Returns:
        List[int]
    """

def get_inactive_visible_identifiable_element_ids() -> List[int]:
    """get inactive visible identifiable element ids
    Args:

    Returns:
        List[int]
    """

def check_if_point_is_in_element(point: point_3d, element_id: int) -> bool:
    """check if point is in element
    Args:
        point ( point_3d): point
        element_id ( int): element_id

    Returns:
        bool
    """

def check_if_point_is_on_element(point: point_3d, element_id: int) -> bool:
    """check if point is on element
    Args:
        point ( point_3d): point
        element_id ( int): element_id

    Returns:
        bool
    """

def get_element_contact_facets(first_id: int, second_id: int) -> facet_list:
    """get element contact facets
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        facet_list
    """

def get_element_raw_interface_vertices(first_id: int, second_id: int) -> List[point_3d]:
    """get element raw interface vertices
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        List[point_3d]
    """

def get_standard_export_solid_list() -> List[str]:
    """get standard export solid list
    Args:

    Returns:
        List[str]
    """

def get_standard_container_list() -> List[str]:
    """get standard container list
    Args:

    Returns:
        List[str]
    """

def get_standard_beam_list() -> List[str]:
    """get standard beam list
    Args:

    Returns:
        List[str]
    """

def get_standard_panel_list() -> List[str]:
    """get standard panel list
    Args:

    Returns:
        List[str]
    """

def get_variant_sibling_element_ids(a0: int) -> List[int]:
    """get variant sibling element ids
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """

def get_reference_element(element: int) -> int:
    """get reference element
    Args:
        element ( int): element

    Returns:
        int
    """

def get_element_contact_vertices(first_id: int, second_id: int) -> List[point_3d]:
    """get element contact vertices
    Args:
        first_id ( int): first_id
        second_id ( int): second_id

    Returns:
        List[point_3d]
    """

def get_nesting_parent_id(element_id: int) -> int:
    """get nesting parent id
    Args:
        element_id ( int): element_id

    Returns:
        int
    """

def check_if_elements_are_in_collision(first_element_id: int, second_element_id: int) -> bool:
    """check if elements are in collision
    Args:
        first_element_id ( int): first_element_id
        second_element_id ( int): second_element_id

    Returns:
        bool
    """

def check_if_elements_are_in_contact(first_element_id: int, second_element_id: int) -> bool:
    """check if elements are in contact
    Args:
        first_element_id ( int): first_element_id
        second_element_id ( int): second_element_id

    Returns:
        bool
    """

def get_element_module_properties_for_element(element_id: int) -> element_module_properties:
    """get element module properties for element
    Args:
        element_id ( int): element_id

    Returns:
        element_module_properties
    """

def get_element_type_description(element_id: int) -> str:
    """get element type description
    Args:
        element_id ( int): element_id

    Returns:
        str
    """

def get_opening_variant_ids(elements: List[int], opening_type: int) -> List[int]:
    """get opening variant ids
    Args:
        elements ( List[int]): elements
        opening_type ( int): opening_type

    Returns:
        List[int]
    """

def get_parent_container_id(element_id: int) -> int:
    """get parent container id
    Args:
        element_id ( int): element_id

    Returns:
        int
    """

def get_export_solid_content_elements(element_id: int) -> List[int]:
    """get export solid content elements
    Args:
        element_id ( int): element_id

    Returns:
        List[int]
    """

def get_container_content_elements(element_id: int) -> List[int]:
    """get container content elements
    Args:
        element_id ( int): element_id

    Returns:
        List[int]
    """

def get_element_detail_path() -> str:
    """get element detail path
    Args:

    Returns:
        str
    """

def get_element_cadwork_guid(element_id: int) -> str:
    """get element cadwork guid
    Args:
        element_id ( int): element_id

    Returns:
        str
    """

def get_bounding_box_vertices_local(a0: int, a1: List[int]) -> List[point_3d]:
    """get bounding box vertices local
    Args:
        a0 ( int): a0
        a1 ( List[int]): a1

    Returns:
        List[point_3d]
    """

def get_bounding_box_vertices_global(a0: List[int]) -> List[point_3d]:
    """get bounding box vertices global
    Args:
        a0 ( List[int]): a0

    Returns:
        List[point_3d]
    """

def get_all_nesting_raw_parts() -> List[int]:
    """get all nesting raw parts
    Args:

    Returns:
        List[int]
    """

def get_joined_elements(a0: int) -> List[int]:
    """get joined elements
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """

def check_element_duplicates(elements: List[int]) -> List[int]:
    """check element duplicates
    Args:
        elements ( List[int]): elements

    Returns:
        List[int]
    """

def get_elements_in_contact(a0: int) -> List[int]:
    """get elements in contact
    Args:
        a0 ( int): a0

    Returns:
        List[int]
    """

def create_text_object_with_options(position: point_3d, xl: point_3d, zl: point_3d, text_options: text_object_options) -> int:
    """create text object with options
    Args:
        position ( point_3d): position
        xl ( point_3d): xl
        zl ( point_3d): zl
        text_options ( text_object_options): text_options

    Returns:
        int
    """

