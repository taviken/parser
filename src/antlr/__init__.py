from pathlib import Path
import subprocess


_this_dir = Path(__file__).parent
_default_grammar = _this_dir.parent / "grammars/IDL.g4"


def generate_parser(grammar_path: Path = _default_grammar):

    cmds = f"anltr4 -Dlanguage=Python3 {grammar_path} -o {_this_dir}".split()

    p = subprocess.Popen(
        cmds, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, err = p.communicate()
    return output, err


from antlr4 import *
from .IDLLexer import IDLLexer
from .IDLParser import IDLParser

from IDLVisitor import IDLVisitor
from IDLListener import IDLListener


def parse_idl(path: Path):
    with open(path, "r") as fp:
        lexer = IDLLexer(fp)
        stream = CommonTokenStream(lexer)
        parser = IDLParser(stream)
        tree = parser.specification()
    return tree
