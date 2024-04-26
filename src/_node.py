from collections import deque
from dataclasses import dataclass
from typing import TypeVar, Any, Optional, Deque

N = TypeVar("N", bound="Node")


def _find_value_bfs(node: N, value: Any) -> Optional[N]:
    if node.children:
        children = node.children.copy()
    else:
        return

    while children:
        child = children.popleft()
        if child.value == value:
            return child
        if child.children:
            _find_value_bfs(child, value)


@dataclass
class Node:
    value: Any
    children: Deque[N] = None

    def __post_init__(self) -> None:
        self.children = deque([]) if self.children is None else self.children

    def add_left(self, child: N) -> None:
        self.children.appendleft(child)

    def add_right(self, child: N) -> None:
        self.children.append(child)

    def bfs(self, value: Any) -> Optional[N]:
        return _find_value_bfs(self, value)
