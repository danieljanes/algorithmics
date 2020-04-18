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
from typing import Any, List, Tuple

from algorithmics.balanced_parentheses import balanced_parentheses

alphabet = [("{", "}"), ("(", ")"), ("[", "]")]


class Test(unittest.TestCase):
    def test_empty(self):
        assert balanced_parentheses("", alphabet)

    def test_single(self):
        for p in alphabet:
            assert not balanced_parentheses(p[0], alphabet)
            assert not balanced_parentheses(p[1], alphabet)

    def test_balanced(self):
        b0 = "{}()[{}]"
        b1 = "[({})]"
        b2 = "({[]})"
        b3 = "{()[{({})[]()}]}([])"

        bs = [b0, b1, b2, b3]

        for b in bs:
            assert balanced_parentheses(b, alphabet)

    def test_unbalanced(self):
        u0 = "[({)}]"
        u1 = "({[})"
        u2 = "()}[]"
        u3 = "{()[{({}{)[]()}]}([])"

        us = [u0, u1, u2, u3]

        for u in us:
            assert not balanced_parentheses(u, alphabet)


if __name__ == "__main__":
    unittest.main()
