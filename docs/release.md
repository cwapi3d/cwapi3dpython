---
hide:
  - navigation
  - toc
---

# Release Notes

| Date       | Action                      | Changes                                                          | controller    | cadwork 3D build | cwapi3d  |
| :--------- | :-------------------------- | :--------------------------------------------------------------- | :------------ | :--------------- | :------- |
| 06.09.2022 | :material-check: Add        | get_rgb_from_cadwork_color_id                                    | visualization | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | set_color (update / correction signature)                        | visualization | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | create_rectangular_beam_vectors (update signature)               | element       | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | export_production_list (add .csv format extension)               | list          | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | export_part_list (add .csv format extension)                     | list          | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | export_production_list_with_settings (add .csv format extension) | list          | 29.309           | 1.3.14   |
| 06.09.2022 | :material-check-all: Update | export_part_list_with_settings (add .csv format extension)       | list          | 29.309           | 1.3.14   |
| 13.10.2022 | :material-check: Add        | get_user_points                                                  | utility       | 29.341           | 1.3.14   |
| 13.10.2022 | :material-check: Add        | get_user_points_with_count                                       | utility       | 29.341           | 1.3.14   |
| 20.10.2022 | :material-check: Add        | get_scene_list                                                   | scene         | 29.341           | 1.3.14   |
| 20.10.2022 | :material-check: Add        | is_circular_mep                                                  | cadwork       | 29.344           | 1.3.14   |
| 20.10.2022 | :material-check: Add        | is_rectangular_mep                                               | cadwork       | 29.344           | 1.3.14   |
| 10.05.2023 | :material-check: Add        | get_machine_calculation_state                                    | machine       | 30.218           | 2.0.0    |
| 10.05.2023 | :material-check: Add        | get_machine_calculation_set_machine_type                         | machine       | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | execute_shortcut                                                 | utility       | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | set_grade                                                        | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | get_grade                                                        | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | set_quality                                                      | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | get_quality                                                      | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | set_composition                                                  | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | get_composition                                                  | material      | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | set_texture_rotated                                              | visualization | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | is_texture_rotated                                               | visualization | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | get_name_list_items                                              | attribute     | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | add_item_to_name_list                                            | attribute     | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | get_user_path_from_dialog_in_path                                | utility       | 30.218           | 2.0.0    |
| 16.05.2023 | :material-check: Add        | import_element_light                                             | file          | 30.218           | 2.0.0    |
| 01.06.2023 | :material-check: Add        | enumeration types                                                | cadwork       | 30.240           | 2.0.9    |
| 12.06.2023 | :material-check: Add        | get_joined_elements                                              | element       | 30.240           | 2.0.9    |
| 12.06.2023 | :material-check: Add        | start_element_module_calculation_silently                        | element       | 30.240           | 2.0.9    |
| 12.06.2023 | :material-check: Add        | add dimension controller                                         | dimension     | 30.240           | 2.0.9    |
| 12.06.2023 | :material-check: Add        | export_ifc2x3_silently                                           | bim           | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | export_ifc4_silently                                             | bim           | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | add extended_settings                                            | cadwork       | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | convert_bolt_to_standardconnector                                | element       | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | create_division_zone                                             | geometry      | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | delete_division_zone                                             | geometry      | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | get_division_zone_points                                         | geometry      | 30.317           | 30.317.0 |
| 12.06.2023 | :material-check: Add        | get_3d_hwnd                                                      | utility       | 30.317           | 30.317.0 |
| 05.10.2023 | :material-check: Add        | export_ifc2x3_silently                                           | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | export_ifc4_silently                                             | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | get_element_id_from_base64_ifc_guid                              | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | get_ifc_base64_guid                                              | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | export_ifc2x3_silently_with_options                              | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | export_ifc4_silently_with_options                                | bim           | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | ifc_options                                                      | cadwork       | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | rhino_options                                                    | cadwork       | 30.334           | 30.334.0 |
| 05.10.2023 | :material-check: Add        | export_rhino_file_with_options                                   | file          | 30.334           | 30.334.0 |
