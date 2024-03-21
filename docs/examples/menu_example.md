---
hide:
  - toc
---

# menu_controller
## create a simple cadwork menu 

```python 
import menu_controller as mec 
import utility_controller as uc
import cadwork

menu_options = 'Foo', 'Bar', 'Baz', '', 'Return'

while True:
    menu = mec.display_simple_menu(menu_options)

    if menu == 'Foo':
        uc.print_error('You pressed Foo')
        
    elif menu == 'Bar':
        uc.print_error('You pressed Bar')
        
    elif menu == 'Baz':
        uc.print_error('You pressed Baz')
        
    elif menu == 'Return':
        break

```

Above code generates a menu structure like this.

![Backup Text](../img/menu.png "Example Menu")


## Process type setter

```python

import cadwork as cw
import attribute_controller as ac
import element_controller as ec
import visualization_controller as vc
import utility_controller as uc
import menu_controller as mc


def list_ele_types(ele_type):
    l_ele_types = [[cw.element_type.is_additional_element(ele_type), 'is_additional_element'],
               [cw.element_type.is_auxiliary(ele_type), 'is_auxiliary'],
               [cw.element_type.is_cadwork(ele_type), 'is_cadwork'],
               [cw.element_type.is_circular_axis(ele_type), 'is_circular_axis'],
               [cw.element_type.is_circular_beam(ele_type), 'is_circular_beam'],
               [cw.element_type.is_connector_axis(ele_type), 'is_connector_axis'],
               [cw.element_type.is_connector_node(ele_type), 'is_connector_node'],
               [cw.element_type.is_container(ele_type), 'is_container'],
               [cw.element_type.is_dimension(ele_type), 'is_dimension'],
               [cw.element_type.is_drilling_axis(ele_type), 'is_drilling_axis'],
               [cw.element_type.is_eave_axis(ele_type), 'is_eave_axis'],
               [cw.element_type.is_export_solid(ele_type), 'is_export_solid'],
               [cw.element_type.is_export_solid_scene(ele_type), 'is_export_solid_scene'],
               [cw.element_type.is_floor(ele_type), 'is_floor'],
               [cw.element_type.is_global_cut(ele_type), 'is_global_cut'],
               [cw.element_type.is_graphical_object(ele_type), 'is_graphical_object'],
               [cw.element_type.is_line(ele_type), 'is_line'],
               [cw.element_type.is_nesting_parent(ele_type), 'is_nesting_parent'],
               [cw.element_type.is_none(ele_type), 'is_none'],
               [cw.element_type.is_normal_node(ele_type), 'is_normal_node'],
               [cw.element_type.is_opening(ele_type), 'is_opening'],
               [cw.element_type.is_panel(ele_type), 'is_panel'],
               [cw.element_type.is_rectangular_axis(ele_type), 'is_rectangular_axis'],
               [cw.element_type.is_rectangular_beam(ele_type), 'is_rectangular_beam'],
               [cw.element_type.is_roof(ele_type), 'is_roof'],
               [cw.element_type.is_room(ele_type), 'is_room'],
               [cw.element_type.is_rotation_element(ele_type), 'is_rotation_element'],
               [cw.element_type.is_section_trace(ele_type), 'is_section_trace'],
               [cw.element_type.is_steel_shape(ele_type), 'is_steel_shape'],
               [cw.element_type.is_surface(ele_type), 'is_surface'],
               [cw.element_type.is_text_document(ele_type), 'is_text_document'],
               [cw.element_type.is_wall(ele_type), 'is_wall'],
               [cw.element_type.is_wire_axis(ele_type), 'is_wire_axis']]
    return l_ele_types


def list_process_types_is(process_type):
    l_process_types_i = [[cw.process_type.is_hip_valley(process_type), 'is_hip_valley'],
                       [cw.process_type.is_jack_rafter(process_type), 'is_jack_rafter'],
                       [cw.process_type.is_log(process_type), 'is_log'],
                       [cw.process_type.is_none(process_type), 'is_none'],
                       [cw.process_type.is_panel_1(process_type), 'is_panel_1'],
                       [cw.process_type.is_panel_2(process_type), 'is_panel_2'],
                       [cw.process_type.is_panel_3(process_type), 'is_panel_3'],
                       [cw.process_type.is_panel_4(process_type), 'is_panel_4'],
                       [cw.process_type.is_panel_5(process_type), 'is_panel_5'],
                       [cw.process_type.is_purlin(process_type), 'is_purlin'],
                       [cw.process_type.is_rafter(process_type), 'is_rafter'],
                       [cw.process_type.is_rough_volume_framed_wall(process_type), 'is_rough_volume_framed_wall'],
                       [cw.process_type.is_rough_volume_log_home(process_type), 'is_rough_volume_log_home'],
                       [cw.process_type.is_rough_volume_solid_wood_wall(process_type),
                        'is_rough_volume_solid_wood_wall'],
                       [cw.process_type.is_stud(process_type), 'is_stud'],
                       [cw.process_type.is_tread(process_type), 'is_tread'],
                       [cw.process_type.is_truss(process_type), 'is_truss'],
                       [cw.process_type.is_user_1(process_type), 'is_user_1'],
                       [cw.process_type.is_user_2(process_type), 'is_user_2'],
                       [cw.process_type.is_user_3(process_type), 'is_user_3'],
                       [cw.process_type.is_user_4(process_type), 'is_user_4'],
                       [cw.process_type.is_user_5(process_type), 'is_user_5'],
                       [cw.process_type.is_user_5(process_type), 'is_user_5']]
    return l_process_types_i


def list_process_types_set(z, process_type):
    if z == 1:
        process_type.set_hip_valley()
    elif z == 2:
        process_type.set_jack_rafter()
    elif z == 3:
        process_type.set_log()
    elif z == 4:
        process_type.set_none()
    elif z == 5:
        process_type.set_panel_1()
    elif z == 6:
        process_type.set_panel_2()
    elif z == 7:
        process_type.set_panel_3()
    elif z == 8:
        process_type.set_panel_4()
    elif z == 9:
        process_type.set_panel_5()
    elif z == 10:
        process_type.set_purlin()
    elif z == 11:
        process_type.set_rafter()
    elif z == 12:
        process_type.set_rough_volume_framed_wall()
    elif z == 13:
        process_type.set_rough_volume_log_home()
    elif z == 14:
        process_type.set_rough_volume_solid_wood_wall()
    elif z == 15:
        process_type.set_stud()
    elif z == 16:
        process_type.set_tread()
    elif z == 17:
        process_type.set_truss()
    elif z == 18:
        process_type.set_user_1()
    elif z == 19:
        process_type.set_user_2()
    elif z == 20:
        process_type.set_user_3()
    elif z == 21:
        process_type.set_user_4()
    else:
        process_type.set_user_5()

    return process_type



def menu_output_type():
    menu_items = ['hip_valley', 'jack_rafter', 'log', 'none', 'panel_1', 'panel_2', 'panel_3',
                'panel_4', 'panel_5', 'purlin', 'rafter', 'rough_volume_framed_wall', 'rough_volume_log_home',
                'rough_volume_solid_wood_wall', 'stud', 'tread', 'truss', 'user_1', 'user_2', 'user_3',
                'user_4', 'user_5']

    menu_select = mc.display_simple_menu(menu_items)
    menu_i = menu_items.index(menu_select)

    return menu_i+1


def main():
    active_elements = ec.get_active_identifiable_element_ids()

    if len(active_elements) > 0:
        for element in active_elements:
            ele_type = ac.get_element_type(element)
            l_ele_types = list_ele_types(ele_type)
            process_type = ac.get_output_type(element)
            l_process_types = list_process_types_is(process_type)

    for p_type in l_process_types:
        if p_type[0]:
         for e_type in l_ele_types:
            if e_type[0]:
                vc.hide_all_elements()
                vc.set_visible([element])
                vc.zoom_all_elements()
                uc.print_error(f'Elementyp = {e_type[1]} / Ausgabeart = {p_type[1]}')

    n_process_type = list_process_types_set(menu_output_type(), process_type)
    ac.set_output_type([element], n_process_type)
    l_process_types = list_process_types_is(process_type)

    for p_type_n in l_process_types:
        if p_type_n[0]:
            uc.print_error(f'Ausgabeart neu = {p_type_n[1]}')


if __name__ == '__main__':
    main()

```

