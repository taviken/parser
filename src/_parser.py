from dataclasses import dataclass
from typing import List, Any, Union
from functools import wraps
from tokenize import ENDMARKER, NAME, NEWLINE, STRING





@dataclass
class Node:
    type: str
    children: Union[Any, "Node"]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}:{self.type}"


@dataclass
class Rule:
    name: str
    alts: List[str]


class Parser:

    def __init__(self, lexer):
        self.tokenset = lexer.tokenset
        self.memos = {}

    def mark(self):
        return self.tokenset.mark()

    def reset(self, pos):
        self.tokenset.reset(pos)

    def expect(self, arg):
        token = self.tokenset.peek_token()
        if token.kind == arg or token.text == arg:
            return self.tokenset.get_token()
        return None


class GrammarParser(Parser):

    def grammar(self):
        pos = self.mark()
        rule = self.rule()
        if rule:
            rules = [rule]
            rule = self.rule()
            while rule:
                rules.append(rule)
                rule = self.rule()
            if self.expect(ENDMARKER):
                return rules
        self.reset(pos)
        return None

    def rule(self):
        pos = self.mark()
        name = self.expect(NAME)
        if name:
            if self.expect(":"):
                alt = self.alternative()
                if alt:
                    alts = [alt]
                    apos = self.mark()
                    while self.expect("|") and alt:
                        alts.append(alt)
                        apos = self.mark()
                        alt = self.alternative()
                    self.reset(apos)
                    if self.expect(NEWLINE):
                        return Rule(name.text, alts)
        self.reset(pos)
        return None

    def alternative(self):
        items = []
        item = self.item()
        while item:
            items.append(item)
            item = self.item()
        return items

    def item(self):
        name = self.expect(NAME)
        if name:
            return name.text
        string = self.expect(STRING)
        if string:
            return string.text
        return None
