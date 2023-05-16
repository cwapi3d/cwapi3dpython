from typing import List
from cadwork import (element_module_properties,
                     point_3d,
                     element_module_detail)


def get_all_identifiable_element_ids() -> List[int]:
    """get all identifiable element IDs (visible and unvisible)

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def get_visible_identifiable_element_ids() -> List[int]:
    """get all visible identifiable elemnt ids

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def get_invisible_identifiable_element_ids() -> List[int]:
    """Get invisible cadwork element IDs

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def get_active_identifiable_element_ids() -> List[int]:
    """Get active cadwork element IDs

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def get_inactive_all_identifiable_element_ids() -> List[int]:
    """Get inactive cadwork element IDs

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def get_inactive_visible_identifiable_element_ids() -> List[int]:
    """Get inactive visible cadwork element IDs

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element_id list
    """


def delete_elements(elements: List[int]) -> None:
    """Delete elements 

    Args:
        elements (List[int]): element IDs
    """


def join_elements(elements: List[int]) -> None:
    """join elements (group)

    Args:
        elements (List[int]): element IDs
    """


def join_top_level_elements(elements: List[int]) -> None:
    """join elements on highest leve. Previously joined elements are dissolved and joined at the top level.

    Args:
        elements (List[int]): element IDs
    """


def create_rectangular_beam_points(width: float, height: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create a rectangular beam. The direction (local x axis) and length of the beam is defined via p1 and p2. 
    The parameter p3 is used to set the local z vector (height) of the beams coordinate system. 

    Args:
        width (float): beam width
        height (float): beam height
        p1 (point_3d): start point
        p2 (point_3d): end point
        p3 (point_3d): height point

    Returns:
        int: element ID
    """


def create_circular_beam_points(diameter: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create a circular beam. The direction (local x axis) and length of the beam is defined via p1 and p2. 
   The parameter p3 is used to set the local z vector (height) of the beams coordinate system. 

    Args:
        diameter (float): circle diameter
        p1 (point_3d): start point
        p2 (point_3d): end point
        p3 (point_3d): height point

    Returns:
        int: element ID
    """


def create_square_beam_points(width: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create a square beam. The direction (local x axis) and length of the beam is defined via p1 and p2. 
    The parameter p3 is used to set the local z vector (height) of the beams coordinate system. 

    Args:
        width (float): beam width
        p1 (point_3d): start point
        p2 (point_3d): end point
        p3 (point_3d): height point

    Returns:
        int: element ID
    """


def create_rectangular_beam_vectors(width: float, height: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create a rectangular beam from vectors. The start point of the element is defined by p1. Then the direction (local x axis) is definied by p2 (e.g. point_3d(1.,0.,0.)).
    The local z vector is defined via p3 (e.g. point_3d(0.,1.,0.)). 

    Examples:
        >>> beam = ec.create_rectangular_beam_vectors(120.0, 240.0, 2800.0, cadwork.point_3d(0.,0.,0.), cadwork.point_3d(1.,0.,0.), cadwork.point_3d(0.,0.,1.))

    Args:
        length (float): length of beam axis
        width (float): beam width
        height (float): beam height
        p1 (point_3d): start point 
        xl (point_3d): local x vector
        zl (point_3d): local z vector

    Returns:
        int: element ID
    """


def create_circular_beam_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create a circular beam from vectors. The start point of the element is defined by p1. Then the direction (local x axis) is definied by xl (e.g. point_3d(1.,0.,0.)).
    The local z vector is defined via zl (e.g. point_3d(0.,1.,0.)).

    Args:
        diameter (float): circle diameter
        length (float): beam/axis length
        p1 (point_3d): start point
        xl (point_3d): local x vector
        zl (point_3d): local z vector

    Returns:
        int: element ID
    """


def create_square_beam_vectors(width: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create a square beam from vectors. The start point of the element is defined by p1. Then the direction (local x axis) is definied by xl (e.g. point_3d(1.,0.,0.)).
    The local z vector is defined via zl (e.g. point_3d(0.,1.,0.)).

    Args:
        width (float): beam width
        length (float): beam/axis length
        p1 (point_3d): start point
        xl (point_3d): local x vector
        zl (point_3d): local z vector

    Returns:
        int: element ID
    """


def create_rectangular_panel_points(width: float, thickness: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create a rectangular panel. The direction (local x axis) and length of the panel is defined via p1 and p2. 
    The parameter (p3) is used to set the local z vector (thickness) of the beams coordinate system.

    Args:
        width (float): beam width
        thickness (float): beam thickness
        p1 (point_3d): start point
        p2 (point_3d): end point
        p3 (point_3d): height point

    Returns:
        int: element ID
    """


def create_rectangular_panel_vectors(width: float, thickness: float, length: float, p1: point_3d, xl: point_3d, zl: point_3d) -> int:
    """create a rectangular panel from vectors. The start point of the element is defined by p1. Then the direction (local x axis) is definied by p2 (e.g. point_3d(1.,0.,0.)).
    The local z vector is defined via p3 (e.g. point_3d(0.,1.,0.)). 

    Args:
        width (float): panel width
        thickness (float): panel thickness
        length (float):  panel/axis length
        p1 (point_3d): start point
        xl (point_3d): local x vector
        zl (point_3d): local z vector

    Returns:
        int: element ID
    """


def create_drilling_points(diameter: float, p1: point_3d, p2: point_3d) -> int:
    """Create a drilling from two points. 

    Args:
        diameter (float): drilling diameter
        p1 (point_3d): start point
        p2 (point_3d): end point

    Returns:
        int: element ID
    """


def create_drilling_vectors(diameter: float, length: float, p1: point_3d, xl: point_3d) -> int:
    """Create a drilling from a point and a direction vector. 

    Args:
        diameter (float): drilling diameter
        length (float): drilling length
        p1 (point_3d): start point
        xl (point_3d): vector direction

    Returns:
        int: [description]
    """


def create_line_points(p1: point_3d, p2: point_3d) -> int:
    """crete a line

    Args:
        p1 (point_3d): start point
        p2 (point_3d): end point

    Returns:
        int: element ID
    """


def create_line_vectors(length: float, p1: point_3d, xl: point_3d) -> int:
    """crete a line

    Args:
        length (float): line length
        p1 (point_3d): start point
        xl (point_3d): vector direction

    Returns:
        int: elmement id
    """


def create_node(p1: point_3d) -> int:
    """create a node

    Args:
        p1 (point_3d): point

    Returns:
        int: element ID
    """


def solder_elements(elements: List[int]) -> List[int]:
    """solder elements, if they are in contact. 

    Args:
        elements (List[int]): element IDs

    Returns:
        List[int]: element ID
    """


def convert_beam_to_panel(elements: List[int]) -> None:
    """convert beam(s) to panel(s)

    Args:
        elements (List[int]): element IDs
    """


def convert_panel_to_beam(elements: List[int]) -> None:
    """convert panel(s) to beam(s)

    Args:
        elements (List[int]): element IDs
    """


def delete_all_element_end_types(elements: List[int]) -> None:
    """delete end types

    Args:
        elements (List[int]): element IDs
    """


def delete_all_element_processes(elements: List[int]) -> None:
    """delete element processes

    Args:
        elements (List[int]): element IDs
    """


def move_element(elements: List[int], vector: point_3d) -> None:
    """move element by a vector

    Args:
        elements (List[int]): element IDs
        vector (point_3d): vector
    """


def create_polygon_beam(points: List[point_3d], thickness: float, xl: point_3d, zl: point_3d) -> int:
    """create a polygon beam. Define the polygon outline in a vertex list.  

    Args:
        points (List[point_3d]): vertex list
        thickness (float): beam thickness
        xl (point_3d): vector (length dir)
        zl (point_3d): vector (height dir)

    Returns:
        int: element ID
    """


def create_text_object(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float) -> int:
    """create text object

    Args:
        text (str): your text
        position (point_3d): location
        xl (point_3d): length dir
        zl (point_3d): height dir
        size (float): font size

    Returns:
        int: element ID
    """


def copy_elements(elements: List[int], vector: point_3d) -> List[int]:
    """copy elements

    Args:
        elements (List[int]): element IDs
        vector (point_3d): copy vector

    Returns:
        List[int]: element IDs
    """


def rotate_elements(elements: List[int], origin: point_3d, rotation_axis: point_3d, rotation_angle: float) -> None:
    """rotate elements

    Args:
        elements (List[int]): element IDs
        origin (point_3d): element origin (p1)
        rotation_axis (point_3d): vector axis
        rotation_angle (float): radians
    """


def subtract_elements(hard_elements: List[int], soft_elements: List[int]) -> List[int]:
    """Subtract elements. The first element is hard, the second soft.

    Args:
        hard_elements (List[int]): subtract with
        soft_elements (List[int]): subtract from

    Returns:
        List[int]: element IDs
    """


def subtract_elements_with_undo(hard_elements: List[int], soft_elements: List[int], with_undo: bool) -> List[int]:
    """Subtract elements with undo. The first element is hard, the second soft.

    Args:
        hard_elements (List[int]): subtract with
        soft_elements (List[int]): subtract from
        with_undo (bool): with undo

    Returns:
        List[int]: element IDs
    """


def check_element_id(element: int) -> bool:
    """check element ID

    Args:
        element (int): element ID

    Returns:
        bool: True/False
    """


def start_element_module_calculation(elements: List[int]) -> None:
    """start the elemend module calculation. Inputarguments are cover elements. 

    Args:
        elements (List[int]): element IDs (cover(s) architectural elementtypes)
    """


def set_element_detail_path(path: str) -> None:
    """set element detail path

    Args:
        path (str): path to elementmodule directory
    """


def get_element_detail_path() -> str:
    """get the path from active elmeentmodule

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        str: path
    """


def get_element_cadwork_guid(element: int) -> str:
    """get cadwork element guid

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: guid
    """


def get_element_from_cadwork_guid(guid: str) -> int:
    """get element from cadwork guid

    Args:
        guid (str): cadwork guid

    Returns:
        int: element ID
    """


def add_elements_to_undo(elements: List[int], number: int) -> None:
    """add elements to undo

    Args:
        elements (List[int]): element IDs
        number (int): enum(1:add, 2:modify)
    """


def make_undo() -> None:
    """make undo
    """


def make_redo() -> None:
    """make redo
    """


def split_elements(elements: List[int]) -> None:
    """split joined elmements

    Args:
        elements (List[int]): element IDs
    """


def set_line_to_marking_line(elements: List[int]) -> None:
    """modify a line to a marking line

    Args:
        elements (List[int]): element IDs
    """


def set_line_to_normal_line(elements: List[int]) -> None:
    """set line to normal line

    Args:
        elements (List[int]): element IDs
    """


def create_auto_export_solid_from_standard(elements: List[int], name: str, standard_element_name: str) -> int:
    """create automatic export solid from a standard export solid

    Args:
        elements (List[int]): element IDs
        name (str): new name for export solid
        standard_element_name (str): name of standard export solid

    Returns:
        int: element ID
    """


def set_element_module_properties_for_elements(elements: List[int], properties: element_module_properties) -> None:
    """set element module properties for elements

    Examples:
        >>> import cadwork as cw
        >>> import element_controller as ec
        >>> element_properties = ec.get_element_module_properties_for_element(540915) # 540915 = some element ID
        >>> cw.element_module_properties.set_bottom_plate(element_properties, True)
        >>> cw.element_module_properties.set_solder_in_axis_direction(element_properties, True)
        >>> cw.element_module_properties.set_main_element(element_properties, True)
        >>> cw.element_module_properties.set_strecht_according_thickness_axis(element_properties, True)
        >>> ec.set_element_module_properties_for_elements([540915],element_properties)
        None

    Args:
        elements (List[int]): element IDs
        properties (element_module_properties): elment module properties
    """


def get_element_module_properties_for_element(element: int) -> element_module_properties:
    """get element module properties for element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        element_module_properties: elmement module properties
    """


def get_element_type_description(element: int) -> str:
    """get the description of the cadwork element type

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        str: element type (e.g. beam)
    """


def create_text_object_with_font(text: str, position: point_3d, xl: point_3d, zl: point_3d, size: float, font: str) -> int:
    """create text object with font

    Args:
        text (str): your text
        position (point_3d): location
        xl (point_3d): length dir
        zl (point_3d): height dir
        size (float): font size
        font (str): font type (e.g. , "Times New Roman")

    Returns:
        int: element ID
    """


def get_opening_variant_ids(elements: List[int], opening_type: int) -> List[int]:
    """get opening variant ids

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]): element IDs
        opening_type (int): number of opening type (enum)

    Returns:
        List[int]: element IDs
    """


def get_parent_container_id(element: int) -> int:
    """get parent container id

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: element ID
    """


def get_export_solid_content_elements(element: int) -> List[int]:
    """get export solid content elements

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID of export solid
    Returns:
        List[int]: element IDs
    """


def get_container_content_elements(element: int) -> List[int]:
    """get container content elements

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
    Returns:
        List[int]: element IDs
    """


def apply_transformation_coordinate(elments: List[int], old_point: point_3d, old_xl: point_3d, old_yl: point_3d, new_point: point_3d, new_xl: point_3d, new_yl: point_3d) -> None:
    """apply transformation coordinate to transform elements in 3D space

    Args:
        elments (List[int]): element IDs to transform
        old_point (point_3d): location origin
        old_xl (point_3d): origin x dir (vector)
        old_yl (point_3d): origin y dir (vector)
        new_point (point_3d): new location
        new_xl (point_3d): new x dir (vector)
        new_yl (point_3d): new y dir (vector)
    """


def delete_elements_with_undo(elements: List[int]) -> None:
    """delete elements and store the in undo

    Args:
        elements (List[int]): element IDs
    """


def add_created_elements_to_undo(elements: List[int]) -> None:
    """add created elementes to undo storeage

    Args:
        elements (List[int]): element IDs
    """


def add_modified_elements_to_undo(elements: List[int]) -> None:
    """add modified elementes to undo storeage

    Args:
        elements (List[int]): element IDs
    """


def recreate_elements(elements: List[int]) -> None:
    """recreate elements

    Args:
        elements (List[int]): element IDs
    """


def check_if_elements_are_in_collision(first_element: int, second_element: int) -> bool:
    """collision detection

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): first element ID
        element (int): second element ID

    Returns:
        bool: true/false
    """


def check_if_elements_are_in_contact(first_element: int, second_element: int) -> bool:
    """check if element faces are in contact

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): first element ID
        element (int): second element ID

    Returns:
        bool: true/false
    """


def create_multi_wall(elements: List[int]) -> None:
    """create multi wall

    Args:
        elements (List[int]): element IDs
    """


def get_user_element_ids() -> List[int]:
    """prompt that user select element IDs in 3D

    Returns:
        List[int]: elmement ids from selection
    """


def get_element_contact_vertices(first_element: int, second_element: int) -> List[point_3d]:
    """get element contact vertices

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): first element ID
        element (int): second element ID

    Returns:
        List[point_3d]: vertices list
    """


def get_nesting_parent_id(element: int) -> int:
    """get nesting parent id

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: element ID
    """


def get_user_element_ids_with_existing(elements: List[int]) -> List[int]:
    """
    """


def clear_errors() -> None:
    """
    """


def glide_elements(elements: List[int], glide_point: point_3d) -> None:
    """glide elements

    Args:
        elements (List[int]): element IDs
        glide_point (point_3d): a glide point
    """


def get_element_contact_facets(first_element: int, second_element: int) -> List[List[point_3d]]:
    """get element contact faces

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        element (int): element ID

    Returns:
        List[List[point_3d]]: contact face vertice list
    """


def get_element_raw_interface_vertices(first_element: int, second_element: int) -> List[point_3d]:
    """get element raw interface vertices

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID
        element (int): element ID

    Returns:
        List[point_3d]: vertice list
    """


def cut_elements_with_miter(first_element: int, second_element: int) -> bool:
    """cut elements with miter. The miter is "cut" on loxal x-axis. 

    Args:
        element (int): element ID
        element (int): element ID

    Returns:
        bool: true/false
    """


def cut_element_with_plane(element: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """cut an elment with a plane

    Args:
        element (int): element ID
        cut_plane_normal_vector (point_3d): plane normal vector
        distance_from_global_origin (float): distance from origin to plane

    Returns:
        bool: true/false
    """


def create_circular_mep(diameter: float, points: List[point_3d]) -> int:
    """create a circular mep

    Args:
        diameter (float): diameter
        points (List[point_3d]): vertice list

    Returns:
        int: element ID
    """


def create_rectangular_mep(width: float, depth: float, points: List[point_3d]) -> int:
    """create rectangular mep. The mep is orientied by an active element face.

    Args:
        width (float): mep width
        depth (float): mep depth
        points (List[point_3d]): vertice list

    Returns:
        int: element ID
    """


def slice_element_with_plane(element: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: float) -> bool:
    """slice an elment with a plane

    Args:
        element (int): element ID
        cut_plane_normal_vector (point_3d): plane normal vector
        distance_from_global_origin (float): distance from origin to plane

    Returns:
        bool: true/false
    """


def create_auto_container_from_standard(elements: List[int], output_name: str, standard_element_name: str) -> int:
    """create an automatic container from a standard container

    Args:
        elements (List[int]): element ID
        output_name (str): container name
        standard_element_name (str): default container name

    Returns:
        int: element ID
    """


def create_auto_export_solid_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto export solid from standard. The orientation is determined according to an element. 

    Args:
        elements (List[int]): element IDs
        output_name (str): export solid name
        standard_element_name (str): standard element name
        reference_id (int): element ID (reference - orientation)

    Returns:
        int: element ID
    """


def create_auto_container_from_standard_with_reference(elements: List[int], output_name: str, standard_element_name: str, reference_id: int) -> int:
    """create auto container from standard. The orientation is determined according to an element. 

    Args:
        elements (List[int]): element IDs
        output_name (str): export solid name
        standard_element_name (str): standard element name
        reference_id (int): element ID (reference - orientation)

    Returns:
        int: element ID
    """


def slice_elements_with_plane_and_get_new_elements(element: int, cut_plane_normal_vector: point_3d, distance_from_global_origin: point_3d) -> List[int]:
    """slice elments in two with a cutting plane.

    Args:
        element (int): element ID
        cut_plane_normal_vector (point_3d): plane normal vector
        distance_from_global_origin (float): distance from origin to plane

    Returns:
        bool: true/false
    """


def create_surface(points: List[point_3d]) -> int:
    """create a surface

    Args:
        points (List[point_3d]): vertex list

    Returns:
        int: element ID
    """


def convert_circular_beam_to_drilling(elements: List[int]) -> None:
    """convert circular beam to drilling 

    Args:
        elements (List[int]): element ID
    """


def get_standard_export_solid_list() -> List[str]:
    """get list of standard export solid names

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[str]: names
    """


def get_standard_container_list() -> List[str]:
    """get list of standard container names

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[str]: names
    """


def stretch_start_facet(elements: List[int], stretch_vector: point_3d) -> None:
    """stretch start facet of element(s)

    Args:
        elements (List[int]): element ID
        stretch_vector (point_3d): vector
    """


def stretch_end_facet(elements: List[int], stretch_vector: point_3d) -> None:
    """stretch end facet of element(s)

    Args:
        elements (List[int]): element ID
        stretch_vector (point_3d): vector
    """


def get_variant_sibling_element_ids(element: int) -> List[int]:
    """get variant sibling element IDs

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        List[int]: element IDs
    """


def set_export_solid_contents(solid_id: int, elements: List[int]) -> None:
    """set export solid contents

    Args:
        solid_id (int): element ID of export solid
        elements (List[int]): element IDs to assign
    """


def set_container_contents(container_id: int, elements: List[int]) -> None:
    """set container contents

    Args:
        solid_id (int): element ID
        elements (List[int]): element IDs
    """


def set_parent_opening_variants_opening_angle(elements: List[int], angle: float) -> None:
    """set parent opening variants opening angle

    Args:
        elements (List[int]): element IDs
        angle (float): radians
    """


def mirror_move_elements(elements: List[int], plane_definition: point_3d, plane_distance: float) -> None:
    """mirror elements (no copy)

    Args:
        elements (List[int]): element IDs
        plane_definition (point_3d): mirror plane
        plane_distance (float): perp. distance from origin to plane
    """


def mirror_copy_elements(elements: List[int], plane_definition: point_3d, plane_distance: float) -> List[int]:
    """mirror elements (copy)

    Args:
        elements (List[int]): element IDs
        plane_definition (point_3d): mirror plane
        plane_distance (float): perp. distance from origin to plane

    Returns:
        List[int]: element IDs
    """


def check_if_point_is_on_element(point: point_3d, element: int) -> bool:
    """Checks if a point is on a element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        point (point_3d): a cadwork point
        element (int): element ID

    Returns:
        bool: if point 
    """


def check_if_point_is_in_element(point: point_3d, element: int) -> bool:
    """Check if point is in element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        point (point_3d): a cadwork point
        element (int): element ID

    Returns:
        bool: if point 
    """


def get_bounding_box_vertices_local(element: int, elements: List[int]) -> List[point_3d]:
    """create a bounding box that is aligned to a reference element. 
    The bounding box includes all elements contained in the list.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID reference element
        elements (List[int]): element IDs

    Returns:
        List[point_3d]: bbx vertices
    """


def get_bounding_box_vertices_global(elements: List[int]) -> List[point_3d]:
    """create a bounding box that is aligned to the global coordinate system.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        elements (List[int]): element IDs

    Returns:
        List[point_3d]: bbx vertices
    """


def create_bounding_box_local(element: int, elements: List[int]) -> int:
    """create a bounding box that is aligned to a reference element. 
    The bounding box includes all elements contained in the list.

    Args:
        element (int): element ID reference element
        elements (List[int]): element IDs

    Returns:
        int: element ID bounding box
    """


def create_bounding_box_global(elements: List[int]) -> int:
    """create a bounding box that is aligned to the global coordinate system.

    Args:
        elements (List[int]): element IDs

    Returns:
        int: element ID bounding box
    """


def extrude_surface_to_auxiliary_vector(element: int, vector: point_3d) -> int:
    """Extrude a surface to a auxiliary element. 

    Args:
        element (int): element ID
        vector (point_3d): vector e.g. point_3d(0,0,1200)

    Returns:
        int: element ID
    """


def extrude_surface_to_beam_vector(element: int, vector: point_3d) -> int:
    """Extrude a surface to a beam. 

    Args:
        element (int): element ID
        vector (point_3d): vector e.g. point_3d(0,0,1200)

    Returns:
        int: element ID
    """


def extrude_surface_to_panel_vector(element: int, vector: point_3d) -> int:
    """Extrude a surface to a panel.

    Args:
        element (int): element ID
        vector (point_3d): vector e.g. point_3d(0,0,1200)

    Returns:
        int: element ID
    """


def activate_parts_without_situation() -> List[int]:
    """

    Returns:
        List[int]: element IDs
    """


def activate_rv_without_situation() -> List[int]:
    """

    Returns:
        List[int]: element IDs
    """


def parts_situation_manual(element: int, addChilds: List[int], removeChilds: List[int]) -> None:
    """

    Args:
        element (int): element ID
        addChilds (List[int]): add childs
        removeChilds (List[int]): remove childs
    """


def auto_set_parts_situation(elements: List[int]) -> None:
    """

    Args:
        elementIDs (List[int]): element IDs
    """


def auto_set_rough_volume_situation(elements: List[int]) -> None:
    """

    Args:
        elements (List[int]): element IDs
    """


def rough_volume_situation_manual(element: int, addPartner: List[int], removePartner: List[int]) -> None:
    """

    Args:
        element (int): element ID
        addPartner (List[int]): add partner
        removePartner (List[int]): remove partner
    """


def add_elements_to_detail(elements: List[int], detail_group: int) -> None:
    """
    detail groups:
    0: without assigment

    1: Angle; 2: Area; 3: Cross; 4: Edge; 5: End; 6: Line; 7: Open; 
    8: T; 9: FloorArea; 10: FloorEnd; 11: FloorLine; 12: FloorOpen

    Args:
        elements (List[int]): element IDs
        detail_group (int): a detail group
    """


def get_all_nesting_raw_parts() -> List[int]:
    """Get all nesting raw parts.

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[int]: element IDs
    """


def get_standard_beam_list() -> List[str]:
    """Get standard beam list

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[str]: standard beam names
    """


def get_standard_panel_list() -> List[str]:
    """Get standard panel list

    [:information_source: Available for script filled attributes](#){.mark-text}

    Returns:
        List[str]: standard panel names
    """


def get_reference_element(element: int) -> int:
    """Get reference element

    [:information_source: Available for script filled attributes](#){.mark-text}

    Args:
        element (int): element ID

    Returns:
        int: element ID
    """


def create_linear_optimization(elements: List[int], optimization_number: int,
                               total_length: float, start_cut: float,
                               end_cut: float, saw_kerf: float, is_production_list: bool) -> int:
    """create linear optimization

    Args:
        elements (List[int]): element IDs
        optimization_number (int): number of nesting volume
        total_length (float): total length nesting volume
        start_cut (float): start cut
        end_cut (float): end cut
        saw_kerf (float): saw kerf
        is_production_list (bool): measurements

    Returns:
        int: element ID
    """


def move_element_with_undo(elements: List[int], aVector: point_3d) -> None:
    """Move elements and add 'step' to undo memory.

     Examples:
        >>> import element_controller as ec
        >>> import geometry_controller as gc
        >>> import cadwork
        >>> element_ids = ec.get_active_identifiable_element_ids()
        >>> ec.move_element_with_undo(element_ids, gc.get_yl(*element_ids) * 1500.)

    Args:
        elements (List[int]): element IDs
        aVector (point_3d): a Target
    """
