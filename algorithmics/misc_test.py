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

from algorithmics.misc import (
    find_missing_int_using_hash_map,
    find_missing_int_using_sum,
)

complete = [4, 8, 12, 9, 3]
incomplete = [4, 8, 9, 3]


class Test(unittest.TestCase):
    def test_find_missing_int_using_hash_map(self):
        assert 12 == find_missing_int_using_hash_map(complete, incomplete)

    def test_find_missing_int_using_sum(self):
        assert 12 == find_missing_int_using_sum(complete, incomplete)


if __name__ == "__main__":
    unittest.main()
