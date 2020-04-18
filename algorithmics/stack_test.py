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

from algorithmics.stack import Stack


class Test(unittest.TestCase):
    def test_empty(self):
        s = Stack()
        try:
            s.peek()
            fail()
        except:
            pass
        try:
            s.pop()
            fail()
        except:
            pass
        assert s.is_empty()
        assert len(s) == 0

    def test_single_push_peek_pop(self):
        s = Stack()
        s.push(0)
        assert not s.is_empty()
        assert len(s) == 1
        v = s.peek()
        assert v == 0
        v = s.pop()
        assert v == 0
        assert s.is_empty()
        assert len(s) == 0

    def test_multiple(self):
        s = Stack()
        vs = "Hello, world!"
        for v in vs:
            s.push(v)
        assert v == s.peek()
        xs = ""
        while not s.is_empty():
            xs = s.pop() + xs
        assert xs == vs


if __name__ == "__main__":
    unittest.main()
