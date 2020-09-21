# Connector Axis Controller

## `get_last_error`
- **_out_** `string`
- **_in_** `int32` _error_code_

## `create_standard_connector`
- **_out_** `element`
- **_in_** `string` _axis_name_
- **_in_** `point_3d` _point1_
- **_in_** `point_3d` _point2_

## `get_item_guid_by_name`
- **_out_** `string`
- **_in_** `string` _name_
- **_in_** `uint64` _item_type_

## `get_bolt_length`
- **_out_** `double`
- **_in_** `element` _axis_id_

## `set_bolt_length`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `double` _length_

## `get_bolt_over_length`
- **_out_** `double`
- **_in_** `element` _axis_id_

## `set_bolt_over_length`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `double` _over_length_

## `get_bolt_length_automatic`
- **_out_** `boolean`
- **_in_** `element` _axis_id_

## `set_bolt_length_automatic`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `boolean` _length_automatic_

## `get_bolt_item_guid`
- **_out_** `string`
- **_in_** `element` _axis_id_

## `set_bolt_item`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `string` _item_guid_

## `set_diameter`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `double` _diameter_

## `set_section_diameter`
- **_out_** `none`
- **_in_** `element` _axis_id_
- **_in_** `uint32` _section_nr_
- **_in_** `double` _diameter_

## `get_section_diameter`
- **_out_** `double`
- **_in_** `element` _axis_id_
- **_in_** `uint32` _section_nr_

## `get_axis_items_guids`
- **_out_** `string_list`
- **_in_** `element` _axis_id_

## `get_axis_item_name`
- **_out_** `string`
- **_in_** `string` _guid_

## `get_axis_item_material`
- **_out_** `string`
- **_in_** `string` _guid_

## `get_axis_item_norm`
- **_out_** `string`
- **_in_** `string` _g_u_id_

## `get_axis_item_strength_category`
- **_out_** `string`
- **_in_** `string` _guid_

## `get_axis_item_user_field`
- **_out_** `string`
- **_in_** `string` _guid_
- **_in_** `int32` _user_item_nr_

## `get_axis_item_order_number`
- **_out_** `string`
- **_in_** `string` _guid_

## `get_bolt_order_number`
- **_out_** `string`
- **_in_** `element` _axis_id_

## `check_axis`
- **_out_** `boolean`
- **_in_** `element` _axis_id_

## `clear_errors`
- **_out_** `none`
