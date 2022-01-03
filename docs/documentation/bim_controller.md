# BIM Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `get_ifc_guid`
- **_out_** `string`
- **_in_** `element` _id_

## `set_building_and_storey`
- **_out_** `none`
- **_in_** `element_list` _element_id_list_
- **_in_** `string` _building_
- **_in_** `string` _storey_

## `get_building`
- **_out_** `string`
- **_in_** `element` _element_

## `get_storey`
- **_out_** `string`
- **_in_** `element` _element_

## `clear_errors`
- **_out_** `none`

## `get_ifc2x3_element_type`
- **_out_** `ifc_2x3_element_type`
- **_in_** `element` _element_id_

## `set_ifc2x3_element_type`
- **_out_** `none`
- **_in_** `element_list` _element_ids_
- **_in_** `ifc_2x3_element_type` _element_type_

## `import_ifc_as_graphical_object`
- **_out_** `boolean`
- **_in_** `string` _file_path_

## `import_bcf`
- **_out_** `boolean`
- **_in_** `string` _file_path_

## `export_bcf`
- **_out_** `boolean`
- **_in_** `string` _file_path_

## `export_ifc`
- **_out_** `boolean`
- **_in_** `element_list` _element_ids_
- **_in_** `string` _file_path_
