# Utility Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `get_3d_version`
- **_out_** `uint32`

## `get_3d_build`
- **_out_** `uint32`

## `get_3d_file_name`
- **_out_** `string`

## `get_3d_file_path`
- **_out_** `string`

## `set_project_data`
- **_out_** `none`
- **_in_** `string` _id_
- **_in_** `string` _data_

## `get_project_data`
- **_out_** `string`
- **_in_** `string` _id_

## `print_error`
- **_out_** `none`
- **_in_** `string` _message_

## `get_language`
- **_out_** `string`

## `print_message`
- **_out_** `none`
- **_in_** `string` _message_
- **_in_** `uint32` _row_
- **_in_** `uint32` _column_

## `get_user_int`
- **_out_** `int32`
- **_in_** `string` _message_

## `get_user_double`
- **_out_** `double`
- **_in_** `string` _message_

## `get_user_bool`
- **_out_** `boolean`
- **_in_** `string` _message_
- **_in_** `boolean` _default_yes_

## `get_user_string`
- **_out_** `string`
- **_in_** `string` _message_

## `get_project_name`
- **_out_** `string`

## `set_project_name`
- **_out_** `none`
- **_in_** `string` _project_name_

## `get_project_number`
- **_out_** `string`

## `set_project_number`
- **_out_** `none`
- **_in_** `string` _project_number_

## `get_project_part`
- **_out_** `string`

## `set_project_part`
- **_out_** `none`
- **_in_** `string` _project_part_

## `get_project_architect`
- **_out_** `string`

## `set_project_architect`
- **_out_** `none`
- **_in_** `string` _project_architect_

## `get_project_customer`
- **_out_** `string`

## `set_project_customer`
- **_out_** `none`
- **_in_** `string` _project_customer_

## `get_project_designer`
- **_out_** `string`

## `set_project_designer`
- **_out_** `none`
- **_in_** `string` _project_designer_

## `get_project_deadline`
- **_out_** `string`

## `set_project_deadline`
- **_out_** `none`
- **_in_** `string` _project_deadline_

## `get_project_user_attribute`
- **_out_** `string`
- **_in_** `uint32` _number_

## `set_project_user_attribute`
- **_out_** `none`
- **_in_** `uint32` _number_
- **_in_** `string` _user_attribute_

## `get_project_user_attribute_name`
- **_out_** `string`
- **_in_** `uint32` _number_

## `set_project_user_attribute_name`
- **_out_** `none`
- **_in_** `uint32` _number_
- **_in_** `string` _user_attribute_name_

## `get_project_latitude`
- **_out_** `double`

## `get_project_longitude`
- **_out_** `double`

## `set_project_latitude`
- **_out_** `none`
- **_in_** `double` _latitude_

## `set_project_longitude`
- **_out_** `none`
- **_in_** `double` _longitude_

## `get_project_address`
- **_out_** `string`

## `set_project_address`
- **_out_** `none`
- **_in_** `string` _address_

## `get_project_postal_code`
- **_out_** `string`

## `set_project_postal_code`
- **_out_** `none`
- **_in_** `string` _postal_code_

## `get_project_city`
- **_out_** `string`

## `set_project_city`
- **_out_** `none`
- **_in_** `string` _city_

## `get_project_country`
- **_out_** `string`

## `set_project_country`
- **_out_** `none`
- **_in_** `string` _country_

## `get3_d_userprofil_path`
- **_out_** `string`

## `get_user_file_from_dialog`
- **_out_** `string`
- **_in_** `string` _filter_

## `get_client_number`
- **_out_** `string`

## `get_user_point`
- **_out_** `point_3d`

## `disable_auto_display_refresh`
- **_out_** `none`

## `enable_auto_display_refresh`
- **_out_** `none`

## `create_new_guid`
- **_out_** `string`

## `print_to_console`
- **_out_** `none`
- **_in_** `string` _message_

## `export_screen_to_image`
- **_out_** `none`
- **_in_** `string` _file_path_
- **_in_** `uint32` _factor_

## `get_new_user_file_from_dialog`
- **_out_** `string`
- **_in_** `string` _filter_

## `api_autostart`
- **_out_** `uint32`
- **_in_** `string` _api_name_
- **_in_** `uint32` _option_

## `enable_autostart`
- **_out_** `none`
- **_in_** `string` _api_name_

## `disable_autostart`
- **_out_** `none`
- **_in_** `string` _api_name_

## `check_autostart`
- **_out_** `boolean`
- **_in_** `string` _api_name_

## `delete_project_data`
- **_out_** `none`
- **_in_** `string` _id_

## `run_external_program`
- **_out_** `boolean`
- **_in_** `string` _name_

## `save_3d_file_silently`
- **_out_** `none`

## `get_project_guid`
- **_out_** `string`

## `get_licence_first_part`
- **_out_** `string`

## `get_licence_second_part`
- **_out_** `string`

## `show_progress_bar`
- **_out_** `none`

## `update_progress_bar`
- **_out_** `none`
- **_in_** `int32` _value_

## `hide_progress_bar`
- **_out_** `none`

## `get_user_color`
- **_out_** `uint32`
- **_in_** `uint32` _initial_color_

## `get_3d_linear_units`
- **_out_** `string`

## `get_3d_linear_display_units`
- **_out_** `string`

## `get_3d_angular_units`
- **_out_** `string`

## `get_3d_angular_display_units`
- **_out_** `string`

## `get_3d_build_date`
- **_out_** `string`

## `get_project_elevation`
- **_out_** `double`

## `set_project_elevation`
- **_out_** `none`
- **_in_** `double` _elevation_

## `clear_errors`
- **_out_** `none`
