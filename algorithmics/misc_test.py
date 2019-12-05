from algorithmics.misc import find_missing_int_using_hash_map
from algorithmics.misc import find_missing_int_using_sum


complete = [4, 8, 12, 9, 3]
incomplete = [4, 8, 9, 3]


def test_find_missing_int_using_hash_map():
    assert 12 == find_missing_int_using_hash_map(complete, incomplete)


def test_find_missing_int_using_sum():
    assert 12 == find_missing_int_using_sum(complete, incomplete)
