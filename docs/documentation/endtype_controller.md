# End-Type Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `get_endtype_name`
- **_out_** `string`
- **_in_** `end_type` _id_

## `get_endtype_id`
- **_out_** `end_type`
- **_in_** `string` _name_

## `get_endtype_id_start`
- **_out_** `end_type`
- **_in_** `element` _id_

## `get_endtype_id_end`
- **_out_** `end_type`
- **_in_** `element` _id_

## `get_endtype_id_fac`
- **_out_** `end_type`
- **_in_** `element` _id_
- **_in_** `uint32` _face_number_

## `get_endtype_name_start`
- **_out_** `string`
- **_in_** `element` _id_

## `get_endtype_name_end`
- **_out_** `string`
- **_in_** `element` _id_

## `get_endtype_name_facet`
- **_out_** `string`
- **_in_** `element` _id_
- **_in_** `uint32` _face_number_

## `set_endtype_name_start`
- **_out_** `none`
- **_in_** `element` _id_
- **_in_** `string` _name_

## `set_endtype_name_end`
- **_out_** `none`
- **_in_** `element` _id_
- **_in_** `string` _name_

## `set_endtype_name_facet`
- **_out_** `none`
- **_in_** `element` _element_id_
- **_in_** `string` _name_
- **_in_** `uint32` _face_nuber_

## `set_endtype_id_start`
- **_out_** `none`
- **_in_** `element` _element_id_
- **_in_** `end_type` _endtype_id_

## `set_endtype_id_end`
- **_out_** `none`
- **_in_** `element` _element_id_
- **_in_** `end_type` _endtype_id_

## `set_endtype_id_fac`
- **_out_** `none`
- **_in_** `element` _element_id_
- **_in_** `end_type` _endtype_id_
- **_in_** `uint32` _face_number_

## `create_new_endtype`
- **_out_** `end_type`
- **_in_** `string` _endtype_name_
- **_in_** `uint32` _endtype_id_
- **_in_** `string` _folder_name_

## `clear_errors`
- **_out_** `none`
