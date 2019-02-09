from typing import Any
from typing import List
from typing import Tuple
from algorithmics.stack import Stack


def balanced_parentheses(s: str, a: List[Tuple[str, str]]) -> bool:
    opening_chars = [x[0] for x in a]
    closing_chars = [x[1] for x in a]
    
    stack = Stack()

    for c in s:
        if c in opening_chars:
            stack.push(c)
        else:
            if stack.is_empty():
                return False
            c_popped = stack.pop()
            for p_open, p_close in a:
                if p_open == c_popped:
                    if p_close is not c:
                        return False
    return stack.is_empty()
