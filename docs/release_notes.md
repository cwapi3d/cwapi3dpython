# Release Notes

Changes to the `cwapi3d` Python API, newest first. Each version is published to
[PyPI](https://pypi.org/project/cwapi3d/). The major version tracks the cadwork 3D release (`33` = cadwork v2026).

This page keeps the **last 10 releases**. Older notes are in the
[git history](https://github.com/cwapi3d/cwapi3dpython/commits/main/docs/release_notes.md).
For everything that changed between two cadwork major versions, see the [Major Release Notes](release_notes_major.md).

<!-- release:33.384.0 -->
## 33.384.0 — 2026-10-20

`pip install cwapi3d==33.384.0`

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

<!-- release:33.383.0 -->
## 33.383.0 — 2026-10-13

[PR #418](https://github.com/cwapi3d/cwapi3dpython/pull/418) · `pip install cwapi3d==33.383.0`

SAT, STEP and IGES exports can now be configured through typed option objects and combined with element level-of-detail settings.

### Added

- [`file_controller.export_file_with_options`][file_controller.export_file_with_options]: exports a file using format-specific export options decorated with element level-of-detail options.
- [`file_controller.get_sat_export_options`][file_controller.get_sat_export_options], [`file_controller.get_step_export_options`][file_controller.get_step_export_options], [`file_controller.get_iges_export_options`][file_controller.get_iges_export_options]: create a new options instance for that format with default values.
- [`cadwork.file_export_options`][cadwork.file_export_options]: common base for all format-specific export options, with `get_file_export_format` and `get_level_of_detail_options`.
- [`cadwork.sat_export_options`][cadwork.sat_export_options]: SAT options: binary output, scale factor and ACIS version (`ACIS_V21_0` … `ACIS_V34_0`).
- [`cadwork.step_export_options`][cadwork.step_export_options]: STEP options: scale factor, imperial units and version (`AP203`, `AP214`).
- [`cadwork.iges_export_options`][cadwork.iges_export_options]: IGES options: scale factor.
- [`cadwork.file_export_format`][cadwork.file_export_format]: new enum identifying the format of an options instance: `sat`, `step`, `iges`.
- [`cadwork.element_level_of_detail_options`][cadwork.element_level_of_detail_options]: format-agnostic level-of-detail options: cut drillings, openings, MEP elements and end type counterparts, and materialize end types and MEP elements.
<!-- /release:33.383.0 -->

<!-- release:33.382.0 -->
## 33.382.0 — 2026-10-13

[PR #414](https://github.com/cwapi3d/cwapi3dpython/pull/414) · `pip install cwapi3d==33.382.0`

Corrects the documented signature of `set_texture_transparency`.

### Fixed

- [`material_controller.set_texture_transparency`][material_controller.set_texture_transparency]: the stub declared the arguments in the wrong order. It now matches the binding: `set_texture_transparency(material_id: MaterialId, texture_transparency: UnsignedInt)`, with the transparency given in percent (0–100).

### Documentation

- `material_controller`: improved docstring of `get_texture_transparency`.
<!-- /release:33.382.0 -->

<!-- release:33.380.0 -->
## 33.380.0 — 2026-10-09

[PR #417](https://github.com/cwapi3d/cwapi3dpython/pull/417) · `pip install cwapi3d==33.380.0`

New export solid cuts and wall sections in shop drawings, and many more element type checks.

### Added

- [`shop_drawing_controller.add_export_solid_cut`][shop_drawing_controller.add_export_solid_cut]: adds a named cut to an export solid or container, defined by a plane normal and an origin point on the plane.
- [`shop_drawing_controller.add_export_solid_cut_at_relative_position`][shop_drawing_controller.add_export_solid_cut_at_relative_position]: adds a named cut to an export solid or container, defined by a plane normal and a relative position.
- [`shop_drawing_controller.add_wall_section_horizontal_at_relative_position`][shop_drawing_controller.add_wall_section_horizontal_at_relative_position]: adds a horizontal section to a wall, floor or roof at a relative position across the element's width.
- [`cadwork.element_type`][cadwork.element_type]: new type tests `is_framed_wall`, `is_framed_floor`, `is_framed_roof`, `is_solid_wood_wall`, `is_solid_wood_floor`, `is_solid_wood_roof`, `is_log_wall`, `is_roof_surface`, `is_roof_lathing_surface`, `is_circular_mep`, `is_rectangular_mep`, `is_element_light`, `is_exchange_object`, `is_pdf_object`, `is_point_cloud`, `is_point_cloud_clipping_box`, and the matching setters `set_framed_wall`, `set_framed_floor`, `set_framed_roof`, `set_solid_wood_wall`, `set_solid_wood_floor`, `set_solid_wood_roof`, `set_log_wall`, `set_roof_surface`, `set_circular_mep`, `set_rectangular_mep`.
- [`cadwork.shortcut_key_modifier`][cadwork.shortcut_key_modifier]: new member `no_modifier`.

### Documentation

- More usage examples across the documentation.
<!-- /release:33.380.0 -->

<!-- release:33.378.0 -->
## 33.378.0 — 2026-10-07

[PR #412](https://github.com/cwapi3d/cwapi3dpython/pull/412) · `pip install cwapi3d==33.378.0`

Line elements from arc and spline segments, prefab layer queries, multi layer set editing and navigation widget control.

### Added

- [`element_controller.create_line_from_segments`][element_controller.create_line_from_segments]: creates a Line element from a mixed path of straight, arc and natural-cubic-spline segments.
- [`element_controller.get_line_segments`][element_controller.get_line_segments]: gets the defining segments of a Line element, whether straight, arc or spline.
- [`cadwork.element_segment`][cadwork.element_segment]: a line segment with `type`, `position` and `support_position`.
- [`cadwork.element_segment_type`][cadwork.element_segment_type]: new enum: `straight`, `arc`, `spline`.
- [`attribute_controller.get_prefab_layer_info_all_assigned`][attribute_controller.get_prefab_layer_info_all_assigned], [`…_with_dimensions`][attribute_controller.get_prefab_layer_info_with_dimensions], [`…_without_dimensions`][attribute_controller.get_prefab_layer_info_without_dimensions]: get the prefab layers assigned to an element, either all of them or only those output with or without dimensions.
- [`cadwork.prefab_layer_info`][cadwork.prefab_layer_info]: a prefab layer with `get_layer_number` and `get_side`.
- [`cadwork.prefab_layer_side`][cadwork.prefab_layer_side]: new enum: `referenceSide`, `oppositeSide`, `referenceElement`.
- [`attribute_controller.get_additional_data_keys`][attribute_controller.get_additional_data_keys]: gets the additional data keys set on an element through this API.
- [`bim_controller.load_ifc_export_settings`][bim_controller.load_ifc_export_settings]: loads an IFC export settings file into the active document.
- [`geometry_controller.get_element_collision_type`][geometry_controller.get_element_collision_type]: classifies how the geometry of two elements relates (touching, contained, interlocking, …).
- Multi layer sets: [`multi_layer_cover_controller.insert_layer`][multi_layer_cover_controller.insert_layer], [`remove_layer`][multi_layer_cover_controller.remove_layer], [`remove_all_layers`][multi_layer_cover_controller.remove_all_layers], [`unset_element_multi_layer_set`][multi_layer_cover_controller.unset_element_multi_layer_set].
- Navigation widget: [`utility_controller.set_navigation_widget_enabled`][utility_controller.set_navigation_widget_enabled], [`set_navigation_widget_axis`][utility_controller.set_navigation_widget_axis], [`set_navigation_widget_cube`][utility_controller.set_navigation_widget_cube], [`set_navigation_widget_north_arrow`][utility_controller.set_navigation_widget_north_arrow], [`set_navigation_widget_size`][utility_controller.set_navigation_widget_size].
- [`cadwork.navigation_widget_subwindow_position`][cadwork.navigation_widget_subwindow_position]: new enum: `none`, `top_left`, `top_right`, `bottom_left`, `bottom_right`.
- [`cadwork.event_type`][cadwork.event_type]: new enum: `on_activate`, `on_attribute`, `on_close`, `on_geometry`, `on_hide`, `on_show`.
<!-- /release:33.378.0 -->

<!-- release:33.343.2 -->
## 33.343.2 — 2026-08-24

[PR #411](https://github.com/cwapi3d/cwapi3dpython/pull/411) · `pip install cwapi3d==33.343.2`

Look up a connector axis by name.

### Added

- [`connector_axis_controller.get_connector_axis_guid_by_name`][connector_axis_controller.get_connector_axis_guid_by_name]: gets the GUID of a connector axis by its name.
<!-- /release:33.343.2 -->

<!-- release:33.333.2 -->
## 33.333.2 — 2026-08-14

[PR #408](https://github.com/cwapi3d/cwapi3dpython/pull/408) · `pip install cwapi3d==33.333.2`

Packaging-only release: no API changes.
<!-- /release:33.333.2 -->

<!-- release:33.333.1 -->
## 33.333.1 — 2026-08-14

[PR #407](https://github.com/cwapi3d/cwapi3dpython/pull/407) · `pip install cwapi3d==33.333.1`

Packaging-only release: no API changes.
<!-- /release:33.333.1 -->

<!-- release:33.333.0 -->
## 33.333.0 — 2026-08-10

[PR #404](https://github.com/cwapi3d/cwapi3dpython/pull/404) · `pip install cwapi3d==33.333.0`

Corrects how the end type is passed to `create_new_endtype`, and documents the end type controller.

### Added

- [`cadwork.end_type`][cadwork.end_type]: new enum for the kind of end type: `Tenon`, `JapaneseTenon`, `DovetailTenon`, `DovetailMortise`, `FrontSlot`, `Lengthening`, `GMIWithCounterpart`, `Unknown`.

### Fixed

- [`endtype_controller.create_new_endtype`][endtype_controller.create_new_endtype]: the second argument was documented as an existing end type ID (`endtype_id: EndtypeId`). It is the kind of end type to create: `end_type_id: int`, taking a [`cadwork.end_type`][cadwork.end_type] value.

    ```python
    import cadwork
    import endtype_controller as etc

    new_id = etc.create_new_endtype('Custom_Joint_80x40', cadwork.end_type.Tenon, 'Custom_Joints')
    ```

### Documentation

- `endtype_controller`: improved docstrings for 13 getters and setters of end type names and IDs.
<!-- /release:33.333.0 -->

<!-- release:33.330.0 -->
## 33.330.0 — 2026-08-10

[PR #403](https://github.com/cwapi3d/cwapi3dpython/pull/403) · `pip install cwapi3d==33.330.0`

Permanent hiding of elements, division zones, IFC 2x3/4 export, multi layer set standard elements and more.

### Added

- Permanent hiding: [`visualization_controller.hide_permanently`][visualization_controller.hide_permanently] takes elements out of the model's working set and keeps them there; [`show_permanently_hidden`][visualization_controller.show_permanently_hidden], [`is_permanently_hidden`][visualization_controller.is_permanently_hidden] and [`get_permanently_hidden_elements`][visualization_controller.get_permanently_hidden_elements] complete the set.
- [`visualization_controller.leave_working_plane`][visualization_controller.leave_working_plane]: leaves the 2D working plane and restores a 3D view.
- [`cadwork.working_plane_exit_view`][cadwork.working_plane_exit_view]: new enum: `keep_current_camera`, `previous_view`, `standard_axonometry`, `view_positive_x`, `view_positive_y`, `view_positive_z`.
- Division zones: [`geometry_controller.create_division_zone`][geometry_controller.create_division_zone], [`delete_division_zone`][geometry_controller.delete_division_zone], [`get_division_zone_points`][geometry_controller.get_division_zone_points].
- [`geometry_controller.stretch_facet`][geometry_controller.stretch_facet]: moves one facet of an element along its own plane normal, growing or shrinking the body at that face.
- [`bim_controller.export_ifc2x3`][bim_controller.export_ifc2x3], [`bim_controller.export_ifc4`][bim_controller.export_ifc4]: export an IFC 2x3 or IFC 4 file.
- [`file_controller.export_step_file_ex`][file_controller.export_step_file_ex]: exports a STEP file with the new algorithm.
- [`list_controller.export_container_list`][list_controller.export_container_list]: exports a container list.
- [`element_controller.apply_image_to_surface`][element_controller.apply_image_to_surface]: applies an image texture to a surface element.
- Multi layer sets: [`multi_layer_cover_controller.add_layer_by_standard_elements`][multi_layer_cover_controller.add_layer_by_standard_elements], [`get_layer_standard_beam_guid`][multi_layer_cover_controller.get_layer_standard_beam_guid] / [`set_…`][multi_layer_cover_controller.set_layer_standard_beam_guid], [`get_layer_standard_panel_guid`][multi_layer_cover_controller.get_layer_standard_panel_guid] / [`set_…`][multi_layer_cover_controller.set_layer_standard_panel_guid], [`get_layer_sub_type`][multi_layer_cover_controller.get_layer_sub_type] / [`set_…`][multi_layer_cover_controller.set_layer_sub_type], [`get_multi_layer_set_component_type`][multi_layer_cover_controller.get_multi_layer_set_component_type] / [`set_…`][multi_layer_cover_controller.set_multi_layer_set_component_type].
<!-- /release:33.330.0 -->
