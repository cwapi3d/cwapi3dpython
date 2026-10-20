<!-- release:{version} -->
## {version} — {date}

[PR #{pr}](https://github.com/cwapi3d/cwapi3dpython/pull/{pr}) · `pip install cwapi3d=={version}`

{One or two sentences for plugin authors: what this release lets them do, or "No API changes." for a packaging-only release.}

### ⚠ Breaking changes

- [`controller.function`][controller.function]: what changed and why.
  **Migration:** what to change in calling code.

    ```python
    # before
    controller.function(old_arg)
    # after
    controller.function(new_arg)
    ```

### Added

- [`controller.function`][controller.function]: {first sentence of its docstring, rephrased if needed}.
- [`cadwork.type_name`][cadwork.type_name]: new {class|enum} with `member_a`, `member_b`, ….

### Changed

- [`controller.function`][controller.function]: `old_signature` → `new_signature`.

### Deprecated

### Removed

### Fixed

- [`controller.function`][controller.function]: the stub declared `old_signature`; it now matches the binding: `new_signature`.

### Documentation

- `controller`: improved docstrings and examples for N functions.
<!-- /release:{version} -->
