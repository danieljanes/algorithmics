from typing import Any
from typing import List
from typing import Tuple
from algorithmics.balanced_parentheses import balanced_parentheses


alphabet = [("{", "}"), ("(",")"), ("[", "]")]


def test_empty():
    assert balanced_parentheses("", alphabet)


def test_single():
    for p in alphabet:
        assert not balanced_parentheses(p[0], alphabet)
        assert not balanced_parentheses(p[1], alphabet)


def test_balanced():
    b0 = "{}()[{}]"
    b1 = "[({})]"
    b2 = "({[]})"
    b3 = "{()[{({})[]()}]}([])"

    bs = [b0, b1, b2, b3]

    for b in bs:
        assert balanced_parentheses(b, alphabet)
    

def test_unbalanced():
    u0 = "[({)}]"
    u1 = "({[})"
    u2 = "()}[]"
    u3 = "{()[{({}{)[]()}]}([])"

    us = [u0, u1, u2, u3]

    for u in us:
        assert not balanced_parentheses(u, alphabet)
