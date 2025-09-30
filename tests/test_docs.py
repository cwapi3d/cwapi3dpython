import pytest
import pathlib
from __internal.cw_python_analyser import CwPythonAnalyser

EXAMPLES_DIR = pathlib.Path(__file__).parent.parent / "docs" / "examples"
STUBS_ROOT = pathlib.Path(__file__).parent.parent / "src"

def get_all_md_files():
    return list(EXAMPLES_DIR.glob("*.md"))

@pytest.mark.parametrize("md_file", get_all_md_files(), ids=lambda f: f.name)
def test_pyAPI_signatures_blocks(md_file):
    content = md_file.read_text(encoding="utf-8")
    raw_blocks = CwPythonAnalyser.extract_markdown_py_code_blocks(content)
    py_code_blocks = [block["code"] for block in raw_blocks if block["language"] == "python"]
    
    for py_block in py_code_blocks:
        extracted_symbols = CwPythonAnalyser.extract_py_dotted_symbols_from_code(py_block)
        matched_signatures, uncertain_signatures = CwPythonAnalyser.match_symbols_to_api_signatures(
            api_calls=extracted_symbols,
            stubs_root=STUBS_ROOT
        )
        # Only fail if possible signatures are present for any uncertain signature
        filtered = [
            (symbol, possible)
            for symbol, possible in uncertain_signatures
            if possible  # Only include if possible signatures are found
        ]
        if filtered:
            formatted = "\n".join(
                f"Symbol: {symbol}\nPossible signatures: {', '.join(possible)}"
                for symbol, possible in filtered
            )
            pytest.fail(f"In file {md_file.name}:\nUncertain signatures found:\n{formatted}")