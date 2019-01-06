from algorithmics.search import binary_search
from algorithmics.search import linear_search


def test_linear_search_empty_list():
    # prepare
    l = []
    k = 0
    # execute
    r = linear_search(l, k)
    # assert
    assert r == False


def test_linear_search_single_positive_item():
    # prepare
    l = [0]
    k = 0
    # execute
    r = linear_search(l, k)
    # assert
    assert r == True


def test_linear_search_single_negative_item():
    # prepare
    l = [1]
    k = 0
    # execute
    r = linear_search(l, k)
    # assert
    assert r == False


def test_linear_search_multi_item_positive():
    # prepare
    l = [0, 2, 1, 0]
    k = 1
    # execute
    r = linear_search(l, k)
    # assert
    assert r == True


def test_linear_search_multi_item_last_positive():
    # prepare
    l = [0, 2, 0, 1]
    k = 1
    # execute
    r = linear_search(l, k)
    # assert
    assert r == True


def test_linear_search_multi_item_negative():
    # prepare
    l = [0, 2, 3, 0]
    k = 1
    # execute
    r = linear_search(l, k)
    # assert
    assert r == False


def test_binary_search_negative():
    # prepare
    l = [0, 2, 3]
    k = 1
    # execute
    r = binary_search(l, k)
    # assert
    assert r == False


def test_binary_search_positive():
    # prepare
    l = [0, 2, 3]
    k = 3
    # execute
    r = binary_search(l, k)
    # assert
    assert r == False
