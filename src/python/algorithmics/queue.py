from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[Node] = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value: Any) -> None:
        node = Node(value)
        if self.tail is not None:
            self.tail.next = node
        if self.head is None:
            self.head = node
        self.tail = node
        self.length += 1

    def dequeue(self) -> Any:
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return value

    def peek(self) -> Any:
        return self.head.value
    
    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.length
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "[ <empty> ]\n"
        else:
            rep = "["
            nxt = self.head
            while nxt is not None:
                rep += " " + str(nxt.value) + " "
                nxt = nxt.next
            rep += "]\n"
            return rep
