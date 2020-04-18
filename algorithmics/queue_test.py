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

from algorithmics.queue import Queue, StackBasedQueue


class Test(unittest.TestCase):
    def test_Queue_empty(self):
        q = Queue()
        try:
            s.peek()
            fail()
        except:
            pass
        try:
            s.dequeue()
            fail()
        except:
            pass
        assert q.is_empty()
        assert len(q) == 0

    def test_Queue_single_enqueue_peek_dequeue(self):
        q = Queue()
        q.enqueue(0)
        assert not q.is_empty()
        assert len(q) == 1
        v = q.peek()
        assert v == 0
        v = q.dequeue()
        assert v == 0
        assert q.is_empty()
        assert len(q) == 0

    def test_Queue_multiple(self):
        q = Queue()
        vs = "Hello, world!"
        for v in vs:
            q.enqueue(v)
            assert vs[0] == q.peek()
        xs = ""
        while not q.is_empty():
            xs += q.dequeue()
        assert xs == vs

    def test_StackBasedQueue_empty(self):
        q = StackBasedQueue()
        try:
            s.peek()
            fail()
        except:
            pass
        try:
            s.dequeue()
            fail()
        except:
            pass
        assert q.is_empty()
        assert len(q) == 0

    def test_StackBasedQueue_single_enqueue_peek_dequeue(self):
        q = StackBasedQueue()
        q.enqueue(0)
        assert not q.is_empty()
        assert len(q) == 1
        v = q.peek()
        assert v == 0
        v = q.dequeue()
        assert v == 0
        assert q.is_empty()
        assert len(q) == 0

    def test_StackBasedQueue_multiple(self):
        q = StackBasedQueue()
        vs = "Hello, world!"
        for v in vs:
            q.enqueue(v)
            assert vs[0] == q.peek()
        xs = ""
        while not q.is_empty():
            xs += q.dequeue()
        assert xs == vs


if __name__ == "__main__":
    unittest.main()
