def linear_search(list, key):
    i = 0
    while i < len(list):
        if list[i] == key:
            return True
        i += 1
    return False


def binary_search(list, key):
    l = 0
    r = len(list) - 1
    while l < r:
        i = l + int((r-l) / 2)
        item = list[i]
        if item == key:
            return True
        elif item > key:
            r = i - 1
        else:
            l = i + 1
    return False
