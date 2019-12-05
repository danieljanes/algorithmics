from typing import Any
from typing import List
from typing import Tuple
from algorithmics.balanced_parentheses import balanced_parentheses


def main():
    alphabet = [("{", "}"), ("(",")"), ("[", "]")]
    
    # balanced
    b0 = "{}()[{}]"
    b1 = "[({})]"
    b2 = "({[]})"
    b3 = "{()[{({})[]()}]}([])"
    
    bs = [b0, b1, b2, b3]
    
    # unbalanced
    u0 = "[({)}]"
    u1 = "({[})"
    u2 = "()}[]"
    u3 = "{()[{({}{)[]()}]}([])"

    us = [u0, u1, u2, u3]

    print("\nA few balanced examples:")
    for b in bs:
        print("\tIs", b, "balanced?", balanced_parentheses(b, alphabet))

    print("\nA few unbalanced examples:")
    for u in us:
        print("\tIs", u, "balanced?", balanced_parentheses(u, alphabet))


if __name__ == "__main__":
    main()
