# Copyright 2020 Daniel J. Beutel. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


import unittest
from typing import Any

from algorithmics.hash_map import HashMap, SimpleHashMap

pairs = [("k0", "v0"), ("k1", 1), (2, "v2"), (3, 3)]


class Test(unittest.TestCase):
    def test_HashMap_insert_one(self):
        # prepare
        hm = HashMap()
        # execute
        hm["k"] = "v"
        # assert
        assert "v" == hm["k"]
        assert fail_if_present(hm, "l")

    def test_HashMap_contains(self):
        # prepare
        hm = HashMap()
        # execute
        hm["k"] = "v"
        # assert
        assert "k" in hm
        assert "v" not in hm

    def test_HashMap_delete_one(self):
        # prepare
        hm = HashMap()
        hm.insert_tuples([("k0", "v0"), ("k1", "v1")])
        assert "v0" == hm["k0"]
        assert "v1" == hm["k1"]
        # execute
        del hm["k0"]
        # assert
        assert fail_if_present(hm, "k0")
        assert "v1" == hm["k1"]

    def test_HashMap_insert_many(self):
        # prepare & execute
        hm = HashMap()
        hm.insert_tuples(pairs)
        # assert
        assert "v0" == hm["k0"]
        assert 1 == hm["k1"]
        assert "v2" == hm[2]
        assert 3 == hm[3]

    def test_HashMap_delete_all(self):
        # prepare
        hm = HashMap()
        hm.insert_tuples(pairs)
        # execute
        for k, _ in pairs:
            del hm[k]
        # assert
        for k, _ in pairs:
            assert fail_if_present(hm, k)

    def test_SimpleHashMap_insert_one(self):
        # prepare
        hm = SimpleHashMap()
        # execute
        hm["k"] = "v"
        # assert
        assert "v" == hm["k"]
        assert fail_if_present(hm, "l")

    def test_SimpleHashMap_delete_one(self):
        # prepare
        hm = SimpleHashMap()
        hm.insert_tuples([("k0", "v0"), ("k1", "v1")])
        assert "v0" == hm["k0"]
        assert "v1" == hm["k1"]
        # execute
        del hm["k0"]
        # assert
        assert fail_if_present(hm, "k0")
        assert "v1" == hm["k1"]

    def test_SimpleHashMap_insert_many(self):
        # prepare & execute
        hm = SimpleHashMap()
        hm.insert_tuples(pairs)
        # assert
        assert "v0" == hm["k0"]
        assert 1 == hm["k1"]
        assert "v2" == hm[2]
        assert 3 == hm[3]

    def test_SimpleHashMap_delete_all(self):
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


if __name__ == "__main__":
    unittest.main()
