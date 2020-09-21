# Shop Drawing Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `export_2d_wireframe_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `boolean` _with_layout_

## `export_2d_hidden_lines_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `boolean` _with_layout_

## `export_2d_wireframe_with_2dc`
- **_out_** `none`
- **_in_** `string` _file_path_
- **_in_** `boolean` _with_layout_

## `export_2d_hidden_lines_with_2dc`
- **_out_** `none`
- **_in_** `string` _file_path_
- **_in_** `boolean` _with_layout_

## `export_wall_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `element_list` _element_id_list_

## `export_export_solid_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `element_list` _element_id_list_

## `export_piece_by_piece_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `element_list` _element_id_list_

## `assign_export_solid`
- **_out_** `none`
- **_in_** `element_list` _ceo_element_
- **_in_** `element_list` _element_id_list_

## `export_container_with_clipboard`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `element_list` _elements_

## `add_wall_section_horizontal`
- **_out_** `none`
- **_in_** `element` _element_
- **_in_** `point_3d` _position_

## `add_wall_section_vertical`
- **_out_** `none`
- **_in_** `element` _element_
- **_in_** `point_3d` _position_

## `export_wall_with_clipboard_and_presetting`
- **_out_** `none`
- **_in_** `uint32` _clipboard_number_
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _presetting_file_

## `load_export_piece_by_piece_settings`
- **_out_** `none`
- **_in_** `string` _settings_file_path_

## `save_export_piece_by_piece_settings`
- **_out_** `none`
- **_in_** `string` _settings_file_path_

## `clear_errors`
- **_out_** `none`
