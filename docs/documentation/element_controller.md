# Element Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `get_all_identifiable_element_ids`
- **_out_** `element_list`

## `get_visible_identifiable_element_ids`
- **_out_** `element_list`

## `get_invisible_identifiable_element_ids`
- **_out_** `element_list`

## `get_active_identifiable_element_ids`
- **_out_** `element_list`

## `get_inactive_all_identifiable_element_ids`
- **_out_** `element_list`

## `get_inactive_visible_identifiable_element_ids`
- **_out_** `element_list`

## `delete_elements`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `join_elements`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `join_top_level_elements`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `create_rectangular_beam_points`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `double` _height_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_
- **_in_** `point_3d` _p3_

## `create_circular_beam_points`
- **_out_** `element`
- **_in_** `double` _diameter_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_
- **_in_** `point_3d` _p3_

## `create_square_beam_points`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_
- **_in_** `point_3d` _p3_

## `create_rectangular_beam_vectors`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `double` _height_
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_

## `create_circular_beam_vectors`
- **_out_** `element`
- **_in_** `double` _diameter_
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_

## `create_square_beam_vectors`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_

## `create_rectangular_panel_points`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `double` _thickness_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_
- **_in_** `point_3d` _p3_

## `create_rectangular_panel_vectors`
- **_out_** `element`
- **_in_** `double` _width_
- **_in_** `double` _thickness_
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _x_l_
- **_in_** `point_3d` _z_l_

## `create_drilling_points`
- **_out_** `element`
- **_in_** `double` _diameter_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_

## `create_drilling_vectors`
- **_out_** `element`
- **_in_** `double` _diameter_
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _x_l_

## `create_line_points`
- **_out_** `element`
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _p2_

## `create_line_vectors`
- **_out_** `element`
- **_in_** `double` _length_
- **_in_** `point_3d` _p1_
- **_in_** `point_3d` _xl_

## `create_node`
- **_out_** `element`
- **_in_** `point_3d` _p1_

## `solder_elements`
- **_out_** `element_list`
- **_in_** `element_list` _element_id_list_

## `convert_beam_to_panel`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `convert_panel_to_beam`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `delete_all_element_end_types`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `delete_all_element_processes`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `move_element`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `point_3d` _vector_

## `create_polygon_beam`
- **_out_** `element`
- **_in_** `vertex_list` _polygon_vertices_
- **_in_** `double` _thickness_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_

## `create_text_object`
- **_out_** `element`
- **_in_** `string` _text_
- **_in_** `point_3d` _position_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_
- **_in_** `double` _size_

## `copy_elements`
- **_out_** `element_list`
- **_in_** `element_list` _element_id_list_
- **_in_** `point_3d` _copy_vector_

## `rotate_elements`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `point_3d` _origin_
- **_in_** `point_3d` _rotation_axis_
- **_in_** `double` _rotation_angle_

## `subtract_elements`
- **_out_** `element_list`
- **_in_** `element_list` _hard_elements_
- **_in_** `element_list` _soft_elements_

## `check_element_id`
- **_out_** `boolean`
- **_in_** `element` _id_

## `start_element_module_calculation`
- **_out_** `none`
- **_in_** `element_list` _covers_

## `set_element_detail_path`
- **_out_** `none`
- **_in_** `string` _path_

## `get_element_detail_path`
- **_out_** `string`

## `get_element_cadwork_guid`
- **_out_** `string`
- **_in_** `element` _id_

## `get_element_from_cadwork_guid`
- **_out_** `element`
- **_in_** `string` _cadwork_guid_

## `add_elements_to_undo`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `int32` _cmd_

## `make_undo`
- **_out_** `none`

## `make_redo`
- **_out_** `none`

## `split_elements`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `set_line_to_marking_line`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `set_line_to_normal_line`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `create_auto_export_solid_from_standard`
- **_out_** `element`
- **_in_** `element_list` _elements_
- **_in_** `string` _output_name_
- **_in_** `string` _standard_element_name_

## `set_element_module_properties_for_elements`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `element_module_properties` _properties_

## `get_element_module_properties_for_element`
- **_out_** `element_module_properties`
- **_in_** `element` _id_

## `get_element_type_description`
- **_out_** `string`
- **_in_** `element` _id_

## `create_text_object_with_font`
- **_out_** `element`
- **_in_** `string` _text_
- **_in_** `point_3d` _position_
- **_in_** `point_3d` _xl_
- **_in_** `point_3d` _zl_
- **_in_** `double` _size_
- **_in_** `string` _font_name_

## `get_opening_variant_ids`
- **_out_** `element_list`
- **_in_** `element_list` _elements_
- **_in_** `int32` _opening_type_

## `get_parent_container_id`
- **_out_** `element`
- **_in_** `element` _id_

## `get_export_solid_content_elements`
- **_out_** `element_list`
- **_in_** `element` _id_

## `get_container_content_elements`
- **_out_** `element_list`
- **_in_** `element` _id_

## `apply_transformation_coordinate`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `point_3d` _old_point_
- **_in_** `point_3d` _old_xl_
- **_in_** `point_3d` _old_yl_
- **_in_** `point_3d` _new_point_
- **_in_** `point_3d` _new_xl_
- **_in_** `point_3d` _new_yl_

## `delete_elements_with_undo`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `add_created_elements_to_undo`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `add_modified_elements_to_undo`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `recreate_elements`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `check_if_elements_are_in_collision`
- **_out_** `boolean`
- **_in_** `element` _first_element_id_
- **_in_** `element` _second_element_id_

## `check_if_elements_are_in_contact`
- **_out_** `boolean`
- **_in_** `element` _first_element_id_
- **_in_** `element` _second_element_id_

## `create_multi_wall`
- **_out_** `none`
- **_in_** `element_list` _elements_

## `get_user_element_ids`
- **_out_** `element_list`

## `get_element_contact_vertices`
- **_out_** `vertex_list`
- **_in_** `element` _first_id_
- **_in_** `element` _second_id_

## `get_nesting_parent_id`
- **_out_** `element`
- **_in_** `element` _id_

## `get_user_element_ids_with_existing`
- **_out_** `element_list`
- **_in_** `element_list` _elements_

## `clear_errors`
- **_out_** `none`

## `glide_elements`
- **_out_** `none`
- **_in_** `element_list` _element_ids_
- **_in_** `point_3d` _glide_point_

## `get_element_contact_facets`
- **_out_** `faet_list`
- **_in_** `element` _first_id_
- **_in_** `element` _second_id_

## `get_element_raw_interface_vertices`
- **_out_** `vertex_list`
- **_in_** `element` _first_id_
- **_in_** `element` _second_id_

## `cut_elements_with_miter`
- **_out_** `boolean`
- **_in_** `element` _first_id_
- **_in_** `element` _second_id_

## `cut_element_with_plane`
- **_out_** `boolean`
- **_in_** `element` _id_
- **_in_** `point_3d` _cut_plane_normal_vector_
- **_in_** `double` _distance_from_global_origin_
