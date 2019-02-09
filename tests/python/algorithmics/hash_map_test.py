from typing import Any
from algorithmics.hash_map import HashMap
from algorithmics.hash_map import SimpleHashMap


pairs = [('k0', 'v0'), ('k1', 1), (2, 'v2'), (3, 3)]


def test_HashMap_insert_one():
    # prepare
    hm = HashMap()
    # execute
    hm['k'] = 'v'
    # assert
    assert 'v' == hm['k']
    assert fail_if_present(hm, 'l')


def test_HashMap_contains():
    # prepare
    hm = HashMap()
    # execute
    hm['k'] = 'v'
    # assert
    assert 'k' in hm
    assert 'v' not in hm


def test_HashMap_delete_one():
    # prepare
    hm = HashMap()
    hm.insert_tuples([('k0', 'v0'), ('k1', 'v1')])
    assert 'v0' == hm['k0']
    assert 'v1' == hm['k1']
    # execute
    del hm['k0']
    # assert
    assert fail_if_present(hm, 'k0')
    assert 'v1' == hm['k1']


def test_HashMap_insert_many():
    # prepare & execute
    hm = HashMap()
    hm.insert_tuples(pairs)
    # assert
    assert 'v0' == hm['k0']
    assert 1 == hm['k1']
    assert 'v2' == hm[2]
    assert 3 == hm[3]


def test_HashMap_delete_all():
    # prepare
    hm = HashMap()
    hm.insert_tuples(pairs)
    # execute
    for k, _ in pairs:
        del hm[k]
    # assert
    for k, _ in pairs:
        assert fail_if_present(hm, k)


def test_SimpleHashMap_insert_one():
    # prepare
    hm = SimpleHashMap()
    # execute
    hm['k'] = 'v'
    # assert
    assert 'v' == hm['k']
    assert fail_if_present(hm, 'l')


def test_SimpleHashMap_delete_one():
    # prepare
    hm = SimpleHashMap()
    hm.insert_tuples([('k0', 'v0'), ('k1', 'v1')])
    assert 'v0' == hm['k0']
    assert 'v1' == hm['k1']
    # execute
    del hm['k0']
    # assert
    assert fail_if_present(hm, 'k0')
    assert 'v1' == hm['k1']


def test_SimpleHashMap_insert_many():
    # prepare & execute
    hm = SimpleHashMap()
    hm.insert_tuples(pairs)
    # assert
    assert 'v0' == hm['k0']
    assert 1 == hm['k1']
    assert 'v2' == hm[2]
    assert 3 == hm[3]


def test_SimpleHashMap_delete_all():
    # prepare
    hm = SimpleHashMap()
    hm.insert_tuples(pairs)
    # execute
    for k, _ in pairs:
        del hm[k]
    # assert
    for k, _ in pairs:
        assert fail_if_present(hm, k)


def fail_if_present(hm: SimpleHashMap, key: Any):
    try:
        hm[key]
        return False
    except:
        return True
