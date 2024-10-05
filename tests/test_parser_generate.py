from parser.src.antlr import parse_idl
from pathlib import Path

_this_dir = Path(__file__).parent
test_idl = _this_dir / "test_src/test.idl"


def test_parse():
    tree = parse_idl(test_idl)
    breakpoint()
    assert tree
