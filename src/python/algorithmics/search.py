from typing import Any, List


def linear_search(list: List[Any], key: Any) -> bool:
    i: int = 0
    while i < len(list):
        if list[i] == key:
            return True
        i += 1
    return False


def binary_search(list: List[Any], key: Any) -> bool:
    l: int = 0
    r: int = len(list) - 1
    while l < r:
        i: int = l + (r-l) // 2
        item = list[i]
        if item == key:
            return True
        elif item > key:
            r = i - 1
        else:
            l = i + 1
    return False
