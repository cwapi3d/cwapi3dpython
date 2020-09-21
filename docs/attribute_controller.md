# Attribute Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `get_name`
- **_out_** `string`
- **_in_** `element` _id_

## `set_name`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _name_

## `get_group`
- **_out_** `string`
- **_in_** `element` _id_

## `set_group`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _group_

## `get_subgroup`
- **_out_** `string`
- **_in_** `element` _id_

## `set_subgroup`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _subgroup_

## `get_comment`
- **_out_** `string`
- **_in_** `element` _id_

## `set_comment`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _comment_

## `get_user_attribute`
- **_out_** `string`
- **_in_** `element` _id_
- **_in_** `uint32` _number_

## `set_user_attribute`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `uint32` _number_
- **_in_** `string` _user_attribute_

## `get_sku`
- **_out_** `string`
- **_in_** `element` _id_

## `set_sku`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _sku_

## `get_production_number`
- **_out_** `uint32`
- **_in_** `element` _id_

## `set_production_number`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `uint32` _production_number_

## `get_part_number`
- **_out_** `uint32`
- **_in_** `element` _id_

## `set_part_number`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `uint32` _part_number_

## `get_additional_data`
- **_out_** `string`
- **_in_** `element` _id_
- **_in_** `string` _data_id_

## `set_additional_data`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _data_id_
- **_in_** `string` _data_text_

## `delete_additional_data`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _data_id_

## `get_user_attribute_name`
- **_out_** `string`
- **_in_** `uint32` _number_

## `set_user_attribute_name`
- **_out_** `none`
- **_in_** `uint32` _number_
- **_in_** `string` _user_attribute_name_

## `get_wall_situation`
- **_out_** `string`
- **_in_** `element` _id_

## `is_beam`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_panel`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_opening`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_wall`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_floor`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_roof`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_metal`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_export_solid`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_container`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_connector_axis`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_drilling`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_node`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_auxiliary`
- **_out_** `boolean`
- **_in_** `element` _id_

## `get_element_material_name`
- **_out_** `string`
- **_in_** `element` _id_

## `get_prefab_layer`
- **_out_** `string`
- **_in_** `element` _id_

## `get_machine_calculation_set`
- **_out_** `string`
- **_in_** `element` _id_

## `get_cutting_set`
- **_out_** `string`
- **_in_** `element` _id_

## `set_process_type_and_extended_settings_from_name`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `set_name_process_type`
- **_out_** `none`
- **_in_** `string` _name_
- **_in_** `process_type` _process_type_

## `get_name_process_type`
- **_out_** `process_type`
- **_in_** `string` _name_

## `set_name_extended_settings`
- **_out_** `none`
- **_in_** `string` _name_
- **_in_** `extended_settings` _extended_settings_

## `get_name_extended_settings`
- **_out_** `extended_settings`
- **_in_** `string` _name_

## `get_output_type`
- **_out_** `process_type`
- **_in_** `element` _id_

## `set_output_type`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `process_type` _process_type_

## `get_extended_settings`
- **_out_** `extended_settings`
- **_in_** `element` _id_

## `set_extended_settings`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `extended_settings` _extended_settings_

## `get_element_type`
- **_out_** `element_type`
- **_in_** `element` _id_

## `set_wall`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `set_floor`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `set_opening`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_

## `get_fastening_attribute`
- **_out_** `string`
- **_in_** `element` _id_

## `set_fastening_attribute`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _value_

## `is_roof_surface`
- **_out_** `boolean`
- **_in_** `element` _id_

## `is_caddy_object`
- **_out_** `boolean`
- **_in_** `element` _id_

## `set_element_material`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `material` _material_

## `get_assembly_number`
- **_out_** `string`
- **_in_** `element` _id_

## `set_assembly_number`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _assembly_number_

## `get_list_quantity`
- **_out_** `uint32`
- **_in_** `element` _id_

## `set_list_quantity`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `uint32` _list_quantity_

## `is_envelope`
- **_out_** `boolean`
- **_in_** `element` _id_

## `set_layer_settings`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `layer_settings` _layer_settings_

## `set_ignore_in_vba_calculation`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `boolean` _ignore_

## `get_ignore_in_vba_calculation`
- **_out_** `boolean`
- **_in_** `element` _element_

## `clear_errors`
- **_out_** `none`

## `is_architecture_wall2dc`
- **_out_** `boolean`
- **_in_** `element` _element_

## `is_architecture_wall_xml`
- **_out_** `boolean`
- **_in_** `element` _element_

## `set_reference_wall2dc`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `string` _2dc_file_path_
