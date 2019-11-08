from typing import Optional, Dict

def first_recurring_char(input: str) -> Optional[str]:
    seen: Dict = {}
    for char in input:
        if char in seen:
            return char
        seen[char] = 1
    return None
