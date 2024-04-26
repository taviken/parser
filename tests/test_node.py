from src import Node
from collections import deque
import pytest


def test_node():
    node_a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    node_a.add_left(c)
    node_a.add_right(b)
    b.add_left(d)
    b.add_right(e)
    expected = Node(value=1, children=deque([Node(value=3, children=deque([])), Node(value=2, children=deque([Node(value=4, children=deque([])), Node(value=5, children=deque([]))]))]))
    assert node_a == expected

def test_node_bfs():
    node_a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    node_a.add_left(c)
    node_a.add_right(b)
    b.add_left(d)
    b.add_right(e)

    actual = node_a.bfs(3)
    expected = c
    assert actual == expected
    actual = node_a.bfs("won't find me")
    assert actual is None
