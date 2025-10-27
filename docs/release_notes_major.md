# New methods added between the latest version of v30 and v32

## New methods in class:

### Class: connector_axis_controller

* get_counterbore_depth_for_end_side
* get_counterbore_depth_for_start_side
* get_counterbore_diameter_for_end_side
* get_counterbore_diameter_for_start_side
* get_counterbore_is_conical_for_end_side
* get_counterbore_is_conical_for_start_side
* get_intersection_count
* get_item_guids_at_intersection
* get_section_length
* get_section_oblong_drilling_angle
* get_section_oblong_drilling_is_enabled
* get_section_oblong_drilling_negative_value
* get_section_oblong_drilling_positive_value
* set_counterbore_for_end_side
* set_counterbore_for_start_side
* set_item_guids_at_intersection
* set_section_oblong_drilling_is_disabled
* set_section_oblong_drilling_is_enabled

### Class: dimension_controller

* get_dimension_base_format

### Class: element_controller

* cast_ray_and_get_element_intersections
* filter_elements
* map_elements

### Class: file_controller

* export_dstv_file
* export_dxf_file

### Class: machine_controller

* get_element_btl_processings
* get_element_hundegger_processings
* get_processing_btl_parameter_set
* get_processing_code
* get_processing_name
* get_processing_points

### Class: utility_controller

* get_3d_version_name
* redirect_python_output_to_logger

## New classes

### Class: dimension_base_format

* __int__

### Class: dxf_export_version

* __int__

### Class: dxf_layer_format_type

* __int__

### Class: element_filter

* set_comment
* set_group
* set_name
* set_part_number
* set_production_number
* set_sku
* set_subgroup
* set_user_attribute

### Class: element_map_query

* set_by_building
* set_by_comment
* set_by_group
* set_by_name
* set_by_part_number
* set_by_production_number
* set_by_sku
* set_by_storey
* set_by_subgroup
* set_by_user_attribute

### Class: hit_result

* get_hit_element_ids
* get_hit_vertices_by_element

### Class: ifc_options_properties

* get_export_quantity_sets
* set_export_quantity_sets

### Class: point

* __init__

### Class: point_3d

* __add__
* __eq__
* __getitem__
* __iadd__
* __imul__
* __isub__
* __itruediv__
* __mul__
* __ne__
* __neg__
* __repr__
* __rmul__
* __setitem__
* __sub__
* __truediv__

### Class: text_object_options

* get_draw_on_top
* set_draw_on_top

### Class: vba_catalog_item_type

* __int__

### Class: window_geometry

* __init__
