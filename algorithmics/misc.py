from algorithmics.hash_map import HashMap


def find_missing_int_using_hash_map(complete, incomplete):
    """
    Problem: There are distinct integers in list `complete`. The same integers are in list `incomplete`, except for one.
    
    Task: Find the one integer which is missing from the incomplete list.

    Algorithm:
    - Insert all elements of the shorter list into a hash map
    - Then test each element of the full list for presence

    Complexity: O(n) time, O(n) space
    """
    hm = HashMap()  # Or use dict()
    for i in incomplete:
        hm[i] = 1
    for j in complete:
        if j not in hm:
            return j


def find_missing_int_using_sum(complete, incomplete):
    """
    Problem: There are distinct integers in list `complete`. The same integers are in list `incomplete`, except for one.
    
    Task: Find the one integer which is missing from the incomplete list.

    Complexity: O(n) time, O(1) space
    """
    s = 0
    for a, b in zip(complete[:-1], incomplete):
        s += a
        s -= b
    return s + complete[len(complete) - 1]
