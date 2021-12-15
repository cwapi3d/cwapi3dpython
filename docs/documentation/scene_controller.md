# Scene Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `add_scene`
- **_out_** `boolean`
- **_in_** `string` _name_

## `rename_scene`
- **_out_** `boolean`
- **_in_** `string` _old_name_
- **_in_** `string` _new_name_

## `delete_scene`
- **_out_** `boolean`
- **_in_** `string` _name_

## `add_elements_to_scene`
- **_out_** `boolean`
- **_in_** `string` _name_
- **_in_** `element_list` _element_ids_

## `remove_elements_from_scene`
- **_out_** `boolean`
- **_in_** `string` _name_
- **_in_** `element_list` _element_ids_

## `get_elements_from_scene`
- **_out_** `element_list`
- **_in_** `string` _name_

## `activate_scene`
- **_out_** `boolean`
- **_in_** `string` _name_

## `clear_errors`
- **_out_** `none`
