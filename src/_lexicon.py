from dataclasses import dataclass
from typing import List, Dict, Optional
from ._constants import _operators


@dataclass
class Lexicon:
    keywords: Optional[List[str]] = None
    operators: Optional[Dict[str, str]] = None
    comments: Optional[Dict[str, str]] = None


default_lexicon = Lexicon(
    keywords=[],
    operators=_operators,
    comments={
        "LINE_COMMENT": r"//.*$",
        "PYTHON_COMMENT": r"#.*$",
    },
)
