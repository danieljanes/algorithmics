from typing import Any
from typing import Optional


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[Node] = None


class Stack(object):
    def __init__(self) -> None:
        self.top: Any = None

    def peek(self) -> Any:
        return self.top.value

    def pop(self) -> Any:
        value = self.top.value
        self.top = self.top.next
        return value
    
    def push(self, value: Any) -> None:
        node = Node(value)
        node.next = self.top
        self.top = node

    def __len__(self) -> int:
        l = 0
        node = self.top
        while node is not None:
            l += 1
            node = node.next
        return l

    def __repr__(self) -> str:
        if self.top is None:
            return "-- [ empty stack ] --"
        else:
            def pad_or_shorten(s: str) -> str:
                return '{s:{c}^{n}}'.format(s=s[:6],n=5,c=' ')
            rep = "-- [" + pad_or_shorten(str(self.top.value)) + "] --"
            node = self.top.next
            while node is not None:
                rep += "\n   [" + pad_or_shorten(str(node.value)) + "]   "
                node = node.next
            return rep + "\n"
