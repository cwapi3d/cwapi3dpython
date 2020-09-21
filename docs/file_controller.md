# File Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `export_stl_file`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _file_path_

## `import_step_file`
- **_out_** `element_list`
- **_in_** `string` _file_path_
- **_in_** `double` _scale_factor_

## `import_step_file_with_message_option`
- **_out_** `element_list`
- **_in_** `string` _file_path_
- **_in_** `double` _scale_factor_
- **_in_** `boolean` _hide_message_

## `export_webgl`
- **_out_** `boolean`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _file_path_

## `export3d_file`
- **_out_** `boolean`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _file_path_

## `import_sat_file`
- **_out_** `element_list`
- **_in_** `string` _file_path_
- **_in_** `double` _scale_factor_
- **_in_** `boolean` _binary_

## `import_3dc_file`
- **_out_** `element_list`
- **_in_** `string` _file_path_

## `import_rhino_file`
- **_out_** `element_list`
- **_in_** `string` _file_path_
- **_in_** `boolean` _without_dialog_

## `export_step_file`
- **_out_** `none`
- **_in_** `element_list` _element_list_
- **_in_** `string` _file_path_
- **_in_** `double` _scale_factor_
- **_in_** `int32` _version_
- **_in_** `boolean` _text_mode_

## `import_3dz_file`
- **_out_** `none`
- **_in_** `string` _file_path_

## `export_obj_file`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `string` _file_path_

## `import_sat_file_silently`
- **_out_** `element_list`
- **_in_** `string` _file_path_
- **_in_** `double` _scale_factor_
- **_in_** `boolean` _binary_

## `export_fbx_file`
- **_out_** `none`
- **_in_** `element_list` _elements_
- **_in_** `string` _file_path_
- **_in_** `uint32` _f_b_x_format_

## `clear_errors`
- **_out_** `none`

## `import_3dc_file_with_glide`
- **_out_** `element_list`
- **_in_** `string` _file_path_

## `import_btl_file`
- **_out_** `none`
- **_in_** `string` _file_path_

## `export_3dc_file`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _file_path_

## `import_btl_file_for_nesting`
- **_out_** `none`
- **_in_** `string` _file_path_

## `export_btl_file_for_nesting`
- **_out_** `none`
- **_in_** `string` _file_path_

## `export_rhino_file`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _file_path_
- **_in_** `int32` _version_
- **_in_** `boolean` _use_default_assignment_
- **_in_** `boolean` _write_standard_attributes_
