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

from algorithmics.search import binary_search, linear_search


class Test(unittest.TestCase):
    def test_linear_search_empty_list(self):
        # prepare
        l = []
        k = 0
        # execute
        r = linear_search(l, k)
        # assert
        assert r == False

    def test_linear_search_single_positive_item(self):
        # prepare
        l = [0]
        k = 0
        # execute
        r = linear_search(l, k)
        # assert
        assert r == True

    def test_linear_search_single_negative_item(self):
        # prepare
        l = [1]
        k = 0
        # execute
        r = linear_search(l, k)
        # assert
        assert r == False

    def test_linear_search_multi_item_positive(self):
        # prepare
        l = [0, 2, 1, 0]
        k = 1
        # execute
        r = linear_search(l, k)
        # assert
        assert r == True

    def test_linear_search_multi_item_last_positive(self):
        # prepare
        l = [0, 2, 0, 1]
        k = 1
        # execute
        r = linear_search(l, k)
        # assert
        assert r == True

    def test_linear_search_multi_item_negative(self):
        # prepare
        l = [0, 2, 3, 0]
        k = 1
        # execute
        r = linear_search(l, k)
        # assert
        assert r == False

    def test_binary_search_negative(self):
        # prepare
        l = [0, 2, 3]
        k = 1
        # execute
        r = binary_search(l, k)
        # assert
        assert r == False

    def test_binary_search_positive(self):
        # prepare
        l = [0, 2, 3]
        k = 3
        # execute
        r = binary_search(l, k)
        # assert
        assert r == False


if __name__ == "__main__":
    unittest.main()
