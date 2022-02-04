"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("test").glob("**/*.py")):
    print(path)
    # module_path = path.relative_to("test").with_suffix("")
    # doc_path = path.relative_to("test", "test").with_suffix(".md")
    # full_doc_path = Path("reference", doc_path)
    mod_path = Path("element_controller\\__init__.pyi")
    parts = list(mod_path.parts)
    parts[-1] = f"{parts[-1]}"
    with mkdocs_gen_files.open("test\\test.md", "w") as fd:
        ident = ".".join(mod_path.parts)
        print("::: " + ident, file=fd)
