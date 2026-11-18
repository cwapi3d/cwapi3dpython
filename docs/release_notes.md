# Release Notes

Changes to the `cwapi3d` Python API, newest first. Each version is published to
[PyPI](https://pypi.org/project/cwapi3d/). The major version tracks the cadwork 3D release (`33` = cadwork v2026).

This page keeps the **last 10 releases**. Older notes are in the
[git history](https://github.com/cwapi3d/cwapi3dpython/commits/main/docs/release_notes.md).

<!-- release:33.407.2 -->
## 33.407.2 — 2026-11-18

[PR #453](https://github.com/cwapi3d/cwapi3dpython/pull/453) · `pip install cwapi3d==33.407.2`

Plugins can now set, switch and read the rotated origin (the "Ref" button coordinate system). The user-input functions now document what they return in scripts started with `/PLUGIN=` or `/RUNPROGRAM=`.

### Added

- Rotated origin, the "Ref" button coordinate system (requires API version 406; not available in auto-attribute scripts):
  [`utility_controller.set_rotated_origin_axes`][utility_controller.set_rotated_origin_axes] saves its axes,
  [`utility_controller.enable_rotated_origin`][utility_controller.enable_rotated_origin] and
  [`utility_controller.disable_rotated_origin`][utility_controller.disable_rotated_origin] switch it on and off,
  [`utility_controller.is_rotated_origin_enabled`][utility_controller.is_rotated_origin_enabled] and
  [`utility_controller.has_rotated_origin_axes`][utility_controller.has_rotated_origin_axes] check its state, and
  [`utility_controller.get_rotated_origin_x_axis`][utility_controller.get_rotated_origin_x_axis],
  [`utility_controller.get_rotated_origin_y_axis`][utility_controller.get_rotated_origin_y_axis] and
  [`utility_controller.get_rotated_origin_z_axis`][utility_controller.get_rotated_origin_z_axis] get the saved axes as unit vectors.

### Documentation

- `utility_controller`: the 14 `get_user_*` input functions now state what they return in a script started with `/PLUGIN=` or `/RUNPROGRAM=`, where no query is shown. [`utility_controller.close_cadwork_document_unsaved`][utility_controller.close_cadwork_document_unsaved] is ignored in such a script, and [`utility_controller.close_cadwork_document_saved`][utility_controller.close_cadwork_document_saved] only saves.
- [`menu_controller.display_simple_menu`][menu_controller.display_simple_menu]: returns an empty string in a `/PLUGIN=` or `/RUNPROGRAM=` script; new example.
- `file_controller`: 10 import functions now explain that imported elements stay visible with automatic display refresh off, and how to display them afterwards.
- [`bim_controller.set_building_and_storey`][bim_controller.set_building_and_storey]: no IFC license is required.
<!-- /release:33.407.2 -->

<!-- release:33.407.0 -->
## 33.407.0 — 2026-11-18

[PR #452](https://github.com/cwapi3d/cwapi3dpython/pull/452) · `pip install cwapi3d==33.407.0`

Documentation-only release: no API changes.

### Documentation

- [`multi_layer_cover_controller.set_element_multi_layer_set`][multi_layer_cover_controller.set_element_multi_layer_set]: now documents that the cover takes the thickness of the assigned multi layer set.
- Reworked guide pages for setup, debugging and troubleshooting.
<!-- /release:33.407.0 -->

<!-- release:33.397.17 -->
## 33.397.17 — 2026-11-11

[PR #450](https://github.com/cwapi3d/cwapi3dpython/pull/450) · `pip install cwapi3d==33.397.17`

The docstrings of every controller were rewritten from the C++ implementation, and several stub signatures were corrected to match the bindings. Type hints and IDE hints change for the functions listed under Fixed.

### Added

- [`geometry_controller.element_collision_type`][geometry_controller.element_collision_type]: new enum for how the geometry of two elements relates, as returned by [`geometry_controller.get_element_collision_type`][geometry_controller.get_element_collision_type]: `none`, `touching`, `contained`, `contained_and_touching`, `interlocking`, `coincident`, `unclassified`, `unknown`.

### Fixed

- [`connector_axis_controller.get_intersection_count`][connector_axis_controller.get_intersection_count]: the stub declared `get_intersection_count(intersection_index: UnsignedInt) -> int`; it now matches the binding: `get_intersection_count(axis_id: ElementId) -> int`.
- [`connector_axis_controller.get_section_contact_element`][connector_axis_controller.get_section_contact_element]: `axis_id` is an `ElementId`, not a `float`.
- [`endtype_controller.get_endtype_name`][endtype_controller.get_endtype_name]: the stub declared `get_endtype_name(element_id: ElementId) -> str`; it now matches the binding: `get_endtype_name(endtype_id: EndtypeId) -> str`.
- [`geometry_controller.get_element_collision_type`][geometry_controller.get_element_collision_type]: returns `element_collision_type` instead of `Any`.
- [`material_controller.set_texture_color`][material_controller.set_texture_color]: the stub declared `set_texture_color(color_nb: UnsignedInt, material_id: MaterialId) -> None`; it now matches the binding: `set_texture_color(material_id: MaterialId, color: int) -> None`.
- `multi_layer_cover_controller`: the layer type is an `int`, not `multi_layer_type`, in [`multi_layer_cover_controller.add_layer`][multi_layer_cover_controller.add_layer], [`multi_layer_cover_controller.add_layer_by_standard_elements`][multi_layer_cover_controller.add_layer_by_standard_elements], [`multi_layer_cover_controller.insert_layer`][multi_layer_cover_controller.insert_layer], [`multi_layer_cover_controller.set_layer_type`][multi_layer_cover_controller.set_layer_type] and the return value of [`multi_layer_cover_controller.get_layer_type`][multi_layer_cover_controller.get_layer_type].
- [`utility_controller.create_snapshot`][utility_controller.create_snapshot]: the stub declared `create_snapshot() -> str`; it now matches the binding: `create_snapshot(image_format: str = 'PNG', quality: int = -1, white_background: bool = True) -> str`.
- [`utility_controller.get_project_data`][utility_controller.get_project_data] and [`utility_controller.delete_project_data`][utility_controller.delete_project_data]: the parameter is `project_data_id`, not `element_id`.
- [`attribute_controller.set_attribute_display_settings_for_3d`][attribute_controller.set_attribute_display_settings_for_3d] and [`attribute_controller.set_attribute_display_settings_for_framed_wall_beam`][attribute_controller.set_attribute_display_settings_for_framed_wall_beam]: a duplicate declaration was removed.

### Documentation

- Docstrings rewritten from the C++ implementation, with parameter meaning, failure values, side effects and examples: `attribute_controller` (188 functions), `element_controller` (207), `utility_controller` (134), `geometry_controller` (104), `material_controller` (80), `visualization_controller` (72), `connector_axis_controller` (50), `multi_layer_cover_controller` (48), `file_controller` (43), `bim_controller` (42), `shop_drawing_controller` (23), `dimension_controller` (22), `endtype_controller` (20), `machine_controller` (20), `scene_controller` (17), `list_controller` (16), `menu_controller` (1) and `cadwork` (2).
<!-- /release:33.397.17 -->

<!-- release:33.397.2 -->
## 33.397.2 — 2026-11-10

[PR #434](https://github.com/cwapi3d/cwapi3dpython/pull/434) · `pip install cwapi3d==33.397.2`

Documentation-only release: no API changes.

### Documentation

- `element_controller`: docstrings of 207 functions rewritten from the C++ implementation.
<!-- /release:33.397.2 -->

<!-- release:33.397.0 -->
## 33.397.0 — 2026-11-04

[PR #430](https://github.com/cwapi3d/cwapi3dpython/pull/430) · `pip install cwapi3d==33.397.0`

Plugins can now ask the user to pick an edge in the 3D view.

### Added

- [`utility_controller.get_user_edge`][utility_controller.get_user_edge]: asks the user to pick an edge in the 3D view, either by clicking an existing edge or by clicking 2 points, and returns its two end points in global coordinates (an empty list if the user aborted with Esc). The point order is not guaranteed.
<!-- /release:33.397.0 -->

<!-- release:33.396.0 -->
## 33.396.0 — 2026-11-03

[PR #428](https://github.com/cwapi3d/cwapi3dpython/pull/428) · `pip install cwapi3d==33.396.0`

The background of each render view can now be read and set from a plugin: plain black, plain white or a user-defined color, as in the graphics options dialog.

### Added

- [`visualization_controller.get_background_color`][visualization_controller.get_background_color]: gets the color a render view actually shows: black or white for those types, the stored color for [`user`][cadwork.background_type.background_type.user], and black for an [`image`][cadwork.background_type.background_type.image] background, which has no single color. The render view need not be the one currently displayed.
- [`visualization_controller.set_background_color`][visualization_controller.set_background_color]: stores a color for a render view and switches its background type to [`user`][cadwork.background_type.background_type.user], so it shows immediately. Components above 255 are clamped. The background is saved with the drawing, so the active document is marked modified.
- [`visualization_controller.get_background_type`][visualization_controller.get_background_type]: gets how a render view's background is filled; [`black`][cadwork.background_type.background_type.black] for an undefined render view.
- [`visualization_controller.set_background_type`][visualization_controller.set_background_type]: switches a render view between [`black`][cadwork.background_type.background_type.black], [`white`][cadwork.background_type.background_type.white] and [`user`][cadwork.background_type.background_type.user]; switching away from `user` keeps the stored color for later. [`image`][cadwork.background_type.background_type.image] cannot be set through the API, because it needs an image chosen in the graphics options dialog; passing it changes nothing.
- [`cadwork.render_view_type`][cadwork.render_view_type]: new enum for the render views of the 3d window, each with its own background: `wireframe`, `shading1`, `shading2`, `hidden_line`, `hidden_line_dashed`, `drawing2d`.
- [`cadwork.background_type`][cadwork.background_type]: new enum for how a render view's background is filled: `black`, `white`, `user`, `image`.
<!-- /release:33.396.0 -->

<!-- release:33.394.1 -->
## 33.394.1 — 2026-11-03

[PR #429](https://github.com/cwapi3d/cwapi3dpython/pull/429) · `pip install cwapi3d==33.394.1`

Documentation-only release: no API changes.

### Documentation

- [`cadwork.extended_settings`][cadwork.extended_settings.extended_settings]: the class and its 29 getters and setters are now documented.
<!-- /release:33.394.1 -->

<!-- release:33.394.0 -->
## 33.394.0 — 2026-10-29

[PR #427](https://github.com/cwapi3d/cwapi3dpython/pull/427) · `pip install cwapi3d==33.394.0`

Documentation-only release: no API changes.

### Documentation

- `element_controller`: documents the name and folder limits of standard elements in the docstrings of 16 standard element functions, such as [`create_standard_beam_points`][element_controller.create_standard_beam_points], [`export_as_standard_element`][element_controller.export_as_standard_element] and [`get_standard_beam_list`][element_controller.get_standard_beam_list].
<!-- /release:33.394.0 -->

<!-- release:33.392.0 -->
## 33.392.0 — 2026-10-27

[PR #426](https://github.com/cwapi3d/cwapi3dpython/pull/426) · `pip install cwapi3d==33.392.0`

Standard elements can now be looked up by name and their names resolved from a GUID.

### Added

- [`element_controller.get_standard_element_guid_from_name`][element_controller.get_standard_element_guid_from_name]: gets the GUID of a standard element from its name, matched in the current cadwork language.
- [`element_controller.get_standard_element_name_from_guid`][element_controller.get_standard_element_name_from_guid]: gets the name of a standard element from its GUID, for every kind of standard element, steel profiles included.
<!-- /release:33.392.0 -->

<!-- release:33.384.0 -->
## 33.384.0 — 2026-10-20

[PR #423](https://github.com/cwapi3d/cwapi3dpython/pull/423) · `pip install cwapi3d==33.384.0`

Spline volumes can now be created from surfaces, and shop drawing wall sections and export solid cuts can be read back as planes.

### Added

- [`element_controller.create_spline_from_surfaces`][element_controller.create_spline_from_surfaces]: creates a spline volume by skinning a series of surface elements, like the "Spline" command of the GUI.
- [`element_controller.create_spline_from_surface_and_line`][element_controller.create_spline_from_surface_and_line]: creates a spline volume by sweeping a surface element along a line element.
- [`shop_drawing_controller.get_wall_sections`][shop_drawing_controller.get_wall_sections]: gets the wall sections of a wall, floor or roof as planes.
- [`shop_drawing_controller.get_export_solid_cuts`][shop_drawing_controller.get_export_solid_cuts]: gets the cuts of an export solid or container as planes.
- [`cadwork.wall_section`][cadwork.wall_section]: new class with `get_type`, `get_point` and `get_normal`.
- [`cadwork.export_solid_cut`][cadwork.export_solid_cut]: new class with `get_name`, `get_point`, `get_normal` and `get_up_vector`.
- [`cadwork.spline_surface_order`][cadwork.spline_surface_order]: new enum with `linear` and `circular`.
- [`cadwork.wall_section_type`][cadwork.wall_section_type]: new enum with `horizontal` and `vertical`.
<!-- /release:33.384.0 -->
